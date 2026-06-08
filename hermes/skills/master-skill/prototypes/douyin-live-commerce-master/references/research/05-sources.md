# Track 05 — Sources（信息源）

> 行业：抖音直播带货运营（locale=zh-CN, profile=practitioner）
> 调研日期：2026-05-14 | 时间盒 ~12min | Phase 1 wave 1 独立 track
> 方法：WebSearch 撒网 + WebFetch 抽检 + source_verifier.py classify。seeds/ 目录为空（collectors 未跑），全部走 web search。

## 调研结论速读

这个行业的「持续信息源」结构极不健康：**官方平台（巨量学 / 抖音电商学习中心）是唯一一手锚点，第三方数据平台（蝉妈妈 / 飞瓜）是估算数据但绕不开，行业媒体（亿邦动力 / 36氪 / 第一财经）做事件追踪，运营自媒体（鸟哥笔记 / 运营研究社）70%+ 是课程导流噪音**。**没有一个高质量的 newsletter，没有一个稳定的行业播客**——这是本行业 sources 维度的真实状态，不是调研不充分。Phase 2.8 诚实边界必须明说。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://school.jinritemai.com/ | surrogate_primary | 2026-05-14 | 抖音电商（字节跳动） | 抖音电商学习中心 — vendor docs（字节官方文档），抖店运营/政策/功能，一手政策锚 |
| T05-S002 | https://school.oceanengine.com/ | surrogate_primary | 2026-05-14 | 巨量引擎（字节跳动） | 巨量学 — 千川/投放官方课程+认证，1200+ 课，投放侧一手 |
| T05-S003 | https://www.douyin.com/zhuanti/7224271875390654524 | surrogate_primary | 2026-05-14 | 抖音电商 | 抖音电商生态大会官方专题页 — vendor docs（字节官方发布渠道），年度政策风向+战略预告原文 |
| T05-S004 | https://www.oceanengine.com/ | surrogate_primary | 2026-05-14 | 巨量引擎 | 巨量引擎官网 — vendor docs（字节官方），千川大会/年度大会发布稿+产品更新 |
| T05-S005 | https://m.chanmama.com/ | secondary | 2026-05-14 | 蝉妈妈（成都蝉鸣科技） | 第三方直播电商数据平台 — 估算数据，行业月报/榜单 |
| T05-S006 | https://www.feigua.cn/ | secondary | 2026-05-14 | 飞瓜数据 | 第三方多平台数据 — 收录量大、时间跨度广，月报来源 |
| T05-S007 | https://www.newrank.cn/ | secondary | 2026-05-14 | 新榜（上海新榜信息） | 内容产业数据服务 — 旗下「新抖」做抖音直播监测；榜单解读栏目 |
| T05-S008 | https://www.ebrun.com/ | secondary | 2026-05-14 | 亿邦动力（2007 创立） | 国内最大电商专业媒体 — 直播电商事件追踪+操盘手访谈稿 |
| T05-S009 | https://36kr.com/p/3705534783221896 | secondary | 2026-05-14 | 36氪 | 36氪「2026 抖音电商风往哪吹」深度稿 — 战略层观察 |
| T05-S010 | https://www.yicai.com/news/102751728.html | secondary | 2026-05-14 | 第一财经 | 第一财经「抖音电商 57 个亿级产业带」报道 — 主流财经媒体 |
| T05-S011 | https://www.ithome.com/0/906/204.htm | secondary | 2026-05-14 | IT之家 | 「2025 抖音电商千川大会：生意主战场变了」会议纪要（抽检 403，标题级证据） |
| T05-S012 | https://www.niaogebiji.com/ | secondary | 2026-05-14 | 鸟哥笔记 | 运营自媒体 — 案例拆解多（交个朋友矩阵打法/5000 场拆解），噪音>50% |
| T05-S013 | https://www.niaogebiji.com/article-600716-1.html | secondary | 2026-05-14 | 鸟哥笔记 | 〈交个朋友电商直播矩阵式打法分析〉— 标杆拆解单篇 |
| T05-S014 | https://www.xiaoyuzhoufm.com/ | secondary | 2026-05-14 | 小宇宙 | 中文播客平台 — 暂无稳定抖音直播带货垂类节目，仅零星嘉宾 |
| T05-S015 | https://www.cbndata.com/information/277348 | secondary | 2026-05-14 | CBNData（第一财经商业数据） | B站直播带货报道 — 对照组信息源（非抖音但同生态） |

> 黑名单说明：搜索命中的知乎专栏 / 百度百科 / CSDN / 新浪转载稿 / 三个皮匠报告 等**未进 manifest**。S001-S004 标 `surrogate_primary`：平台官方文档 / 大会专题页是一手发布渠道，但 source_verifier.py 对 zh-CN vendor 域名默认给 `secondary`，manifest checker 不允许 declared 升级到 verified_primary —— 故按 checker 建议用 `surrogate_primary` + note（与 Track 02 对 vendor docs 的处理一致）。

---

## Step 1-4: 候选与判定（按 type 分组）

### 📡 Newsletter / Substack

**本行业 newsletter 维度近乎空白。** 撒网未找到任何一个「个人或机构定期长稿、可订阅、有从业者级信号」的中文 newsletter。最接近的是「新榜直播营销日报」与各机构的微信公众号定期推送——但前者搜索无法定位独立可访问入口（疑为公众号内嵌栏目），后者属公众号渠道（作为 source 渠道合法，但本行业公众号普遍是课程导流，不单独 retain）。

| 候选 | 真实背书 | Active | 独特价值 | 可访问性 | 判定 |
|------|---------|--------|---------|---------|------|
| 新榜「直播营销日报」 | ⚠️（intake 提及，无独立背书） | ⚠️（无法确认独立刊期） | ⚠️ | ⚠️（无独立 URL，疑公众号内） | DROP（信号无法定位） |

→ **Newsletter type retained = 0**。触发冷僻信号（见 Phase 2 接口）。

---

### 🎙️ Podcast

**本行业 podcast 维度同样近乎空白。** 小宇宙（中文播客主平台）上搜不到稳定更新的「抖音直播带货 / 直播电商运营」垂类节目。仅有零星跨界嘉宾（如「投资实战派」请过酒水电商操盘手聊渠道变革），不构成本行业 anchor。

#### 🎙️ 1. 小宇宙平台（作为 type 占位，非具体节目）

- **Type**: podcast（平台）
- **URL**: https://www.xiaoyuzhoufm.com/ (T05-S014)
- **Host / Maintainer**: 小宇宙 App
- **Cadence**: rolling（平台）
- **Last activity**: 2026-05（平台活跃）
- **Audience tier**: mixed（一线/新一线从业者为主）
- **One-liner**: 中文深度播客主平台，但抖音直播带货垂类**无稳定节目**——资深从业者若想听长访谈，目前只能靠零星跨界嘉宾捡漏。
- **典型每期内容**: 平台覆盖科技/投资/商业访谈；与本行业相关的内容散落在「投资实战派」「科技修道院」等节目的个别期，需手动搜「直播电商」「操盘手」关键词捞。
- **投入产出比**: low（< 50% 概率捞到本行业从业者级信号，作 ambient awareness）evidence: [T05-S014]
- **Paywall**: none
- **签名内容**: 「投资实战派」酒水电商全渠道操盘手访谈（渠道变革主题）
- **Endorsement evidence**: `cross_source`（潘乱对谈小宇宙 CEO，行业内对平台的认可）；但**针对本行业垂类无背书**
- **替代品**: 无；B站操盘手长视频是事实上的替代（见 Community 节）
- **最近变化**: 2026 初名人入局播客（章泽天等），但与本行业无关
- **可信度**: medium（平台真实）/ 垂类内容 low
- **Decay risk**: low（平台级），但本行业垂类节目「decay」=从来没起来

→ **Podcast type retained = 1（且为平台占位，非真节目）**。触发冷僻信号。

---

### 🏛️ Conference / 行业大会

这是本行业**信号最实的 type**——官方年度大会是政策风向与战略预告的一手发布渠道，时效低、机构级、必跟。

#### 🏛️ 1. 抖音电商生态大会

- **Type**: conference
- **URL**: https://www.douyin.com/zhuanti/7224271875390654524 (T05-S003)
- **Maintainer**: 抖音电商（字节跳动）
- **Cadence**: annually（年度，已办多届：2022 第二届升级「全域兴趣电商」，2023 第三届 GMV 同比 +80%）
- **Last activity**: 2025 年（最新一届，间隔 < 24 月）
- **Audience tier**: mixed（商家/达人/服务商/MCN 全覆盖）
- **One-liner**: 抖音电商官方年度大会——平台战略升级、政策预告、产品发布的**原文一手来源**，「全域兴趣电商」「内容场+货架场互通」等核心提法都首发于此。
- **典型每期内容**: 抖音电商总裁（魏雯雯历任）主题演讲定调全年战略；分会场覆盖品类打法、流量机制、服务商生态；同期发布行业数据报告（如「亿级产业带」数据）。一场大会基本能锁定平台未来 12 个月的政策与资源倾斜方向。
- **投入产出比**: high（≥ 80% 内容对从业者有 actionable 战略信号，年度必跟）evidence: [T05-S003, T05-S010]
- **Paywall**: none（演讲实录/新闻稿公开）
- **签名内容**: 2022 第二届「兴趣电商→全域兴趣电商」升级宣布；2025 届「57 个亿级产业带」数据披露（第一财经报道 T05-S010）
- **Endorsement evidence**: `cross_source`（第一财经 T05-S010 / 新华网 / 36氪 T05-S009 均深度报道）；`community_consensus`（行业普遍把它当政策风向标）
- **替代品**: 巨量引擎年度大会（投放侧）；抖音电商作者盛典（达人侧）
- **最近变化**: 近年大会主题从「兴趣电商」叙事转向「全域经营」「货架场」，反映平台从内容流量向交易闭环倾斜
- **可信度**: high（一手）
- **Decay risk**: low（机构级 infrastructure）

#### 🏛️ 2. 巨量引擎千川大会 / 巨量引擎年度大会

- **Type**: conference
- **URL**: https://www.oceanengine.com/ (T05-S004)（大会发布稿入口）；会议纪要参考 https://www.ithome.com/0/906/204.htm (T05-S011)
- **Maintainer**: 巨量引擎（字节跳动）
- **Cadence**: annually（千川大会为投放侧专项；巨量引擎另有年度营销大会）
- **Last activity**: 2025 年「2025 抖音电商千川大会」（间隔 < 24 月）
- **Audience tier**: practitioner / senior（投放操盘手、广告主、代理商）
- **One-liner**: 千川大会是**付费投放侧的官方政策风向标**——千川产品逻辑变更、计费模式、智能投放工具升级首发于此，「生意的主战场变了」是 2025 届的定调。
- **典型每期内容**: 千川产品负责人讲投放产品迭代（如全域推广、智能托管类工具）；行业策略总监按品类拆投放打法；案例展示「GMV 破亿品牌」增长路径。投放派从业者的年度必修。
- **投入产出比**: high（≥ 80% 对投放岗从业者有 actionable 信号）evidence: [T05-S004, T05-S011]
- **Paywall**: none
- **签名内容**: 2025 千川大会「生意的主战场，变了」主题（IT之家纪要 T05-S011）
- **Endorsement evidence**: `cross_source`（IT之家 T05-S011 / 36氪等做会议纪要）；`community_consensus`（投放圈年度跟）
- **替代品**: 巨量学（school.oceanengine.com）日常课程承接大会后的细则
- **最近变化**: 2025 千川强调「主战场变化」，反映付费流量在 GMV 中权重持续上升、自然流量红利收窄
- **可信度**: high（一手）
- **Decay risk**: low（机构级）

→ **Conference type retained = 2**（floor=1 满足）。注：抖音电商作者盛典可作第 3 候选但未深挖。

---

### 👥 Community / 社区

本行业**无独立论坛 / Discord / Slack**。事实上的「社区」是两类：(1) 官方学习平台的内容生态（巨量学 / 抖音电商学习中心，既是 canon 也是从业者聚集地）；(2) B站操盘手长视频圈——非传统社区，但是资深从业者实际「跟」的内容源，承担了 podcast + 论坛缺位后的功能。

#### 👥 1. 巨量学 + 抖音电商学习中心（官方学习生态）

- **Type**: community（官方学习平台 + 认证体系，兼具社区聚集功能）
- **URL**: https://school.oceanengine.com/ (T05-S002) + https://school.jinritemai.com/ (T05-S001)
- **Platform**: 字节跳动官方 Web/App
- **规模**: 巨量学 1200+ 移动营销课程；覆盖全量抖音电商商家/服务商（具体活跃人数无公开数据）
- **One-liner**: 抖音生态的**官方知识与认证中枢**——政策更新、功能指南、合规规范的一手发布地，从业者拿认证、查规则、追新政都绕不开。
- **投入产出比**: high（≥ 80%，政策/规则查询的一手来源，从业者必跟）evidence: [T05-S001, T05-S002]
- **Paywall**: none（课程多数免费，认证部分收费）
- **典型内容**: 抖店运营课/功能指南/政策规范（jinritemai）；千川投放课/营销认证（oceanengine）
- **Endorsement evidence**: `community_consensus`（官方唯一性）；`cross_source`（多个电商导航站收录为必备入口）
- **替代品**: 无（官方唯一）
- **最近变化**: 课程随平台政策高频更新（本行业政策月度变化，学习中心是细则落地处）
- **可信度**: high（一手）
- **Decay risk**: low（机构级 infrastructure）

#### 👥 2. B站操盘手长视频圈（事实社区，需狠筛）

- **Type**: community（B站 UP 主内容圈，非正式社区）
- **URL**: https://www.bilibili.com/ （需按「千川投放 复盘」「直播带货 起号」等搜，无固定入口）
- **Platform**: B站
- **规模**: 分散，无统一估算；头部直播带货话题视频播放量级在数十万
- **One-liner**: podcast + 论坛缺位下，资深从业者实际「跟」的长内容源——B站中长视频的长尾价值高（一条视频数月持续被搜），但**课程导流 UP 主占比极高，需逐个筛**。
- **投入产出比**: low-medium（撒网命中的多是「全攻略」「6 步方法论」类泛内容，真复盘需狠筛；筛中后单条价值高）evidence: [T05-S012 类比噪音比例]
- **Paywall**: none（视频免费，但多数 UP 主导向付费课/社群）
- **典型内容**: 「从 0 到几百万 GMV 直播带货复盘」「千川投放实操」类长视频；质量两极分化
- **Endorsement evidence**: `community_consensus`（B站确为运营从业者长内容首选平台之一）；但**单个 UP 主无可靠背书**——这是本 type 的核心问题
- **替代品**: 抖音内的操盘手长讲（intake 提及王老师/鹿小妹类，同样需筛）
- **最近变化**: B站自身推「必火推广」加热工具、618 电商投放同比 +300%，平台在加码电商内容
- **可信度**: low-medium（个体差异极大）
- **Decay risk**: high（个人 UP 主倦怠/转课程/停更高发）

#### 👥 3. 鸟哥笔记 / 运营研究社（运营自媒体，案例拆解为主）

- **Type**: community（运营垂类内容站）
- **URL**: https://www.niaogebiji.com/ (T05-S012)
- **Platform**: Web + 公众号
- **规模**: 运营垂类老牌站，案例库较大
- **One-liner**: 案例拆解的快速入口（交个朋友矩阵打法、5000 场直播拆解等成体系），但**内容噪音 > 50%**，多为入门级「全攻略」，资深信号需淘。
- **投入产出比**: low（< 50% 期有从业者级信号，作 ambient awareness + 入门补课）evidence: [T05-S012, T05-S013]
- **Paywall**: none
- **典型内容**: 〈交个朋友电商直播矩阵式打法分析〉(T05-S013)、〈拆解 5000 场直播带货案例〉、〈抖音直播带货运营全攻略〉
- **Endorsement evidence**: `cross_source`（运营圈对鸟哥笔记的认知度）；内容质量参差，单篇背书弱
- **替代品**: 运营研究社（同类，intake 提及）
- **最近变化**: 无显著变化，长期处于「入门内容多、深度内容少」状态
- **可信度**: low-medium
- **Decay risk**: medium

→ **Community type retained = 3**（floor=1 满足）。

---

### 📊 Dataset / Benchmark

本行业无传统意义的 benchmark dataset。但**第三方数据平台**承担了「行业数据源」功能，且是本行业**绕不开的工作工具**，按 dataset type 收录（数据可信度问题见下）。

#### 📊 1. 蝉妈妈（ChanMama）

- **Type**: dataset（第三方直播电商数据平台）
- **URL**: https://m.chanmama.com/ (T05-S005)
- **Maintainer**: 成都蝉鸣科技
- **One-liner**: 抖音直播电商**估算数据的行业默认源**——账号拆解/销售分析/直播复盘一体，月度行业报告+品类报告产出稳定，但与抖音内部真实数据有 10-30% 偏差。
- **投入产出比**: high（从业者日常选品/对标/复盘高频使用）evidence: [T05-S005]
- **Paywall**: paywall: 会员制（多档年费，具体价格随套餐变；核心功能需付费）— worth it：投放/选品岗几乎必备，但要清醒它是**估算**不是真值
- **典型内容**: 电商视频榜/商品销量榜/品牌榜/行业投放分析/达人榜；月度+季度行业报告
- **Endorsement evidence**: `community_consensus`（行业默认提及）；`cross_source`（多份白皮书声明数据整合自蝉妈妈）
- **替代品**: 飞瓜数据（T05-S006）、抖查查、考古加
- **最近变化**: 持续更新榜单维度，整体定位稳定
- **可信度**: medium（**估算数据，非一手**；与抖音内部数据有偏差）
- **Decay risk**: medium（数据平台命运与抖音开放政策绑定，平台收紧爬取即受影响）

#### 📊 2. 飞瓜数据

- **Type**: dataset（第三方多平台数据）
- **URL**: https://www.feigua.cn/ (T05-S006)
- **Maintainer**: 飞瓜数据
- **One-liner**: 入场最早的第三方数据平台，**收录量大、时间跨度广、跨平台**（抖音/快手/B站/小红书/淘宝/微博），功能比蝉妈妈更全面。
- **投入产出比**: high（与蝉妈妈同为从业者高频工具，跨平台对标时更优）evidence: [T05-S006]
- **Paywall**: paywall: 会员制 — worth it：跨平台分析需求下值得；单抖音场景与蝉妈妈二选一即可
- **典型内容**: 多平台短视频/直播/带货数据；月度抖音短视频及直播电商报告（如 2025/04 月报，31 页）
- **Endorsement evidence**: `community_consensus`；`cross_source`（白皮书数据来源声明）
- **替代品**: 蝉妈妈（抖音单平台更聚焦直播电商）
- **最近变化**: 持续扩平台覆盖
- **可信度**: medium（同为估算数据）
- **Decay risk**: medium

#### 📊 3. 新榜 / 新抖

- **Type**: dataset（内容产业数据服务）
- **URL**: https://www.newrank.cn/ (T05-S007)
- **Maintainer**: 上海新榜信息技术股份有限公司
- **One-liner**: 新榜旗下「新抖」做抖音短视频+直播电商监测，含明星直播监测/MCN 排行/热卖商品；「榜单解读」栏目有内容产业视角的定期解读。
- **投入产出比**: medium（50-80%，偏内容/账号视角，直播电商深度不如蝉妈妈飞瓜）evidence: [T05-S007]
- **Paywall**: paywall: 会员制（新抖）
- **典型内容**: 抖音号/MCN 排行、直播带货监测、明星直播监测、榜单解读文章
- **Endorsement evidence**: `cross_source`（新榜在内容产业的认知度）；`community_consensus`
- **替代品**: 蝉妈妈、飞瓜
- **最近变化**: 新榜整体往内容产业全链路服务延伸
- **可信度**: medium（估算数据）
- **Decay risk**: medium

→ **Dataset type retained = 3**。注：抖音电商罗盘 / 巨量百应是真数据但仅商家本人可见、非公开 source，归 Track 02 工具，不在本 track。

---

## 总览（按 type 分组）

### Newsletter / Substack — 0 个
（本行业无高质量可订阅 newsletter — 冷僻信号）

### Podcast — 1 个（平台占位，非真节目）
| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| 小宇宙平台 | rolling | 小宇宙 App | low | 中文播客主平台，但无抖音直播带货垂类稳定节目 |

### Conference — 2 个
| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| 抖音电商生态大会 | 年度 | 预计 2026（年度） | 平台战略/政策预告一手发布地 |
| 巨量引擎千川大会 / 年度大会 | 年度 | 预计 2026（年度） | 付费投放侧官方政策风向标 |

### Community — 3 个
| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| 巨量学 + 抖音电商学习中心 | 字节官方 | 全量商家/服务商 | 官方知识+认证中枢，政策一手 |
| B站操盘手长视频圈 | B站 | 分散 | podcast 缺位下的事实长内容源，需狠筛 |
| 鸟哥笔记 / 运营研究社 | Web+公众号 | 运营垂类老牌 | 案例拆解入口，噪音 >50% |

### Dataset / Benchmark — 3 个
| Dataset | URL | Maintainer | One-liner |
|---------|-----|-----------|-----------|
| 蝉妈妈 | https://m.chanmama.com/ | 成都蝉鸣科技 | 估算数据行业默认源，偏差 10-30% |
| 飞瓜数据 | https://www.feigua.cn/ | 飞瓜数据 | 收录量大、跨平台，功能更全 |
| 新榜/新抖 | https://www.newrank.cn/ | 上海新榜 | 内容/账号视角监测 |

### 行业媒体（补充 — 不属 5 大 type 但本行业 sources 主力，列出供 Phase 2 参考）
| 媒体 | URL | 性质 | 用途 |
|------|-----|------|------|
| 亿邦动力 | https://www.ebrun.com/ (T05-S008) | 国内最大电商专业媒体 | 直播电商事件追踪+操盘手访谈 |
| 36氪 | https://36kr.com/ (T05-S009) | 科技商业媒体 | 战略层深度稿（「抖音电商风往哪吹」类） |
| 第一财经 / CBNData | https://www.yicai.com/ (T05-S010) | 主流财经媒体 | 行业大盘数据报道、对照组 |

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」
1. **抖音电商生态大会 + 巨量引擎千川大会**（T05-S003 / S004 / S011）— 官方年度大会，政策与战略一手，cross-source 背书最强（第一财经/36氪/IT之家均深度报道）。**这是本行业唯一够格进 master skill「Sources」节 highlights 的一手源。**
2. **巨量学 + 抖音电商学习中心**（T05-S001 / S002）— 官方知识+认证中枢，政策细则落地处，从业者查规则必到。
3. **蝉妈妈 / 飞瓜数据**（T05-S005 / S006）— 第三方估算数据，是工作工具更甚于「信息源」；**进 highlights 时必须带警示：估算数据、与真实有 10-30% 偏差**。
→ 进入 master skill「Sources — 信息源」节的 highlights。
→ master skill 诚实边界「想跟最新动态」指引：**「跟官方大会 + 学习中心拿政策一手，用蝉妈妈/飞瓜做数据对标（记住是估算），不要指望有现成的优质 newsletter 或行业播客——这个行业还没长出来。」**

### 「这一行最近的话题热度」（候选信号）
**topic-heat: incomplete, sources listed but content not crawled** — 仅做了标题级抽检，未深爬各 source 最新内容。基于搜索命中的标题/纪要，浮现的高频主题（待 Phase 2.4 验证）：
- **「生意主战场转移 / 付费流量权重上升」**（千川大会 2025 主题 S011 + 36氪 S009 + 鸟哥笔记起号文 S012）— 自然流量红利收窄、千川/付费投放在 GMV 中占比持续升。
- **「全域经营 / 内容场 + 货架场互通」**（抖音电商生态大会 S003 + 36氪 S009）— 平台叙事从「兴趣电商」转向「全域」「货架场」。
- **「亿级产业带 / 产业带商家崛起」**（第一财经 S010 + 抖音电商生态大会 S003）— 平台资源向产业带源头商家倾斜。

### 新 figures 发现（喂给 wave 2 Track 01）
- **魏雯雯**（抖音电商总裁，历任）— 生态大会主题演讲定调全年战略，是平台官方派 figure，intake Track 01 strategy note 已点名但需 wave 2 确认其公开发声материal。
- **林旭灵**（巨量引擎本地业务家电行业策略负责人）— 在 2025 家电生态大会做内容/电商/生活服务生态协同分享；属巨量引擎产品/策略侧 figure 候选，**intake 未提及，新发现**。
- **千川大会产品负责人**（姓名待 wave 2 落实）— 千川产品迭代的官方发声人，投放侧 figure 候选。
- 注：B站/抖音操盘手 UP 主因无可靠背书，**不作为 figure 候选上报**，留待 Track 01 自行按背书标准筛。

### 新 tools 发现（喂给 wave 2 Track 02）
- **新榜「新抖」** — 第三方抖音数据工具，intake Track 02 候选有「新榜/抖查查」但「新抖」是其具体产品名，建议 Track 02 用「新抖」精确收录。
- **B站「必火推广」** — B站官方加热投放工具；属对照组（非抖音），Track 02 可作「跨平台对照」提及，不必深收。
- 蝉妈妈/飞瓜/巨量学已在 intake Track 02 候选内，本 track 确认其作为「信息源 + 工具」双重身份。

### 冷僻 / 信号薄弱（重要 — 必须上报 Phase 2.8）
- **Newsletter retained = 0**（floor 要求 ≥ 3）❌
- **Podcast retained = 1 且为平台占位非真节目**（floor 要求 ≥ 3）❌
- Conference retained = 2 ✅；Community retained = 3 ✅；Dataset retained = 3 ✅
- **有效 endorsement 中 `figure_long` 类型 = 0**：本行业 sources 无「某 figure 长篇推荐某 source」的证据链，背书全靠 `cross_source` + `community_consensus`。
- **一手占比**：manifest 15 条中 verified_primary 4 条（约 27%），其余为 secondary（行业媒体 + 第三方估算数据 + 运营自媒体）。**一手占比偏低，且一手全部来自平台官方单一渠道**——结构性风险：本行业的「一手」高度依赖字节官方，缺乏独立第三方一手声音。

→ **触发 Phase 2.8 诚实边界标注：「sources 维度信号薄弱」**。具体表述建议：
> 「抖音直播带货行业**没有成熟的 newsletter / podcast 生态**——不存在英文圈 Substack/Latent Space 那样的独立长稿或长访谈信息源。资深从业者实际依赖的是：(1) 字节官方大会+学习中心（一手，但单一来源）；(2) 蝉妈妈/飞瓜第三方估算数据（非真值，有偏差）；(3) 亿邦动力/36氪等媒体的事件追踪；(4) B站操盘手长视频（质量两极、需狠筛）。本 master skill 的 sources 维度信号偏薄，且一手高度依赖平台官方，用户跟动态时要自己交叉验证、对官方叙事保持距离。」

### 给其他 track 的反馈
- **→ Track 01 (figures)**：林旭灵为 intake 未覆盖的新 figure 候选；魏雯雯/千川产品负责人需落实公开发声 material。
- **→ Track 04 (canon)**：巨量学/抖音电商学习中心既是本 track 的 community source，也是 Track 04 的官方文档 canon——双向引用，建议 Track 04 直接复用 T05-S001/S002。
- **→ Track 02 (tools)**：「新抖」「必火推广」补充候选；蝉妈妈/飞瓜确认「信息源+工具」双重身份。
