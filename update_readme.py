from github import Github
import os

# 从环境变量读取 GitHub Token
token = os.getenv("GH_TOKEN")
username = "你的GitHub用户名"  # 👈 修改为你的用户名

g = Github(token)
user = g.get_user(username)
starred = user.get_starred()

lines = ["# 🌟 我的 GitHub 星标项目\n"]

for repo in starred:
    name = repo.full_name
    url = repo.html_url
    desc = repo.description or "暂无描述"
    lines.append(f"- [{name}]({url})  \n  > {desc}")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
