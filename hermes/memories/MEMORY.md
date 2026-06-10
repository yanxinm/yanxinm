文档管线：笔记本 Ethan(100.86.148.56) E:\百度云同步盘\工作台账\ → 基地 ~/工作台账/（3726份2.49GB不含PPT）。周末SSH+rsync同步（Tailscale DERP中继TCP双向不通，需直连）。脚本：sync_taizhang.sh + weekly_scan.py。笔记本已装OpenSSH Server、免密密钥待配。
§
用户原则（6条）：1.隐私保护。2.事实核查—全网搜索不编创。3.文件操作限工作台账目录（基地本地副本 /home/miao/工作台账/，源在笔记本 E:\百度云同步盘\工作台账\）。4.自主执行者+思考伙伴，不等命令。5.正确时大胆反对，拿出证据。6.主动提醒长期未推的工作、主动改进不好用的材料。
§
用户明确要求：长时间运行的任务必须定期主动汇报进度，任务完成后必须主动输出验证结果，不能等用户来问。安静不报=失职。
§
基地M710q: Ubuntu22.04 GNOME/Docker/Tailscale 100.86.13.11，家里局域网IP常见为192.168.1.42。Hermes Desktop/Dashboard 走 9119，Tailscale Funnel 根路径 `/` 必须只给 Hermes；HomeAssistant 必须另走 `/ha` 或独立入口，不要混。Desktop 网页能开但提示词发不出时，优先查 Dashboard session token/客户端缓存和 `/api/ws` WebSocket；单位网络可能拦 WebSocket/Tailscale，家里可用 `http://192.168.1.42:9119` 直连验证。apikey-fun gpt-5.5 CLI 已验证可用。
§
html-video (nexu-io) 已部署在基地 /home/miao/html-video/，22 模板，Hyperframes 引擎，Hermes Agent 驱动。Studio 端口 3071（已 patch 为 0.0.0.0），通过 Tailscale http://100.86.13.11:3071 远程访问。启动命令：export PATH="/home/miao/.hermes/node/bin:$PATH" && cd /home/miao/html-video && node packages/cli/dist/bin.js studio --port 3071。pnpm 在 /home/miao/.hermes/node/bin/pnpm。
§
多角色团队（2026-06-08落地）：总负责=我(default)；文案=wenan profile(公文/方案/报告)；极客=jike profile(工具/编程/运维)；旅游定制师=lvyou profile(行程/记账)；制度规划师=zhidu profile(制度/考核/规章)。
路由规则：含"报告/策划/方案/请示/公文/意识形态/台账"→wenan；"行程/旅游/酒店/记账/美食"→lvyou；"脚本/Python/部署/LoRA/代码/运维/报错"→jike；"制度/考核/管理办法/安全制度/规章"→zhidu。
Kanban已初始化。Cron：台账扫描每周一9:00(wenan)、月度报告提醒25日9:00(wenan)、意识形态提醒季末25日9:00(wenan)。
§
贵州自驾v4(2026.06.08定):7.18-25一家三口南京⇌贵阳。环线:贵阳→安顺→黄果树(西门三核心)→织金洞→乌蒙草原→遵义→茅台→赤水(2晚深度)→贵阳。Day4最长3.5h。~1350km,人均3100-5000元。预约:黄果树7.19西门/织金洞7.20/遵义会址7.21。偏好:1大床+1双床≥1.35m,新酒店优先,不推狗肉,先紧后松。HTML:/home/miao/贵州自驾游-v4.html
§
搜索默认用 AnySearch（~/.hermes/skills/anysearch/，v2.1.0）。CLI：python3 ~/.hermes/skills/anysearch/scripts/anysearch_cli.py search "query" -m N。支持 search/batch_search/extract/get_sub_domains。匿名模式可用，不再用其他搜索方式。
§
HA社区：6/9已加Xiaomi Miot(21设备)；Midea AC LAN v0.3.22兼容补丁(常量+server类型)已打但一体机本地握手失败(online:false)；Dreame已解决py_mini_racer桩。待加：haier/hon、treeow。老缪偏好API操作。