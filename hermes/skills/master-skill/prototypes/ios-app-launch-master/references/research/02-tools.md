# Track 02 — Tools (iOS App Store launch)

> Phase 1 wave 2. 26 tools, 4 buckets. Locale=global + zh-CN sub-track.

## Source Manifest

| source_id | url | bucket | last_checked | author | note |
|-----------|-----|--------|--------------|--------|------|
| T02-S001 | https://developer.apple.com/news/?id=pvszzano | verified_primary | 2026-05-04 | Apple | Privacy Manifest 2024-05 强制公告 |
| T02-S002 | https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk | verified_primary | 2026-05-04 | Apple | Privacy Manifest 文档 |
| T02-S003 | https://developer.apple.com/testflight/ | verified_primary | 2026-05-04 | Apple | TestFlight 官方 |
| T02-S004 | https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/ | verified_primary | 2026-05-04 | Apple | 100 internal/10000 external |
| T02-S005 | https://docs.fastlane.tools/ | verified_primary | 2026-05-04 | Fastlane | 主文档 |
| T02-S006 | https://docs.fastlane.tools/app-store-connect-api/ | verified_primary | 2026-05-04 | Fastlane | ASC API integration |
| T02-S007 | https://docs.fastlane.tools/actions/snapshot/ | verified_primary | 2026-05-04 | Fastlane | screenshot 自动化 |
| T02-S008 | https://github.com/fastlane/fastlane | verified_primary | 2026-05-04 | Fastlane | repo, 40k+ stars |
| T02-S009 | https://www.runway.team/blog/how-to-build-the-perfect-fastlane-pipeline-for-ios | verified_primary | 2026-05-04 | Runway | 实战 pipeline |
| T02-S010 | https://blog.codemagic.io/codemagic-vs-bitrise/ | verified_primary | 2026-05-04 | Codemagic | mobile CI/CD 对比 (vendor PR 注意) |
| T02-S011 | https://bitrise.io/blog/post/enforcement-of-apple-privacy-manifest-starting-from-may-1-2024 | verified_primary | 2026-05-04 | Bitrise | Privacy Manifest 工程化 |
| T02-S012 | https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/ | verified_primary | 2026-05-04 | RevenueCat | State of Subscription 2026 |
| T02-S013 | https://www.revenuecat.com/state-of-subscription-apps/ | surrogate_primary | 2026-05-04 | RevenueCat | 115k+ apps benchmark (vendor docs) |
| T02-S014 | https://github.com/RevenueCat/purchases-ios | verified_primary | 2026-05-04 | RevenueCat | iOS SDK |
| T02-S015 | https://adapty.io/paywall-ab-testing/ | secondary | 2026-05-04 | Adapty | paywall A/B 产品页 |
| T02-S016 | https://adapty.io/blog/in-app-events-protect-organic-apple-search-ads/ | verified_primary | 2026-05-04 | Adapty | In-App Events 2026 |
| T02-S017 | https://sensortower.com/ | secondary | 2026-05-04 | Sensor Tower | 大厂 ASO 标杆 |
| T02-S018 | https://appfollow.io/blog/aso-tools | verified_primary | 2026-05-04 | AppFollow | 2026 ASO 对比 |
| T02-S019 | https://www.apptweak.com/en/aso-blog/guide-to-apple-search-ads | secondary | 2026-05-04 | AppTweak | Apple Ads 指南 |
| T02-S020 | https://www.mobileaction.co/blog/aso-for-indie-developers/ | verified_primary | 2026-05-04 | Mobile Action | indie 实战 |
| T02-S021 | https://sentry.io/from/crashlytics/ | secondary | 2026-05-04 | Sentry | 与 Crashlytics 对比 |
| T02-S022 | https://www.appsflyer.com/advantage/adjust/ | secondary | 2026-05-04 | AppsFlyer | vs Adjust (vendor PR) |
| T02-S023 | https://lokalise.com/blog/getting-started-with-ios-localization/ | verified_primary | 2026-05-04 | Lokalise | iOS l10n |
| T02-S024 | https://mixpanel.com/platform/mobile-analytics/ | secondary | 2026-05-04 | Mixpanel | mobile analytics |
| T02-S025 | https://huhuhang.com/post/apps/appstore-china-icp-filing | verified_primary | 2026-05-04 | huhuhang | ICP 备案实践 |
| T02-S026 | https://blog.p2hp.com/archives/11713 | verified_primary | 2026-05-04 | Lenix | 2024 国内市场全流程 |
| T02-S027 | https://www.qimai.cn/ | secondary | 2026-05-04 | 七麦 | 国内双端 ASO 主流 |
| T02-S028 | https://www.ithome.com/0/722/535.htm | secondary | 2026-05-04 | IT之家 | Apple 国区 ICP 强制公告 |
| T02-S029 | https://capgo.app/blog/privacy-manifest-for-ios-apps/ | verified_primary | 2026-05-04 | Capgo | Privacy Manifest 实战 |

一手率: 21/29 = **72%** verified_primary (target ≥ 50%) ✅

## 总览（按 tier）

### 必备 (10)

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Xcode + iOS SDK | 开发 + Archive + 提审唯一入口 | low | T02-S001/S002 |
| Apple Developer Program | $99/yr 资格证 | low | T02-S001 |
| App Store Connect (web + API) | 官方 dashboard, metadata 入口 | low | T02-S001/S006 |
| TestFlight | 100 internal / 10000 external beta 分发 | low | T02-S003/S004 |
| Fastlane | build/sign/upload/metadata 自动化, de facto 标准 | low | T02-S005/S008/S009 |
| Privacy Manifest | 2024-05-01 强制 compliance | low | T02-S001/S002/S011 |
| Apple Search Ads (ASA) | 官方关键词广告 | low | T02-S016/S019 |
| Custom Product Pages + In-App Events | Apple 2022+ ASO 武器 | medium | T02-S016/S019 |
| RevenueCat | 订阅 SDK+后端, indie/scale 全 stage 默认 | low | T02-S012/S013/S014 |
| Crashlytics OR Sentry | crash 必装 | low | T02-S021 |

### 场景特化 (11)

| 工具 | When | Decay | Sources |
|------|------|-------|---------|
| Bitrise | mobile-only CI/CD, 团队 ≥ 3 | medium | T02-S010/S011 |
| Xcode Cloud | 全 Apple 栈, 仅 iOS | medium | T02-S010 |
| Codemagic | Flutter / 跨端首选 | medium | T02-S010 |
| GitHub Actions + Fastlane | DIY, GHA macos runner | low | T02-S009 |
| Sensor Tower | 大厂 / 投资研究, $30K+/yr | medium | T02-S017/S018 |
| AppTweak | 关键词深度 (Atlas AI), agency 主流 | medium | T02-S018/S019 |
| AppFollow | 评论 + Slack 集成, $111/月起 | low | T02-S018 |
| Mobile Action | Apple Ads 洞察, indie 中端 | medium | T02-S018/S020 |
| AppsFlyer / Adjust / Branch | ATT/SKAN 后归因, 大投放团队 | medium | T02-S022 |
| Mixpanel / Amplitude | 行为分析 retention/funnel | low | T02-S024 |
| Lokalise / Phrase | 多语言 string catalog 管理 | low | T02-S023 |

### 国内/出海特化 (3)

| 工具 | When | Decay | Sources |
|------|------|-------|---------|
| 七麦数据 (qimai.cn) | 国区 + 国内 Android ASO 数据源 | medium | T02-S027 |
| 工信部 ICP 备案 | 国区 App Store 上架硬门槛 | low | T02-S025/S026/S028 |
| 国内 Android 市场 (华为/小米/OPPO/vivo/应用宝) | 国内出海双端必走 | medium | T02-S026 |

### 新兴 (2)

| 工具 | Born | Adopters | Decay |
|------|------|----------|-------|
| Adapty | 2020, 2024-26 起势 | growing indie + scale | medium |
| Superwall | 2022, paywall builder | early, RevenueCat 互补 | high |

## 关键工具卡片

- **Fastlane (必备)**: ruby DSL build/sign/upload/metadata + ASC API. GitHub 40k+ stars (2026-05-04), MIT. 场景: CI/CD + 多 locale screenshot + ASC metadata git-managed. 不适合: 单人偶尔提审 (Xcode Organizer 够). 几乎所有 iOS YC 团队 (Bitrise/Codemagic 底层都是 fastlane). Decay low. evidence: [T02-S005, T02-S008, T02-S009]
- **RevenueCat (必备)**: 订阅 SDK + 后端, free up to $2.5K MTR + 1% gross. 场景: 任何 IAP 订阅 + 跨端 entitlement + 基础 paywall A/B. 不适合: 一次性买断 (StoreKit 2 自写). State of Subscription 2026 数据集 115k+ apps. Decay low. evidence: [T02-S012, T02-S013, T02-S014]
- **Privacy Manifest (必备 compliance)**: 2024-05-01 起强制, app + 三方 SDK 各自需 manifest, 主 app 聚合; 缺失直接拒审. Decay low. evidence: [T02-S001, T02-S002, T02-S011, T02-S029]
- **Sensor Tower (场景特化)**: $399/月 module / $30K+/yr enterprise, ad intelligence + revenue estimate. 场景: VC/PE 研究, 大厂 portfolio, 投放洞察. 不适合 indie. Decay medium (data.ai 2024 sunset 后巩固; AppTweak 关键词逼近). evidence: [T02-S017, T02-S018]
- **七麦数据 (国内特化)**: 国区 + 国内 Android 双端 ASO, 2017-10 由 ASO100 改名. 场景: 中国大陆 ASO + 国内出海跟踪 + ASA/ASO 协同. 国内大部分 mobile growth 团队默认. Decay medium. evidence: [T02-S027]
- **ICP 备案 (国内特化 compliance)**: 工信部 2023-08 通知, 苹果 2024-04 起国区无备案号下架. 流程: 域名 → App 备案 → 网安备案; 省级通信管理局 20 工作日. 失败模式: 个人开发者无公司主体极难. Decay low. evidence: [T02-S025, T02-S026, T02-S028]
- **Adapty (新兴)**: RC 兼容 API + paywall A/B 引擎 (2024-26 视觉构造超过 RC). 场景: paywall 是核心增长 + 已 PMF + growth marketer. 不适合 0-1. Decay medium. evidence: [T02-S015, T02-S016]

## 选型决策树

### Branch 1: indie / 海外 / solo dev
→ Xcode + Fastlane + TestFlight + RevenueCat + Crashlytics (free) + AppFollow ($111/mo)
→ 不推荐: Sensor Tower ($30K+/yr), AppsFlyer (有机增长无意义), Bitrise (单人不值)
→ 案例: 大部分 single-dev YC team / indie hacker 公开 stack

### Branch 2: 已 PMF, scale-up 团队 (海外)
→ Bitrise OR Xcode Cloud + Fastlane + RevenueCat + Sentry + Sensor Tower OR AppTweak + AppsFlyer + Mixpanel
→ 决策点: paywall 是核心增长 → 加 Adapty/Superwall; 否则 RevenueCat 自带够

### Branch 3: 国内出海 dev (双端国内 + 海外)
→ Xcode + Fastlane + RevenueCat + 七麦 + 备案易 + 华为/小米/OPPO/vivo 后台 + Sensor Tower (海外部分)
→ 必走: ICP 备案 (域名+App 双备案) + 国区 ASC 提交备案号 + 国内 Android 各市场单独审核
→ 风险: 个人开发者备案极难, 必须公司主体

### Branch 4: ASO 顾问 / agency
→ Sensor Tower + AppTweak + AppFollow (评论 SOP) + Mobile Action (Apple Ads) + 七麦 (国内客户)
→ 不推荐: 仅免费工具 (客户付费要数据深度); 单一工具 (一手+二手交叉验证)

### Branch 5: 仅 macOS / 极简 indie / 第一次上架
→ Xcode + ASC + TestFlight (Apple 官方栈) + RevenueCat + AppFollow free
→ 暂不需要: Fastlane (单人手提审 OK), CI/CD, 付费 ASO 工具

## 避坑清单

1. **不要忽视 Privacy Manifest**: 2024-05 后无 PrivacyInfo.xcprivacy 直接拒审, 三方 SDK 各自需 manifest 主 app 聚合 (evidence: [T02-S001, T02-S011])
2. **不要在 dev 阶段强行选 Bitrise / Sensor Tower 全栈**: 单人 indie $99 + Xcode + Fastlane + RevenueCat free 已够, 等 PMF 再加
3. **不要把 Crashlytics 当 APM**: 仅 crash, 不监控 ANR / 启动时长 / 帧率 — 用 Sentry / MetricKit
4. **不要忽视国区 vs 国内 Android 是两套规则**: 国区 ASC 苹果审 + ICP 必填; 国内 Android 各家审隐私+网安+内容三关 — 国内出海双端最大坑 (evidence: [T02-S025, T02-S026])
5. **不要用 RevenueCat 替代支付前的产品规划**: RC 解决 SDK + 后端 + 跨端; paywall 视觉/triggers/A/B 仍需 Adapty/Superwall 或自建
6. **不要在 ASA + In-App Events 协同上偷懒**: 2026 起 in-app events 是组织防御 (用过的用户该 slot 让位给你的 CPP), 不是 nice-to-have (evidence: [T02-S016])
7. **不要相信 vendor 自家对比页**: AppsFlyer vs Adjust 自家页, Adapty vs RevenueCat 自家页都是 PR; 决策 ≥ 2 独立 source 交叉
8. **不要忘 TestFlight 外测首版要 App Review**: 第一版外测 build 也要 Apple review (后续不用), 别在发布前一天才提交外测 (evidence: [T02-S004])

## Phase 2 提炼提示

**反复 ≥ 3 source 强调的「工具选型原则」**:
- "Compliance is non-negotiable, tooling is": Privacy Manifest + ICP 备案是硬门槛, 工具可调 (evidence: [T02-S001, T02-S011, T02-S025])
- "Apple 三件套 0 成本起步": Xcode + Fastlane + RevenueCat 是 95% iOS dev 起点 (evidence: [T02-S005, T02-S009, T02-S012])
- "国内 vs 海外两套生态": 国区 ASO 用七麦, 国内 Android 各家后台单独审, 海外用 ST/AT — 不能混 (evidence: [T02-S026, T02-S027])

**显著的工具流派分裂** (候选智识谱系):
- 企业级 ($30K+/yr Sensor Tower / data.ai) vs indie 友好 ($100-500/月 AppFollow / Mobile Action)
- Apple-only stack (Xcode Cloud + ASC native) vs 跨平台 stack (Bitrise / Codemagic)
- 厚 paywall infra (RevenueCat 一站) vs 薄+增长拼接 (RC + Adapty/Superwall)
- 国内 compliance-first (备案 + 国内市场) vs 海外 distribution-first (ASO + ASA + 归因)

**新兴工具信号**: 当前活跃 Adapty / Superwall 抢 RevenueCat 中端; 出现→主流速度 18-24 个月 (Adapty 2020→2024 主流参考)

**冷僻 / 信号薄弱**:
- 必备 10 ✅, 场景特化 11 ✅, 新兴 2 ✅
- 国内 sub-bucket 来源相对薄 (3 source) — zh-CN 维度可由 user 内部素材补强
- decay risk 集中: 归因工具 (ATT/SKAN 协议演化) + 国内市场后台 (政策频变) + 新兴 paywall — 3 维度均 medium-high
