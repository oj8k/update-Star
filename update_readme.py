# ===========================================
#  update-Star - GitHub Star 项目列表生成器
# ===========================================
#
#  【环境变量配置】
#
#  REQUIRED:
#    GH_TOKEN        - GitHub Personal Access Token
#    GH_USERNAME     - GitHub 用户名（默认: oj8k）
#
#  OPTIONAL:
#    OPENAI_API_KEY  - ChatGPT API Key（留空则跳过翻译）
#    CHATGPT_API_URL - ChatGPT API 地址（默认: https://api.openai.com/v1/chat/completions）
#    CHATGPT_MODEL   - ChatGPT 模型（默认: gpt-3.5-turbo）
#    TRANSLATE_DELAY - 翻译间隔秒数（默认: 0.5，避免 API 限流）
#    TRANSLATION_CACHE - 翻译缓存文件路径（默认: translations.json）
#
#  【功能说明】
#    - 自动获取 GitHub Star 列表并生成 README.md 表格
#    - 纯英文描述自动翻译为中文；已有中文的跳过翻译
#    - 翻译缓存：已翻译过的描述不再重复调用 API，节省配额并避免限流
#    - 429 限流时自动指数退避重试
#    - 翻译失败时只显示原文，不显示错误信息
#    - 自动去重（按项目 URL）
#
#  【使用示例】
#    export GH_TOKEN="ghp_xxxxxxxxxxxx"
#    export GH_USERNAME="oj8k"
#    export OPENAI_API_KEY="sk-xxxxxxxxxxxx"
#    python update_readme.py
#
# ===========================================

import json
import os
import time

import requests
from github import Github, Auth


# ─── 翻译缓存 ─────────────────────────────────
CACHE_FILE = os.getenv("TRANSLATION_CACHE", "translations.json")


def load_cache():
    """加载翻译缓存，返回 {原文: 翻译} 字典"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"  ⚠️  加载缓存失败: {e}")
    return {}


def save_cache(cache):
    """保存翻译缓存到文件"""
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"  ⚠️  保存缓存失败: {e}")


# ─── ChatGPT 翻译 ─────────────────────────────
def chatgpt_translate(text, cache):
    """调用 ChatGPT API 翻译，失败返回空字符串；缓存命中则直接返回"""
    # 1. 先查缓存
    if text in cache:
        print(f"      💾 使用缓存翻译")
        return cache[text]

    api_url = os.getenv("CHATGPT_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("CHATGPT_MODEL", "gpt-3.5-turbo")
    api_key = os.getenv("OPENAI_API_KEY", "")

    if not api_key:
        return ""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个专业的中英翻译助手。"},
            {"role": "user", "content": f"请将以下英文翻译成中文：\n{text[:500]}"},
        ],
        "temperature": 0.3,
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            resp = requests.post(api_url, headers=headers, json=payload, timeout=30)
            if resp.status_code == 429:
                # 429 限流：指数退避后重试
                wait = 2 ** attempt + 1
                print(f"      ⚠️  API 限流（429），等待 {wait} 秒后重试... ({attempt + 1}/{max_retries})")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            translated = resp.json()["choices"][0]["message"]["content"].strip()
            cache[text] = translated  # 写入缓存
            return translated
        except Exception as e:
            print(f"      ⚠️  翻译失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                return ""
    return ""


# ─── 中文检测 ─────────────────────────────────
def has_chinese(text):
    """检测是否包含中文字符"""
    return any("\u4e00" <= c <= "\u9fff" for c in text)


def needs_translation(text):
    """只有不含中文的描述才需要翻译"""
    return not has_chinese(text)


# ─── 项目名称 ─────────────────────────────────
def fmt_name(name, max_len=18):
    """
    项目名称格式化（自动换行，优先在单词边界断行）：
    - 每行不超过 max_len 字符
    - 优先在空格处断行，保持单词完整
    - 单个超长单词（无空格）强制按字符数断行
    - 最多 3 行，超出则第 3 行截断加 ...
    """
    name = name.strip()
    if len(name) <= max_len:
        return name

    lines = []
    # 先按单词处理
    words = name.split()
    current = ""

    for w in words:
        # 当前行还能放下这个单词
        if len(current) + len(w) + (1 if current else 0) <= max_len:
            current += (" " if current else "") + w
        else:
            # 放不下：保存当前行，新单词另起一行
            if current:
                lines.append(current)
                current = ""
            # 如果这个单词本身就超长，强制按字符断行
            if len(w) > max_len:
                while len(w) > max_len and len(lines) < 3:
                    lines.append(w[:max_len])
                    w = w[max_len:]
                if w and len(lines) < 3:
                    current = w
                elif w and len(lines) >= 3:
                    # 已达 3 行，截断
                    lines[-1] = lines[-1][:max_len - 3] + "..."
                    return "<br>".join(lines[:3])
            else:
                current = w

    if current:
        if len(lines) < 3:
            lines.append(current)
        else:
            lines[-1] = lines[-1][:max_len - 3] + "..."

    return "<br>".join(lines[:3])


# ─── 项目简介 ─────────────────────────────────
def clean_desc(desc, max_len=120):
    """
    清理原始描述（不添加任何 <br>）：
    - 去掉已有的 <br> 标签和换行符
    - 压缩多余空格
    - 超过 max_len 在空格处截断加 ...
    - 让浏览器自动换行，不强制断行
    """
    desc = (
        desc.replace("<br>", " ")
        .replace("<br/>", " ")
        .replace("\n", " ")
        .replace("|", "｜")
        .strip()
    )
    while "  " in desc:
        desc = desc.replace("  ", " ")

    if len(desc) > max_len:
        cut = desc[:max_len].rfind(" ")
        if cut > max_len * 0.6:
            desc = desc[:cut] + "..."
        else:
            desc = desc[:max_len] + "..."
    return desc


# ─── Star 数 ──────────────────────────────────
def fmt_stars(count):
    """
    Star 数格式化：
    - 用不间断空格(U+00A0)连接 ⭐ 和数字，防止被拆成两行
    - >= 10000 → X.XW, >= 1000 → X.XK, 其他 → 原始数字
    """
    nbsp = "\u00a0"  # 不间断空格，兼容 Markdown 链接文本
    if count >= 10000:
        return f"⭐{nbsp}{count / 10000:.1f}W"
    if count >= 1000:
        return f"⭐{nbsp}{count / 1000:.1f}K"
    return f"⭐{nbsp}{count}"


# ─── 主流程 ───────────────────────────────────
def main():
    token = os.getenv("GH_TOKEN")
    username = os.getenv("GH_USERNAME", "oj8k")
    translate_delay = float(os.getenv("TRANSLATE_DELAY", "0.5"))

    if not token:
        raise ValueError("❌ 未设置 GH_TOKEN 环境变量")

    auth = Auth.Token(token)
    g = Github(auth=auth)
    user = g.get_user(username)
    starred = list(user.get_starred())

    cache = load_cache()
    seen = set()

    lines = [
        "# 🌟 我的 GitHub Star 项目\n",
        "<a id='top'></a>\n",
        "本仓库通过 GitHub Actions 自动同步我的 GitHub Star 项目列表，并生成 README 表格。\n",
        "> 如需 Fork/复用本项目，请在仓库的 **Settings → Secrets and variables → Actions** 中配置以下变量。\n",
        "## 🔧 环境变量配置\n",
        "| 变量名 | 必填 | 说明 |",
        "|--------|------|------|",
        "| `GH_TOKEN` | ✅ | GitHub Personal Access Token（需勾选 `repo` 权限） |",
        "| `GH_USERNAME` | ✅ | GitHub 用户名，例如 `oj8k` |",
        "| `OPENAI_API_KEY` | ❌ | ChatGPT API Key，用于翻译纯英文项目描述 |",
        "| `CHATGPT_API_URL` | ❌ | ChatGPT API 地址，默认 `https://api.openai.com/v1/chat/completions` |",
        "| `CHATGPT_MODEL` | ❌ | ChatGPT 模型，默认 `gpt-3.5-turbo` |",
        "| `TRANSLATE_DELAY` | ❌ | 翻译间隔秒数，默认 `0.5` |",
        "| `TRANSLATION_CACHE` | ❌ | 翻译缓存文件路径，默认 `translations.json` |\n",
        "## ⚡ 触发方式\n",
        "- 手动触发：仓库 Actions → 自动更新星标项目 → Run workflow\n",
        "- 自动触发：每天 UTC 00:00（北京时间 08:00）运行一次\n",
        "---\n",
        "| 项目名称 | 项目简介 | 项目链接 |",
        "|----------|-----------|:-----------:|",
    ]

    print(f"📊 共获取 {len(starred)} 个 Star 项目，开始处理...\n")

    for repo in starred:
        if repo.html_url in seen:
            continue
        seen.add(repo.html_url)

        name = fmt_name(repo.name)
        desc_raw = clean_desc(repo.description or "暂无描述")

        if needs_translation(desc_raw):
            print(f"  🔄 翻译: {repo.name}")
            desc_cn = chatgpt_translate(desc_raw, cache)
            if desc_cn:
                desc_final = f"{desc_raw}<br>{desc_cn}"
            else:
                desc_final = desc_raw
            time.sleep(translate_delay)  # 控制 API 请求频率
        else:
            print(f"  ✅ 跳过翻译: {repo.name}")
            desc_final = desc_raw

        star_txt = fmt_stars(repo.stargazers_count)
        star_link = f"[{star_txt}]({repo.html_url})"

        lines.append(f"| {name} | {desc_final} | {star_link} |")

    # 底部添加回到顶部链接（右下角）
    lines.append("\n---")
    lines.append("<div align='right'>⬆ <a href='#top'>回到顶部</a></div>")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    save_cache(cache)

    print(f"\n✅ README.md 生成完成！共 {len(seen)} 个项目")
    print(f"💾 翻译缓存已保存到 {CACHE_FILE}")


if __name__ == "__main__":
    main()
