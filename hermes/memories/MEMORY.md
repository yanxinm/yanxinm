文档管线：笔记本 Ethan(100.86.148.56) E:\百度云同步盘\工作台账\ → 基地 ~/工作台账/（3726份2.49GB不含PPT）。周末SSH+rsync同步（Tailscale DERP中继TCP双向不通，需直连）。脚本：sync_taizhang.sh + weekly_scan.py。笔记本已装OpenSSH Server、免密密钥待配。
§
用户原则：1.隐私保护 2.事实核查不编创 3.文件操作限 /home/miao/工作台账/ 4.自主执行不等命令 5.正确时反对拿证据 6.主动提醒未推工作。+长任务主动汇报、完成后主动验证，安静=失职。
§
html-video (nexu-io) 已部署在基地 /home/miao/html-video/，22 模板，Hyperframes 引擎，Hermes Agent 驱动。Studio 端口 3071（已 patch 为 0.0.0.0 允许远程访问）。启动命令：export PATH="/home/miao/.hermes/node/bin:$PATH" && cd /home/miao/html-video && node packages/cli/dist/bin.js studio --port 3071。pnpm 在 /home/miao/.hermes/node/bin/pnpm。注意：Studio 进程偶尔会僵住（Chromium/playwright 后台初始化卡住），卡住时 kill 掉重启即可。
§
多角色AI团队：default=我(总负责)；wenan=文案；jike=极客；lvyou=旅游；zhidu=制度；sheji=设计师(海报/修图/视觉)出图→/home/miao/出图/。路由：wenan←报告/公文；lvyou←行程/美食；jike←脚本/运维；zhidu←制度/考核；sheji←设计/修图。
§
搜索默认用 AnySearch（~/.hermes/skills/anysearch/，v2.1.0）。CLI：python3 ~/.hermes/skills/anysearch/scripts/anysearch_cli.py search "query" -m N。支持 search/batch_search/extract/get_sub_domains。匿名模式可用，不再用其他搜索方式。
§
灾备/备份类cron任务（hermes_backup.sh等）一旦报错必须主动查修，不等用户提醒。发现问题直接修，修完验证通过再汇报。
§
GitHub全墙(SSH/HTTPS git不可用,仅HTTP)。灾备走本地tar(~/.hermes/scripts/hermes_backup.sh)。Codex CLI用apikey.fun+echobird(:53682)，bwrap需apparmor_restrict_unprivileged_userns=0。Chrome 149 ~/apps/chrome/ headless正常。SSH key已生成未加GitHub。
§
智能家居自动路由：无论当前profile，老缪在微信/飞书发家居指令时直接执行。识别词：温度/湿度/空气质量、扫地/机器人/回充/清扫、窗帘/开关/打开关闭、灯/灯光、空调/制冷/制热、家电状态。全部走HA API(localhost:8123,token→~/.ha_token)。dreame扫地机用dreame_vacuum集成(Dreamehome云)。
§
Hermes Provider配置铁律:GLM用内置`zai`(非`custom:zhipu`)。`${GLM_API_KEY}`不解析须硬编码。在providers.zhipu段直接写完整key值。WebUI灰按钮+模型下拉空=provider/config问题。Gateway restart因drain挂住→`sudo kill -9 PID`。
§
Jellyfin:8097（端口被Tailscale占用，从8096改为8097）。媒体目录 /home/miao/1tb-data/nas/media/movies/ 已挂载到容器。
§
用户偏好：能用现有系统就不重装。换OS代价大，优先在现有Ubuntu+Docker基础上扩展。
§
HomeKit Bridge 防火墙配置：需要开放 21064-21070/tcp（HomeKit Bridge 端口）和 5353/udp（mDNS/Bonjour）。ufw 命令：sudo ufw allow 21064:21070/tcp comment 'HomeKit Bridge' && sudo ufw allow 5353/udp comment 'mDNS'