import os
import requests
from github import Github, Auth

# ✅ ChatGPT 翻译函数（支持自定义模型和 API 地址）
def chatgpt_translate(text, model="gpt-3.5-turbo", api_url="https://api.openai.com/v1/chat/completions"):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }

    prompt = f"请将以下英文翻译成中文：\n{text[:500]}..."  # 限制长度，避免 prompt 过长

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
        print(f"⚠️ ChatGPT 翻译失败：{e}")
        print(f"失败内容：{text}")
        return "（翻译失败）"

# ✅ 英文检测函数
def is_english(text):
    return all(ord(c) < 128 for c in text)

# ✅ 项目名称断行（每 20 字插入 <br>）
def wrap_name(name, max_len=20):
    return "<br>".join([name[i:i+max_len] for i in range(0, len(name), max_len)])

# ✅ 简介断行（每 40 字插入 <br>）
def wrap_description(desc, max_len=40):
    desc = desc.replace("|", "｜").replace("\n", " ").strip()
    return "<br>".join([desc[i:i+max_len] for i in range(0, len(desc), max_len)])

# ✅ Star 图标使用 Emoji
def format_stars(count):
    value = f"{count/1000:.1f}K" if count >= 1000 else str(count)
    return f"⭐ {value}"

# ✅ 获取 GitHub Token 和用户名
token = os.getenv("GH_TOKEN")
if not token:
    raise ValueError("GH_TOKEN 环境变量未设置或为空")

auth = Auth.Token(token)
g = Github(auth=auth)

username = "oj8k"
user = g.get_user(username)
starred = list(user.get_starred())  # 转为列表以便排序
starred.sort(key=lambda repo: repo.updated_at, reverse=True)

# ✅ 构建 Markdown 表格
lines = [
    "# 🌟 我的 GitHub 星标项目（按更新时间排序）\n",
    "| 项目名称 | 项目简介 | Star | 更新时间 | 链接 |",
    "|----------|-----------|------:|:----------:|:--:|"
]

# ✅ 获取 ChatGPT 模型和 API 地址（支持自定义）
chat_model = os.getenv("CHATGPT_MODEL", "gpt-3.5-turbo")
chat_api_url = os.getenv("CHATGPT_API_URL", "https://api.openai.com/v1/chat/completions")

for repo in starred:
    name = wrap_name(repo.name)
    desc_raw = repo.description or "暂无描述"

    # ✅ 翻译英文简介
    if is_english(desc_raw):
        desc_cn = chatgpt_translate(desc_raw, model=chat_model, api_url=chat_api_url)
        desc_combined = f"{desc_raw}<br><br><i>{desc_cn}</i>"
    else:
        desc_combined = desc_raw

    desc = wrap_description(desc_combined)
    stars = format_stars(repo.stargazers_count)
    updated = repo.updated_at.strftime("%Y-%m-%d")
    url = repo.html_url
    link_html = f"<a href='{url}' target='_blank'>GitHub</a>"

    lines.append(f"| {name} | {desc} | {stars} | {updated} | {link_html} |")

# ✅ 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
