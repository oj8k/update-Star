import os
import requests
from github import Github, Auth

# ✅ ChatGPT 翻译函数
def chatgpt_translate(text):
    api_url = os.getenv("CHATGPT_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("CHATGPT_MODEL", "gpt-3.5-turbo")
    api_key = os.getenv("OPENAI_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }

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
        if response.status_code != 200:
            print(f"❌ API 请求失败，状态码: {response.status_code}")
            print(f"❌ 接口返回内容: {response.text}")
            response.raise_for_status()

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

# ✅ 检测是否包含中文字符
def contains_chinese(text):
    for c in text:
        if '\u4e00' <= c <= '\u9fff':  # 基本汉字
            return True
    return False

# ✅ 判断是否纯英文（只有纯英文才翻译）
def is_pure_english(text):
    if contains_chinese(text):
        return False
    return all(ord(c) < 128 for c in text)

# ✅ 项目名称断行
def wrap_name(name, max_len=35):
    if len(name) <= max_len:
        return name
    return "<br>".join([name[i:i+max_len] for i in range(0, len(name), max_len)])

# ✅ 简介断行 - 优化：大幅增加长度，减少断行
def wrap_description(desc, max_len=100):
    desc = desc.replace("|", "｜").replace("\n", " ").strip()
    if len(desc) <= max_len:
        return desc
    # 智能断行：优先在空格、标点处断行
    lines = []
    current_line = ""
    for char in desc:
        current_line += char
        if len(current_line) >= max_len and char in ' ,，。！？；：、（）【】《》':
            lines.append(current_line)
            current_line = ""
    if current_line:
        lines.append(current_line)
    return "<br>".join(lines)

# ✅ Star 图标
def format_stars(count):
    if count >= 1000:
        value = f"{count/1000:.1f}K"
    else:
        value = str(count)
    return f"⭐ {value}"

# ✅ GitHub 认证
token = os.getenv("GH_TOKEN")
if not token:
    raise ValueError("GH_TOKEN 环境变量未设置或为空")

auth = Auth.Token(token)
g = Github(auth=auth)

username = os.getenv("GH_USERNAME", "oj8k")
user = g.get_user(username)
starred = list(user.get_starred())  # ✅ 保留默认顺序，不排序

# ✅ 去重：使用集合记录已添加的项目 URL
added_repos = set()

# ✅ 构建 README 表格
lines = [
    "# 🌟 我的 GitHub Star 项目\n",
    "| 项目名称 | 项目简介 | 项目链接 |",
    "|----------|-----------|:-----------:|"
]

print(f"📊 开始处理 {len(starred)} 个 Star 项目...")

for repo in starred:
    # 去重检查
    if repo.html_url in added_repos:
        print(f"⚠️ 跳过重复项目: {repo.name}")
        continue
    added_repos.add(repo.html_url)
    
    name = wrap_name(repo.name)
    desc_raw = repo.description or "暂无描述"

    # ✅ 关键优化：如果已包含中文，跳过翻译
    if is_pure_english(desc_raw):
        print(f"🔄 翻译: {repo.name}")
        desc_cn = chatgpt_translate(desc_raw)
        # ✅ 优化：使用单 <br> 减少空白，翻译紧跟原文
        desc_combined = f"{desc_raw}<br><i>{desc_cn}</i>"
    else:
        # ✅ 已包含中文，直接使用原描述
        print(f"✅ 跳过翻译（已有中文）: {repo.name}")
        desc_combined = desc_raw

    desc = wrap_description(desc_combined)
    stars = format_stars(repo.stargazers_count)
    url = repo.html_url
    star_link = f"<a href='{url}' target='_blank'>{stars}</a>"

    lines.append(f"| {name} | {desc} | {star_link} |")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"✅ README.md 生成完成！共 {len(added_repos)} 个项目")
