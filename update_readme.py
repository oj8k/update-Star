# ===========================================
#  update-Star - GitHub Star 项目列表生成器
# ===========================================
#
#  【环境变量配置】
#
#  REQUIRED:
#    GH_TOKEN       - GitHub Personal Access Token
#    GH_USERNAME   - GitHub 用户名（默认: oj8k）
#
#  OPTIONAL:
#    OPENAI_API_KEY   - ChatGPT API Key（留空则跳过纯英文描述的翻译）
#    CHATGPT_API_URL - ChatGPT API 地址（默认: https://api.openai.com/v1/chat/completions）
#    CHATGPT_MODEL   - ChatGPT 模型（默认: gpt-3.5-turbo）
#
#  【功能说明】
#    - 自动获取指定用户的 GitHub Star 列表
#    - 纯英文项目描述自动调用 ChatGPT 翻译为中文
#    - 已有中文描述的项目自动跳过翻译（节省 API 配额）
#    - 自动去重（按项目 URL 判断）
#    - 生成格式化的 README.md 表格
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


# ─── ChatGPT 翻译函数 ──────────────────────────
def chatgpt_translate(text):
    """调用 ChatGPT API 将英文翻译为中文"""
    api_url = os.getenv("CHATGPT_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("CHATGPT_MODEL", "gpt-3.5-turbo")
    api_key = os.getenv("OPENAI_API_KEY", "")

    if not api_key:
        return "（未配置 API Key，跳过翻译）"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }

    prompt = f"请将以下英文翻译成中文：\n{text[:500]}"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个专业的中英翻译助手。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  ⚠️  翻译失败: {e}")
        return "（翻译失败）"


# ─── 中文检测函数 ──────────────────────────
def has_chinese(text):
    """检测字符串中是否包含中文字符"""
    for c in text:
        if '\u4e00' <= c <= '\u9fff':
            return True
    return False


def is_pure_english(text):
    """判断是否纯英文（不含中文则视为需要翻译）"""
    return not has_chinese(text)


# ─── 项目名称格式化 ──────────────────────────
def fmt_name(name, max_len=18):
    """
    项目名称格式化：
    - 超过 max_len 字符时按单词断行
    - 避免把单词劈成两半
    - 保持紧凑，避免挤占「项目链接」列空间
    """
    if len(name) <= max_len:
        return name
    
    # 按单词边界断行
    parts, line = [], ""
    for w in name.split():
        if len(line) + len(w) + 1 <= max_len:
            line += (" " if line else "") + w
        else:
            if line:
                parts.append(line)
            line = w
    if line:
        parts.append(line)
    return "<br>".join(parts)


# ─── 项目简介格式化 ──────────────────────────
def fmt_desc(desc, max_len=80):
    """
    项目简介格式化：
    - 尽量不断行，保持紧凑
    - 超过 max_len 才在标点 / 空格处断行
    - 原文和翻译之间只用单 <br>，避免大片空白
    """
    desc = desc.replace("|", "｜").replace("\n", " ").strip()
    if len(desc) <= max_len:
        return desc
    
    # 智能断行：优先在标点、空格处断开
    buf, lines = "", []
    for c in desc:
        buf += c
        if len(buf) >= max_len and c in " ,，。！？；：、（）【】《》":
            lines.append(buf)
            buf = ""
    if buf:
        lines.append(buf)
    return "<br>".join(lines)


# ─── Star 数格式化 ──────────────────────────
def fmt_stars(count):
    """
    Star 数格式化：
    - >= 10000 显示为 X.XW
    - >= 1000 显示为 X.XK
    - < 1000 显示为原始数字
    - 保持紧凑，避免 ⭐ 图标被挤成两行
    """
    if count >= 10000:
        return f"⭐ {count/10000:.1f}W"
    if count >= 1000:
        return f"⭐ {count/1000:.1f}K"
    return f"⭐ {count}"


# ─── 主流程 ──────────────────────────────────
def main():
    # 读取环境变量
    token = os.getenv("GH_TOKEN")
    username = os.getenv("GH_USERNAME", "oj8k")

    if not token:
        raise ValueError("❌ 未设置 GH_TOKEN 环境变量")

    # GitHub 认证
    auth = Auth.Token(token)
    g = Github(auth=auth)
    user = g.get_user(username)
    starred = list(user.get_starred())  # 保持默认顺序

    # 去重集合
    seen = set()

    # README 表格头部
    lines = [
        "# 🌟 我的 GitHub Star 项目\n",
        "| 项目名称 | 项目简介 | 项目链接 |",
        "|----------|-----------|:-----------:|"
    ]

    print(f"📊 共获取 {len(starred)} 个 Star 项目，开始处理...\n")

    for repo in starred:
        # 去重检查
        if repo.html_url in seen:
            print(f"  ⚠️  跳过重复: {repo.name}")
            continue
        seen.add(repo.html_url)

        # 项目名称
        name = fmt_name(repo.name)

        # 项目描述
        desc_raw = repo.description or "暂无描述"

        # 纯英文才翻译；已有中文直接跳过
        if is_pure_english(desc_raw):
            print(f"  🔄 翻译: {repo.name}")
            desc_cn = chatgpt_translate(desc_raw)
            # 只用单 <br> 连接原文和翻译，减少空白
            desc_final = f"{desc_raw}<br><i>{desc_cn}</i>"
        else:
            print(f"  ✅ 跳过翻译（已有中文）: {repo.name}")
            desc_final = desc_raw

        # 格式化简介
        desc = fmt_desc(desc_final)

        # Star 数和链接（保持紧凑，避免换行）
        star_txt = fmt_stars(repo.stargazers_count)
        star_link = f"<a href='{repo.html_url}' target='_blank'>{star_txt}</a>"

        # 添加到表格
        lines.append(f"| {name} | {desc} | {star_link} |")

    # 写入 README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n✅ README.md 生成完成！共 {len(seen)} 个项目")


if __name__ == "__main__":
    main()
