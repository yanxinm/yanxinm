# Track 06 — Glossary：术语 + 标准 + 合规 + 外行破绽

> 微信私域运营（private-domain-ops）行业。locale=zh-CN。Phase 1 wave 1 第 3 路 subagent 产出。
> 调研时间盒 ~12 min，research_date = 2026-05-14。
> **本行业 type 分布**：Term / Acronym 极多（黑话密集），Standard 偏少且多为平台规则而非正式标准，Regulation 中等（微信平台规则 + 国家个人信息保护法），Certification 几乎 N/A（无正式执业认证，营销课程"认证"不算）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://work.weixin.qq.com/nl/norm | surrogate_primary | 2026-05-14 | 腾讯企业微信 | 企业微信用户账号使用规范 — 平台规则原文(vendor docs), 含外挂/裂变/数据条款编号 |
| T06-S002 | https://weixin.qq.com/agreement/weixin_external_links_content_management_specification | surrogate_primary | 2026-05-14 | 腾讯微信 | 微信外部链接内容管理规范 — 诱导分享/诱导关注红线原文(vendor docs) |
| T06-S003 | https://work.weixin.qq.com/help?doc_id=14117 | surrogate_primary | 2026-05-14 | 腾讯企业微信 | 企业微信违规场景及处罚规则(vendor docs) |
| T06-S004 | https://qn.uqudao.com/3190c25972c0d823b2f583ebfba38837.pdf | secondary | 2026-05-14 | 见实科技 | 《见实私域流量运营词汇手册》1.0, 105 词条 — 私域专门媒体编的行业词典, 拿不准标 secondary |
| T06-S005 | https://www.digitaling.com/articles/382970.html | secondary | 2026-05-14 | 数英 digitaling | 转载见实词汇手册的行业媒体长稿 |
| T06-S006 | https://npcobserver.com/wp-content/uploads/2023/09/2021-Personal-Information-Protection-Law_Gazette.pdf | surrogate_primary | 2026-05-14 | NPC Observer | 《个人信息保护法》英译+公报版 — 立法原文 surrogate, 中文原文在 npc.gov.cn |
| T06-S007 | https://www.wescrm.com/about/news/1025.html | secondary | 2026-05-14 | 群应用 SCRM | SCRM 厂商科普「私域常用术语」— vendor 内容, 拿不准标 secondary |
| T06-S008 | https://www.wescrm.com/siyuzhishiku/qiweiyunying/4659.html | secondary | 2026-05-14 | 群应用 SCRM | SCRM 厂商整理企微客户运营「红线」清单 |
| T06-S009 | https://developer.work.weixin.qq.com/document/path/92522 | surrogate_primary | 2026-05-14 | 腾讯企业微信 | 企业微信第三方应用平台运营规则(vendor docs) |
| T06-S010 | https://www.hanyilaw.com/upload/202210/ea29a271-328e-4a7b-9fb3-4ec4a653a942.pdf | secondary | 2026-05-14 | 瀚一律师事务所 | 《私域流量营销中的个人信息保护合规性初探》— 律所长稿 |

---

## 术语库（按 type + tier）

### Tier 1 — 核心必懂

> 所有从业者必懂。Tier 1 全部填 outsider-tell。

### 1. 私域 / 私域流量 — Private-domain (traffic)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 品牌可**自主拥有、免费反复触达、能精细化运营**的用户池;在微信生态里特指能直接 1v1 / 1vN 触达的用户(企微好友 / 个人号好友 / 微信群成员)。
- **Definition (outsider-friendly)**: 不用每次买广告就能直接联系到的「自家客户」,跟「公域」(抖音/小红书,流量是平台的、要花钱买)相对。
- **Etymology / 来源**: 「私域流量」概念约 2018-2019 年在中文互联网爆发,见实把它做成专门媒体赛道。无海外对应物。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行(以及很多甲方)把「公众号粉丝 / 微博粉丝 / 抖音粉丝 / 自营 APP 用户」都叫私域;内行认为这些**最多算「弱连接」或「伪私域」**——真私域的判据是「能不能直接、免费、反复 1v1 触达」,公众号推送有频次限制+打开率低,不算强私域。**这个定义混乱本身是行业最大的术语坑**。(evidence: [T06-S004, T06-S007])
  - `usage_tell`: 把「私域」等同于「微信群」。内行:私域是**用户池+触达关系**,微信群只是其中一个触点(touchpoint),企微 1v1、朋友圈、小程序都是。
  - `register_tell`: 外行说「我们要做私域」像在说一个新渠道;内行说「私域」时默认指**一整套引流→沉淀→触达→转化→复购→裂变的运营体系**。
- **关联术语**: 公域、触点、私域流量池、公转私
- **是否被错位包装**: SCRM 厂商普遍把「私域」收编成「装我的 SCRM = 做私域」(evidence: [T06-S007]);平台方(抖音/支付宝/小红书)把站内粉丝包装成「平台私域」,业内普遍称之为「伪私域」(evidence: [T06-S004])。
- **可信度**: high
- **Decay risk**: low(核心术语已稳定 5+ 年)

### 2. 公转私 — Public-to-private (traffic conversion)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 把公域(抖音/小红书/视频号/线下门店)的流量引导加到企微/个人号/微信群,沉淀为可反复触达的私域用户。
- **Definition (outsider-friendly)**: 把在别的平台刷到你的人,导流成你微信里的好友。
- **Etymology / 来源**: 私域运营核心动作命名,与「私转公」对仗。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为「公转私」=「让粉丝关注公众号」。内行:关注公众号只是弱沉淀,「公转私」的达标动作是**加到企微好友或进群**(强连接)。
  - `usage_tell`: 外行把它当一次性动作;内行把它当**漏斗**(曝光→点击→扫码→添加→通过→破冰),每层都有转化率,「公转私率/加粉率」是核心 KPI。
- **关联术语**: 私转公、引流、承接、加粉率、钩子
- **可信度**: high
- **Decay risk**: low

### 3. 私转公 — Private-to-public

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 反向操作——把私域用户引导回公域做动作(如引导私域用户去抖音/视频号点赞评论、去大众点评写评、去小红书发种草),给公域内容做数据冷启动。
- **Definition (outsider-friendly)**: 让你微信里的老客户回到公开平台帮你「撑数据」。
- **Etymology / 来源**: 与「公转私」对仗,2021 年后随视频号崛起更常用。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行听到「私转公」以为是「把私域用户变成公司公共资源」(指个人号迁企微)。内行:那叫「个人号转企微 / 资产化」,「私转公」专指**导流回公域平台**。
- **关联术语**: 公转私、视频号、内容回路
- **可信度**: medium
- **Decay risk**: medium(玩法随平台算法变)

### 4. 触点 / 触点建设 — Touchpoint

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 能触达用户的渠道载体——公众号、微信群、小程序、企业微信、朋友圈、视频号;触点建设 = 把这些环节打通提效。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 你能跟客户「碰上面」的每一个入口。
- **Etymology / 来源**: 见实词汇手册第 3 条;源自营销学 touchpoint 概念,私域语境特化。
- **常见误用 (outsider-tell)**:
  - `usage_tell`: 外行把「触点」和「触达」混用。内行:触点是**渠道/载体**(名词,静态),触达是**动作**(动词,把信息送到用户面前)。「多触点」指铺了多个渠道,「高触达」指实际送达率高。
- **关联术语**: 触达、私域流量池、闭环营销
- **可信度**: high
- **Decay risk**: low

### 5. 触达 / 1v1 触达 — Reach / 1-on-1 outreach

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 把信息主动送到用户面前的动作;「1v1 触达」特指企微/个人号一对一私聊(单聊),区别于群发(1vN)和朋友圈(1v 全部)。
- **Definition (outsider-friendly)**: 主动联系到客户;「1v1」就是单独私聊。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「触达」理解成「发出去了」;内行的「触达」隐含**「用户实际看到」**,所以才有「触达率」「打开率」之分——发了但没看到不算有效触达。
  - `usage_tell`: 外行把「1v1 触达」当成「跟每个人都聊」;内行的 1v1 触达**高度依赖 SOP 和标签**,是「按分层、按节奏、半模板化」的私聊,不是真人逐个闲聊。
- **关联术语**: 触点、SOP、群发、标签分层、首席聊天师
- **可信度**: high
- **Decay risk**: low

### 6. SOP — Standard Operating Procedure / 标准作业程序

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 把某个运营动作的标准步骤、时间节点、话术、负责人以统一格式固化下来;私域里最常见的是「1v1 SOP」「社群 SOP」「朋友圈 SOP」「公转私 SOP」。(evidence: [T06-S004, T06-S007])
- **Definition (outsider-friendly)**: 「第几天发什么、谁来发」的标准流程脚本。
- **Etymology / 来源**: 通用管理术语,私域行业把它做成核心交付物;SCRM 工具普遍支持「自动化 SOP」(系统按预设时间把话术推到员工企微,员工点发送即可)。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行说 SOP 指「一份操作手册文档」;内行的私域 SOP 是**带时间轴的、可被 SCRM 自动触发的动作序列**——「第 1 天破冰、第 3 天发福利、第 7 天促单」这种,不是静态文档。
  - `pronunciation_tell`: 念字母「S-O-P」是对的;念成单词「sop」(/sɑp/)会暴露。
  - `usage_tell`: 外行以为「SOP 越细越好」;资深者知道私域 SOP **保鲜期只有 3-6 个月**(平台规则一变、玩法一过气就得重写),过度精细的 SOP 反而是包袱。
- **关联术语**: 1v1 触达、社群运营、朋友圈 SOP、SCRM、自动化
- **可信度**: high
- **Decay risk**: low(术语本身稳定,但具体 SOP 内容 decay 极快)

### 7. 裂变 — Viral / referral growth

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用激励驱动老用户拉新用户、形成指数级传播的玩法总称;载体通常是裂变海报+诱饵+渠道,典型形态是任务宝、拼团、砍价、邀请有礼、分销。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 「老带新」——给奖励让现有用户帮你拉人,像细胞分裂一样扩散。
- **Etymology / 来源**: 「裂变」是中文私域/增长黑客圈造的词(对应 viral / referral),零一裂变等机构把它方法论化。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把任何「分享有奖」都叫裂变;内行:裂变的判据是**自传播闭环**(A 拉来的 B 又能去拉 C),一次性的「转发抽奖」不算裂变,只是活动。
  - `usage_tell`: 外行不知道**裂变是微信合规高危区**——纯利益诱导分享朋友圈、诱导关注、口令码,都踩微信红线,会被封链接/封号。资深者做裂变第一反应是「这个玩法合不合规、保鲜期多久」。(evidence: [T06-S002])
  - `register_tell`: 「裂变」在课程营销话术里被滥用成万能词;内行严肃讨论时会拆成「任务宝裂变 / 群裂变 / 个人号裂变」,不会笼统说「做个裂变」。
- **关联术语**: 任务宝、拼团、砍价、分销、钩子、诱导分享(红线)、邀请有礼
- **可信度**: high
- **Decay risk**: medium-high(具体玩法保鲜期 3-6 个月,平台持续收紧)

### 8. 任务宝 — "Task treasure" (invite-task viral tool/playbook)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 一种裂变玩法/工具:用户完成「邀请 N 个好友关注/进群」的任务后领取奖励,系统自动统计助力进度并发奖。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 「邀请够 X 个人就送你东西」的自动化拉新工具。
- **Etymology / 来源**: 微信生态裂变 SaaS 造的产品化玩法名(小裂变、零一裂变等都有),「宝」是中文工具命名习惯(对比「群裂变」「拼团」)。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为「任务宝」是某一个具体软件品牌;内行:它是**一类玩法的统称**,各家 SaaS 都有自己的任务宝模块。
  - `usage_tell`: 不知道公众号任务宝因「诱导关注」红线已大幅受限,2024 后更多走「企微任务宝/群任务宝」。
- **关联术语**: 裂变、拼团、砍价、邀请有礼、诱导关注(红线)
- **可信度**: high
- **Decay risk**: high(强依赖平台规则,公众号任务宝已大面积失效)

### 9. SCRM — Social Customer Relationship Management

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: 社会化客户关系管理,即基于社交媒体(在中国 = 微信/企微)的 CRM;实操中特指「企微 SCRM 工具」——做标签、自动化 SOP、渠道活码、会话存档、群发、数据看板。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 装在企业微信上的客户管理软件。
- **Etymology / 来源**: Social CRM,2010 年代海外概念;中国市场被企微生态彻底特化,微伴/句子互动/探马等是头部。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 念「S-C-R-M」四个字母;念成「scrum」(敏捷开发那个)是经典外行破绽。
  - `semantic_tell`: 外行把 SCRM 等同于传统 CRM(销售管线管理);内行:SCRM 重心在**社交触达和内容运营**,传统 CRM 重心在销售漏斗和客户档案,两者侧重完全不同。
  - `usage_tell`: 外行以为「上了 SCRM 就等于做了私域」;内行:SCRM 只是工具,私域是运营体系——工具派 vs 运营派的分歧就在这。
- **关联术语**: 企业微信、标签分层、自动化 SOP、会话存档、CDP
- **可信度**: high
- **Decay risk**: low(术语稳定;具体工具能力 12 月内会变)

### 10. RFM / RFM 模型 — Recency, Frequency, Monetary model

- **Type**: acronym + term
- **Tier**: tier-1
- **Definition (insider)**: 用最近一次消费(Recency)、消费频率(Frequency)、消费金额(Monetary)三个维度给用户分层、衡量客户价值的模型,私域里用来决定「对谁推什么、谁该重点维护、谁该召回」。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 按「多久没买、买多勤、花多少钱」把客户分成三六九等。
- **Etymology / 来源**: 经典数据库营销模型(1990 年代,Hughes 等),私域沿用,常配合 SCRM 标签落地。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 念「R-F-M」三个字母。
  - `semantic_tell`: 外行把 RFM 当成「会员等级体系」;内行:RFM 是**动态分层模型**(用户会在格子间移动),会员等级是相对静态的权益体系,两者可配合但不是一回事。
  - `usage_tell`: 外行以为有 RFM 就能精细化运营;资深者知道**中小商家数据量不够、消费链路太短**时 RFM 跑不出有效分层,是「看起来专业但用不起来」的典型。
- **关联术语**: 标签分层、用户分层、LTV、会员体系、生命周期
- **可信度**: high
- **Decay risk**: low

### 11. 标签 / 用户标签 / 打标签 — User tags / tagging

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 给私域用户打的属性/行为/意向标记(如「宝妈」「618 下过单」「咨询未购」),是分层运营、精准触达、SCRM 自动化的最小颗粒度。
- **Definition (outsider-friendly)**: 给每个客户贴的「便利贴」,记下他是谁、想要啥。
- **常见误用 (outsider-tell)**:
  - `usage_tell`: 外行以为标签越多越好,埋头打几百个标签;资深者:**没有触达策略对应的标签是死标签**——标签体系必须反推自「我要做哪些差异化动作」,不是先打标签再想用途。
  - `semantic_tell`: 外行把「标签」和「分组」混用;内行:一个用户可以有 N 个标签(多对多),分组/分层是基于标签的运营动作。
- **关联术语**: 标签分层、用户分层、RFM、SCRM、千人千面
- **可信度**: high
- **Decay risk**: low

### 12. 分层 / 用户分层 / 分层运营 — User stratification / layered operations

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 按是否留存、是否购买、是否复购、活跃度、传播力,把用户分成不同群体,对不同层设计不同运营策略,目标是提升整体活跃和转化。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 把客户分组,对不同组用不同的运营方式,而不是对所有人发一样的东西。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「分层」理解成「按消费金额分 VIP 等级」;内行的分层是**多维度的**(生命周期阶段 × 价值 × 意向 × 活跃度),金额只是一维。
  - `usage_tell`: 外行做完分层就不动了;内行知道分层是**动态的**,用户会跨层流动,运营动作要跟着用户当前所处的生命周期走。
- **关联术语**: 标签、RFM、用户生命周期、千人千面、精细化运营
- **可信度**: high
- **Decay risk**: low

### 13. 朋友圈 / 发圈 / 朋友圈 SOP — Moments / posting to Moments

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 微信朋友圈作为私域触达渠道;「发圈」是日常运营动作,「朋友圈 SOP」规定发圈频率、内容矩阵(种草/案例/福利/人设)、时间段;企微员工发圈受规则和频次限制。
- **Definition (outsider-friendly)**: 把朋友圈当广告位经营——但要讲究频率和内容配比,发太多会被客户屏蔽。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把发朋友圈当「随手发广告」;内行的朋友圈是**有内容矩阵和人设的**——纯广告刷屏会被屏蔽/删好友,「屏蔽率」是隐性 KPI。
  - `usage_tell`: 外行不知道朋友圈打卡裂变(「晒打卡返现」)早已是微信明令违规(2018 年起),还在教学员发打卡;资深者把这类归为过时灰黑玩法。(evidence: [T06-S002])
- **关联术语**: IP / 人设、SOP、屏蔽率、种草
- **可信度**: high
- **Decay risk**: medium

### 14. IP / 人设 / IP 化 — Persona / IP-building

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 通过「微信四件套」(头像、昵称、个性签名、朋友圈)给个人号/企微账号塑造一个有信任感的人格形象;「IP 化」是私域五步法则第一步——建立品牌人格、拉近用户距离。(evidence: [T06-S004, T06-S007])
- **Definition (outsider-friendly)**: 把那个加你微信的账号,经营成一个有血有肉、让人愿意信任的「人」,而不是冷冰冰的客服号。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「IP」理解成「知识产权」或「网红」;私域语境的 IP 特指**账号人格化**——哪怕是个客服岗,也要有人设。
  - `usage_tell`: 外行以为人设 = 起个亲切的昵称;内行:人设要**贯穿四件套+朋友圈内容+聊天话术 register**,不一致就「穿帮」。
- **关联术语**: 微信四件套、朋友圈、首席聊天师、破冰
- **可信度**: high
- **Decay risk**: low

### 15. 破冰 — Ice-breaking (first-contact engagement)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用户刚加上好友/刚进群时,用首次话术、欢迎语、福利钩子建立初步互动和信任,避免「加了就死」;是 1v1 SOP 和社群 SOP 的第一个节点。
- **Definition (outsider-friendly)**: 刚加上客户后的「第一句话」该怎么说,让对方愿意理你。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为破冰 = 发个「你好,欢迎」;内行的破冰是**有钩子、有引导动作的设计**(领福利、做选择题、回复关键词),目的是产生第一次互动行为,不是打招呼。
  - `usage_tell`: 外行只在加好友时想破冰;内行知道**进群也要破冰**(群欢迎语+@新成员+引导改备注),且破冰失败的用户基本就废了。
- **关联术语**: 1v1 SOP、社群运营、欢迎语、钩子、加粉率
- **可信度**: high
- **Decay risk**: low

### 16. 社群 / 微信群 / 群运营 — Community / WeChat group operations

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 把用户聚在微信群里做 1vN 运营;「群运营」覆盖建群、破冰、内容节奏、群活跃、群转化、群裂变;企微社群可配渠道活码、会话存档、关键词回复。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 把客户拉进微信群一起经营,但群很容易变「死群」,要持续运营。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「私域 = 建群」「社群 = 微信群」;内行:社群是**有运营节奏和目标的用户组织**,光建群不运营就是死群——「死群率」是行业默认要面对的现实。
  - `usage_tell`: 外行以为群越多越好、人越多越好;资深者:**500 人死群不如 50 人活跃群**,且大量低质群是运营负担。
  - `register_tell`: 外行管理群像发通知;内行的群有「群人设」「群文化」,内容 register 跟着社群定位走。
- **关联术语**: 群活跃度、破冰、群裂变、渠道活码、KOC、死群
- **可信度**: high
- **Decay risk**: low

### 17. 群活跃度 / 群活跃 — Group activeness

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 衡量微信群是否「活着」的指标体系——发言人数、消息条数、互动率、打开率;低活跃群即「死群」。
- **Definition (outsider-friendly)**: 群里还有多少人说话、有没有互动,反映这个群是不是「死了」。
- **常见误用 (outsider-tell)**:
  - `usage_tell`: 外行用「群消息条数」衡量活跃;内行知道**机器人刷屏、水军接龙也能堆消息数**,真活跃看「真实发言独立人数 / 转化相关互动」,纯热闹不等于有价值。
  - `semantic_tell`: 外行以为活跃度高就是好群;内行:活跃度要和**转化目标**挂钩,一个天天斗图但不下单的群,活跃度高也是失败。
- **关联术语**: 社群运营、死群、KOC、群转化
- **可信度**: high
- **Decay risk**: low

### 18. 公众号(订阅号 / 服务号) — Official Account (Subscription / Service)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 微信公众平台账号;订阅号每天可推 1 次(折叠在订阅号列表),服务号每月推 4 次(出现在对话列表、可调接口)。私域里公众号是「弱连接」内容触点。
- **Definition (outsider-friendly)**: 微信里的内容号;订阅号像每天更新的栏目,服务号更像企业的官方服务窗口。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「公众号粉丝」当成核心私域资产;内行:公众号是**弱连接**(推送频次受限、打开率常低于 5%),不能直接 1v1,只算「半私域」。
  - `usage_tell`: 外行分不清订阅号和服务号该选哪个;内行清楚——要做内容选订阅号,要做服务/交易/接口能力选服务号,且服务号才能跟小程序、模板消息深度打通。
- **关联术语**: 视频号、私域流量池、触点、模板消息
- **可信度**: high
- **Decay risk**: low

### 19. 企业微信 / 企微 — WeCom (WeChat Work)

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 腾讯面向企业的办公+客户运营平台;2024 年起已成私域主战场 default,客户资产归企业(员工离职可继承),支持外部联系人、客户群、SCRM 接口。
- **Definition (outsider-friendly)**: 企业版微信。现在做私域基本都用它,因为客户是公司的,不会跟着员工走。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把企微当「换个皮的个人微信」;内行:企微的核心价值是**客户资产化**(归公司不归个人)+**合规承接**(个人号自动化已大面积被封),功能逻辑和风控完全不同。
  - `usage_tell`: 外行还在教「个人号无脑加好友」;2024 年后业内共识是**企微为主、个人号为辅**,给「个人号矩阵」式建议会被认为停留在 2022 年。
  - `pronunciation_tell`: 「企微」是行业通用简称;说全称「企业微信」不算错但偏外;说「微信工作版 / WeChat Work」会暴露不熟中文圈语境。
- **关联术语**: 个人号、外部联系人、客户群、SCRM、会话存档
- **可信度**: high
- **Decay risk**: low(战略定局;具体规则 12 月内会变,见时效信号)

### 20. 个人号 / 微信个人号 — Personal WeChat account (as ops channel)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用个人微信号做私域承接;好友上限约 5000、单日主动加好友 30-40 个,任何自动化(自动加好友/自动回复/多开/外挂)都是封号高危,2023-2025 屡次大封。(evidence: [T06-S008])
- **Definition (outsider-friendly)**: 用普通个人微信做生意。能更「像真人」,但风险大、客户跟着员工走、批量操作会被封。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行(尤其老玩家)把「个人号」当私域 default;2024 后业内已转向**企微为主**,个人号被压缩为辅助/特定高客单场景。
  - `usage_tell`: 外行以为个人号「加好友、群发、多开」是常规操作;内行知道这些是**封号红线**,且第三方多开/自动化工具本身违反微信协议。
- **关联术语**: 企业微信、外挂、封号、多开、5040 上限
- **可信度**: high
- **Decay risk**: medium

### 21. 公域 — Public domain (traffic)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 流量归平台所有、需要持续花钱/做内容才能获取的流量场——抖音、小红书、视频号(信息流部分)、电商平台、线下;与私域相对。
- **Definition (outsider-friendly)**: 不是你的、得花钱或拼内容去抢的流量,跟「私域」(自己能直接联系的客户)相对。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「有曝光的地方」都笼统叫公域;内行的判据是**流量所有权和触达成本**——平台控分发、要反复付费/做内容才能拿到的,才是公域。
  - `usage_tell`: 外行把公域私域对立成「二选一」;内行讲「公私域协同」「全域」——公域负责拉新曝光,私域负责沉淀复购,是漏斗的上下游。
- **关联术语**: 私域、公转私、全域、触点
- **可信度**: high
- **Decay risk**: low

### 22. 复购 — Repeat purchase

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用户在私域内的二次及以上购买;是私域 ROI 的核心来源(私域的经济性主要靠复购而非首购),「复购率」是头号长期 KPI。私域五步法则:复购 = 需求 + 信任 + 曝光。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 老客户回头再买。私域赚钱主要靠这个,不是靠拉新。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「复购」等同于「老客户」;内行:复购是**行为/比率**,不是身份——加了好友没再买的不算复购贡献。
  - `usage_tell`: 外行用私域拼命拉新冲首购;资深者知道私域的经济模型是**「首购可能亏、复购才赚」**,运营重心应放在复购和 LTV,不是 GMV 表面数。
- **关联术语**: LTV、留存、会员体系、RFM、三单策略
- **可信度**: high
- **Decay risk**: low

### 23. 留存 — Retention

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用户加入私域后没有流失(没删好友/没退群/没拉黑)、持续可被触达的状态;「加了就死」「加了就删」是留存失败的典型。
- **Definition (outsider-friendly)**: 客户加了你之后还「留得住」,没把你删掉。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「加粉数」当成果;内行:**加粉只是入口,留存才是地基**——大量加完即删的「僵尸好友」毫无价值,「7 日留存率」比「加粉总数」更说明问题。
  - `usage_tell`: 外行不区分「在册」和「可触达」;内行知道把你设了「免打扰/不看朋友圈」的好友,数字上在册、实际已流失。
- **关联术语**: 复购、破冰、屏蔽率、流失、加粉率
- **可信度**: high
- **Decay risk**: low

### 24. KOC — Key Opinion Consumer / 关键意见消费者

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: 高参与度、对周边小圈子有真实影响力的普通用户/超级用户;私域里 KOC 既是种草节点也是裂变节点,「1+3 微域运营模型」的目标就是把客户养成 KOC。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 不是大网红,但在自己朋友圈里说话有人信、愿意帮你安利的真实用户。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 念「K-O-C」三个字母。
  - `semantic_tell`: 外行把 KOC 当「小号 KOL」;内行:KOC 的核心不是粉丝量小,而是**「消费者身份的真实性和近距离信任」**——KOL 是「意见领袖」(单向影响),KOC 是「意见消费者」(同侪推荐)。
  - `usage_tell`: 外行把 KOC 当外部投放对象;私域语境的 KOC 更多是**从自己私域用户里培养出来的**,不是花钱买的。
- **关联术语**: KOL、超级用户、裂变、种草、社群
- **可信度**: high
- **Decay risk**: low

### 25. 钩子 / 钩子产品 / 诱饵 — Hook / bait

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用来吸引用户完成某个动作(加好友/进群/分享/下单)的低成本高吸引力激励——福利、赠品、优惠券、爆款引流款、资料包;裂变能否成功取决于「诱饵 + 海报 + 渠道」。(evidence: [T06-S008])
- **Definition (outsider-friendly)**: 用来「勾」住用户的小好处,让他愿意加你、进群或转发。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把钩子理解成「打折」;内行:钩子讲究**「高感知价值、低实际成本、和后续转化强相关」**——送的东西要能筛出目标用户,送泛而无关的礼品引来的是羊毛党。
  - `usage_tell`: 外行用钩子只看「加粉数」;资深者警惕**钩子越猛、留存越差**(被福利吸来的人福利停了就走),钩子要和「精准度」平衡。
- **关联术语**: 公转私、裂变、加粉率、留存、羊毛党
- **可信度**: high
- **Decay risk**: low

### 26. 私域流量池 — Private-domain traffic pool

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 沉淀下来的、可反复低成本触达的用户总量载体——企微好友库 + 微信群 + 个人号好友 + 公众号/视频号粉丝的总和;用来「蓄水」再做转化。(evidence: [T06-S007])
- **Definition (outsider-friendly)**: 你攒下来的、能反复联系的「客户水池」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「池子大小」当成绩;内行:**池子的「质量和可触达性」比「数量」重要**,一池僵尸好友是负资产(占企微外部联系人额度还要花钱)。
  - `usage_tell`: 外行「只进不出」地蓄水;内行讲「蓄水—养鱼—捕鱼」的循环,光蓄不转化等于囤死水。
- **关联术语**: 私域、触点、蓄水、企业微信、外部联系人额度
- **可信度**: high
- **Decay risk**: low

### 27. 操盘手 — Operator / private-domain campaign lead

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 统筹整个私域项目(从引流到复购全链路)的核心负责人;群响、见实等把「私域操盘手」做成了一个职业身份和付费社群标签。
- **Definition (outsider-friendly)**: 私域项目的「总操盘」——不是只发发朋友圈的执行,而是定策略、搭体系、扛 GMV 的人。
- **常见误用 (outsider-tell)**:
  - `register_tell`: 「操盘手」在营销课程里被滥用成「学完就能当」的头衔(「7 天成为私域操盘手」);内行用「操盘手」时指**有完整项目操盘经验、对结果负责**的人,听到「速成操盘手」会直接判定对方是被课程割过的。
  - `semantic_tell`: 外行把「私域运营」和「私域操盘手」当同义;内行有隐含层级——运营是执行层,操盘手是策略层。
- **关联术语**: 私域运营、首席聊天师、群响、见实
- **可信度**: high
- **Decay risk**: low

### 28. 承接 — Funnel reception / landing

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 公域流量被引导过来后,在私域入口侧「接住」的环节——加好友通过率、欢迎语、首次话术、进群引导;「承接没做好」指流量来了但没沉淀住。
- **Definition (outsider-friendly)**: 流量引过来之后,在你这边「接得住接不住」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行只盯「引流」不管「承接」;内行:**引流和承接是两段**,引来 1000 个、加好友通过率 30%、破冰留存 50%,实际只剩 150,承接漏损往往比引流本身更致命。
  - `usage_tell`: 外行把承接当客服被动应答;内行的承接是**有 SOP、有钩子、有节奏的主动设计**。
- **关联术语**: 公转私、破冰、漏斗、加粉率、留存
- **可信度**: high
- **Decay risk**: low

### 29. GMV — Gross Merchandise Volume / 商品交易总额

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: 一段时间内通过私域达成的成交总额;私域常用「私域 GMV」「私域 GMV 占比」作对外汇报口径。
- **Definition (outsider-friendly)**: 总成交金额。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 念「G-M-V」三个字母。
  - `semantic_tell`: 外行把 GMV 当「赚到的钱」;内行:GMV 是**流水不是利润**,且含退款/刷单/未付款,「私域 GMV」尤其容易注水。
  - `usage_tell`: 头部品牌(完美日记/名创/屈臣氏)公开的私域 GMV 业内普遍认为有夸大;资深者听到亮眼私域 GMV 第一反应是「归因口径是什么、含不含自然复购」。
- **关联术语**: ROI、复购、LTV、归因
- **可信度**: high
- **Decay risk**: low

### 30. LTV — Life Time Value / 用户终身价值

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: 一个用户在与品牌的全部互动中贡献的经济收益总和;私域终身价值含两个维度——更多品类复购 + 进私域后跨品牌购买。是判断私域值不值得做的核心指标。(evidence: [T06-S004])
- **Definition (outsider-friendly)**: 一个客户从头到尾总共能给你带来多少钱。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 念「L-T-V」三个字母。
  - `semantic_tell`: 外行把 LTV 当「客单价」;内行:LTV 是**全生命周期累计**,客单价只是单次——私域的核心命题就是「用运营成本撬动 LTV > CAC」。
  - `usage_tell`: 外行只算 GMV 不算 LTV/CAC;资深者用 LTV∶CAC 比值判断私域健康度,这是「数据派」的基本功。
- **关联术语**: CAC、复购、留存、ARPU、RFM
- **可信度**: high
- **Decay risk**: low

### Tier 2 — 周边熟知

> 资深者熟知。Tier 2 至少 50% 填 outsider-tell。

### 31. 拼团 — Group-buy

- **Type**: term | **Tier**: tier-2
- **Insider def**: 多人成团享低价的裂变玩法,傻瓜式裂变工具 1 小时可搭;在微信内拼团曾被规范限制(诱导分享/虚假拼团)。(evidence: [T06-S007, T06-S002])
- **Outsider-friendly**: 拉够人一起买就便宜。
- **outsider-tell**: `usage_tell` 外行不知道「微信外链规范」对违规拼团有明确限制,纯诱导式拼团是灰区。
- **Decay risk**: medium

### 32. 砍价 — Bargain / price-slash

- **Type**: term | **Tier**: tier-2
- **Insider def**: 用户发起、邀请好友帮砍价到指定价的裂变玩法。
- **outsider-tell**: `semantic_tell` 外行当促销;内行当裂变拉新工具,核心是「帮砍 = 加好友/进群」的引流动作,2024 后因羊毛党泛滥+合规收紧已降温。
- **Decay risk**: high

### 33. 分销 / 全民分销 — Distribution / referral commission

- **Type**: term | **Tier**: tier-2
- **Insider def**: 商品成交后利润按规则分配给推广者;企微私域把员工/好友变成分销节点,演变成「新型微商分销关系」。(evidence: [T06-S004])
- **outsider-tell**: `usage_tell` 外行分不清「二级分销」(合规)和「三级及以上」(涉传销红线);资深者做分销先卡「层级数」。
- **Decay risk**: medium

### 34. 邀请有礼 — Invite-with-reward

- **Type**: term | **Tier**: tier-2
- **Insider def**: 「邀请好友得奖励」的通用裂变机制,任务宝是其产品化形态。
- **Decay risk**: medium

### 35. 渠道活码 / 群活码 / 活码 — Channel QR code / group live-QR

- **Type**: term | **Tier**: tier-2
- **Insider def**: 一个二维码后台可关联多个员工/多个群、可统计来源渠道、永不过期(群活码满 200/期后自动切下一个群),是企微承接和归因的基础设施。(evidence: [T06-S007])
- **outsider-tell**: `semantic_tell` 外行以为是普通二维码;内行知道活码的价值在「渠道归因 + 不过期 + 自动分流」。
- **Decay risk**: low

### 36. 会话存档 — Conversation archiving

- **Type**: term | **Tier**: tier-2
- **Insider def**: 企微官方功能,在员工授权前提下留存与外部联系人的聊天记录,用于质检、合规、SOP 优化;是「企微私域+社群模式」的标配。(evidence: [T06-S004])
- **outsider-tell**: `usage_tell` 外行以为是「监控员工」;内行强调它是**官方接口**(区别于第三方违规抓取),且需员工知情授权,本身是合规工具。
- **Decay risk**: low

### 37. 千人千面 — Thousand-faces personalization

- **Type**: term | **Tier**: tier-2
- **Insider def**: 基于标签/数据对接,给不同用户推不同内容/优惠的个性化触达。(evidence: [T06-S004])
- **outsider-tell**: `register_tell` 这是个偏「话术化」的词,SCRM 厂商和案例分享里高频,内行严肃讨论时更常说「标签化精准触达」。
- **Decay risk**: low

### 38. 用户生命周期 / 生命周期管理 — User lifecycle

- **Type**: term | **Tier**: tier-2
- **Insider def**: 用户从引流→新客→活跃→复购→沉睡→流失/召回的阶段轨迹;运营动作要匹配用户当前阶段。
- **outsider-tell**: `usage_tell` 外行对所有用户用同一套 SOP;内行按生命周期阶段切换策略。
- **Decay risk**: low

### 39. 会员体系 — Membership system

- **Type**: term | **Tier**: tier-2
- **Insider def**: 等级 + 权益 + 积分 + 储值的结构化用户体系,与私域分层配合落地长期复购。
- **outsider-tell**: `semantic_tell` 外行把「会员体系」和「RFM 分层」混为一谈;会员体系是相对静态的权益结构,RFM 是动态分层模型。
- **Decay risk**: low

### 40. 超级用户 — Super user

- **Type**: term | **Tier**: tier-2
- **Insider def**: 高复购、高传播、高贡献的头部用户,常等价于私域培养出的 KOC;陈历《超级用户增长》是代表性论述。
- **Decay risk**: low

### 41. ROI — Return on Investment / 投资回报率

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 投资回报率 =(税前年利润 / 投资总额)×100%。(evidence: [T06-S004])
- **outsider-tell**: `usage_tell` 中小商家私域 ROI 真实数据极少公开,行业 ROI 不透明是公认现实;听到「私域 ROI 1∶10」要追问口径。
- **Decay risk**: low

### 42. CAC — Customer Acquisition Cost / 获客成本

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 获取一个用户的成本。(evidence: [T06-S004])
- **outsider-tell**: `semantic_tell` 外行把私域 CAC 当「零成本」(因为「免费触达」);内行:触达免费,但**引流到私域、运营维护都有成本**,私域 CAC 不为零。
- **Decay risk**: low

### 43. ARPU — Average Revenue Per User / 每用户平均收入

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 每个最终用户带来的平均收入,不反映利润率。(evidence: [T06-S004])
- **outsider-tell**: `pronunciation_tell` 多念「A-R-P-U」字母,也有念「阿璞」的。
- **Decay risk**: low

### 44. CDP — Customer Data Platform / 客户数据平台

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 由营销主导的企业顾客信息数据库,把不同部门/系统的消费者信息统一连接。(evidence: [T06-S004])
- **outsider-tell**: `semantic_tell` 外行把 CDP / SCRM / DMP 混为一谈;内行:CDP 管「打通后的统一用户档案」,SCRM 管「社交触达执行」,DMP 管「广告投放的人群包」。
- **Decay risk**: low

### 45. DMP — Data Management Platform / 数据管理平台

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 整合多方数据、标准化细分,把人群包推向互动营销环境(主要服务广告投放)。(evidence: [T06-S004])
- **Decay risk**: low

### 46. UnionID — 微信开放平台统一用户标识

- **Type**: term + acronym | **Tier**: tier-2
- **Insider def**: 同一用户在同一开放平台账号下的多个应用(公众号/小程序/网站)中拥有的统一 ID,使企业能跨触点统一画像和打标签。(evidence: [T06-S004])
- **outsider-tell**: `semantic_tell` 外行把 UnionID 和 OpenID 混淆;内行:OpenID 是单应用内的,UnionID 才是跨应用打通的关键。
- **Decay risk**: low

### 47. CPM — Cost Per Mille / 千人展现成本

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 广告每展现给一千人的成本,只看展现量计费。(evidence: [T06-S004])
- **Decay risk**: low

### 48. LBS — Location Based Services / 基于位置的服务

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 用定位技术获取设备位置并提供服务;私域里「LBS + 社群」用于门店周边 1-3 公里用户拉群运营(瑞幸、久久丫案例)。(evidence: [T06-S004])
- **Decay risk**: low

### 49. 微信四件套 — WeChat "four-piece set"

- **Type**: term | **Tier**: tier-2
- **Insider def**: 头像、昵称、个性签名、朋友圈——打造账号 IP / 人设的四个基础位。(evidence: [T06-S007])
- **outsider-tell**: `semantic_tell` 这是私域圈内造的固定搭配,外行不会用「四件套」指代这组元素。
- **Decay risk**: low

### 50. 群发 — Mass send / broadcast

- **Type**: term | **Tier**: tier-2
- **Insider def**: 企微/个人号一次性给多个客户或多个群推送同一内容;企微有官方群发接口(有频次和合规限制),区别于 1v1。
- **outsider-tell**: `usage_tell` 外行把群发当高效触达;内行知道**高频/机器化群发是骚扰红线**(企微规范明确禁止),且无差别群发打开率极低。(evidence: [T06-S001])
- **Decay risk**: medium

### 51. 私域 IP 矩阵 / 朋友圈矩阵 — Persona matrix / Moments matrix

- **Type**: term | **Tier**: tier-2
- **Insider def**: 多个企微/个人号账号(不同人设、不同定位)组成的运营矩阵,朋友圈内容分工配合。
- **outsider-tell**: `usage_tell` 外行把「矩阵」理解成「多开账号堆数量」;内行:矩阵讲人设分工和合规边界,无脑多开本身是封号高危。
- **Decay risk**: medium

### 52. 漏斗 — Funnel

- **Type**: term | **Tier**: tier-2
- **Insider def**: 从曝光→点击→添加→留存→转化→复购逐层收窄的转化模型,公转私漏斗是私域核心分析框架。
- **outsider-tell**: `usage_tell` 外行只看头尾;内行每层都算转化率,找「漏损最大的那一层」优化。
- **Decay risk**: low

### 53. 蓄水 — "Reservoir filling" (pre-campaign accumulation)

- **Type**: term | **Tier**: tier-2
- **Insider def**: 大促/活动前提前把用户引导沉淀进私域池,为集中转化储备流量。(evidence: [T06-S004])
- **Decay risk**: low

### 54. 种草 — "Planting grass" (seeding desire)

- **Type**: term | **Tier**: tier-2
- **Insider def**: 通过内容(案例/测评/晒单)激发用户购买欲望;私域朋友圈和社群内容矩阵的核心动作之一。
- **outsider-tell**: `register_tell` 「种草」是泛中文电商黑话(小红书重灾区);在私域语境里更偏「朋友圈/社群内容运营」环节,不是外行理解的「网红推荐」。
- **Decay risk**: low

### 55. 私域八门 / 私域大法师 类公众号黑话 — Practitioner-circle in-jokes

- **Type**: term | **Tier**: tier-2
- **Insider def**: 私域操盘手圈层的自嘲式社群/公众号命名风格(「大法师」「日历」「手记」),反映这个圈子「玩梗 + 反课程营销 + 实操派」的 register。
- **Decay risk**: medium

### 56. 首席聊天师 — Chief Chat Officer

- **Type**: term | **Tier**: tier-2
- **Insider def**: 见实提出的私域岗位概念——专门开发话术、构建聊天 SOP、指导聊天员与客户互动的人。(evidence: [T06-S004])
- **outsider-tell**: `register_tell` 半正式造词,见实/案例分享里出现,落地中更常叫「话术运营 / 私聊运营」。
- **Decay risk**: medium

### 57. 三单策略 — "Three-order" strategy

- **Type**: term | **Tier**: tier-2
- **Insider def**: 美妆私域常用打法——第一单(加好友即成交特价品)、第二单(次日 1v1 私聊复购)、第三单(一周内社群/直播再促单)。(evidence: [T06-S004])
- **Decay risk**: medium

### 58. 私域运营 18 节拍 — "18-beat" private-domain ops cadence

- **Type**: term | **Tier**: tier-2
- **Insider def**: 导购私域运营的 18 个标准动作序列(统一人设→吸粉→日常沟通→内容库→种草→社群激活→直播引流→转化→数据监控等)。(evidence: [T06-S004])
- **outsider-tell**: `usage_tell` 这是品牌导购体系的特定方法论,不是通用框架;外行容易当成「私域标准流程」套用。
- **Decay risk**: medium

### 59. 私域流量五步法则 — Five-step private-domain rule

- **Type**: term | **Tier**: tier-2
- **Insider def**: IP 化 → 连接 → 促活 → 分层 → 复购,见实词汇手册收录的经典框架。(evidence: [T06-S004])
- **Decay risk**: low

### 60. AARRR — 海盗模型(Acquisition/Activation/Retention/Revenue/Referral)

- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 拉新→激活→留存→变现→自传播的增长模型,私域常借用其框架描述用户全旅程。
- **outsider-tell**: `pronunciation_tell` 念「海盗模型」或逐字母,念成一个音「啊」是玩梗不是正式;`usage_tell` 增长黑客通用模型,非私域原生,资深私域人会说「这是从增长黑客借的」。
- **Decay risk**: low

### 61. 养号 / 防封 — Account "nurturing" / ban-avoidance

- **Type**: term | **Tier**: tier-2
- **Insider def**: 新企微/个人号上手前通过模拟真人行为(逐步加好友、正常聊天、不批量操作)降低被风控封禁的概率。(evidence: [T06-S008])
- **outsider-tell**: `usage_tell` 「养号」一词本身游走在灰区——它的存在前提是「平台风控」,过度的养号技巧往往是为了规避规则做批量操作,资深白帽派会强调「合规使用比养号技巧重要」。
- **Decay risk**: high(强依赖平台风控策略)

### 62. 外部联系人 — External contact

- **Type**: term | **Tier**: tier-2
- **Insider def**: 企微体系里员工添加的、企业外部的客户;企业外部联系人规模超 2000 需付费「外部联系人规模」,否则限制加新客、只能 48 小时内被动回复。(evidence: [T06-S003])
- **outsider-tell**: `usage_tell` 外行以为企微加客户无限免费;内行清楚 2000 以上要按规模付费,这直接影响私域池成本模型。
- **Decay risk**: medium(收费规则会调整)

### 63. 客户群 — Customer group (WeCom)

- **Type**: term | **Tier**: tier-2
- **Insider def**: 企微官方的「外部群」形态,可由员工创建并归企业管理,支持入群欢迎语、防骚扰、群活码。
- **outsider-tell**: `semantic_tell` 外行把企微「客户群」和个人微信群当一回事;内行知道客户群归企业资产、有官方管理能力,逻辑不同。
- **Decay risk**: low

### 64. 私域 1.0 / 2.0 / 3.0 — Private-domain "versions"

- **Type**: term | **Tier**: tier-2
- **Insider def**: 行业自造的阶段叙事(1.0 个人号加好友群发→2.0 企微+SCRM 工具化→3.0 全域协同+数据驱动+精细化),用来描述范式演进。(evidence: [T06-S007])
- **outsider-tell**: `register_tell` 「X.0」叙事在课程和厂商 PR 里高频,版本划分各家口径不一,**属于 disputed**——内行用它做叙事,不会当严格标准。`disputed: 各机构对 1.0/2.0/3.0 的分界定义不统一`
- **Decay risk**: medium

### 65. 屏蔽率 / 删粉率 — Block rate / unfriend rate

- **Type**: term | **Tier**: tier-2
- **Insider def**: 被用户屏蔽朋友圈或删除好友的比例,是朋友圈 SOP 和触达节奏的负向 KPI。
- **outsider-tell**: `usage_tell` 外行不监控这个,只看加粉;内行把屏蔽率/删粉率当「触达过度」的预警信号。
- **Decay risk**: low

### 66. 羊毛党 — "Wool-pullers" (deal hunters / freebie abusers)

- **Type**: term | **Tier**: tier-2
- **Insider def**: 专薅福利/优惠/裂变奖励、不产生真实复购的低质用户;钩子越猛羊毛党越多。
- **outsider-tell**: `usage_tell` 外行把裂变拉来的人都算战果;内行第一时间要「筛羊毛党」,因为他们拉低留存和 ROI。
- **Decay risk**: low

### 67. 私域中台 / 私域流量中台 — Private-domain middle-platform

- **Type**: term | **Tier**: tier-2
- **Insider def**: 「企业微信 + 社群 + 小程序」搭建的、连接公域和线下门店、统一承接和运营私域的能力底座。(evidence: [T06-S004])
- **outsider-tell**: `register_tell` 「中台」是被互联网行业用滥的词,私域语境多指 SCRM + 小程序 + 数据的组合,不必当严格架构概念。
- **Decay risk**: medium

### 68. 多开 / 外挂 — Multi-instancing / plugins (cheating tools)

- **Type**: term | **Tier**: tier-2
- **Insider def**: 「多开」= 一台设备登录多个微信/企微账号;「外挂」= 企微规范定义为「独立于本软件之外、能影响其正常运行的所有程序,含用 RPA 模拟用户手动操作」——两者都是平台明令禁止的违规行为。(evidence: [T06-S001, T06-S009])
- **outsider-tell**: `semantic_tell` 外行(尤其老个人号玩家)把多开/外挂当「行业常规工具」;内行/白帽派明确这是**黑帽**,封号高危且违反协议。
- **Decay risk**: medium

---

## Standards / 平台规则 / Regulations

> **本行业特点**:几乎没有正式行业「标准」(无 ISO / 国标 / 协会标准),真正的「硬约束」是 **微信平台规则**(平台即裁判)+ **国家个人信息保护法律**。平台规则修订频繁、且常不预告——这是本行业 decay 最快的维度。

### R1. 企业微信用户账号使用规范 — WeCom Account Usage Norm

- **Type**: regulation(平台规则)
- **Issued / Last revised**: 持续滚动修订,无固定版本号;调研时(2026-05)线上版含分级条款编号(3.x)。
- **影响范围**: 所有企微私域操作的合规底线。
- **Insider def**: 企微对账号行为的禁止性规则总集。核心红线条款:
  - **禁外挂/第三方工具**:禁止用插件、外挂或非腾讯授权的第三方工具接入(3.1.2.4);「外挂」定义含「通过 RPA 等技术模拟用户手动操作」(3.1.3)。
  - **禁批量自动化加好友/骚扰**:不得恶意添加外部联系人造成骚扰(3.7.5);禁止滥用管理权限反复推送添加邀请(3.6.4.7)。
  - **禁裂变诱导**:禁止以金钱/实物/虚拟奖品等利益诱导分享(3.5.11.1.1);禁止「不转不是中国人」式胁迫引诱话术(3.5.11.1.2)。
  - **数据隐私**:未经同意不得获取/利用/披露/共享用户数据(3.4);管理员未经外部联系人明确同意或未如实披露用途,不得复制/存储/使用/传输其数据。
  - (evidence: [T06-S001])
- **变化历史**: 2023-2025 持续收紧裂变和数据真实性;条款编号会变,引用时需以官网当时版本为准。
- **Decay risk**: **high**(平台规则,12 月内大概率有调整)
- **Source**: [T06-S001] surrogate_primary(微信官方规则原文 / vendor docs)

### R2. 企业微信违规场景及处罚规则 — WeCom Violation & Penalty Rules

- **Type**: regulation(平台规则)
- **Issued / Last revised**: 滚动修订,无版本号。
- **影响范围**: 违规后的处置预期(从删内容→限功能→封号)。
- **Insider def**: 列举违规场景(滥用互通、恶意加外部联系人、机器生成骚扰/垃圾信息、用外挂多开批量加好友等)及对应处罚(删除违规内容、限制展示、限制账号功能、封禁、拒绝服务)。(evidence: [T06-S003])
- **Decay risk**: high
- **Source**: [T06-S003] surrogate_primary(vendor docs)

### R3. 微信外部链接内容管理规范 — WeChat External Links Content Management Spec

- **Type**: regulation(平台规则)
- **Issued / Last revised**: 2016 年首发;2018-05-30 起禁朋友圈口令码类信息;2019-10 新增违规类型 + 建用户投诉机制;之后持续修订。
- **影响范围**: 所有在微信内传播的裂变海报、拼团链接、分享落地页——裂变玩法的合规天花板。
- **Insider def**: 微信对外链行为的禁止性规则。核心红线:
  - **禁诱导分享**:禁夸张/胁迫/诅咒话术诱导分享(「不转不是中国人」「转发后一生平安」等)。
  - **禁诱导关注**:禁「关注后才能看答案/领红包/参与活动」。
  - **禁利益诱导下载/跳转**:禁以金钱/实物/虚拟奖品(红包/优惠券/积分/话费/流量)诱导下载或跳转外部 APP。
  - **禁违规拼团**、禁朋友圈打卡返现类(2018 起)。
  - 处置:限制链接在微信内打开、封域名/IP、停止传播、朋友圈不可见处理。
  - (evidence: [T06-S002])
- **Decay risk**: medium-high
- **Source**: [T06-S002] surrogate_primary(微信官方规则原文 / vendor docs)

### R4. 企业微信第三方应用平台运营规则 — WeCom 3rd-party App Platform Rules

- **Type**: regulation(平台规则) | **Issued / Last revised**: 滚动修订。
- **影响范围**: SCRM 服务商(微伴/句子互动/探马等)及其能力边界——间接决定私域工具能做什么不能做什么。
- **Insider def**: 规范第三方应用(含 SCRM)接入企微的行为,违规者下架/封禁。SCRM 厂商被官方收编进规则体系,意味着「合规 SCRM」与「违规外挂」是两条道。(evidence: [T06-S009])
- **Decay risk**: high
- **Source**: [T06-S009] surrogate_primary(vendor docs)

### R5. 《中华人民共和国个人信息保护法》(PIPL) — Personal Information Protection Law

- **Type**: regulation(国家法律)
- **Issued**: 2021-08-20 通过 | **生效**: 2021-11-01 | **Last revised**: 截至 2026-05 未修订(稳定)。
- **影响范围**: 私域采集/存储/使用用户个人信息(手机号、画像、标签、行为数据)的法律底线;与《网络安全法》《数据安全法》构成数据合规三支柱。
- **Insider def / 关键条款**:
  - 处理个人信息须取得用户**同意**;采集遵循**最小必要**原则。
  - **第 24 条**:通过自动化决策做信息推送/商业营销,须同时提供「不针对个人特征的选项」或便捷的**拒绝方式**——直接约束私域的「千人千面」精准推送。
  - 落地动作:私域需用会员注册表单获取明示授权、更新隐私条款、留存同意证据。
  - (evidence: [T06-S006, T06-S010])
- **变化历史**: 2021 立法;配套的《个人信息保护合规审计管理办法》等细则后续陆续出台(细则层 decay 中等)。
- **Decay risk**: low(主法稳定);**medium**(配套细则/执法口径)
- **Source**: [T06-S006] surrogate_primary(立法原文 surrogate,中文原文在 npc.gov.cn);[T06-S010] secondary(律所合规长稿)

### 注:不存在的「标准」

- 私域运营**无正式行业标准**(无 ISO / 国标 / 行业协会标准),「私域 1.0/2.0/3.0」「五步法则」「18 节拍」等是机构方法论,不是标准 → 见 Tier 2 词条,标 disputed / 方法论。


---

## Certifications

**本行业认证维度 = N/A(基本空白)**。

- **无正式执业认证**:私域运营没有国家职业资格、没有行业协会颁发的执业证书。
- **平台「认证」≠ 资质**:腾讯有「企业微信服务商认证」「微信广告代理商」等,但那是**渠道商资质**,不是从业者能力认证。
- **课程「认证」是营销话术**:大量培训机构发「私域操盘手认证证书」「私域运营师」,这些**无任何行业公信力**,本质是课程交付物。intake 警示「70%+ 营销课程噪音」在认证维度体现最明显——听到「考个私域操盘手证」基本可判定对方在被收割。
- **Phase 2 处理**:本行业 certification 维度明确标 N/A,不要在 SKILL.md 里假装有认证路径。能力背书靠**实操案例 + 操盘过的 GMV 体量**,不靠证书。

---

## 总览表

### Tier 1 — 核心必懂（30 个，目标 30-50 ✅）

| 术语 | Type | Insider def(精简) | Outsider tell(核心) | Last_updated |
|------|------|-------------------|---------------------|--------------|
| 私域 / 私域流量 | term | 可自主拥有、免费反复触达的用户池 | 把公众号/抖音粉丝都叫私域(应叫伪私域/弱连接) | 2026-05 |
| 公转私 | term | 公域流量引导加企微/进群沉淀 | 以为关注公众号就算公转私(达标是加企微/进群) | 2026-05 |
| 私转公 | term | 把私域用户导回公域做数据冷启动 | 误以为是个人号转企微 | 2026-05 |
| 触点 | term | 能触达用户的渠道载体 | 和「触达」混用(触点是载体,触达是动作) | 2026-05 |
| 触达 / 1v1 触达 | term | 把信息送到用户面前;1v1=单聊 | 以为「发出去」=触达(隐含「看到」) | 2026-05 |
| SOP | term+acronym | 带时间轴、可被 SCRM 自动触发的动作序列 | 念成单词「sop」;以为是静态文档 | 2026-05 |
| 裂变 | term | 激励驱动的自传播闭环增长 | 把任何分享有奖都叫裂变;不知是合规高危区 | 2026-05 |
| 任务宝 | term | 邀请 N 人完成任务领奖的裂变玩法 | 以为是某个具体软件品牌 | 2026-05 |
| SCRM | acronym | 基于微信/企微的社交化客户关系管理 | 念成「scrum」;等同传统 CRM | 2026-05 |
| RFM / RFM 模型 | acronym+term | 按最近/频率/金额给用户动态分层 | 当成静态会员等级体系 | 2026-05 |
| 标签 / 打标签 | term | 用户属性/行为/意向标记 | 埋头打标签不想用途(死标签) | 2026-05 |
| 分层 / 分层运营 | term | 多维分群+差异化策略 | 以为=按金额分 VIP 等级 | 2026-05 |
| 朋友圈 / 发圈 | term | 朋友圈作触达渠道,有内容矩阵 | 当随手发广告(会被屏蔽/删) | 2026-05 |
| IP / 人设 | term | 用四件套塑造账号人格信任感 | 理解成知识产权/网红 | 2026-05 |
| 破冰 | term | 首次互动建立信任的设计动作 | 以为=发句「你好欢迎」 | 2026-05 |
| 社群 / 群运营 | term | 有运营节奏和目标的用户组织 | 以为建群=做私域(死群) | 2026-05 |
| 群活跃度 | term | 真实发言/有效互动指标 | 用消息条数衡量(机器人可刷) | 2026-05 |
| 公众号(订/服务号) | term | 微信内容号,私域弱连接触点 | 把公众号粉丝当核心私域资产 | 2026-05 |
| 企业微信 / 企微 | term+acronym | 私域主战场,客户资产归企业 | 当「换皮个人微信」;还教个人号无脑加好友 | 2026-05 |
| 个人号 | term | 个人微信做私域,自动化=封号高危 | 当 default;以为多开/群发是常规操作 | 2026-05 |
| 公域 | term | 流量归平台、需持续付费的流量场 | 把「有曝光的地方」都叫公域;当二选一 | 2026-05 |
| 复购 | term | 私域内二次及以上购买,ROI 核心 | 用私域拼命拉新冲首购(应做复购/LTV) | 2026-05 |
| 留存 | term | 加入私域后没流失、可持续触达 | 把加粉数当成果(加完即删无价值) | 2026-05 |
| KOC | acronym | 有真实近距离影响力的超级用户 | 念字母错;当「小号 KOL」 | 2026-05 |
| 钩子 / 诱饵 | term | 高感知价值低成本的引导激励 | 理解成「打折」;只看加粉数 | 2026-05 |
| 私域流量池 | term | 可反复低成本触达的用户总量载体 | 把池子大小当成绩(僵尸粉是负资产) | 2026-05 |
| 操盘手 | term | 对私域全链路结果负责的策略层 | 当「7 天速成」头衔 | 2026-05 |
| 承接 | term | 流量引来后入口侧「接住」的环节 | 只盯引流不管承接漏损 | 2026-05 |
| GMV | acronym | 私域成交总额(对外汇报口径) | 念字母错;当「赚到的钱」;易注水 | 2026-05 |
| LTV | acronym | 用户全生命周期累计经济贡献 | 念字母错;当「客单价」 | 2026-05 |

### Tier 2 — 周边熟知（38 个，目标 30-70 ✅）

拼团 / 砍价 / 分销·全民分销 / 邀请有礼 / 渠道活码·群活码·活码 / 会话存档 / 千人千面 / 用户生命周期 / 会员体系 / 超级用户 / ROI / CAC / ARPU / CDP / DMP / UnionID / CPM / LBS / 微信四件套 / 群发 / 私域 IP 矩阵·朋友圈矩阵 / 漏斗 / 蓄水 / 种草 / 私域八门类圈层黑话 / 首席聊天师 / 三单策略 / 私域运营 18 节拍 / 私域流量五步法则 / AARRR / 养号·防封 / 外部联系人 / 客户群 / 私域 1.0·2.0·3.0(disputed) / 屏蔽率·删粉率 / 羊毛党 / 私域中台 / 多开·外挂(黑帽)

> 完整定义见上「Tier 2 — 周边熟知」各条(词条 31-68)。

### Standards / Regulations / Certifications 时间轴（仅近 5 年内有显著变化的进表）

| 名称 | Issued | Last revised | Decay |
|------|--------|--------------|-------|
| 企业微信用户账号使用规范 (R1) | 持续修订无版本号 | 2023-2025 持续收紧裂变/数据,2026-05 在线版含 3.x 条款 | **high** |
| 企业微信违规场景及处罚规则 (R2) | 滚动修订 | 持续 | **high** |
| 微信外部链接内容管理规范 (R3) | 2016 首发 | 2018-05 禁口令码;2019-10 增违规类型+投诉机制;之后持续 | medium-high |
| 企业微信第三方应用平台运营规则 (R4) | 滚动修订 | 持续 | **high** |
| 个人信息保护法 PIPL (R5) | 2021-08-20 通过 / 2021-11-01 生效 | 主法未修订;配套细则陆续出台 | low(主法)/ medium(细则) |

> Certification 时间轴 = N/A(本行业无正式认证)。

### 行业「外行破绽」高亮（最容易暴露的）

| 误用 | 内行实际意思 | 出现频率 |
|------|-------------|---------|
| 把「公众号/抖音/APP 粉丝」都叫私域 | 真私域=能直接免费反复 1v1 触达;其余是弱连接/伪私域 | 极高(甲方+新人通病) |
| SCRM 念成「scrum」 | S-C-R-M,社交化客户关系管理 | 高 |
| 「私域=建群」「社群=微信群」 | 私域是触达体系,社群是有运营目标的用户组织 | 高 |
| 还在教「个人号无脑加好友/多开」 | 2024 后企微为主;个人号自动化=封号红线 | 高(老玩家+过时课程) |
| 把「7 天速成私域操盘手」当真 | 操盘手=有完整操盘经验、对 GMV 负责 | 高(被课程营销污染) |
| 用「加粉数」当成果汇报 | 加粉是入口,留存+复购+LTV 才是地基 | 高 |
| 把外挂/多开当「行业常规工具」 | 企微规范明文定义并禁止,是黑帽 | 中(老个人号圈) |
| 把「触点」和「触达」混用 | 触点=载体(名词),触达=动作(动词) | 中 |
| 以为企微加客户无限免费 | 外部联系人超 2000 需按规模付费 | 中 |
| 把私域 GMV 当利润/当真实数据 | GMV 是流水,头部公开数据普遍被质疑夸大 | 中 |
| 听到「考个私域运营师证」觉得有用 | 本行业无任何有公信力的执业认证 | 中 |
| SOP 念成单词「sop」/ 当成静态文档 | 念字母 S-O-P;SOP 是带时间轴可自动触发的动作序列 | 中 |

---

## 白帽 / 灰帽 / 黑帽 区分

intake 警示「暗黑面广,严格区分白帽 / 黑帽 / 灰帽」。这组术语本身借自黑客圈(白帽=合规、黑帽=违法、灰帽=模糊地带,判据是**意图 + 合法性**),私域圈把它套用到运营手法上。**判据 = 是否违反微信平台规则 + 是否违反个人信息保护法 + 是否欺骗用户**。

| 帽色 | 定义(私域语境) | 典型手法 | 判据 |
|------|----------------|---------|------|
| **白帽** | 完全在微信平台规则 + PIPL 框架内的运营 | 企微官方功能(渠道活码/会话存档/官方群发)、用户授权后打标签、合规裂变(不诱导分享、不利益诱导关注)、真实内容种草、靠服务和信任做复购 | 不违规、不违法、不欺骗 |
| **灰帽** | 平台规则模糊地带 / 打擦边球 / 规则没明说但风险高 | 个人号「养号」技巧、轻度的自动化辅助、朋友圈高频发圈、利益诱导边缘的裂变文案、爬虫式扒取公开信息、过度精准的标签推送(可能踩 PIPL 第 24 条) | 规则未明令禁止但风险高,或踩规则边缘 |
| **黑帽** | 明确违反平台规则 / 违法 / 欺骗用户 | 外挂/多开/RPA 批量自动加好友、刷量、假人僵尸粉、数据造假(假 GMV/假裂变/假分销)、三级以上分销(涉传销)、未授权抓取用户数据、机器生成骚扰群发、口令码诱导 | 违反微信规范明文 / 违反 PIPL / 欺骗 |

**关键发现**:
- 「养号 / 防封」这组高频术语本身就活在灰区——它存在的前提是「我要做平台风控不喜欢的事」(evidence: [T06-S008])。白帽派的立场是「合规使用 > 养号技巧」。
- 「外挂」不是模糊词:**企业微信规范白纸黑字定义并禁止**(含 RPA 模拟操作),用第三方多开/自动化加好友工具是**黑帽**,不是「行业常规」(evidence: [T06-S001, T06-S009])。
- 数据造假(夸大私域 GMV、刷裂变数据)在头部品牌案例里被业内普遍质疑——ROI 不透明 + 成功者发声多,是这行的结构性「黑历史」。
- **SKILL.md 默认走白帽**,灰帽手法要明确标注「这是灰区、保鲜期短、平台一收紧就失效」,黑帽手法只作「反模式」陈列,不教。

---

## Phase 2 接口

### 「行业表达 DNA」直接素材（喂给 Phase 2.5 expression-DNA 提炼）

**高频黑话 top 10**(秒懂=内行,听不懂/用错=外行):
1. **公转私 / 私转公** —— 私域人描述流量流向的基本动词,不会说「引流到微信」这种外行话。
2. **触点 / 触达** —— 严格区分载体(触点)和动作(触达),且「触达」隐含「用户实际看到」。
3. **SOP**(1v1 SOP / 社群 SOP / 朋友圈 SOP) —— 念字母,默认指带时间轴、可被 SCRM 自动触发的动作序列。
4. **裂变**(任务宝 / 拼团 / 砍价 / 分销) —— 判据是「自传播闭环」,且开口就带「合规吗、保鲜期多久」的本能。
5. **企微 / 个人号** —— 用「企微」简称,且默认企微为主战场;还在主推个人号矩阵=暴露停留在 2022。
6. **承接 / 蓄水** —— 把「引流」和「接住/储备」拆成独立环节。
7. **打标签 / 分层 / 千人千面** —— 标签是颗粒度,分层是动作,且强调「死标签」「动态分层」。
8. **复购 / 留存 / LTV** —— 私域人谈成绩谈复购和 LTV,不谈加粉数;「加了就死」是行话。
9. **钩子 / 诱饵 / 羊毛党** —— 谈拉新必谈钩子精准度,且警惕「钩子越猛留存越差」。
10. **操盘手** —— 圈层身份认同词,且对「速成操盘手」有强烈鄙视链。

**行业拒绝的厂商话术 top 5**(拒绝 → 反映行业的价值观 + 反模式):
1. **「装了 SCRM = 做了私域」** —— SCRM 厂商最常见的收编话术。行业反模式:工具不等于运营体系。反映价值观:**运营 > 工具**(运营派对工具派的核心反驳)。
2. **「7 天搭建私域 / 月入 5 万 / 人人能做私域」** —— 课程营销话术。行业(尤其见实、群响实操派)明确拒绝,反映价值观:**私域有前置条件,不适合 70% 商家,且玩法保鲜期只有 3-6 个月**。
3. **「私域是免费流量 / 零成本获客」** —— 把「触达免费」偷换成「获客免费」。行业反驳:引流、运营、企微外部联系人额度都有成本,私域 CAC 不为零。
4. **平台方把站内粉丝包装成「平台私域」(抖音私域 / 支付宝私域)** —— 行业称之为「伪私域」,反映价值观:**真私域的判据是流量所有权 + 能否直接反复 1v1 触达**,不是「有个粉丝列表」。
5. **「私域 1.0/2.0/3.0」「私域中台」「数字化营销中台」等 X.0 / 中台叙事** —— 厂商 PR 和课程高频包装。行业内行用它做叙事但不当严格标准(disputed),反映价值观:**警惕被滥用的宏大概念,看实操**。

**外行破绽 top 10**(insider-only spotting tells —— 见上「行业外行破绽高亮」表,精选):
1. 把公众号/抖音/APP 粉丝都叫「私域」(真私域=能直接免费反复 1v1 触达)。
2. SCRM 念成「scrum」/ 当成传统 CRM。
3. 「私域=建群」,把社群等同微信群。
4. 还在教「个人号无脑加好友 / 多开」(2024 后企微为主,个人号自动化=封号红线)。
5. 把「7 天速成私域操盘手」当真 / 觉得「考个私域运营师证」有用。
6. 汇报只看「加粉数」,不看留存+复购+LTV。
7. 把外挂/多开当「行业常规工具」(企微规范明文禁止,是黑帽)。
8. 「触点」「触达」混用。
9. 以为企微加客户无限免费(超 2000 需付费)。
10. 把私域 GMV 当利润 / 当真实数据(头部公开数据普遍被质疑夸大)。

### 「智识谱系」线索（喂给 Phase 2.7 智识谱系）

- **标准/规则的演变路径暗示范式更替**:
  - 微信平台规则 2018→2023→2025 持续收紧(禁口令码 → 禁朋友圈打卡 → 严打个人号自动化 → 企微裂变/数据收紧)→ 反映行业范式从「钻空子的增长黑客玩法」被迫转向「合规化、工具化、精细化运营」。这是「黑灰玩法红利期 → 白帽运营期」的范式更替。
  - 「个人号为主 → 企微为主」(2024 定局)→ 反映「客户资产归属」从个人转向企业、从游击战转向正规军。
  - PIPL(2021)落地 → 数据采集从「随便扒」转向「需授权」,是合规驱动的范式硬约束。
- **术语 X.0 叙事**:「私域 1.0/2.0/3.0」本身是行业自我编年——1.0 个人号群发、2.0 企微+SCRM 工具化、3.0 全域协同+数据驱动。各家分界不一(disputed),但叙事方向一致:工具化程度和合规化程度逐代提升。
- **多流派术语偏好不同(流派之争的语言层)**:
  - **工具派**话术密集 SCRM / 自动化 SOP / 标签 / 数据看板 / 中台。
  - **销售派**话术密集 1v1 / 话术 / 三单策略 / 转化率 / 逼单。
  - **内容派**话术密集 公众号 / 视频号 / 种草 / 内容矩阵 / IP。
  - **社群派**话术密集 群活跃 / 破冰 / KOC / 群裂变。
  - **品牌派**话术密集 LTV / 用户资产 / 会员体系 / 长期价值 / 六次互动理论。
  - → 同一个人面对「该怎么做私域」给的术语组合,能反推他是哪个流派。这是 Track 06 给 Phase 2.7 的硬证据。

### 「时效性」信号（喂给 Phase 2.8 诚实边界）

- **过去 12 月内有修订/收紧的规则**:企业微信用户账号使用规范、企业微信违规场景及处罚规则、企业微信第三方应用平台运营规则 —— 这三个**都是滚动修订、无版本号、常不预告**,是 master skill 时效衰减的最大来源。
- **预计 12 月内会变的**:
  - 企微对裂变、自动化、数据真实性的规则大概率继续收紧(趋势明确)。
  - 企微外部联系人付费规则、各项额度限制可能调整。
  - PIPL 配套细则(合规审计办法等)陆续落地,执法口径会变。
- **decay 最快的术语**:任务宝、砍价、养号/防封、个人号自动化相关 —— 强依赖平台风控,玩法保鲜期 3-6 个月。
- **诚实边界建议写法**:「Track 06 的『平台规则』维度 decay risk 普遍为 high;微信/企微规则滚动修订且不预告,本 SKILL 引用的条款编号(如企微规范 3.x)需以使用时官网当时版本为准。具体裂变玩法保鲜期仅 3-6 个月。」

### 「工作流变化触发」种子（喂给 wave 3 Track 03）

法规/规则的最新修订是 workflow 变化最重要的触发源。近期修订 + 影响的 workflow 假设:

| 规则修订 | 影响的 workflow 假设 |
|---------|---------------------|
| 微信外链规范持续禁诱导分享/诱导关注/利益诱导 | 「裂变 SOP」不能再依赖朋友圈利益诱导文案;任务宝从公众号转企微/群;裂变玩法设计第一步变成「合规审查」 |
| 企微规范严打外挂/RPA/批量自动化加好友 | 「公转私 SOP」「1v1 触达 SOP」不能依赖第三方自动化加好友/自动回复;承接环节回归「半自动+人工」 |
| 个人号自动化大封 + 企微成 default(2024) | 整个私域工作流的「沉淀」环节默认载体从个人号切到企微;「个人号矩阵」工作流被「企微+SCRM」工作流取代 |
| 企微外部联系人超 2000 需付费 | 私域池规模工作流要纳入「成本-额度」考量;不能无脑「加满好友」 |
| PIPL 第 24 条(自动化营销须提供拒绝方式) | 「千人千面精准推送」工作流要内置「用户可拒绝」选项;标签采集工作流要前置「明示授权表单」 |

### 「冷僻 / 信号薄弱」自检

- 总术语数 = **68**(Tier 1: 30,Tier 2: 38)→ 远超 floor 40,**不冷僻** ✅
- Tier 1 = 30 ≥ 15 ✅;Tier 1 + Tier 2 = 68 ≥ 40 ✅
- Tier 1 全部填了 outsider-tell ✅;Tier 2 约 75% 填了 outsider-tell(≥ 50%)✅
- 有 outsider-tell 的术语 > 50% ✅
- **信号充足**。本行业反而是「噪音过载」型(70%+ 营销课程噪音),Track 06 的难点不是「材料少」,是「筛掉课程话术、抓平台规则原文」。
- **type 分布说明**:Term / Acronym 极丰富(黑话密集行业);Standard = N/A(无正式行业标准,只有平台规则,已归入 Regulation);Regulation 中等(5 条,微信平台规则 4 + 国家法律 1);Certification = **N/A**(无任何有公信力的执业认证,课程证书不算)。这个分布符合「平台特化的实操型行业 + 弱监管 + 强平台规则」的特征。

### 给 Phase 2 的一句话总结

私域的术语体系有三个特征,Phase 2 提炼时务必带上:**(1) 核心词「私域」自身定义混乱,SKILL.md 必须先锁定「私域 = WeChat 生态内可直接 1v1/1vN 触达的用户」;(2) 真正的硬约束不是行业标准而是『平台即裁判』的微信规则 + PIPL,且 decay 极快;(3) 黑话密度高但被营销课程严重污染,内行的表达 DNA 一半体现在『用什么词』,另一半体现在『拒绝什么词』(拒绝速成话术、拒绝『工具=私域』、拒绝『伪私域』)。**

---

## 调研元信息

- research_date: 2026-05-14 | locale: zh-CN | track: 06-glossary | wave: 1
- 来源数: 10(T06-S001 ~ S010);bucket 分布:surrogate_primary 6(微信官方规则原文 / 立法原文,均标 vendor docs / 立法 surrogate)、secondary 4
- 一手 / 二手:核心术语定义一手来源 = 见实《私域流量运营词汇手册》(私域专门媒体编的 105 词行业词典);合规规则一手来源 = 微信/企微官方规则原文 + PIPL 立法原文。二手 = 行业媒体转载 + SCRM 厂商科普 + 律所合规长稿,均作交叉印证。
- 黑名单执行:搜索中出现的知乎专栏、微信公众号、百度百科、CSDN 链接**全部丢弃未入 manifest**。
- 时间盒:~12 min,到点出文件。
- 失败处理:见实词汇手册 PDF 经 WebFetch 无法解析二进制,改用本地 pdfplumber 提取全文 30 页 / 105 词条,成功。
- 待 Phase 2 / 后续 track 补强:① 2026 年最新企微规则条款编号需复核(规则滚动修订);② 视频号相关术语(私转公、视频号直播+私域)随平台演进,Track 03 可补;③ 各 SCRM 工具的术语差异留给 wave 2 Track 02。
