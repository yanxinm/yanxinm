文档管线：笔记本 Ethan(100.86.148.56) E:\百度云同步盘\工作台账\ → 基地 ~/工作台账/（3726份2.49GB不含PPT）。周末SSH+rsync同步（Tailscale DERP中继TCP双向不通，需直连）。脚本：sync_taizhang.sh + weekly_scan.py。笔记本已装OpenSSH Server、免密密钥待配。
§
用户原则：1.隐私保护 2.事实核查不编创 3.文件操作限 /home/miao/工作台账/ 4.自主执行不等命令 5.正确时反对拿证据 6.主动提醒未推工作。+长任务主动汇报、完成后主动验证，安静=失职。
§
Dashboard WebSocket 反复断的根因：systemd 服务 `/etc/systemd/system/hermes-dashboard.service` 以随机 token 启动，与固定 token 文件不一致导致 Desktop 发送失败。修法：`sudo systemctl stop/disable hermes-dashboard.service`，再手动 `HERMES_DASHBOARD_SESSION_TOKEN=... hermes dashboard --port 9119`。watchdog 脚本在 `~/.hermes/scripts/dashboard_watchdog.sh` 每分钟检测自恢复。
§
html-video (nexu-io) 已部署在基地 /home/miao/html-video/，22 模板，Hyperframes 引擎，Hermes Agent 驱动。Studio 端口 3071（已 patch 为 0.0.0.0），通过 Tailscale http://100.86.13.11:3071 远程访问。启动命令：export PATH="/home/miao/.hermes/node/bin:$PATH" && cd /home/miao/html-video && node packages/cli/dist/bin.js studio --port 3071。pnpm 在 /home/miao/.hermes/node/bin/pnpm。
§
多角色AI团队：default=我(总负责)；wenan=文案；jike=极客；lvyou=旅游；zhidu=制度；sheji=设计师(海报/修图/视觉)出图→/home/miao/出图/。路由：wenan←报告/公文；lvyou←行程/美食；jike←脚本/运维；zhidu←制度/考核；sheji←设计/修图。
§
贵州自驾v4(7.18-25):一家三口南京⇌贵阳环线(织金洞+赤水丹霞+黄果树+乌蒙+茅台+遵义),~1350km,人均3100-5000。偏好1大床+1双床≥1.35m,新酒店优先。HTML:/home/miao/贵州自驾游-v4.html
§
搜索默认用 AnySearch（~/.hermes/skills/anysearch/，v2.1.0）。CLI：python3 ~/.hermes/skills/anysearch/scripts/anysearch_cli.py search "query" -m N。支持 search/batch_search/extract/get_sub_domains。匿名模式可用，不再用其他搜索方式。
§
Cron投递已切回微信(不飞书): 每日简报/灾备/全链路自检→微信。jike的零点自检+简报→微信。Tailscale确认为远程方案(UU远程被否)。笔记本通过100.86.13.11访问基地WebUI(:8648)和API(:8642)。HA在基地Docker运行(:8123)，dreame_vacuum已修复(auth_key刷新+config注入绕过MQTT超时)。
§
GitHub全墙(SSH/HTTPS git不可用,仅HTTP)。灾备走本地tar(~/.hermes/scripts/hermes_backup.sh)。Codex CLI用apikey.fun+echobird(:53682)，bwrap需apparmor_restrict_unprivileged_userns=0。Chrome 149 ~/apps/chrome/ headless正常。SSH key已生成未加GitHub。
§
智能家居自动路由：无论当前profile，老缪在微信/飞书发家居指令时直接执行。识别词：温度/湿度/空气质量、扫地/机器人/回充/清扫、窗帘/开关/打开关闭、灯/灯光、空调/制冷/制热、家电状态。全部走HA API(localhost:8123,token→~/.ha_token)。dreame扫地机用dreame_vacuum集成(Dreamehome云)。