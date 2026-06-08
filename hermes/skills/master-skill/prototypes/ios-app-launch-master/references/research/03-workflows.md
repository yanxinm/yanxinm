# Track 03 — Workflows (iOS App Store Launch — global + zh-CN supplement)

> Phase 1 wave 2. 8 workflows: ship 0→1 / rejection 救火 / ASO / 海外隐私合规 / 国内合规 / 多区策略 / 订阅付费 / 持续维护. 学派 DNA (Apple 官方 / 海外 indie / 大厂 release engineering / ASO 优化派 / 国内合规派 / 反 Apple) 在每条 workflow 显式标注. Wave 1 5 轨贡献 ≈ 28 个 seed, web search 补 12 个 2026 anchor. 时效衰减极快: 8 workflow 中 5 个 high decay, Apple 政策 12 月内多次微调.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review/ | verified_primary | 2026-05-04 | Apple Developer | App Review submission overview |
| T03-S002 | https://developer.apple.com/news/upcoming-requirements/ | verified_primary | 2026-05-04 | Apple Developer | iOS 26 SDK 强制 (2026-04-28) + age rating 强制 (2026-01-31) |
| T03-S003 | https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/ | verified_primary | 2026-05-04 | Apple Developer | Phased release 7-day rollout (1/2/5/10/20/50/100%) |
| T03-S004 | https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/ | verified_primary | 2026-05-04 | Apple Developer | TestFlight 100 internal / 10000 external + Beta App Review |
| T03-S005 | https://developer.apple.com/news/?id=pvszzano | verified_primary | 2026-05-04 | Apple Developer | Privacy Manifest 2024-05-01 强制 |
| T03-S006 | https://developer.apple.com/support/dma-and-apps-in-the-eu/ | verified_primary | 2026-05-04 | Apple Developer | DMA EU 分发 + CTC 2026-01 (5% 替代 €0.50 CTF) |
| T03-S007 | https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/ | verified_primary | 2026-05-04 | RevenueCat | State of Subs 2026: hard paywall 10.7% vs freemium 2.1% |
| T03-S008 | https://www.revenuecat.com/blog/growth/apple-anti-steering-ruling-monetization-strategy/ | verified_primary | 2026-05-04 | RevenueCat | Anti-steering 2025-04 ruling 实操 |
| T03-S009 | https://9to5mac.com/2025/05/01/apple-app-store-guidelines-external-links/ | secondary | 2026-05-04 | 9to5Mac | Apple ARG 25-05 link-out 改写 |
| T03-S010 | https://www.apptweak.com/en/aso-blog/guide-to-custom-product-pages-cpp | surrogate_primary | 2026-05-04 | AppTweak | CPP 2026: 35→70 槽位 + keyword 绑定 (vendor docs) |
| T03-S011 | https://adapty.io/blog/in-app-events-protect-organic-apple-search-ads/ | verified_primary | 2026-05-04 | Adapty | In-App Events 2026 防御 ASA 双广告位 |
| T03-S012 | https://huhuhang.com/post/apps/appstore-china-icp-filing | surrogate_primary | 2026-05-04 | 胡涵 | ICP 备案实操长文 (figure-owned 升级) (vendor docs) |
| T03-S013 | https://www.cac.gov.cn/2026-03/17/c_1775482074695536.htm | verified_primary | 2026-05-04 | 国家网信办 | 生成式 AI 备案公告 (2026-Q1 累计 800+) |
| T03-S014 | https://www.runway.team/blog/how-to-set-up-a-ci-cd-pipeline-for-your-ios-app-fastlane-github-actions | verified_primary | 2026-05-04 | Runway | Fastlane + GHA mac runner pipeline |
| T03-S015 | https://twinr.dev/blogs/apple-app-store-rejection-reasons-2025/ | secondary | 2026-05-04 | twinr | 2025 拒审 top reasons + 修复 |
| T03-S016 | https://adapty.io/blog/app-store-rejection/ | secondary | 2026-05-04 | Adapty | 拒审分类 + Resolution Center 实操 |
| T03-S017 | https://capgo.app/blog/privacy-manifest-for-ios-apps/ | verified_primary | 2026-05-04 | Capgo | Privacy Manifest + ITMS-91061/91065 (12% 拒审) |
| T03-S018 | https://blog.p2hp.com/archives/11713 | verified_primary | 2026-05-04 | Lenix | 2024 国内 8 大市场上架全流程 |
| T03-S019 | https://podcasts.apple.com/cn/podcast/%E7%A1%AC%E5%9C%B0%E9%AA%87%E5%AE%A2/id1678465783 | verified_primary | 2026-05-04 | 硬地骇客 | 国内 indie 出海 (RevenueCat/ASO/备案多集) |
| T03-S020 | https://world.hey.com/dhh/apple-rejects-the-hey-calendar-from-their-app-store-4316dc03 | secondary | 2026-05-04 | DHH | Hey Calendar 24-01 拒审长文 + 公开战 |
| T03-S021 | https://marco.org/2014/12/09/get-the-word-out | surrogate_primary | 2026-05-04 | Marco Arment | Launcher 拒审长文 (figure-owned) (vendor docs) |

> 一手率: 12/21 verified_primary + 4/21 surrogate_primary = **76%** 一手. 跨 Wave 1 引用厚度叠加. 黑名单 0 条.

---

## 总览 (按 decay risk 分组)

| # | Workflow | Decay | Trigger | Output | Last_updated | 资深差异 |
|---|----------|-------|---------|--------|--------------|---------|
| W1 | 上架 0→1 主流程 | high | 决定做 iOS app + Apple Dev 注册 | Ready for Sale | 2026-04 (iOS 26 SDK) | skip+optimize+add |
| W2 | Rejection 救火 | high | ASC Resolution Center 收到拒绝 | 重提通过 / 公开战 | 2026-Q1 | skip+optimize+add |
| W3 | ASO 优化主流程 | high | 上架前 4-6 周 / 季度迭代 | 关键词 ranking + CVR | 2026-Q2 (CPP organic + 多 ASA slot) | skip+optimize+add |
| W4 | 隐私 / 合规 (海外栈) | medium | SDK 集成 / EU/CA 用户 | xcprivacy + nutrition + ATT + GDPR | 2025-02 (SDK signed) | optimize+add |
| W5 | 国内合规 | medium | 国区上架 / 大陆运营 / 出海 | ICP + 算法备案 + 多市场 | 2026-Q1 (算法备案收紧) | skip+add |
| W6 | 多区上架策略 | high | 跨区扩张 / DMA 改写 EU | 各区合规清单 + 分发架构 | 2026-01 (CTC 5% 替代 CTF) | skip+optimize+add |
| W7 | 订阅 / 付费优化 | high | IAP 上线 / paywall 转化掉 | paywall 方案 + LTV | 2026-Q1 (anti-steering 落地) | skip+optimize+add |
| W8 | 持续维护 + 政策跟踪 | low | WWDC 6 月 / iOS major 9 月 | 12 月 roadmap + 政策响应 | 2026 持续 | optimize+add |

---

## W1. 上架 0→1 主流程 — evidence: [T03-S001..S005, T03-S014, T03-S017, T01-S001/S005/S007]

**Trigger**: 决定做 iOS app + Apple Developer 注册 ($99/yr 个人 / $299 org). **Output**: ASC = Ready for Sale + 真可下载 link.

**入门 SOP** (8 步):
1. **Apple Developer 注册** (1-3 工作日 D-U-N-S). 跳 → 无 ship 资格.
2. **Xcode 项目配置**: Bundle ID + Provisioning Profile + Distribution Certificate + Capabilities. **iOS 26 SDK + Xcode 26 强制 2026-04-28**.
3. **ASC App 创建 + Metadata**: name (30) + subtitle (30) + keyword (100) + description + nutrition labels + age rating (**2026-01-31 起新 5 档 4+/9+/13+/16+/18+ 强制**) + Pricing. 跳任一字段 → metadata reject (40% 拒审是 2.1 incomplete).
4. **Privacy Manifest + 三方 SDK**: 2024-05-01 强制 + 2025-02-12 起 SDK signed 强制. **Q1 2025 Apple 12% 拒审是 Privacy Manifest 违规** (T03-S017). 跳 → ITMS-91061/91065 直接拒.
5. **Archive & Upload**: Xcode Organizer / Fastlane `gym` + `pilot`. 跳 Validate App → 浪费 1 review cycle.
6. **TestFlight Beta**: 100 internal 无审 / 10000 external **第一版必走 Beta App Review 24-48h**. 跳 → 直接 App Review 踩 crash 1-2 周回炉.
7. **App Review 提审**: **2026 平均 90% 24h / 98% 48h, 但首次 + 复杂 1-2 周**.
8. **Release**: Manual / Automatic / Phased (7 天 1/2/5/10/20/50/100%, 可暂停 ≤30 天但**不能回滚**).

**资深差异**:
- *skip*: **海外 indie** (Marco/Smith) 跳 ASA 启动 + ASO 顾问, 1.0 靠编辑推荐 + community shoutout.
- *optimize*: **大厂 release engineering** Fastlane + Bitrise/GHA mac runner + ASC API 全自动 (T03-S014); 单人 indie Xcode Organizer 手提即可.
- *add*: 资深 add 4 件: (a) **下架预演** build < 2h 可重传; (b) **法律审 ARG** 用自家 app 对照 5.x 国别条款 (Marco DNA); (c) **关键词预研 4-6 周前** — name+subtitle+100 字占搜索权重 ≈70%, 上线后改 = 失 1 周 ranking 训练; (d) **三方 SDK Privacy Manifest 提前 1 周对账** (30+ SDK 缺 1 拒).
- *学派 DNA*: **海外 indie** 1-2 人 1-3 周, Fastlane + RevenueCat + AppFollow free, 跳 CI/CD (Smith 50M+ 单人 T01-S007); **大厂** 5-15 人 + release manager 专职; **国内出海** 海外栈 + 七麦 + 国内多市场并行, **备案前置** (W5 必跑通才提交国区).

**近期变化** (2026): iOS 26 SDK 2026-04-28 + 5 档 age rating 2026-01-31 + ASC Analytics 100+ 新指标 2026-04. 触发: 平台政策.

**典型耗时**: 入门 1-3 周 / 资深 3-5 天. **关键工具**: Xcode + ASC + Fastlane + TestFlight + RevenueCat + Sentry/Crashlytics. **关键人物**: Marco/Smith / 硬地骇客.

**失败模式**: Bundle ID 改 = 新 app / Privacy Manifest 漏 SDK / TF 公链当 production / metadata reject 后重传 binary / 首次 external TF 1 天前才提.

---

## W2. Rejection 救火 — evidence: [T03-S015, T03-S016, T03-S020, T03-S021, T01-S001/S013/S019]

**Trigger**: ASC = Metadata/Binary Rejected, Resolution Center 收到 reviewer + 引 ARG 条款号. **Output**: 重提通过 OR 公开发声战.

**入门 SOP** (5 步):
1. **拒绝分类**: 1.x Safety / 2.x Performance (crash/不完整, 40% 拒) / 3.x Business (IAP/anti-steering) / 4.x Design (HIG/4.3 spam) / 5.x Legal (隐私/版权/国别). 跳 → 误用 fix path 第二轮再拒.
2. **复现 + 修复**: reviewer 截图 / 操作步骤; 同 iOS / 国别 / 网络重现.
3. **Resolution Center 沟通**: 短 + 具体 + **引 ARG 条款号**. 成功模板: "Per ARG 4.3, we removed duplicate templates and replaced with X. Build 1.0.1 for review." 跳 → 卡 7+ 天.
4. **Expedited Review**: 一年 1-2 次额度, 关键 launch / 用户损失才用. 滥用 → 失额度.
5. **重提 + 监控**: 改 metadata 不重传 binary; 改 binary 必须 increment build number.

**资深差异**:
- *skip*: 资深 skip 长邮件辩论, 1 句话 + diff link. reviewer 90% 看不完长文.
- *optimize*: 第一份提交就 attach「Review notes」— demo account + 测试步骤 + 国别说明 (60% 拒审是 reviewer 没复现到核心 flow).
- *add*: **「拒审日志」** — 每次条款号 + reviewer 原话 + 修复 diff + 重提时间. 半年后能识别**某条款 reviewer 真在管 vs 写但不查** (Marco 15 年 corpus T01-S001).
- *学派 DNA*: **海外 indie** (DHH/Marco) 公开发声 — Twitter/blog/podcast 制造舆论 (Hey 24-01 T03-S020 + Launcher 14-12 T03-S021), **风险**: indie 资源不足扛不住; **大厂** 私下 Apple Account Manager / Dev Relations partner 通道, 不公开战 (Stripe/TikTok/Lyft); **国内合规派** 5.6 China Mainland 拒走工信部/网信办行政申诉 (W5).

**近期变化** (2026-Q1): Apple Review summaries LLM 自动生成 + 编辑团队复核 (WWDC 2025).

**典型耗时**: 入门 1-7 天 / 资深 4-24h. **极端公开战** (DHH/Marco): 数周-数月. **关键工具**: Resolution Center + 拒审日志 (Notion/Linear). **关键人物**: DHH / Marco / 硬地骇客嘉宾.

**失败模式**: 抄 ARG 不读条文 / metadata reject 重传 binary / Resolution Center 写 1000 字 / 普通 indie 学 DHH 公开战 backfire / Expedited 滥用第 3 次失额.

---

## W3. ASO 优化主流程 — evidence: [T03-S010, T03-S011, T01-S020/S021/S022/S023, T02-S016/S019/S020]

**Trigger**: 上架前 4-6 周 / 季度迭代 / ASA 启动 / keyword 排名掉 / iOS major 后重测. **Output**: keyword ranking top 10 + CVR 提升 + organic 增长.

**入门 SOP** (4 步):
1. **Pre-launch keyword 调研** (4-6 周): Sensor Tower (大厂) / AppTweak (agency) / Mobile Action (indie) / 七麦 (国内). 选 3-5 词放 title (30) + subtitle (30) + 100 字 keyword. 跳 → 上线 organic 0.
2. **Screenshots + Preview Video**: 第 1-2 张占 70% 转化. **2026 算法变化**: 截图 caption 文字也被索引 (T03-S010, 2025-06 起).
3. **Custom Product Pages (CPP) + In-App Events (IAE)**: **2026 起 CPP 35→70 槽位 + 可绑定 keyword 进 organic** (T03-S010); IAE 物理移除 ASA 槽位 (T03-S011).
4. **ASA + 评论 + 持续 iterate**: ASA exact match 自家品牌词 (90% intent 低 CPC); 引导评论 (Apple prompt API); 季度 iterate. **2026-03-17 起 ASA 多广告位生效, organic 第 3 位也可能 sponsored**.

**资深差异**:
- *skip*: **ASO 优化派** (Seufert/Petit/Young) 跳"100 字 keyword 塞满" — 5-10 词聚焦 ranking 高.
- *optimize*: **每 4-6 周 metadata 刷新** + IAE + screenshot A/B (2026 算法权重最高); PPO 是 entry-level.
- *add*: **「关键词 + 评论 + 转化率」三角联动** (硬地骇客嘉宾 Una T01-S027) — 任一掉 ranking 必崩.
- *学派 DNA*: **海外 indie** (Marco/Smith) 跳 ASA + 顾问, audience-first ship-then-aso (Smith 14 年 craft + iOS 14 widget 偶然爆 T01-S007); **ASO 优化派** (Seufert/Petit/Young) 系统化, AppTweak/Sensor Tower + ASA + CPP + IAE 全栈, ASO 1.0 (keyword stuffing) 死, ASO 2.0 把 product page 当 webpage A/B test (Petit T01-S022); **大厂** ASO 3-10 + 投放 5-20, ASA 月 spend $100K+; **国内** (鸟哥/七麦) 国区用七麦双端 + 国内多市场各家算法不同 (W5).

**近期变化** (2026-Q2): CPP organic 2025-07 + 35→70 槽位 2026 / ASA 多 slot 2026-03-17 / 截图 caption 索引 2025-06. 采用率: 大厂 ≥90% CPP+IAE; indie ≈30%; 国内 ≈50%.

**典型耗时**: 入门 4-6 周 pre-launch + 季度 1 周 / 资深 2 周 + 月度刷新. **关键工具**: AppTweak / Sensor Tower / Mobile Action / 七麦 + ASA + CPP + IAE + AppFollow.

**失败模式**: title 塞品牌词+":"+长 keyword 串 (4.x design 风险) / keyword 100 字废词 / screenshot 第 1 张是 splash / 不做 IAE 在 2026 (ASA 第 3 槽吃 organic) / 上线后再做 ASO (前 30 天 ranking 训练数据丢).

---

## W4. 隐私 / 合规 (海外栈) — evidence: [T03-S005, T03-S017, T01-S020, T04-S016/S024/S025/S026]

**Trigger**: 任何 SDK 集成 / 新版本提交 / EU/CA/<13 用户进入. **Output**: PrivacyInfo.xcprivacy + nutrition labels + ATT + GDPR + CCPA + COPPA.

**入门 SOP** (6 件并行):
1. **Privacy Manifest (.xcprivacy)** — 2024-05-01 强制 + 2025-02-12 SDK signed 强制. app + 每个三方 SDK 各 1 份, 主 app 聚合. **Required Reason API 4 类** (file system / boot time / disk space / user defaults) 各需 reason code. 跳 → ITMS-91061/91065.
2. **Privacy Nutrition Labels** (ASC metadata 展示, 跟 Privacy Manifest 区分: 展示 vs 机器读). 跳 → metadata reject.
3. **ATT** — iOS 14.5 起强制 opt-in, 25-30% 平均 opt-in. 用 IDFA 必弹, 文案需准确合规.
4. **GDPR** — consent banner + DSR + DPA + sub-processor list. 不可绕 (Spotify €1.84B 案).
5. **CCPA + CPRA** — "Do Not Sell or Share" link 强制; 2023-01 加 CPRA. CA 事实美国基线.
6. **COPPA** (≤13) — Kids Category 4+ 强制无 ATT + 无 IDFA + 父母同意. 误判 → FTC 罚.

**资深差异**:
- *optimize*: 资深用 **compliance-as-code** — PrivacyInfo.xcprivacy YAML 版控 + SDK manifest CI lint (Bitrise/GHA + Fastlane) 阻断. SDK 升级 → 自动 diff, 节奏 vs 单人手填差 10x.
- *add*: **annual SDK manifest 审计** — 三方 SDK 半年升 1 次, 跟不上 = 拒. 资深季度全 SDK 重读.
- *学派 DNA*: **海外 indie** 单人手填 + GDPR 用 OneTrust / 自建; **大厂** Privacy team 专职 + manifest 从内部 data lineage 自动生成 + GDPR 全栈 (Vanta/OneTrust + DPO); **ASO 派** (Seufert) 反 ATT (T01-S020 self-preferencing 反垄断), 实操 post-IDFA SKAN 4.0 + incrementality; **反 Apple** (DHH/Sweeney) 公开战 ATT, 实操合规; **Apple 派** ATT + Privacy Manifest 是平台护城河 + 隐私品牌.

**近期变化** (2025-2026): 2025-02-12 SDK signed 强制 / 2025-04 法国 ATT 罚 €150M / 2026-Q1 ASC 加严 nutrition labels 与 manifest 一致性.

**典型耗时**: 入门 1-2 周 / 资深 2-3 天 (模板). **关键工具**: PrivacyInfo.xcprivacy + ATTrackingManager + OneTrust/Cookiebot + Sentry.

**失败模式**: Privacy Manifest 漏 SDK (12% 拒审主因) / ATT 文案误导 / nutrition labels 错填 / GDPR consent dark pattern / COPPA Kids 用 IDFA.

---

## W5. 国内合规 (大陆 / 出海) — evidence: [T03-S012, T03-S013, T03-S018, T01-S025/S026/S027/S028, T04-S019/S021/S023]

**Trigger**: 国区 ASC 上架 / 大陆运营 / 国内 Android 多市场出海. **Output**: ICP 备案号 + 算法备案 (推荐/AI) + 版号 (游戏) + 国内 8-10 市场 + 个保法.

**入门 SOP** (5 件, 多数并行 + 备案前置):
1. **ICP 备案** (工信部 beian.miit.gov.cn) — **2024-04 强制, 国区 ASC 不填直接拒**. 流程: 域名 → App 备案 → 网安备案; 通过云接入 (阿里云/腾讯云/华为云) 提交; 个人 7-15 工作日, 公司 1-2 月. **个人备案极难** (无主体), 实操多走公司.
2. **算法备案** (网信办 beian.cac.gov.cn) — 推荐算法 + 生成式 AI 强制, 2026-Q1 累计 800+ 服务备案 (T03-S013). 法定 30 工作日, 实操 2-3 月. "舆论属性 / 社会动员能力" 必备. 跳 → 下架 + 罚款.
3. **游戏版号** (出版署 nppa.gov.cn) — 仅游戏, 极严, 审批 20+60 工作日; 非游戏跳过.
4. **国内 Android 8-10 市场** (T03-S018): 华为 / 小米 / OPPO / vivo / 应用宝 / 百度 / 360 / 豌豆荚 — **各自后台 + 各自审 + 各自标准 + 各自 ICP**. 流程: 各开发者账号 + 实名 + 软著 + APK + 截图 + 描述 + 隐私协议. 单家 1-3 工作日, 8 家齐 1-2 周. **鸿蒙 (HarmonyOS NEXT) 2026-09-30 华为激励截止 — 单独 native rebuild**.
5. **个保法 + 等保 + 中文隐私协议**: PIPL (2021) 强制中文 + 数据本地化 + 主体责任清晰; 大型 app 等保 2/3 级. 工信部抽检违规 SDK 持续.

**资深差异**:
- *skip*: **海外 indie 出海** 跳国内 Android 多市场 (8 家 ROI 低), 仅 Apple 国区 + 海外 — 失国内 80% 用户量.
- *add*: **「备案 → 提交 → 上线」串行预演** — 国区 ASC 提交前 ICP 必须已下证; 算法备案前置 1-2 月; 版号前置 6-12 月. 资深 6 月前就开备案.
- *学派 DNA*: **海外 indie** 多数跳大陆; **国内合规派** (鸟哥/七麦/胡涵 T01-S025/S026/S027) 备案当主线, 海外栈 add-on, 国内多市场必修; **国内出海派** (硬地骇客 T01-S027/S028) 双轨海外 + 国内栈, "红海市场破局指南" — 高付费用户密度而非大流量 (Saga EP110); **大厂** (TikTok/字节出海) 三轨极致 — 海外 / 大陆 / 国内 Android, team 10+.

**近期变化** (2026-Q1): 算法备案持续收紧 (每月公告); 双轨制 (算法 + 大模型 + 登记三套); 鸿蒙激励 2026-09-30.

**典型耗时**: 入门 3-6 月 / 资深 1-2 月 (公司主体 + 模板). **关键工具**: 阿里云/腾讯云接入 + 七麦 + 各市场后台. **关键人物**: 胡涵 / 硬地骇客 / 鸟哥/七麦.

**失败模式**: ICP 不备案 ship 国区 (ASC 不进队列) / 个人无公司主体备案 / 国内 8 市场当一刀切 (工作量 8x) / 抄 ARG 不读 5.6 China Mainland 条款 / 生成式 AI 不备案 (下架+罚款) / 隐私协议英文版直译中文.

---

## W6. 多区上架策略 (US / EU / CN / Global) — evidence: [T03-S006, T03-S008, T03-S009, T01-S016/S017, T04-S014]

**Trigger**: 跨区扩张 / DMA 后改写 EU / Anti-steering 后 US 链外支付 / 国区出海. **Output**: 各区合规清单 + 分发架构 + 支付路径.

**入门 SOP** (按 region):
1. **美区 (US)**: Apple 唯一分发. 2024-01 Anti-steering 终审 + **2025-04-30 Apple 改 ARG 允许 link-out** (T03-S008/S009): app 内 button + URL 直跳 web 支付**无 27% 抽佣** (Rogers 2025-04 willfully 强化裁定). 但 link-out 转化漏斗下降 30-50%, 需 paywall 重设计.
2. **EU**: DMA 2024-03-07 主体生效, **2026-01 起 CTC 5% 替代 €0.50/install CTF** (T03-S006). 三条分发路径: (a) App Store + Apple IAP; (b) App Store + 外部 link-out; (c) Web Distribution / Alt Marketplace (Epic Games Store + AltStore). **总最低费率 ≈7%** (2% Initial Acquisition + 5% CTC). DMA 第二轮调查持续 (Daniel Ek "DMA farce" T01-S017).
3. **中国 (CN)**: ICP + 算法备案 + 版号 + Apple 国区 + 国内 Android 8-10 市场 (W5).
4. **Global / 其他**: 默认 Apple + IAP, 各国本地化 metadata + Apple Pricing Tier + 当地隐私法 (印度 DPDP / 巴西 LGPD / 日本 APPI).

**资深差异**:
- *skip*: **indie** 通常只做美区 + 自己国家 — 跨区 ROI 低, 合规成本高.
- *optimize*: 资深**先 region 列合规清单, 再 architecture** — 不是 architecture 完了才发现 EU 要 DPO / CN 要 ICP.
- *add*: **paywall 多变体 per region** — US link-out + EU 多路径 + CN IAP+微信支付混合; pricing tier per region (购买力差 5-10x).
- *学派 DNA*: **海外 indie** 仅美区 + 自己国家; **大厂** 跨区 release pipeline + paywall A/B + 合规 team; **国内出海** 双大陆海外栈; **反 Apple** (Sweeney/Ek/DHH) EU DMA 是 alt store 入口, 公开推 sideloading; 但 indie 实操 alt store 流量 < App Store 5%.

**近期变化** (2026-01): EU CTC 5% 替代 CTF / US link-out 2025-04-30 落地 + 2025-06 上诉 (Apple "reasonably necessary") / Epic Games Store + AltStore 2026-01 日本上线. 采用率: indie ≈5% 跨区; 大厂 ≈100%; 国内出海 ≈80%.

**典型耗时**: 入门 单区 1-3 月 / 跨多区 6-12 月. **关键工具**: ASC + DMA addendum (EU) + RevenueCat + 各国本地支付. **关键人物**: Sweeney / Ek / DHH.

**失败模式**: link-out 抄海外做大陆 (5.6 不允许) / EU 没 DPO 直接做 EU 客户 / CTC 5% 没在合同价格反映 (dev 自吃) / 跨区 paywall 一刀切 / Alt store 抢预算 (< App Store 5%).

---

## W7. 订阅 / 付费优化 — evidence: [T03-S007, T03-S008, T03-S009, T02-S012/S013/S014/S015, T01-S027]

**Trigger**: IAP 上线 / paywall 转化掉 / 模型成本 / 竞品改价 / Apple Tax 政策变. **Output**: paywall 方案 (hard/freemium/hybrid) + LTV + retention.

**入门 SOP** (5 步):
1. **IAP 类型决策**: consumable / non-consumable / auto-renewable subscription / non-renewable. **订阅是 95% indie 主流** (RevenueCat 115k apps benchmark T03-S007).
2. **Pricing Tier + Promotional Offers + Family Sharing**: Apple 800+ price points; intro offer (free trial / pay-up-front / pay-as-you-go); Family Sharing 一份用 6 人 (Y2+ 续按月单算).
3. **StoreKit 2** (WWDC21+): async/await + JWS + server-side validation; 替代 StoreKit 1 (deprecated). **资深用 RevenueCat / Adapty 替代**.
4. **Paywall 设计 + A/B**: **hard paywall 10.7% trial-to-paid vs freemium 2.1% — 5x 差距** (T03-S007). 长 trial (17-32 天) 比短 trial (<4 天) **高 70%**. iOS 2.6% vs Android 0.9% (3x). 资深用 RevenueCat/Adapty/Superwall A/B.
5. **Apple Tax 4 档**: 30% 标准 / 15% small biz (≤$1M/yr) / 15% subscription Y2+ / 0 link-out (US 2025-04+) + 0 EU alt-store + 5% EU CTC.

**资深差异**:
- *skip*: **indie** skip 自建 server (RevenueCat free up to $2.5K MTR + 1% gross 后); 大厂自建仍是常态.
- *optimize*: **Day 0 onboarding momentum > paywall 优化** (T03-S007 关键发现) — **55% 3-day trial 取消在 Day 0**. 先做 onboarding 再做 paywall A/B. 模式: 先 1 个 value moment 后再弹.
- *add*: **annual pricing review** — Apple Tier 涨 + 模型成本降 + 竞品改价. 资深每年 1 次重定价 + 2 次 paywall A/B.
- *学派 DNA*: **海外 indie** (Marco/Smith) RevenueCat 全 stage 默认 (硬地骇客共识 T01-S027), paywall 简单 + free trial 7 天; **大厂** 自建 server + RevenueCat + Mixpanel/Amplitude + AppsFlyer/Adjust 归因; **ASO 派** (Steve P. Young T01-S023) paywall design 是 indie 增长第一杠杆 (7-day trial vs no trial 改 conversion 20-50%); **反 Apple** (DHH T03-S020) 反对 IAP 强制, 实操 link-out (US) / 第三方 (CN 微信支付); **国内** (硬地骇客) 海外做 RevenueCat 订阅, 国内非 IAP 业务用微信支付.

**近期变化** (2026-Q1): Anti-steering link-out 2025-04-30 落地 / **Hybrid 定价 default** (hybrid adoption ≥60%, AI app 主推) / EU CTC 5% 2026-01. 采用率: hard paywall ≈60% indie; freemium ≈30% (RPI 9x 低); RevenueCat ≈70% 订阅 app.

**典型耗时**: 入门 1-2 周 接 RevenueCat / 资深 季度 paywall A/B. **关键工具**: RevenueCat + Adapty (paywall A/B) + Superwall.

**失败模式**: 30% Apple Tax 抗议不接受 (5 年法律战换 link-out, 不是 indie 资源能玩) / Day 0 直接弹 paywall (55% 取消) / Long trial 当唯一杠杆 / Family Sharing 当净增长 (-83% rev) / link-out 抄美区做全球 / 不用 RevenueCat 自写 StoreKit (退款/跨设备/试用都是噩梦, 硬地骇客共识).

---

## W8. 持续维护 + 政策跟踪 — evidence: [T03-S002, T01-S008/S012, T05-S001/S004/S005]

**Trigger**: WWDC 6 月 / iOS major 9 月 / 季度 ASC 更新 / 政策公告. **Output**: 12 月 roadmap + 政策响应 + crash/rating monitor.

**入门 SOP** (年节奏):
1. **WWDC** (每年 6 月): 当年 iOS major + 政策更新. 必看 sessions: "What's New in App Review" / "App Store Connect" / "StoreKit". 年度政策硬主源.
2. **ASC 月度更新**: developer.apple.com/news + Hello Developer monthly. **2026-01-31 / 2026-04-28 两次 deadline 集中** (age rating + iOS 26 SDK).
3. **iOS major** (每年 9 月): 用户 50-80% 6 月内升级, 必须支持新 SDK + Live Activity / Widgets / Lock Screen.
4. **持续 monitor**: crash (Crashlytics/Sentry) / rating (AppFollow) / keyword rank (七麦/AppTweak) / 评论 — 季度 review.
5. **政策变化响应**: ATT 2021 / Privacy Manifest 2024 / Anti-steering 2024-01 / DMA 2024-03 / iOS 26 SDK 2026-04 — 每个 12 月内适应. 反例: 12 月不更新 → 政策变 → 下架.

**资深差异**:
- *optimize*: 资深订**6 个高浓度源每周走半小时**: Apple Dev News + WWDC 短 talk + Marco/Smith/Viticci 长 review + Mobile Dev Memo + RevenueCat + ATP. **不是订 50 个 newsletter**.
- *add*: **「政策日历」** — Notion/Linear 自建, 每 deadline 提前 60/30/7 天 reminder (Smith 50M 14 年 indie 节奏 T01-S007).
- *学派 DNA*: **海外 indie** (Marco/Smith/Viticci) MacStories iOS 年度长评是行业 reading list (T01-S008), ATP / Under the Radar 政策吐槽 + 历史; **大厂** 专职 release manager + Apple Account Manager 通道 + Dev Relations partner program; **ASO 派** 季度 ASA/CPP/ASO 报告 + keyword ranking 重测 (Seufert MDM weekly Wed); **国内** 双轨 — Apple WWDC + 网信办/工信部公告 (备案系统每月公告 T03-S013).

**近期变化** (2026): 2026-01-31 age rating 5 档 / 2026-04-28 iOS 26 SDK + Xcode 26 / 2026-06 WWDC26 / 2026-09 iOS 27 (推断) / Apple ARG 季度微调.

**典型耗时**: 入门 每月 4h / 资深 每周 1h. **关键工具**: Apple Dev News RSS + WWDC + MDM + ATP / AppStories / 硬地骇客 + AppFollow / Crashlytics. **关键人物**: Viticci / Marco / Smith.

**失败模式**: 12 月不更新 → 政策变 → 下架 (Privacy Manifest/ICP/iOS SDK 任一 missing 都触发) / WWDC 不看半年内被超 / 订 50 个 newsletter 没用 / 不监控 rating/crash / 政策日历靠 memory.

---

## 学派分歧典型例 (≥ 3)

**例 1: 同一拒审 → indie 公开战 vs 大厂私下沟通 vs 国内行政申诉**
- **海外 indie** (DHH/Marco): 公开 Twitter/blog/podcast 制造舆论. DHH "Hey" 2020 → Apple 史上最快 carve-out (24h); DHH "Hey Calendar" 24-01 (T03-S020); Marco 14-12 Launcher (T03-S021).
- **大厂 release engineering**: 私下 Apple Account Manager / Dev Relations partner, 不公开战 (Stripe/TikTok/Lyft).
- **国内合规派**: 5.6 China Mainland 拒走工信部/网信办行政申诉, 公开战在国内不仅无效, 还可能加大监管 attention.
- **Consensus**: 资源/网络决定路径, 不是道德选择. DHH = 37signals (Basecamp 影响力 + 财务后盾), 普通 indie 不学.

**例 2: "ATT opt-in 25%" 触发学派相反操作**
- **Apple 派**: ATT 是隐私品牌资产, opt-in rate 不重要. **海外 indie** (Marco/Smith): ATT 让 ad-supported model 死 → 推 subscription 是好事. **ASO 派** (Seufert T01-S020): ATT 是 self-preferencing 反垄断 (法国 €150M 罚款 2025-04 第一个监管确认), 实操 post-IDFA SKAN 4.0 + incrementality + MMM. **反 Apple** (Sweeney/Ek): 公开推法律 challenge. **国内**: ATT 不在国内主战场, 个保法是真正合规框架.

**例 3: "$1M/年" 触发学派相反操作**
- **Apple 派**: $1M 是 small biz 上限, 之后回 30%; Schiller 2025-02 庭审证实 Apple 内部对 27% commission 也有分歧. **海外 indie**: $1M 是 indie "成功" 门槛, 18 月后切 30% 是经济事实. **大厂**: $1M 是 noise, target $100M+ ARR. **反 Apple** (DHH/Sweeney): "$1M small biz 是 PR 策略, 不是真减税". **国内**: $1M 之外另叠 ICP + 算法备案 + 8-10 市场分成, 实际 cost 远超 30%.

---

## 失败模式汇总 (跨 workflow, ≥ 8)

1. **Privacy Manifest 漏 SDK** — 12% 提交拒审主因 (T03-S017); ITMS-91061/91065 直接拒. (W1, W4)
2. **ICP 不备案 ship 国区** — 2024-04 起 ASC 不进 review 队列. (W1, W5)
3. **隐私 nutrition labels 错填 + Privacy Manifest 不一致** — metadata reject + ASC 加严一致性. (W1, W4)
4. **抄 ARG 不读条文** — 引错条款号让 reviewer 觉得在 gaming. (W2)
5. **TestFlight 公链当上架 / TF 当 production** — TF 90 天到期, 不计 ranking. (W1, W2)
6. **反垄断 link-out 抄海外做大陆** — 大陆 IAP 仍强制, 5.6 不允许. (W6, W7)
7. **30% Apple Tax 抗议而不接受** — 实操绕不开, 5 年法律战换 link-out 仅美区. (W7)
8. **国内多市场各自后台不同 — 当一刀切** — 工作量 8x. (W5)
9. **Day 0 onboarding 直接弹 paywall** — 55% 3-day trial 取消在 Day 0 (T03-S007). (W7)
10. **Metadata reject 后重传 binary 浪费 cycle**. (W2)
11. **12 月不更新 → 政策变 → 下架** — Privacy Manifest/ICP/iOS SDK 任一 missing. (W8)
12. **改 Bundle ID 上线一下** — 等于全新 app, 失 reviews/ranking. (W1, W3)
13. **首次 external TestFlight 1 天前才提交** — Beta App Review 24-48h 来不及. (W1)
14. **个人开发者无公司主体备案** — 极难, 实操多走公司. (W5)
15. **link-out 抄美区做全球** — 仅 US 2025-04+, 其他区仍 IAP 强制. (W6, W7)

---

## 衰减时点 (≥ 5)

| 时点 | 触发事件 | 影响 workflow | Decay |
|------|---------|--------------|-------|
| **每年 6 月** | Apple WWDC — iOS major + ARG 修订 + StoreKit/Privacy Manifest 新规 | W1/W2/W4/W7/W8 | high (年度强制) |
| **每年 9 月** | iOS major release (用户 50-80% 6 月内升级) | W1/W3/W8 | high (年度强制) |
| **每季度** | ASC 更新 + ARG 微调 + nutrition/age rating 一致性加严 | W1/W4/W8 | medium |
| **2026-04-28** | iOS 26 SDK + Xcode 26 强制提交 (T03-S002) | W1/W8 | high (一次性) |
| **2026-01-31** | 新 5 档 age rating 强制 (T03-S002) | W1/W8 | high (一次性) |
| **2026-01** | EU CTC 5% 替代 €0.50 CTF (T03-S006) | W6/W7 | high (政策替换) |
| **持续 (DMA 2024-03 起)** | EU DMA 演化 + Apple 反复改 (2024-01/08 / 2025-06 / 2026-01) | W6/W7 | high (季度变) |
| **持续 (国内 2024-04 起)** | 工信部 ICP + 网信办算法备案持续收紧 + 大模型备案 (每月公告 T03-S013) | W5 | medium (季度变) |
| **持续 (anti-steering 2024-01 / 2025-04)** | 美区 link-out 上诉持续 (Apple "reasonably necessary") | W6/W7 | high (法律未定) |
| **持续 (LLM 6 月一波)** | AI app hybrid 定价, 模型成本下降 → paywall 重定价 | W7 | high (季度变) |

---

## Phase 2 接口

### 反复出现 ≥ 3 workflow 的步骤 (playbook 候选)
- **「先 region 列合规清单, 再 architecture」** (W4+W5+W6) → "compliance-first, distribution-second".
- **「Privacy Manifest + nutrition labels + ATT」三件套预演** (W1+W4+W5) → "三件套不齐 = 任何 SDK 升级都拒".
- **「关键词 + 评论 + 转化率」三角联动** (W3+W7+W8) → "ASO 不是单 keyword, 是三轴联动" (硬地骇客共识 T01-S027).
- **「政策日历前置」** (W1+W4+W5+W8) → "deadline 提前 60/30/7 天 reminder".
- **「Resolution Center 短 + 引条款号 + diff link」** (W2) — 4 类条款拒审都用.

### 入门 SOP vs 资深路径最大差距 (心智模型候选)
- 入门 5-8 步全跑, 资深 3-4 步 + 多动作并行 (备案前置 / Privacy Manifest CI / paywall A/B 季度 batch).
- 资深 add 6 件: **下架预演 / 拒审日志 / 政策日历 / 三轴联动 / annual SDK manifest 审计 / annual pricing review** — 初学者不会做, 5+ 年见过坑必加.
- 资深 skip: ASA 0→1 用 / 自建 StoreKit / 100 字 keyword 塞满 / 单一 metadata 上线后再 ASO — 都 ROI 低.
- **核心心智模型**: (a) **App Store 是黑盒, 任何 guarantee 通过都是假的** (Marco/Smith/DHH 共识) → rejection 是迭代一步; (b) **政策变更比代码变更频繁** → 12 月以前攻略多过期, 必须订 6 个高浓度源; (c) **合规叠加比合规单一更难** — 国内 ICP+算法+版号 vs 海外 GDPR+CCPA+ATT vs DMA+anti-steering — playbook: 先按 region 列合规清单再 architecture.

### 近期变化触发事件分布
| 触发类型 | 影响 workflow | # |
|---------|--------------|---|
| Apple 平台政策 (ARG / Privacy Manifest / age rating / SDK) | W1/W2/W4/W8 | 4 |
| 法律 / 反垄断 (anti-steering / DMA / Epic v Apple / ATT 罚款) | W6/W7 | 2 |
| 国内 / 监管 (ICP / 算法 / 版号 / PIPL / 等保) | W5/W6 | 2 |
| Apple 算法 (CPP organic / ASA 多 slot / 截图 caption 索引) | W3 | 1 |
| Vendor / SDK 升级 (Privacy Manifest signed / RevenueCat / Adapty / Sentry) | W1/W4/W7 | 3 |
| 模型成本 / paywall 数据 (RevenueCat 2026 hard vs freemium 5x) | W7 | 1 |

主要驱动: **Apple 平台政策 + 法律 + 国内监管** 三轴同时高频. 12 月内 8 workflow 中至少 5 个有 deadline-class 变化.

### 学派 DNA 覆盖 — 8/8 workflow 显式标 5 学派
W1: indie / 大厂 / 国内三派 + ASO 反 Apple 次级 · W2: indie 公开 vs 大厂私下 vs 国内行政三派对立 · W3: ASO 派主线 + indie audience-first 反线 + 国内多市场 · W4: 5 派对 ATT/Privacy Manifest 立场不同 · W5: 国内合规/出海主线, 海外多跳, 大厂双轨 · W6: 4 派完全对立路径 · W7: 5 派定价路径 · W8: 4 派内容订阅源.

### 反馈给其他 Track
- **→ T02**: CPP 2026 35→70 (T03-S010) 必备层标"2026 升级"; In-App Events 2026 必备防御 (T03-S011).
- **→ T04**: Anti-steering 2025-04 willfully + RevenueCat 2026 paywall benchmark 进 canon.
- **→ T06**: "CTC 5%" (2026-01) 替代 "CTF €0.50" 进 Tier 2; "ITMS-91061/91065" 错误码进 Tier 2.

### 冷僻 / 信号薄弱自检
workflow 数 8 (≥4) ✓ / 每个 ≥2 资深差异 (W1/W2/W3/W6/W7 全 3 类) ✓ / 一手率 76% ✓ / 学派 DNA 8/8 ✓ / 学派分歧 3 例 ✓ / 失败模式 15 条 ✓ / 衰减时点 10 处 ✓.

### Phase 2.8 诚实边界节必引
- **衰减最快行业之一** — 5/8 high decay, **6 月内必复查** (Apple 政策 12 月内多次微调).
- **学派分歧不可平均化** — 拒审 indie 公开战 vs 大厂私下不是中间态, 是路径分支.
- **国内 vs 海外不能一刀切** — ICP/算法/多市场 vs Apple 单家黑盒, 几乎无共享术语.
- **2026 仍是政策密集期** — iOS 26 SDK (2026-04-28) / age rating (2026-01-31) / EU CTC 5% (2026-01) / anti-steering 上诉持续 — 任一 deadline 错过都可能下架.
- **Privacy Manifest + ICP 备案并列两大硬红线** — Q1 2025 Apple 12% 拒审是 Privacy Manifest 违规 (T03-S017); 国区 ICP 不备案 ASC 不进队列 (T03-S012).
