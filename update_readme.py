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

# GitHub 图标
GITHUB_ICON = '<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="16">'

def format_stars(count):
    return f"{GITHUB_ICON} {count/1000:.1f}K" if count >= 1000 else f"{GITHUB_ICON} {count}"

# 构建 HTML 表格
lines = [
    "<table>",
    "<thead><tr><th style='width:15%'>项目名称</th><th style='width:45%'>项目简介</th><th style='width:10%'>Star</th><th style='width:15%'>更新时间</th><th style='width:15%'>链接</th></tr></thead>",
    "<tbody>"
]

for repo in starred:
    name = repo.name
    url = repo.html_url
    desc = (repo.description or "暂无描述").replace("|", "｜").replace("\n", " ")
    stars = format_stars(repo.stargazers_count)
    updated = repo.updated_at.strftime("%Y-%m-%d")
    lines.append(f"<tr><td><code>{name}</code></td><td>{desc}</td><td>{stars}</td><td>{updated}</td><td><a href='{url}'>🔗</a></td></tr>")

lines.append("</tbody></table>")

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌟 我的 GitHub 星标项目\n\n")
    f.write("\n".join(lines))
