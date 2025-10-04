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

# GitHub 图标（Octocat）
GITHUB_ICON = '<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="16">'

# 格式化 Star 数（加图标 + K 单位）
def format_stars(count):
    if count >= 1000:
        return f"{GITHUB_ICON} {count/1000:.1f}K"
    else:
        return f"{GITHUB_ICON} {count}"

# 构建 Markdown 表格
lines = [
    "| 项目名称 | 项目简介 | Star | 更新时间 | 链接 |",
    "|----------|-----------|------:|:----------:|:--:|"
]

for repo in starred:
    name = f"`{repo.name}`"
    url = repo.html_url
    desc = repo.description or "暂无描述"

    # 清洗简介：去除换行、替换竖线、截断过长内容
    desc = desc.strip().replace("\n", " ").replace("|", "｜")
    if len(desc) > 60:
        desc = desc[:57] + "..."

    stars = format_stars(repo.stargazers_count)
    updated = repo.updated_at.strftime("%Y-%m-%d")
    lines.append(f"| {name} | {desc} | {stars} | {updated} | [🔗]({url}) |")

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌟 我的 GitHub 星标项目\n\n")
    f.write("\n".join(lines))
