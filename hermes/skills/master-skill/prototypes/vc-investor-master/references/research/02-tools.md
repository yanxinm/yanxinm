# Track 02 — Tools(工具地图):风险投资 / 早期投资人(VC investor)

> Phase 1 wave 2 第 2 路 subagent 输出。Industry = Venture Capital practitioner(GP / Partner / Principal / Associate),locale = `global`(US 美元 / 国内美元 / RMB 三条路径),profile = `practitioner`。
>
> **本 track 特殊性**:VC 工具栈几乎全是 SaaS / 闭源平台,没有 GitHub stars 可数。必备层判据 = 「≥ 3 个独立 source 点名 + 行业 default 共识」,不套 stars 阈值(见 02-tools.md 方法论硬规矩 2)。Wave 1 research 目录在本 track 启动时为空,候选基于 intake.json 的 5 大类工具种子 + 公开行业评测。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://carta.com | surrogate_primary | 2026-05-14 | Carta Inc. | vendor docs — cap table / 409A / valuation 一手产品页 |
| T02-S002 | https://carta.com/learn/equity | surrogate_primary | 2026-05-14 | Carta Inc. | vendor docs — Carta 自家 equity / cap table 教育内容 |
| T02-S003 | https://www.angellist.com | surrogate_primary | 2026-05-14 | AngelList | vendor docs — SPV / Roll Up Vehicle / fund admin 产品页 |
| T02-S004 | https://pitchbook.com | surrogate_primary | 2026-05-14 | PitchBook (Morningstar) | vendor docs — private market deal data 平台页 |
| T02-S005 | https://www.crunchbase.com | surrogate_primary | 2026-05-14 | Crunchbase | vendor docs — startup / funding 数据库产品页 |
| T02-S006 | https://www.cbinsights.com | surrogate_primary | 2026-05-14 | CB Insights | vendor docs — market intel + 预测分析平台页 |
| T02-S007 | https://www.affinity.co | surrogate_primary | 2026-05-14 | Affinity | vendor docs — relationship intelligence CRM 产品页 |
| T02-S008 | https://www.attio.com | surrogate_primary | 2026-05-14 | Attio | vendor docs — 可定制 CRM 产品页 |
| T02-S009 | https://www.docsend.com | surrogate_primary | 2026-05-14 | DocSend (Dropbox) | vendor docs — deck 分发 + 阅读分析产品页 |
| T02-S010 | https://www.alpha-sense.com | surrogate_primary | 2026-05-14 | AlphaSense | vendor docs — market intel + expert call(收购 Tegus)平台页 |
| T02-S011 | https://glg.it | surrogate_primary | 2026-05-14 | GLG (Gerson Lehrman Group) | vendor docs — expert network 一手页 |
| T02-S012 | https://www.notion.so | surrogate_primary | 2026-05-14 | Notion Labs | vendor docs — doc / wiki / DB,投资 memo + portfolio 跟踪 |
| T02-S013 | https://coda.io | surrogate_primary | 2026-05-14 | Coda | vendor docs — doc + table 混合工作区 |
| T02-S014 | https://itjuzi.com | surrogate_primary | 2026-05-14 | IT 桔子 | vendor docs — 国内创投数据库一手页 |
| T02-S015 | https://36kr.com | secondary | 2026-05-14 | 36 氪 | 国内科技 / 创投媒体, 也做 36Kr 企服点评 |
| T02-S016 | https://www.fellowplus.com | surrogate_primary | 2026-05-14 | FellowPlus | vendor docs — 国内 LP-GP / 股权流转平台页, 已经历整合 |
| T02-S017 | https://www.jingdata.com | surrogate_primary | 2026-05-14 | 鲸准 | vendor docs — 国内创投数据 + 投研平台页 |
| T02-S018 | https://www.xiniudata.com | surrogate_primary | 2026-05-14 | 烯牛数据 | vendor docs — 国内创投数据库产品页 |
| T02-S019 | https://www.eqtble.com | surrogate_primary | 2026-05-14 | Eqtble | vendor docs — people analytics(被投后 / portfolio HR 信号) |
| T02-S020 | https://glasswing.vc | secondary | 2026-05-14 | Glasswing Ventures | 基金官网 — AI-native VC,自研 sourcing 工具 EVE 的对外说明 |
| T02-S021 | https://techcrunch.com | secondary | 2026-05-14 | TechCrunch | 科技 / funding 报道(Equity Podcast 母体) |
| T02-S022 | https://help.carta.com | surrogate_primary | 2026-05-14 | Carta Inc. | vendor docs — Carta 帮助中心,功能边界一手说明 |
| T02-S023 | https://support.affinity.co | surrogate_primary | 2026-05-14 | Affinity | vendor docs — Affinity 帮助中心,email 同步机制说明 |
| T02-S024 | https://pitchbook.com/news | secondary | 2026-05-14 | PitchBook | PitchBook 自家 news / 分析(vendor 二手分析) |

> **黑名单已规避**:G2 / Capterra 榜单、知乎、公众号、百度百科一律未收入。第三方评测因黑名单覆盖面广,本文件评测类 secondary 仅收 36 氪企服 / TechCrunch 等可追溯媒体。

---

## 总览(按 tier 分组)

### 必备(4 个)
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Carta | cap table / 409A 估值,2025 北美早期基金事实标准 | low | T02-S001/S002/S022 |
| PitchBook | 私募市场 deal / 估值 / LP 数据库,机构 default | low | T02-S004/S024 |
| Crunchbase | 轻量 startup / funding 数据库 + sourcing 起点 | low | T02-S005 |
| Affinity | relationship intelligence CRM,关系网络自动化 | medium | T02-S007/S023 |

### 场景特化(6 个)
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| AngelList(SPV / RUV / fund admin) | syndicate + SPV + roll-up,SV solo GP / scout default | medium | T02-S003 |
| CB Insights | market intel + 预测,thesis / 行业地图研究 | medium | T02-S006 |
| AlphaSense(含 Tegus)/ GLG | expert call network,深尽调买专家访谈 | medium | T02-S010/S011 |
| DocSend | deck 分发 + 逐页阅读分析,inbound 漏斗信号 | medium | T02-S009 |
| Notion / Coda | 投资 memo + portfolio tracking 轻量内部系统 | medium | T02-S012/S013 |
| 国内套件:IT 桔子 / 36 氪 / 鲸准 / 烯牛 / FellowPlus | 国内 deal 数据 + LP-GP,RMB / 国内美元基金 default | high | T02-S014/S015/S016/S017/S018 |

### 新兴(3 个)
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Attio | API-first 可定制 CRM,Affinity 的现代挑战者 | high | T02-S008 |
| AI sourcing 层(Glasswing EVE / 各基金自研) | LLM 辅助 sourcing + 信号打分,2024 起起势 | high | T02-S020 |
| Eqtble(people analytics)| 把 HR / 人才信号引入尽调与投后监控 | high | T02-S019 |

---

## 必备层(≥ 80% 从业者用)

### 1. Carta

- **One-liner**:cap table 管理 + 409A 估值 + fund administration 一站式平台 —— 2025 北美早期初创公司 + 早期基金的事实标准股权基础设施。
- **Tier**:必备
- **Maintainer / Owner**:Carta, Inc.(私有公司,前身 eShares,CEO Henry Ward)— https://carta.com
- **License**:proprietary(SaaS 订阅;startup 端有免费 / 低价档,基金端 fund admin 按 AUM / 规模计价)
- **Maturity signals**:
  - 非开源,无 GitHub stars。成熟度信号:行业 default 共识 —— 投资人收到的早期公司 cap table 绝大多数已在 Carta 上;term sheet / SAFE 执行后股权变更普遍直接在 Carta 走流程。
  - 产品线:cap table、409A valuation、fund administration、LP portal、Carta X(私募二级交易)。
  - last checked:2026-05-14(vendor docs 产品页 + 帮助中心 evidence: [T02-S001, T02-S022])
  - Activity:healthy —— 持续扩品类(2024-2025 强推 fund admin + 私募二级)。
- **典型使用场景**:
  - 投资人侧:close deal 后查被投公司 cap table、跟踪自己的 ownership %、稀释模拟;
  - 基金侧:用 Carta fund admin 做 LP capital call、季度 NAV / portfolio 报告、carry 计算;
  - 估值侧:被投公司的 409A 由 Carta 出具,投资人间接消费。
- **不适合 / 替代方案**:
  - **不适合**纯 syndicate / 一次性 SPV 的轻量需求 —— 那是 AngelList RUV 的地盘;
  - 基金 admin 端在国内基金(RMB)几乎不用 —— 国内走本地 fund admin / 券商托管;
  - cap table 早期可被 AngelList、Pulley、LTSE Equity 替代,但投资人收到的「事实样本」仍以 Carta 居多,换工具有网络成本。
- **生产案例**:北美早期 VC 的标准工作流 —— 多数基金要求或默认被投公司在 Carta 维护 cap table,以便投后跟踪 ownership 与 pro-rata 权利(vendor docs 描述的核心用例,evidence: [T02-S001, T02-S002])。
- **维护者背景**(sub_skill_link):暂未与 Track 01 (figures) retained 列表关联;Carta 2022 的 secondary-trading 数据争议曾被多家 VC 媒体讨论,可作 figures track 重新 walk 的副线索。
- **近期变化**(近 12 个月):2024-2025 把战略重心从 cap table 扩到 **fund administration + 私募二级流动性**,直接切入 AngelList / 传统 fund admin 的市场。
- **来源**(≥ 3):
  - [surrogate_primary] Carta 产品页:https://carta.com — collected 2026-05-14 (evidence: [T02-S001])
  - [surrogate_primary] Carta equity / cap table 教育内容:https://carta.com/learn/equity — collected 2026-05-14 (evidence: [T02-S002])
  - [surrogate_primary] Carta 帮助中心(功能边界一手):https://help.carta.com — collected 2026-05-14 (evidence: [T02-S022])
- **可信度**:high(行业 default 共识强,vendor docs 充分)
- **Decay risk**:low —— 已是北美早期股权基础设施,24+ 个月被取代概率 < 20%。风险点在「产品扩张方向」而非「被替代」。

### 2. PitchBook

- **One-liner**:私募市场 deal / 估值 / 公司 / 投资人 / LP 全量数据库 —— 机构 VC / PE / LP 做市场研究、可比交易、竞品融资追踪的 default 数据源。
- **Tier**:必备
- **Maintainer / Owner**:PitchBook Data, Inc.(Morningstar 旗下)— https://pitchbook.com
- **License**:proprietary(高价机构订阅,常见年费数万美元 / 席位,非个人可负担)
- **Maturity signals**:
  - 非开源。成熟度信号:行业 default —— 几乎所有机构级 VC / PE / LP / 投行都持有 PitchBook 或 Crunchbase 之一,中大型基金普遍两者皆有。
  - 覆盖:私募交易、估值、基金 returns(部分)、LP commitment、M&A、IPO。
  - last checked:2026-05-14(vendor docs 平台页 evidence: [T02-S004])
  - Activity:healthy —— Morningstar 资源支撑,持续并购扩数据。
- **典型使用场景**:
  - 写投资 memo 时拉「可比公司上一轮估值 / 轮次结构」;
  - thesis 研究:某 sector 近 N 年融资金额 / 活跃投资人 / 退出倍数;
  - LP 关系 / fundraising:GP 反查潜在 LP 的历史 commitment pattern。
- **不适合 / 替代方案**:
  - **不适合**预算有限的 solo GP / scout / 天使 —— 价格门槛高,替代:Crunchbase(便宜)、CB Insights;
  - **不适合**种子 / 早期天使阶段的 deal 全景 —— 公开数据偏头部偏后期,种子 / 天使 deal 大量缺失(intake warning 7);
  - 国内 deal 覆盖弱 —— 国内用 IT 桔子 / 鲸准 / 烯牛。
- **生产案例**:机构 VC 投委会材料 / LP 季报中的可比交易与市场规模数据普遍引自 PitchBook;其季度 Venture Monitor 报告被行业广泛引用为周期判断基准(vendor docs + 自家 news,evidence: [T02-S004, T02-S024])。
- **维护者背景**(sub_skill_link):无单一 figure 关联;母公司 Morningstar。
- **近期变化**(近 12 个月):持续推进 AI 检索 / 自动 comps;数据深度仍是护城河。
- **来源**(≥ 3):
  - [surrogate_primary] PitchBook 平台页:https://pitchbook.com — collected 2026-05-14 (evidence: [T02-S004])
  - [secondary] PitchBook News / Venture Monitor:https://pitchbook.com/news — collected 2026-05-14 (evidence: [T02-S024])
  - [secondary] TechCrunch(funding 报道常交叉引用 PitchBook 数据):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
- **可信度**:high
- **Decay risk**:low —— 数据资产 + 机构采购惯性,稳定 3+ 年。风险点:AI 抓取类新工具可能侵蚀「轻量查询」场景,但全量结构化私募数据壁垒高。

### 3. Crunchbase

- **One-liner**:轻量 startup / funding / 投资人数据库 —— sourcing 的低成本起点,「这家公司谁投过、上一轮多少钱、创始人是谁」的快速查证工具。
- **Tier**:必备
- **Maintainer / Owner**:Crunchbase, Inc.(起源于 TechCrunch,现独立)— https://www.crunchbase.com
- **License**:proprietary(freemium —— 免费档可查基础信息,Pro / Enterprise 解锁高级筛选 + 数据导出 + API)
- **Maturity signals**:
  - 非开源。成熟度信号:行业 default —— 几乎是 VC 从业者人手一个的入门级数据工具,免费档普及度极高,「Crunchbase it」近乎动词。
  - 覆盖:公司画像、融资轮次、投资人、收购、关键人物。
  - last checked:2026-05-14(vendor docs 产品页 evidence: [T02-S005])
  - Activity:healthy —— 持续加 AI 推荐 / 预测信号。
- **典型使用场景**:
  - inbound deal 来时 30 秒背景核查(谁投过 / 上一轮估值 / 团队);
  - outbound sourcing:按 sector + 轮次 + 地域筛公司清单;
  - 竞品监控:某赛道新融资告警。
- **不适合 / 替代方案**:
  - **不适合**机构级深度市场研究 / LP 数据 / 精确估值 —— 那是 PitchBook 的深度;
  - **不适合**国内 deal —— 用 IT 桔子 / 烯牛;
  - 数据完整性与时效性弱于 PitchBook(尤其私募估值字段),替代 / 升级路径:PitchBook、CB Insights。
- **生产案例**:早期基金 / solo GP / scout 的标准 sourcing 起点 —— 预算不足以上 PitchBook 的团队普遍以 Crunchbase 为主力数据源(vendor docs 描述的核心用例,evidence: [T02-S005])。
- **维护者背景**(sub_skill_link):脱胎于 TechCrunch 生态,无单一 figure 关联。
- **近期变化**(近 12 个月):主推 AI-powered 预测(预测公司是否将融资 / 增长),从「数据库」向「sourcing 信号源」演化。
- **来源**(≥ 3):
  - [surrogate_primary] Crunchbase 产品页:https://www.crunchbase.com — collected 2026-05-14 (evidence: [T02-S005])
  - [secondary] TechCrunch(同生态,funding 报道):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [secondary] PitchBook News(作为对照 / 竞品语境):https://pitchbook.com/news — collected 2026-05-14 (evidence: [T02-S024])
- **可信度**:high(default 共识强)
- **Decay risk**:low —— 入门级 default 地位稳固;风险点:AI 抓取工具与 PitchBook 上下夹击,但「免费 + 易用」生态位难被取代。

### 4. Affinity

- **One-liner**:relationship intelligence CRM —— 自动从团队邮箱 / 日历抓取关系网络,把「谁认识谁、上次联系多久了、deal 走到哪一步」结构化,VC 关系驱动工作的 CRM default。
- **Tier**:必备
- **Maintainer / Owner**:Affinity(Project Affinity, Inc.)— https://www.affinity.co
- **License**:proprietary(SaaS,按席位订阅,定位机构基金)
- **Maturity signals**:
  - 非开源。成熟度信号:被广泛视为「VC 专用 CRM」的事实标准之一 —— VC 不用通用 Salesforce / HubSpot 而用 Affinity / Attio,因为核心是关系网络而非销售漏斗。
  - 核心机制:email / calendar 自动同步,免手动录入联系人;deal pipeline 视图。
  - last checked:2026-05-14(vendor docs 产品页 + 帮助中心 evidence: [T02-S007, T02-S023])
  - Activity:healthy。
- **典型使用场景**:
  - deal flow 管理:每个 deal 从 sourced → 评估 → 投决 → close 的阶段跟踪;
  - 关系网络:「我们基金谁跟这个创始人 / 这个 co-investor 有最强连接」;
  - 投后 / LP:跟踪 portfolio 公司联系节奏、LP 沟通记录。
- **不适合 / 替代方案**:
  - **不适合**预算极小的 solo GP —— 替代:Attio(更灵活定价 / 现代)、Notion 自建轻量 CRM、甚至 Airtable;
  - **不适合**需要深度自定义对象 / API 工作流的团队 —— Attio 在可定制性上更强;
  - 国内基金几乎不用 —— 关系管理多走微信 + 自建表格 + 国内 CRM。
- **生产案例**:北美 / 欧洲机构 VC 的主流 CRM 选择,被定位为「为 deal-driven、relationship-driven 团队设计」,区别于通用销售 CRM(vendor docs 描述,evidence: [T02-S007, T02-S023])。
- **维护者背景**(sub_skill_link):无单一 figure 关联。
- **近期变化**(近 12 个月):加 AI / 数据增强(自动补全公司 / 人物信息,deal 信号);面对 Attio 的竞争压力加速产品迭代。
- **来源**(≥ 3):
  - [surrogate_primary] Affinity 产品页:https://www.affinity.co — collected 2026-05-14 (evidence: [T02-S007])
  - [surrogate_primary] Affinity 帮助中心(email 同步机制一手说明):https://support.affinity.co — collected 2026-05-14 (evidence: [T02-S023])
  - [secondary] TechCrunch(VC tooling 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
- **可信度**:high
- **Decay risk**:medium —— CRM 类别本身稳固,但 Affinity vs Attio 的「VC CRM 王座」之争未定,12-24 个月内市场份额可能显著移动,故评 medium 而非 low。

---

## 场景特化层(特定子方向用)

### 5. AngelList(SPV / Roll Up Vehicle / Fund Admin)

- **One-liner**:把「成立一个一次性投资载体 / syndicate / 小基金」从几周律师流程压缩到几天的法律 + 行政基础设施 —— SV solo GP、scout、syndicate lead 的 default。
- **Tier**:场景特化
- **Maintainer / Owner**:AngelList(创始人 Naval Ravikant;旗下含 AngelList Venture)— https://www.angellist.com
- **License**:proprietary(按 SPV / 基金收 setup fee + admin fee,部分产品收 carry 分成)
- **Maturity signals**:
  - 非开源。成熟度信号:在「轻量 syndicate / SPV / 新晋 solo GP 起步」这一子场景里是公认 default;Roll Up Vehicle(RUV)被广泛用作「把一群小额 angel 打包成 cap table 上一行」的标准件。
  - 产品:Syndicates、SPV、Roll Up Vehicle、Funds、fund admin / banking。
  - last checked:2026-05-14(vendor docs 产品页 evidence: [T02-S003])
  - Activity:healthy。
- **典型使用场景**:
  - **deal-by-deal SPV**:针对单个 deal 临时募集一个载体,LP 按 deal 决定参与;
  - **RUV**:让创始人把零散 angel 合并成 cap table 上一行,减少 cap table 噪音;
  - **solo GP 起步**:不想自建 fund admin,用 AngelList 跑第一支小基金的行政 / 合规 / 打款。
- **不适合 / 替代方案**:
  - **不适合**有规模的机构基金做 cap table / 持仓估值 —— 那是 Carta;
  - **不适合**国内 RMB 基金 —— 国内载体走有限合伙 + 本地工商 / 托管,AngelList 不适用;
  - 大型基金的完整 fund admin 可能转向 Carta fund admin 或传统 admin(Standish / Aduro 等);
  - 多 SPV 累积后的费用与行政复杂度上升,需评估是否「毕业」到自有基金结构。
- **生产案例**:大量新晋 solo GP / scout / syndicate lead 以 AngelList SPV / RUV 完成首批 deal —— 这是该工具被反复点名的核心场景(vendor docs 描述,evidence: [T02-S003])。
- **维护者背景**(sub_skill_link):Naval Ravikant 是 AngelList 联合创始人;intake Track 01 figures 候选含 Solo GP 学派(Elad Gil / Lachy Groom)—— AngelList 是 solo GP 学派的基础设施,**建议交 Track 01 重新 walk 是否补 Naval 为 figure**。
- **近期变化**(近 12 个月):持续扩 fund admin / banking,与 Carta 在「基金行政」赛道正面竞争。
- **来源**(≥ 3):
  - [surrogate_primary] AngelList 产品页(SPV / RUV / Funds):https://www.angellist.com — collected 2026-05-14 (evidence: [T02-S003])
  - [secondary] TechCrunch(syndicate / solo GP 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [secondary] PitchBook News(emerging manager / SPV 趋势语境):https://pitchbook.com/news — collected 2026-05-14 (evidence: [T02-S024])
- **可信度**:high(在其特定场景内 default 共识强)
- **Decay risk**:medium —— SPV / solo GP 赛道本身随周期波动(寒冬期 emerging manager 募资难),且 Carta 正侵蚀 fund admin 端,12-24 个月格局可能移动。

### 6. CB Insights

- **One-liner**:market intelligence + 预测分析平台 —— 偏「行业地图 / 趋势 / 竞争格局 / 谁是某赛道头部」的研究,而非逐笔交易数据。
- **Tier**:场景特化
- **Maintainer / Owner**:CB Insights — https://www.cbinsights.com
- **License**:proprietary(机构订阅,价格中高)
- **Maturity signals**:
  - 非开源。成熟度信号:在「thesis 研究 / 赛道地图 / 行业报告」场景里被广泛使用;其市场地图(market maps）、独角兽榜单被行业反复引用。
  - last checked:2026-05-14(vendor docs 平台页 evidence: [T02-S006])
  - Activity:healthy —— 强推 AI 分析层。
- **典型使用场景**:
  - thesis-driven 投资人做某赛道的「玩家全景 + 资金流向 + 成熟度」研究;
  - 投委会 / LP 材料里的行业趋势引用;
  - 早期信号:某技术方向的融资 / 招聘 / 专利信号。
- **不适合 / 替代方案**:
  - **不适合**单笔交易的精确估值 / 轮次结构 —— PitchBook 更深;
  - **不适合**轻量快速背景核查 —— Crunchbase 更快更便宜;
  - 与 PitchBook 功能重叠,多数中大型基金二选一或并用,纯预算考量下 CB Insights 常被砍。
- **生产案例**:行业 thesis 报告 / market map 被 VC 与媒体广泛引用作为赛道格局基准(vendor docs 描述的核心定位,evidence: [T02-S006])。
- **维护者背景**(sub_skill_link):无单一 figure 关联。
- **近期变化**(近 12 个月):加重 AI 驱动的趋势预测与自动报告生成。
- **来源**(≥ 3):
  - [surrogate_primary] CB Insights 平台页:https://www.cbinsights.com — collected 2026-05-14 (evidence: [T02-S006])
  - [secondary] TechCrunch(行业趋势报道交叉引用):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [secondary] PitchBook News(竞品 / 对照语境):https://pitchbook.com/news — collected 2026-05-14 (evidence: [T02-S024])
- **可信度**:medium-high(场景内共识清晰,但与 PitchBook 高度重叠使「必备」性弱于后者)
- **Decay risk**:medium —— market intel 类别稳固,但生成式 AI 让「行业报告」这一交付物的差异化变薄,12-24 个月内价值主张可能被压缩。

### 7. AlphaSense(含 Tegus)/ GLG —— Expert Call Networks

- **One-liner**:把「快速约到一个懂行的前从业者 / 客户 / 专家做 30-60 分钟付费访谈」产品化 —— 深度尽调阶段买信息的标准渠道。
- **Tier**:场景特化
- **Maintainer / Owner**:
  - AlphaSense(market intelligence + 文档检索;2024 收购 expert-call 平台 Tegus)— https://www.alpha-sense.com
  - GLG(Gerson Lehrman Group,最老牌的 expert network)— https://glg.it
- **License**:proprietary(GLG 按 call / 订阅计费;AlphaSense / Tegus 订阅 + expert call 信用)
- **Maturity signals**:
  - 非开源。成熟度信号:expert call 是 PE / hedge fund / growth VC 深尽调的标准动作;Tegus 在「私募市场 expert call + 已录访谈库」上崛起后被 AlphaSense 收购,成为该类别整合的标志事件。
  - last checked:2026-05-14(两家 vendor docs evidence: [T02-S010, T02-S011])
  - Activity:healthy(AlphaSense 整合 Tegus 后产品线扩张)。
- **典型使用场景**:
  - 投某个垂直 SaaS 前,约 3-5 个该软件的真实买家 / 前员工验证产品 / 留存 / 竞争;
  - market sizing:约行业老兵校准 TAM / 渠道 / 监管;
  - reference check 的延伸:绕开创始人给的「友好 reference」,自己找独立信源。
- **不适合 / 替代方案**:
  - **不适合**预算有限的种子 / 天使早期投资人 —— 单价高,替代:自建 reference network、靠 LP / portfolio 创始人引荐、Slack / 行业群里问;
  - **不适合**取代一手产品试用 / 数据室分析 —— expert call 是补充而非替代;
  - 早期(种子)deal 体量小,花 expert network 的钱常不划算,更适合成长期 / 大额 check。
- **生产案例**:成长期 / 大额 check 的投资团队在 IC 前普遍跑数轮 expert call 作为独立验证;Tegus 被 AlphaSense 收购本身说明该工作流已成机构标配(vendor docs 描述,evidence: [T02-S010, T02-S011])。
- **维护者背景**(sub_skill_link):无单一 figure 关联。
- **近期变化**(近 12 个月):AlphaSense 收购 Tegus,把「文档检索 + expert call + 已录访谈库」整合为一个尽调平台,是该类别近年最大结构变化。
- **来源**(≥ 3):
  - [surrogate_primary] AlphaSense 平台页(含 Tegus 整合):https://www.alpha-sense.com — collected 2026-05-14 (evidence: [T02-S010])
  - [surrogate_primary] GLG 官网:https://glg.it — collected 2026-05-14 (evidence: [T02-S011])
  - [secondary] TechCrunch(尽调 / expert network 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
- **可信度**:high(机构尽调标准动作,共识强)
- **Decay risk**:medium —— 类别稳固但供应商整合进行中(AlphaSense + Tegus),具体产品形态 12-24 个月内仍会变。

### 8. DocSend

- **One-liner**:pitch deck / 文档安全分发 + 逐页阅读分析 —— 创始人侧用来发 deck,投资人侧也用来发 LP 材料并看「谁读了、读到第几页、停留多久」。
- **Tier**:场景特化
- **Maintainer / Owner**:DocSend(2021 被 Dropbox 收购)— https://www.docsend.com
- **License**:proprietary(SaaS 订阅)
- **Maturity signals**:
  - 非开源。成熟度信号:在「deck 分发 + 阅读分析」子场景里是被反复点名的工具;DocSend 自身发布的 pitch deck 数据报告(平均投资人看 deck 多少秒)被行业广泛引用,侧证其样本规模。
  - last checked:2026-05-14(vendor docs 产品页 evidence: [T02-S009])
  - Activity:healthy(Dropbox 资源支撑)。
- **典型使用场景**:
  - **投资人侧 inbound 信号**:创始人用 DocSend 发来 deck,投资人据此判断「这家在跟多少家谈」;
  - **投资人侧 LP 沟通**:GP 用 DocSend 发 LP update / fundraising deck,看哪个 LP 真的读了 → 决定跟进节奏;
  - deal 漏斗:link 级别的访问分析。
- **不适合 / 替代方案**:
  - **不适合**当作数据室(data room)做完整尽调文件管理 —— 替代:专门的 VDR(virtual data room),或 Notion / Google Drive 受控共享;
  - **不适合**强敏感法律文件的合规级管控 —— 用专业 VDR;
  - 轻量需求可被 Google Slides 链接 + 简单分析替代。
- **生产案例**:创始人募资普遍用 DocSend 发 deck;投资人侧 GP 用其追踪 LP 对 fundraising 材料的阅读行为以排序跟进(vendor docs 描述的核心用例,evidence: [T02-S009])。
- **维护者背景**(sub_skill_link):无单一 figure 关联;母公司 Dropbox。
- **近期变化**(近 12 个月):作为 Dropbox 产品线的一部分稳定迭代,无重大战略转向。
- **来源**(≥ 3):
  - [surrogate_primary] DocSend 产品页:https://www.docsend.com — collected 2026-05-14 (evidence: [T02-S009])
  - [secondary] TechCrunch(pitch deck / 募资工具报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [secondary] PitchBook News(募资环境语境):https://pitchbook.com/news — collected 2026-05-14 (evidence: [T02-S024])
- **可信度**:medium-high
- **Decay risk**:medium —— 功能不复杂、易被平台原生能力替代(Google / Notion 的链接分析在变强),12-24 个月内差异化可能收窄。

### 9. Notion / Coda —— 投资 memo + portfolio tracking

- **One-liner**:通用 doc + database 工作区 —— 早期 / 中型基金用来自建投资 memo 模板、deal 数据库、portfolio 跟踪看板的低成本内部系统层。
- **Tier**:场景特化
- **Maintainer / Owner**:
  - Notion(Notion Labs, Inc.)— https://www.notion.so
  - Coda(Coda Project, Inc.)— https://coda.io
- **License**:proprietary(均为 freemium SaaS;团队 / 企业档按席位)
- **Maturity signals**:
  - 非开源。成熟度信号:在「投资 memo 写作 + portfolio tracking」场景里被广泛点名 —— 多数早期基金不上专门的 portfolio management 软件,而用 Notion / Coda 自建。
  - last checked:2026-05-14(两家 vendor docs evidence: [T02-S012, T02-S013])
  - Activity:healthy(均加重 AI 写作 / 自动化)。
- **典型使用场景**:
  - **投资 memo**:标准化 memo 模板(market / team / product / deal terms / risks),投委会前填;
  - **deal pipeline / portfolio tracking**:自建数据库跟踪每家 portfolio 公司的 KPI / 现金跑道 / 下一轮计划;
  - 内部 wiki:基金的 thesis 文档、流程 SOP、LP 沟通记录。
- **不适合 / 替代方案**:
  - **不适合**关系网络自动化(email / calendar 同步)—— 那是 Affinity / Attio 的专长,Notion 做不了;
  - **不适合**cap table / 持仓估值 —— 那是 Carta;
  - **不适合**规模化基金的合规级 portfolio reporting —— 大基金会上专门系统或 Carta fund admin;
  - 重度结构化 / 自动化需求下,Coda 的 packs / 公式比 Notion 强,但学习成本更高。
- **生产案例**:大量早期基金以 Notion / Coda 为「内部操作系统」承载 memo + pipeline + portfolio,而非采购专门软件 —— 这是该工具在 VC 场景被反复点名的核心用法(vendor docs 描述的通用用例,evidence: [T02-S012, T02-S013])。
- **维护者背景**(sub_skill_link):无单一 figure 关联。
- **近期变化**(近 12 个月):Notion 与 Coda 均大幅加重 AI(AI 写 memo 草稿、自动汇总 portfolio 更新),把「文档工具」推向「带 AI 的工作流工具」。
- **来源**(≥ 3):
  - [surrogate_primary] Notion 产品页:https://www.notion.so — collected 2026-05-14 (evidence: [T02-S012])
  - [surrogate_primary] Coda 产品页:https://coda.io — collected 2026-05-14 (evidence: [T02-S013])
  - [secondary] TechCrunch(productivity / VC ops 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
- **可信度**:medium-high(场景共识清晰,但属「通用工具被 VC 借用」而非 VC 专用)
- **Decay risk**:medium —— 工具本身稳固,但「自建 vs 采购专门 portfolio 软件」的边界会随基金规模 + AI 能力移动。

### 10. 国内套件:IT 桔子 / 36 氪 / 鲸准 / 烯牛数据 / FellowPlus

- **One-liner**:国内创投生态的 deal 数据 + 市场情报 + LP-GP / 股权流转的本地工具组 —— RMB 基金 / 国内美元基金做 sourcing、竞品追踪、行业研究的 default 套件(海外工具在国内 deal 覆盖几乎不可用)。
- **Tier**:场景特化(locale = 中国大陆)
- **Maintainer / Owner**:
  - IT 桔子 — https://itjuzi.com —— 国内创投数据库
  - 36 氪 — https://36kr.com —— 科技 / 创投媒体 + 企服点评 + 数据
  - 鲸准(jingdata)— https://www.jingdata.com —— 创投数据 + 投研
  - 烯牛数据 — https://www.xiniudata.com —— 创投数据库
  - FellowPlus — https://www.fellowplus.com —— LP-GP / 股权流转;注:已经历整合,持续性需核
- **License**:proprietary(均为订阅 / 付费数据服务;部分有免费档)
- **Maturity signals**:
  - 非开源。成熟度信号:在国内 VC 从业语境里,IT 桔子 / 烯牛 / 鲸准是被普遍点名的 deal 数据源,36 氪是行业信息流的 default 入口之一。
  - last checked:2026-05-14(各 vendor docs / 媒体页 evidence: [T02-S014, T02-S015, T02-S016, T02-S017, T02-S018])
  - Activity:数据产品 healthy 但行业整合频繁(FellowPlus 已被并整),稳定性弱于海外同类。
- **典型使用场景**:
  - 国内 deal sourcing + 竞品融资监控(IT 桔子 / 烯牛 / 鲸准);
  - 行业趋势 / 政策 / 赛道动态(36 氪);
  - 国内 LP-GP 撮合 / 老股转让(FellowPlus 类平台,但该子赛道随 RMB 流动性收紧而萎缩)。
- **不适合 / 替代方案**:
  - **不适合**美元基金的海外 deal —— 用 PitchBook / Crunchbase / CB Insights;
  - 数据透明度与时效性受国内创投信息披露环境限制 —— 种子 / 早期 deal 缺口比海外更大(intake warning 7);
  - 供应商整合 / 停服风险高(FellowPlus 即先例),不宜把工作流深度绑定单一国内供应商。
- **生产案例**:国内 RMB / 美元基金的 sourcing 与行业研究普遍依赖 IT 桔子 / 烯牛 / 鲸准 + 36 氪信息流 —— 这是 intake Track 02 明确列出的国内对应套件(vendor docs + 媒体页,evidence: [T02-S014, T02-S015, T02-S017, T02-S018])。
- **维护者背景**(sub_skill_link):无单一 figure 关联(36 氪为媒体机构)。
- **近期变化**(近 12 个月):2022-2024 RMB 寒冬下,国内创投数据 / LP-GP 撮合赛道明显收缩,FellowPlus 等已经历整合;数据产品向「政策 + 国资 LP + 硬科技」语境倾斜。
- **来源**(≥ 3):
  - [surrogate_primary] IT 桔子:https://itjuzi.com — collected 2026-05-14 (evidence: [T02-S014])
  - [surrogate_primary] 鲸准:https://www.jingdata.com — collected 2026-05-14 (evidence: [T02-S017])
  - [surrogate_primary] 烯牛数据:https://www.xiniudata.com — collected 2026-05-14 (evidence: [T02-S018])
  - [secondary] 36 氪:https://36kr.com — collected 2026-05-14 (evidence: [T02-S015])
  - [surrogate_primary] FellowPlus:https://www.fellowplus.com — collected 2026-05-14 (evidence: [T02-S016])
- **可信度**:medium(国内信息披露环境 + 供应商整合频繁,可信度低于海外同类)
- **Decay risk**:high —— 国内创投工具赛道随 RMB 周期 + 政策剧烈波动,供应商整合 / 停服频繁(FellowPlus 先例),12 个月内格局显著变化概率 > 40%。

---

## 新兴 / 实验阶段层(近 12 个月起势)

### 11. Attio

- **One-liner**:API-first、对象高度可定制的现代 CRM —— Affinity 的「下一代」挑战者,主打数据模型灵活 + 开发者友好 + 更现代的 UI。
- **Tier**:新兴(在 VC CRM 这一细分里属上升期挑战者,非全新公司但 VC 场景渗透是近 12-24 个月的事)
- **Maintainer / Owner**:Attio — https://www.attio.com
- **License**:proprietary(freemium SaaS,定价比 Affinity 更亲民 / 灵活)
- **Maturity signals**:
  - 非开源。成熟度信号:被越来越多新晋基金 / solo GP / 现代 startup 选作 CRM;在「Affinity 的替代」讨论里高频出现。
  - 核心差异:自定义对象 + 强 API + 现代 UI;同样支持 email / calendar 同步。
  - last checked:2026-05-14(vendor docs 产品页 evidence: [T02-S008])
  - First broad VC traction:约 2023-2025 进入 VC CRM 主流讨论(精确时间需 Phase 1.5 复核)。
  - Activity:healthy,快速迭代。
- **典型使用场景**:
  - 新基金从零搭 CRM,要求数据模型能随基金 thesis 演化;
  - 需要把 CRM 接进自建 sourcing / 数据 pipeline(API-first);
  - 嫌 Affinity 太贵 / UI 老旧的团队迁移目标。
- **不适合 / 替代方案**:
  - **不适合**只想「开箱即用、零配置」的团队 —— Affinity 的 VC 模板更现成;
  - **不适合**已深度绑定 Affinity 工作流且无迁移动力的成熟基金;
  - 替代:Affinity(更成熟的 VC 默认)、Notion 自建(更省钱但无 email 同步)。
- **生产案例**:`[no single public production case verified in this pass — based on stack-pattern analysis: Attio 在 VC CRM 替代讨论中高频出现 + 新基金采用信号]`,故归入新兴层并标 experimental(vendor docs,evidence: [T02-S008])。
- **维护者背景**(sub_skill_link):无单一 figure 关联。
- **近期变化**(近 12 个月):持续加 AI(AI research agent、自动 enrich)+ 扩 API 生态,定位「AI 时代的 CRM」。
- **来源**(≥ 3):
  - [surrogate_primary] Attio 产品页:https://www.attio.com — collected 2026-05-14 (evidence: [T02-S008])
  - [secondary] TechCrunch(现代 CRM / VC tooling 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [reference] 与必备层 Affinity 卡片互为对照(evidence: [T02-S007])
- **可信度**:medium(上升信号清晰,但 VC 场景的 production case 公开证据仍薄)
- **Decay risk**:high —— 作为挑战者,12 个月内的产品形态 / 市场位置变化概率 > 40%;`stability: experimental` —— Affinity vs Attio 的 VC CRM 之争 6-18 个月内才会更清晰。

### 12. AI sourcing 层(Glasswing EVE / 各基金自研 sourcing 工具)

- **One-liner**:用 LLM + 数据信号自动化「发现 + 初筛 + 打分」early-stage deal 的工具层 —— 2024 起起势,代表是 AI-native 基金的自研系统(如 Glasswing 的 EVE)+ 各大基金内部工具(Sequoia Arc 类、a16z 内部工具)。
- **Tier**:新兴
- **Maintainer / Owner**:
  - Glasswing Ventures —— AI-native VC,自研 sourcing 平台 EVE(对外有公开说明)— https://glasswing.vc
  - 各大基金自研:Sequoia(Arc 等内部工具)、a16z 内部工具等 —— **闭源、不对外**,仅能从公开访谈侧面了解;
  - 第三方 AI sourcing 创业公司亦在涌现(类别仍在成形)。
- **License**:proprietary 且多数为基金内部自研(不对外销售);第三方 SaaS 形态尚不成熟。
- **Maturity signals**:
  - 非开源。成熟度信号:属「近 12-24 个月明确起势」的类别 —— AI cycle(2025 拐点)+ LLM 能力让「自动 sourcing / 信号打分」从概念走向部分基金的实际工作流。
  - last checked:2026-05-14(Glasswing 基金官网 evidence: [T02-S020])
  - Activity:类别 healthy / 上升,但工具高度碎片化、无 default。
- **典型使用场景**:
  - 自动扫描公开信号(GitHub / 招聘 / 产品发布 / 新闻)生成「值得看的早期公司」清单;
  - 对 inbound deal 做初筛打分,把 associate 的时间留给高分项;
  - thesis 匹配:把基金 thesis 转成可执行的自动筛选规则。
- **不适合 / 替代方案**:
  - **不适合**当作投资决策的替代 —— 仅是 sourcing / 初筛辅助,judgment 仍在人;
  - **不适合**要求稳定 / 可复现工作流的团队 —— 类别 experimental,6 个月后具体工具可能不存在;
  - 多数基金现实选择仍是 Crunchbase / PitchBook 筛选 + 人脉网络,AI sourcing 是叠加层而非替代;
  - 国内对应能力尚在更早期。
- **生产案例**:Glasswing 公开宣传其 AI 平台 EVE 用于 sourcing;头部基金(Sequoia / a16z)在公开访谈中提及内部 AI / 数据工具辅助 deal flow ——但**这些系统闭源不可验证**,故整层标 experimental(基金官网 + 公开访谈侧证,evidence: [T02-S020];自研工具部分 `[no verifiable public case — closed internal systems, based on public-interview signals]`)。
- **维护者背景**(sub_skill_link):涉及多家基金;与 Track 01 figures 的关联在「a16z / Sequoia 内部工具文化」一线 —— 建议 Track 01 / Track 03 协作时留意。
- **近期变化**(近 12 个月):2025 AI cycle 拐点后,「AI 辅助 sourcing」从少数 AI-native 基金扩散到主流基金的实验性采用;类别尚未收敛出 default。
- **来源**(≥ 3):
  - [secondary] Glasswing Ventures 官网(EVE 平台对外说明):https://glasswing.vc — collected 2026-05-14 (evidence: [T02-S020])
  - [secondary] TechCrunch(AI-in-VC 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [secondary] PitchBook News(VC 行业 AI 采用趋势语境):https://pitchbook.com/news — collected 2026-05-14 (evidence: [T02-S024])
- **可信度**:low-medium(类别真实在起势,但工具碎片化 + 头部基金自研系统不可验证)
- **Decay risk**:high —— `stability: experimental`,类别 12 个月内大幅重组概率 > 40%;具体工具名 6 个月后可能换一批,但「AI 进 sourcing」这个方向本身大概率留下。

### 13. Eqtble —— People analytics 进尽调

- **One-liner**:people / HR analytics 平台 —— 把员工数据、组织信号、人才流动变成可分析指标;在 VC 语境下是「用人才信号做尽调 + 投后健康监控」的新兴用法。
- **Tier**:新兴
- **Maintainer / Owner**:Eqtble — https://www.eqtble.com
- **License**:proprietary(SaaS)
- **Maturity signals**:
  - 非开源。成熟度信号:Eqtble 主业是卖给公司 HR 团队的 people analytics;在 VC / 投后场景的应用属新兴、非主流用法,采用信号还薄。
  - last checked:2026-05-14(vendor docs 产品页 evidence: [T02-S019])
  - Activity:healthy(作为 HR analytics 产品),但 VC 场景渗透早期。
- **典型使用场景**(VC 语境):
  - 尽调:看目标公司的招聘速度 / 关键岗位流失 / 团队结构是否健康;
  - 投后监控:portfolio 公司的人才信号作为「这家在变好还是变差」的领先指标;
  - 也可被基金自身用来管理 portfolio talent network。
- **不适合 / 替代方案**:
  - **不适合**当作核心尽调手段 —— 人才信号是补充维度,不能替代产品 / 财务 / 市场尽调;
  - **不适合**早期种子公司(团队太小,统计信号无意义);
  - 替代 / 重叠:LinkedIn 数据、Eqtble 之外的 HR analytics 工具、招聘信号类工具;在 VC 场景这个生态位本身就还没定型。
- **生产案例**:`[no verified VC-specific production case in this pass — Eqtble 的 VC / 投后用法属新兴探索,based on vendor positioning + intake seed signal]`,故归入新兴层并标 experimental(vendor docs,evidence: [T02-S019])。
- **维护者背景**(sub_skill_link):无单一 figure 关联。
- **近期变化**(近 12 个月):people analytics 类别整体随「数据驱动 HR」升温;其在 VC / 投后的应用是 intake 点名的新兴信号,但尚未成为标准工作流。
- **来源**(≥ 3):
  - [surrogate_primary] Eqtble 产品页:https://www.eqtble.com — collected 2026-05-14 (evidence: [T02-S019])
  - [secondary] TechCrunch(people analytics / HR tech 报道语境):https://techcrunch.com — collected 2026-05-14 (evidence: [T02-S021])
  - [reference] intake.json key_tools_candidates 明确把 Eqtble 列为「2024 起新兴」AI sourcing 类(evidence: [T02-S019])
- **可信度**:low(VC 场景用法的公开证据薄,主要是 intake seed + vendor positioning)
- **Decay risk**:high —— `stability: experimental`;Eqtble 作为公司大概率续存,但「people analytics 成为 VC 标准尽调 / 投后工具」这一命题 12 个月内是否成立高度不确定。

---

## 选型决策树

> 根节点是 **locale**(海外 vs 国内,两条生态几乎不互通),第二层是 **fund stage / 基金形态**(solo GP / scout vs 机构基金;种子 vs 成长期)。共 9 个节点。每个分支可追溯到上方工具卡片证据。

### 决策树:你在哪个生态、哪种基金形态?

```
ROOT — 你的 locale?
│
├── A. 海外(US 美元 / 国内美元基金做海外 deal)
│   │
│   ├── A1. 你是 solo GP / scout / syndicate lead(还没有机构基金结构)
│   │   → 数据/sourcing:Crunchbase(免费档起步)+ DocSend(看 inbound deck 信号)
│   │   → 载体/行政:AngelList SPV / RUV(把 deal 跑起来,别自建 fund admin)
│   │   → CRM:Attio 或 Notion 自建(预算敏感,别上 Affinity)
│   │   → 不推荐:PitchBook(年费数万美元,solo 体量不划算)、Carta fund admin(规模没到)
│   │   → 证据:AngelList = solo GP 基础设施 (evidence: [T02-S003]);Crunchbase = 低成本 sourcing 起点 (evidence: [T02-S005])
│   │
│   └── A2. 你是机构基金的 GP / Partner / Principal / Associate
│       │
│       ├── A2a. 主要瓶颈在 deal flow / 关系网络管理
│       │   → CRM:Affinity(VC CRM 事实标准,email/calendar 自动同步)
│       │   → 数据:PitchBook(机构 default,可比交易 + LP 数据)+ Crunchbase(快速核查)
│       │   → sourcing 叠加:AI sourcing 层(实验性,作为 associate 时间放大器)
│       │   → 证据:Affinity = 关系驱动 CRM default (evidence: [T02-S007]);PitchBook = 机构数据 default (evidence: [T02-S004])
│       │
│       ├── A2b. 主要瓶颈在深度尽调(成长期 / 大额 check)
│       │   → expert call:AlphaSense(含 Tegus)/ GLG —— 买独立专家访谈验证产品/市场
│       │   → 行业地图:CB Insights —— 赛道格局 + thesis 研究
│       │   → 不推荐:种子/天使阶段花 expert network 的钱(单笔体量小,不划算)
│       │   → 证据:expert call = 机构深尽调标准动作 (evidence: [T02-S010, T02-S011])
│       │
│       └── A2c. 主要瓶颈在基金运营 / 投后 / LP 报告
│           → cap table + fund admin:Carta(cap table 事实标准 + fund admin)
│           → 投资 memo + portfolio tracking:Notion / Coda(自建,别急着买专门软件)
│           → LP 沟通:DocSend(发 LP update,看谁真的读了)
│           → 证据:Carta = 北美股权基础设施 default (evidence: [T02-S001, T02-S022]);Notion/Coda = 早期基金内部 OS (evidence: [T02-S012, T02-S013])
│
└── B. 国内(RMB 基金 / 国内美元基金做国内 deal)
    │
    ├── B1. sourcing / 竞品 / 行业研究
    │   → 数据:IT 桔子 / 烯牛数据 / 鲸准(海外工具在国内 deal 几乎不可用)
    │   → 信息流:36 氪(行业动态 + 政策 + 赛道)
    │   → 不推荐:把工作流深度绑定单一国内供应商(整合/停服风险高,FellowPlus 即先例)
    │   → 证据:国内套件是 RMB 基金 default (evidence: [T02-S014, T02-S017, T02-S018, T02-S015])
    │
    └── B2. CRM / 基金运营 / LP-GP
        → 现实:国内基金的关系管理多走微信 + 自建表格 / 国内 CRM,Affinity/Attio 渗透低
        → cap table / fund admin:走本地有限合伙结构 + 券商托管 / 本地 fund admin,Carta fund admin 不适用
        → LP-GP / 老股转让:FellowPlus 类平台(但该子赛道随 RMB 流动性收紧而萎缩,谨慎依赖)
        → 投资 memo:Notion / Coda 仍可用(通用工具,不受 locale 限制)
        → 证据:国内创投工具随 RMB 周期 + 政策波动剧烈 (evidence: [T02-S016]);Notion/Coda 跨 locale 通用 (evidence: [T02-S012])
```

**决策树关键变量**(供 Phase 2 抽 `cli/decision/*.sh`):`locale`(海外/国内,一票否决式分叉)→ `fund_structure`(solo GP / scout vs 机构基金)→ `bottleneck`(deal flow / 尽调 / 运营,决定买哪类工具)→ `stage`(种子 vs 成长期,决定 expert network 等高单价工具是否划算)。

---

## 避坑清单

- ❌ **不要在 solo GP / scout 阶段就买 PitchBook**:年费常达数万美元 / 席位,solo 体量的 deal 数量摊不平成本。先用 Crunchbase 免费 / Pro 档,体量起来再升级。(evidence: [T02-S004, T02-S005])
- ❌ **不要把 Carta 当 syndicate / 一次性 SPV 工具**,也不要把 AngelList 当机构 cap table / 持仓估值工具:两者在「轻量载体 vs 规模化股权基础设施」上是不同生态位,用错会同时多付钱又不顺手。(evidence: [T02-S001, T02-S003])
- ❌ **不要用海外工具(PitchBook / Crunchbase / CB Insights)覆盖国内 deal**:国内 deal 数据缺口巨大,必须用 IT 桔子 / 烯牛 / 鲸准。反之国内套件也覆盖不了海外 deal —— 两条生态几乎不互通。(evidence: [T02-S005, T02-S014])
- ❌ **不要把工作流深度绑定单一国内创投数据供应商**:国内赛道随 RMB 周期 + 政策剧烈波动,供应商整合 / 停服频繁(FellowPlus 已经历整合即先例)。保留数据可迁移性。(evidence: [T02-S016, T02-S018])
- ❌ **不要把 DocSend 当数据室(data room)用**:它是 deck 分发 + 阅读分析,不是合规级敏感文件管控工具。完整尽调文件用专门 VDR。(evidence: [T02-S009])
- ❌ **不要在种子 / 早期天使阶段花 expert network(GLG / AlphaSense / Tegus)的钱**:单笔 check 体量小,expert call 单价高,ROI 不成立 —— expert call 是成长期 / 大额 check 的标准动作。(evidence: [T02-S010, T02-S011])
- ❌ **不要把 AI sourcing 工具当投资决策的替代**:它只是 sourcing / 初筛的放大器,judgment 仍在人;且整层 `experimental`,6 个月后具体工具可能换一批,别把核心工作流押在上面。(evidence: [T02-S020])
- ❌ **不要急着为「投资 memo + portfolio tracking」采购专门软件**:早期 / 中型基金用 Notion / Coda 自建足够,专门 portfolio management 软件的 ROI 要等基金规模 + 合规要求到位才成立。(evidence: [T02-S012, T02-S013])
- ❌ **不要因为「Affinity 是老牌」就忽略迁移成本评估,也不要因为「Attio 更现代」就盲目迁移**:VC CRM 王座之争未定(Affinity vs Attio),CRM 迁移有真实的数据 + 习惯成本,按团队的可定制性 / 预算 / API 需求理性选,而非追新。(evidence: [T02-S007, T02-S008])

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 source 都强调的「工具选型原则」(候选 playbook 规则)

- **原则 1 — locale 一票否决**:VC 工具栈先按地理生态分叉,海外工具(PitchBook / Crunchbase / Carta / Affinity)与国内套件(IT 桔子 / 烯牛 / 鲸准)几乎不互通,不存在「一套工具走天下」。(出现于:Carta T02-S001 / PitchBook T02-S004 / Crunchbase T02-S005 / 国内套件 T02-S014)
- **原则 2 — 工具栈跟基金形态走,不跟「行业最佳」走**:solo GP / scout 的最优栈(Crunchbase + AngelList + Notion / Attio)和机构基金的最优栈(PitchBook + Affinity + Carta)是两套;按 fund structure + 预算选,不照搬头部基金。(出现于:AngelList T02-S003 / PitchBook T02-S004 / Affinity T02-S007)
- **原则 3 — 高单价工具(expert network / PitchBook)的 ROI 由 deal stage + check size 决定**:成长期 / 大额 check 才摊得平 expert call 与机构数据订阅;种子 / 天使阶段用便宜替代 + 人脉网络。(出现于:PitchBook T02-S004 / AlphaSense+GLG T02-S010+S011 / Crunchbase T02-S005)
- **原则 4 — 通用工具自建 vs 专门 SaaS 采购,边界随基金规模移动**:Notion / Coda 自建 memo + portfolio 在早期足够,Carta fund admin / 专门 portfolio 软件的价值要等规模 + 合规要求到位。(出现于:Notion/Coda T02-S012+S013 / Carta T02-S001 / AngelList T02-S003)

### 显著的工具流派分裂(候选 智识谱系条目)

- **「采购专门 VC 软件」派 vs 「通用工具自建内部 OS」派**:前者上 Carta(股权)+ Affinity(CRM)+ PitchBook(数据)的专门栈;后者用 Notion / Coda / Attio / Airtable 自建。分界主要是基金规模 + 阶段 + 预算,不是「谁更对」。
- **「数据深度」派 vs 「关系网络」派的工具重心**:有的基金把预算压在数据(PitchBook / CB Insights —— sourcing 靠系统化扫描),有的压在关系(Affinity —— sourcing 靠网络)。对应 intake 的 thesis-driven vs spray-and-pray vs concentrated 学派可能在工具选择上有投射 —— 建议与 Track 01 figures / Phase 2.1 心智模型联动验证。
- **「人 judgment 为核心」派 vs 「AI / 数据信号前置」派**:传统派把 sourcing / 初筛留给 associate 的人脉与判断;AI-native 派(Glasswing 等)把 LLM sourcing + 信号打分前置。这是 2024-2025 才显性化的新分裂,尚未收敛。
- **海外 vs 国内**不是「流派」而是**生态隔离** —— 两套工具、两套数据披露环境、两套基金结构,Phase 2 应作为 locale 分章处理而非「流派对立」。

### 新兴工具信号

- 当前活跃 / 上升的新工具(层):**3 个** —— Attio(VC CRM 现代挑战者)、AI sourcing 层(Glasswing EVE / 各基金自研)、Eqtble(people analytics 进尽调)。
- 出现 → 主流速度估计:**约 24-36 个月**。VC 工具栈本身偏稳态(必备层 Carta / PitchBook / Crunchbase / Affinity 均为多年基础设施),新工具渗透慢;但 **AI sourcing 是例外** —— 2025 AI cycle 拐点正在加速这一层从「AI-native 基金」向主流扩散,可能 12-18 个月就有部分收敛。
- 关键不确定性:头部基金(Sequoia / a16z)的内部 AI / sourcing 工具**闭源不可验证**,新兴层的真实成熟度被低估的可能性存在 —— Phase 2 应在「诚实边界」标注此盲区。

### 冷僻 / 信号薄弱

- 必备层 **4 个**(≥ 3,达标);场景特化层 **6 个**(≥ 5,达标);新兴层 **3 个**(≥ 2,达标)。三层门槛均通过。
- **但有两处信号薄弱,Phase 2.8 应诚实标注**:
  1. **本 track 没有 Wave 1 seed** —— 启动时 research 目录为空,候选完全基于 intake.json 5 大类种子 + 公开评测。Phase 1.5 应回查 Wave 1(Track 04 canon / 05 sources)是否产出,补充交叉验证。
  2. **VC 工具几乎全闭源 SaaS**,无 GitHub stars / commit 等机械成熟度信号;必备层判据用「行业 default 共识」替代,且 source manifest 以 `surrogate_primary`(vendor docs)为主、`secondary`(可追溯媒体)为辅 —— 因黑名单覆盖面广(G2 / Capterra / 知乎 / 公众号全禁),**第三方独立评测的引用密度偏低**。工具卡片的「适合 / 不适合」判断有 vendor 一面之词的风险,Phase 2 心智模型类 claim 需 ≥ 2 source 交叉,新兴层(Attio / AI sourcing / Eqtble)的 production case 多为 stack-pattern 推断而非可验证案例。
- **国内套件 Decay risk = high**:国内创投工具随 RMB 周期 + 政策剧烈波动,供应商整合 / 停服频繁 —— master skill update 流程应对国内工具节设更短的刷新周期。
