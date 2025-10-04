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

# 构建 Markdown 表格
lines = [
    "| 项目名称 | 项目简介 | 项目地址 |",
    "|----------|----------|----------|"
]

for repo in starred:
    name = repo.full_name
    url = repo.html_url
    desc = repo.description or "暂无描述"
    lines.append(f"| {name} | {desc} | [GitHub]({url}) |")

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌟 我的 GitHub 星标项目\n\n")
    f.write("\n".join(lines))
