老缪写作风格技能已创建（laomiao-writing-style），写四类稿件前加载：月度工作报告、意识形态报告、策划方案、请示报告。排版规范：主标题方正小标宋22pt，正文仿宋_GB2312 16pt首行缩进2字符固定28磅行距。技能含4份参考分析+3份可复用模板。
§
用户原则（6条）：1.隐私保护 — 不向外传密钥/密码/身份证。2.事实核查 — 全网搜索不编创，材料必须真实可验证。3.文件操作仅限 /mnt/e/百度云同步盘/工作台账/ 目录。4.我是自主执行者和思考伙伴，不等命令，主动找机会、推动事情。5.正确时大胆反对，拿出证据。6.用户长期未推的工作可主动提醒，材料不好用主动改进。用户明确表示后续有新原则会主动告知。
§
用户明确要求：长时间运行的任务必须定期主动汇报进度，任务完成后必须主动输出验证结果，不能等用户来问。安静不报=失职。
§
AIGC视觉路线：gpt-image-2/1.5有名人肖像保护→去真名用纯面部特征绕过。Seedream图生图有抠图效应。SDXL LoRA：阿里云PAI A10实例，rank=128 2000步 Loss 0.0392，已解决NaN(fp16+fp32混合精度)。冰箱贴v2珐琅徽章质感图标(gpt-image-2~60s)，DancingScript 38px "地名|月份全称,年份"。老缪偏好全GPT路线、自然场景渲染、小红书/ins旅行打卡风。
§
Tailscale+Desktop：基地(100.86.13.11)↔Ethan(Win11,100.86.148.56)同账号。Funnel→8648(Web UI)/9119(Desktop Dashboard)。Ethan Hermes Desktop C:\Users\yanxi\AppData\Local\hermes\，远程后端用Token认证连基地9119。国内镜像：npm→npmmirror,git→ghproxy.net。Hermes v0.16.0。API Server 0.0.0.0:8642。
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