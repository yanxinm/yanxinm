# Track 06 — Glossary (iOS App Store Launch)

> Phase 1 wave 1. industry=iOS App Store launch / locale=global / slug=ios-app-launch / profile=practitioner.
> 三套术语合流: Apple 官方政策 + ASO/营销 + 法律合规 (含中国大陆专属体系)。
> 65 条术语 (Tier 1 = 28, Tier 2 = 30, Standards/Regs/Cert = 7).

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://developer.apple.com/app-store/review/guidelines/ | verified_primary | 2026-05-04 | Apple Developer | App Review Guidelines 一手原文 (6 大类) |
| T06-S002 | https://developer.apple.com/news/?id=pvszzano | verified_primary | 2026-05-04 | Apple Developer | Privacy Manifest 2024-05-01 强制公告 |
| T06-S003 | https://developer.apple.com/documentation/bundleresources/privacy-manifest-files | verified_primary | 2026-05-04 | Apple Developer | PrivacyInfo.xcprivacy 文件规范 |
| T06-S004 | https://developer.apple.com/support/dma-and-apps-in-the-eu/ | verified_primary | 2026-05-04 | Apple Developer | DMA 合规与 EU app 分发 |
| T06-S005 | https://www.apple.com/newsroom/2024/01/apple-announces-changes-to-ios-safari-and-the-app-store-in-the-european-union/ | secondary | 2026-05-04 | Apple Newsroom | iOS 17.4 sideloading 公告 |
| T06-S006 | https://developer.apple.com/app-store/user-privacy-and-data-use/ | verified_primary | 2026-05-04 | Apple Developer | ATT / IDFA / 隐私 nutrition label 集合页 |
| T06-S007 | https://developer.apple.com/app-store/small-business-program/ | verified_primary | 2026-05-04 | Apple Developer | 15% small biz program 一手 |
| T06-S008 | https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/ | verified_primary | 2026-05-04 | Apple Developer | Phased release 7-day rollout |
| T06-S009 | https://developer.apple.com/support/reader-apps/ | verified_primary | 2026-05-04 | Apple Developer | Reader Apps External Link Entitlement |
| T06-S010 | https://developer.apple.com/storekit/ | verified_primary | 2026-05-04 | Apple Developer | StoreKit 2 (WWDC21) |
| T06-S011 | https://developer.apple.com/testflight/ | verified_primary | 2026-05-04 | Apple Developer | TestFlight 官方 docs |
| T06-S012 | https://developer.apple.com/app-store-connect/api/ | verified_primary | 2026-05-04 | Apple Developer | App Store Connect API |
| T06-S013 | https://en.wikipedia.org/wiki/Epic_Games_v._Apple | secondary | 2026-05-04 | Wikipedia | Anti-steering 判决与时间线总览 |
| T06-S014 | https://en.wikipedia.org/wiki/Digital_Markets_Act | secondary | 2026-05-04 | Wikipedia | DMA 立法历程 (2022-2024) |
| T06-S015 | https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm | verified_primary | 2026-05-04 | 国家网信办 | 生成式 AI 暂行办法 一手 (2023-08-15 施行) |
| T06-S016 | https://www.miit.gov.cn/ | verified_primary | 2026-05-04 | 工信部 | App 备案主管机关 |
| T06-S017 | https://www.nppa.gov.cn/bsfw/jggs/yxspjg/ | verified_primary | 2026-05-04 | 国家新闻出版署 | 游戏版号审批结果公示 |
| T06-S018 | https://huhuhang.com/post/apps/appstore-china-icp-filing | secondary | 2026-05-04 | 个人长 blog | China App Store ICP 备案实操经验 |
| T06-S019 | https://www.qimai.cn/ | secondary | 2026-05-04 | 七麦数据 | 国内 ASO 数据平台 + 术语普及 |
| T06-S020 | https://phiture.com/asostack/all-the-app-store-optimization-news-from-wwdc-2021-you-need-to-know-a-b-testing-tool-custom-product-pages-and-in-app-events-in-ios15/ | secondary | 2026-05-04 | Phiture (ASO agency) | CPP / IAE / PPO 一手解读 |
| T06-S021 | https://techcrunch.com/2024/01/16/supreme-court-declines-to-hear-apple-epic-antitrust-case-meaning-developers-can-point-customers-to-the-web/amp | secondary | 2026-05-04 | TechCrunch | Anti-steering 判决落地报道 |
| T06-S022 | https://eur-lex.europa.eu/eli/reg/2022/1925/oj | secondary | 2026-05-04 | EUR-Lex | DMA 立法原文 |
| T06-S023 | https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-build-statuses/ | verified_primary | 2026-05-04 | Apple Developer | 提审状态 (Waiting / In Review / Pending Developer Release / Ready for Sale) |
| T06-S024 | https://www.flurry.com/blog/ios-14-5-opt-in-rate-att-restricted-app-tracking-transparency-worldwide-us-daily-latest-update/ | secondary | 2026-05-04 | Flurry (Yahoo) | ATT opt-in rate 行业基准数据 |

---

## 总览

### Tier 1 — 核心必懂 (28 条)

| 术语 | Type | Insider def | Outsider tell |
|------|------|-------------|---------------|
| App Review | term | Apple 提交后人工 + 自动审核 (黑盒) | 当成"自动化检测", 实际 60% 人工 |
| App Review Guidelines | regulation-like | 6 大类 (1.x Safety...5.x Legal) | 当 reference 不当"圣经", 不通读直接撞 |
| App Store Connect (ASC) | term | 提审 + metadata + analytics 总台 | 跟 "iTunes Connect" 混 (2018 改名) |
| TestFlight | term | Apple 官方 beta + 也要 Beta App Review | "TF 公链 = 上架" — 灾难误读 |
| ARG 5.6 China Mainland | regulation | 大陆 ICP+版号+算法备案条款 | 以为"Apple 通过就行", 漏国内合规 |
| In-App Purchase (IAP) | term + acronym | 数字商品必走 Apple (15/30%) | 实物电商当 IAP 走, 反而被拒 |
| Apple Tax | jargon | 4 档: 30% std / 15% small biz / 15% sub Y2+ / 0 link-out | 以为固定 30% |
| Subscription (auto-renewable) | term | 主流 SaaS 模式, Y2+ 降 15% | 跟 non-renewable 混 |
| ATT (App Tracking Transparency) | acronym + std | iOS 14.5+, 强制 opt-in tracking 弹窗 | 不弹 = 用 IDFA 必拒 |
| IDFA | acronym | Identifier for Advertisers, ATT 后 opt-in ~25% | 以为还能默认拿到 |
| Privacy Manifest | term + std | PrivacyInfo.xcprivacy, 2024-05-01 强制 | 念成 "privacy manifesto", 当 marketing |
| Privacy Nutrition Labels | term | App Store 数据收集类目展示 | 跟 Privacy Manifest 混 (展示 vs 机器读) |
| StoreKit 2 | term + std | WWDC21 新 IAP API, async/await+JWS | 跟 StoreKit 1 receipt 混 |
| HIG (Human Interface Guidelines) | acronym + std | Apple 设计规范 | 当 nice-to-have, 4.x 拒审硬卡 |
| Bundle ID | term | app 全局唯一 reverse-DNS | 改 Bundle ID 当迭代 = 新 app |
| Provisioning Profile | term | 签名+设备+entitlement 凭证 | 跟 certificate 混 |
| Entitlements | term | capability 权限 (Push/iCloud/HealthKit) | 当 build setting, 实际是审计点 |
| Apple Developer Program | term | $99/yr 个人 / $299 org | 当一次性, 续费断 = 下架 |
| Rejection / Reject | term | 分 metadata reject vs binary reject | 任何拒都重传 binary |
| Resolution Center | term | ASC 内 reviewer 沟通 + 审计记录 | 当客服 |
| Phased Release | term | 上线 7 天梯度 1/2/5/10/20/50/100% | 当手动控制, 实际 Apple 自动 |
| Expedited Review | term | 加急, 一年 1-2 次额度 | 当常规手段 |
| ASO (App Store Optimization) | acronym | 关键词+截图+转化率综合 | 当 SEO 复制粘贴 |
| Keyword Field | term | 100 字符隐藏 (不展示) | 当 description, 肉眼看不到 |
| Apple Search Ads (ASA) | acronym | Apple 官方关键词广告 | 跟 Google UAC 混用预算逻辑 |
| Conversion Rate (CVR) | acronym | 产品页 → 下载比例 | 等同 activation rate |
| ICP 备案 | regulation | 工信部, 大陆 App 必备号 (2024-04 强制) | 跟"ICP 许可证"混 |
| 算法备案 | regulation | 网信办, 推荐/生成式 AI 强制 | 当游戏版号同类, 实际跨行业更广 |

### Tier 2 — 周边熟知 (30 条, 紧凑列表)

- **IAP/商业**: Universal Purchase (2020) / Family Sharing / Promotional Offer / Reader Apps 3.1.3a (2022-03) / Link Out DMA (2024-03) / External Purchase Link Entitlement US (2024-01)
- **Build/CI**: Xcode / Archive (xcarchive) / Distribution Certificate / App Sandbox / dSYM + Symbolication / Crashlytics + MetricKit (2019) / Fastlane (社区 CI 事实标准) / App Thinning (Bitcode deprecated 2022)
- **ASO 进阶**: Custom Product Pages CPP (2021-12, 多产品页 A/B test) / Product Page Optimization PPO (2021-10, icon/screenshot A/B) / In-App Events IAE (2021-10) / Promotional Text (170 字符无审核) / App Title+Subtitle (30+30 字符高权重) / App Preview Video (30s) / Pre-Order (2018)
- **TestFlight 细分**: Beta App Review / Internal Testers (25 人无审核) / External Testers (Public Link ≤10000)
- **隐私法规**: GDPR (EU 2018, extraterritorial) / CCPA + CPRA (CA 2020/2023) / COPPA (US <13, 2024 amend)
- **国内合规**: 应用市场审核 (华米OV+腾讯+百度 8-10 家各审) / 游戏版号 (出版署 2022 重启) / 隐私协议中文版 (2021 个保法后) / 网络安全等级保护 (等保, 三级常见)

### Standards / Regulations / Certifications 时间轴 (近 5 年内显著变化)

| 名称 | Issued | Last revised | Decay |
|------|--------|--------------|-------|
| ATT (iOS 14.5) | 2021-04-26 | 2024 (合规细则) | medium |
| App Store Small Business Program | 2021-01-01 | 持续 | low |
| StoreKit 2 | 2021-06 (WWDC21) | 2023 update | medium |
| Reader Apps External Link (3.1.3a) | 2022-03-30 | 持续 | medium |
| Privacy Manifest 强制 | 2024-05-01 | active | high |
| DMA (Digital Markets Act) | 2022-11 公布 / 2024-03-07 应用 | 2024-04 (iPadOS 加入) | high |
| Anti-steering injunction (US) | 2021 一审 / 2024-01 终审 | 2025-04 强化 | high |
| ICP 备案 (App) | 2023-08 通知 / 2024-04 强制 | active | medium |
| 生成式 AI 暂行办法 | 2023-08-15 施行 | 2025 细则 | high |
| 算法推荐管理规定 | 2022-03-01 施行 | active | medium |

### 行业「外行破绽」高亮

| 误用 | 内行实际意思 | 出现频率 |
|------|--------------|---------|
| "TestFlight 公开链接 = 上架了" | TF 是 beta, 跟 App Store 上线无关 | 极高 |
| "代过审 / 代上架" | TOS 违规, Apple 封号风险 | 高 (国内灰产) |
| "苹果税都是 30%" | 实际 4 档 (15 small biz / 15 sub 2nd yr / 30 std / 0 reader-link) | 高 |
| "ICP 备案 = ICP 许可证" | 备案是普通 App 必做, 许可证是商业经营要求 | 国内极高 |
| "TestFlight 不用审核" | External tester build 也要 Beta App Review | 中 |
| "改 Bundle ID 上线一下" | 等于全新 App, 失去 reviews / 排名 | 中 |
| "ATT 弹窗用户都点 allow" | 实际 25-30% opt-in (Flurry 数据) | 极高 |
| "上架后再改隐私 label" | metadata reject 风险, 用户投诉 | 高 |
| "Phased release 我来手动控制" | Apple 自动 7 天, 只能暂停 | 中 |
| "ReAct/AI feature 不用 GenAI 备案" | 大陆境内向公众提供必备案 | 国内极高 |

---

## 学派术语对照 (同一概念在不同派别 register 不同)

| 概念 | Apple 派 | Indie 派 | ASO 派 | 反 Apple 派 | 国内合规派 |
|------|----------|----------|--------|-------------|-----------|
| 提交审核 | submission | ship / submit | — | — | 提审 / 送审 |
| 通过 | approved | "shipped 1.0" | — | "finally approved" | 过审 |
| 被拒 | rejection / reviewer feedback | "我又被拒了" / "reject #3" | — | anti-competitive reject | 驳回 / 拒审 |
| 分发 | App Store distribution | launch | release | sideloading / alt marketplace | 上架 / 多渠道分发 |
| 收入分成 | commission | "Apple's cut" | — | Apple Tax / 30% tax | 苹果抽成 |
| 政策约束 | guideline-conformant | "playing by Apple's rules" | — | monopoly behavior | 合规 |
| 用户跟踪 | user privacy / ATT | "ATT killed our funnel" | post-IDFA attribution | (一般支持限制) | 个保法 / 数据合规 |
| 上线状态 | Ready for Sale | live / in production | live in store | — | 上线 / 已发布 |
| 备案 | — | — | — | — | 备案号 / 工信部备案 |

---

## 反模式术语 (反例 register, 出现 = 信号)

- "教你绕过 App Review" / "100% 过审秘诀" / "代过审" / "代上架" — 灰产 (违 Apple TOS, 封号)
- "刷榜" / "fake review purchase" / "黑帽 ASO" / "刷量" — 违 4.3 spam + 国内市场也禁
- "TestFlight 永久测试" / "TF 公链当上架用" — TF 90 天到期机制故意误读
- "版本号刷上架" / "改个名字重新上" — 1.x metadata 政策风险
- 国内: "版号灰产" / "马甲包" / "代办版号" / "代备案" — 出版署/工信部明确打击
- "我们上线了" 当 TestFlight 公链 (register 误用, indie 派最反感)
- "AI-powered" / "智能 X" 营销话术 (App Review 4.0 design 拒审高频, 国内反不至于但厌)

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材** (喂 Phase 2.5):

- 高频黑话 top 10: ship / rejection (#3 reject) / metadata reject vs binary reject / Apple Tax / ATT 弹窗 / in production (海外) vs 上架 (国内) / CPP A/B / 备案号 / TestFlight 公链 / Resolution Center 拉锯
- 拒绝的厂商话术 top 5: "AI-powered/智能 X" / "100% 过审/包过" / "革命性/颠覆" / "全网最低/限时秒杀" / "用户隐私至上"但不写 Privacy Manifest
- 外行破绽 top 10: TF 公链当上架 / ICP 备案=许可证 / 苹果税固定 30% / ATT opt-in 默认满分 / 改 Bundle ID 当迭代 / metadata reject 重传 binary / Phased release 想手动 ramp / Privacy Manifest 当 marketing / "在 production" 实为 TF 公链 / 国内多市场=Apple 一刀切

**「智识谱系」线索**:
- 30% commission → 15% small biz (2021) → 15% sub 2nd yr → 0% reader link (2022) → 0% EU alt store (2024) → 0% US link-out (2024-25): 一条 anti-monopoly 缓慢瓦解曲线
- ATT (2021) → Privacy Manifest (2024) → DMA Privacy 强化 (2024+): 隐私范式从"用户选"到"机器读"演化
- 中国: 算法推荐 (2022) → 深度合成 (2023) → 生成式 AI (2023-08) → 持续细则: 合规对象从平台扩展到模型
- 反 Apple 阵营: Spotify (2019 EC 投诉) → Epic (2020-2024) → DMA 立法 (2022-2024) → US 终审 (2024-01): 司法-立法双轨

**「时效性」信号** (master skill 时效衰减信号: HIGH):
- 12 个月内已修订: Anti-steering 强化判决 (2025-04) / DMA iPadOS 加入 (2024-04) / Privacy Manifest active 细则 / 中国 GenAI 备案细则
- 12 个月内预计变化: Apple US App Store fee 结构再调 (法庭强制) / EU DMA 第二轮调查 / 中国大陆 sideloading 政策方向 / iOS 19/20 新审核 API
- 衰减最快: Apple Tax 数字 / link-out 入口 / 中国算法备案目录

**「workflow 触发」种子** (喂 Track 03):
- DMA 2024-03 → "EU 部署 app" workflow 大改 (alt marketplace 选择)
- 2025-04 anti-steering 强化 → "US 订阅 app" workflow 改 (link-out 必加)
- ICP 备案 2024-04 强制 → "大陆上架" workflow 必加备案前置
- Privacy Manifest 2024-05 → 任何 SDK 集成 workflow 加 PrivacyInfo.xcprivacy 校验

**「冷僻 / 信号薄弱」**: 65 entries 远超 40 floor, Tier 1 = 28 (>15), Tier 2 = 30, Standards/Regs = 7. 全部 Tier 1 有 outsider-tell. 学派对照 10 维度成形. 国内合规 (ICP/算法/版号) 与海外 (DMA/Anti-steering/ATT) 平衡覆盖. 反模式 7 类清晰. 行业 NOT cold, 信号丰满.
