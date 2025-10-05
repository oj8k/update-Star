from github import Github, Auth
import os

# 获取 Token 和用户名
token = os.getenv("GH_TOKEN")
if not token:
    raise ValueError("GH_TOKEN 环境变量未设置或为空")

auth = Auth.Token(token)
g = Github(auth=auth)

username = "oj8k"
user = g.get_user(username)
starred = user.get_starred()

# Star 图标压缩显示
def format_stars(count):
    value = f"{count/1000:.1f}K" if count >= 1000 else str(count)
    return f"<sub>{value}</sub>"  # 小号字体，视觉紧凑

# 项目名称断行（每 20 字插入 <br>）
def wrap_name(name, max_len=20):
    return "<br>".join([name[i:i+max_len] for i in range(0, len(name), max_len)])

# 简介断行（每 40 字插入 <br>，不截断）
def wrap_description(desc, max_len=40):
    desc = (desc or "暂无描述").replace("|", "｜").replace("\n", " ").strip()
    return "<br>".join([desc[i:i+max_len] for i in range(0, len(desc), max_len)])

# 构建 Markdown 表格
lines = [
    "# 🌟 我的 GitHub 星标项目\n",
    "| 项目名称 | 项目简介 | Star | 更新时间 | 链接 |",
    "|----------|-----------|------:|:----------:|:--:|"
]

for repo in starred:
    name = wrap_name(repo.name)
    desc = wrap_description(repo.description)
    stars = format_stars(repo.stargazers_count)
    updated = repo.updated_at.strftime("%Y-%m-%d")  # 保持一行显示
    url = repo.html_url

    lines.append(f"| {name} | {desc} | {stars} | {updated} | [GitHub]({url}) |")

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
