# Track 05 — Sources（信息源:权威指南 / 机构 / 期刊 / podcast / 培训体系 / 社区）

> 行业:心理咨询 / 心理治疗(临床实践者视角) | locale=global | profile=practitioner
> Phase 1 wave 1 第 2 路。覆盖文件,last full pass 2026-05-14。

## 0. 阅读须知 — 临床领域的源分层

本 track 的源**必须**分两层读,不能混:

1. **循证 / 权威机构源(高可信)** — APA / WHO / Cochrane / NICE / 各国注册系统 / 同行评审期刊。这些是「临床共识」的 ground truth,SKILL.md 的 mental model claim 应优先挂这层。
2. **从业者社区 / 大众内容(需甄别)** — podcast / 培训机构 / 公众号 / 大众心理博客。价值在「行业氛围、争议、从业者真实声音、入门科普」,但**不能当知识真伪来源**;尤其国内大众心理内容(武志红 / KnowYourself 一类)流行说法与临床共识常有距离。

> manifest 红线:APA / WHO / Cochrane / NICE / 中国心理学会官网 → `surrogate_primary`(note「行业协会」);gov / WHO `.int` 域 → `verified_primary`;期刊官网 / DOI → `verified_primary`;podcast 官网 → `secondary`;作者裸域博客 / Substack → `secondary`。黑名单 URL(知乎 / 微信公众号 / 百度百科)绝不进 manifest。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://www.apa.org/ethics/code | surrogate_primary | 2026-05-14 | American Psychological Association | 行业协会 — APA 伦理守则全文,北美伦理 ground truth |
| T05-S002 | https://www.div12.org/treatments/ | surrogate_primary | 2026-05-14 | APA Division 12 (Society of Clinical Psychology) | 行业协会 — 循证治疗清单(按障碍 × 流派分级) |
| T05-S003 | https://www.cochranelibrary.com/ | surrogate_primary | 2026-05-14 | Cochrane Collaboration | 行业协会 — 系统综述金标准,Common Mental Disorders 组 |
| T05-S004 | https://www.nice.org.uk/guidance | surrogate_primary | 2026-05-14 | NICE (UK) | 行业协会 — 英国 NHS 临床指南,按障碍出 stepped-care 路径 |
| T05-S005 | https://www.who.int/standards/classifications/classification-of-diseases | verified_primary | 2026-05-14 | World Health Organization | WHO 一手 — ICD-11 诊断分类官方入口 |
| T05-S006 | https://www.apaservices.org/practice | surrogate_primary | 2026-05-14 | APA Services | 行业协会 — 执业实务指引(记录 / 远程治疗 / 法律) |
| T05-S007 | https://www.psychiatry.org/psychiatrists/practice/dsm | surrogate_primary | 2026-05-14 | American Psychiatric Association | 行业协会 — DSM-5-TR 官方页(注意:APA = 精神医学会,与心理学会不同) |
| T05-S008 | http://www.chinacpb.org/ | surrogate_primary | 2026-05-14 | 中国心理学会临床与咨询心理学专业委员会 | 行业协会 — 国内注册系统标准 + 伦理守则;访问不稳定 |
| T05-S009 | https://www.apa.org/pubs/journals/ccp | surrogate_primary | 2026-05-14 | APA / JCCP | 行业协会刊物 — Journal of Consulting and Clinical Psychology |
| T05-S010 | https://www.apa.org/pubs/journals/pst | surrogate_primary | 2026-05-14 | APA / Div 29 | 行业协会刊物 — Psychotherapy(过程-关系-整合取向) |
| T05-S011 | https://www.journals.elsevier.com/clinical-psychology-review | secondary | 2026-05-14 | Elsevier | 期刊官网 — Clinical Psychology Review,只发综述/元分析;商业出版社门户,classifier 判 secondary |
| T05-S012 | https://www.tandfonline.com/journals/uemr20 | secondary | 2026-05-14 | Taylor & Francis / EMDRIA-linked | 期刊官网 — 占位:创伤/EMDR 方向期刊群入口;商业出版社门户,classifier 判 secondary |
| T05-S013 | https://www.psychotherapyresearch.org/ | surrogate_primary | 2026-05-14 | Society for Psychotherapy Research (SPR) | 行业协会 — 心理治疗过程-结果研究学会,办 Psychotherapy Research 期刊 |
| T05-S014 | https://therapistuncensored.com/ | secondary | 2026-05-14 | Sue Marriott & Ann Kelley | podcast 官网 — 依恋 / 神经科学取向,practitioner 向 |
| T05-S015 | https://verybadtherapy.com/ | secondary | 2026-05-14 | Carrie Wiita & Ben Fineman | podcast 官网 — 来访者讲「糟糕治疗」经历,反思治疗失败 |
| T05-S016 | https://shrinkrapradio.com/ | secondary | 2026-05-14 | David Van Nuys | podcast 官网 — 长访谈档案库,2005 年至今覆盖各流派人物 |
| T05-S017 | https://www.estherperel.com/podcast | verified_primary | 2026-05-14 | Esther Perel | brand 一手 — Where Should We Begin,真实伴侣会谈录音 |
| T05-S018 | https://societyforpsychotherapy.org/ | surrogate_primary | 2026-05-14 | APA Division 29 | 行业协会 — Div 29 网刊,短文形态的过程/整合派内容 |
| T05-S019 | https://www.contextualscience.org/ | surrogate_primary | 2026-05-14 | ACBS | 行业协会 — ACT / RFT 官方学会,培训目录 + 资源 |
| T05-S020 | https://www.emdria.org/ | surrogate_primary | 2026-05-14 | EMDRIA | 行业协会 — EMDR 北美认证体系 + 培训目录 |
| T05-S021 | https://ifs-institute.com/ | surrogate_primary | 2026-05-14 | IFS Institute (R. Schwartz) | 行业协会/机构 — IFS 官方培训(Level 1-3)体系 |
| T05-S022 | https://www.beckinstitute.org/ | surrogate_primary | 2026-05-14 | Beck Institute (J. Beck) | 机构 — CBT 官方培训认证 + CE 课程 |
| T05-S023 | https://www.psychotherapy.net/ | secondary | 2026-05-14 | Psychotherapy.net | 内容站 — 流派演示视频库 + 访谈,培训补充材料 |
| T05-S024 | https://www.apa.org/monitor | surrogate_primary | 2026-05-14 | APA Monitor on Psychology | 行业协会 — APA 会员月刊,行业动态/政策/职业图景 |
| T05-S025 | https://offthecouch.libsyn.com/ | secondary | 2026-05-14 | various analysts | podcast 官网 — 精神分析取向访谈,niche senior 向 |

> 国内一手深度信息源说明:曾奇峰 / 李松蔚 / KnowYourself / 武志红 的主阵地是微信公众号(黑名单 URL,绝不进 manifest)。简单心理 Uni / 壹心理学院主要是 app/小程序内课程,无稳定可引用 web URL。这导致**国内侧 manifest 条目稀薄** — 已在 Phase 2 接口诚实标注,不硬塞黑名单 URL。

---

## 1. 权威指南 / 机构 — Top 5（循证 / 高可信层）

> 这五个是临床「能说什么算共识」的裁判席。SKILL.md 任何「循证证据强」「指南推荐」类 claim 应回到这层,而不是回到 podcast 或公众号。

### 📋 1. APA Division 12 — 循证治疗清单（Research-Supported Psychological Treatments）

- **Type**: 机构指南库 / rolling 数据库
- **URL**: https://www.div12.org/treatments/
- **Maintainer**: APA Division 12(Society of Clinical Psychology)
- **Cadence**: rolling(新研究出来后更新条目,非定期发布)
- **Last activity**: 持续维护,2024-2025 仍在更新条目(机构级,稳定)
- **Audience tier**: practitioner / senior
- **One-liner**: 「障碍 × 流派」二维查表 —— 想知道「焦虑障碍下哪些治疗有强证据」,这是最快的权威入口,把流派之争降维成可查的证据等级 (evidence: [T05-S002])
- **典型内容**: 每个条目按障碍组织(抑郁 / PTSD / 强迫 / 边缘性人格…),列出该障碍下「Strong Research Support / Modest Support」的具体治疗,附关键 RCT 引用与一句话疗法描述。是 intake.json 中 key_tools「APA Division 12 清单」的源头。
- **投入产出比**: high —— 不是订阅式 source,是工具书式 source,接到不熟悉的障碍/流派时查一次省大量时间 (evidence: [T05-S002])
- **Paywall**: none
- **可信度**: high(APA 官方分会,同行评审证据驱动)
- **Decay risk**: low(机构级基础设施)
- **甄别提示**: 它呈现的是「有 RCT 证据支持」,不等于「最适合这个来访者」—— 精神动力 / 人本取向的证据形态不同(过程研究 / 长程随访),不在此清单不代表无效。SKILL.md 引用时必须带这句。

### 📋 2. Cochrane Library（Common Mental Disorders 相关综述）

- **Type**: 系统综述数据库
- **URL**: https://www.cochranelibrary.com/
- **Maintainer**: Cochrane Collaboration(国际非营利)
- **Cadence**: rolling(综述持续更新版本)
- **Last activity**: 持续,机构级稳定
- **Audience tier**: senior(读元分析需要方法学基础)
- **One-liner**: 心理治疗疗效证据的「最高法院」—— 系统综述 + 元分析的金标准,判断「这个疗法到底有多硬的证据」时的终审参考 (evidence: [T05-S003])
- **典型内容**: 针对某一干预-某一障碍的系统综述,GRADE 证据分级,森林图,异质性分析。抑郁、焦虑、PTSD、失眠的心理治疗综述都在 Common Mental Disorders / Depression, Anxiety and Neurosis 组下。
- **投入产出比**: medium —— 信号极硬但单篇阅读成本高,作 ambient reference 而非每周读 (evidence: [T05-S003])
- **Paywall**: 摘要 + Plain Language Summary 免费;全文多数地区通过机构订阅,部分国家(含中国)有国家级免费许可
- **可信度**: high
- **Decay risk**: low

### 📋 3. NICE Guidelines（英国 — 心理健康临床指南）

- **Type**: 国家级临床指南
- **URL**: https://www.nice.org.uk/guidance(心理健康专题在 Conditions and diseases > Mental health and behavioural conditions)
- **Maintainer**: National Institute for Health and Care Excellence(英国 NHS）
- **Cadence**: 每个指南有定期 review 周期(数年一次大修),期间出 surveillance 更新
- **Last activity**: 持续;抑郁、PTSD、社交焦虑等指南均在 2022-2024 有更新
- **Audience tier**: practitioner / mixed
- **One-liner**: 把证据翻译成「分级照护(stepped care)」可执行路径 —— 不只说「什么有效」,还说「先做什么、什么时候升级」,是英联邦体系临床决策的事实标准 (evidence: [T05-S004])
- **典型内容**: 每个障碍一份指南,含 stepped-care 模型(从低强度干预到高强度治疗到药物)、推荐的具体治疗与疗程、转诊节点。比 Div 12 清单更「操作化」。
- **投入产出比**: high —— 即使不在英国执业,stepped-care 框架对个案概念化和转介决策有直接迁移价值 (evidence: [T05-S004])
- **Paywall**: none(全文免费公开)
- **可信度**: high
- **Decay risk**: low
- **locale 提示**: 路径与英国 NHS 资源绑定,中国 / 美国执业者取其「证据 → 决策」的方法论,不照搬具体转诊流程。

### 📋 4. APA 伦理守则 + APA Services 执业实务（Ethics Code + Practice）

- **Type**: 伦理守则 + 执业实务指引
- **URL**: https://www.apa.org/ethics/code ; https://www.apaservices.org/practice
- **Maintainer**: American Psychological Association
- **Cadence**: 伦理守则数年一修(现行 2017 修订版);Practice 资源 rolling 更新
- **Last activity**: 持续维护
- **Audience tier**: practitioner / mixed
- **One-liner**: 北美心理治疗伦理的成文 ground truth —— 保密及其例外、知情同意、双重关系、胜任力范围的判断都回到这里 (evidence: [T05-S001, T05-S006])
- **典型内容**: 伦理守则五大 General Principles + 十类 Ethical Standards 条文;Practice 板块覆盖记录保存、远程心理治疗(telepsychology)指引、法律风险。intake.json 警示「伦理与法律是硬约束」的成文出处。
- **投入产出比**: high(作为 reference 必备;伦理是硬边界不是建议)
- **Paywall**: none
- **可信度**: high
- **locale 提示**: 这是美国体系。英国对应 BACP / UKCP 的伦理框架(Ethical Framework for the Counselling Professions);中国对应中国心理学会注册系统伦理守则(见 S008)。SKILL.md 伦理章必须按 locale 分,不能把 APA 守则当全球通用。

### 📋 5. 中国心理学会临床与咨询心理学专业委员会 — 注册系统（中国大陆 ground truth）

- **Type**: 行业自律组织 / 注册标准 + 伦理守则
- **URL**: http://www.chinacpb.org/(注:本次核验访问不稳定,可能需多次尝试或查中国心理学会主站 cpsbeijing.org 转入)
- **Maintainer**: 中国心理学会临床与咨询心理学专业委员会(注册工作委员会)
- **Cadence**: 注册标准与伦理守则数年一修;注册系统名录持续更新
- **Last activity**: 注册系统持续运行;伦理守则现行为修订版本
- **Audience tier**: practitioner(国内从业者)
- **One-liner**: 2017 年人社部取消「心理咨询师」国家职业资格认证后,这套「注册心理师 / 注册督导师」体系是中国大陆**最接近行业公认门槛**的标准,也是国内伦理守则的成文出处 (evidence: [T05-S008])
- **典型内容**: 注册心理师 / 注册督导师的申请条件(学历 + 受训时数 + 督导时数 + 个人体验时数)、注册系统伦理守则、注册机构与注册督导师名录。
- **投入产出比**: high —— 国内 locale 章节的锚点,判断「什么算正规受训路径」绕不开它 (evidence: [T05-S008])
- **Paywall**: none
- **可信度**: high(国内行业语境下的权威自律组织;但非政府强制持照 —— 这点本身要写进 SKILL.md)
- **Decay risk**: medium(网站工程稳定性差;标准本身稳定)
- **背景标注（必写进 SKILL.md）**: 注册系统是「行业自律」不是「法律持照」。中国大陆目前没有国家强制的心理咨询执业牌照;注册心理师是自愿注册的高标准认证,不是从业法律前提。这与欧美的强制持照(美国各州 licensing board / 英国 statutory regulation 讨论)体系本质不同。

## 2. 期刊 — Top 5

> 临床实践者真实订阅的不是「读每一期」,而是「需要某主题最新证据时回这几本查」。这五本覆盖循证 / 过程-关系 / 综述三个证据形态。

### 📰 1. Journal of Consulting and Clinical Psychology（JCCP）

- **Type**: 同行评审期刊
- **URL**: https://www.apa.org/pubs/journals/ccp
- **Maintainer**: APA
- **Cadence**: monthly
- **Last activity**: 持续出刊(2025 在刊)
- **Audience tier**: senior(实证研究为主,读需方法学基础)
- **One-liner**: 临床心理学循证治疗 RCT 的旗舰刊 —— 「这个疗法对这个障碍有效吗」类问题的一手研究主要发在这里 (evidence: [T05-S009])
- **典型每期内容**: 治疗结果 RCT、干预的调节/中介机制、评估工具的心理测量学研究。CBT / DBT / 暴露疗法等手册化治疗的关键试验常见于此。
- **投入产出比**: medium —— 不必每期读,作「某障碍治疗证据」的检索目标库;一线临床者更多通过综述刊间接消费它 (evidence: [T05-S009])
- **Paywall**: 多数文章机构订阅;部分 open access
- **可信度**: high
- **Decay risk**: low

### 📰 2. Psychotherapy（APA Division 29）

- **Type**: 同行评审期刊
- **URL**: https://www.apa.org/pubs/journals/pst
- **Maintainer**: APA Division 29(Society for the Advancement of Psychotherapy)
- **Cadence**: quarterly
- **Last activity**: 持续出刊(2025 在刊)
- **Audience tier**: practitioner / senior
- **One-liner**: 治疗「过程、关系、共同要素」的核心阵地 —— 治疗联盟、共情、整合取向的实证研究在这里,是「关系 > 流派」一派的学术家 (evidence: [T05-S010])
- **典型每期内容**: 治疗联盟与疗效的实证、治疗师效应、流派整合、共同要素研究。与 JCCP 的「技术-障碍」视角互补 —— 这本看「关系-过程」。intake.json 子领域「治疗关系与共同要素」的期刊源。
- **投入产出比**: medium-high —— 对在职临床者比纯 RCT 刊更「可读」,过程类发现更易迁移到下一次会谈 (evidence: [T05-S010])
- **Paywall**: 机构订阅为主;Div 29 会员含订阅
- **可信度**: high
- **Decay risk**: low

### 📰 3. Clinical Psychology Review

- **Type**: 同行评审期刊（只发综述 / 元分析）
- **URL**: https://www.journals.elsevier.com/clinical-psychology-review
- **Maintainer**: Elsevier
- **Cadence**: 约 8 期/年
- **Last activity**: 持续出刊(2025 在刊)
- **Audience tier**: practitioner / senior
- **One-liner**: 不发原始研究、只发综述与元分析 —— 想用一篇文章追上某主题的整体证据格局,这本投入产出比最高 (evidence: [T05-S011])
- **典型每期内容**: 某障碍/某干预的系统综述、元分析、理论整合综述。对临床者是「证据地图」式的入口,一篇抵几十篇 RCT。
- **投入产出比**: high —— 综述刊的性质决定了单篇信息密度高,是一线临床者性价比最高的期刊源 (evidence: [T05-S011])
- **Paywall**: 机构订阅为主;部分 open access
- **可信度**: high
- **Decay risk**: low

### 📰 4. Psychotherapy Research（SPR 会刊）

- **Type**: 同行评审期刊
- **URL**: 经 Society for Psychotherapy Research 入口 https://www.psychotherapyresearch.org/(Taylor & Francis 出版)
- **Maintainer**: Society for Psychotherapy Research(SPR)
- **Cadence**: 约 8 期/年
- **Last activity**: 持续出刊(2025 在刊)
- **Audience tier**: senior
- **One-liner**: 国际心理治疗过程-结果研究的专门刊 —— 治疗如何起效(机制 / 过程 / 时刻)而非是否起效,共同要素研究(Wampold 一脉)的重要发表地 (evidence: [T05-S013])
- **典型每期内容**: 治疗过程的精细研究、时刻分析、治疗师差异、跨文化心理治疗研究。是 Track 06 学术轨「共同要素 / 过程研究」的期刊源。
- **投入产出比**: medium —— niche,主要对深入过程研究的 senior 从业者;一般临床者作 ambient awareness (evidence: [T05-S013])
- **Paywall**: 机构订阅;SPR 会员含订阅
- **可信度**: high
- **Decay risk**: low

### 📰 5. 《中国心理卫生杂志》/《心理学报》临床方向（中国大陆）

- **Type**: 同行评审期刊（中文）
- **URL**: 无稳定独立官网可作 verified_primary;通过中国知网 / 万方检索(知网为黑名单聚合站,不进 manifest 作 URL,仅说明检索路径)
- **Maintainer**:《中国心理卫生杂志》由中国心理卫生协会主办;《心理学报》由中国心理学会主办
- **Cadence**: monthly（《中国心理卫生杂志》)/ monthly（《心理学报》)
- **Last activity**: 均持续出刊
- **Audience tier**: practitioner / senior
- **One-liner**: 国内临床与咨询心理学实证研究(含本土化研究、量表中国常模、本土干预试验)的主要中文发表地 (evidence: 国内期刊体系常识 — manifest URL gap, 见下)
- **典型每期内容**:《中国心理卫生杂志》偏临床与精神卫生应用、量表修订与常模、干预研究;《心理学报》是综合性顶刊,临床方向文章占比小但质量高。
- **投入产出比**: medium —— 国内 locale 章节的本土证据源;但与海外刊相比,心理治疗 RCT 的体量与方法学严格度仍在追赶 (evidence: 见下 manifest gap 说明)
- **Paywall**: 通过知网 / 万方等数据库订阅(机构)
- **可信度**: high(期刊本身权威);medium(作为「临床治疗证据源」的厚度 —— 国内心理治疗高质量 RCT 数量仍有限)
- **Decay risk**: low
- **manifest gap 说明**: 两刊无可作 `verified_primary` 的稳定独立官网,主流访问路径是知网(黑名单聚合站)。诚实标注:**国内期刊源在 manifest 中缺可引用 URL**,Phase 4 若需补,优先找 DOI 或主办协会页。

## 3. Podcast — Top 5（从业者社区层 — 需甄别）

> 这层的价值是「行业氛围、争议、从业者真实声音、入门访谈」,**不是知识真伪来源**。听一个流派创立者的长访谈了解 ta 怎么想,有价值;把 podcast 一句话当临床共识引用,不行。

### 🎙️ 1. Therapist Uncensored

- **Type**: podcast
- **URL**: https://therapistuncensored.com/
- **Host**: Sue Marriott(LCSW)& Ann Kelley(PhD)—— 二人均为执业临床者
- **Cadence**: biweekly 左右(rolling,多年稳定产出)
- **Last activity**: 持续更新,2025 在更(本次核验官网 200)
- **Audience tier**: practitioner / mixed —— 从业者听同行,也有受过教育的来访者听众
- **One-liner**: 依恋理论 + 人际神经生物学(IPNB)取向的从业者长谈 —— 把依恋、调节、创伤的当代研究翻成临床者能用的语言 (evidence: [T05-S014])
- **典型每期内容**: 围绕依恋类型、神经科学、关系修复、治疗师自我成长的主题集;常请相关领域作者/研究者对谈。偏「整合 + 依恋 + 神经科学」这条线。
- **投入产出比**: medium —— 主题集质量稳,但属「拓宽视野 / ambient」而非「每集必有 actionable」,不必每集追 (evidence: [T05-S014])
- **签名内容**: 依恋类型系列、与创伤/神经科学作者的访谈集(具体集名未逐集核验,Phase 2 如需 topic-heat 高置信度需爬 episode list)
- **Endorsement evidence**: cross_source(被多个从业者向 podcast 推荐列表收录);community_consensus(治疗师社群常被点名为「入门依恋科学」推荐)
- **替代品**: Attachment Theory in Action(更窄、更临床培训向)
- **可信度**: medium(host 是持照临床者,内容靠谱;但 podcast 体裁本身非证据源)
- **Decay risk**: medium(双 host 个人 podcast,默认 medium;运行多年降低风险)

### 🎙️ 2. Very Bad Therapy

- **Type**: podcast
- **URL**: https://verybadtherapy.com/
- **Host**: Carrie Wiita & Ben Fineman(均为执业治疗师)
- **Cadence**: 大致 weekly/biweekly
- **Last activity**: 持续更新(本次核验官网 200)
- **Audience tier**: practitioner —— 主要听众是从业者,用别人的失败案例反思自己
- **One-liner**: 请「经历过糟糕治疗」的来访者讲述,再由两位治疗师复盘哪里出了问题 —— 行业里少有的「从失败学习」结构,直击伦理边界、治疗联盟破裂、文化不敏感 (evidence: [T05-S015])
- **典型每期内容**: 前半段来访者第一人称讲述一段不好的治疗经历,后半段两位 host 拆解:边界、知情同意、流派误用、治疗师自恋、文化议题。是 intake.json「伦理边界 / 治疗关系」的反面教材库。
- **投入产出比**: high —— 对从业者罕见的高信号:每集都是一个「不要这样做」的具体案例,直接喂临床判断 (evidence: [T05-S015])
- **签名内容**: 多集涉及治疗师越界 / 治疗联盟破裂的复盘(具体集名未逐集核验)
- **Endorsement evidence**: cross_source(被多个「最佳治疗师 podcast」列表收录);community_consensus(从业社群推荐为「伦理与失败反思」必听)
- **替代品**: 无直接对应 —— 「从来访者角度复盘失败治疗」这个结构较独特
- **可信度**: medium(体裁限制 —— 单一来访者叙述有主观性;但 host 的复盘是临床视角)
- **Decay risk**: medium

### 🎙️ 3. Shrink Rap Radio

- **Type**: podcast（访谈档案库）
- **URL**: https://shrinkrapradio.com/
- **Host**: David Van Nuys(PhD,退休心理学教授)
- **Cadence**: rolling(发布频率随年份变化,近年放缓但仍在更新)
- **Last activity**: 仍在更新(本次核验 406 = bot 拦截非死站;站点为 2005 至今的活跃档案)
- **Audience tier**: mixed —— 入门到 senior 都能取用,因覆盖面极广
- **One-liner**: 2005 年至今数百集的访谈档案 —— 各流派的人物、研究者、临床者几乎都进过,是「想了解某个取向 / 某个人怎么想」的免费深访谈库 (evidence: [T05-S016])
- **典型每期内容**: 一对一长访谈,嘉宾覆盖精神分析、荣格、CBT、创伤、超个人心理学、神经科学等。价值更多在「档案库」属性 —— 按嘉宾/主题翻旧集。
- **投入产出比**: medium —— 作「点播式档案库」高价值,作「订阅追更」一般;按需翻特定嘉宾集最划算 (evidence: [T05-S016])
- **签名内容**: 与各流派代表人物的历史访谈集(具体集名未逐集核验)
- **Endorsement evidence**: cross_source(长寿 + 被反复引为心理学 podcast 元老);community_consensus
- **替代品**: 无 —— 档案深度与年限难替代
- **可信度**: medium
- **Decay risk**: medium(host 已退休,产出放缓;但已存档案不会消失,作为档案库 decay 低)

### 🎙️ 4. Where Should We Begin?（Esther Perel）

- **Type**: podcast
- **URL**: https://www.estherperel.com/podcast
- **Host**: Esther Perel(执业伴侣治疗师)
- **Cadence**: 按季发布(season-based)
- **Last activity**: 持续(按季);2024-2025 仍有新内容
- **Audience tier**: mixed —— 大众听众多,从业者也听「真实会谈长什么样」
- **One-liner**: 真实(匿名)伴侣 / 个体的单次会谈录音 —— 极少数能让从业者「旁听」一位资深治疗师实际工作的公开素材 (evidence: [T05-S017])
- **典型每期内容**: 一对来访者的一次匿名会谈完整录音,Esther Perel 现场工作。对从业者的价值是「过程示范」:提问、节奏、命名情绪、处理张力。
- **投入产出比**: medium —— 作「过程观摩」价值高,但单一治疗师 / 单一取向,不能当通用模板;且 Perel 本人已在 love-coach-master 蒸馏,本 skill 引用其框架不重复列为主要人物 (evidence: [T05-S017])
- **Paywall**: 部分集 / 完整版通过付费(Audible / 订阅);部分免费 —— 标 `paywall: 部分内容付费`,过程观摩价值使其仍 worth 收录
- **签名内容**: 各季匿名伴侣会谈集
- **Endorsement evidence**: figure_short(Perel 本人即 figure,love-coach skill 已覆盖);cross_source
- **可信度**: medium(过程示范有价值;非证据源,且取向单一)
- **Decay risk**: low(机构化运营 + 大流量,稳定)
- **边界提示**: 与 love-coach-master 重叠 —— 本 skill 取其「伴侣治疗临床过程示范」一面,「亲密关系日常经营」导向 love-coach。

### 🎙️ 5. New Books in Psychoanalysis / Off the Couch（精神分析取向访谈 — niche）

- **Type**: podcast
- **URL**: https://offthecouch.libsyn.com/(Off the Couch);另有 New Books Network 的 Psychoanalysis 频道作平行选择
- **Host**: 执业分析师(轮值 / 多 host)
- **Cadence**: rolling
- **Last activity**: 持续(libsyn 托管,在更)
- **Audience tier**: senior —— 听众基础小,主要是精神分析取向受训者 / 从业者
- **One-liner**: 精神分析 / 精神动力取向的人物与著作访谈 —— 平衡 podcast 列表里偏 CBT/依恋的倾向,给动力取向从业者一个声音 (evidence: [T05-S025])
- **典型每期内容**: 与精神分析作者 / 临床者对谈,围绕移情反移情、防御、长程工作、理论流派。
- **投入产出比**: low-medium —— niche, primarily senior practitioner audience;作 ambient awareness (evidence: [T05-S025])
- **Endorsement evidence**: community_consensus(精神分析受训圈推荐);cross_source(被「精神分析 podcast」列表收录)
- **替代品**: New Books in Psychoanalysis(同生态,更新更勤)
- **可信度**: medium
- **Decay risk**: medium(niche + 轮值 host)

> Podcast 层整体甄别提示:五个 host 均为执业临床者或资深教授,内容相对可靠 —— 但 podcast 永远是「从业者声音」不是「临床共识裁判」。SKILL.md 引用 podcast 只能用于「行业氛围 / 争议 / 人物观点 / 过程示范」,知识真伪回到第 1、2 节。

## 4. 培训体系 — 5

> **国内背景红线（必写进 SKILL.md）**:2017 年人社部取消「心理咨询师」国家职业资格认证后,国内认证市场陷入混乱 —— 山寨证书、培训机构自发证、「21 天 / 考证躺赚」营销泛滥(intake.json 警示)。本节区分:**国外有协会认证体系的正规培训** vs **国内「连续培训项目 + 注册系统」这类被行业公认的正规路径** vs(不列入但提示存在的)营销噪音。判断「正规」的锚:有无学会/协会背书、有无结构化时数要求、有无督导与个人体验环节。

### 🎓 1. Beck Institute（CBT 官方培训认证）

- **Type**: 培训机构 / 认证体系
- **URL**: https://www.beckinstitute.org/
- **Maintainer**: Beck Institute for Cognitive Behavior Therapy（Judith Beck 主持,Aaron Beck 创立）
- **Cadence**: rolling(常年开课 + workshop + CE 课程)
- **Last activity**: 持续运营(2025 在办)
- **Audience tier**: practitioner / mixed
- **One-liner**: CBT 的「祖庭」官方培训 —— CBT 认证(CBT certification)、临床者培训、CE 课程的权威来源,intake.json figures「Beck 父女」的机构延续 (evidence: [T05-S022])
- **典型内容**: CBT 基础到进阶培训、特定障碍的 CBT 培训、面向机构的培训、CBT 治疗师认证项目。
- **投入产出比**: high(对走 CBT 路线的从业者,这是 gold-standard 认证来源) (evidence: [T05-S022])
- **Paywall**: 课程收费(培训机构性质)
- **可信度**: high(流派创立机构,正规认证)
- **Decay risk**: low
- **正规性**: ✅ 正规 —— 流派创立机构 + 结构化认证体系。

### 🎓 2. ACBS（ACT / RFT 官方学会与培训生态）

- **Type**: 学会 + 培训认证生态
- **URL**: https://www.contextualscience.org/
- **Maintainer**: Association for Contextual Behavioral Science（Steven Hayes 一脉）
- **Cadence**: rolling(培训目录持续更新 + 年度世界大会)
- **Last activity**: 持续运营,办年度 ACBS World Conference
- **Audience tier**: practitioner / senior
- **One-liner**: ACT 的官方学会 —— 培训目录、peer-reviewed trainer 名录、年度大会,intake.json figures「Steven Hayes / ACT」的机构家 (evidence: [T05-S019])
- **典型内容**: ACT 培训目录与认可 trainer 名录、RFT 资源、年度世界大会(兼具 conference 属性)、会员资源库。
- **投入产出比**: high(走第三浪潮 / ACT 路线的从业者必跟) (evidence: [T05-S019])
- **Paywall**: 会员制 + 培训收费;部分资源公开
- **可信度**: high
- **Decay risk**: low
- **正规性**: ✅ 正规 —— 国际学会 + 认可 trainer 体系。

### 🎓 3. EMDRIA / IFS Institute（创伤治疗专项认证）

- **Type**: 培训认证体系（两个,创伤方向并列)
- **URL**: https://www.emdria.org/（EMDR);https://ifs-institute.com/（IFS)
- **Maintainer**: EMDR International Association;IFS Institute（Richard Schwartz)
- **Cadence**: rolling
- **Last activity**: 均持续运营(2025 在办)
- **Audience tier**: practitioner / senior
- **One-liner**: 创伤治疗两条主流路线的官方认证家 —— EMDRIA 管 EMDR 北美认证与培训目录,IFS Institute 管 IFS 的 Level 1-3 阶梯培训 (evidence: [T05-S020, T05-S021])
- **典型内容**: EMDRIA — EMDR 基础培训认可、Certified Therapist / Approved Consultant 认证、培训目录;IFS Institute — Level 1/2/3 官方培训、认证、继续教育。对应 intake.json figures Shapiro(EMDR)、Schwartz(IFS)。
- **投入产出比**: high(创伤方向从业者认证绕不开) (evidence: [T05-S020, T05-S021])
- **Paywall**: 培训收费
- **可信度**: high
- **Decay risk**: low
- **正规性**: ✅ 正规 —— 流派官方认证体系。

### 🎓 4. 国内精神分析连续培训项目（中德班 / 中挪班 / 中美班)

- **Type**: 长程结构化连续培训项目
- **URL**: 无统一官网 —— 各项目分散在主办机构(如中德心理医院 / 各地精神卫生中心 / 大学)。中德项目相关信息可经施琪嘉一脉机构(德中心理治疗研究院方向)了解;manifest 无稳定可引用 URL
- **Maintainer**: 中德心理治疗研究院(中德班)、中挪 / 中美精神分析连续培训项目各主办方
- **Cadence**: 多年期项目(典型 2-3 年一期,分阶段集中授课 + 督导 + 个人体验)
- **Last activity**: 持续招生开班(行业内长期运行的成熟项目)
- **Audience tier**: practitioner / senior
- **One-liner**: 中国大陆精神动力 / 精神分析取向从业者**公认的正规深度受训路径** —— 在 2017 取消国家资格证后认证混乱的背景下,「上过中德 / 中挪 / 中美班」是国内行业内被广泛认可的受训凭证 (evidence: 国内培训生态常识 — manifest URL gap, 见下)
- **典型内容**: 多年期、分阶段的理论授课 + 案例督导 + 受训者个人体验(被分析),由中外资深分析师授课。intake.json figures 施琪嘉、曾奇峰均与此生态深度关联。
- **投入产出比**: high —— 对走精神动力路线的国内从业者,这是「正规」的事实标准之一 (evidence: 见下 manifest gap 说明)
- **Paywall**: 项目收费(长程培训,费用高)
- **可信度**: high(行业内公认正规)
- **Decay risk**: low(成熟项目长期运行)
- **manifest gap 说明**: 这类项目无统一官网、无稳定可引用 URL,信息分散在主办机构页与培训圈口碑中。诚实标注:**国内培训体系在 manifest 中缺可引用一手 URL** —— 这是国内 locale 信息源结构性偏薄的一部分。
- **正规性**: ✅ 正规 —— 结构化时数 + 督导 + 个人体验,行业公认。**对照**:与之相对的「21 天速成」「网课考证拿咨询师证」是营销噪音,不是受训路径,SKILL.md 必须点破。

### 🎓 5. 简单心理 Uni / 壹心理学院（国内平台化培训)

- **Type**: 在线培训平台
- **URL**: 主阵地为 app / 小程序内课程,无稳定可作 verified_primary 的 web 课程页;简单心理主站 jianshin.com、壹心理 xinli001.com 可作机构身份页
- **Maintainer**: 简单心理(简单心理 Uni)、壹心理(壹心理学院)
- **Cadence**: rolling(课程持续上新)
- **Last activity**: 持续运营(2025 在营)
- **Audience tier**: beginner / practitioner —— 入门科普到部分系统课程都有
- **One-liner**: 国内规模最大的两个平台化心理培训入口 —— 把流派课程、伦理课、督导资源、继续教育做成可购买的在线产品,降低了入门门槛 (evidence: 国内平台生态常识 — manifest URL gap, 见下)
- **典型内容**: 各流派入门到进阶课程、伦理与危机干预课、面向准从业者的系统培养项目、督导服务对接。质量参差 —— 既有正规师资的系统课,也有偏科普 / 偏营销的内容,需甄别。
- **投入产出比**: medium —— 作「了解国内培训市场长什么样 + 入门课程」有价值;但平台课程**不等同于**注册系统认可的受训时数,不能替代连续培训 + 督导 + 个人体验的正规路径 (evidence: 见下 manifest gap 说明)
- **Paywall**: 课程收费
- **可信度**: medium(平台本身正规;单个课程质量需逐一甄别 —— 这点要写进 SKILL.md)
- **Decay risk**: medium(平台商业模式 + 课程更替)
- **manifest gap 说明**: 课程内容在 app/小程序内,无稳定可引用 web URL。诚实标注:**国内平台培训在 manifest 中缺可引用一手 URL**。
- **正规性**: ⚠️ 部分正规 —— 平台是正规商业实体,但「买了平台课 = 完成正规受训」是误解;判断单个项目是否正规,仍看有无学会背书 / 结构化时数 / 督导与个人体验。

## 5. 社区 — 5

> 心理治疗的「社区」与 AI / 软件行业不同 —— 没有活跃的 Discord/Slack 主流圈,真实的同行连接发生在**专业学会(会员通讯 + 年会)**、**督导小组(私密、不公开)**、**机构平台的从业者后台**。下面列的是「资深从业者实际所在」的连接渠道,而非公开论坛。

### 👥 1. APA Division 12 / Division 29 会员生态（学会作为社区）

- **Type**: community（专业学会会员生态）
- **Platform**: 学会官网 + 会员通讯 + 年会 + listserv
- **URL**: https://www.div12.org/ ; https://societyforpsychotherapy.org/
- **规模**: 学会级(数千会员量级)
- **Audience tier**: practitioner / senior
- **One-liner**: 北美临床心理学者的「圈子」事实上由分会承载 —— 会员通讯、年会、邮件组是同行连接与共识形成的真实场所,Division 29 的网刊还提供短文形态的过程派内容 (evidence: [T05-S002, T05-S018])
- **典型内容**: 会员通讯(行业动态 / 政策 / 招聘)、年会、专业兴趣组、Division 29 的 societyforpsychotherapy.org 网刊短文。
- **投入产出比**: medium(对北美从业者是 ambient 行业连接;非北美从业者价值递减) (evidence: [T05-S018])
- **可信度**: high
- **Decay risk**: low(机构级)
- **locale**: 北美。

### 👥 2. 中国心理学会注册系统 — 注册督导师 / 注册机构网络（国内）

- **Type**: community（注册体系承载的从业者网络）
- **Platform**: 注册系统名录 + 注册机构 + 区域督导小组
- **URL**: http://www.chinacpb.org/（访问不稳定)
- **规模**: 注册心理师 / 督导师 + 注册机构网络(国内行业核心圈)
- **Audience tier**: practitioner / senior
- **One-liner**: 国内最接近「行业正规圈子」的连接 —— 注册系统的督导师名录、注册机构、由此延伸的督导小组,是国内从业者找正规督导、确认同行资质的入口 (evidence: [T05-S008])
- **典型内容**: 注册督导师名录、注册机构、伦理工作组、区域性继续教育与年会。
- **投入产出比**: medium-high(国内 locale 的核心同行网络锚点) (evidence: [T05-S008])
- **可信度**: high(行业自律组织;非政府牌照,这点要写明)
- **Decay risk**: medium(网站工程稳定性差;体系本身稳定)
- **locale**: 中国大陆。

### 👥 3. 督导小组 / 同辈督导（私密 — 行业真实连接形态）

- **Type**: community（线下/线上小组,非公开)
- **Platform**: 私密小组(微信群 / Zoom / 线下),不对外
- **URL**: 无(性质决定不公开)—— manifest `manifest:none`,此处不列入 manifest,仅作行业结构说明
- **规模**: 小(典型 3-8 人/组)
- **Audience tier**: practitioner / senior
- **One-liner**: 心理治疗行业**最实质的同行连接发生在督导小组**,而非公开社区 —— 个案讨论、反移情处理、伦理两难的同辈支持都在这里,但它按设计就是封闭的 (evidence: intake.json 子领域「督导与个人成长」)
- **典型内容**: 个案呈报与讨论、同辈督导、反移情与替代性创伤的相互支持。
- **投入产出比**: high(对在职从业者是不可替代的成长与支持渠道) —— 但**无法作为「可订阅 source」推荐**,SKILL.md 应说明「这是行业结构,不是一个你能去关注的账号」
- **可信度**: n/a(非公开信息源)
- **Decay risk**: n/a
- **说明**: 列出是为了让 SKILL.md 的「社区」图景诚实 —— 不能因为它不公开就假装行业没有社区。

### 👥 4. r/therapists 等从业者线上社区（公开,质量参差）

- **Type**: community（公开论坛)
- **Platform**: Reddit（r/therapists / r/psychotherapy 等）
- **URL**: https://www.reddit.com/r/therapists/
- **规模**: 数十万订阅级(英文从业者公开社区中规模较大者)
- **Audience tier**: mixed —— 受训者、新手、在职从业者混杂
- **One-liner**: 英文圈从业者公开吐槽 / 求助 / 讨论执业现实(收费、保险、耗竭、机构 vs 私执)的地方 —— 信号嘈杂但能看到行业「真实职业图景」的一面 (evidence: community_consensus)
- **典型内容**: 执业经营问题、职业耗竭、伦理求助、行业政策吐槽、新手提问。
- **投入产出比**: low —— 作 ambient「行业情绪 / 职业现实」观察有价值;**不能作知识来源**(匿名 + 质量参差) (evidence: community_consensus)
- **可信度**: low(匿名公开论坛;Reddit 非黑名单,但内容不可作临床真伪依据)
- **Decay risk**: medium(与 Reddit 平台命运绑定)
- **locale**: 英文圈为主。
- **甄别提示**: 与国内公众号评论区 / 知乎类似 —— 看「行业氛围」可以,看「怎么做临床」不行。

### 👥 5. 国内从业者社区现状 — 结构性偏薄（诚实标注)

- **Type**: community（现状说明,非单一 source)
- **Platform**: 微信群(督导群 / 同行群)、机构平台从业者后台(简单心理 / 壹心理的咨询师社群)、知识星球
- **URL**: 主阵地为微信群(无公开 URL)+ 平台 app 内社群 —— 均无可引用一手 URL
- **规模**: 分散,无统一大型公开社区
- **Audience tier**: practitioner
- **One-liner**: 国内从业者的同行连接高度依赖微信群与机构平台后台,**没有一个公开、可被外部关注、可引用的中心化社区** —— 这是国内 locale 信息源结构性偏薄的直接体现 (evidence: 国内社区生态常识 — 见 Phase 2 接口)
- **投入产出比**: n/a(无法作为「可推荐 source」—— 你无法从外部「关注」一个微信督导群)
- **可信度**: n/a
- **Decay risk**: n/a
- **诚实标注**: 国内心理治疗从业者社区**没有可引用、可公开关注的中心化渠道**,真实连接在私密微信群与机构平台后台。SKILL.md「想跟最新动态 / 找同行」的国内指引只能落到:注册系统(S008)+ 正规连续培训项目的同期同学网络 + 机构平台从业者社群,不能假装有一个「国内的 r/therapists」。

---

## 总览（按 type 分组）

### 权威指南 / 机构 — 5 个
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| APA Division 12 循证治疗清单 | rolling | practitioner/senior | high | 「障碍 × 流派」查表,流派之争降维成可查证据等级 |
| Cochrane Library | rolling | senior | medium | 心理治疗疗效证据的「最高法院」,系统综述金标准 |
| NICE Guidelines | 数年 review | practitioner/mixed | high | 把证据翻成 stepped-care 可执行路径 |
| APA 伦理守则 + Practice | 数年一修 | practitioner/mixed | high | 北美伦理 ground truth — 保密/知情同意/双重关系 |
| 中国心理学会注册系统 | 数年一修 | practitioner | high | 2017 取消国家证后,国内最接近行业公认门槛的标准 |

### 期刊 — 5 个
| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Journal of Consulting and Clinical Psychology | monthly | APA | medium | 循证治疗 RCT 旗舰刊 |
| Psychotherapy (Div 29) | quarterly | APA Div 29 | medium-high | 治疗过程/关系/共同要素核心阵地 |
| Clinical Psychology Review | ~8/yr | Elsevier | high | 只发综述/元分析,证据地图入口 |
| Psychotherapy Research | ~8/yr | SPR | medium | 过程-结果研究专门刊,共同要素一脉 |
| 中国心理卫生杂志 / 心理学报临床向 | monthly | 中国心理(卫生)学会 | medium | 国内临床实证 + 本土化研究主要中文发表地 |

### Podcast — 5 个
| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Therapist Uncensored | biweekly | Marriott & Kelley | medium | 依恋 + 人际神经生物学取向的从业者长谈 |
| Very Bad Therapy | weekly/biweekly | Wiita & Fineman | high | 来访者讲糟糕治疗 + 治疗师复盘,从失败学习 |
| Shrink Rap Radio | rolling | David Van Nuys | medium | 2005 至今数百集访谈档案库,覆盖各流派 |
| Where Should We Begin? | season-based | Esther Perel | medium | 真实匿名伴侣会谈录音,过程观摩(love-coach 已覆盖人物) |
| Off the Couch / New Books in Psychoanalysis | rolling | 分析师轮值 | low-medium | 精神分析取向访谈,平衡列表偏 CBT 的倾向 |

### Conference — 1 个（非独立成节,合并在培训体系/学会内）
| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| ACBS World Conference | annual | 年度(2025/2026 持续) | ACT/RFT 国际年会,兼具培训与社区属性,在 S019 ACBS 生态内 |

> 说明:心理治疗行业的会议(APA Convention、各分会年会、ACBS 世界大会、各流派学会年会)主要嵌在「学会/培训体系」里,不构成独立的、像 AI 行业那样高 signal 的 conference 赛道。故不单列 conference 节,合并入培训体系(第 4 节)与社区(第 5 节)。

### Community — 5 个
| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| APA Div 12 / Div 29 会员生态 | 学会官网+通讯+年会 | 学会级 | 北美临床心理学者的圈子事实上由分会承载 |
| 中国心理学会注册系统网络 | 注册名录+机构+督导组 | 国内行业核心圈 | 国内最接近「正规圈子」的同行连接入口 |
| 督导小组 / 同辈督导 | 私密小组(不公开) | 小(3-8人/组) | 行业最实质的同行连接,但按设计封闭 |
| r/therapists 等 | Reddit | 数十万订阅级 | 英文圈从业者吐槽执业现实,信号嘈杂 |
| 国内从业者社区现状 | 微信群+平台后台 | 分散无中心 | 结构性偏薄,无可公开关注的中心化社区 |

### Dataset / Benchmark — N/A for this industry
心理治疗行业无 AI / 量化金融意义上的公开 dataset / benchmark。最接近的是评估量表(PHQ-9 / C-SSRS 等)与诊断系统(DSM-5-TR / ICD-11)—— 这些属 Track 02 tools,不在本 track 重复。

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」→ 进 master skill「Sources — 信息源」节 highlights

1. **APA Division 12 循证治疗清单**(evidence: [T05-S002])—— 跨多 track 引用的事实标准:接到不熟悉的障碍/流派时的第一查询点。临床「证据等级」类 claim 的根。
2. **Cochrane + NICE 指南**(evidence: [T05-S003, T05-S004])—— 「这个疗法证据有多硬 / 临床路径怎么走」的终审参考。建议在 master skill 中作为一组(循证裁判席)呈现。
3. **Very Bad Therapy(podcast 层 top)**(evidence: [T05-S015])—— podcast 层投入产出比唯一 high 的:从失败案例反推伦理与治疗联盟,从业者级高信号。
   → master skill「想跟最新动态 / 想理解行业」指引:权威知识去 1+2,行业氛围与失败教训去 3。

### 「这一行最近的话题热度」（候选信号）

`topic-heat: incomplete — sources listed but content not crawled`
本 track 未逐集 / 逐期爬取 episode / issue / 综述标题(时间盒约束)。从 source 性质可推断的长期热点(非「最近 3 个月」精确热度):创伤治疗(EMDR / IFS / 躯体取向)持续走高、共同要素 vs 特定技术之争、远程治疗的伦理、依恋科学的临床化、文化适配。**若 Phase 2 需要高置信度近期热度,需对 S014/S015/S011 等爬最近 10-15 条目。**

### 新 figures 发现（喂给 wave 2 Track 01）

- **Lori Gottlieb** —— 《也许你该找个人聊聊》作者(intake.json canon 已列其书),执业治疗师 + 大众科普高影响力,有 Dear Therapists podcast。intake key_figures 未列 → **figure 候选**(归类:大众科普 / 从业者真实声音)。
- **Bruce Wampold** —— 在期刊层(Psychotherapy Research / Psychotherapy)反复出现的「共同要素 / contextual model」代表人物,intake.json research_strategy_notes 的 Track 06 已点名 Wampold,但 key_figures 未列 → 确认 **figure 候选**,figures 与 academic track 应交叉。
- **Sue Marriott & Ann Kelley**(Therapist Uncensored host)、**David Van Nuys**(Shrink Rap Radio host)—— 作为「信息源运营者」是 figure 弱候选,优先级低于上两位,但可记入候选池。

### 新 tools 发现（喂给 wave 2 Track 02）

- 本 track 未发现 intake.json key_tools 之外的新工具 —— sources 反复指向的工具(PHQ-9 / C-SSRS / DSM-5-TR / ICD-11 / SimplePractice)均已在 intake key_tools_candidates 内。**无新增 tool 候选**,但确认了 Div 12 清单、APA 伦理守则、注册系统标准这三个「制度性 source」与 Track 02/03 的 tools/workflows 强耦合,Phase 2 应交叉引用。

### 国内 vs 海外信息源密度差（重要 — 喂给 Phase 2.8 诚实边界）

**信号强弱判定:海外强,国内结构性偏薄。**

- **海外**:权威指南(APA / Cochrane / NICE)、期刊(4 本一手 URL)、podcast(5 个活跃可引用官网)、培训(Beck / ACBS / EMDRIA / IFS 均有官网与结构化认证)—— manifest 中 `verified_primary` + `surrogate_primary` 充足,信号厚。
- **国内**:核心问题是**一手深度信息源缺可引用 URL**:
  - 中国心理学会注册系统官网(chinacpb.org)工程稳定性差,本次核验访问失败。
  - 曾奇峰 / 李松蔚 / KnowYourself / 武志红 主阵地是微信公众号(黑名单 URL,**未也不应进 manifest**)。
  - 简单心理 Uni / 壹心理学院课程在 app/小程序内,无稳定 web URL。
  - 中德 / 中挪 / 中美连续培训项目无统一官网。
  - 《中国心理卫生杂志》《心理学报》无可作 verified_primary 的独立官网,主流访问经知网(黑名单聚合站)。
  - 国内从业者社区无公开可关注的中心化渠道(在私密微信群 + 平台后台)。
- **诚实边界建议写法**:master skill 的「想跟最新动态」指引在国内 locale 部分必须明说 ——「国内一手深度信息源结构性偏薄:权威标准看中国心理学会注册系统(网站不稳定),正规受训看连续培训项目 + 注册系统名录,但**国内没有一个像 APA/Cochrane 那样可直接引用的中心化权威源,也没有可公开关注的从业者社区**;曾奇峰 / 李松蔚等的内容在公众号 —— 可作行业氛围与科普参考,**不可作临床真伪依据**,且需自行甄别科普流行说法 vs 临床共识」。

### 冷僻 / 信号薄弱自检

- newsletter < 3? —— **不适用/弱**:心理治疗行业无 Substack 式个人 newsletter 生态;最接近的「机构通讯」是 APA Monitor(S024)。本 track 未单列 newsletter 节,合理(行业特性,非调研缺陷)。
- podcast < 3? —— 否,retained 5 个。
- conference < 1? —— 边缘:仅 ACBS World Conference 一个明确年度会,且合并在培训体系内呈现(行业会议多嵌在学会里)。
- 有效 endorsement source < 50%? —— 否,权威机构层(APA/Cochrane/NICE/注册系统)自带机构背书,podcast 层均有 cross_source / community_consensus。
- **结论**:整体信号**不薄**(海外厚),但有两处需 Phase 2.8 诚实标注:① **newsletter 与 conference 赛道在本行业天然稀薄**(非缺陷,是行业结构);② **国内 locale 一手深度信息源结构性偏薄 + 无中心化权威源/公开社区**(这是真实 gap,必须写进诚实边界)。
