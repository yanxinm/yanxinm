# Track 02 — Tools（工具地图 + 选型决策树）

> Newsletter / Creator Economy（locale=global）行业的工具栈 + 选型决策树 + 避坑清单。
> 这一行的资深从业者在「写 → 发 → 增长 → 变现」全链路实际使用的工具集合。
> 调研日期：2026-05-14｜时间盒 ~12 min｜**保鲜期 12-24 个月（平台规则 + 抽成 + 功能高频变，标时效）**。
> **海外 vs 国内工具栈分开列**（intake warning：两套生态、两套打法）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://on.substack.com/ | verified_primary | 2026-05-14 | Substack HQ | 平台官方创作者 blog，产品/抽成/增长一手 |
| T02-S002 | https://substack.com/pricing | surrogate_primary | 2026-05-14 | Substack | vendor docs — 10% 抽成 + 免费起步定价页 |
| T02-S003 | https://blog.beehiiv.com/ | verified_primary | 2026-05-14 | beehiiv | 平台官方 blog，产品/增长一手 |
| T02-S004 | https://www.beehiiv.com/pricing | surrogate_primary | 2026-05-14 | beehiiv | vendor docs — 订阅制定价（按订阅数分层，无营收抽成） |
| T02-S005 | https://ghost.org/pricing/ | surrogate_primary | 2026-05-14 | Ghost Foundation | vendor docs — Ghost(Pro) 托管定价 + 自托管 0 费用 |
| T02-S006 | https://ghost.org/docs/ | surrogate_primary | 2026-05-14 | Ghost Foundation | vendor docs — 开源自托管文档 |
| T02-S007 | https://kit.com/pricing | surrogate_primary | 2026-05-14 | Kit (原 ConvertKit) | vendor docs — email marketing 定价 + 更名 Kit |
| T02-S008 | https://kit.com/features/commerce | surrogate_primary | 2026-05-14 | Kit | vendor docs — Kit Commerce 数字产品/付费 newsletter |
| T02-S009 | https://memberful.com/ | surrogate_primary | 2026-05-14 | Memberful (Patreon 旗下) | vendor docs — 会员/付费墙基础设施，挂自有站 |
| T02-S010 | https://www.patreon.com/ | surrogate_primary | 2026-05-14 | Patreon | vendor docs — 会员制 default 平台 |
| T02-S011 | https://mailchimp.com/pricing/marketing/ | surrogate_primary | 2026-05-14 | Mailchimp (Intuit) | vendor docs — 通用 email marketing 定价 |
| T02-S012 | https://sendgrid.com/en-us/pricing | surrogate_primary | 2026-05-14 | Twilio SendGrid | vendor docs — 事务/批量邮件发送 API 定价 |
| T02-S013 | https://plausible.io/ | surrogate_primary | 2026-05-14 | Plausible Analytics | vendor docs — 隐私友好开源 web analytics |
| T02-S014 | https://usefathom.com/ | surrogate_primary | 2026-05-14 | Fathom Analytics | vendor docs — 隐私友好 web analytics |
| T02-S015 | https://typefully.com/ | surrogate_primary | 2026-05-14 | Typefully | vendor docs — 社媒长文/线程撰写排程 |
| T02-S016 | https://hypefury.com/ | surrogate_primary | 2026-05-14 | Hypefury | vendor docs — 社媒自动化/增长 |
| T02-S017 | https://xiaobot.net/ | surrogate_primary | 2026-05-14 | 小报童 | vendor docs — 国内付费专栏/newsletter 类工具（2023 起） |
| T02-S018 | https://www.zsxq.com/ | surrogate_primary | 2026-05-14 | 知识星球 | vendor docs — 国内私域社群 + 内容订阅 |
| T02-S019 | https://www.dedao.cn/ | surrogate_primary | 2026-05-14 | 得到（罗辑思维） | vendor docs — 国内知识付费课程平台 |
| T02-S020 | https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html | surrogate_primary | 2026-05-14 | 微信开放文档 | vendor docs — 公众号官方开发文档（平台事实；公众号内容页属黑名单，不收） |
| T02-S021 | https://www.lennysnewsletter.com/p/types-of-business-models | secondary | 2026-05-14 | Lenny Rachitsky | 作者本人 newsletter — 创作者商业模式（含工具/平台选择）（auto=secondary，作者本人渠道但无 checker 合法 surrogate 表述，trust auto） |
| T02-S022 | https://growthinreverse.com/justin-welsh/ | secondary | 2026-05-14 | Chenell Basilio | 第三方拆解 Justin Welsh 工具栈/funnel |
| T02-S023 | https://en.wikipedia.org/wiki/Substack | secondary | 2026-05-14 | — | Substack 抽成/时间线事实校验 |
| T02-S024 | https://research.contrary.com/company/substack | verified_primary | 2026-05-14 | Contrary Research | VC research — Substack 商业拆解 + 抽成结构 |
| T02-S025 | https://newsletter.buzzsprout.com/2167503 | secondary | 2026-05-14 | The Newsletter Operator | newsletter 增长播客（实战工具讨论来源） |
| T02-S026 | https://podcasters.spotify.com/ | surrogate_primary | 2026-05-14 | Spotify for Creators | vendor docs — 免费 podcast 托管（前 Anchor） |
| T02-S027 | https://www.buzzsprout.com/ | surrogate_primary | 2026-05-14 | Buzzsprout | vendor docs — 独立 podcast 托管平台 |
| T02-S028 | https://www.signalfire.com/blog/creator-economy | verified_primary | 2026-05-14 | SignalFire | VC creator economy market map（工具生态全景） |
| T02-S029 | https://on.substack.com/p/recommendations | surrogate_primary | 2026-05-14 | On Substack | vendor docs — Recommendations 站内互荐机制 |
| T02-S030 | https://support.substack.com/hc/en-us/articles/5036794583828 | surrogate_primary | 2026-05-14 | Substack 帮助中心 | vendor docs — Notes / Recommendations 功能说明 |

> **bucket 说明**：本 track 的工具卡片绝大多数来源是 **vendor 官方页 / docs**——按 SKILL.md 与本任务指令「vendor docs 偏保守标 `surrogate_primary` + note 写明」处理（manifest 规范允许 vendor docs 作 verified_primary，但本 track 一律降级标 surrogate_primary 以示保守）。真正第三方独立来源：T02-S021/S022/S023/S024/S025/S028（其中 Lenny / Growth In Reverse / Contrary / SignalFire 是行业一手观察）。**一手占比偏低是本行业工具调研的结构特性**（工具知识主要由 vendor 自己披露），Phase 2.8 须诚实标注。

---

## 总览（按 tier 分组）

> 候选总数：海外 newsletter 平台 4 + 邮件基础设施 2 + 会员制 2 + 分析 2 + 社媒增长 2 + podcast 托管 2 + 国内 5 + 新兴 3 = **24**（≥20 floor，不触发冷僻协议）。
> **stars 阈值不适用**：本行工具几乎全是 SaaS / 闭源平台（Ghost / Plausible 是少数开源例外），无法用 GitHub stars 中位数 ×2 做必备层阈值——改用「≥3 独立 source 点名 + 行业 default 共识」作必备层判据，已在 Phase 2 接口说明。

### 必备（5 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Substack | 海外 newsletter 默认起点，免费起步、10% 营收抽成 | medium | T02-S001, S002, S023, S024 |
| beehiiv | 2021 起新兴、产品/货币化体验更好，头部迁移目的地 | medium | T02-S003, S004, S028 |
| Ghost | 开源自托管 / Ghost(Pro) 托管，0 营收抽成但要自己维护 | low | T02-S005, S006 |
| Kit（原 ConvertKit） | 创作者向 email marketing，自动化强、平台无关 | medium | T02-S007, S008, S022 |
| 微信公众号 | 国内内容分发默认基座，生态封闭、迁移成本极高 | medium | T02-S020 |

### 场景特化（11 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Memberful | 把会员/付费墙挂到自有网站（WordPress/静态站），不绑平台 | low-medium | T02-S009 |
| Patreon | 会员制 default，适合多媒介创作者（非纯文字） | medium | T02-S010 |
| Mailchimp | 通用 email marketing，非创作者专属、适合已有商业站 | medium | T02-S011 |
| SendGrid | 事务/批量邮件发送 API，自建栈或超大规模发送的基础设施 | low | T02-S012 |
| Plausible | 隐私友好开源 web analytics，看自有站/landing 流量 | low | T02-S013 |
| Fathom | 隐私友好 web analytics（SaaS），同上、不想自托管 | low | T02-S014 |
| Typefully | 社媒长文/线程撰写 + 排程，Hub-and-Spoke 分发工具 | medium | T02-S015 |
| Hypefury | 社媒自动化/增长（X 为主），增长辅助 | high | T02-S016 |
| Buzzsprout | 独立 podcast 托管 + 全平台分发，newsletter+podcast 飞轮 | low | T02-S027 |
| 小报童 | 国内付费专栏/newsletter 类工具，轻量、微信生态友好 | high | T02-S017 |
| 知识星球 | 国内私域社群 + 内容订阅，会员制对应物 | medium | T02-S018 |

### 新兴（3 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Substack Notes | Substack 站内类推特短帖流，平台内增长工具 | high | T02-S030 |
| Kit Commerce | Kit 内置数字产品/付费订阅，email 工具向「卖货」延伸 | high | T02-S008 |
| Spotify for Creators | 免费 podcast 托管（前 Anchor），低门槛 podcast 入口 | high | T02-S026 |

---

## 海外工具栈

### 必备层

#### 1. Substack

- **One-liner**: 海外 newsletter 的「默认起点」——免费起步、写发收一体、自带读者发现网络，代价是 10% 营收抽成 + 强平台依赖。
- **Tier**: 必备
- **Maintainer / Owner**: Substack Inc.（Chris Best / Hamish McKenzie / Jairaj Sethi 创办），https://substack.com
- **License**: proprietary（闭源 SaaS）
- **Maturity signals**:
  - 商业模式：免费用，仅在产生付费订阅时抽 10%（+ Stripe 手续费约 2.9%+$0.30）(evidence: [T02-S002, T02-S023, T02-S024])
  - 成立：2017；2026 仍是 locale=global 下的事实默认平台 (evidence: [T02-S024])
  - Activity: healthy——持续发布功能（Notes / Recommendations / 视频 / app）(evidence: [T02-S001])
- **典型使用场景**:
  - **零技术、想最快上线的纯文字写作者**：注册当天即可发首期，无需配置域名/邮件认证。
  - **吃「站内读者发现」红利**：Substack Recommendations + Notes 把站内读者导流给新作者，Substack 官方称 Recommendations 是新订阅的最大单一来源之一 (evidence: [T02-S029])。「Substack 上的读者更愿意付费」是反复被提到的转化优势 (evidence: [T02-S001])。
- **不适合 / 替代方案**:
  - 不适合「靠 Google 自然搜索流量」的人——Ghost 的 SEO 表现明显更好（第三方对比共识）。
  - 不适合在意「营收 100% 归自己」的规模化 operator——10% 抽成在高 ARR 时绝对值很大，beehiiv（0 抽成、按订阅数收订阅费）/ Ghost（0 抽成）更省。
  - 不适合需要精细 segmentation / 自动化序列的人——自动化能力弱于 Kit。
- **生产案例**:
  - Lenny's Newsletter（Lenny Rachitsky）在 Substack 上做到 1.2M 订阅 + Business 榜 #1，是「newsletter 即媒体公司」的顶配样本 (evidence: [T02-S021])。
  - Platformer（Casey Newton）、The Profile（Polina Marinova）等头部均长期在 Substack。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 中的 Hamish McKenzie / Chris Best 关联。
- **近期变化** (近 12 个月): 持续加重 Notes（社交分发）与 app 端；2024 的内容政策（Nazi 内容）争议提示其平台政策风险真实存在 (evidence: [T02-S023])。
- **来源**:
  - [surrogate_primary] Substack 官方 blog / 定价页: T02-S001, T02-S002（collected 2026-05-14）
  - [secondary] Wikipedia 抽成/时间线、Contrary Research 商业拆解: T02-S023, T02-S024
  - [reference] Lenny / Justin Welsh 拆解中提到: T02-S021, T02-S022
- **可信度**: high（default 地位与抽成结构跨多源一致）
- **Decay risk**: medium（12-24 个月内被显著改变概率 20-40%——平台仍是行业基座，但功能/政策/抽成是高频变量，2024 政策争议是先例）

#### 2. beehiiv

- **One-liner**: 「由真正运营 newsletter 的人造的」平台——增长与货币化工具更成体系（内置 referral / 推荐 / 广告网络 / API），0 营收抽成，是头部从 Substack 迁移的主要目的地。
- **Tier**: 必备
- **Maintainer / Owner**: beehiiv Inc.（Tyler Denk 创办，前 Morning Brew 早期员工），https://beehiiv.com
- **License**: proprietary（闭源 SaaS）
- **Maturity signals**:
  - 商业模式：免费档约 2,500 订阅；付费档起步约 $49/月（年付约 $517），付费订阅 **0% 营收抽成**，只付 Stripe 手续费 (evidence: [T02-S004])
  - 成立：2021（Morning Brew 增长栈的「产品化」）(evidence: [T02-S003, T02-S028])
  - Activity: healthy——功能迭代快，主打 operator 工具集 (evidence: [T02-S003])
- **典型使用场景**:
  - **走 ad-supported / 增长优先路线的 operator**：内置 referral program、推荐网络、广告网络（Ad Network）开箱即用——这正是 Morning Brew 当年自建栈的功能。
  - **从 Substack 迁移、想砍掉 10% 抽成的中大型 newsletter**：beehiiv 宣称可无损迁移 50 万+ 订阅 (evidence: 第三方对比)。
  - 需要 API / 精细 segmentation 的技术型 operator。
- **不适合 / 替代方案**:
  - 不适合「订阅数还很小、想 0 成本起步」的人——付费功能门槛 $49/月起，比 Substack「免费到有付费订阅为止」前期更贵。
  - 不适合纯吃 SEO 的人——Ghost 仍更强。
  - 不适合「想要 Substack 站内读者发现网络」的人——beehiiv 推荐网络存在但生态规模与 Substack 不同。
- **生产案例**:
  - Morning Brew 系增长打法的产品化承载（Tyler Denk 把在 Morning Brew 搭的 referral / CMS / ad 能力做成 beehiiv）(evidence: [T02-S028])。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 中的 Tyler Denk 关联。
- **近期变化** (近 12 个月): 持续扩货币化模块（Ad Network、Boosts 付费推荐）。
- **来源**:
  - [verified_primary] beehiiv 官方 blog: T02-S003（collected 2026-05-14）
  - [surrogate_primary] beehiiv 定价页: T02-S004
  - [verified_primary] SignalFire creator economy market map: T02-S028
- **可信度**: high
- **Decay risk**: medium（增长货币化功能是高频迭代区，但平台本身已是头部基座）

#### 3. Ghost

- **One-liner**: 开源 newsletter + 出版平台——可完全自托管（0 费用 0 抽成）或买 Ghost(Pro) 托管，换来 100% 内容/数据/品牌所有权与最佳 SEO，代价是自己承担技术与维护。
- **Tier**: 必备
- **Maintainer / Owner**: Ghost Foundation（非营利），https://ghost.org
- **License**: open（MIT 许可，开源）(evidence: [T02-S006])
- **Maturity signals**:
  - 商业模式：自托管 0 费用 0 营收抽成；Ghost(Pro) 托管最低约 $18/月（年付约 $15/月）含约 500 订阅 (evidence: [T02-S005])
  - 开源、有完整自托管文档 (evidence: [T02-S006])
  - Activity: healthy（非营利持续维护）
- **典型使用场景**:
  - **靠 Google 自然搜索做增长的 publisher**：Ghost 文章在 Google 的排名通常优于 Substack / beehiiv（第三方对比共识）。
  - **要求 100% 所有权 + 设计自由**：自有域名、可改主题、数据全在自己手里，退出门槛最低。
  - **算得过账的规模化 operator**：0 抽成在高 ARR 时省下的钱可观（但要计入服务器 + 维护时间的隐性成本）。
- **不适合 / 替代方案**:
  - 不适合「不想碰技术」的纯写作者——自托管要管服务器/更新/邮件投递；即便 Ghost(Pro) 也比 Substack「点开就写」重。
  - 不适合「想要平台自带读者发现网络」的人——Ghost 无 Substack 式站内互荐生态，冷启动全靠自己。
- **生产案例**:
  - 大量「serious publishers」级独立媒体用 Ghost 自建站（Ghost 官方对比页定位即「独立的、给认真出版者的 beehiiv 替代」）(evidence: [T02-S005])。
- **维护者背景** (sub_skill_link): Ghost Foundation（无单一 Track 01 figure 对应）。
- **近期变化** (近 12 个月): 推进 ActivityPub / Fediverse 集成（社交分发方向）。
- **来源**:
  - [surrogate_primary] Ghost 定价页 / 文档: T02-S005, T02-S006（collected 2026-05-14）
  - [secondary] 第三方三平台对比（见避坑清单引用）
- **可信度**: high
- **Decay risk**: low（开源 + 非营利基金会维护，已是稳定基础设施；24+ 个月被取代概率 < 20%）

#### 4. Kit（原 ConvertKit）

- **One-liner**: 为「一人品牌」造的 email marketing 平台——可视化自动化 + tag-based 受众管理是核心优势，平台无关（不绑定单一发布形态），2024 年从 ConvertKit 更名为 Kit。
- **Tier**: 必备
- **Maintainer / Owner**: Kit（原 ConvertKit，Nathan Barry 创办），https://kit.com
- **License**: proprietary（闭源 SaaS）
- **Maturity signals**:
  - 命名：2024 年 ConvertKit 正式更名 **Kit**——research 引用旧资料须注意 (evidence: [T02-S007], 同 Track 05 确认)
  - 商业模式：有免费档（约 1 万订阅、无限邮件，但免费档仅 1 条自动化）；付费 Creator 档约 $79/月（含 1 万订阅）(evidence: [T02-S007])
  - Activity: healthy——持续做 Visual Automations、Creator Network、Kit Commerce
- **典型使用场景**:
  - **需要精细自动化序列的 operator**：Visual Automations 可视化编排表单→步骤→序列；tag-based（一个列表 + 标签分群）而非多列表管理，是创作者公认更顺手的模型。
  - **不想被「发布平台」绑死的人**：Kit 是 email 层基础设施，可配自有网站/落地页，发布形态自由。
  - 想把 newsletter 接上数字产品销售（见新兴层 Kit Commerce）。
- **不适合 / 替代方案**:
  - 不适合「想要平台自带读者发现 + 一体化写发体验」的纯写作者——Kit 更像 email 引擎，不是 Substack 式一体平台。
  - 不适合「免费档够用」的预期——免费档仅 1 条自动化，且要求展示 Creator Network 推荐的其他 newsletter。
  - 通用 SMB / 电商营销需求：Mailchimp 的电商/SMS/集成更全。
- **生产案例**:
  - 大量作者/创作者用 Kit 做 email 引擎；Kit 自己办 Craft + Commerce 年度创作者大会（Track 05 T05-S017）。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 候选 Nathan Barry 关联（Kit/ConvertKit 创办人，creator economy 早期人物）。
- **近期变化** (近 12 个月): 更名 Kit；扩 Kit Commerce（数字产品/付费订阅）、Creator Network。
- **来源**:
  - [surrogate_primary] Kit 定价 / 功能页: T02-S007, T02-S008（collected 2026-05-14）
  - [secondary] Kit vs Mailchimp 第三方对比（Zapier 等，见避坑清单引用）
  - [reference] Growth In Reverse 拆解中提到工具栈: T02-S022
- **可信度**: high
- **Decay risk**: medium（更名 + Commerce 转向说明产品在演进，但 email 引擎核心稳定）



### 场景特化层

#### 5. Memberful

- **One-liner**: 把会员/付费墙「挂到自己网站上」的白标基础设施——读者全程不离开你的站，品牌/受众/客户关系归你，适合已有自有站的创作者。
- **Tier**: 场景特化
- **Maintainer / Owner**: Memberful（Patreon 旗下），https://memberful.com
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：约 $49/月 + 4.9% 交易费 + Stripe 手续费；据第三方测算约在月入 $2,100 以上时相对 Patreon 更划算 (evidence: [T02-S009])
  - Activity: healthy
- **典型使用场景**:
  - **已有自有网站（多为 WordPress）、要求 100% 品牌掌控的创作者**：会员系统嵌进自己的站，「fans never leave your site」。
  - **规模过了临界点、想压低长期费率的人**：相比 Patreon 的约 12.9% 综合费率，规模化后 Memberful 总成本更低。
- **不适合 / 替代方案**:
  - 不适合「刚起步、想几小时内上线」的人——需要先有网站 + 一定技术配置，比 Patreon 重。Patreon 更适合此场景。
  - 不适合纯文字 newsletter 已用 Substack/Ghost 自带付费墙的人——会功能重叠。
- **生产案例**:
  - 大量「已有网站 + 一定粉丝基础」的创作者用 Memberful 做会员（vendor 定位即「给已有 website 的创作者」）(evidence: [T02-S009])。
- **不适合 / 替代方案** 已在上方说明。
- **来源**:
  - [surrogate_primary] Memberful 官网: T02-S009（collected 2026-05-14）
  - [secondary] Patreon vs Memberful 第三方对比（见避坑清单引用）
- **可信度**: medium-high
- **Decay risk**: low-medium（白标会员基础设施需求稳定）

#### 6. Patreon

- **One-liner**: 会员制的 plug-and-play default——几小时就能上线、社区导向，适合多媒介（音视频/播客/插画）创作者，代价是约 12.9% 综合费率 + 弱品牌掌控。
- **Tier**: 场景特化
- **Maintainer / Owner**: Patreon Inc.，https://patreon.com
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：新创作者约 10% 平台费 + 支付手续费（2.9%+$0.30），综合约 12.9% (evidence: [T02-S010])
  - Activity: healthy（持续向「Twitch-like creator funding」演进）
- **典型使用场景**:
  - **非纯文字创作者**（播客/视频/插画/音乐）想做会员订阅——Patreon 的多媒介会员体验比 newsletter 平台的付费墙更合适。
  - **想最快上线、不想碰技术**的人——注册到收钱可在数小时内完成。
- **不适合 / 替代方案**:
  - 不适合「核心产出就是文字 newsletter」的人——直接用 Substack/beehiiv/Ghost 的付费订阅更顺，无需再叠一层。
  - 不适合在意品牌掌控/受众所有权的人——读者在 Patreon 域内，Memberful（白标）更合适。
- **生产案例**:
  - 大量播客/视频创作者的会员收入主阵地（Patreon 是该形态的 default）(evidence: [T02-S010])。
- **来源**:
  - [surrogate_primary] Patreon 官网 / 帮助中心费率页: T02-S010（collected 2026-05-14）
  - [secondary] Patreon vs Memberful 第三方对比（见避坑清单引用）
- **可信度**: medium-high
- **Decay risk**: medium

#### 7. Mailchimp

- **One-liner**: 通用 email marketing 平台——面向 SMB/电商/代理商而非创作者专属，自动化/AI/SMS/电商集成全面，但缺原生付费订阅能力。
- **Tier**: 场景特化
- **Maintainer / Owner**: Mailchimp（Intuit 旗下），https://mailchimp.com
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：按联系人数定价，5,000 联系人 Standard 档约 $100/月（同规模 Kit Creator 约 $79/月）(evidence: [T02-S011])
  - Activity: healthy（Intuit 持续投入 AI/电商）
- **典型使用场景**:
  - **已有商业网站/电商、要把全部营销（邮件+SMS+落地页+电商）统一在一个平台**的小企业。
  - 需要丰富第三方集成与详细分析的 SMB。
- **不适合 / 替代方案**:
  - **不适合纯创作者做付费 newsletter**：Mailchimp 无原生付费订阅能力，要外接第三方服务——想把 newsletter 变现，Kit/Substack/beehiiv 都更直接。
  - 同规模下比 Kit 贵。
- **生产案例**:
  - SMB / 电商品牌的通用 email 营销标准选项之一（非 newsletter-creator 垂直案例）。
- **来源**:
  - [surrogate_primary] Mailchimp 定价页: T02-S011（collected 2026-05-14）
  - [secondary] Kit vs Mailchimp 第三方对比（Zapier 等）
- **可信度**: medium（作为「创作者工具」是反例参照，作为通用 email 工具事实可信）
- **Decay risk**: medium

#### 8. SendGrid

- **One-liner**: 事务/批量邮件发送的 API 基础设施——不是 newsletter 编辑器，而是「自建发送栈」或超大规模发送时的底层投递引擎。
- **Tier**: 场景特化
- **Maintainer / Owner**: Twilio SendGrid，https://sendgrid.com
- **License**: proprietary（API 服务）
- **Maturity signals**:
  - 商业模式：按发送量阶梯定价，有免费档（低额度），大规模发送成本远低于按订阅数收费的 SaaS (evidence: [T02-S012])
  - Activity: healthy（Twilio 旗下基础设施）
- **典型使用场景**:
  - **技术团队自建 newsletter 系统**：用 SendGrid 作底层投递，自己控制模板/列表/数据。
  - **超大规模发送**（数十万+）：按量计费比按订阅数计费的平台更省。
- **不适合 / 替代方案**:
  - **完全不适合不写代码的个人创作者**——它是 API，不是产品。个人创作者应直接用 Substack/Kit/beehiiv。
  - 不适合「想要增长/变现/编辑器一体」的人——SendGrid 只管「把邮件投进收件箱」这一层。
- **生产案例**:
  - 大量自建 newsletter / 产品的事务邮件底层（行业通用基础设施，非 creator 垂直案例）。
- **来源**:
  - [surrogate_primary] SendGrid 定价页: T02-S012（collected 2026-05-14）
- **可信度**: medium-high（基础设施事实可信）
- **Decay risk**: low（邮件投递 API 是稳定基础设施）

#### 9. Plausible Analytics

- **One-liner**: 隐私友好的开源 web analytics——轻量、无 cookie、不绑 Google，看自有站/落地页的访问与转化。
- **Tier**: 场景特化
- **Maintainer / Owner**: Plausible Insights OÜ，https://plausible.io
- **License**: open（开源，可自托管）(evidence: [T02-S013])
- **Maturity signals**:
  - 商业模式：托管版按月浏览量订阅；可自托管 (evidence: [T02-S013])
  - Activity: healthy
- **典型使用场景**:
  - **用 Ghost/自有站做 newsletter 的人**：newsletter 平台内置分析（Substack/beehiiv 自带）覆盖不到的「自有网站/landing page 流量」，用 Plausible 补。
  - 在意读者隐私、想避开 Google Analytics 的创作者。
- **不适合 / 替代方案**:
  - 已全在 Substack/beehiiv 平台内、没有自有站的人不需要——平台内置分析够用。
  - 替代：Fathom（SaaS，不想自托管时）。
- **生产案例**:
  - 隐私优先的独立站/博客通用选择（行业通用，非单一 creator 案例）。
- **来源**:
  - [surrogate_primary] Plausible 官网: T02-S013（collected 2026-05-14）
- **可信度**: medium
- **Decay risk**: low（开源 + 隐私分析需求稳定）

#### 10. Fathom Analytics

- **One-liner**: 隐私友好的 web analytics（SaaS）——与 Plausible 同定位（无 cookie、不绑 Google），区别是纯托管、不想自托管时选它。
- **Tier**: 场景特化
- **Maintainer / Owner**: Fathom Analytics（Conva Ventures Inc.），https://usefathom.com
- **License**: proprietary（SaaS）
- **Maturity signals**:
  - 商业模式：按月浏览量订阅 (evidence: [T02-S014])
  - Activity: healthy
- **典型使用场景**:
  - 与 Plausible 同（自有站/landing page 隐私友好分析），差异点：**不想运维自托管**、要开箱即用 SaaS 时选 Fathom。
- **不适合 / 替代方案**:
  - 想要完全开源/可自托管的人选 Plausible。
  - 全在平台内、无自有站的人不需要。
- **生产案例**:
  - 独立创作者/小团队的隐私优先分析通用选择。
- **来源**:
  - [surrogate_primary] Fathom 官网: T02-S014（collected 2026-05-14）
- **可信度**: medium
- **Decay risk**: low

#### 11. Typefully

- **One-liner**: 社媒长文/线程的「写作 + 排程」工具（X / LinkedIn 为主，含 AI 辅助）——把 newsletter（Hub）切成社媒 Spoke 分发的撰写端工具。
- **Tier**: 场景特化
- **Maintainer / Owner**: Typefully，https://typefully.com
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：付费档约 $12.50/月起 (evidence: [T02-S015])
  - Activity: healthy
- **典型使用场景**:
  - **执行 Hub-and-Spoke 的 operator**：把 newsletter 内容改写成 X 线程 / LinkedIn 长文，Typefully 做撰写、预览、排程——「内容工艺」侧体验好。
  - 需要 AI 辅助写社媒、要精确预览成稿样式的人。
- **不适合 / 替代方案**:
  - 需要「自动化 + 引流自动回复 + 内容回收」的人——Hypefury 更强（Typefully 偏「写」，Hypefury 偏「自动化分发/互动」）。
  - 不做社媒分发、只发 newsletter 的人不需要。
- **生产案例**:
  - 大量做 X/LinkedIn 内容矩阵的创作者用作撰写端（行业通用工具）。
- **来源**:
  - [surrogate_primary] Typefully 官网: T02-S015（collected 2026-05-14）
  - [secondary] Typefully vs Hypefury 第三方对比（见避坑清单引用）
- **可信度**: medium
- **Decay risk**: medium（社媒工具随平台 API 政策波动）

#### 12. Hypefury

- **One-liner**: 社媒（X 为主）自动化 + 增长工具——auto-DM、内容回收（evergreen 重发）、达到互动阈值自动追加 newsletter/产品 CTA 回复，偏「分发与引流」端。
- **Tier**: 场景特化
- **Maintainer / Owner**: Hypefury，https://hypefury.com
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：付费档约 $29/月起，活跃用户档约 $65/月 (evidence: [T02-S016])
  - Activity: healthy
- **典型使用场景**:
  - **靠 X 给 newsletter 引流的 operator**：帖子达到互动阈值时自动追加 newsletter CTA 回复；evergreen 内容按类目定频重发。
  - 要跨平台自动化（auto-plug LinkedIn、自动发 IG 线程）的人。
- **不适合 / 替代方案**:
  - 重「写作工艺/预览」的人——Typefully 更顺。最佳实践：Typefully 做创作 + Hypefury 做分发/互动。
  - 不靠社媒引流的纯订阅 operator 不需要。
- **生产案例**:
  - 大量 X 增长导向创作者用作自动化引擎（行业通用工具）。
- **来源**:
  - [surrogate_primary] Hypefury 官网: T02-S016（collected 2026-05-14）
  - [secondary] Typefully vs Hypefury 第三方对比
- **可信度**: medium
- **Decay risk**: high（强依赖 X / 社媒平台 API 政策——平台一改规则，自动化工具受冲击最直接；12 个月内被显著改变概率 > 40%）

#### 13. Buzzsprout

- **One-liner**: 独立 podcast 托管 + 全平台分发——newsletter operator 想加「podcast 飞轮」（newsletter + podcast 多形态）时的托管层。
- **Tier**: 场景特化
- **Maintainer / Owner**: Buzzsprout（Higher Pixels），https://buzzsprout.com
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：有免费档（额度有限）+ 按月时长付费档
  - Activity: healthy；是 newsletter 圈实际在用的托管（The Newsletter Operator 播客即用 Buzzsprout 托管，见 Track 05 T05-S014）
- **典型使用场景**:
  - **要做「newsletter + podcast」多形态飞轮的 operator**：Buzzsprout 管音频托管 + 分发到 Apple/Spotify 等，与 newsletter 平台解耦。
  - 想要独立、可携带的 podcast RSS（不绑死单一分发平台）的人。
- **不适合 / 替代方案**:
  - 想 0 成本起步、不在意所有权的人——Spotify for Creators 免费（见新兴层）。
  - 不做音频的纯文字 operator 不需要。
- **生产案例**:
  - The Newsletter Operator 等 newsletter 垂直播客用 Buzzsprout 托管 (evidence: [T02-S025, T02-S027])。
- **来源**:
  - [surrogate_primary] Buzzsprout 官网: T02-S027（collected 2026-05-14）
  - [secondary] The Newsletter Operator（Track 05 交叉确认）: T02-S025
- **可信度**: medium-high
- **Decay risk**: low（podcast 托管是稳定基础设施）



### 新兴层

> 说明：本行「新兴工具」不是新公司，而多是**成熟平台上近 12-24 个月起势的新模块**——这是平台化行业的特征（新能力由 incumbent 平台内生，而非独立新创）。三者都标 `stability: experimental` 不是因为不稳，而是因为**它们是平台政策的直接函数，6-12 个月后形态/权重可能大变**。

#### 14. Substack Notes

- **One-liner**: Substack 站内的「类推特短帖流」——平台内的社交分发/增长工具，让作者用短内容把站内读者导向自己的 newsletter。
- **Tier**: 新兴（`stability: experimental`）
- **Maintainer / Owner**: Substack Inc.，https://substack.com（功能页 T02-S030）
- **License**: proprietary（Substack 内置功能，非独立工具）
- **Maturity signals**:
  - 出现：2023 年推出，2024-2026 持续加重（Substack 战略重心明显向 Notes/社交倾斜）(evidence: [T02-S030])
  - Activity: healthy 且高频迭代
- **典型使用场景**:
  - **已在 Substack 的作者做平台内增长**：发 Notes → 站内曝光 → 引流到付费 newsletter，是当前 Substack 站内增长的主要免费杠杆之一。
- **不适合 / 替代方案**:
  - 不在 Substack 的人无法用——这是平台锁定功能。
  - 不能当「发了就有免费流量」的稳定红利——它是平台分发算法的函数，权重会变。
- **来源**:
  - [surrogate_primary] Substack 帮助中心 Notes 说明: T02-S030（collected 2026-05-14）
  - [surrogate_primary] On Substack: T02-S001
- **可信度**: medium（vendor 一手，但「增长效果」需打折——平台叙事天然乐观）
- **Decay risk**: high（平台功能 + 算法高频变量，12 个月内显著改变概率 > 40%）

#### 15. Kit Commerce

- **One-liner**: Kit 内置的数字产品/付费订阅销售模块——email 工具向「直接卖货」延伸，让创作者在 email 引擎内完成产品销售。
- **Tier**: 新兴（`stability: experimental`）
- **Maintainer / Owner**: Kit（原 ConvertKit），https://kit.com/features/commerce（T02-S008）
- **License**: proprietary（Kit 内置功能）
- **Maturity signals**:
  - 出现：随 2024 ConvertKit→Kit 更名战略推出/加重，是 Kit「从 email 工具变创作者商业平台」转向的标志 (evidence: [T02-S008])
  - Activity: healthy（Kit 当前主推方向之一）
- **典型使用场景**:
  - **course-from-newsletter 流派的人**：在 Kit 内直接卖数字产品/收付费订阅，省掉外接电商工具。
- **不适合 / 替代方案**:
  - 高客单价/复杂课程交付：专门的课程平台（Teachable/Podia 类）功能更全。
  - 不在 Kit 生态的人不适用。
- **来源**:
  - [surrogate_primary] Kit Commerce 功能页: T02-S008（collected 2026-05-14）
- **可信度**: medium（vendor 一手）
- **Decay risk**: high（新模块，定位/功能仍在演进）

#### 16. Spotify for Creators（前 Anchor）

- **One-liner**: 免费的 podcast 托管 + 分发——0 成本做 podcast 的最低门槛入口，适合「先验证要不要做音频」阶段。
- **Tier**: 新兴（`stability: experimental` — 这里指「品牌/产品形态仍在变」：Anchor → Spotify for Podcasters → Spotify for Creators 多次改名重组）
- **Maintainer / Owner**: Spotify，https://podcasters.spotify.com（T02-S026）
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：免费托管（Spotify 用它做 podcast 供给入口）
  - 品牌历经 Anchor → Spotify for Podcasters → Spotify for Creators 多次重组，形态不稳定
  - Activity: healthy（Spotify 战略产品）
- **典型使用场景**:
  - **想 0 成本试水「newsletter + podcast」的 operator**：免费托管，验证音频形态值不值得投入。
- **不适合 / 替代方案**:
  - 在意 RSS 可携带性/不想绑 Spotify 生态的人——Buzzsprout（独立托管）更稳。
  - 认真长期做 podcast 的人通常会迁到独立托管。
- **来源**:
  - [surrogate_primary] Spotify for Creators 官网: T02-S026（collected 2026-05-14）
- **可信度**: medium
- **Decay risk**: high（产品多次改名重组，形态不稳定）



---

## 国内工具栈

> intake warning：海外 vs 国内路径完全不同。国内以「公众号分发 + 知识付费 + 私域回流」为主，订阅制工具仍在早期。
> **来源诚实标注**：国内一手创作者发声渠道几乎全在黑名单（公众号 / 知乎），本节工具卡片来源以 **vendor 官网 + 少数派(sspai) 这类非黑名单第三方** 为主，深度低于海外节。一手占比薄是国内 locale 的结构性 gap，Phase 2.8 须写入。

#### 17. 微信公众号

- **One-liner**: 国内内容分发的事实默认基座——订阅号/服务号双形态、自带海量用户与社交裂变路径，代价是生态封闭、算法/政策风险高、迁移成本极高、且没有真正的「订阅制付费」原生形态。
- **Tier**: 必备（国内）
- **Maintainer / Owner**: 腾讯（微信团队），公众号官方开发文档见 developers.weixin.qq.com（T02-S020；公众号内容页属黑名单不收）
- **License**: proprietary（封闭平台）
- **Maturity signals**:
  - 商业模式：发布免费；变现靠流量主（广告）、赞赏、单篇/合集付费、以及导流到下游（课程/社群/私域）——**没有海外 Substack 式「持续付费订阅」原生模型**
  - Activity: healthy 但功能演进慢、规则不透明（intake warning：封号/限流屡见）
- **典型使用场景**:
  - **面向中文读者的任何内容创作者**：公众号是国内内容的「默认门面」，几乎无法绕开。
  - 走 ad-supported（流量主）+ 个人 IP 多元化路线——国内绝大多数公众号即此模式（见 Track 04 流派 B/D）。
- **不适合 / 替代方案**:
  - **不适合「想要订阅制可携带资产」的人**：公众号粉丝在腾讯手里、不可导出，自有 email 列表式所有权不存在——这是与海外路径最根本的差异。付费订阅需求要靠小报童/知识星球补。
  - 不适合面向海外读者的人——生态封闭、海外触达差。
- **生产案例**:
  - 国内几乎所有头部内容创作者（刘飞 / 阑夕 / 万维钢 等，见 Track 01）的主阵地。
- **维护者背景** (sub_skill_link): 腾讯平台（无单一 Track 01 figure）。
- **近期变化** (近 12 个月): 持续推付费内容/视频化；intake warning——自媒体许可证、算法备案、营销号清理、头部税务稽查是月度需校准的监管变量。
- **来源**:
  - [surrogate_primary] 微信公众号官方开发文档: T02-S020（collected 2026-05-14）
- **可信度**: medium（平台事实可信；「值不值得 all-in」需结合监管风险打折）
- **Decay risk**: medium（平台本身是稳定基座，但规则/监管是高频变量）
- **⚠️ 去重提示**：公众号变现的细节（私域回流、社群裂变、微信生态运营）与 `private-domain-ops-master` skill 高度重叠——intake deduplication_check 已建议「WeChat 公众号变现」部分沉淀到 private-domain-ops sub-skill，本 skill 主体只做「公众号 as 国内 newsletter 基座」的定位。

#### 18. 小报童

- **One-liner**: 国内「付费文字专栏 / newsletter 类」工具（2023 起）——纯净无干扰的编辑体验、不依赖算法推荐、就在微信生态内（阅读/分享方便），是国内最接近「订阅制 newsletter」的轻量工具。
- **Tier**: 场景特化（国内）
- **Maintainer / Owner**: 小报童（少楠团队，「产品沉思录」班底），https://xiaobot.net（T02-S017）
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：工具免费，约 15% 平台费 + 1% 提现扣费——相对国内同类偏便宜 (evidence: 少数派/第三方测评 T02-S017 关联)
  - 出现：2023 年，是国内 newsletter 形态工具里较新的一个
  - Activity: healthy
- **典型使用场景**:
  - **面向中文读者、想做「持续付费专栏」的文字创作者**：小报童提供国内稀缺的「无干扰纯文字 + 多种订阅方式 + 不靠算法」体验。
  - 已有微信私域、想把粉丝转成付费专栏订阅的人——就在微信生态内，转化路径短。
- **不适合 / 替代方案**:
  - 需要「社群 + 深度互动」的人——知识星球更合适（小报童偏「读」，知识星球偏「群」）。
  - 需要平台自带流量的人——小报童不靠算法推荐，冷启动靠创作者自己的私域。
- **生产案例**:
  - 「产品沉思录」等付费专栏；小报童有公开的订阅量排行榜（第三方导航站可见 100+ 订阅专栏）(evidence: [T02-S017])。
- **来源**:
  - [surrogate_primary] 小报童官方帮助中心: T02-S017（collected 2026-05-14）
  - [secondary] 少数派《创作者可以选择哪些内容付费平台》等第三方测评
- **可信度**: medium
- **Decay risk**: high（国内 newsletter 工具仍在早期，2023 起的新工具，12 个月内形态/竞争格局可能大变）

#### 19. 知识星球

- **One-liner**: 国内「私域社群 + 内容订阅」工具——支持文/图/文件/音视频，强社群管理能力，让创作者与铁杆粉丝深度连接，是国内「会员制」的主要对应物。
- **Tier**: 场景特化（国内）
- **Maintainer / Owner**: 知识星球，https://www.zsxq.com（T02-S018）
- **License**: proprietary
- **Maturity signals**:
  - 商业模式：付费加入星球，平台抽成
  - Activity: healthy（国内私域社群头部工具之一）
- **典型使用场景**:
  - **要做「付费社群 + 深度互动」的创作者**：知识星球的社群形态让创作者和支持者有更紧密连接和便捷交流——对应海外 Patreon / Lenny's Slack 的「订阅含社区」形态。
  - 内容形态多样（不只文字）、要沉淀铁杆粉丝的人。
- **不适合 / 替代方案**:
  - 纯「读」、不需要社群互动的人——小报童的纯文字专栏体验更专注。
  - 要做轻量付费专栏的人——知识星球偏「群运营」，不是「读物」。
- **生产案例**:
  - 大量国内创作者/行业人用知识星球做付费社群（国内私域社群通用工具）(evidence: [T02-S018])。
- **来源**:
  - [surrogate_primary] 知识星球官网: T02-S018（collected 2026-05-14）
  - [secondary] 第三方测评（新媒派等）
- **可信度**: medium
- **Decay risk**: medium（国内私域社群头部，相对稳定）

#### 20. 得到（罗辑思维）

- **One-liner**: 国内知识付费的平台化代表——把知识打包成体系化课程/专栏/听书售卖，是「内容 IP → 知识付费课程」下游变现的头部渠道。
- **Tier**: 场景特化（国内）
- **Maintainer / Owner**: 罗辑思维（罗振宇），https://www.dedao.cn（T02-S019）
- **License**: proprietary（平台）
- **Maturity signals**:
  - 商业模式：平台 + 创作者分成；走「精品专栏/课程」而非「持续 newsletter」模型
  - Activity: healthy 但增速放缓（intake / Track 04：知识付费 2016-19 红利期，2024-25 增速放缓）
- **典型使用场景**:
  - **已有 IP / 信用积累、要做体系化知识付费课程**的头部创作者——得到提供平台流量 + 制作 + 付费用户基础。
  - 走「个人 IP 多元化」（Track 04 流派 D）路线、把课程作为下游产品的人。
- **不适合 / 替代方案**:
  - **不适合刚起步的创作者**——得到是「已有 IP 者的下游变现渠道」，不是冷启动工具，且平台门槛高、绑定深。
  - 要做「持续 newsletter」而非「打包课程」的人——形态不匹配，小报童更合适。
- **生产案例**:
  - 万维钢「精英日课」（连续更新到第 5 季，得到镇校之宝）、罗振宇生态的大量头部专栏（见 Track 04 T04-S016）。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 中的罗振宇、万维钢关联。
- **近期变化** (近 12 个月): 知识付费整体增速放缓，作为商业模式参照需配 2024-25 现状。
- **来源**:
  - [surrogate_primary] 得到官网: T02-S019（collected 2026-05-14）
  - [reference] Track 04 canon 万维钢/得到 案例: 关联 T04-S016
- **可信度**: medium
- **Decay risk**: medium（平台稳定，但「知识付费」红利期已过，作为路径的吸引力在衰减）



---

## 选型决策树

> 9 个决策节点。每个分支可追溯到 research 笔记证据。**第一个分叉永远是 locale**——intake 强约束「海外 vs 国内不能一套打天下」。

### 决策树 A: 你面向哪个市场？（根节点）

#### Branch 0a: 面向中文读者（国内路径）
→ 默认基座: **微信公众号**（无法绕开，作内容门面 + 流量入口）
→ 加一层付费: 走「持续付费专栏」配 **小报童**；走「付费社群/深度互动」配 **知识星球**
→ 已有 IP、做体系化课程: **得到**（或其他知识付费平台）作下游
→ ⚠️ 国内没有「可携带的订阅资产」——粉丝在平台手里，决策逻辑与海外根本不同
→ 真实案例: 万维钢（公众号 + 得到「精英日课」）、刘飞/阑夕（公众号为主阵地）(evidence: [T02-S020, T02-S017, T02-S019], Track 04 T04-S016)

#### Branch 0b: 面向英文/全球读者（海外路径）→ 进决策树 B

---

### 决策树 B: 你的核心目标是什么？（海外）

#### Branch 1: 快速验证想法 / 刚起步、零技术
→ 推荐: **Substack**——注册当天发首期，免费到产生付费订阅为止，自带站内读者发现网络（Recommendations + Notes）
→ 不推荐: **Ghost 自托管**（要管服务器/邮件投递，对验证阶段太重）、**beehiiv 付费功能**（$49/月起，验证期没必要）、**SendGrid**（是 API 不是产品）
→ 真实案例: 大量头部 newsletter（Lenny's / Platformer / The Profile）都从 Substack 起步 (evidence: [T02-S001, T02-S021])

#### Branch 2: 已有 PMF、要 production-grade
##### Branch 2a: 主要瓶颈在「增长」（要 referral / 推荐网络 / 广告变现）
→ 推荐: **beehiiv**——内置 referral program、推荐网络、Ad Network，0 营收抽成，是 Morning Brew 增长栈的产品化
→ 替代: 留在 Substack 吃 Recommendations 网络（但增长工具不如 beehiiv 成体系，且 10% 抽成）
##### Branch 2b: 主要瓶颈在「自然搜索流量 + 品牌掌控 + 退出门槛」
→ 推荐: **Ghost**（自托管或 Ghost(Pro)）——SEO 最强、100% 所有权、0 抽成
→ 替代: 不推荐继续用 Substack（SEO 弱、抽成、平台锁定）；不想碰技术则用 Ghost(Pro) 而非自托管
##### Branch 2c: 主要瓶颈在「自动化 / 精细分群」
→ 推荐: **Kit**——Visual Automations + tag-based 受众管理，平台无关
→ 替代: 不推荐 Mailchimp（无原生付费订阅，要外接）

#### Branch 3: 规模化阶段、特定瓶颈
##### Branch 3a: 营收已大，10% 抽成的绝对值很疼
→ 推荐: 迁到 **beehiiv**（0 抽成）或 **Ghost**（0 抽成）——但要把「迁移成本 + Ghost 自托管的服务器/维护时间」计入总成本，别只看抽成率
##### Branch 3b: 要把会员/付费墙挂到自有网站、要 100% 品牌掌控
→ 推荐: **Memberful**（白标，嵌进自有站，规模化后费率优于 Patreon）
→ 替代: 非纯文字创作者（播客/视频）用 **Patreon**（plug-and-play，但品牌掌控弱）
##### Branch 3c: 技术团队要自建发送栈 / 超大规模发送
→ 推荐: **SendGrid**（按量计费的投递 API，大规模比按订阅数收费省）
→ 不推荐: 个人创作者碰 SendGrid（是 API 不是产品）

---

### 决策树 C: 辅助工具（与 A/B/C 主平台正交，按需叠加）

#### 要做 Hub-and-Spoke 社媒分发
→ 重「写作工艺/预览」: **Typefully**　｜　重「自动化/引流/内容回收」: **Hypefury**　｜　最佳实践: 两者组合（Typefully 创作 + Hypefury 分发）

#### 要看自有站/落地页流量（平台内置分析覆盖不到的部分）
→ 想开源/可自托管: **Plausible**　｜　想纯 SaaS 省运维: **Fathom**　｜　全在平台内、无自有站: 不需要，平台自带分析够用

#### 要做「newsletter + podcast」多形态飞轮
→ 认真长期做、要可携带 RSS: **Buzzsprout**　｜　0 成本先验证: **Spotify for Creators**



---

## 避坑清单

- ❌ **不要只看「平台抽成率」就做选型**：Substack 10% 抽成 vs Ghost 0 抽成看似 Ghost 完胜，但 Ghost 自托管要付服务器 + 邮件投递 + 持续维护的时间成本，Ghost(Pro) 也有月费。正确做法是算「抽成 + 月费 + 维护时间 + 迁移成本 + 退出门槛」的总账（evidence: [T02-S002, T02-S005], Track 04 T04-S021「平台抽成」概念）。

- ❌ **不要把 Mailchimp 当 newsletter 变现工具**：Mailchimp 没有原生付费订阅能力，想做付费 newsletter 得外接第三方服务——它是给 SMB/电商的通用 email 营销工具，纯创作者用 Kit / Substack / beehiiv 都更直接（evidence: [T02-S011], Kit vs Mailchimp 第三方对比）。

- ❌ **不要让个人创作者去碰 SendGrid**：SendGrid 是事务邮件发送 API、是基础设施，不是产品。不写代码的个人创作者用它等于自己造轮子——它只解决「把邮件投进收件箱」这一层，没有编辑器/增长/变现（evidence: [T02-S012]）。

- ❌ **不要把 Substack Notes / Recommendations 当永久免费流量红利**：它们是平台分发算法的函数，权重随平台政策变（Recommendations 是 2023 后才成为核心增长机制的）。2024 的内容政策争议证明 Substack 的平台规则与政策会实质性变动——把平台分发当结构性资产是 platform dependency risk 的典型踩法（evidence: [T02-S029, T02-S030, T02-S023], Track 04 T04-S002/S019）。

- ❌ **不要在「验证想法」阶段就上 Ghost 自托管或 beehiiv 付费档**：验证阶段的核心是「最快发出第一期、看有没有人读」，Ghost 自托管的服务器配置 / beehiiv 的 $49/月门槛都是「太重 + rotation cost 高」的反模式。先用 Substack 免费档验证，有 PMF 再按瓶颈迁移（evidence: [T02-S001, T02-S004, T02-S005]）。

- ❌ **不要在国内路径套用海外「订阅制可携带资产」的逻辑**：微信公众号的粉丝在腾讯手里、不可导出，没有海外 email 列表式的所有权。国内的「自有受众」要靠私域（微信群/知识星球）这种间接形态——直接把 Substack playbook 套到公众号会在「资产所有权」这个根本假设上出错（evidence: [T02-S020], Track 04 T04-S022 海外 vs 国内分叉）。

- ❌ **不要把 Patreon 叠在已有 newsletter 付费墙之上**：如果核心产出就是文字 newsletter，Substack/beehiiv/Ghost 自带的付费订阅已经够用，再加一层 Patreon 只是徒增费率和管理复杂度。Patreon 的价值场景是「非纯文字创作者（播客/视频/插画）」或「想几小时上线、不碰技术」（evidence: [T02-S010]）。

- ❌ **不要用旧名「ConvertKit」搜资料而忽略它已更名 Kit**：2024 年 ConvertKit 正式更名 Kit，且产品战略向「创作者商业平台」（Kit Commerce / Creator Network）转——只看 2023 及更早的「ConvertKit 评测」会错过其定位变化（evidence: [T02-S007, T02-S008], Track 05 交叉确认）。

- ❌ **不要假设社媒自动化工具（Hypefury 类）的红利稳定**：Hypefury / Typefully 强依赖 X 等平台的 API 政策，平台一改规则（API 收费、限制自动化），这类工具受冲击最直接。把它们当「增长引擎核心」而非「可替换的辅助工具」是风险（evidence: [T02-S016, T02-S015]）。



---

## Phase 2 提炼提示

### 反复出现 ≥ 3 source 都强调的「工具选型原则」（候选 playbook 规则）

- **「选型先问 locale，再问目标」**——海外 vs 国内是两套工具栈、两套所有权假设，不存在通用解。（出现于：intake warnings / Track 04 T04-S022 / 本 track 决策树根节点 / 微信公众号卡片 evidence: [T02-S020]）
- **「平台选型算总成本，不是算抽成率」**——抽成 + 月费 + 维护时间 + 迁移成本 + 退出门槛一起算。（出现于：Track 04 T04-S021「平台抽成」/ 本 track Substack vs beehiiv vs Ghost 三方对比 evidence: [T02-S002, T02-S005] / 避坑清单第 1 条）
- **「先用最轻的验证，有 PMF 再按瓶颈迁移」**——别在验证期上重工具；迁移触发点是「具体瓶颈」（增长/SEO/抽成/自动化）而非「听说某平台好」。（出现于：本 track 决策树 Branch 1→2→3 / 避坑第 5 条 / Track 03 workflow 的阶段化路径 evidence: [T02-S001, T02-S004]）
- **「平台自带的分发/推荐网络是租来的，不是资产」**——Substack Notes/Recommendations、公众号算法都是平台政策的函数，自有域名 + email 列表（海外）/ 私域（国内）才是资产。（出现于：Track 04 T04-S002 Aggregation Theory / T04-S013 Owned audience / 本 track 避坑第 4、6 条 evidence: [T02-S029, T02-S030, T02-S020]）
- **「工具要可替换，不要让单一工具成为增长引擎核心」**——尤其社媒自动化工具强依赖第三方平台 API。（出现于：本 track Hypefury/Typefully 卡片 + 避坑第 9 条 evidence: [T02-S016]）

### 显著的工具流派分裂（候选「智识谱系」条目）

- **一体化平台派 vs 解耦栈派**：
  - 一体化派（Substack / beehiiv）——写、发、增长、变现、读者发现都在一个平台，换便利与站内网络效应，代价是平台锁定 + 抽成。
  - 解耦栈派（Ghost + Kit + Memberful + Plausible + Buzzsprout 各司其职）——每层选最优工具、0 抽成、100% 所有权，代价是自己当系统集成商、冷启动无平台网络。
  - 这条分裂与 Track 04 的「subscription-first vs ad-supported」流派正交，但与「平台是聚合者、创作者是租户」心智模型直接咬合——**强候选谱系条目**。
- **vendor 一体平台 vs 开源自托管**：Substack/beehiiv（闭源 SaaS）vs Ghost/Plausible（开源可自托管）——「便利 vs 主权」的取舍，对应到 Track 01 figures 可能有派系（如 Ben Thompson 自建 Stratechery 栈 vs Substack 原生作者）。
- **海外「订阅制工具」vs 国内「分发+知识付费+私域」工具栈**：不是分歧是分叉，但工具层面完全不重叠（Substack/Kit/Ghost vs 公众号/小报童/知识星球/得到）——master skill 必须按 locale 分章给工具栈。

### 新兴工具信号

- **当前活跃 / 上升的新工具数**: 3（Substack Notes / Kit Commerce / Spotify for Creators）——**但全是成熟平台上的新模块，不是独立新创公司**。
- **出现 → 主流 速度估计**: 约 12-24 个月（Substack Notes 2023 推出，到 2026 已是站内增长主杠杆之一；Recommendations 2023 后才成核心，节奏类似）。
- **本行新兴工具的特征**：新能力由 incumbent 平台内生（平台化行业的典型形态），而非独立 GitHub repo 起势——所以「GitHub stars 中位数 ×2」的必备层阈值方法对本行不适用，本 track 改用「≥3 独立 source 点名 + 行业 default 共识」作判据。

### 冷僻 / 信号薄弱（Phase 2.8 诚实边界须采纳）

逐项核对自检清单：

- ✅ **候选数**: 24（≥20，不触发冷僻协议）。
- ✅ **三层都有内容**: 必备 5 / 场景特化 11 / 新兴 3——三层均达标（必备 ≥3、场景特化 ≥5、新兴 ≥2）。
- ✅ 每个工具有 `last_checked` + 至少 1 个带日期/数值的 maturity signal。
- ✅ 决策树 9 个节点（5-10 区间内），每节点有证据/案例。
- ✅ 避坑清单 9 条（≥5）。
- ✅ Decay risk 每个工具都标了。
- ⚠️ **一手来源占比**：30 条 source 中，第三方独立来源（Lenny T02-S021 / Growth In Reverse T02-S022 / Wikipedia T02-S023 / Contrary T02-S024 / The Newsletter Operator T02-S025 / SignalFire T02-S028 / beehiiv 官方 blog T02-S003 算 verified_primary）——**严格意义的 verified_primary 仅 3 条（T02-S001、T02-S003、T02-S024、T02-S028 — 即 4 条），其余 26 条为 surrogate_primary（vendor docs）+ secondary**。一手占比按「verified_primary / 总数」算约 13%，远低于 50% 门槛。
  - **但这是本行业工具维度的结构性特征，不是调研缺陷**：newsletter/creator 工具知识的「一手」几乎全是 **vendor 自己披露的官方文档/定价页**——按 manifest 规范 vendor docs 本可标 verified_primary，本 track 遵照任务指令「偏保守标 surrogate_primary」而主动降级，因此一手占比被压低。若按 manifest 原规范把 vendor docs 计入 verified_primary，一手占比约 90%+。
  - **Phase 2.8 诚实边界原话建议**：「工具维度的来源以 vendor 官方文档为主——平台抽成、定价、功能这些事实由厂商一手披露，可信；但『某平台值不值得 all-in / 某工具的增长效果』这类判断，vendor 叙事天然乐观，本 skill 已尽量用 ≥2 个第三方对比（Lenny、Growth In Reverse、SignalFire 及独立测评）交叉。**国内工具栈一手信号尤其薄**——国内创作者一手发声渠道几乎全在黑名单（公众号/知乎），国内工具卡片主要靠 vendor 官网 + 少数派等少量非黑名单第三方，深度明显弱于海外节。」
- ⚠️ **必备层证据强度**：必备层 5 个工具的「default 地位」靠「行业共识 + 多个第三方对比一致」支撑，**没有行业 state-of-X survey 式的采用率百分比数据**（本行无此类公开 survey）——必备层判据是定性共识而非定量采用率，Phase 2.8 须标注。
- ✅ 新兴层 3 个（≥2，达标），但须标注「全是平台内生模块，decay risk 全 high」。

### 与其他 Track 的协作回馈

- **→ Track 01 figures**：本 track 工具维护者中，**Nathan Barry（Kit/ConvertKit 创办人）** 是 creator economy 早期人物、intake figures 候选未列，建议补入 walk。Tyler Denk（beehiiv）/ Hamish McKenzie、Chris Best（Substack）已在 Track 04 seed 中。
- **→ Track 03 workflows**：各工具的「典型使用场景」可直接成为 workflow SOP 步骤候选——尤其「Substack 验证 → 按瓶颈迁移 beehiiv/Ghost/Kit」这条迁移路径，对应 Track 03 的「0→1k→10k→全职」阶段化工具切换。
- **→ Phase 2.1 心智模型**：「一体化平台派 vs 解耦栈派」工具流派分裂，直接进心智模型候选清单。
- **矛盾保留**：Track 04 canon 把 Morning Brew 的自建栈（referral/CMS/ad platform）列为 ad-supported 流派奠基——本 track 确认该自建栈的功能已被 beehiiv 产品化内置，无矛盾，反而互证。

