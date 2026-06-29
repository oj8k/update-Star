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
#
#  【功能说明】
#    - 自动获取 GitHub Star 列表并生成 README.md 表格
#    - 纯英文描述自动翻译为中文；已有中文的跳过翻译
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

import os
import requests
from github import Github, Auth


# ─── ChatGPT 翻译 ─────────────────────────────
def chatgpt_translate(text):
    """调用 ChatGPT API 将英文翻译为中文，失败返回空字符串"""
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

    try:
        resp = requests.post(api_url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  ⚠️  翻译失败: {e}")
        return ""


# ─── 中文检测 ─────────────────────────────────
def has_chinese(text):
    """检测是否包含中文字符"""
    return any("\u4e00" <= c <= "\u9fff" for c in text)


def needs_translation(text):
    """只有不含中文的描述才需要翻译"""
    return not has_chinese(text)


# ─── 项目名称 ─────────────────────────────────
def fmt_name(name, max_len=20):
    """
    项目名称格式化：
    - 不超过 max_len 直接返回
    - 超长则截断加 ...，不换行
    """
    if len(name) <= max_len:
        return name
    return name[: max_len - 3] + "..."


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
    # 压缩连续空格
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
    - 用 &nbsp; 连接 ⭐ 和数字，防止被拆成两行
    - >= 10000 → X.XW, >= 1000 → X.XK, 其他 → 原始数字
    """
    if count >= 10000:
        return f"⭐&nbsp;{count / 10000:.1f}W"
    if count >= 1000:
        return f"⭐&nbsp;{count / 1000:.1f}K"
    return f"⭐&nbsp;{count}"


# ─── 主流程 ───────────────────────────────────
def main():
    token = os.getenv("GH_TOKEN")
    username = os.getenv("GH_USERNAME", "oj8k")

    if not token:
        raise ValueError("❌ 未设置 GH_TOKEN 环境变量")

    auth = Auth.Token(token)
    g = Github(auth=auth)
    user = g.get_user(username)
    starred = list(user.get_starred())

    seen = set()
    lines = [
        "# 🌟 我的 GitHub Star 项目\n",
        "本仓库通过 GitHub Actions 自动同步我的 GitHub Star 项目列表，并生成 README 表格。\n",
        "> 如需 Fork/复用本项目，请在仓库的 **Settings → Secrets and variables → Actions** 中配置以下变量。\n",
        "## 🔧 环境变量配置\n",
        "| 变量名 | 必填 | 说明 |",
        "|--------|------|------|",
        "| `GH_TOKEN` | ✅ | GitHub Personal Access Token（需勾选 `repo` 权限） |",
        "| `GH_USERNAME` | ✅ | GitHub 用户名，例如 `oj8k` |",
        "| `OPENAI_API_KEY` | ❌ | ChatGPT API Key，用于翻译纯英文项目描述 |",
        "| `CHATGPT_API_URL` | ❌ | ChatGPT API 地址，默认 `https://api.openai.com/v1/chat/completions` |",
        "| `CHATGPT_MODEL` | ❌ | ChatGPT 模型，默认 `gpt-3.5-turbo` |\n",
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

        # 清理原始描述（去掉已有 <br>，截断超长文本，不加新 <br>）
        desc_raw = clean_desc(repo.description or "暂无描述")

        # 只有纯英文才翻译
        if needs_translation(desc_raw):
            print(f"  🔄 翻译: {repo.name}")
            desc_cn = chatgpt_translate(desc_raw)
            if desc_cn:
                # 原文和翻译之间只用一个 <br>，翻译紧跟原文，无空白
                desc_final = f"{desc_raw}<br><i>{desc_cn}</i>"
            else:
                # 翻译失败 → 只显示原文，不显示错误信息
                desc_final = desc_raw
        else:
            print(f"  ✅ 跳过翻译: {repo.name}")
            desc_final = desc_raw

        star_txt = fmt_stars(repo.stargazers_count)
        star_link = f"<a href='{repo.html_url}' target='_blank'>{star_txt}</a>"

        lines.append(f"| {name} | {desc_final} | {star_link} |")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n✅ README.md 生成完成！共 {len(seen)} 个项目")


if __name__ == "__main__":
    main()
