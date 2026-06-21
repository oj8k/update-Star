import os
import requests
from github import Github, Auth

# ✅ 修改后的 ChatGPT 翻译函数
def chatgpt_translate(text):
    api_url = os.getenv("CHATGPT_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("CHATGPT_MODEL", "gpt-3.5-turbo")
    api_key = os.getenv("OPENAI_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # ⬇️ 新增以下三行伪装头部 ⬇️
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }

    # 稍微优化一下 prompt 拼接，避免切片影响结构
    clean_text = text[:500]
    prompt = f"请将以下英文翻译成中文：\n{clean_text}"

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
        
        # 如果状态码不是 200，先不急着 raise_for_status，先打印出接口返回了什么
        if response.status_code != 200:
            print(f"❌ API 请求失败，状态码: {response.status_code}")
            print(f"❌ 接口返回内容: {response.text}")
            response.raise_for_status()

        # 尝试解析 JSON
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
        
    except requests.exceptions.JSONDecodeError:
        print(f"⚠️ ChatGPT 响应解析 JSON 失败！")
        print(f"真实返回的非 JSON 内容为: \n{response.text}")
        return "（翻译解析失败）"
    except Exception as e:
        print(f"⚠️ ChatGPT 翻译发生其他错误：{e}")
        print(f"失败原始内容：{text}")
        return "（翻译失败）"

# ✅ 英文检测函数
def is_english(text):
    return all(ord(c) < 128 for c in text)

# ✅ 项目名称断行
def wrap_name(name, max_len=20):
    return "<br>".join([name[i:i+max_len] for i in range(0, len(name), max_len)])

# ✅ 简介断行
def wrap_description(desc, max_len=35):
    desc = desc.replace("|", "｜").replace("\n", " ").strip()
    return "<br>".join([desc[i:i+max_len] for i in range(0, len(desc), max_len)])

# ✅ Star 图标
def format_stars(count):
    value = f"{count/1000:.1f}K" if count >= 1000 else str(count)
    return f"⭐ {value}"

# ✅ GitHub 认证
token = os.getenv("GH_TOKEN")
if not token:
    raise ValueError("GH_TOKEN 环境变量未设置或为空")

auth = Auth.Token(token)
g = Github(auth=auth)

username = os.getenv("GH_USERNAME")
user = g.get_user(username)
starred = list(user.get_starred())  # ✅ 保留默认顺序，不排序

# ✅ 构建 README 表格（无时间列，Star+链接合并）
lines = [
    "# 🌟 我的 GitHub Star项目\n",
    "| 项目名称 | 项目简介 | 项目链接 |",
    "|----------|-----------|:-----------:|"
]

for repo in starred:
    name = wrap_name(repo.name)
    desc_raw = repo.description or "暂无描述"

    if is_english(desc_raw):
        desc_cn = chatgpt_translate(desc_raw)
        desc_combined = f"{desc_raw}<br><br><i>{desc_cn}</i>"
    else:
        desc_combined = desc_raw

    desc = wrap_description(desc_combined)
    stars = format_stars(repo.stargazers_count)
    url = repo.html_url
    star_link = f"<a href='{url}' target='_blank'>{stars}</a>"

    lines.append(f"| {name} | {desc} | {star_link} |")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
