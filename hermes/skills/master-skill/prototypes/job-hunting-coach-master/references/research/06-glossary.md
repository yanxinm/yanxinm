# Track 06 — Glossary（术语 + 标准 + 概念）

> 行业:求职 / 面试辅导（求职教练视角）。locale=`global`(中国大陆 vs 海外英语区两套体系)。profile=`practitioner`。industry_type=`coaching_practitioner`。
> 本 track 输出术语体系 + 标准 / 概念框架 + outsider-tell + **行业拒绝的营销话术**(求职领域营销噪音和「包 offer」黑产很重,这一节是 Phase 2 表达 DNA 反例版的核心素材)。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.eeoc.gov/laws/guidance/employment-tests-and-selection-procedures | verified_primary | 2026-05-14 | EEOC (US gov) | 美国就业甄选程序反歧视指南 — 影响简历匿名化 / 面试合规 |
| T06-S002 | https://www.eeoc.gov/prohibited-employment-policiespractices | verified_primary | 2026-05-14 | EEOC (US gov) | 禁止的招聘做法清单 — 年龄 / 性别 / 婚育等受保护类别 |
| T06-S003 | https://www.dol.gov/general/topic/hiring | verified_primary | 2026-05-14 | US DOL | 美国劳工部招聘合规总览 |
| T06-S004 | https://www.bls.gov/news.release/jolts.nr0.htm | verified_primary | 2026-05-14 | US BLS | JOLTS 职位空缺与劳动力流动报告 — 就业市场周期数据 ground truth |
| T06-S005 | https://www.gov.uk/government/organisations/equality-and-human-rights-commission | verified_primary | 2026-05-14 | UK gov (EHRC) | 英国平等与人权委员会 — 英式反歧视招聘规范 |
| T06-S006 | https://www.mohrss.gov.cn/ | verified_primary | 2026-05-14 | 中国人社部 | 中国人力资源和社会保障部 — 三方协议 / 劳动合同 / 就业政策 ground truth |
| T06-S007 | https://www.gov.cn/zhengce/ | verified_primary | 2026-05-14 | 中国政府网 | 国务院政策库 — 就业 / 反就业歧视 / 应届生政策原文 |
| T06-S008 | https://en.wikipedia.org/wiki/Applicant_tracking_system | secondary | 2026-05-14 | — | ATS 术语入门定义 + 机制 |
| T06-S009 | https://en.wikipedia.org/wiki/Situation,_task,_action,_result | secondary | 2026-05-14 | — | STAR 法术语定义 |
| T06-S010 | https://en.wikipedia.org/wiki/Structured_interview | secondary | 2026-05-14 | — | 结构化面试定义 + 效度引用 |
| T06-S011 | https://en.wikipedia.org/wiki/Case_interview | secondary | 2026-05-14 | — | case interview 术语定义 |
| T06-S012 | https://en.wikipedia.org/wiki/The_Strength_of_Weak_Ties | secondary | 2026-05-14 | — | Granovetter 弱关系理论词条 — hidden job market 理论根 |
| T06-S013 | https://en.wikipedia.org/wiki/Job_hunting | secondary | 2026-05-14 | — | 求职流程总览 + 术语网络 |
| T06-S014 | https://en.wikipedia.org/wiki/Reference_(employment) | secondary | 2026-05-14 | — | reference check / 背调术语定义 |
| T06-S015 | https://www.jobscan.co/blog/8-things-you-need-to-know-about-applicant-tracking-systems/ | surrogate_primary | 2026-05-14 | Jobscan | vendor docs — ATS 关键词匹配机制厂商解释(需 ≥2 source 印证) |
| T06-S016 | https://www.levels.fyi/blog/ | surrogate_primary | 2026-05-14 | levels.fyi | vendor docs — base/bonus/RSU/总包 拆解的薪资数据平台 |
| T06-S017 | https://www.indeed.com/career-advice/finding-a-job/what-is-an-informational-interview | secondary | 2026-05-14 | Indeed | 信息面谈术语入门解释 |
| T06-S018 | https://www.themuse.com/advice/informational-interview-questions-tips | secondary | 2026-05-14 | The Muse | 信息面谈实操解释 |
| T06-S019 | https://hbr.org/2017/04/how-to-write-a-cover-letter | secondary | 2026-05-14 | HBR | cover letter 概念 + 写作规范 |
| T06-S020 | https://www.shrm.org/topics-tools/news/talent-acquisition | secondary | 2026-05-14 | SHRM | 招聘方视角术语(recruiter screen / sourcing) — 行业协会 |
| T06-S021 | https://www.askamanager.org/2021/01/how-to-negotiate-salary.html | secondary | 2026-05-14 | Alison Green | 谈薪话术 / counter-offer / competing offer 实操 |
| T06-S022 | https://www.investopedia.com/terms/c/competing-offer.asp | secondary | 2026-05-14 | Investopedia | competing offer / counter-offer 词典定义 |
| T06-S023 | https://corporatefinanceinstitute.com/resources/career/ | secondary | 2026-05-14 | CFI | base/bonus/equity 术语词典 |
| T06-S024 | https://en.wikipedia.org/wiki/Cold_calling | secondary | 2026-05-14 | — | cold outreach / cold call 术语根 |
| T06-S025 | https://en.wikipedia.org/wiki/Behavioral_interviewing | secondary | 2026-05-14 | — | 行为面试术语定义 |

> **bucket 说明**:gov / 监管原文 → `verified_primary`;招聘平台 / 工具厂商对术语的官方解释 → `surrogate_primary` + note 标「vendor docs」(source_verifier 把 jobscan/blog、levels/blog 自动判为 verified_primary,本 track 按规矩降级为 surrogate_primary);Wikipedia / 词典站 / 创作者博客 → `secondary`。黑名单(知乎 / 公众号 / 百度百科 / CSDN / 内容农场)未进 manifest。
> **国内术语困境**:中国大陆求职术语的权威解释多散落在黑名单平台(知乎 / 公众号 / 牛客),gov 原文只覆盖三方协议 / 劳动合同 / 反歧视政策这类法律概念。国内特色术语(35 岁、第一学历、春秋招、提前批)的定义主要靠 verified_primary 的政策原文 + 海外通用术语类比 + 行业现状描述,标 `定义来源受限`。

---

## 一、Tier 1 术语表 — 核心必懂(所有求职教练必须秒懂)

### 1. ATS — applicant tracking system / 申请人追踪系统

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**:雇主用来收、存、筛、排简历的软件;教练真正关心的是它的「解析层」(parsing)和「关键词 / 标准问题筛选层」,而不是把它当成一个会自动拒人的黑箱。(evidence: [T06-S008, T06-S015])
- **Definition (outsider-friendly)**:公司收简历的系统,会先按关键词和格式过一遍,简历得先「机器可读」才能到 HR 眼前。
- **Etymology / 来源**:applicant tracking system 的首字母缩写,HR 软件行业术语,2000s 起随网申普及成为标配。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行(和不少卖课机构)说「ATS」时指「一个会自动打分、自动拒掉简历的 AI」,内行的 ATS 主要是数据库 + 解析 + 关键词检索,真正的「自动拒」往往是招聘方设的 knockout 问题(是否需要 sponsorship 等),不是 ATS 在「看不懂你简历的才华」。(evidence: [T06-S008, T06-S015])
  - `usage_tell`:把「过 ATS」等同于「塞满关键词」「用纯文本无格式简历」「字体调白藏关键词」——内行知道关键词堆砌 / 白字作弊会被人工环节识破,且现代 ATS 解析能力已大幅提升。
  - `pronunciation_tell`:读「A-T-S」三个字母,不读成单词。
- **关联术语**:[关键词匹配]、[简历解析 resume parsing]、[knockout question]、[海投]
- **是否被错位包装**:简历 / ATS 工具厂商(Jobscan / Rezi 等)倾向把「ATS 匹配度分数」包装成求职成败的核心指标,实际匹配分只是「机器可读 + 关键词覆盖」的代理,不衡量人岗匹配本身 — 厂商 vendor docs 一面之词,需与招聘方视角(SHRM)交叉印证。(evidence: [T06-S015, T06-S020])
- **可信度**: high
- **Decay risk**: medium(ATS 厂商 + AI 解析能力 2024-2025 演化快;术语本身稳定,机制描述会变)

### 2. STAR / SBI — 行为面试回答结构

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**:STAR = Situation / Task / Action / Result,把一段经历讲成「有情境、有动作、有结果」的结构化故事;SBI = Situation / Behavior / Impact,更轻、常用于即时反馈。教练用 STAR 是为了把候选人的「流水账」逼成「证据」,核心在 Action 是「我」做了什么、Result 要量化。(evidence: [T06-S009, T06-S025])
- **Definition (outsider-friendly)**:回答「讲一次你 XX 的经历」时的固定套路:先说背景,再说你要解决什么,然后说你具体做了什么,最后说结果。
- **Etymology / 来源**:STAR 出自行为面试方法论(behavioral interviewing),与结构化面试同源;SBI 由 Center for Creative Leadership 推广为反馈模型。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行把 STAR 当「背诵模板」,逐字背 4 段;内行知道 STAR 是「检查清单」不是「剧本」,死背会僵、会被追问打穿,且 Situation 讲太长、Result 不量化是最常见塌方点。(evidence: [T06-S025])
  - `semantic_tell`:外行的「Action」常说成团队 / 公司做了什么(「我们」),内行坚持 Action 必须是第一人称「我」的具体动作,否则面试官无法评估你本人。
  - `register_tell`:把 STAR 用在所有题型上 — 内行知道它只适合行为题 / 经历题,事实题、假设题、技术题不套 STAR。
- **关联术语**:[行为面试]、[结构化面试]、[量化成就]、[反向提问]
- **是否被错位包装**:卖课机构常把「STAR 模板」包装成「万能答题公式 / 套了就过」,弱化「内容真实性 + 追问承压」才是面试通过的实质。(无独立厂商 source,标为行业内常见营销话术,详见第五节)
- **可信度**: high
- **Decay risk**: low(行为面试结构稳定 20+ 年)

### 3. 行为面试 — behavioral interview

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:基于「过去行为是未来行为最好预测指标」假设的面试形式,问「讲一次你……」而非「你会怎么做」。教练眼里行为面试是可大量准备的——因为题库高度收敛(领导力 / 冲突 / 失败 / 抗压 / 影响力等几大类)。(evidence: [T06-S025, T06-S010])
- **Definition (outsider-friendly)**:面试官让你举真实例子证明你有某种能力,而不是问你「如果遇到 X 你会怎样」。
- **Etymology / 来源**:behavioral interviewing,源自 I/O 心理学(工业与组织心理学)的甄选研究,1970s 起进入企业招聘。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行把行为面试和「闲聊 / 性格测试」混为一谈;内行知道行为题有明确的能力锚点(competency),面试官在按 rubric 打分。
  - `semantic_tell`:外行以为行为面试「答得流畅 = 过」,内行知道关键是「证据强度 + 可信度 + 与岗位能力的匹配」,流畅但空洞照样挂。
- **关联术语**:[STAR]、[结构化面试]、[case interview]、[结构化面试效度]
- **是否被错位包装**:见第五节「背题库就能过」类话术。
- **可信度**: high
- **Decay risk**: low

### 4. 结构化面试 vs 非结构化面试 — structured / unstructured interview

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:结构化 = 所有候选人问同一组预设问题、用同一套评分标准(rubric)打分;非结构化 = 面试官随性聊、凭印象判断。教练必须知道这个区分,因为它直接决定「准备策略」——结构化面试可针对性准备,非结构化面试更吃临场气场和契合感。(evidence: [T06-S010])
- **Definition (outsider-friendly)**:结构化面试是「标准化考试」,每个人题目和评分一样;非结构化是「随便聊聊」,看面试官心情和直觉。
- **Etymology / 来源**:结构化 / 非结构化的区分来自 I/O 心理学的甄选效度研究(selection validity)。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行以为「结构化 = 死板没用」「凭感觉聊更能看出真人」;内行知道大量实证显示结构化面试的预测效度显著高于非结构化(见第三节标准框架),非结构化更容易被偏见和「像我」效应污染。(evidence: [T06-S010])
  - `usage_tell`:外行不知道很多大厂的「行为面 + 评分卡」就是结构化面试的工业化版本,误以为只有笔试才「标准化」。
- **关联术语**:[结构化面试效度]、[行为面试]、[rubric / 评分卡]、[unconscious bias]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 5. case interview — 案例面试

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:咨询(及部分战略 / 投资 / 产品)岗位的标志性面试,给一个商业问题让候选人当场拆解。教练眼里 case 是「可训练的结构化思维表演」——框架、假设树、量化、沟通节奏都能练,但「装作有商业 sense」练不出来。(evidence: [T06-S011])
- **Definition (outsider-friendly)**:面试官给你一道开放的商业难题(「某航空公司利润下滑,怎么办」),看你怎么一步步分析。
- **Etymology / 来源**:case interview,起源于管理咨询公司(McKinsey / BCG / Bain)的招聘传统,后扩散到产品 / 战略岗。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行把 case interview 当「智力题 / 脑筋急转弯」;内行知道考的是结构化拆解 + 沟通 + 商业判断,答案不唯一,过程比「猜对」重要。(evidence: [T06-S011])
  - `semantic_tell`:外行把「背框架」(profitability / 4P / Porter)等同于会做 case;内行知道死套框架反而是减分项,框架是脚手架不是答案。
- **关联术语**:[结构化面试]、[system design 面]、[行为面试]、[mock interview]
- **是否被错位包装**:case 培训机构常把「我们的框架库」包装成「过咨询面的钥匙」,弱化真实商业判断和临场沟通。
- **可信度**: high
- **Decay risk**: low

### 6. system design 面 — 系统设计面试

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:中高级软件 / 基础设施岗的核心面试环节,要求候选人设计一个可扩展的系统(「设计一个短链服务 / 设计 Twitter feed」)。教练知道这是「资历分水岭」面试——junior 靠 coding,senior/staff 靠 system design 和 behavioral。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:让工程师在白板上设计一个大型系统的架构,看他如何权衡容量、速度、可靠性。
- **Etymology / 来源**:system design interview,随互联网大厂规模化招聘形成的标准面试类型,2010s 成型。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行(尤其只刷过 LeetCode 的新人)以为「刷题 = 准备好技术面」;内行知道 system design 和 coding 是两套能力,且越往高级走 system design 权重越高。
  - `semantic_tell`:外行把 system design 当「画出标准答案架构图」;内行知道考的是「澄清需求 → 估算 → 权衡 → 沟通取舍」的过程。
- **关联术语**:[case interview]、[coding 面]、[结构化面试]、[可迁移技能]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 7. informational interview — 信息面谈 / 信息访谈

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:不是求职面试,是求职者主动约行业内人「喝杯咖啡聊 20 分钟」,目的是了解行业 / 公司 / 岗位真相、建立弱关系、为未来的内推或机会埋线。教练眼里这是 networking-first 方法论的核心动作。(evidence: [T06-S017, T06-S018])
- **Definition (outsider-friendly)**:你约一个在目标行业工作的人,纯粹请教和了解情况,不是去要工作。
- **Etymology / 来源**:informational interview,职业咨询领域术语,因《What Color Is Your Parachute?》(Bolles)等求职经典而广为人知。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行一开口就「能不能帮我内推 / 你们招人吗」,把信息面谈做成了变相求职面试;内行知道信息面谈的铁律是「不要在第一次就要工作」,先给价值、先建立关系。(evidence: [T06-S017, T06-S018])
  - `semantic_tell`:外行把「informational interview」当成「面试」(interview)的一种,紧张得像考试;内行知道这里 interview 是「访谈」义,主动权和提问权在求职者手里。
  - `register_tell`:外行用过于正式 / 谄媚的语气;内行知道这是平等的、好奇驱动的对话。
- **关联术语**:[networking]、[hidden job market]、[弱关系]、[cold outreach]、[内推]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 8. hidden job market — 隐藏就业市场

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:指那些没有公开发布招聘广告、通过内部推荐 / 人脉 / 主动接触填补的职位。教练用这个概念论证「为什么只盯招聘网站会漏掉大量机会」,是 networking 派的理论旗帜。(evidence: [T06-S012, T06-S013])
- **Definition (outsider-friendly)**:很多工作机会从来不公开发广告,而是靠认识的人介绍填掉的——这部分就是「隐藏」的就业市场。
- **Etymology / 来源**:hidden job market,职业咨询行业术语;理论根在 Granovetter《The Strength of Weak Ties》(1973)对求职信息如何通过弱关系流动的研究。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行(和部分卖课机构)把 hidden job market 说成一个具体的「秘密渠道 / 内部名单」,只要花钱就能接入;内行知道它不是一个地方,是「机会通过关系网络流动」这个现象的统称,接入方式是长期 networking,不是买门票。(evidence: [T06-S012])
  - `usage_tell`:有人用「hidden job market」反过来否定一切网申,内行知道这是程度问题不是非此即彼(见 intake 警示「网申 vs networking 之争没有唯一答案」)。
- **关联术语**:[弱关系]、[networking]、[informational interview]、[内推]、[cold outreach]
- **是否被错位包装**:「内推保过 / 接入隐藏岗位」是国内黑产话术的常见包装,详见第五节。
- **可信度**: medium(现象真实,但「隐藏市场占比 X%」这类具体数字多为营销夸大,无可靠统一数据)
- **Decay risk**: low

### 9. 弱关系 / 强关系 — weak ties / strong ties

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:强关系 = 家人 / 密友(信息高度重叠);弱关系 = 点头之交 / 前同事 / 二度人脉(信息更新鲜、触达更广)。Granovetter 的核心洞察是「弱关系」在求职信息传递上反而更有效,因为它们连接到你圈子外的信息。教练用这个区分指导 networking 策略:不要只找熟人,要激活弱关系。(evidence: [T06-S012])
- **Definition (outsider-friendly)**:帮你找到工作的,往往不是关系最亲的人,而是那些「认识但不熟」的人——因为他们知道你不知道的信息。
- **Etymology / 来源**:Mark Granovetter, "The Strength of Weak Ties"(1973),社会学经典论文。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把「找关系」理解成「走后门 / 靠强关系硬塞」;内行知道弱关系的力量恰恰在于它是「信息桥」而非「人情债」,激活弱关系是要信息和引荐线索,不是要对方欠人情。(evidence: [T06-S012])
  - `usage_tell`:外行只在急需工作时才联系人(「临时抱佛脚」);内行知道弱关系网络要平时维护,用时才不尴尬。
- **关联术语**:[hidden job market]、[networking]、[informational interview]、[内推]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 10. cold outreach / cold email — 冷启动接触 / 陌生开发

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:主动联系一个完全不认识的人(招聘经理 / 团队成员 / 行业前辈),目的是约信息面谈、表达兴趣或争取机会。教练眼里 cold outreach 是「把弱关系从 0 造出来」的技能,核心在「短、具体、给对方一个低成本的回应理由」。(evidence: [T06-S024])
- **Definition (outsider-friendly)**:给一个不认识的人发邮件 / 私信,礼貌地介绍自己并提出一个小请求。
- **Etymology / 来源**:cold call / cold outreach 借自销售术语(cold calling),指接触没有预先关系的对象。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行的 cold email 又长又通用、上来就要工作;内行知道有效 cold outreach 是高度个性化、极短、请求极小(「能否聊 15 分钟」而非「能否给我 offer」)。
  - `register_tell`:外行要么过度谄媚要么过度随意;内行用「专业但有人味」的 register,且不群发。
- **关联术语**:[informational interview]、[networking]、[pain letter]、[弱关系]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: medium(渠道礼仪随平台演化;LinkedIn / 邮件 / 脉脉 各有不同惯例)

### 11. cover letter / pain letter — 求职信 / 痛点信

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:cover letter = 随简历提交的一封信,解释「为什么是这家公司 + 为什么是我」;pain letter(Liz Ryan 提出)= 不走 HR 流程、直接写给招聘经理,开门见山点出「我猜你团队正被 X 问题困扰」,把自己定位成解药。教练眼里 cover letter 是「叙事派」的主场,pain letter 是反套路化招聘的代表打法。(evidence: [T06-S019])
- **Definition (outsider-friendly)**:求职信是简历之外的一段自我介绍;pain letter 是它的一个变体——绕开模板,直接说「我能解决你的什么麻烦」。
- **Etymology / 来源**:cover letter 是数十年的求职标配;pain letter 由 Liz Ryan(Human Workplace 创始人,前 500 强 HR 高管)提出并推广。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行的 cover letter 是「简历的复述 + 一堆形容词」(「我勤奋好学有责任心」);内行知道有效 cover letter 要么讲一个证明性的具体故事,要么直接对接公司的真实需求,空洞形容词是垃圾信号。(evidence: [T06-S019])
  - `semantic_tell`:外行以为 cover letter「人人要写、套模板就行」;内行知道它在不同地区 / 岗位权重差异大,且模板化 cover letter 不如不写。
- **关联术语**:[human-voiced resume]、[cold outreach]、[量化成就]、[叙事派]
- **是否被错位包装**:无显著厂商错位(pain letter 是 figure 自创概念,非厂商话术)。
- **可信度**: high
- **Decay risk**: medium(AI 普及后 cover letter 的作用和雇主态度正在变化)

### 12. 海投 vs 精准投 — spray-and-pray vs targeted application

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:海投 = 大规模、低定制地投递大量职位(「广撒网」);精准投 = 少量、高度定制、配合 networking 的投递。教练几乎一致认为纯海投的转化率极低,但也知道某些场景(国内校招规模化网申、求职早期试水)海投有其位置——关键是判断场景,不是站队。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:海投是把同一份简历投给几百个岗位碰运气;精准投是针对少数几个岗位认真定制、做足功课。
- **Etymology / 来源**:对应英文 "spray and pray";行业口语术语。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行把「投得多 = 努力 = 该有结果」,投了 300 份没回音就觉得是市场或运气问题;内行知道海投的低回复率是结构性的,问题常在「定位 + 简历 + 投法」而非数量。
  - `semantic_tell`:外行以为精准投就是「投得少」;内行知道精准投的「精准」在前置功课(公司研究 / 关系触达 / 简历定制),不只是数量少。
- **关联术语**:[精准投]、[networking]、[hidden job market]、[求职漏斗]、[ATS]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 13. 内推 — referral

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:由公司现有员工把候选人推荐进招聘流程。教练知道内推的真实价值是「让简历被真人看到 + 一个初步信任背书」,它显著提高「拿到面试」的概率,但**不替代面试本身**——内推进去面试挂掉照样挂。(evidence: [T06-S013, T06-S020])
- **Definition (outsider-friendly)**:公司里认识的人帮你把简历递到招聘流程里,通常比自己网申更容易得到面试机会。
- **Etymology / 来源**:employee referral,HR 招聘术语;国内口语「内推」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行(和黑产话术)把「内推」说成「保过 / 走后门 / 内定」;内行知道正规内推只是「把你送到起跑线」,绝大多数公司的内推仍要走完整面试,且推荐人会被关联评价,没人愿意推一个明显不合格的人。(evidence: [T06-S020])
  - `usage_tell`:外行群发「求内推」给所有人;内行知道有效的内推请求要先建立关系、附上匹配的简历、说清为什么适合,让推荐人愿意为你背书。
- **关联术语**:[referral]、[networking]、[弱关系]、[hidden job market]、[reference check]
- **是否被错位包装**:「内推保过 / 付费内推」是国内求职黑产的核心包装,详见第五节。
- **可信度**: high
- **Decay risk**: low

### 14. recruiter screen / HR 面 / 终面 — 招聘流程的面试轮次

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:典型招聘漏斗的轮次:recruiter screen(招聘官初筛,聊背景 / 动机 / 薪资预期 / 基本匹配)→ 业务面 / 技术面(hiring manager 和团队)→ 终面(更高级别 / 跨团队 / 文化契合)。教练必须知道每轮的「考核重点不同」——recruiter screen 不挂在能力上而常挂在「沟通 / 动机 / 薪资不匹配」。(evidence: [T06-S020])
- **Definition (outsider-friendly)**:求职面试通常分好几轮:第一轮是招聘专员的电话初筛,中间是用人部门的专业面试,最后是更高层的终面。
- **Etymology / 来源**:recruiter screen / phone screen / onsite / final round,招聘行业标准术语。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行把所有轮次当成一回事、用同一套准备应对;内行知道 recruiter screen 考的是「能不能进下一轮 + 薪资动机有没有雷」,技术面考能力,终面考契合,准备策略不同。
  - `semantic_tell`:外行以为「HR 面」不重要(「HR 又不懂业务」);内行知道 recruiter / HR 是流程守门人,初筛挂掉的人根本到不了业务面。
- **关联术语**:[求职漏斗]、[reference check]、[结构化面试]、[谈薪]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 15. reference check / 背调 — 背景调查

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:offer 前后,雇主联系候选人的前主管 / 同事 / 前雇主核实经历真实性、工作表现和离职原因。教练把背调当成「为什么简历和面试不能造假」的硬约束——背调是造假最常暴露的环节之一。(evidence: [T06-S014])
- **Definition (outsider-friendly)**:公司在给你 offer 前后,会联系你以前的同事或上司,核实你简历上写的是不是真的、工作表现如何。
- **Etymology / 来源**:reference check / background check,HR 招聘术语;国内口语「背调」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把背调当「走过场」;内行知道背调能查出头衔灌水、时间线造假、离职原因隐瞒,且第三方背调公司(尤其外企 / 金融)查得很细。(evidence: [T06-S014])
  - `usage_tell`:外行临到背调才慌着找证明人;内行教候选人提前沟通好 reference、确保口径一致、选对人。
- **关联术语**:[简历造假 vs 优化]、[试用期]、[recruiter screen]、[offer]
- **是否被错位包装**:无显著厂商错位。「代过背调」是黑产服务,详见第五节。
- **可信度**: high
- **Decay risk**: low

### 16. 谈薪 anchoring / counter-offer / competing offer — 薪资谈判术语簇

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:anchoring(锚定)= 谈判中先抛出的数字会拉动整个区间,教练教候选人「尽量不要第一个报死数 / 一旦报就报有依据的高位」;counter-offer 有两义——(a) 候选人对公司 offer 的还价,(b) 现雇主为留人开出的挽留 offer;competing offer = 手上另一家公司的 offer,是最强的谈判筹码。(evidence: [T06-S021, T06-S022])
- **Definition (outsider-friendly)**:谈薪有套路:第一个报出的数字会影响最终结果;你可以对公司的 offer 还价;手上有别家的 offer 时谈判力最强。
- **Etymology / 来源**:anchoring 来自谈判 / 行为经济学;counter-offer / competing offer 是招聘与薪酬领域术语。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把 counter-offer 默认理解成「现公司挽留我」,听到「counter-offer」就想到加薪留任;招聘语境里它常指「候选人对 offer 的还价」,两义混用会误事。(evidence: [T06-S022])
  - `usage_tell`:外行要么完全不谈(「人家给多少是多少」)要么瞎谈(报一个无依据的高数还硬刚);内行知道谈薪要基于市场数据 + competing offer + 对总包结构的理解,且 recruiter screen 阶段过早暴露期望值是常见失误。
  - `usage_tell`:外行编造一个不存在的 competing offer 当筹码;内行知道这极度危险——一旦被要求出示或撤回就崩,且诚信受损。
- **关联术语**:[base / bonus / RSU / 总包]、[竞争性 offer]、[recruiter screen]、[offer 决策]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 17. base / bonus / RSU / 总包 — 薪酬结构术语

- **Type**: term + acronym(RSU)
- **Tier**: tier-1
- **Definition (insider)**:base = 基本工资(每月固定现金);bonus = 奖金(年终 / 绩效 / 签字费);RSU = restricted stock unit 限制性股票单位(分期归属 vesting 的股权);总包(total compensation / TC)= 把这些按年折算后的整体数字。教练必须能拆解总包——尤其科技 / 外企岗位,offer 之间不可比就是因为只看 base。(evidence: [T06-S016, T06-S023])
- **Definition (outsider-friendly)**:工资不只是月薪。base 是固定月薪,bonus 是奖金,RSU 是分几年才能拿到的公司股票,把它们加起来按年算才是「总包」。
- **Etymology / 来源**:base salary / bonus / RSU(restricted stock unit)是薪酬(compensation)领域标准术语;「总包」是国内对 total comp / TC 的口语译法。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行比 offer 只比 base 月薪;内行知道两个 base 相同的 offer,总包可能差一倍,RSU 归属节奏(4 年均匀 vs 前低后高 backloaded)和股价波动都要算进去。(evidence: [T06-S016])
  - `pronunciation_tell`:RSU 读「R-S-U」三个字母。
  - `usage_tell`:外行把签字费(signing bonus)当成「每年都有」;内行知道签字费通常一次性,且常带追回条款(clawback)。
- **关联术语**:[谈薪 anchoring]、[竞争性 offer]、[vesting / 归属]、[offer 决策]、[levels.fyi]
- **是否被错位包装**:无显著厂商错位(levels.fyi 等是数据平台,术语用法标准)。
- **可信度**: high
- **Decay risk**: low

### 18. 量化成就 — quantified achievement / quantifying impact

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:把简历和面试里的经历从「做了什么」改写成「做了什么 + 带来了可衡量的结果」(数字、百分比、规模、对比)。这是简历技术派的核心动作,也是行为面试 Result 部分的要求。教练眼里量化是「把模糊主张变成证据」的最快杠杆。(evidence: [T06-S019, T06-S025])
- **Definition (outsider-friendly)**:简历上别只写「负责销售工作」,要写「负责华东区销售,一年内业绩增长 30%」——用数字让成绩可信。
- **Etymology / 来源**:resume 写作与行为面试方法论的通用原则。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行要么完全不量化(全是「负责 / 参与 / 协助」),要么乱编数字凑量化;内行知道量化必须真实可追溯(背调和追问会查),没有硬数字时用相对量 / 范围 / 对比也比空话强。
  - `semantic_tell`:外行以为「量化 = 加数字」;内行知道量化的本质是「证明影响和规模」,数字要和岗位关心的指标对齐才有意义。
- **关联术语**:[STAR]、[简历造假 vs 优化]、[行为面试]、[ATS]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 19. mock interview — 模拟面试

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:在真实面试前进行的演练,由教练 / 同行 / 工具扮演面试官,事后复盘。教练眼里 mock interview 的价值不在「押到题」,而在「暴露问题 + 脱敏 + 建立肌肉记忆」——尤其是承压追问下的表现。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:正式面试前的彩排,有人扮演面试官提问,结束后帮你复盘哪里需要改进。
- **Etymology / 来源**:mock interview,职业咨询与面试准备的通用术语。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把 mock interview 当「提前知道答案」;内行知道它是「在低风险环境里犯错和调整」,如果只是背一遍准备好的答案,就失去了模拟的意义。
  - `usage_tell`:外行只做一次 mock 就觉得「准备好了」;内行知道关键是「mock → 复盘 → 改进 → 再 mock」的迭代,以及找会真追问的人来 mock。
- **关联术语**:[行为面试]、[case interview]、[复盘]、[面试焦虑]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 20. 求职漏斗 — job search funnel / application funnel

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:把求职过程看成一个逐级收窄的漏斗:投递 / 接触 → 回复 / 初筛 → 面试 → 终面 → offer。教练用漏斗做「诊断工具」——卡在哪一层,问题就在哪一层(投递多但没回复 = 定位 / 简历问题;面试多但没 offer = 面试表现问题)。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:求职像一个漏斗,从投出去的简历到最后拿 offer 一层层筛。看你卡在哪一层,就知道该改进什么。
- **Etymology / 来源**:借自销售 / 营销的 funnel 概念,职业教练用于求职过程诊断。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行求职「凭感觉」,失败了归因于运气 / 市场;内行用漏斗逼出可定位的瓶颈——这是教练区别于「打气加油」的核心方法之一。
  - `semantic_tell`:外行把「投得多」当成漏斗顶部健康;内行知道顶部是「有效触达」不是「投递数」,海投把漏斗顶撑大但转化率塌。
- **关联术语**:[海投 vs 精准投]、[recruiter screen]、[ghosting]、[复盘]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 21. ghosting — 已读不回 / 招聘方失联

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:招聘方(或候选人)在流程中途突然停止一切沟通、不给任何反馈或拒信。教练必须帮候选人正确归因 ghosting——它在 2023-2025 就业市场中极普遍,大多是招聘方流程问题 / 岗位冻结 / 优先级变化,**不是对候选人个人价值的判决**。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:你投了简历或面试完之后,公司就消失了——不回复、不拒绝、不给任何说法。
- **Etymology / 来源**:ghosting,借自社交 / 约会语境,2010s 后扩散到招聘场景。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把被 ghosting 解读成「我一定是哪里很差」,陷入自我否定;内行知道 ghosting 高度结构性(岗位被砍 / HR 离职 / 内部候选人胜出 / 流程混乱),个人能控制的是「跟进礼仪 + 不把鸡蛋放一个篮子」,不是「为什么我不够好」。
  - `usage_tell`:外行被 ghosting 后要么死等要么再不联系;内行教「专业地跟进 1-2 次,然后把这条线降权、继续推进其他机会」。
- **关联术语**:[求职漏斗]、[recruiter screen]、[市场周期 vs 个人可控部分]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 22. 可迁移技能 — transferable skills

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:在不同岗位 / 行业之间通用、可以「带着走」的能力(项目管理、数据分析、沟通、谈判、写作等),区别于行业特定的硬技能。这是转行 / 跨行业求职叙事的核心概念——教练帮转行者识别和重新包装可迁移技能,把「我没做过这行」翻译成「我具备这行需要的 X / Y / Z」。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:有些能力换个行业还是有用的(比如带团队、做分析、谈判),这些就是「可迁移技能」,转行时要靠它们搭桥。
- **Etymology / 来源**:transferable skills,职业咨询与生涯发展领域术语。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把可迁移技能当「万能借口」(「我什么都能做」),反而显得没定位;内行知道可迁移技能必须「具体 + 有证据 + 对接目标岗位的真实需求」,泛泛而谈的「学习能力强」是空话。
  - `usage_tell`:外行转行时只强调「我对新行业很有热情」;内行知道热情不是技能,要把过往经历翻译成目标岗位听得懂的能力语言。
- **关联术语**:[转行叙事]、[职业空窗 gap]、[求职定位]、[量化成就]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 23. 职业空窗 / gap — employment gap / career gap

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:简历时间线上的空白期(失业、照顾家庭、生病、深造、间隔年等)。教练的工作是帮候选人「诚实但有策略地」处理 gap——不隐瞒、不撒谎,但也不必过度道歉,把 gap 重新框定(reframe)为有内容的一段时间。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:简历上一段没有工作的空白时间。求职时需要能合理地解释它。
- **Etymology / 来源**:employment gap / career gap,招聘与简历术语。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行要么用假经历填补 gap(造假,背调会暴露),要么对 gap 过度道歉显得心虚;内行知道处理 gap 的原则是「简洁、诚实、向前看」——一句话说清,然后把对话拉回能力和动机。
  - `semantic_tell`:外行以为「有 gap = 减分定局」;内行知道很多 gap(育儿、照护、深造、甚至刻意的求职)在合理表述下完全可被接受,真正减分的是「遮遮掩掩」本身。
- **关联术语**:[可迁移技能]、[转行叙事]、[简历造假 vs 优化]、[特殊群体求职]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

### 24. 校招 / 社招 — campus recruiting / experienced (lateral) hiring

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:校招 = 面向应届毕业生的招聘,有专门的流程 / 时间窗 / 评估标准(更看潜力和学校);社招 = 面向有工作经验者的招聘,看过往业绩和岗位匹配。这是国内求职生态最基础的二分,两套流程、两套打法。海外对应概念是 new grad hiring vs experienced hiring,但海外校招不像国内那样高度工业化、有统一时间窗。(evidence: [T06-S007])
- **Definition (outsider-friendly)**:校招是公司专门招应届毕业生的通道,社招是招有工作经验的人——两者流程和要求完全不同。
- **Etymology / 来源**:中国大陆招聘生态术语;海外对应 campus recruiting / new grad vs lateral / experienced hire。
- **常见误用 (outsider-tell)**:
  - `usage_tell`:外行(尤其留学生 / 海归)把海外的 rolling 招聘思维套到国内校招,错过国内春秋招的统一时间窗;或反过来用国内校招的「投递季」思维理解海外 rolling,一直等「最佳时机」。
  - `semantic_tell`:外行把「应届生身份」当成一个模糊概念;内行知道在国内它是有政策定义、有时效、影响校招资格和部分政策待遇的「身份」(见第三节)。
- **关联术语**:[春招 / 秋招 / 提前批]、[应届生身份]、[rolling recruiting]、[三方协议]、[转正]
- **是否被错位包装**:国内校招培训机构把「校招辅导」高度产品化,详见第五节。
- **可信度**: high
- **Decay risk**: medium(国内校招政策 / 时间窗 / 应届生认定口径会调整)

### 25. 求职定位 — career positioning / job search targeting

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**:在开始投简历之前,收敛清楚「我要找什么岗位 / 什么行业 / 什么层级 / 我的卖点是什么」。教练几乎一致认为这是求职的第一性问题——定位错了,简历、面试、networking 全部白做。它不是「我什么都能做」,而是「我针对 X 提供 Y 价值」。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:开始找工作前先想清楚:你到底要找什么样的岗位、你凭什么是合适人选。定位不清,后面所有努力都打折扣。
- **Etymology / 来源**:career positioning,借自营销的 positioning 概念,职业教练领域核心术语。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`:外行把「定位宽 = 机会多」,简历写得什么岗位都能投;内行知道模糊定位的简历对每个岗位都「不够对口」,定位窄而清反而命中率高。
  - `usage_tell`:外行跳过定位直接投递,投了几百份没结果才回头;内行坚持「定位 → 简历 → 投递」的顺序,定位是地基。
- **关联术语**:[职业叙事]、[personal branding]、[可迁移技能]、[精准投]、[求职漏斗]
- **是否被错位包装**:无显著厂商错位。
- **可信度**: high
- **Decay risk**: low

---

## 二、Tier 2 术语表 — 周边熟知(资深教练熟知)

### 26. 关键词匹配 / 简历解析 — keyword matching / resume parsing

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:ATS 把简历文档拆解成结构化字段(姓名 / 经历 / 技能)的过程叫 parsing;再把简历内容与 JD 关键词比对叫 keyword matching。教练用它指导「简历要用 JD 同款词、避免花哨排版干扰解析」。(evidence: [T06-S008, T06-S015])
- **Definition (outsider-friendly)**:招聘系统把你的简历「读」成数据,并和职位描述里的关键词对照。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行为了「过解析」用纯文本无格式简历或塞满关键词;内行知道适度结构化的简历现代 ATS 能正常解析,关键是用对词不是堆词。
- **关联术语**:[ATS]、[knockout question]、[量化成就]
- **可信度**: high / **Decay risk**: medium

### 27. knockout question — 淘汰式问题 / 硬性筛选题

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:网申表单里的硬性筛选问题(是否需要工作签证 sponsorship / 是否有 X 年经验 / 是否接受出差),答「不符合」会被直接刷掉。教练提醒候选人:很多「ATS 自动拒」其实是 knockout 题触发的,不是简历不好。(evidence: [T06-S020])
- **Definition (outsider-friendly)**:申请表里的「一票否决」问题,答错了系统直接把你筛掉。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把所有自动拒信归因于「简历差」;内行会先排查是不是 knockout 题导致的。
- **关联术语**:[ATS]、[关键词匹配]、[sponsorship / 工作签证]
- **可信度**: medium / **Decay risk**: low

### 28. rolling recruiting — 滚动招聘

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:岗位常年开放、招满即止、没有统一截止日的招聘模式,海外(尤其美国)的常态。与国内校招的「统一时间窗」相对。教练据此给海外求职者「越早投越好、不要等」的策略。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:职位一直开放、招到合适的人就关,没有固定的「报名季」。
- **常见误用 (outsider-tell)**:`usage_tell` — 国内求职者误以为海外也有「秋招季」,一直等;内行知道 rolling 模式下拖延就是丢机会。
- **关联术语**:[校招 / 社招]、[春招 / 秋招 / 提前批]、[new grad]
- **可信度**: high / **Decay risk**: low

### 29. 春招 / 秋招 / 提前批 — 国内校招时间窗

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:国内校招高度工业化,有明确节奏:秋招(约 8-11 月,主战场,岗位最多)、春招(约 次年 2-5 月,补录 + 留学生)、提前批(秋招前的更早批次,部分企业 / 行业用来锁定优秀生源)。教练必须按这个日历倒推应届生的准备节奏。(evidence: [T06-S007])
- **Definition (outsider-friendly)**:国内应届生招聘集中在每年的固定时段:秋招是大头,春招是补充,提前批更早。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行(尤其留学生)按海外节奏准备,错过秋招主战场;`semantic_tell` — 把「提前批」当成「不重要的预演」,内行知道某些行业提前批就锁定了大量名额。
- **关联术语**:[校招 / 社招]、[rolling recruiting]、[应届生身份]、[三方协议]
- **可信度**: high / **Decay risk**: medium(具体时间窗逐年微调)

### 30. 第一学历 — "first degree" / initial academic credential(国内特色)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:国内职场对「本科就读院校层次」的非正式称呼,常被部分企业 / HR 用作隐性筛选门槛(即使你后来读了名校硕士)。教练必须把它当成「真实存在但程度因行业 / 岗位 / 公司而异」的结构性约束,既不否认也不替机构放大焦虑。(evidence: [T06-S007])
- **Definition (outsider-friendly)**:指你本科读的是什么学校。国内有些公司即便看研究生学历,也会看本科出身。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行(或卖课机构)把「第一学历」说成铁律「定终身」;内行知道它是程度问题——某些大厂 / 体制内岗位看得重,大量岗位并不卡,且能用经历 / 作品 / 内推对冲。
- **关联术语**:[35 岁]、[就业反歧视]、[特殊群体求职]
- **可信度**: medium(社会现象,非法律概念) / **Decay risk**: medium

### 31. 35 岁(职场年龄门槛) — the "age-35 ceiling"(国内特色)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:国内职场对「35 岁后求职 / 转岗难度上升」的普遍说法,部分源于公务员考试年龄线、部分源于企业用人偏好。教练的立场:这是真实存在的结构性约束,但被部分培训机构刻意放大变现;程度因行业 / 岗位 / 层级差异极大,要给真实图景而非贩卖焦虑(intake 警示明确要求)。(evidence: [T06-S007])
- **Definition (outsider-friendly)**:国内有种说法,35 岁之后找工作会明显变难——这有一定现实基础,但被夸大了。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行 / 焦虑营销把「35 岁」当成断崖式定论;内行知道它是「特定岗位 / 特定企业的偏好」而非全行业铁律,且管理岗 / 专业深耕岗 / 部分行业并不适用。
- **关联术语**:[第一学历]、[就业反歧视]、[职业空窗 gap]、[特殊群体求职]
- **可信度**: medium(社会现象) / **Decay risk**: medium

### 32. 三方协议 — tripartite agreement(国内特色)

- **Type**: term + regulation-adjacent
- **Tier**: tier-2
- **Definition (insider)**:中国大陆应届生、用人单位、学校三方签署的就业意向协议,在正式劳动合同签订前生效,涉及违约金条款、报到、户籍 / 档案派遣等。教练必须懂三方协议的约束力和违约后果,这是国内应届生求职决策(尤其手握多 offer 时)的硬约束。(evidence: [T06-S006])
- **Definition (outsider-friendly)**:国内应届生毕业前和公司、学校一起签的就业协议,有法律约束,违约通常要赔违约金。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把三方协议当「随便签、想毁就毁」;内行知道它有违约金和实际后果,签之前要想清楚。
- **关联术语**:[应届生身份]、[校招 / 社招]、[转正]、[户籍 / 档案]
- **变化历史**:三方协议制度由教育部门主导,具体格式和电子化流程各省 / 各高校逐年调整。
- **可信度**: high / **Decay risk**: medium

### 33. 应届生身份 — "fresh graduate" status(国内特色)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:国内有政策含义的身份——通常指毕业当年(及部分政策下毕业后一两年内未缴社保 / 未签劳动合同)的毕业生,关系到校招资格、部分城市落户 / 选调 / 公考的报考资格。教练要提醒应届生:这个身份有时效,某些决策(如先随便找份工作过渡)可能消耗掉它。(evidence: [T06-S007])
- **Definition (outsider-friendly)**:国内对「刚毕业的学生」有专门的身份认定,能享受校招通道和一些政策,但这个身份有时间限制。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行不知道应届生身份会「过期」或被「用掉」,随意签约 / 缴社保后才发现失去校招资格。
- **关联术语**:[校招 / 社招]、[三方协议]、[春招 / 秋招 / 提前批]、[转正]
- **可信度**: high / **Decay risk**: medium(各地认定口径不同且会调整)

### 34. 转正 / 试用期 — conversion to permanent / probation period

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:试用期 = 入职后用人单位和员工互相考察的法定期限(国内由劳动合同法规定上限);转正 = 通过试用期成为正式员工;实习转正 = 实习生转为正式员工。教练用这两个词强调「拿到 offer 不是终点」——靠造假 / 背题撑过面试的人,试用期会崩(intake 警示反复强调)。(evidence: [T06-S006])
- **Definition (outsider-friendly)**:试用期是入职后的考察期,通过了就「转正」成为正式员工。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把「拿 offer」当求职成功的终点;内行知道试用期才是真实能力的检验,造假和能力不匹配在这一关暴露。
- **关联术语**:[reference check]、[简历造假 vs 优化]、[应届生身份]、[offer]
- **可信度**: high / **Decay risk**: low

### 35. 跳槽周期 — job-hopping cadence / tenure(国内语境敏感)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:指一个人在每家公司的平均任职时长。国内 HR(及部分海外招聘方)会用「频繁跳槽」(每份工作都很短)作为隐性减分信号。教练帮候选人处理「跳槽过频」的简历叙事——不撒谎,但把短期经历合理归类 / 解释。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:你平均在一家公司待多久。换工作太频繁,有些招聘方会有顾虑。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行以为「跳得多 = 经验丰富」;内行知道频繁短期跳槽常被解读为「稳定性 / 忠诚度风险」,需要叙事处理。
- **关联术语**:[职业空窗 gap]、[转行叙事]、[reference check]
- **可信度**: medium / **Decay risk**: low

### 36. personal branding — 个人品牌

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:让目标受众(招聘方 / 行业)对「你是做什么的、擅长什么」形成清晰一致的认知,载体包括 LinkedIn / 脉脉 profile、作品、公开内容。教练用它把「求职定位」外化成可被看见的信号。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:让别人一看就知道你是什么领域、什么水平的人——通过你的简介、作品、网上形象传递出去。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把 personal branding 当「自我包装 / 吹嘘」;内行知道它是「让真实的定位被准确感知」,过度包装与真实能力不符反而是负债。
- **关联术语**:[求职定位]、[职业叙事]、[LinkedIn / 脉脉]
- **可信度**: medium / **Decay risk**: low

### 37. 职业叙事 — career narrative / career story

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:把一个人零散的经历串成一条有逻辑、指向未来目标的故事线(「我为什么从 A 走到 B,为什么现在要做 C」)。叙事派的核心概念,尤其对转行者 / 有 gap 者至关重要。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:把你的经历讲成一个连贯的故事,而不是一堆互不相干的工作罗列。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把「叙事」理解成「编故事」;内行知道职业叙事是「对真实经历的有逻辑组织和呈现」,不是虚构。
- **关联术语**:[求职定位]、[STAR]、[可迁移技能]、[转行叙事]
- **可信度**: medium / **Decay risk**: low

### 38. 反向提问 — candidate's questions to the interviewer

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:面试尾声「你有什么想问我的吗」环节,候选人向面试官提的问题。教练把它当成「双向评估 + 展示思考深度」的机会,而非走过场——好问题本身就是能力信号。(evidence: [T06-S025])
- **Definition (outsider-friendly)**:面试快结束时,面试官让你提问的环节。问什么、怎么问,本身就是评分项。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行说「没有问题」或只问薪资假期;内行知道这是展示对岗位 / 团队 / 业务真实思考的机会,也是候选人评估公司的窗口。
- **关联术语**:[行为面试]、[结构化面试]、[谈薪]
- **可信度**: medium / **Decay risk**: low

### 39. signing bonus / clawback — 签字费 / 追回条款

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:signing bonus = 入职时一次性给的奖金(常用于弥补放弃的旧公司 RSU 或作为吸引筹码);clawback = 若员工在约定期限内离职,需退还已领的签字费 / 部分薪酬的条款。教练帮候选人读懂 offer 里的这些细则。(evidence: [T06-S016, T06-S023])
- **Definition (outsider-friendly)**:签字费是入职时一次性给的钱;但通常附带条件——太早离职可能要退回来。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把签字费当「白拿的钱」或「每年都有」;内行知道它常一次性、带 clawback,要算进留任成本。
- **关联术语**:[base / bonus / RSU / 总包]、[谈薪 anchoring]、[offer 决策]
- **可信度**: high / **Decay risk**: low

### 40. vesting / 归属(股权) — equity vesting

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:RSU / 期权按时间表逐步「归属」给员工的机制(常见 4 年、含 1 年 cliff 悬崖期)。教练比较 offer 时必须算 vesting 节奏——同样的总 RSU,4 年均匀 vs backloaded(前少后多)实际价值差很多。(evidence: [T06-S016])
- **Definition (outsider-friendly)**:公司给的股票不是马上全给你,而是分几年逐步「兑现」,通常第一年满了才开始。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把 offer 上的 RSU 总额当「立刻到手的钱」;内行知道要看归属节奏和 cliff。
- **关联术语**:[base / bonus / RSU / 总包]、[offer 决策]、[竞争性 offer]
- **可信度**: high / **Decay risk**: low

### 41. 996(国内工时文化) — "996" work culture(国内特色)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:指「早 9 晚 9、一周 6 天」的高强度工作制,国内(尤其互联网业)的工时文化标签。教练在 offer 决策环节会把工时文化作为「offer 横向对比」的非薪酬维度之一,也提醒候选人在面试中如何侧面打探。(evidence: [T06-S006])
- **Definition (outsider-friendly)**:国内一种说法,指「早九点到晚九点、一周上六天」的高强度加班工作制。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行 offer 决策只看薪资数字;内行知道工时 / 强度 / 出差是要折算进「真实时薪和可持续性」的。
- **关联术语**:[offer 决策]、[base / bonus / RSU / 总包]、[反向提问]
- **可信度**: medium / **Decay risk**: medium

### 42. 作品集 — portfolio

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:设计 / 内容 / 部分产品与工程岗位的核心求职材料,用实际作品而非简历文字证明能力。教练知道对这些岗位「作品集 > 简历」,且作品集本身的呈现 / 叙事 / 选品是可辅导的。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:设计、内容这类岗位,靠展示真实作品来证明能力,这一组作品就是「作品集」。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把作品集当「作品的堆砌」;内行知道作品集要有选择(选最对口的)、有叙事(讲清你的角色和思考过程)。
- **关联术语**:[专业 / 技术面试]、[量化成就]、[求职定位]
- **可信度**: medium / **Decay risk**: low

### 43. coding 面 / 白板题 — coding interview / whiteboard interview

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:软件工程岗的算法 / 编码面试环节,常要求当场写代码解决数据结构与算法题(LeetCode 风格)。教练知道它「可大量刷题准备」,但也是「背题撑过、能力不匹配」风险的高发区(intake 警示)。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:工程师面试时当场写代码解题的环节。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行把「刷够题数」当准备完成;内行知道考的是问题分析 + 沟通 + 编码,且只刷题不练沟通照样挂。
- **关联术语**:[system design 面]、[mock interview]、[应试派 vs 能力派]
- **可信度**: high / **Decay risk**: low

### 44. 笔面经 — interview/test experience reports(国内特色)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:候选人面试 / 笔试后写的经历记录(题目、流程、问到什么),在国内(牛客网)和北美华人圈(一亩三分地)有海量积累。教练用它帮候选人做「公司情报 + 题型预判」,但提醒:笔面经是参考不是答案,且「背笔面经」≠ 有能力。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:别人面试完写下来的「面试经历」,包括问了什么题、流程怎样,供后来者参考。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把刷笔面经当「押题」;内行知道它是了解题型 / 流程的情报,不是能力的替代品。
- **关联术语**:[mock interview]、[应试派 vs 能力派]、[牛客 / 一亩三分地]
- **可信度**: medium / **Decay risk**: low

### 45. unconscious bias / 隐性偏见 — 招聘中的无意识偏见

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:招聘方在评估中不自觉受到与岗位无关因素(性别、年龄、口音、长相、校友身份、「像我」效应)影响。这是「结构化面试 + 简历匿名化」要解决的核心问题,也是教练向候选人解释「为什么有些拒绝不是你的问题」的依据。(evidence: [T06-S001, T06-S010])
- **Definition (outsider-friendly)**:招聘的人会不自觉地受一些和工作无关的因素影响——结构化流程就是用来减少这种影响的。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把所有拒绝都归因于「能力不行」或反过来「都是歧视」;内行知道偏见真实存在但程度不一,可控部分是「减少触发偏见的无关信号」,不可控部分要正确归因。
- **关联术语**:[结构化面试]、[就业反歧视]、[简历匿名化]、[ghosting]
- **可信度**: high / **Decay risk**: low

### 46. sponsorship / 工作签证 — visa sponsorship

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:雇主为外籍 / 需签证的候选人办理工作许可的承诺。海外求职(尤其国际学生)的关键约束——很多岗位 / 公司明确「不 sponsor」,是常见的 knockout 条件。教练帮国际学生筛选「会 sponsor 的雇主」并规划时间线(如美国 OPT / H-1B)。(evidence: [T06-S003])
- **Definition (outsider-friendly)**:外国人在某国工作通常需要公司「担保」办工作签证,很多公司不提供这种担保。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行(国际学生)海投所有岗位不筛 sponsorship,大量石沉大海;内行先按「是否 sponsor」过滤目标公司。
- **关联术语**:[knockout question]、[特殊群体求职]、[就业反歧视]
- **可信度**: high / **Decay risk**: medium(各国签证政策变化快)

### 47. human-voiced resume — 「有人味」的简历(Liz Ryan 概念)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:Liz Ryan 提出的概念——用真实、口语化、有人格的语言写简历,取代「负责 / 协助 / 致力于」式的官腔套话。叙事派对「简历技术派模板化」的反拨。(evidence: [T06-S019])
- **Definition (outsider-friendly)**:用像真人说话一样的语言写简历,而不是堆砌空洞的职场套话。
- **常见误用 (outsider-tell)**:`register_tell` — 外行以为简历必须用「正式僵硬」的措辞;Liz Ryan 派认为过度套话化的简历反而失去人味和说服力。
- **关联术语**:[cover letter / pain letter]、[叙事派]、[量化成就]
- **可信度**: medium(单一 figure 提出的概念,非行业统一术语) / **Decay risk**: low

### 48. 简历造假 vs 优化 — resume fabrication vs optimization(边界概念)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:行业的硬边界。优化 = ATS 关键词、量化真实成就、改善措辞和结构(合法、应做);造假 = 编造经历、改头衔、虚构数字、伪造时间线(背调和试用期会暴露,职业污点)。每个负责任的教练都必须能清晰划这条线(intake 警示反复强调)。(evidence: [T06-S014])
- **Definition (outsider-friendly)**:把简历写得更好(用对词、突出真实成绩)是优化,应该做;编造没发生的事是造假,会被查出来,后果严重。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行(和黑产话术)把「美化」和「造假」混为一谈,以为「大家都改简历」;内行有清晰的红线:呈现真实的最好版本 = OK,虚构 = 红线。
- **关联术语**:[reference check]、[量化成就]、[转正 / 试用期]、[能力造假]
- **可信度**: high / **Decay risk**: low

### 49. 竞争性 offer — competing offer(作为筹码)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:手握的多个 offer 互为筹码,用于谈薪和加速决策。教练教候选人「制造良性的 offer 并行」(把流程节奏对齐)以及如何专业地用 competing offer 谈判——但绝不教编造假 offer(危险且失信)。(evidence: [T06-S021, T06-S022])
- **Definition (outsider-friendly)**:同时拿到几个 offer,可以用一个去和另一个谈条件。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行要么不敢提 competing offer,要么编造一个不存在的;内行知道真实的 competing offer 是最强筹码,假的一旦被戳穿就全盘崩。
- **关联术语**:[谈薪 anchoring]、[counter-offer]、[offer 决策]、[recruiter screen]
- **可信度**: high / **Decay risk**: low

### 50. exploding offer — 限时 offer

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:带很短接受期限的 offer(「48 小时内答复」),常用于施压、阻止候选人等其他 offer。教练教候选人如何专业地争取延期(reasonable extension),并识别「过度施压」可能反映的公司文化信号。(evidence: [T06-S021])
- **Definition (outsider-friendly)**:给你很短时间(比如两天)就要答复的 offer,常是为了不让你再等别家。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行被 exploding offer 吓得仓促接受;内行知道大多数情况下可以礼貌地争取合理的延期。
- **关联术语**:[竞争性 offer]、[offer 决策]、[谈薪 anchoring]
- **可信度**: medium / **Decay risk**: low

### 51. onsite / final loop — 现场面 / 终面环节(海外语境)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:海外(尤其科技公司)指把多轮面试集中在一天 / 半天完成的环节(疫情后多为「virtual onsite」),通常是录用决策前的最后一关。教练帮候选人规划 onsite 当天的体力 / 节奏 / 多轮切换。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:把好几轮面试集中在一天做完的环节,通常是录用前的最后一关。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行不为「连续多轮」的体力和节奏做准备;内行知道 onsite 是耐力 + 切换能力的考验。
- **关联术语**:[recruiter screen / HR 面 / 终面]、[system design 面]、[mock interview]
- **可信度**: medium / **Decay risk**: low

### 52. 户籍 / 档案 — household registration / personnel file(国内特色)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:户籍(户口)= 国内的户籍登记,关系到落户城市 / 子女教育等;档案 = 个人人事档案,随就业派遣流转。校招 offer 决策中,「能否解决户口」「档案怎么走」是部分候选人(尤其想留一线城市的)的重要非薪酬考量。(evidence: [T06-S006])
- **Definition (outsider-friendly)**:国内的户口和人事档案制度,会影响你能在哪个城市落户、享受哪些福利,有些公司 offer 会涉及「解决户口」。
- **常见误用 (outsider-tell)**:`usage_tell` — 海归 / 外行不了解户口 / 档案对一线城市落户的影响,offer 决策时漏掉这个维度。
- **关联术语**:[三方协议]、[应届生身份]、[offer 决策]、[校招 / 社招]
- **可信度**: high / **Decay risk**: medium(落户政策逐年调整)

### 53. 求职过程管理 / application tracker — 投递追踪

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:用表格 / 工具系统化记录每个职位的投递状态、跟进时间、面试日程、联系人。教练推 application tracker 是为了把求职从「凭记忆的混乱」变成「可复盘的流程」,也支撑求职漏斗诊断。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:用一个表格或工具记录你投了哪些岗位、进展到哪一步、什么时候该跟进。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行靠记忆管理几十个投递,漏跟进、记错状态;内行知道系统化追踪是求职效率和复盘的基础设施。
- **关联术语**:[求职漏斗]、[复盘]、[精准投]
- **可信度**: medium / **Decay risk**: low

### 54. 复盘 — debrief / retrospective(求职语境)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:每次面试 / 每个阶段后系统回顾「哪些做对、哪些做错、下次怎么改」。教练把复盘当成「把单次经历转化为可迁移改进」的核心动作,与 mock interview、求职漏斗诊断配套。(evidence: [T06-S013])
- **Definition (outsider-friendly)**:每次面试后认真回顾总结,而不是「过去了就过去了」。
- **常见误用 (outsider-tell)**:`usage_tell` — 外行面试完只记得「感觉好 / 不好」;内行做结构化复盘,定位具体可改进项。
- **关联术语**:[mock interview]、[求职漏斗]、[ghosting]
- **可信度**: medium / **Decay risk**: low

### 55. 招聘方视角 / hiring manager — 用人经理

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**:hiring manager = 真正要用这个人、对录用有决定权的部门负责人(区别于 recruiter / HR)。教练教候选人「站在 hiring manager 角度想他要解决什么问题」——pain letter、精准定位、好的反向提问都建立在这个换位上。(evidence: [T06-S020])
- **Definition (outsider-friendly)**:真正要招你进团队、对要不要你说了算的那个部门领导(不是 HR)。
- **常见误用 (outsider-tell)**:`semantic_tell` — 外行把 HR / recruiter 当「决策者」;内行知道 recruiter 是流程方,hiring manager 才是用人决策方,两者关注点不同。
- **关联术语**:[recruiter screen / HR 面 / 终面]、[cover letter / pain letter]、[内推]
- **可信度**: high / **Decay risk**: low

---

## 三、标准 / 概念框架

> 求职 / 面试辅导是 `coaching_practitioner` 行业:**没有执业认证、没有行业 ISO 标准、没有针对教练本身的法规**。本节的「标准 / 概念」是两类:(a) 有扎实实证基础的有效性结论(给「哪些做法真有效」提供证据底座);(b) 影响简历 / 面试规范的外部法规框架(就业反歧视)。这是把「真方法」与「营销话术」分开的关键依据。

### 框架 1:结构化面试效度 — 为什么结构化面试预测效度更高

- **Type**: 实证概念框架(I/O 心理学甄选研究)
- **核心内容**:I/O 心理学(工业与组织心理学)数十年的甄选效度研究一致显示:**结构化面试**(统一问题 + 统一评分标准)对工作绩效的**预测效度显著高于非结构化面试**(随性聊、凭印象)。原因:结构化降低了无关因素干扰、减少了「像我」效应和隐性偏见、让不同候选人可比。(evidence: [T06-S010])
- **对求职教练的意义**:这是「行为面试可以系统准备」「面试不全是玄学 / 气场」的科学依据——结构化面试既然是按 rubric 评分,准备方向就是清晰的。也是判断面试辅导方法靠不靠谱的试金石:基于结构化面试逻辑的准备(对着能力锚点准备证据)= 靠谱;「教你读面试官微表情 / 靠气场征服」= 伪科学。
- **Issued / 稳定性**:这是积累数十年的学术共识,非单一标准文件。`Decay`: low(核心结论稳定)
- **Source**:[T06-S010](Wikipedia Structured interview 词条,内含对甄选效度元分析的引用);I/O 心理学的甄选效度文献(Schmidt & Hunter 等经典元分析)是 Track 06 学术轨的核心 — 详见 academic track。
- **可信度**: high

### 框架 2:弱关系理论 — 求职信息如何通过人脉网络流动

- **Type**: 社会学理论框架
- **核心内容**:Mark Granovetter《The Strength of Weak Ties》(1973)发现:人们找到工作的信息,更多来自「弱关系」(点头之交、前同事、二度人脉)而非「强关系」(家人密友)。因为弱关系连接到你自己圈子之外的、不重叠的信息源。(evidence: [T06-S012])
- **对求职教练的意义**:这是 networking-first 方法论(Belcak 等)和 hidden job market 概念的理论根基。它把「找关系」从「走后门」重新定义为「信息桥」,指导 networking 策略——不要只找熟人,要系统激活弱关系网络。
- **Issued / 稳定性**:1973 年发表的社会学经典,后续大量研究延伸。`Decay`: low(理论稳定;但「弱关系在数字化招聘时代的具体权重」有新研究在更新)
- **Source**:[T06-S012];Granovetter 原论文是 academic track 核心。
- **可信度**: high

### 框架 3:ATS 工作机制 — 简历解析 + 关键词检索,不是「AI 自动拒人」

- **Type**: 技术机制(HR 软件行业事实)
- **核心内容**:ATS 的核心功能是**收集、存储、解析(parsing)、检索**简历,让招聘方能在大量申请中按关键词 / 标准筛选条件搜索和排序。它本身通常**不是一个自动给简历「打分判生死」的 AI**——真正的硬性淘汰来自招聘方配置的 knockout 问题(签证 / 经验年限等)和人工筛选;现代 ATS 的解析能力已能处理适度结构化的简历。(evidence: [T06-S008, T06-S015, T06-S020])
- **对求职教练的意义**:厘清 ATS 机制,才能给出正确的简历建议——用 JD 同款关键词、避免极端花哨排版干扰解析,而不是「字体调白藏关键词」「纯文本无格式」这类基于误解的伪技巧;也不必把 ATS 妖魔化成「埋没人才的算法黑箱」。注意:ATS 厂商的 vendor docs(如 [T06-S015])对「ATS 多重要 / 匹配分多关键」有商业动机夸大,需与招聘方视角([T06-S020])交叉印证。
- **Issued / 稳定性**:ATS 作为软件类别 2000s 成熟;但 **2024-2025 招聘方在 ATS 上叠加 AI 筛选 / AI 面试的能力演化很快**。`Decay`: medium-high(机制描述需定期刷新)
- **Source**:[T06-S008](Wikipedia)、[T06-S015](Jobscan vendor docs,标 surrogate)、[T06-S020](SHRM 招聘方视角)
- **可信度**: high(机制方向稳定);具体「AI 叠加」部分 medium

### 框架 4:就业反歧视法规 — 影响简历与面试规范的外部约束(地域差异巨大)

- **Type**: regulation(地域特异 `geographic-specific`)
- **核心内容**:多数发达法域有就业反歧视立法,禁止基于受保护类别(种族、性别、年龄、宗教、残疾、婚育等)的招聘歧视。这直接塑造了「简历该放什么 / 不该放什么」「面试能问什么 / 不能问什么」的规范。
  - **US**:EEOC(Equal Employment Opportunity Commission)执行 Title VII、ADEA(年龄)、ADA(残疾)等;EEOC 还有专门的《Employment Tests and Selection Procedures》指南约束甄选程序。后果:**美式简历严格匿名化**——不放照片、不放年龄 / 出生日期、不放婚育 / 性别 / 种族信息,面试官也被规避问这些。(evidence: [T06-S001, T06-S002, T06-S003])
  - **UK / 英语区其他**:英国有 Equality Act 2010,由 EHRC(Equality and Human Rights Commission)等机构监督,规范类似(简历去身份化)。(evidence: [T06-S005])
  - **中国大陆**:就业促进法及相关规定原则上禁止就业歧视(民族、性别、宗教等),但**实践中**国内简历仍普遍带照片、年龄、性别、婚育状况,「35 岁」「第一学历」等隐性门槛广泛存在,反歧视的实际约束力与海外差距明显。(evidence: [T06-S006, T06-S007])
- **对求职教练的意义**:这是「**国内 vs 海外简历格式分野**」的根本原因——不是审美差异,是法律环境差异。教练给跨地域求职者(海归 / 出海)建议时,简历必须按 locale 重做:海外版严格匿名化,国内版按本地惯例。也是诚实边界的依据:歧视是真实的结构性约束,海外有法律工具但不能根除偏见,国内法律保护弱于实践——教练能教「约束下最大化」,不能假装约束不存在。
- **变化历史 / 时间轴**:
  - US EEOC 体系:Title VII(1964)、ADEA(1967)、ADA(1990)— 核心法规稳定 50+ 年,但 EEOC 指南和执法重点会更新(如近年对 AI 招聘工具的反歧视审查指引)。
  - UK Equality Act:2010 年整合此前多部反歧视法。
  - 中国就业促进法:2008 年施行,后续有反就业歧视相关的司法解释和地方规定补充。
  - **近 12-24 月动态**:多个法域(尤其 US 部分州)正在出台**针对 AI 招聘 / 自动化甄选工具的反歧视和透明度规定**,这是 decay 信号。
- **Decay**: medium(核心反歧视法规稳定;但「AI 招聘监管」这一子领域 12 月内大概率有新动作)
- **Source**:[T06-S001]、[T06-S002]、[T06-S003](US gov)、[T06-S005](UK gov)、[T06-S006]、[T06-S007](中国 gov)
- **可信度**: high

### 框架 5:就业市场周期 — 个人可控部分 vs 宏观不可控部分的边界

- **Type**: 概念框架(劳动经济学 / 诚实边界)
- **核心内容**:求职结果 = 个人可控部分(定位 / 简历 / 面试表现 / networking) × 宏观不可控部分(就业市场周期、行业冷热、岗位供需、年龄 / 学历结构性门槛)。2023-2025 全球科技业裁员潮 + 国内就业市场承压 + 应届生规模创新高,使宏观项的权重显著上升。劳动力市场的客观状态可由 JOLTS(US)、各国就业报告等数据观测。(evidence: [T06-S004])
- **对求职教练的意义**:这是诚实边界的核心框架——教练能优化的是可控部分,**不能把「找不到工作」全归因于「你不够努力 / 技巧不行」**(那既是 victim-blaming 也是不诚实),也不能承诺确定结果。教练的价值是「把可控部分做到最好 + 帮求职者管理预期 + 正确归因」。也是识别黑产话术的依据:无视市场周期、承诺「保 offer」的,要么不诚实要么是骗局。
- **Issued / 稳定性**:框架本身稳定;但「当前市场处于什么周期」是高频变化的事实。`Decay`: high(市场状态需持续刷新,JOLTS 等月度更新)
- **Source**:[T06-S004](US BLS JOLTS — 劳动力市场流动数据);各国就业报告见 academic / sources track。
- **可信度**: high(框架);市场状态部分 high decay

### 框架 6:呈现优化 vs 能力造假 — 面试准备的合法边界

- **Type**: 概念框架(行业伦理边界)
- **核心内容**:面试准备分两类——**呈现优化**(把真实具备的能力讲清楚、结构化、量化、脱敏紧张)是合理且应做的;**能力造假**(假装有不具备的能力、背题库撑过技术面、面试作弊 / 代面)是危险红线。区别在「你是否真的具备你所展示的能力」。(evidence: [T06-S014, T06-S025])
- **对求职教练的意义**:与「简历造假 vs 优化」是一对孪生边界,共同构成行业的硬伦理线。背题撑过面试但能力不匹配的人,试用期和实际工作会崩(背调 + 试用期是兜底检验)。负责任的教练在「应试派 vs 能力派」之争中的立场:应试技巧用于「呈现」是 OK 的,用于「伪造能力」是害了求职者。
- **Issued / 稳定性**:伦理框架,稳定。`Decay`: low
- **Source**:[T06-S014]、[T06-S025];与 intake 警示 #1/#2/#5 一致。
- **可信度**: high

### 标准 / 法规时间轴(近 5 年内有显著变化的)

| 名称 | Issued | 近期变化 | Decay |
|------|--------|---------|-------|
| US EEOC 体系(Title VII / ADEA / ADA) | 1964 / 1967 / 1990 | 核心法稳定;**近 1-2 年新增对 AI 招聘工具的反歧视指引** | medium(AI 子领域 high) |
| UK Equality Act | 2010 | 稳定 | low |
| 中国就业促进法 + 反就业歧视相关规定 | 2008 起 | 持续有司法解释 / 地方规定补充 | medium |
| **多法域 AI 招聘 / 自动化甄选监管** | 2023-2025 陆续出台 | **活跃立法中,12 月内大概率有新动作** | high |
| ATS + AI 筛选 / AI 面试机制 | — | 2024-2025 招聘两端 AI 化快速演进(非法规,是技术事实) | high |

> 长期稳定的反歧视核心法规不单列时间轴,只在框架 4 记 issued 年份。**真正的 decay 热点是「AI 招聘监管」与「ATS/AI 筛选机制」**——这是喂给 wave 3 Track 03 workflow 变化触发的核心种子。

---

## 四、外行破绽(outsider-tell)高亮

> 一开口就暴露「没被求职教练 / 资深 HR 训练过」的破绽。Phase 2 表达 DNA 节的核心 spotting tells。

| # | 外行的说法 / 做法 | 内行实际意思 / 做法 | 出现频率 | evidence |
|---|------------------|---------------------|---------|----------|
| 1 | 「ATS 是个 AI,它看不懂我的才华就把我拒了」 | ATS 主要是数据库 + 解析 + 关键词检索;硬性淘汰多来自 knockout 题和人工,不是 AI 在判生死。把 ATS 妖魔化 = 没搞懂机制 | 极高 | [T06-S008, T06-S015] |
| 2 | 「我投了 300 份简历都没回音,是市场太差 / 我运气不好」 | 投得多没回音,问题通常在定位 / 简历 / 投法(漏斗顶部),不全是市场——海投低回复率是结构性的 | 极高 | [T06-S013] |
| 3 | 「STAR 就是背 4 段答案」/ 逐字背模板 | STAR 是检查清单不是剧本;死背会被追问打穿,Action 要第一人称、Result 要量化 | 高 | [T06-S009, T06-S025] |
| 4 | 信息面谈一开口就「你们招人吗 / 能帮我内推吗」 | 信息面谈铁律是「第一次不要工作」——先了解、先建立关系、先给价值 | 高 | [T06-S017, T06-S018] |
| 5 | 「内推 = 保过 / 内定 / 走后门」 | 正规内推只是「送到起跑线」+ 一个信任背书,绝大多数公司内推仍要走完整面试 | 极高(国内尤甚) | [T06-S020] |
| 6 | 比 offer 只比 base 月薪 | 要拆总包:base + bonus + RSU,加上 vesting 节奏 / 股价 / 工时,两个 base 相同的 offer 总价可能差一倍 | 高 | [T06-S016, T06-S023] |
| 7 | 「行为面试答得流畅 = 过」 | 关键是证据强度 + 可信度 + 与岗位能力锚点的匹配,面试官在按 rubric 打分,流畅但空洞照样挂 | 高 | [T06-S010, T06-S025] |
| 8 | 把被 ghosting 解读成「我一定哪里很差」 | ghosting 高度结构性(岗位被砍 / HR 离职 / 内部候选人胜出 / 流程混乱),不是对个人价值的判决 | 高 | [T06-S013] |
| 9 | cover letter 写成「简历复述 + 一堆形容词」(「我勤奋好学有责任心」) | 有效 cover letter 要么讲一个证明性的具体故事,要么直接对接公司真实需求;空洞形容词是垃圾信号 | 高 | [T06-S019] |
| 10 | case interview 当「智力题 / 猜对答案」/ 死套框架(4P、Porter) | case 考结构化拆解 + 沟通 + 商业判断,答案不唯一,死套框架反而减分 | 中(目标咨询岗者) | [T06-S011] |
| 11 | 「HR 面不重要,HR 又不懂业务」 | recruiter / HR 是流程守门人,初筛挂掉根本到不了业务面;recruiter screen 常挂在动机 / 薪资不匹配上 | 中 | [T06-S020] |
| 12 | 把「美化简历」和「编造经历」混为一谈,觉得「大家都改简历」 | 优化(关键词 / 量化真实成就 / 措辞)和造假(虚构经历 / 头衔 / 数字)有清晰红线,背调和试用期会暴露造假 | 中高 | [T06-S014] |
| 13 | 国际学生海投所有岗位、不筛 sponsorship | 先按「是否提供签证 sponsorship」过滤目标公司,否则大量是 knockout 直接刷掉 | 中(国际学生) | [T06-S003] |
| 14 | 把「定位宽 = 机会多」,简历什么岗位都能投 | 模糊定位的简历对每个岗位都不够对口;定位窄而清反而命中率高 | 高 | [T06-S013] |
| 15 | 留学生 / 海归把海外 rolling 思维套国内校招(或反之),错过统一时间窗 | 国内校招有秋招 / 春招 / 提前批的工业化时间窗,海外是 rolling,两套节奏不能混用 | 中(跨地域求职者) | [T06-S007] |



---

## 五、行业拒绝的话术(营销 / 黑产话术 — Phase 2 表达 DNA 反例版核心素材)

> intake 明确警示:求职培训行业营销噪音和「包 offer」黑产很重。**负责任的求职教练 / 资深从业者会主动拒绝、甚至明确反对下列话术**。这些话术 ≠ 行业术语,是行业要切割的对象。Phase 2.5 表达 DNA「反例版」直接用本节——一个真懂行的求职教练,绝不会说这些话。
> **判定原则**:把「正经术语 / 有效概念」(第一~三节)和「制造焦虑 / 兜售确定性 / 黑产」(本节)分开,是本 track 的核心任务。

### 行业拒绝的话术 top 5(Phase 2 反例版核心)

| # | 营销 / 黑产话术 | 为什么行业拒绝它 | 真实情况 / 内行会怎么说 | evidence |
|---|----------------|-----------------|------------------------|----------|
| 1 | **「包 offer / 保 offer」** | 求职结果受市场周期、行业冷热、岗位供需、个人面试表现等多重因素影响,**没有人能保证 offer**。承诺「包过」要么是不诚实的营销,要么背后是黑产(买内推 / 代写造假 / 代面)。 | 教练能提升「拿到 offer 的概率」(优化可控部分),不能保证结果。任何「保过 / 包 offer」承诺都要警惕。 | [T06-S004, T06-S013, T06-S014] |
| 2 | **「内推保过 / 付费内推 / 内推直通终面」** | 正规内推只是把简历送到招聘流程 + 一个信任背书,**绝大多数公司内推仍要走完整面试**。「付费内推」「内推保过」是把内推这个正常概念黑产化——花钱买的「内推」常是伪造的,或推荐人根本不认识你、不会为你背书。 | 内推的真实价值是「让简历被真人看到」,要靠真实关系建立,不是商品。买来的内推进去面试照样挂。 | [T06-S013, T06-S020] |
| 3 | **「按我们的模板套就能拿大厂 offer」/「简历模板包过」** | 把求职简化成「填模板」,无视定位、真实能力、岗位匹配、面试承压表现。模板化简历(尤其套话 cover letter)反而是减分信号;ATS 匹配分不衡量人岗匹配本身。 | 简历是「定位 + 真实成就的有效呈现」,因人因岗定制。模板能给结构参考,不能替代内容。 | [T06-S015, T06-S019] |
| 4 | **「21 天逆袭 / 7 天速成 / 一个月从 0 到大厂」** | 制造「求职是可被快速攻破的关卡」的幻觉。求职定位、能力建设、networking、面试准备都需要时间;速成叙事配合的往往是「背题库 / 套模板」这类有上限且有风险的捷径。 | 可控部分能在合理周期内显著优化,但「逆袭」式承诺是焦虑营销。能力造假撑过面试,试用期会崩。 | [T06-S014, T06-S025] |
| 5 | **「保你进世界 500 强 / 名企内定」+ 放大「35 岁」「第一学历」焦虑卖课** | 双重套路:一边把「35 岁」「第一学历」这类结构性约束**刻意放大成断崖式定论**制造焦虑,一边兜售「内定名企」的确定性解药。前者不诚实(约束真实存在但程度因行业 / 岗位 / 公司差异极大),后者是骗局。 | 给真实图景:这些约束确实存在但不是铁律,可用经历 / 作品 / 内推 / 定位对冲。教练不贩卖焦虑也不粉饰,更不承诺「内定」。 | [T06-S007, T06-S013] |

### 其他被行业拒绝的话术 / 做法(延伸,非 top 5)

- **「代写简历(虚构经历版)/ 代投 / 面试代面 / 远程面试作弊」** —— 这些不是「服务」是黑产和造假,会害了求职者:背调暴露、试用期崩盘、职业污点甚至法律风险。是行业绝对红线。(evidence: [T06-S014])
- **「教你读面试官微表情 / 靠气场 / 话术征服面试官」** —— 把面试神秘化 / 玄学化。结构化面试是按 rubric 评分的,准备方向是「对着能力锚点准备真实证据」,不是表演术。(evidence: [T06-S010])
- **「背熟这套题库就稳了」(尤其技术岗)** —— 背题撑过面试但能力不匹配,试用期和实际工作会崩。区分「呈现优化」(合理)和「能力造假」(危险)。(evidence: [T06-S025])
- **「networking 就是求人 / 走后门」或反过来「海投就是不努力」** —— 两种极端站队都是话术。networking 是激活信息桥不是欠人情;海投 vs 精准投是「什么场景用什么」的判断问题,没有唯一正确答案。(evidence: [T06-S012, T06-S013])
- **「找不到工作就是你不够努力 / 技巧不行」** —— victim-blaming 式话术。无视市场周期和结构性约束,把宏观不可控的失败全压给求职者,既不诚实也有害。(evidence: [T06-S004])
- **把「求职教练」包装成「掌握内部资源的中间人」** —— 模糊了教练(理论上站求职者一边)与猎头(用人方付费)、与「卖内推抽成」的利益关系。利益冲突要讲清,不能含糊。(evidence: [T06-S020])



---

## Phase 2 提炼提示

### 「行业表达 DNA」直接素材(喂给 Phase 2.5 expression-DNA 提炼)

**Tier 1 高频术语 top 10(真懂行的求职教练张口就用)**:
1. ATS / 关键词匹配 — 但内行知道它是数据库不是「判生死的 AI」
2. STAR — 内行当检查清单不是背诵模板,Action 第一人称、Result 量化
3. 结构化 vs 非结构化面试 — 内行知道结构化预测效度更高
4. hidden job market / 弱关系 — networking 派的旗帜,源自 Granovetter
5. informational interview(信息面谈)— 铁律「第一次不要工作」
6. 内推 referral — 「送到起跑线 + 背书」,不是「保过」
7. 总包(base / bonus / RSU)— 比 offer 不能只比 base
8. 求职漏斗 — 内行的诊断工具:卡哪层问题在哪层
9. 求职定位 — 求职的第一性问题,定位错全白做
10. 海投 vs 精准投 / 量化成就 / 可迁移技能 — 简历与策略的核心动作语言

**行业拒绝的厂商 / 营销话术 top 5**(拒绝 → 反映行业的价值观 + 反模式,反例版核心):
1. 「包 offer / 保 offer」 → 行业价值观:教练提升概率,不兜售确定性
2. 「内推保过 / 付费内推」 → 行业价值观:内推是关系不是商品,反对黑产化
3. 「按模板套就能拿大厂 offer」 → 行业价值观:求职是定位 + 真实能力的呈现,反模板崇拜
4. 「21 天逆袭 / 速成」 → 行业价值观:反焦虑营销,反速成幻觉
5. 「保你进 500 强」+ 放大「35 岁 / 第一学历」焦虑 → 行业价值观:给真实图景,不贩卖焦虑也不粉饰
> 完整 top 5 表 + 延伸 6 条见第五节。一个真懂行的求职教练,绝不会说这些话——这是表达 DNA 反例版的硬素材。

**外行破绽 top 10(insider-only spotting tells)**:
1. 把 ATS 当「看不懂才华的 AI 黑箱」
2. 「投 300 份没回音 = 市场差 / 运气差」(实际是漏斗顶部定位 / 简历问题)
3. STAR 逐字背模板
4. 信息面谈一开口就要工作 / 要内推
5. 「内推 = 保过 / 内定」
6. 比 offer 只比 base 月薪,不拆总包
7. 「行为面试答得流畅 = 过」
8. 把 ghosting 解读成「我一定很差」(实际高度结构性)
9. cover letter 写成「形容词堆砌 + 简历复述」
10. 把「美化简历」和「编造经历」混为一谈
> 完整 15 条见第四节。

### 「智识谱系」线索(喂给 Phase 2.7 智识谱系)

- **流派分歧的术语层硬件**:本行业的核心流派之争都在 glossary 里有对应术语锚点 ——
  - networking 派 vs 网申优化派 → 锚在 [hidden job market]、[弱关系]、[informational interview] vs [ATS]、[关键词匹配]、[海投]
  - 简历技术派 vs 叙事派 → 锚在 [ATS 关键词]、[量化成就]、[模板] vs [human-voiced resume]、[职业叙事]、[cover letter / pain letter]
  - 应试派 vs 能力派 → 锚在 [背题库]、[笔面经]、[押题] vs [呈现优化 vs 能力造假]框架、[mock interview]
- **理论根**:整个 networking 方法论的智识源头是 Granovetter 弱关系理论(1973);「面试可系统准备」的智识源头是 I/O 心理学的结构化面试效度研究。两条学术根是这一行「真方法」区别于「营销话术」的底座。
- **范式更替信号**:ATS → ATS+AI 筛选 → AI 面试的演进,反映招聘从「人工筛选」到「算法 + 人工」的范式迁移;就业反歧视法规从「保护类别清单」扩展到「AI 招聘工具审查」,反映监管对自动化甄选的范式跟进。

### 「时效性」信号(喂给 Phase 2.8 诚实边界)

- **decay 热点(预计 12 月内会变)**:
  1. **多法域 AI 招聘 / 自动化甄选监管** —— 2023-2025 活跃立法中,12 月内大概率有新动作(框架 4 时间轴)
  2. **ATS + AI 筛选 / AI 面试机制** —— 2024-2025 招聘两端 AI 化快速演进,任何「具体 ATS 行为 / 破解技巧」保鲜期短
  3. **国内校招政策 / 时间窗 / 应届生认定口径** —— 逐年微调
  4. **签证 sponsorship 政策** —— 各国变化快
  5. **就业市场周期状态** —— JOLTS 等月度更新,「当前是什么市场」是高频变化的事实
- **稳定的(low decay,可长期引用)**:STAR / 行为面试 / 结构化面试 / 弱关系理论 / case interview / 求职漏斗等核心术语和概念框架,稳定 5-20+ 年。
- **诚实边界提示**:本行业「具体工具 / 话术 / 模板」保鲜期短,SKILL.md 工具与战术章节必须教「原理」(ATS 是解析+检索、结构化面试按 rubric 评分)而非只给「当下话术」。

### 「工作流变化触发」种子(喂给 wave 3 Track 03)

近 12 月内有 / 即将有变动、会改变 workflow 假设的标准 / 法规 / 机制:
1. **AI 招聘监管立法** → 改变「简历该不该为 AI 优化」「AI 面试如何应对」「招聘方能不能用 AI 自动拒」的工作流假设
2. **ATS+AI 筛选机制演进** → 改变简历优化工作流(关键词策略、格式策略、AI 生成简历的检测风险)
3. **AI 在求职两端的普及** → 求职者用 AI 改简历 / 模拟面 vs 招聘方用 AI 筛 / AI 初面,双向变化使「模拟面试」「简历定制」「公司研究」三个工作流都在重构
4. **国内校招时间窗 / 应届生政策调整** → 改变国内校招求职弧线的节奏假设

### 冷僻 / 信号薄弱评估

- 总术语数:**55**(Tier 1: 25,Tier 2: 30)—— 远超 floor 40,**不触发冷僻协议**
- Tier 1: 25 ≥ 15 ✅;Tier 1 + Tier 2 = 55 ≥ 40 ✅
- Tier 1 术语**全部填了 outsider-tell** ✅;Tier 2 术语 100% 填了 outsider-tell ✅(远超 50% 要求)
- 5 个 type 分布:**term 占绝对大头**(符合 `coaching_practitioner` 行业特征);**acronym** 适量(ATS / STAR / SBI / RSU 等);**standard / certification 为 N/A**(本行业无执业认证、无行业 ISO 标准——这是真实的行业特征,不是缺漏);**regulation** 以「外部约束」形式存在(就业反歧视法规影响简历 / 面试规范,但不规范教练本身)。
- **信号强度:健康**。不标「信号薄弱」。唯一的数据厚度注意点:**国内特色术语**(35 岁 / 第一学历 / 春秋招 / 提前批 / 户籍档案)的权威定义来源受限——gov 原文只覆盖三方协议 / 劳动合同 / 反歧视政策这类法律概念,其余社会现象类术语的解释多散落在黑名单平台(知乎 / 公众号 / 牛客),本 track 用「verified_primary 政策原文 + 海外通用术语类比 + 行业现状描述」处理,Phase 2.8 诚实边界可注明「国内非法律类术语的定义颗粒度弱于海外」。
- **国内 vs 海外术语差异(必须 Phase 2 分章呈现)**:
  - **简历**:海外严格匿名化(无照片 / 年龄 / 婚育)vs 国内普遍带照片 / 年龄 / 性别 / 婚育——根因是反歧视法律环境差异(框架 4),不是审美
  - **渠道**:海外 LinkedIn + recruiter screen + networking vs 国内 BOSS 直聘聊天式 + 牛客校招生态
  - **校招**:海外 rolling recruiting(无统一时间窗)vs 国内春招 / 秋招 / 提前批工业化时间窗
  - **薪酬**:海外 base/bonus/RSU 总包 + levels.fyi 等数据相对透明 vs 国内薪资信息透明度明显更低
  - **国内独有概念**:三方协议、应届生身份、第一学历、35 岁、户籍 / 档案、996——海外无直接对应,是国内求职的结构性约束
  - **海外独有 / 权重更高**:visa sponsorship、严格匿名化简历、EEOC 式反歧视合规、informational interview 文化(国内校招权重相对低)

---

## Track 06 完成回报

- **术语数**:55 个(Tier 1 核心 25 + Tier 2 周边 30)—— 全部填了 outsider-tell
- **标准 / 概念框架**:6 条(结构化面试效度 / 弱关系理论 / ATS 工作机制 / 就业反歧视法规 / 就业市场周期 / 呈现优化 vs 能力造假)+ 1 个标准法规时间轴
- **outsider-tell**:15 条高亮(第四节)+ 嵌入每个术语条目
- **行业拒绝的话术**:top 5 表(包 offer / 内推保过 / 模板包过 / 21 天逆袭 / 保进 500 强+放大焦虑)+ 延伸 6 条 —— Phase 2.5 反例版核心素材
- **Source Manifest**:25 条(verified_primary 7 条全为 gov:US EEOC/DOL/BLS、UK gov、中国人社部/政府网;surrogate_primary 2 条 vendor docs 已按规矩从 verifier 的 verified_primary 降级并标注;secondary 16 条 Wikipedia/词典/创作者)。黑名单平台(知乎/公众号/百度百科/CSDN/内容农场)全部未进 manifest
- **type 分布说明**:term 为主 + acronym 适量,**standard/certification = N/A**(coaching_practitioner 行业无执业认证、无行业标准,真实特征非缺漏),regulation 以「外部约束」形式存在
- **未触发冷僻协议**(55 > floor 40);唯一数据厚度注意点:国内非法律类特色术语定义来源受限,已在冷僻评估节注明
