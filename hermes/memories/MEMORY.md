文档管线：笔记本 Ethan(100.86.148.56) E:\百度云同步盘\工作台账\ → 基地 ~/工作台账/（3726份2.49GB不含PPT）。周末SSH+rsync同步（Tailscale DERP中继TCP双向不通，需直连）。脚本：sync_taizhang.sh + weekly_scan.py。笔记本已装OpenSSH Server、免密密钥待配。
§
用户原则：1.隐私保护 2.事实核查不编创 3.文件操作限 /home/miao/工作台账/ 4.自主执行不等命令 5.正确时反对拿证据 6.主动提醒未推工作。+长任务主动汇报、完成后主动验证，安静=失职。
§
Dashboard WebSocket 反复断的根因：systemd 服务 `/etc/systemd/system/hermes-dashboard.service` 以随机 token 启动，与固定 token 文件不一致导致 Desktop 发送失败。修法：`sudo systemctl stop/disable hermes-dashboard.service`，再手动 `HERMES_DASHBOARD_SESSION_TOKEN=... hermes dashboard --port 9119`。watchdog 脚本在 `~/.hermes/scripts/dashboard_watchdog.sh` 每分钟检测自恢复。
§
html-video (nexu-io) 已部署在基地 /home/miao/html-video/，22 模板，Hyperframes 引擎，Hermes Agent 驱动。Studio 端口 3071（已 patch 为 0.0.0.0），通过 Tailscale http://100.86.13.11:3071 远程访问。启动命令：export PATH="/home/miao/.hermes/node/bin:$PATH" && cd /home/miao/html-video && node packages/cli/dist/bin.js studio --port 3071。pnpm 在 /home/miao/.hermes/node/bin/pnpm。
§
多角色AI团队：default=我(总负责)；wenan=文案；jike=极客；lvyou=旅游；zhidu=制度；sheji=设计师(海报/修图/视觉)出图→/home/miao/出图/。路由：wenan←报告/方案/公文；lvyou←行程/旅游/美食；jike←脚本/代码/运维；zhidu←制度/考核；sheji←海报/设计/修图/封面/视觉。Cron：台账扫描周一9:00(wenan)、月报25日9:00(wenan)、意识形态季末25日9:00(wenan)
§
贵州自驾v4(2026.06.08定):7.18-25一家三口南京⇌贵阳。环线:贵阳→安顺→黄果树(西门三核心)→织金洞→乌蒙草原→遵义→茅台→赤水(2晚深度)→贵阳。Day4最长3.5h。~1350km,人均3100-5000元。预约:黄果树7.19西门/织金洞7.20/遵义会址7.21。偏好:1大床+1双床≥1.35m,新酒店优先,不推狗肉,先紧后松。HTML:/home/miao/贵州自驾游-v4.html
§
搜索默认用 AnySearch（~/.hermes/skills/anysearch/，v2.1.0）。CLI：python3 ~/.hermes/skills/anysearch/scripts/anysearch_cli.py search "query" -m N。支持 search/batch_search/extract/get_sub_domains。匿名模式可用，不再用其他搜索方式。
§
iLink微信出站单向限流，cron执行成功但微信投递失败。解决方案：每日待办(09:00)→微信；全链路自检(00:00/12:00)→飞书；每日灾备(08:10)→飞书；每日简报(08:30)→飞书。飞书无此限流。
§
HA备忘：Dreame X50 Ultra增强版用Dreamehome App独立云(非米家生态)，无miio/第三方/现成HA集成。haier国内版需client_id+refresh_token，海外hon(Andre0512/hon)支持账号密码直登含烤箱/净水。WiFi双频：1804-5G(基地)、1804(IoT)。鸿蒙HA原生App。
§
GitHub git协议（SSH/HTTPS）全被墙，仅HTTP可达。ghproxy.net已配git代理但smart HTTP仍断。灾备脚本走本地tar兜底(~/.hermes/scripts/hermes_backup.sh)。Chrome 149装于~/apps/chrome/，headless正常，Hermes browser工具已启用。SSH key已生成未加GitHub。