# 🌟 我的 GitHub Star 项目

<a id='top'></a>

本仓库通过 GitHub Actions 自动同步我的 GitHub Star 项目列表，并生成 README 表格。

> 如需 Fork/复用本项目，请在仓库的 **Settings → Secrets and variables → Actions** 中配置以下变量。

## 🔧 环境变量配置

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `GH_TOKEN` | ✅ | GitHub Personal Access Token（需勾选 `repo` 权限） |
| `GH_USERNAME` | ✅ | GitHub 用户名，例如 `oj8k` |
| `OPENAI_API_KEY` | ❌ | ChatGPT API Key，用于翻译纯英文项目描述 |
| `CHATGPT_API_URL` | ❌ | ChatGPT API 地址，默认 `https://api.openai.com/v1/chat/completions` |
| `CHATGPT_MODEL` | ❌ | ChatGPT 模型，默认 `gpt-3.5-turbo` |
| `TRANSLATE_DELAY` | ❌ | 翻译间隔秒数，默认 `0.5` |
| `TRANSLATION_CACHE` | ❌ | 翻译缓存文件路径，默认 `translations.json` |

## ⚡ 触发方式

- 手动触发：仓库 Actions → 自动更新星标项目 → Run workflow

- 自动触发：每天 UTC 00:00（北京时间 08:00）运行一次

---

| 项目名称 | 项目简介 | 项目链接 |
|----------|-----------|:-----------:|
| GPT5.6-5.5- | 此项目为gpt5.6/5.5破甲方案 | [⭐ 150](https://github.com/zxr-roro/GPT5.6-5.5-) |
| frp-openwrt-one-cl<br>ick | 一键安装 Frp，支持 VPS/云服务器和 OpenWrt/iStoreOS/软路由安装管理 frps/frpc | [⭐ 6](https://github.com/slobys/frp-openwrt-one-click) |
| rustdesk | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer.<br>一款开源远程桌面应用程序，专为自托管设计，作为TeamViewer的替代方案。 | [⭐ 11.9W](https://github.com/rustdesk/rustdesk) |
| AIStudioToAPI | A wrapper that exposes Google AI Studio Build as OpenAI, Gemini, and Anthropic compatible APIs.（一个将 Google AI Studio... | [⭐ 1.4K](https://github.com/iBUHub/AIStudioToAPI) |
| flutter_server_box | ServerBox - server status & toolbox<br>ServerBox - 服务器状态与工具箱 | [⭐ 8.2K](https://github.com/lollipopkit/flutter_server_box) |
| saladict | 🌈一个跨平台的划词翻译和OCR软件 ｜ A cross-platform software for text translation and recognition. | [⭐ 123](https://github.com/allentown521/saladict) |
| open-reverselab | Agent-native reverse-engineering lab with a 197-article knowledge base, MCP tools, and CTF/APK/PE automation workflows.<br>一个原生代理逆向工程实验室，配备包含197篇文章的知识库、MCP工具，以及CTF/APK/PE自动化工作流。 | [⭐ 880](https://github.com/LING71671/open-reverselab) |
| Codex-X | Codex Switch & Instruct desktop manager<br>Codex Switch & Instruct 桌面管理器 | [⭐ 1.5K](https://github.com/yynxxxxx/Codex-X) |
| CLIProxyAPI | Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service,...<br>将 Antigravity、ChatGPT Codex、Claude Code、Grok Build 封装为与 OpenAI/Gemini/Claude/Codex 兼容的 API 服务，…… | [⭐ 4.4W](https://github.com/router-for-me/CLIProxyAPI) |
| wxapkg | 跨平台微信小程序反编译 GUI 工具，.wxapkg 文件扫描 + 解密 + 解包工具 | [⭐ 3.8K](https://github.com/wux1an/wxapkg) |
| UFI-TOOLS | A functional tools for z*e devices (F50 ｜ U30 Air)<br>一个适用于z*e设备（F50 | U30 Air）的功能工具。 | [⭐ 1.6K](https://github.com/kanoqwq/UFI-TOOLS) |
| QtScrcpy | Android real-time display control software<br>Android实时显示控制软件 | [⭐ 3.1W](https://github.com/barry-ran/QtScrcpy) |
| grok-register | 【已存活三个月+，无封号】批量注册稳定 Grok 账号，可直接导入 grok2api 和 cpa 使用，并且可以与cloudflare无限域名邮箱等联动。通过1000+账号连续注册测试。 | [⭐ 1.5K](https://github.com/AaronL725/grok-register) |
| grok2api | 暂无描述 | [⭐ 1.9K](https://github.com/jiujiu532/grok2api) |
| nodewarden | Bitwarden-compatible server running on Cloudflare Workers<br>运行在Cloudflare Workers上的与Bitwarden兼容的服务器 | [⭐ 3.2K](https://github.com/shuaiplus/nodewarden) |
| dnsmgr | 彩虹聚合DNS管理系统 | [⭐ 1.4K](https://github.com/netcccyun/dnsmgr) |
| sub2api | Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 | [⭐ 3.4W](https://github.com/Wei-Shaw/sub2api) |
| dji-4g-vohive-mac | 在 Mac（Apple Silicon / Intel）上用 UTM 跑 Linux 虚拟机，把大疆 4G 模块（EG25-G）伪装成移远 Quectel EC25 并部署 vohive 平台的完整步骤 | [⭐ 725](https://github.com/wlzh/dji-4g-vohive-mac) |
| fluxdo | 一个 Linux.do 第三方客户端 | [⭐ 2.1K](https://github.com/Lingyan000/fluxdo) |
| GeekezBrowser | A professional anti-detect browser built on Electron and Puppeteer, integrated with the powerful Xray-core....<br>一款基于Electron和Puppeteer构建的专业反检测浏览器，集成了强大的Xray-core...... | [⭐ 984](https://github.com/EchoHS/GeekezBrowser) |
| tg-vault | 暂无描述 | [⭐ 132](https://github.com/hicocos/tg-vault) |
| Netcatty | SSH workspace, SFTP, and terminals in one<br>SSH工作区、SFTP和终端三合一。 | [⭐ 3.9K](https://github.com/binaricat/Netcatty) |
| CF-Server-Monitor | 一个基于 Cloudflare Workers + D1 + Durable Objects 的多服务器监控探针系统，支持实时监控、离线告警，到期通知，历史数据查看、延迟追踪、地图展示等功能。兼容主流Linux系统，Alpine... | [⭐ 905](https://github.com/huilang-me/CF-Server-Monitor) |
| argosbx | 小白自建代理神器！ArgoSBX一键无交互小钢炮脚本💣：Sing-box、Xray、Argo三内核自动搭配；支持VPS、Docker、容器多环境部署；套CDN的5大方案+套WARP的15种组合；已支持协议：Naiveproxy、AnyTLS... | [⭐ 5.5K](https://github.com/yonggekkk/argosbx) |
| codex-candy-eval | Codex 降智测试 | [⭐ 767](https://github.com/haowang02/codex-candy-eval) |
| cc-switch | A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent....<br>一个跨平台桌面一体化助手，适用于Claude Code、Codex、OpenCode、OpenClaw、Grok Build和Hermes Agent等…… | [⭐ 12.0W](https://github.com/farion1231/cc-switch) |
| CodexPlusPlus | An enhanced tool for CodexApp, striving to make Codex better to use and more comfortable...<br>一款针对CodexApp的增强工具，致力于让Codex更好用、更舒适…… | [⭐ 2.6W](https://github.com/BigPizzaV3/CodexPlusPlus) |
| vohive-release | 暂无描述 | [⭐ 731](https://github.com/iniwex5/vohive-release) |
| dujiao-next | Dujiao-Next Server 独角Next服务端 | [⭐ 825](https://github.com/dujiao-next/dujiao-next) |
| daidai-panel | Lightweight scheduled task management panel, similar to Qinglong Panel. 轻量级定时任务管理面板 | [⭐ 280](https://github.com/linzixuanzz/daidai-panel) |
| carrier-ims-for-pi<br>xel | Carrier IMS for Pixel (TurboIMS): multilingual (中文/English) pixel ims / ims / carrierconfig / volte / vowifi / 5G+... | [⭐ 1.3K](https://github.com/ryfineZ/carrier-ims-for-pixel) |
| ds-free-api | DeepSeek网页端API代理，支持OpenAI与Anthropic兼容接口 ｜ OpenAI & Anthropic compatible API proxy for DeepSeek web | [⭐ 542](https://github.com/NIyueeE/ds-free-api) |
| karing | Simple & Powerful proxy utility, Support routing rules for clash/sing-box<br>简单而强大的代理工具，支持 clash/sing-box 的路由规则。 | [⭐ 1.4W](https://github.com/KaringX/karing) |
| read-frog | 🐸 Read Frog - Open Source Immersive Translate ｜ 🐸 陪读蛙 - 开源沉浸式翻译 | [⭐ 8.6K](https://github.com/mengxi-ream/read-frog) |
| clash-rules | 🦄️ 🎃 👻 Clash Premium 规则集(RULE-SET)，兼容 ClashX Pro、Clash for Windows 等基于 Clash Premium 内核的客户端。 | [⭐ 2.8W](https://github.com/Loyalsoldier/clash-rules) |
| meta-rules-dat | rules-dat for mihomo<br>mihomo 的规则 dat 文件 | [⭐ 4.8K](https://github.com/MetaCubeX/meta-rules-dat) |
| Xray | 最好用的 Xray 一键安装脚本 & 管理脚本 | [⭐ 16](https://github.com/justypist/Xray) |
| Sing-box | 既然来了，就留下你的Star吧！Serv00 ｜ CT8 ｜ Hostuno ｜ VPS ｜ 游戏机 ｜ sing-box(reality + hy2 + vmess-argo... | [⭐ 4.9K](https://github.com/eooce/Sing-box) |
| flvx | FLVX转发面板 | [⭐ 258](https://github.com/Sagit-chu/flvx) |
| dstatus | DStatus 探针 是一个现代化的服务器状态监控系统，提供简洁美观的UI界面和强大的探针 agent 监控功能。 | [⭐ 396](https://github.com/fev125/dstatus) |
| linuxdo-checkin | linux.do Daily Check-In. 每日签到，每日打卡 | [⭐ 328](https://github.com/doveppp/linuxdo-checkin) |
| aimili-vpngate | aimili-vpngate是一个借助vpngate.net让Linux用干净ip出站的代理工具。 | [⭐ 1.4K](https://github.com/baoweise-bot/aimili-vpngate) |
| DTV | 抖音、b站、斗鱼、虎牙跨平台轻量化桌面客户端 | [⭐ 1.9K](https://github.com/chen-zeong/DTV) |
| sms-jiema | 汇总国外1000个免费手机号接码 - 国外免费手机号验证平台 | [⭐ 305](https://github.com/workwayfi/sms-jiema) |
| worldmonitor | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure...<br>实时全球情报仪表盘。由人工智能驱动的新闻聚合、地缘政治监控及基础设施…… | [⭐ 6.9W](https://github.com/koala73/worldmonitor) |
| BilibiliSponsorBlo<br>ck | 一款跳过小电视视频中恰饭片段的浏览器插件，移植自 SponsorBlock。A browser extension to skip sponsored segments in videos, ported from the... | [⭐ 5.7K](https://github.com/hanydd/BilibiliSponsorBlock) |
| SSTap-Rule | 支持更多游戏规则，让SSTap成为真正的“网游加速器” | [⭐ 6.6K](https://github.com/FQrabbit/SSTap-Rule) |
| Saber-Translator | ✨ 一款小白也能轻松使用的漫画翻译工具，旨在帮助漫画爱好者轻松跨越语言障碍，畅享原汁原味的日文漫画。 利用先进的 AI 技术，智能检测漫画中的对话气泡，精准识别日文文本，并快速翻译成流畅自然的中文。 ✨ 无论是图片还是 PDF... | [⭐ 3.4K](https://github.com/MashiroSaber03/Saber-Translator) |
| templates | 基于开源新版 QD 框架站发布的公共har模板库，仅供示例 | [⭐ 1.6K](https://github.com/qd-today/templates) |
| douyin_downloader | 抖音福袋扭蛋机，抖音抢福袋工具，自己工作之余用VC++写的，功能还包含了一些其他小功能，抖音无水印视频下载器，抖音直播间录制下载器，抖音批量取消关注取关器 | [⭐ 605](https://github.com/testusyd/douyin_downloader) |
| medicine | 原研药列表 | [⭐ 1.4K](https://github.com/lvwzhen/medicine) |
| free-proxy-list | 🚀 Free HTTP, SOCKS4, & SOCKS5 proxy list * Updated every 5 minutes * and rotating proxy API (100+ countries)<br>🚀 免费HTTP、SOCKS4和SOCKS5代理列表 * 每5分钟更新一次 * 以及轮换代理API（覆盖100多个国家） | [⭐ 6.3K](https://github.com/proxifly/free-proxy-list) |
| acg-faka | 个人发卡源码，发卡系统，二次元发卡系统，二次元发卡源码，发卡程序，动漫发卡，PHP发卡源码，异次元发卡 | [⭐ 5.3K](https://github.com/lizhipay/acg-faka) |
| dujiaoka | 🦄独角数卡(自动售货系统)-开源站长自动化售货解决方案、高效、稳定、快速！🚀🚀🎉🎉 | [⭐ 1.2W](https://github.com/assimon/dujiaoka) |
| sh | KEJILION.SH 一款全功能的Linux管理脚本！An all-in-one Linux management script! | [⭐ 3.0K](https://github.com/kejilion/sh) |
| Awesome-NAS-Docker | 一个专注于 NAS 和 Docker 部署的开源项目合集，覆盖 AI、开发、数据管理、多媒体、运维等场景，提供一键式部署指南和实用教程，让 NAS 变身全能生产力工具！ | [⭐ 4.2K](https://github.com/TWO-ICE/Awesome-NAS-Docker) |
| opentrace | Open Source Visualized Route Tracing Tool for macOS, Windows, and Linux.<br>面向macOS、Windows和Linux的开源可视化路由追踪工具。 | [⭐ 4.4K](https://github.com/Archeb/opentrace) |
| sun-panel | A server, NAS navigation panel, Homepage, browser homepage. ｜ 一个服务器、NAS导航面板、Homepage、浏览器首页。 | [⭐ 5.2K](https://github.com/hslr-s/sun-panel) |
| appstore | 1Panel 应用商店的非官方应用适配库 1Panel Store Unofficial App Adaptation Repository (https://t.me/dockerbox) | [⭐ 1.0K](https://github.com/okxlin/appstore) |
| nexus-terminal | 一款现代化的 Web SSH / RDP / VNC 客户端，提供独立桌面端，支持人机验证、2FA、界面定制、操作审计等强大功能。 | [⭐ 1.8K](https://github.com/Heavrnl/nexus-terminal) |
| fly-cursor-free | 轻松一键续杯 Cursor Pro，保持14天试用不掉。【支持 Claude 4】 | [⭐ 1.9K](https://github.com/liqiang-xxfy/fly-cursor-free) |
| NapCatQQ | Modern protocol-side framework based on NTQQ<br>基于NTQQ的现代协议侧框架 | [⭐ 9.9K](https://github.com/NapNeko/NapCatQQ) |
| s-ui | An advanced Web Panel • Built for SagerNet/Sing-Box<br>一个高级Web面板 • 专为SagerNet/Sing-Box打造 | [⭐ 9.6K](https://github.com/alireza0/s-ui) |
| taosync | TaoSync是一个适用于OpenList v3+的自动化同步工具/Sync for OpenList/AList | [⭐ 1.5K](https://github.com/dr34m-cn/taosync) |
| alist-sync | 暂无描述 | [⭐ 173](https://github.com/xjxjin/alist-sync) |
| cloudflare_temp_em<br>ail | CloudFlare free temp domain email 免费收发 临时域名邮箱 支持附件 IMAP SMTP TelegramBot | [⭐ 1.1W](https://github.com/dreamhunter2333/cloudflare_temp_email) |
| oci-helper | 基于 Oracle OCI SDK 🐢 开发的 web 端可视化甲骨文云助手（Y探长），目前实现的功能有：批量添加多个租户配置、更改实例配置、引导卷配置、一键开启免费AMD实例下行500Mbps、一键更新、一键救援/缩小硬盘、附加ipv6、... | [⭐ 765](https://github.com/Yohann0617/oci-helper) |
| vaultwarden | Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs<br>用Rust编写的非官方Bitwarden兼容服务器，以前称为bitwarden_rs。 | [⭐ 6.4W](https://github.com/dani-garcia/vaultwarden) |
| NodePassDash | A modern web dashboard for managing NodePass<br>一个用于管理NodePass的现代Web仪表板。 | [⭐ 434](https://github.com/NodePassProject/NodePassDash) |
| flux-panel | 基于gost的转发面板 | [⭐ 170](https://github.com/BrunuhVille/flux-panel) |
| nav-item | 导航站 | [⭐ 383](https://github.com/eooce/nav-item) |
| watchtower | A process for automating Docker container base image updates.<br>自动化Docker容器基础镜像更新的流程。 | [⭐ 2.5W](https://github.com/containrrr/watchtower) |
| NodeSeekSignin | NodeSeek 论坛自动签到Cookie版，支持青龙、直接运行、钉钉机器人通知。 | [⭐ 39](https://github.com/wugeng20/NodeSeekSignin) |
| nftables-nat-rust | nftables nat规则生成器 | [⭐ 946](https://github.com/arloor/nftables-nat-rust) |
| realm-xwPF | Realm 全功能一键中转脚本，终端可视化界面构建网络转发服务.Realm: Full-featured one-click network relay — configure and manage forwarding rules... | [⭐ 1.1K](https://github.com/zywe03/realm-xwPF) |
| UniBoard | 个人介绍，导航页、笔记、短链、文件分享、探针，私有化部署。Profile、Note、ShortURL、FileSharing、probeMonitor…… with self-host | [⭐ 241](https://github.com/Coooolfan/UniBoard) |
| ChinaTextbook | 所有小初高、大学PDF教材。 | [⭐ 7.6W](https://github.com/TapXWorld/ChinaTextbook) |
| BillionMail | BillionMail gives you open-source MailServer, NewsLetter, Email Marketing — fully self-hosted, dev-friendly, and free...<br>BillionMail 为您提供开源邮件服务器、新闻简报、电子邮件营销——完全自托管，对开发者友好，且免费…… | [⭐ 1.5W](https://github.com/Billionmail/BillionMail) |
| oneclickvirt.githu<br>b.io | 一键虚拟化说明文档(OneClickVirt Documentation) | [⭐ 163](https://github.com/oneclickvirt/oneclickvirt.github.io) |
| karakeep | A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search<br>一个可自托管的书签全能应用（支持链接、笔记和图片），具备基于AI的自动标签和全文搜索功能。 | [⭐ 2.8W](https://github.com/karakeep-app/karakeep) |
| reinstall | 一键DD/重装脚本 (One-click reinstall OS on VPS) | [⭐ 1.3W](https://github.com/bin456789/reinstall) |
| cloud-mail | A Cloudflare-based email service ｜ 基于 Cloudflare 的邮箱服务 ｜ Cloudflare Email 邮箱 Mail | [⭐ 1.3W](https://github.com/maillab/cloud-mail) |
| ContextMenuManager | 🖱️ 一个管理 Windows 右键上下文菜单的程序（支持Windows 7 - 11）A program to manage the Windows right-click context menu with support of... | [⭐ 838](https://github.com/Jack251970/ContextMenuManager) |
| SafeLine | SafeLine is a self-hosted WAF(Web Application Firewall) / reverse proxy to protect your web apps from attacks and...<br>SafeLine 是一个自托管的 WAF（Web 应用防火墙）/反向代理，用于保护您的 Web 应用免受攻击以及…… | [⭐ 2.2W](https://github.com/chaitin/SafeLine) |
| Termix | Self-hosted SSH and remote desktop management.<br>自托管SSH与远程桌面管理。 | [⭐ 1.4W](https://github.com/Termix-SSH/Termix) |
| komari-theme-purca<br>rte | 一个为 Komari 设计的磨砂玻璃风格主题 | [⭐ 426](https://github.com/Montia37/komari-theme-purcarte) |
| NodeQuality | 在沙箱环境中运行vps测试脚本，并排版测试结果 | [⭐ 1.9K](https://github.com/LloydAsp/NodeQuality) |
| subs-check | 订阅转换、测速、测活、流媒体检测、重命名、导出为任意格式订阅的工具 | [⭐ 5.1K](https://github.com/beck-8/subs-check) |
| zjm | 暂无描述 | [⭐ 44](https://github.com/vpsbuy/zjm) |
| nezha | :trollface: Self-hosted, lightweight server and website monitoring and O&M tool<br>:trollface: 自托管、轻量级的服务器和网站监控与运维工具 | [⭐ 1.0W](https://github.com/nezhahq/nezha) |
| komari | A simple server monitor tool.<br>一个简单的服务器监控工具。 | [⭐ 5.4K](https://github.com/komari-monitor/komari) |
| aya | Android ADB desktop app<br>Android ADB桌面应用程序 | [⭐ 5.3K](https://github.com/liriliri/aya) |
| GitHubDaily | 坚持分享 GitHub 上高质量、有趣实用的开源技术教程、开发者工具、编程网站、技术资讯。A list cool, interesting projects of GitHub. | [⭐ 4.7W](https://github.com/GitHubDaily/GitHubDaily) |
| AiNiee | 一款专注于Ai翻译的工具，一键自动翻译RPG SLG游戏，Epub TXT小说，PDF Word MD文档，Srt Vtt Lrc字幕等等复杂长文本。 | [⭐ 6.0K](https://github.com/NEKOparapa/AiNiee) |
| Duckfolio | 个人主页 | [⭐ 80](https://github.com/Yorlg/Duckfolio) |
| pansou | PanSou是一款高性能的网盘资源搜索API服务，支持TG频道和插件搜索。系统设计以性能和可扩展性为核心，支持多频道多插件并发搜索、结果智能排序和网盘类型分类。docker集成前后端，一键启动，开箱即用。仅供学习研究，请勿以各种形式用于盈利... | [⭐ 1.4W](https://github.com/fish2018/pansou) |
| idcard_generator- | 身份证图片生成工具-仅供学习交流。已打包Maocs app和Windows exe，可直接下载使用 | [⭐ 635](https://github.com/xiamuguizhi/idcard_generator-) |
| OpenList | A new AList Fork to Anti Trust Crisis<br>一个新的AList分叉，以对抗信任危机。 | [⭐ 2.4W](https://github.com/OpenListTeam/OpenList) |
| lucky | 软硬路由公网神器,ipv6/ipv4 端口转发,反向代理,DDNS,WOL,ipv4 stun内网穿透,cron,acme,rclone,ftp,webdav,filebrowser | [⭐ 8.0K](https://github.com/gdy666/lucky) |
| cherry-studio | AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs<br>AI生产力工作室，具备智能聊天、自主代理以及300多个助手功能。统一接入前沿大语言模型。 | [⭐ 4.9W](https://github.com/CherryHQ/cherry-studio) |
| Cloudflare-vless-t<br>rojan | CF-workers/pages代理脚本：支持Vless-ws(tls)、Trojan-ws(tls)；Socks5/http本地代理脚本：可选ECH-TLS、普通TLS、无TLS三种代理模式 | [⭐ 1.6W](https://github.com/yonggekkk/Cloudflare-vless-trojan) |
| portainer-ce | portainer-ce 2.33.x 中文汉化版docker镜像，支持X86、ARM、ARM64、Windows | [⭐ 937](https://github.com/eysp/portainer-ce) |
| hexhub | Hexhub 是一款开源的SSH、SFTP、数据库管理客户端，数据库管理模块目前还在开发之中 | [⭐ 467](https://github.com/EdikKing/hexhub) |
| PixivUserBatchDown<br>load | P站画师个人作品批量下载工具，UserScript + Aria2。可高度自定义重命名，发送到本地或远程(如路由器)下载。 | [⭐ 1.2K](https://github.com/Mapaler/PixivUserBatchDownload) |
| Remove-MS-Edge | Uninstall Microsoft Edge with an executable or batch script.<br>使用可执行文件或批处理脚本卸载 Microsoft Edge。 | [⭐ 5.3K](https://github.com/ShadowWhisperer/Remove-MS-Edge) |
| ecs | VPS 融合怪服务器测评项目 更推荐使用无环境依赖的Go版本 VPS Fusion Monster Server Test Script – More recommended to use the Go version with no... | [⭐ 7.1K](https://github.com/spiritLHLS/ecs) |
| bilijump-ai | 一个使用 AI 自动跳过 Bilibili 视频植入广告的扩展程序。 | [⭐ 422](https://github.com/qingmeng1/bilijump-ai) |
| ChatGPT-Next-Web-L<br>angChain | 一键拥有你自己的 ChatGPT 网页服务。 One-Click to deploy your own ChatGPT web UI.（基于 langchain 实现的插件版本 Plugin version implemented... | [⭐ 1.2K](https://github.com/Hk-Gosuto/ChatGPT-Next-Web-LangChain) |
| new-api | A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into...<br>一个统一的人工智能模型中心，用于聚合与分发。它支持将各种大语言模型相互转换为…… | [⭐ 4.3W](https://github.com/QuantumNous/new-api) |
| mtg | Highly opinionated MTPROTO proxy for Telegram<br>高度个性化的Telegram MTProto代理 | [⭐ 3.6K](https://github.com/9seconds/mtg) |
| Yunzai | Yunzai 应用端，支持多账号，支持协议端：go-cqhttp、ComWeChat、GSUIDCore、ICQQ、QQBot、QQ频道、微信、KOOK、Telegram、Discord | [⭐ 610](https://github.com/TimeRainStarSky/Yunzai) |
| Yunzai-Bot-plugins<br>-index | Yunzai-Bot云崽QQ机器人插件索引 | [⭐ 1.2K](https://github.com/yhArcadia/Yunzai-Bot-plugins-index) |
| LinkSwift | 一个基于 JavaScript 的网盘文件下载地址获取工具。基于【网盘直链下载助手】修改 ，支持 百度网盘 / 阿里云盘 / 中国移动云盘 / 天翼云盘 / 迅雷云盘 / 夸克网盘 / UC网盘 / 123云盘 八大网盘 | [⭐ 1.8W](https://github.com/hmjz100/LinkSwift) |
| telegram-msg-forwa<br>rder | 一个功能强大的Telegram机器人，能够转发指定链接的消息，支持随机消息获取和批量消息管理。 | [⭐ 57](https://github.com/cubezhao/telegram-msg-forwarder) |
| TelegramForwarder | 一个功能强大的 Telegram 消息转发器，支持多源转发、关键词过滤、正则替换、RSS订阅，AI处理，多平台推送等功能。 | [⭐ 1.2K](https://github.com/Heavrnl/TelegramForwarder) |
| ok-wuthering-waves | 鸣潮 后台自动战斗 自动刷声骸 一键日常 Automation for Wuthering Waves | [⭐ 6.8K](https://github.com/ok-oldking/ok-wuthering-waves) |
| MobaXterm-Chinese-<br>Simplified | MobaXterm 简体中文汉化版🌏🖥🖥🖥 【💌慢工精心制作，"提示"也汉化💻】 【😍控件布局精细调整】 | [⭐ 7.1K](https://github.com/RipplePiam/MobaXterm-Chinese-Simplified) |
| 3x-ui | Xray panel supporting multi-protocol multi-user expire day & traffic & IP limit (Vmess, Vless, Trojan, ShadowSocks,...<br>Xray面板支持多协议、多用户的到期日期、流量及IP限制（Vmess、Vless、Trojan、ShadowSocks等）。 | [⭐ 4.3W](https://github.com/MHSanaei/3x-ui) |
| IDM-Activation-Scr<br>ipt | An open source tool to activate and reset trial of Internet Download Manager<br>一个开源工具，用于激活和重置 Internet Download Manager 的试用期。 | [⭐ 7.7K](https://github.com/WindowsAddict/IDM-Activation-Script) |
| mc_auto_boss | 鸣潮后台自动刷BOSS声骸 没弃坑，程序已升级，请前往新项目 https://github.com/wakening/WutheringWavesAssistant | [⭐ 30](https://github.com/wakening/mc_auto_boss) |
| Bilibili-Evolved | 强大的哔哩哔哩增强脚本 | [⭐ 3.0W](https://github.com/the1812/Bilibili-Evolved) |
| tabby | A terminal for a more modern age<br>一个为更现代时代打造的终端 | [⭐ 7.3W](https://github.com/Eugeny/tabby) |
| WuWa-Configs | WuWa configs to improve visuals or performance<br>WuWa 配置以提升视觉效果或性能 | [⭐ 1.6K](https://github.com/AlteriaX/WuWa-Configs) |
| MingChaoSign | 鸣潮与社区签到 | [⭐ 8](https://github.com/Maojuan-lang/MingChaoSign) |
| mc_auto_boss | 鸣潮后台自动刷BOSS声骸 | [⭐ 734](https://github.com/lazydog28/mc_auto_boss) |
| MobileModels | 手机品牌型号汇总 ｜ Mobile Models ｜ This repository is licensed under CC BY-NC-SA 4.0 | [⭐ 4.3K](https://github.com/KHwang9883/MobileModels) |
| openwrt-Exclusive | 暂无描述 | [⭐ 192](https://github.com/firkerword/openwrt-Exclusive) |
| NetworkPanel | 测试您的网速，多出口查询您的ip地址 | [⭐ 958](https://github.com/ljxi/NetworkPanel) |
| guoba-plugin | Yunzai-Bot的插件，主要提供后台管理界面。 | [⭐ 237](https://github.com/guoba-yunzai/guoba-plugin) |
| Qsign | Windows的一键搭建签名api | [⭐ 192](https://github.com/touchscale/Qsign) |
| Miao-Yunzai | 喵版Yunzai-V3 | [⭐ 1.1K](https://github.com/yoimiya-kokomi/Miao-Yunzai) |
| waves-plugin | 基于 Yunzai 的鸣潮游戏数据查询插件 | [⭐ 326](https://github.com/erzaozi/waves-plugin) |
| nonebot-plugin-wut<br>heringwaves | NoneBot2 - 鸣潮签到机器人 - 库街区 | [⭐ 5](https://github.com/Night-stars-1/nonebot-plugin-wutheringwaves) |
| Yunzai-Kuro-Plugin | 一个库洛游戏 (战双&鸣潮) 的插件，适用于云崽Bot。 ｜ A Plugin of Kuro Games(Punshining Gray Raven & Wuthering Waves), adapt to Yunzai-Bot. | [⭐ 156](https://github.com/TomyJan/Yunzai-Kuro-Plugin) |
| Wuthering_Waves_Au<br>to | 鸣潮自动脚本 | [⭐ 30](https://github.com/linyys/Wuthering_Waves_Auto) |
| TTime | 🚀 Screenshots, word marking, OCR, AI, translation software ｜｜ 截图、划词、文字识别、AI、翻译软件 | [⭐ 3.3K](https://github.com/InkTimeRecord/TTime) |
| gpt_academic | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模... | [⭐ 7.1W](https://github.com/binary-husky/gpt_academic) |
| NextChat | ✨ Light and Fast AI Assistant. Support: Web ｜ iOS ｜ MacOS ｜ Android ｜ Linux ｜ Windows<br>✨ 轻量快速的人工智能助手。支持：Web ｜ iOS ｜ MacOS ｜ Android ｜ Linux ｜ Windows | [⭐ 8.9W](https://github.com/ChatGPTNextWeb/NextChat) |
| Are-u-ok | KoolCenter iStore .run Packages<br>KoolCenter iStore .run 软件包 | [⭐ 2.2K](https://github.com/bcseputetto/Are-u-ok) |
| WutheringWaves | Wuthering Waves ps (0.9.0)<br>《鸣潮》PS (0.9.0) | [⭐ 254](https://github.com/thexeondev/WutheringWaves) |
| Cimoc | 漫画阅读器 | [⭐ 3.8K](https://github.com/Haleydu/Cimoc) |
| hysteria | Hysteria is a powerful, lightning fast and censorship resistant proxy.<br>Hysteria 是一个功能强大、速度如闪电且抗审查的代理工具。 | [⭐ 2.2W](https://github.com/apernet/hysteria) |
| cook | 🍲 好的，今天我们来做菜！OK, Let's Cook! | [⭐ 6.5K](https://github.com/YunYouJun/cook) |
| Are-u-ok | 暂无描述 | [⭐ 1.4W](https://github.com/AUK9527/Are-u-ok) |
| vits-simple-api | A simple VITS HTTP API, developed by extending Moegoe with additional features.<br>一个简单的VITS HTTP API，通过扩展Moegoe并增加额外功能而开发。 | [⭐ 1.1K](https://github.com/Artrajz/vits-simple-api) |
| TTSModels | 暂无描述 | [⭐ 623](https://github.com/CjangCjengh/TTSModels) |
| Aoki | Mirai 一键登录处理器 (现已不可用于登录，请使用签名服务) | [⭐ 229](https://github.com/MrXiaoM/Aoki) |
| AstrBot | AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins and AI feature, and can...<br>AI智能体助手与开发框架，集成了众多即时通讯平台、大语言模型、插件及AI功能，并且可以…… | [⭐ 3.8W](https://github.com/AstrBotDevs/AstrBot) |
| kirara-ai | 🤖 可 DIY 的 多模态 AI 聊天机器人 ｜ 🚀 快速接入 微信、 QQ、Telegram、等聊天平台 ｜ 🦈支持DeepSeek、Grok、Claude、Ollama、Gemini、OpenAI ｜... | [⭐ 1.9W](https://github.com/lss233/kirara-ai) |
| chatbox | Powerful AI Client<br>强大的AI客户端 | [⭐ 4.1W](https://github.com/chatboxai/chatbox) |
| auto_wjx | 不会有人连问卷星都要弄虚作假吧 | [⭐ 5](https://github.com/Lihewin/auto_wjx) |
| chatGPTBox | Integrating ChatGPT into your browser deeply, everything you need is here<br>将ChatGPT深度集成到您的浏览器中，一切所需尽在其中。 | [⭐ 1.1W](https://github.com/ChatGPTBox-dev/chatGPTBox) |
| qBittorrent-Enhanc<br>ed-Edition | [Unofficial] qBittorrent Enhanced, based on qBittorrent<br>[非官方] qBittorrent 增强版，基于 qBittorrent | [⭐ 2.6W](https://github.com/c0re100/qBittorrent-Enhanced-Edition) |
| warp.sh | Cloudflare WARP Installer ｜ WARP 一键安装脚本 | [⭐ 3.9K](https://github.com/P3TERX/warp.sh) |
| docker.ui | 暂无描述 | [⭐ 809](https://github.com/gohutool/docker.ui) |
| chatgpt-web | Pure Javascript ChatGPT demo based on OpenAI API<br>基于OpenAI API的纯JavaScript ChatGPT演示 | [⭐ 1.0K](https://github.com/xqdoo00o/chatgpt-web) |
| chatgpt-web | 基于ChatGPT3.5 API实现的私有化web程序 | [⭐ 3.1K](https://github.com/869413421/chatgpt-web) |
| chatgptProxyAPI | 🔥 使用cloudflare 搭建免费的 OpenAI api代理 ，解决网络无法访问问题。支持流式输出 | [⭐ 3.0K](https://github.com/x-dr/chatgptProxyAPI) |
| Movie_Data_Capture | Local Movies Organizer<br>本地电影管理器 | [⭐ 7.4K](https://github.com/mvdctop/Movie_Data_Capture) |
| qb_rclone | A personal testing record.<br>个人测试记录。 | [⭐ 23](https://github.com/feodorren/qb_rclone) |
| Anime-Repository | Elegant Smart Scraper<br>优雅智能爬虫 | [⭐ 211](https://github.com/Chikage0o0/Anime-Repository) |
| awesome-chatgpt-ap<br>i | Curated list of apps and tools that not only use the new ChatGPT API, but also allow users to configure their own API...<br>精选的应用和工具列表，这些应用和工具不仅使用了新的ChatGPT API，而且允许用户配置自己的API... | [⭐ 6.4K](https://github.com/reorx/awesome-chatgpt-api) |
| nextai-translator | 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用 - Browser extension and cross-platform desktop application for translation based on... | [⭐ 2.5W](https://github.com/nextai-translator/nextai-translator) |
| ChuanhuChatGPT | GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a...<br>ChatGPT API 和多个大语言模型的图形用户界面。支持代理、基于文件的问答、GPT 微调以及带网页搜索的查询。所有这一切都通过一个…… | [⭐ 1.5W](https://github.com/GaiZhenbiao/ChuanhuChatGPT) |
| AVDC | 日本电影元数据刮削器，配合kodi,emby,plex等本地媒体管理工具使用。可批量抓取，也可单个抓取。可抓取子目录下视频，多集视频（-cd1/-cd2）,带字幕作品（-c., -C.）。批量添加emby演员头像。 | [⭐ 2.7K](https://github.com/moyy996/AVDC) |
| vertex | 适用于 PT 玩家的追剧刷流一体化综合管理工具 | [⭐ 1.8K](https://github.com/vertex-app/vertex) |
| Umi-OCR | OCR software, free and offline. 开源、免费的离线OCR软件。支持截屏/批量导入图片，PDF文档识别，排除水印/页眉页脚，扫描/生成二维码。内置多国语言库。 | [⭐ 4.6W](https://github.com/hiroi-sora/Umi-OCR) |
| ChineseSubFinder | 自动化中文字幕下载。字幕网站支持 shooter、xunlei、arrst、a4k、SubtitleBest 。支持 Emby、Jellyfin、Plex、Sonarr、Radarr、TMM | [⭐ 3.9K](https://github.com/ChineseSubFinder/ChineseSubFinder) |
| CasaOS | CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud system.<br>CasaOS - 一个简单、易用、优雅的开源个人云系统。 | [⭐ 3.7W](https://github.com/IceWhaleTech/CasaOS) |
| nas-tools | NAS媒体库管理工具 | [⭐ 9.0K](https://github.com/NAStool/nas-tools) |
| nas-tools | A fork of NAStool/nas-tools:2.9.1<br>NAStool/nas-tools:2.9.1 的一个分支 | [⭐ 495](https://github.com/receyuki/nas-tools) |
| WindTerm | A professional cross-platform SSH/Sftp/Shell/Telnet/Tmux/Serial terminal.<br>一款专业的跨平台SSH/SFTP/Shell/Telnet/Tmux/串行终端。 | [⭐ 3.2W](https://github.com/kingToolbox/WindTerm) |
| Ehviewer_CN_SXJ | ehviewer，用爱发电，快乐前行 | [⭐ 2.6W](https://github.com/xiaojieonly/Ehviewer_CN_SXJ) |
| JdBuyer | 京东抢购自动下单助手，GUI 支持 Windows 和 macOS | [⭐ 4.2K](https://github.com/zas023/JdBuyer) |
| QLDependency | 青龙面板全依赖一键安装脚本 / Qinglong Pannel Dependency Install Scripts. | [⭐ 2.2K](https://github.com/FlechazoPh/QLDependency) |
| Android-DataBackup | DataBackup for Android 7.0+<br>适用于 Android 7.0 及以上版本的数据备份 | [⭐ 7.1K](https://github.com/XayahSuSuSu/Android-DataBackup) |
| HelloGitHub | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. | [⭐ 16.7W](https://github.com/521xueweihan/HelloGitHub) |
| linux-command | Linux命令大全搜索工具，内容包含Linux命令手册、详解、学习、搜集。https://git.io/linux | [⭐ 3.6W](https://github.com/jaywcjlove/linux-command) |
| qinglong | 支持 Python3、JavaScript、Shell、Typescript 的定时任务管理平台（Timed task management platform supporting Python3, JavaScript, Shell,... | [⭐ 2.0W](https://github.com/whyour/qinglong) |
| Bulk-Crap-Uninstal<br>ler | Remove large amounts of unwanted applications quickly.<br>快速删除大量不需要的应用程序。 | [⭐ 2.0W](https://github.com/BCUninstaller/Bulk-Crap-Uninstaller) |
| NeverIdle | 资源定期浪费，可用于 Oracle 甲骨文保活。 | [⭐ 968](https://github.com/layou233/NeverIdle) |
| Cloud-N1-OpenWrt | Github Actions 自动编译 OpenWrt 固件（适配 Phicomm N1） | [⭐ 317](https://github.com/huangqian8/Cloud-N1-OpenWrt) |
| Kwrt | openwrt 软路由固件 | [⭐ 9.0K](https://github.com/kiddin9/Kwrt) |
| small-package | 自动同步更新上游库软件 | [⭐ 1.7K](https://github.com/kenzok8/small-package) |
| telegram_channel_d<br>ownloader | telegram chanle file(image,video,file``) donnload<br>电报频道文件（图片、视频、文件）下载 | [⭐ 68](https://github.com/kuaizi/telegram_channel_downloader) |
| music | 音乐搜索器 - 多站合一音乐搜索解决方案 | [⭐ 2.1K](https://github.com/maicong/music) |
| epic-awesome-gamer | 🍷 Gracefully claim weekly free games and monthly content from Epic Store.<br>🍷 优雅地领取Epic商店每周免费游戏和每月内容。 | [⭐ 1.1K](https://github.com/QIN2DIM/epic-awesome-gamer) |
| ChatGPT | ❄️ ChatGPT Desktop Application (Mac, Windows and Linux)<br>❄️ ChatGPT桌面应用程序（Mac、Windows和Linux） | [⭐ 5.4W](https://github.com/lencx/ChatGPT) |
| BiliBiliToolPro | B 站（bilibili）自动任务工具，支持docker、青龙、k8s等多种部署方式。全面拥抱AI。敏感肌也能用。 | [⭐ 8.8K](https://github.com/RayWangQvQ/BiliBiliToolPro) |
| Doprax-Xray | Doprax一键五协议共存脚本：Xray内核，支持vless，vmess，trojan，shadowsocks，socks五协议同时在线，支持Cloudflare Argo隧道自动生成分享链接 | [⭐ 1.4K](https://github.com/yonggekkk/Doprax-Xray) |
| ms-ra-forwarder | 暂无描述 | [⭐ 93](https://github.com/rogueme/ms-ra-forwarder) |
| java_oci_manage | Web SSH Smart Terminal for multi-cloud management (OCI / AWS / GCP / Azure / DO / SolusVM /VirtFusion), with cloud...<br>用于多云管理的 Web SSH 智能终端（OCI / AWS / GCP / Azure / DO / SolusVM / VirtFusion），带有云... | [⭐ 2.0K](https://github.com/semicons/java_oci_manage) |
| autoplan | 这是一个自动化的托管系统，目前支持bilibili，米游社原神星铁等签到 | [⭐ 673](https://github.com/wyt1215819315/autoplan) |
| HowToCook | Programmer's guide about how to cook at home.<br>程序员居家烹饪指南 | [⭐ 10.1W](https://github.com/Anduin2017/HowToCook) |
| alist | 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用... | [⭐ 5.0W](https://github.com/AlistGo/alist) |
| trojan-go | Go实现的Trojan代理，支持多路复用/路由功能/CDN中转/Shadowsocks混淆插件，多平台，无依赖。A Trojan proxy written in Go. An unidentifiable mechanism that... | [⭐ 8.4K](https://github.com/p4gefau1t/trojan-go) |
| trojan | trojan多用户管理部署程序, 支持web页面管理 | [⭐ 5.7K](https://github.com/Jrohy/trojan) |
| luci-app-cloudflar<br>e-ip | OpenWrt Cloudflare IP 优选工具 - 自动测速优选 Cloudflare IP 并更新 PassWall/OpenClash 节点，支持 LuCI Web 界面、定时任务、CFST 自动下载与自更新 | [⭐ 37](https://github.com/hello-yunshu/luci-app-cloudflare-ip) |
| Multi-EasyGost | 致力于最简单好用的GOST小白脚本 | [⭐ 1.9K](https://github.com/KANIKIG/Multi-EasyGost) |
| freenom | Freenom 域名自动续期。Freenom domain name renews automatically. | [⭐ 3.3K](https://github.com/luolongfei/freenom) |
| x-ui | 支持多协议多用户的 xray 面板 | [⭐ 1.9W](https://github.com/vaxilu/x-ui) |
| openwrt-packages | openwrt常用软件包 | [⭐ 7.2K](https://github.com/kenzok8/openwrt-packages) |
| lede | Lean's LEDE source<br>Lean 的 LEDE 源码 | [⭐ 3.2W](https://github.com/coolsnowwolf/lede) |
| Actions-OpenWrt | A template for building OpenWrt with GitHub Actions ｜ 使用 GitHub Actions 在线云编译 OpenWrt 固件 | [⭐ 7.6K](https://github.com/P3TERX/Actions-OpenWrt) |
| aria2.sh | Aria2 一键安装管理脚本 增强版 | [⭐ 3.0K](https://github.com/P3TERX/aria2.sh) |
| My-Actions | 爱奇艺会员,腾讯视频,哔哩哔哩,百度,各类签到 | [⭐ 510](https://github.com/MayoBlueSky/My-Actions) |
| python_sign | 联通营业厅签到,GLaDOS签到,腾讯视频签到,CSDN签到,每日新闻生成,掘金签到抽奖,邮件批量发送,leetcode每日一题,线报推送,更多脚本正在开发中! | [⭐ 262](https://github.com/wangwangit/python_sign) |
| TrackersListCollec<br>tion | 🎈 Updated daily! A list of popular BitTorrent Trackers! / 每天更新！全网热门 BT Tracker 列表！ | [⭐ 3.2W](https://github.com/XIU2/TrackersListCollection) |
| dnsmasq_sniproxy_i<br>nstall | One-click Install and Configure Dnsmasq and Sniproxy for CentOS/Debian/Ubuntu<br>为CentOS/Debian/Ubuntu一键安装并配置Dnsmasq和Sniproxy | [⭐ 1.4K](https://github.com/myxuchangbin/dnsmasq_sniproxy_install) |
| dnsunblocknetflix | dns解锁netflix 一键修改dns无脑脚本 | [⭐ 21](https://github.com/DayoWong0/dnsunblocknetflix) |
| netflix-proxy | Smart DNS proxy to watch Netflix<br>智能DNS代理观看Netflix | [⭐ 3.7K](https://github.com/ab77/netflix-proxy) |
| SSTAP_ip_crawl_too<br>l | 一个自动获取游戏远程ip，并自动写成SSTAP/NETCH规则文件的脚本 | [⭐ 673](https://github.com/oooldtoy/SSTAP_ip_crawl_tool) |
| qiandao | 签到 | [⭐ 3.4K](https://github.com/binux/qiandao) |

---
<div align='right'>⬆ <a href='#top'>回到顶部</a></div>