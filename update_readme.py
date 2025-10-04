from github import Github, Auth
import os

token = os.getenv("GH_TOKEN")
if not token:
    raise ValueError("GH_TOKEN 环境变量未设置或为空")

auth = Auth.Token(token)
g = Github(auth=auth)

username = "oj8k"
user = g.get_user(username)
starred = user.get_starred()

lines = [
    "| 项目名称 | 项目简介 | ⭐ | 更新时间 | 🔗 |",
    "|----------|-----------|----:|:----------:|:--:|"
]

for repo in starred:
    name = repo.name
    url = repo.html_url
    desc = repo.description or "暂无描述"
    stars = repo.stargazers_count
    updated = repo.updated_at.strftime("%Y-%m-%d")
    lines.append(f"| `{name}` | {desc} | {stars} | {updated} | [🔗]({url}) |")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌟 我的 GitHub 星标项目\n\n")
    f.write("\n".join(lines))
