# Track 02 — Tools（工具地图）：心理咨询 / 心理治疗（临床实践者视角）

> Phase 1 wave 2 · Track 02。locale=`global`（中国大陆 vs 欧美持照体系差异极大，决策树根节点 = locale）。profile=`practitioner`，industry_type=`regulated_practitioner`。
>
> **重要范围说明**：本行业的「工具」不是 SaaS 选型那种工具。它分两类性质完全不同的东西：(A) **临床仪器** —— 测评量表、诊断系统、结构化风险评估、结果监测量表，这些是「临床方法论的物化」，选型逻辑是「信效度 + 临床定位 + 版权可得性」，不是「功能多少 / 价格」；(B) **执业基础设施** —— EHR / 远程平台 / 督导与继教体系 / 循证资源库，这些更接近常规工具选型，但**合规（HIPAA / 数据隐私）与伦理是硬约束**。远程治疗平台（BetterHelp / Talkspace）的商业模式与伦理争议在本文件中按硬规矩标注，不只写功能。
>
> Wave 1 输出（Track 04/05/06）在本 track 启动时尚未落盘 —— 本文件 seed 来自 `intake.json` 的 5 大类工具候选 + 临床领域常识校验。Phase 1.5 review 时若 wave 1 已完成，需回灌 canon / sources 中点名的工具做交叉验证。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://icd.who.int/en | verified_primary | 2026-05-14 | WHO | ICD-11 官方入口，诊断分类 ground truth |
| T02-S002 | https://www.psychiatry.org/psychiatrists/practice/dsm | surrogate_primary | 2026-05-14 | American Psychiatric Association | 行业协会 — DSM-5-TR 出版方官方页 |
| T02-S003 | https://www.apa.org/ethics/code | surrogate_primary | 2026-05-14 | American Psychological Association | 行业协会 — APA 伦理守则（含测评/记录条款） |
| T02-S004 | https://www.div12.org/treatments/ | surrogate_primary | 2026-05-14 | APA Division 12 (SCP) | 行业协会 — 研究支持的心理治疗清单 |
| T02-S005 | https://cssrs.columbia.edu/ | verified_primary | 2026-05-14 | Columbia University | C-SSRS 官方页（.edu）— 自杀风险结构化评估 |
| T02-S006 | https://www.phqscreeners.com/ | surrogate_primary | 2026-05-14 | Pfizer / PHQ developers | vendor docs — PHQ-9/GAD-7 官方授权与计分页 |
| T02-S007 | https://www.simplepractice.com/ | surrogate_primary | 2026-05-14 | SimplePractice LLC | vendor docs — 海外主流 EHR 执业管理平台 |
| T02-S008 | https://www.theranest.com/ | surrogate_primary | 2026-05-14 | TheraNest (Therapy Brands) | vendor docs — EHR，机构/团体执业取向 |
| T02-S009 | https://jane.app/ | surrogate_primary | 2026-05-14 | Jane Software Inc. | vendor docs — 加拿大起家的多专科 EHR |
| T02-S010 | https://www.betterhelp.com/ | surrogate_primary | 2026-05-14 | BetterHelp (Teladoc) | vendor docs — 远程治疗平台，商业模式有争议 |
| T02-S011 | https://www.talkspace.com/ | surrogate_primary | 2026-05-14 | Talkspace Inc. | vendor docs — 上市远程治疗平台，争议样本 |
| T02-S012 | https://www.zoom.com/en/industry/healthcare/ | surrogate_primary | 2026-05-14 | Zoom Video Communications | vendor docs — Zoom for Healthcare 合规视频 |
| T02-S013 | https://www.cochranelibrary.com/ | surrogate_primary | 2026-05-14 | Cochrane | vendor docs — 系统综述循证资源库 |
| T02-S014 | https://www.nice.org.uk/guidance | surrogate_primary | 2026-05-14 | NICE (UK, gov) | 英国国家级临床指南，强监管 ground truth |
| T02-S015 | https://www.scottdmiller.com/ | surrogate_primary | 2026-05-14 | Scott D. Miller / ICCE | vendor docs — ORS/SRS 与 FIT（反馈知情治疗）来源 |
| T02-S016 | https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-mental-health-information-facebook-others | verified_primary | 2026-05-14 | US FTC (gov) | 监管文件 — FTC 对 BetterHelp 数据共享的执法令 |
| T02-S017 | https://www.psychiatry.org/psychiatrists/practice/dsm/frequently-asked-questions | surrogate_primary | 2026-05-14 | American Psychiatric Association | 行业协会 — DSM 与 ICD 关系/差异官方 FAQ |
| T02-S018 | https://www.bacp.co.uk/about-therapy/ | surrogate_primary | 2026-05-14 | BACP (UK) | 行业协会 — 英国咨询行业注册与执业框架 |
| T02-S019 | https://www.theravive.com/ | secondary | 2026-05-14 | Theravive | 第三方治疗师目录/转介平台，行业生态参考 |
| T02-S020 | https://www.apaservices.org/practice/ce | surrogate_primary | 2026-05-14 | APA Services | 行业协会 — 美国 CE credits 继续教育要求 |
| T02-S021 | https://en.wikipedia.org/wiki/Minnesota_Multiphasic_Personality_Inventory | secondary | 2026-05-14 | — | MMPI 背景、版本与版权状况入门 |
| T02-S022 | https://en.wikipedia.org/wiki/Symptom_Checklist-90 | secondary | 2026-05-14 | — | SCL-90 背景与计分入门 |
| T02-S023 | https://www.therapynotes.com/ | surrogate_primary | 2026-05-14 | TherapyNotes LLC | vendor docs — 美国老牌 EHR，SimplePractice 主要替代 |
| T02-S024 | https://www.pearsonassessments.com/ | surrogate_primary | 2026-05-14 | Pearson (Pearson Clinical) | vendor docs — MMPI 等专有量表的出版/版权方 |
| T02-S025 | https://www.beckinstitute.org/ | surrogate_primary | 2026-05-14 | Beck Institute | 行业协会型机构 — BDI/BAI 与 CBT 资源源头 |
| T02-S026 | https://openpsychometrics.org/ | secondary | 2026-05-14 | Open-Source Psychometrics | 量表公有领域可得性参考（非临床用） |
| T02-S027 | https://www.doxy.me/ | surrogate_primary | 2026-05-14 | Doxy.me LLC | vendor docs — 专做 telehealth 的合规视频，Zoom 替代 |

> 黑名单核对：zh-CN（知乎 / 公众号 / 百度百科 / CSDN）、en（G2 / Capterra）均未进表。简单心理 / 壹心理 / KnowYourself / 武志红心理 等国内平台**无可引用的一手 vendor docs URL 进 manifest**（官网内容营销性质强、且非黑名单但权重低），在正文中按「行业生态描述」处理并明确标注信号薄弱，不强行挂 source_id。

## 总览（按 tier 分组）

### 必备（5 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| DSM-5-TR / ICD-11（诊断系统） | 两套并行的诊断语言与分类框架，是「沟通货币」不是「个案概念化」 | low | T02-S001, T02-S002, T02-S017 |
| PHQ-9 / GAD-7（筛查 + 疗效追踪） | 公有领域、超短、可重复施测的抑郁/焦虑测量，基层与私人执业默认 | low | T02-S006, T02-S014 |
| C-SSRS（自杀风险结构化评估） | 把「问没问到位」标准化的自杀风险分诊工具，危机硬边界配套 | low | T02-S005 |
| 结构化个案记录 / 知情同意模板（progress notes） | 法律与伦理要求的最小执业基础设施，非可选项 | low | T02-S003 |
| EHR 执业管理平台（locale 分叉：海外 SimplePractice 等 / 国内基本缺位） | 排期 + 病历 + 收费 + 合规的一体化后台 | medium | T02-S007, T02-S008, T02-S023 |

### 场景特化（7 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| ORS / SRS（反馈知情治疗 FIT） | 每次会谈测量同盟与进展，把「疗效」变成可见数据 | medium | T02-S015 |
| SCL-90 | 90 项多维症状自评，国内体检/机构入组筛查极常见，临床定位有争议 | medium | T02-S022 |
| BDI-II / BAI（贝克抑郁/焦虑量表） | 专有、信效度厚、研究与临床通用，但需付费授权 | low | T02-S025, T02-S024 |
| MMPI-2 / MMPI-3 | 重型、需专业资质解释的人格/精神病理评估，司法与鉴别诊断场景 | medium | T02-S021, T02-S024 |
| 合规远程治疗视频（Zoom for Healthcare / Doxy.me） | 满足 HIPAA/BAA 的一对一视频，远程执业的合规底座 | medium | T02-S012, T02-S027 |
| APA Division 12 清单 / Cochrane / NICE 指南（循证资源库） | 回答「这个问题该用哪种疗法」的证据查询入口 | low | T02-S004, T02-S013, T02-S014 |
| CE credits 体系（海外）/ 注册系统督导（国内）（继教与督导基础设施） | 维持执照/注册资格、保证持续胜任力的制度化工具 | low | T02-S020, T02-S018 |

### 新兴（2 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 远程治疗大平台（BetterHelp / Talkspace） | 把治疗规模化撮合的 marketplace，商业模式与伦理争议是其本质属性 | high | T02-S010, T02-S011, T02-S016 |
| AI 辅助记录 / 逐字稿转写工具（ambient scribe 类） | 自动生成 progress notes 的新一类工具，隐私与知情同意风险未定 | high | T02-S007, T02-S003 |

---

## 必备层（≥80% 从业者用 / 行业基础设施）

### 1. DSM-5-TR / ICD-11（诊断系统）

- **One-liner**: 两套并行的精神障碍诊断语言与分类框架 —— DSM-5-TR（美国精神医学会，临床细节多、北美主导）/ ICD-11（WHO，全球官方统计与医保编码基础）。它是从业者之间、与精神科/保险沟通的「货币」，**不是**个案概念化。 (evidence: [T02-S001, T02-S002])
- **Tier**: 必备
- **Maintainer / Owner**: American Psychiatric Association（DSM）/ World Health Organization（ICD），https://www.psychiatry.org/psychiatrists/practice/dsm 、 https://icd.who.int/en
- **License**: proprietary（DSM-5-TR 需购买，APA 版权）/ ICD-11 由 WHO 免费在线开放（浏览器版可免费查）
- **Maturity signals**:
  - DSM-5-TR 发布：2022-03（DSM-5 主版 2013，TR=text revision）；ICD-11 正式生效：2022-01-01 (last checked: 2026-05-14)
  - Activity: healthy —— 两者都是各自体系的现行版本，无替代品在视野内
- **两套体系的核心差异**（临床领域硬要求）:
  - **目的不同**：DSM 是临床诊断手册（症状清单 + 鉴别诊断 + 共病规则）；ICD 是全球疾病统计与编码系统（精神障碍只是其中一章）。北美保险报销/病历常要求 ICD 编码，但临床思考多用 DSM 语言。
  - **结构与门槛不同**：DSM 倾向更细的亚型与明确的症状计数阈值；ICD-11 在部分诊断上更看重「原型描述 + 临床判断」，并新增了如「复杂性 PTSD（CPTSD）」这类 DSM-5-TR 未单列的诊断 —— 这点对创伤治疗子领域影响很大。
  - **地域**：DSM 北美主导，ICD 全球（含中国大陆官方医疗系统使用 ICD）。(evidence: [T02-S017, T02-S001])
- **不适合 / 替代方案**: **诊断 ≠ 个案概念化**。诊断回答「这组症状叫什么、和精神科/保险怎么对话」；个案概念化回答「这个人为什么现在出现这些问题、关系与历史与情境如何组织成一个可工作的理解、治疗往哪走」。把诊断标签当成治疗计划是最常见的新手错误。诊断也不替代风险评估（见 C-SSRS）。
- **生产案例**: 几乎所有持照体系下的临床记录、保险报销、转介信都要求 DSM/ICD 诊断编码 —— APA 伦理守则与各州执照法规将「在胜任力范围内做诊断」作为执业前提 (evidence: [T02-S003])。
- **维护者背景** (sub_skill_link): DSM 体系与 Track 01 的 Aaron Beck（CBT，早期参与 DSM 相关工作的临床传统）、整体精神医学界关联；非单一人物拥有。
- **近期变化** (近 12 个月): 无版本级变化。DSM-5-TR 持续小幅文本订正；ICD-11 各国落地进度不一。
- **来源** (≥3):
  - [Primary] WHO ICD-11 官方入口: https://icd.who.int/en （collected: 2026-05-14）— T02-S001
  - [Surrogate-Primary] APA DSM 官方页: https://www.psychiatry.org/psychiatrists/practice/dsm — T02-S002
  - [Surrogate-Primary] APA「DSM 与 ICD 关系」FAQ: https://www.psychiatry.org/.../frequently-asked-questions — T02-S017
- **可信度**: high
- **Decay risk**: low（24+ 月稳定 < 20% —— 诊断系统改版周期以十年计；唯一注意点是各国 ICD-11 落地进度）

### 2. PHQ-9 / GAD-7（筛查 + 疗效追踪量表）

- **One-liner**: 两份各 ~7–9 题、2 分钟内完成的抑郁（PHQ-9）/ 焦虑（GAD-7）自评量表。**公有领域、免费、可无限重复施测** —— 是基层医疗、私人执业接案与疗效追踪的事实默认。 (evidence: [T02-S006, T02-S014])
- **Tier**: 必备
- **Maintainer / Owner**: 由 Pfizer 资助开发（Spitzer、Kroenke 等），现作为公共资源发布，https://www.phqscreeners.com/
- **License**: 公有领域 / 免费使用，无需授权付费即可临床与研究使用（PHQ 系列明确开放）—— 这是它压倒 BDI/BAI 成为基层默认的关键原因
- **Maturity signals**:
  - PHQ-9 发表：2001；GAD-7 发表：2006；二十余年大规模验证，被 NICE、各国基层指南纳入 (last checked: 2026-05-14)
  - Activity: healthy —— 信效度证据持续累积，无被取代迹象
- **用途 / 信效度 / 临床定位**:
  - **用途**：接案筛查（是否存在抑郁/焦虑及严重度分级）+ 疗效追踪（每隔几次会谈重测，看分数曲线）。PHQ-9 第 9 题直接问自杀意念，是危机分诊的触发点之一。
  - **信效度**：作为筛查工具，敏感度/特异度在多人群中稳健；分数切点（如 PHQ-9 的 5/10/15/20 对应轻/中/中重/重度）被广泛采用。
  - **临床定位**：是**筛查与监测工具，不是诊断工具** —— 高分提示「需要进一步评估」，不等于「确诊抑郁症」。诊断仍需结构化访谈 + 临床判断。
- **不适合 / 替代方案**: 不适合作为唯一诊断依据；不适合人格/精神病理的复杂评估（用 MMPI）；面向特定问题（如 PTSD、强迫）需换专用量表（PCL-5、Y-BOCS 等）。需要更厚研究证据基线时可用 BDI-II/BAI，但要付授权费。
- **生产案例**: NICE 抑郁指南将 PHQ-9 类工具纳入分级与监测流程 (evidence: [T02-S014])；FIT/测量为本的实践（measurement-based care）普遍以 PHQ-9/GAD-7 作为常规结果指标 (evidence: [T02-S015])。
- **维护者背景** (sub_skill_link): 无单一在世「关键人物」绑定；与 Track 01 无强关联。
- **近期变化** (近 12 个月): 无。工具本身已冻结，变化只在「被纳入更多指南/平台」。
- **来源** (≥3):
  - [Surrogate-Primary] PHQ Screeners 官方页（授权与计分）: https://www.phqscreeners.com/ — T02-S006
  - [Primary] NICE guidance（含抑郁筛查/监测建议）: https://www.nice.org.uk/guidance — T02-S014
  - [Surrogate-Primary] Scott D. Miller / FIT 资源（measurement-based care 语境）: https://www.scottdmiller.com/ — T02-S015
- **可信度**: high
- **Decay risk**: low（公有领域 + 已冻结 + 指南级采用，3+ 年稳定）

### 3. C-SSRS（哥伦比亚自杀严重程度评定量表）

- **One-liner**: 把「自杀风险问没问到位」标准化的结构化分诊工具 —— 用统一的措辞依次问意念、计划、行为，输出一致的风险分层。是危机干预硬边界的配套仪器。 (evidence: [T02-S005])
- **Tier**: 必备（危机评估场景对所有临床执业者都是必备能力，工具本身是该能力的标准化载体）
- **Maintainer / Owner**: Columbia University（Kelly Posner 等），https://cssrs.columbia.edu/
- **License**: 免费用于多数临床、研究与社区场景（需在官网登记/取得版本），非商业可得性高
- **Maturity signals**:
  - 发布并广泛部署于 2010s；被美国 FDA、SAMHSA、众多医院系统、学校系统采纳为标准筛查 (last checked: 2026-05-14)
  - Activity: healthy —— 官方维护多语言、多场景版本（社区、急诊、学校等）
- **用途 / 信效度 / 临床定位**:
  - **用途**：结构化自杀风险评估 —— 不是预测「会不会自杀」（没有工具能做到），而是确保临床访谈系统覆盖了关键维度，并给出可记录、可交接的风险分层。
  - **信效度**：作为风险分诊工具有良好的预测效度证据（相对其它自杀量表）；其价值更多在「标准化 + 可沟通 + 可记录」。
  - **临床定位**：危机干预流程的一环 —— C-SSRS 输出「中/高风险」后，触发的是**安全计划 + 立即转介 + 必要时危机热线/急诊**，工具本身不解决危机。
- **不适合 / 替代方案**: 不适合当成「做完就没责任」的免责清单 —— 风险是动态的，需反复评估。不替代临床判断与安全计划（Stanley-Brown 安全计划等）。不评估自伤（NSSI）以外的其它风险类型。
- **生产案例**: 美国大量医院、急诊、学校把 C-SSRS 作为入组/转诊必筛工具；危机干预 SOP 普遍以「问到位 → 分层 → 转介」为骨架 (evidence: [T02-S005])。
- **维护者背景** (sub_skill_link): Columbia 团队；与 Track 01 临床流派创立者无直接关联（危机评估是跨流派共用能力）。
- **近期变化** (近 12 个月): 无版本级变化；持续推广多场景版本。
- **来源** (≥3):
  - [Primary] C-SSRS 官方页（.edu）: https://cssrs.columbia.edu/ — T02-S005
  - [Surrogate-Primary] APA 伦理守则（危机/胜任力相关条款语境）: https://www.apa.org/ethics/code — T02-S003
  - [Primary] NICE guidance（自伤/自杀评估建议语境）: https://www.nice.org.uk/guidance — T02-S014
- **可信度**: high
- **Decay risk**: low（行业基础设施级，3+ 年稳定）

### 4. 结构化个案记录 / 知情同意模板（progress notes & informed consent）

- **One-liner**: 不是某个 SaaS，而是一类**法律与伦理强制要求的执业文档** —— 知情同意书、初始评估记录、每次会谈进展记录（progress notes）、风险评估与转介记录。是私人执业最小可行基础设施，非可选项。 (evidence: [T02-S003])
- **Tier**: 必备
- **Maintainer / Owner**: 无单一拥有者 —— 标准来自各执照管理机构、APA/BACP 伦理守则、HIPAA（美国）等；EHR 平台（SimplePractice / TherapyNotes 等）内置模板是常见载体
- **License**: 概念层无版权；具体模板有开源的、有 EHR 平台专有的、有协会发布的
- **Maturity signals**:
  - 记录管理作为伦理义务已制度化数十年；HIPAA（1996）确立美国隐私/记录标准 (last checked: 2026-05-14)
  - Activity: healthy —— 形式在演进（纸质 → EHR → 模板化），要求本身稳定
- **为什么是必备而非可选**:
  - **法律责任**：记录缺失/不规范在执照投诉、医疗事故诉讼中是直接软肋；「没写 = 没做」是法律默认。
  - **伦理义务**：APA 伦理守则明确要求维护、保管、适时销毁记录，并就保密及其例外做知情同意。
  - **临床功能**：结构化记录本身支撑个案概念化的连续性与可督导性。
- **不适合 / 替代方案**: 「凭记忆做咨询、不留记录」在任何持照体系下都是高危执业。过度记录（写入不必要的敏感细节）也是风险 —— 记录要「足够支撑临床与法律，但不留多余」。
- **生产案例**: 所有持照执业的标配；EHR 平台的核心卖点之一就是合规模板（见 SimplePractice / TherapyNotes 卡片）(evidence: [T02-S007, T02-S023])。
- **维护者背景** (sub_skill_link): 与 Track 01 无人物关联；属伦理/法律基础设施。
- **近期变化** (近 12 个月): AI ambient scribe 类工具（见新兴层）正在改变「记录怎么生成」，但**也带来新的知情同意与隐私问题** —— 这是当前活跃争议点。
- **来源** (≥3):
  - [Surrogate-Primary] APA 伦理守则（记录/保密/知情同意条款）: https://www.apa.org/ethics/code — T02-S003
  - [Surrogate-Primary] SimplePractice（合规文档模板作为产品核心）: https://www.simplepractice.com/ — T02-S007
  - [Surrogate-Primary] BACP 执业框架（英国记录/伦理语境）: https://www.bacp.co.uk/about-therapy/ — T02-S018
- **可信度**: high
- **Decay risk**: low（义务本身稳定）/ 注意：「生成方式」decay risk medium（AI scribe 冲击）

### 5. EHR 执业管理平台（海外：SimplePractice / TherapyNotes / TheraNest / Jane —— 国内基本缺位）

- **One-liner**: 把排期 + 电子病历 + 收费/保险 + 合规文档 + 客户端门户/远程视频整合在一个后台的执业管理系统。海外私人执业的事实默认；**国内无对等成熟产品**，这是 locale 分叉的关键节点。 (evidence: [T02-S007, T02-S023, T02-S008])
- **Tier**: 必备（海外 locale）/ 在国内 locale 降级为「场景特化甚至缺位」—— 见决策树
- **Maintainer / Owner**: SimplePractice LLC / TherapyNotes LLC / TheraNest（Therapy Brands 旗下）/ Jane Software Inc.
- **License**: proprietary，全部为订阅制 SaaS
- **Maturity signals**:
  - SimplePractice、TherapyNotes 均为 2010 年代起的成熟产品，行业渗透率高；Jane 由加拿大多专科诊所场景起家；TheraNest 偏机构/团体执业 (last checked: 2026-05-14)
  - Activity: healthy —— 均在持续迭代远程医疗、保险计费、AI 记录等模块
- **典型使用场景**（针对差异化选型）:
  - **SimplePractice**：单人/小型私人执业，看重 UI 顺手、客户端门户体验、内置合规模板与远程视频 —— 北美个人执业最常被默认推荐的一个。
  - **TherapyNotes**：同样面向私人执业，老牌、记录/计费功能扎实，常作为 SimplePractice 的主要平替（价格/计费偏好不同的人会选它）。
  - **TheraNest**：多治疗师机构、团体执业、需要更强的多用户管理与机构级报表时。
  - **Jane**：诊所内有多种专科（心理治疗 + 物理治疗等混合）、需要一个跨专科后台时。
- **不适合 / 替代方案**: 受训阶段/极小量个案时，完整 EHR 可能「太重」，可先用合规模板 + 合规视频 + 简单排期。**中国大陆 locale 几乎不适用** —— 数据本地化合规、支付与医保结构、行业形态都不同，海外 EHR 不能照搬；国内目前更多是「平台自带的咨询师后台（简单心理/壹心理等）+ 自行用通用工具拼凑」，没有对标产品（这是行业信号薄弱点，需诚实标注）。
- **生产案例**: 海外私人执业者把 EHR 作为开业第一批基础设施之一 —— 平台官方与第三方治疗师社区普遍如此描述 (evidence: [T02-S007, T02-S023])。无法获取严格意义上的「独立 production case study」（治疗师执业属私密，不公开晒后台），可信度据此标 medium。
- **维护者背景** (sub_skill_link): 与 Track 01 无人物关联（纯执业基础设施供应商）。
- **近期变化** (近 12 个月): 各平台普遍加入 AI 辅助记录（ambient/scribe）、强化远程医疗与保险计费 —— AI 记录模块是当前竞争焦点，也是隐私争议来源（见新兴层）。
- **来源** (≥3):
  - [Surrogate-Primary] SimplePractice vendor docs: https://www.simplepractice.com/ — T02-S007
  - [Surrogate-Primary] TherapyNotes vendor docs: https://www.therapynotes.com/ — T02-S023
  - [Surrogate-Primary] TheraNest vendor docs: https://www.theranest.com/ — T02-S008
  - [Surrogate-Primary] Jane vendor docs: https://jane.app/ — T02-S009
- **可信度**: medium（vendor docs 为主，缺独立 production case；功能描述可信，渗透率描述需 Phase 1.5 用 wave 1 sources 交叉验证）
- **Decay risk**: medium（12–24 月内功能层显著变化概率 20–40%，主要是 AI 记录与保险模块；但「私人执业需要一个执业管理后台」这个需求本身 low decay）

## 场景特化层（特定子方向用）

### 6. ORS / SRS（结果评定量表 / 会谈评定量表 —— 反馈知情治疗 FIT）

- **One-liner**: 一对各 4 项、视觉模拟刻度的超短量表 —— ORS 每次会谈**开头**测来访者近况，SRS 每次会谈**结尾**测治疗同盟。把「治疗有没有效、关系好不好」变成会谈级可见数据，是反馈知情治疗（FIT / measurement-based care）的核心仪器。 (evidence: [T02-S015])
- **Tier**: 场景特化
- **Maintainer / Owner**: Scott D. Miller、Barry Duncan 等（International Center for Clinical Excellence / ICCE），https://www.scottdmiller.com/
- **License**: 个人执业者可免费取得授权使用（官网申请）；机构/规模化使用有付费许可。可得性总体高。
- **Maturity signals**:
  - ORS/SRS 自 2000 年代初发布，FIT 已积累元分析级证据（系统化反馈能改善结果、降低脱落与恶化率）(last checked: 2026-05-14)
  - Activity: healthy —— ICCE 持续培训与版本维护
- **典型使用场景**:
  - 想系统性降低**来访者脱落率 / 早期识别「正在恶化」的个案**时 —— FIT 的核心证据正是「让治疗师及时看到没有进展的个案并调整」。
  - 跨流派通用：不绑定 CBT 或动力学，任何取向都能叠加 FIT。
  - 督导/机构想要客观结果数据（而非只靠治疗师自评）时。
- **不适合 / 替代方案**: 不适合「填了不看」—— FIT 的效力来自治疗师真的根据反馈调整，机械施测无意义。对某些来访者（极度回避评估、特定文化背景）刻度量表的有效性下降。需要症状层细节时仍用 PHQ-9/GAD-7 等。
- **生产案例**: FIT 被多个机构系统采纳为常规结果监测；Scott Miller / ICCE 的培训与出版是主要传播渠道 (evidence: [T02-S015])。
- **维护者背景** (sub_skill_link): Scott D. Miller 是「共同要素 / 反馈知情」一脉的代表人物 —— 与 Track 01 的「整合取向 / 共同要素派」直接关联，候选 figure（若 Track 01 未 retained，提交重 walk）。
- **近期变化** (近 12 个月): 无工具级变化；measurement-based care 整体在保险与机构层面被更多推动。
- **来源** (≥3):
  - [Surrogate-Primary] Scott D. Miller / ICCE vendor docs: https://www.scottdmiller.com/ — T02-S015
  - [Surrogate-Primary] APA Division 12（measurement-based 实践语境）: https://www.div12.org/treatments/ — T02-S004
  - [Surrogate-Primary] APA 伦理守则（评估/胜任力语境）: https://www.apa.org/ethics/code — T02-S003
- **可信度**: high
- **Decay risk**: medium（工具本身 low，但「是否被纳入主流执业常规」仍在变动 —— 标 medium 反映采纳面的不确定性）

### 7. SCL-90（症状自评量表 90 项）

- **One-liner**: 90 个条目、9 个症状维度的多维自评量表。在中国大陆的体检、机构入组、学校心理筛查中极其常见 —— 但其临床定位（尤其作为「诊断/分维度解释」）在学界有争议。 (evidence: [T02-S022])
- **Tier**: 场景特化
- **Maintainer / Owner**: 原版 SCL-90 / SCL-90-R 由 Leonard Derogatis 开发（SCL-90-R 由 Pearson 等出版，专有）；中国大陆广泛流通的是早期版本/本土修订版
- **License**: 情况复杂 —— SCL-90-R 是专有量表（Pearson）；但中国大陆流通的版本长期以「准公有」方式被大量免费使用，版权与版本一致性较混乱（这是使用时的真实坑）
- **Maturity signals**:
  - 原量表 1970 年代；在中国大陆引入并普及数十年，是国内最被「过度使用」的量表之一 (last checked: 2026-05-14)
  - Activity: 工具本身冻结；学界对其使用方式的批评持续
- **典型使用场景**:
  - 国内机构/学校/EAP 的**大规模初筛**（一次性给一群人发，快速找出「需要关注」的个体）。
  - 作为「症状负荷的粗略概览」—— 适合「有没有问题、大致多重」，不适合精细鉴别。
- **不适合 / 替代方案**: **不适合当诊断工具，也不适合把 9 个因子分当成「确诊了 9 类问题」**—— 这是国内最普遍的误用。其因子结构的稳定性在多项研究中受质疑。需要针对性筛查时，PHQ-9/GAD-7 更短、信效度证据更清晰、可得性更干净。需要人格/精神病理深度评估时用 MMPI。
- **生产案例**: 国内高校新生心理普查、企业 EAP 入组筛查长期以 SCL-90 为默认工具 —— 属行业惯例（此为行业生态描述，缺乏可引用的一手公开 case，可信度据此 medium）。
- **维护者背景** (sub_skill_link): 无人物关联。
- **近期变化** (近 12 个月): 无；但「用 SCL-90 还是换更现代的工具」是国内从业讨论的常见话题。
- **来源** (≥3):
  - [Secondary] SCL-90 背景/计分入门: https://en.wikipedia.org/wiki/Symptom_Checklist-90 — T02-S022
  - [Surrogate-Primary] Pearson Clinical（SCL-90-R 专有出版方语境）: https://www.pearsonassessments.com/ — T02-S024
  - [Surrogate-Primary] APA 伦理守则（测评工具适用性/胜任力语境）: https://www.apa.org/ethics/code — T02-S003
- **可信度**: medium（国内使用现状描述基于行业惯例，非一手公开数据；学界争议是真实信号）
- **Decay risk**: medium（工具不变，但其「主流地位」在国内有被更现代工具替换的压力）

### 8. BDI-II / BAI（贝克抑郁量表 / 贝克焦虑量表）

- **One-liner**: Aaron Beck 团队开发的 21 项抑郁（BDI-II）/ 21 项焦虑（BAI）自评量表，信效度证据极厚、研究与临床通用 —— 代价是**专有、需付费授权**。 (evidence: [T02-S025, T02-S024])
- **Tier**: 场景特化
- **Maintainer / Owner**: Aaron Beck 等开发；版权与出版由 Pearson（Pearson Clinical）持有，https://www.pearsonassessments.com/ ；CBT 资源生态由 Beck Institute 承载
- **License**: proprietary —— 需向 Pearson 购买授权/计分材料，不能像 PHQ-9 那样随意复制使用
- **Maturity signals**:
  - BDI 初版 1961，BDI-II 1996，BAI 1988；数十年、上万篇研究使用，是抑郁/焦虑测量的「金标准参照系」之一 (last checked: 2026-05-14)
  - Activity: healthy（作为成熟商业量表稳定供应）
- **典型使用场景**:
  - **研究场景 / 需要与既有文献直接对标**时 —— 大量 RCT 用 BDI-II/BAI，要可比性就用它。
  - CBT 取向执业者、Beck Institute 训练体系内 —— 与 CBT 工作流天然贴合。
  - 需要比 PHQ-9 更细的症状刻画、且预算允许付授权费时。
- **不适合 / 替代方案**: 不适合「免费、想随便重测」的基层场景 —— 那是 PHQ-9/GAD-7 的位置。不适合无授权预算的个人执业者把它当日常工具。不替代诊断。
- **生产案例**: CBT 临床试验与 Beck Institute 培训体系中 BDI-II/BAI 是常规测量工具 (evidence: [T02-S025])。
- **维护者背景** (sub_skill_link): **直接关联 Track 01 的 Aaron Beck（CBT 创立人）与 Judith Beck（传承、Beck Institute）** —— 量表是 CBT 流派物化的一部分。
- **近期变化** (近 12 个月): 无量表级变化。
- **来源** (≥3):
  - [Surrogate-Primary] Beck Institute（BDI/BAI 与 CBT 资源源头）: https://www.beckinstitute.org/ — T02-S025
  - [Surrogate-Primary] Pearson Clinical（版权/出版方）: https://www.pearsonassessments.com/ — T02-S024
  - [Surrogate-Primary] APA Division 12（CBT 循证语境）: https://www.div12.org/treatments/ — T02-S004
- **可信度**: high
- **Decay risk**: low（成熟商业量表，3+ 年稳定）

### 9. MMPI-2 / MMPI-2-RF / MMPI-3（明尼苏达多项人格测验）

- **One-liner**: 数百题、需要专业资质才能施测与解释的人格与精神病理综合评估工具。是「重型仪器」—— 用于鉴别诊断、司法/职业评估、复杂个案，不是日常筛查。 (evidence: [T02-S021, T02-S024])
- **Tier**: 场景特化
- **Maintainer / Owner**: 由明尼苏达大学开发与持有版权；出版与发行由 Pearson（University of Minnesota Press / Pearson）负责
- **License**: proprietary —— 需购买，且**使用者资质受限**（多数地区要求心理学相关研究生级训练 + 测评资质才能施测/解释）
- **Maturity signals**:
  - MMPI 初版 1940s；MMPI-2（1989）、MMPI-2-RF（2008）、MMPI-3（2020）持续修订 (last checked: 2026-05-14)
  - Activity: healthy —— MMPI-3 是当前最新版本，仍在推广
- **典型使用场景**:
  - **鉴别诊断困难、需要客观人格/精神病理画像**的复杂个案。
  - **司法心理评估、职业（如高危岗位）评估、监护权评估**等需要带效度量表（检测装病/否认）的高利害场景 —— MMPI 内建的效度量表是其不可替代之处。
  - 一般只在临床心理学博士/有测评资质的从业者手里。
- **不适合 / 替代方案**: **绝对不适合无资质者使用**（伦理与法律红线）。不适合日常疗效追踪（太长、太贵、不可频繁重测）。不适合作为首选筛查。常规情绪筛查用 PHQ-9/GAD-7；人格层面的非高利害探索可用其它工具。
- **生产案例**: 司法鉴定、临床心理学评估实践中 MMPI 是标准工具之一 —— 属专业惯例（治疗师执业私密，无公开 case study 可引，可信度据此 medium-high）。
- **维护者背景** (sub_skill_link): 无与 Track 01 流派创立者的直接关联（MMPI 属测评心理学传统，非治疗流派）。
- **近期变化** (近 12 个月): MMPI-3（2020）持续替代旧版；从业者在 2-RF 与 3 之间的迁移仍在进行。
- **来源** (≥3):
  - [Secondary] MMPI 背景/版本/版权状况: https://en.wikipedia.org/wiki/Minnesota_Multiphasic_Personality_Inventory — T02-S021
  - [Surrogate-Primary] Pearson Clinical（出版/版权方）: https://www.pearsonassessments.com/ — T02-S024
  - [Surrogate-Primary] APA 伦理守则（测评资质/胜任力条款）: https://www.apa.org/ethics/code — T02-S003
- **可信度**: medium（使用现状基于专业惯例描述）
- **Decay risk**: medium（版本迁移 2-RF→3 仍在进行；工具范式本身 low decay）

### 10. 合规远程治疗视频（Zoom for Healthcare / Doxy.me 等）

- **One-liner**: 满足医疗隐私合规（美国 HIPAA / 可签 BAA 业务伙伴协议）的一对一视频会话工具 —— 是远程执业的合规底座。注意：这一类指**治疗师自己掌控的合规视频工具**，与 BetterHelp/Talkspace 那种「平台撮合 + 平台掌控关系」是两回事。 (evidence: [T02-S012, T02-S027])
- **Tier**: 场景特化
- **Maintainer / Owner**: Zoom Video Communications（Zoom for Healthcare）/ Doxy.me LLC（专做 telehealth）
- **License**: proprietary，订阅制；关键差异在是否提供并签署 BAA
- **Maturity signals**:
  - Zoom for Healthcare、Doxy.me 在 2020 年后远程医疗激增中成为主流；EHR 平台（SimplePractice 等）也内置了合规视频 (last checked: 2026-05-14)
  - Activity: healthy
- **典型使用场景**:
  - 私人执业者做远程会谈、且需要满足美国 HIPAA / 各地医疗数据合规时。
  - **Doxy.me**：专为 telehealth 设计、无需来访者装软件、轻量；适合「只要一个干净的合规视频房间」。
  - **Zoom for Healthcare**：已有 Zoom 生态、需要团体治疗/培训/督导等更复杂会议功能时。
  - **EHR 内置视频**：已经在用 SimplePractice/Jane 等，想把视频与排期/记录打通时，优先用内置的。
- **不适合 / 替代方案**: **普通消费版 Zoom / 微信视频 / FaceTime 不是合规工具** —— 在持照体系下用它们做治疗是合规风险。不适合替代「与来访者的关系归属」判断 —— 工具合规不等于执业合规。
- **生产案例**: 远程私人执业者普遍采用合规视频工具或 EHR 内置视频 —— vendor docs 与行业惯例如此（无公开 case study，可信度 medium）。
- **维护者背景** (sub_skill_link): 无人物关联。
- **近期变化** (近 12 个月): 美国新冠期 HIPAA 执法宽限已结束，合规要求回归常态 —— 这使「用不用真正合规的视频工具」重新变成硬要求。
- **来源** (≥3):
  - [Surrogate-Primary] Zoom for Healthcare vendor docs: https://www.zoom.com/en/industry/healthcare/ — T02-S012
  - [Surrogate-Primary] Doxy.me vendor docs: https://www.doxy.me/ — T02-S027
  - [Surrogate-Primary] SimplePractice（内置合规视频语境）: https://www.simplepractice.com/ — T02-S007
- **可信度**: medium
- **Decay risk**: medium（具体产品可能洗牌，但「远程执业需要合规视频」需求 low decay）

### 11. 循证治疗资源库（APA Division 12 清单 / Cochrane / NICE 指南）

- **One-liner**: 回答「来访者这个问题，证据上该考虑哪种疗法」的查询入口 —— APA Div 12 的「研究支持的心理治疗」清单按问题列出有证据的疗法；Cochrane 出系统综述；NICE 出英国国家级临床指南。是把「循证」落到接案决策的工具。 (evidence: [T02-S004, T02-S013, T02-S014])
- **Tier**: 场景特化
- **Maintainer / Owner**: APA Division 12（Society of Clinical Psychology）/ Cochrane / NICE（UK）
- **License**: APA Div 12 清单网站公开免费；Cochrane 摘要免费、全文部分付费；NICE 指南公开免费
- **Maturity signals**:
  - 三者都是制度化、长期维护的循证基础设施；NICE 指南定期更新，Cochrane 持续出新综述 (last checked: 2026-05-14)
  - Activity: healthy
- **典型使用场景**:
  - 接到不熟悉的问题类型（如特定焦虑障碍、PTSD、强迫），想快速知道「证据指向哪些疗法」时 —— 查 Div 12 清单。
  - 需要更深的证据强度判断、做转介或治疗计划论证时 —— 查 Cochrane 系统综述 / NICE 指南。
  - 督导、个案讨论、向来访者解释「为什么推荐这个方向」时的证据后盾。
- **不适合 / 替代方案**: **循证清单不替代个案概念化** —— 「这个问题有 X 疗法的证据」不等于「这个来访者就该用 X」（共病、文化、关系、来访者偏好都要进决策）。也不适合当成「不在清单上就无效」的排他工具 —— 证据形态因流派而异（动力学/人本的证据形态与 RCT 不同，不等于无效，这是本领域的核心分歧，见 intake warnings）。
- **生产案例**: APA、NICE 指南被各国临床实践、保险审核、培训项目广泛引用为循证基准 (evidence: [T02-S004, T02-S014])。
- **维护者背景** (sub_skill_link): APA Division 12 与「CBT/循证主义」一脉、Track 01 的 Beck/Linehan/Hayes 间接关联（他们的疗法多在 Div 12 清单上）。
- **近期变化** (近 12 个月): 指南持续小幅更新；无结构级变化。
- **来源** (≥3):
  - [Surrogate-Primary] APA Division 12 研究支持治疗清单: https://www.div12.org/treatments/ — T02-S004
  - [Surrogate-Primary] Cochrane Library: https://www.cochranelibrary.com/ — T02-S013
  - [Primary] NICE guidance（gov）: https://www.nice.org.uk/guidance — T02-S014
- **可信度**: high
- **Decay risk**: low（机构级循证基础设施，3+ 年稳定）

### 12. 继续教育与督导基础设施（海外 CE credits 体系 / 国内注册系统督导）

- **One-liner**: 不是软件，而是**维持执照/注册资格、保证持续胜任力的制度化工具** —— 海外 CE credits（继续教育学分，执照续期硬性要求）/ 国内中国心理学会临床与咨询心理学注册系统的督导师名录与继续教育要求。 (evidence: [T02-S020, T02-S018])
- **Tier**: 场景特化（但对「执业资格维持」这一目标是必备）
- **Maintainer / Owner**: 海外 —— APA / 各州执照管理委员会 / 各专业协会；国内 —— 中国心理学会临床与咨询心理学专业委员会（注册系统）
- **License**: 体系本身非「产品」；CE 课程、督导服务有付费市场
- **Maturity signals**:
  - 海外 CE credits 是持照体系数十年的制度化要求；国内注册系统自 2000 年代后期建立，是 2017 年人社部取消「心理咨询师」国家职业资格后，行业内相对可信的专业身份锚点之一 (last checked: 2026-05-14)
  - Activity: healthy（注册系统持续运行；CE 体系稳定）
- **典型使用场景**:
  - **海外**：持照者每个续期周期必须修满规定 CE 学分（含伦理学分），否则执照失效 —— CE 追踪是执业刚需。
  - **国内**：注册系统的注册心理师/督导师身份、其继续教育与督导时数要求，是「在认证混乱市场里证明专业性」的主要路径之一。督导师名录是找合格督导的可信入口。
  - 找督导、规划职业成长路径、向来访者/机构证明资质时都依赖这套体系。
- **不适合 / 替代方案**: **不要把「修了 CE 学分 / 进了某名录」等同于「胜任某种治疗」** —— 学分是最低门槛不是能力证明。国内尤其要警惕：注册系统之外大量「山寨证书 / 21 天速成」培训（intake warnings 明确点名），CE/督导体系是用来对抗这种噪音的，但它本身也不是万能的胜任力保证。
- **生产案例**: 美国各州执照续期普遍要求 CE 学分 (evidence: [T02-S020])；英国 BACP 等协会有持续专业发展（CPD）要求 (evidence: [T02-S018])；国内注册系统督导师名录是行业找督导的常用入口（行业惯例描述）。
- **维护者背景** (sub_skill_link): 与 Track 01 无单一人物关联；属行业制度基础设施。Track 05（sources）会更深入处理注册系统标准/伦理守则。
- **近期变化** (近 12 个月): 国内行业在「2017 取消国家职业资格」后的认证格局仍在演化，注册系统的相对权重值得 Phase 1.5 用 wave 1 sources 复核。
- **来源** (≥3):
  - [Surrogate-Primary] APA Services CE 继续教育: https://www.apaservices.org/practice/ce — T02-S020
  - [Surrogate-Primary] BACP 执业/CPD 框架: https://www.bacp.co.uk/about-therapy/ — T02-S018
  - [Surrogate-Primary] APA 伦理守则（胜任力维持条款）: https://www.apa.org/ethics/code — T02-S003
- **可信度**: medium（海外 high，国内注册系统现状描述需 wave 1 交叉验证）
- **Decay risk**: low（制度框架稳定）/ 国内 locale 标 medium（认证格局仍在演化）

## 新兴 / 实验阶段（近 12 个月起势 / 性质未定）

> 说明：本领域「新兴」不完全等于「刚发布」。BetterHelp/Talkspace 已存在多年，但作为「把治疗规模化为 marketplace」的形态，其商业模式、伦理与监管定位**仍在剧烈演化、远未稳定**，且近 12 个月仍有重大监管动作 —— 故归入新兴/性质未定层，并按硬规矩重点标注争议。AI ambient scribe 则是真正近期起势。

### 13. 远程治疗大平台（BetterHelp / Talkspace）—— 商业模式与伦理争议是其本质属性，不是附注

- **One-liner**: 把「找治疗师」做成 app 撮合的订阅制 marketplace —— 来访者按月付费、平台分配/匹配治疗师，主打可及性与低门槛。**它的商业模式、治疗师待遇、数据隐私争议是理解这个工具的核心，不是边角料。** (evidence: [T02-S010, T02-S011, T02-S016])
- **Tier**: 新兴 / 性质未定（形态与监管定位未稳定）
- **Maintainer / Owner**: BetterHelp（隶属 Teladoc Health）/ Talkspace（上市公司，Nasdaq: TALK），https://www.betterhelp.com/ 、 https://www.talkspace.com/
- **License**: proprietary，消费者订阅制平台
- **Maturity signals**:
  - 两者均为 2010 年代成立、规模巨大（数百万注册用户量级）；Talkspace 已上市 (last checked: 2026-05-14)
  - Activity: healthy（商业上活跃）—— 但「作为一种执业形态是否站得住」仍在被行业、监管、媒体持续质疑
- **典型使用场景（从业者视角）**:
  - 受训后期/早期执业者把它当**获客与积累小时数的渠道**之一（尤其在私人执业病人来源不稳定时）。
  - 想要灵活、远程、不自己处理排期收费的从业者。
  - —— 但务必带着下面的争议清单做决策，不要只看「能接到来访者」。
- **商业模式与伦理争议（硬规矩 · 必须完整标注）**:
  - **数据隐私 —— 已有监管定性**：2023 年美国 FTC 对 BetterHelp 作出执法令，指其在用户被告知信息会保密的情况下，将含心理健康相关信息的用户数据共享给 Facebook、Snapchat 等做广告，要求其退还 780 万美元并禁止此类数据共享 (evidence: [T02-S016])。这不是传言，是政府监管文件。Talkspace 等平台也长期面临数据使用透明度质疑。
  - **治疗师待遇 / 劳动模式争议**：平台普遍被批评治疗师按字数/按时长计酬偏低、缺乏稳定性、平台抽成与算法派单使治疗师议价能力弱 —— 行业内长期讨论「平台把治疗师当 gig 工人」。（此为行业广泛讨论的争议，本文件无可引用的一手 vendor 承认或独立审计 URL —— 标注为争议信号而非已证事实。）
  - **转介费 / 营销模式争议**：平台大量投放广告、与网红/播客做带链接推广（推广带来的注册可能涉及佣金结构），被批评「把心理健康当流量生意」、营销话术弱化了治疗的严肃性与适配性问题。
  - **匹配与连续性问题**：算法/快速匹配 vs 临床适配；来访者更换治疗师成本低也意味着治疗关系连续性弱 —— 与「治疗同盟是核心疗效因素」的临床共识存在张力。
  - **临床适配边界**：低门槛可及性是优点，但平台模式对**高风险/危机来访者、需要严肃诊断与连续治疗的个案**是否合适，是反复被质疑的点 —— 危机场景下平台的响应链条不等同于持照执业的危机流程。
- **不适合 / 替代方案**: 不适合作为「执业形态」的全部理解 —— 把它当成获客渠道之一可以，但从业者要清楚平台对治疗关系、数据、自己劳动权益的影响。需要完整掌控治疗关系/数据/合规的，走「自建私人执业 + EHR + 合规视频」路径（见必备/场景特化层）。
- **生产案例 / 监管案例**: FTC 对 BetterHelp 的执法令本身就是最硬的公开记录 (evidence: [T02-S016])。
- **维护者背景** (sub_skill_link): 与 Track 01 临床流派创立者无关联（纯商业平台）。
- **近期变化** (近 12 个月): 监管与公众审视持续加压；平台在隐私政策、AI 功能上持续调整 —— 正因为「还在被监管和舆论重塑」，归入性质未定层。
- **来源** (≥3):
  - [Verified-Primary] US FTC 对 BetterHelp 数据共享的执法令: https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-mental-health-information-facebook-others — T02-S016
  - [Surrogate-Primary] BetterHelp vendor docs: https://www.betterhelp.com/ — T02-S010
  - [Surrogate-Primary] Talkspace vendor docs: https://www.talkspace.com/ — T02-S011
- **可信度**: medium（数据隐私争议有政府文件背书 = high；治疗师待遇/转介费争议属行业广泛讨论但缺一手审计 = 标为争议信号）
- **Decay risk**: high（12 个月内监管/商业模式被显著改变概率 > 40% —— 这一类平台正处于监管重塑期）

### 14. AI 辅助记录 / 逐字稿转写工具（ambient scribe 类）

- **One-liner**: 在会谈中（或基于录音）自动生成 progress notes / 逐字稿的新一类工具，正被各大 EHR 平台内置或第三方独立提供。它解决「写记录耗时」的真实痛点 —— 但隐私、知情同意、临床准确性问题尚未有定论。 (evidence: [T02-S007, T02-S003])
- **Tier**: 新兴 / 实验阶段
- **Maintainer / Owner**: 多来源 —— SimplePractice 等 EHR 内置的 AI 记录模块 + 一批独立的 telehealth AI scribe 初创（生态分散，无单一主导者）
- **License**: proprietary，普遍订阅制或按用量计费
- **Maturity signals**:
  - 作为「医疗 ambient scribe」的一支，2023 年后随 LLM 能力快速起势；EHR 平台近 12 个月密集上线 AI 记录功能 (last checked: 2026-05-14)
  - Activity: 活跃但产品/合规形态快速变动
- **典型使用场景（实验性）**:
  - 个案量大、被记录工作拖累的从业者，想把「写 note」时间压下来。
  - 已在用支持 AI 记录的 EHR、愿意做早期采用者时。
- **不适合 / 替代方案 + 风险（明确标注）**:
  - **知情同意问题**：用 AI 处理会谈内容必须向来访者明确告知并取得同意 —— 这不是默认可做的事，是新增的伦理动作（与必备层「知情同意模板」直接耦合）。(evidence: [T02-S003])
  - **隐私 / 数据去向**：会谈内容是最敏感的健康信息，AI 工具的数据存储、是否用于训练、是否签 BAA，是采用前的硬尽调项。
  - **临床准确性**：自动生成的 note 可能漏掉/曲解临床关键信息（风险表述、细微的临床观察），治疗师对记录的最终责任不能外包给 AI。
  - **替代方案**：不确定时，沿用「治疗师亲手写的结构化记录」—— 慢，但责任与准确性清晰。
- **生产案例**: EHR 平台官方在主推 AI 记录功能 (evidence: [T02-S007])；但「独立、可追溯的临床效果/合规审计」尚不充分 —— 故标 experimental。
- **维护者背景** (sub_skill_link): 无人物关联。
- **近期变化** (近 12 个月): 这一整类工具就是近 12 个月的主要变化本身；功能、定价、合规姿态都在快速演化。
- **来源** (≥3):
  - [Surrogate-Primary] SimplePractice（AI 记录功能作为产品方向）: https://www.simplepractice.com/ — T02-S007
  - [Surrogate-Primary] APA 伦理守则（知情同意/记录/保密 —— AI 记录必须挂靠的伦理框架）: https://www.apa.org/ethics/code — T02-S003
  - [Surrogate-Primary] TherapyNotes（同样在做 AI 记录方向）: https://www.therapynotes.com/ — T02-S023
- **可信度**: medium-low（工具存在确凿，但临床/合规价值未定）
- **Decay risk**: high（12 个月内产品形态/合规要求显著变化概率 > 40% —— 新兴层默认 high，此处尤其成立）

> **stability: experimental** 适用于本层两个条目 —— 6–12 个月后 BetterHelp/Talkspace 的监管定位、AI scribe 的产品格局都可能与现在显著不同。

---

## 选型决策树

> **根节点 = locale**（intake 明确要求按 locale 分章 —— 中国大陆 vs 欧美持照体系差异极大，工具栈不能照搬）。共 9 个节点。
> 重要前提：本树是**工具选型**树，不是「该不该做治疗」的判断。所有分支都默认使用者是受训中/持照/注册的临床从业者；任何涉及危机的分支都导向「立即转介专业资源 / 危机热线」，工具不解决危机。

### 根节点：你的执业 locale 是？

```
你在哪个体系下执业 / 受训？
├── Branch A: 欧美持照体系（美国 LMFT/LCSW/LPC/临床心理学博士 / 英国 BACP/UKCP 等）
└── Branch B: 中国大陆（2017 年人社部取消「心理咨询师」国家职业资格后的格局）
```

---

### Branch A：欧美持照体系

#### Node A1：你的当前需求是「临床仪器」还是「执业基础设施」？
- → **临床仪器**（评估/筛查/监测）：进 Node A2
- → **执业基础设施**（排期/病历/收费/远程/继教）：进 Node A3

#### Node A2：临床仪器 —— 你要测什么？
- **接案筛查 + 日常疗效追踪（抑郁/焦虑）** → 默认 **PHQ-9 / GAD-7**（公有领域、免费、可频繁重测）。需要与既有 RCT 文献对标、且有授权预算 → 换 **BDI-II / BAI**。
- **每次会谈测同盟与进展、想降脱落/早期识别恶化** → **ORS / SRS（FIT）**，跨流派可叠加。
  - 真实选型逻辑：measurement-based care 的证据指向「系统化反馈本身有效」，所以这里选的是「会不会真的看反馈并调整」，工具只是载体。
- **自杀风险评估** → **C-SSRS**（结构化分诊）—— 但记住它触发的是安全计划 + 转介，不是终点。
- **复杂鉴别诊断 / 司法/职业等高利害评估** → **MMPI-2-RF / MMPI-3**，且**仅限有测评资质者**；无资质 → 不使用，转介有资质的同行。
- **「该用哪种疗法」的证据查询** → **APA Division 12 清单 / Cochrane / NICE 指南** —— 但循证清单不替代个案概念化。

#### Node A3：执业基础设施 —— 你处于哪个执业阶段？
- **受训中 / 个案量极小** → 不要急着上完整 EHR（太重）。先用「合规知情同意 + 结构化记录模板 + 合规视频 + 简单排期」。
- **独立私人执业、单人/小型** → 上一套 EHR。默认候选 **SimplePractice**（UI 顺手、客户端门户、内置合规模板与视频）；计价/计费偏好不同 → **TherapyNotes** 作主要平替。
- **多治疗师机构 / 团体执业** → **TheraNest**（多用户管理、机构报表）；诊所内混合多专科 → **Jane**。
- **需要远程会谈** → 用 EHR 内置合规视频；若 EHR 无内置或需独立工具 → **Doxy.me**（轻量专用）/ **Zoom for Healthcare**（已有 Zoom 生态/需团体功能）。**绝不用消费版 Zoom / 微信视频**。
- **维持执照资格** → 按州/协会要求追踪 **CE credits**（含伦理学分），这是刚需不是可选。

#### Node A4：考虑用 BetterHelp / Talkspace 等大平台获客？
- → **可以当获客渠道之一，但带着争议清单决策**：FTC 已就 BetterHelp 数据共享作出执法令（[T02-S016]）；治疗师待遇、转介费营销、关系连续性、危机适配都是已知问题。
- → **不推荐**把它当作执业形态的全部 —— 需要完整掌控治疗关系/数据/合规的，回到 Node A3 的自建路径。

---

### Branch B：中国大陆

#### Node B1：先认清工具栈的结构性差异
中国大陆 locale 下，**「执业基础设施」这一层基本缺位**：没有 SimplePractice 级别的本土对标 EHR；执业管理多依赖「平台自带的咨询师后台（简单心理 / 壹心理 / KnowYourself / 武志红心理等）+ 自行用通用工具拼凑排期收费」。海外 EHR 不能照搬（数据本地化合规、支付与医保结构、行业形态都不同）。→ 这是本树最需要**诚实标注信号薄弱**的节点。

#### Node B2：临床仪器 —— 国内可得性与海外不同
- **接案筛查 / 疗效追踪** → **PHQ-9 / GAD-7**（公有领域，国内同样可用，最干净的选择）。
- **机构/学校/EAP 大规模初筛** → 现实中默认仍是 **SCL-90**，但**明确知道它的局限**：不是诊断工具、9 因子分不能当「确诊 9 类问题」、版本与版权在国内较混乱。能换 → 优先 PHQ-9/GAD-7 这类更现代、可得性更干净的工具。
- **自杀风险评估** → **C-SSRS** 同样适用（结构化、有中文版本）；危机仍导向立即转介 + 本地危机热线。
- **BDI/BAI、MMPI** → 专有、需授权、MMPI 需资质 —— 国内同样受这些约束。
- **「该用哪种疗法」证据查询** → APA Div 12 / Cochrane / NICE 仍是可用的国际循证入口，但需注意**文化适配**（西方治疗理论的个人主义假设不能直接照搬国内来访者）。

#### Node B3：执业平台与转介来源 —— 你靠什么接案？
- **机构执业 / 平台执业** → 用所在平台（简单心理 / 壹心理等）自带的咨询师后台；接受其抽成与派单规则。
- **想独立 / 私人执业** → 国内缺一体化 EHR，需自行用通用工具（排期、收费、加密存储记录）拼凑，并**严格做合规与保密处理**（录音转写涉及知情同意与数据安全）。
- **远程会谈** → 选择有保密保障的视频工具；通用消费级工具的合规性弱，作为执业用途需谨慎。

#### Node B4：资质、督导与继续教育 —— 在认证混乱市场里锚定专业性
- → 2017 年后国家职业资格取消，市场上大量「山寨证书 / 21 天速成」是营销噪音（intake warnings 明确点名）。
- → 相对可信的专业身份锚点：**中国心理学会临床与咨询心理学注册系统**（注册心理师 / 督导师身份、其继续教育与督导时数要求、督导师名录是找合格督导的可信入口）。
- → 但记住：**进了名录 ≠ 胜任某种治疗** —— 注册体系是对抗市场噪音的工具，不是胜任力的终极证明。真实成长是数年受训 + 长期督导 + 个人体验。
- → 此节点的国内现状描述需 Phase 1.5 用 wave 1（Track 05 sources）交叉验证。

---

## 避坑清单

- ❌ **不要把诊断系统（DSM/ICD）当成个案概念化或治疗计划**：诊断回答「这组症状叫什么、和精神科/保险怎么对话」，个案概念化回答「这个人为什么现在这样、治疗往哪走」。把诊断标签当治疗计划是最普遍的新手错误。(evidence: [T02-S001, T02-S017])
- ❌ **不要把筛查量表（PHQ-9 / GAD-7 / SCL-90）当成诊断工具**：高分只提示「需要进一步评估」。尤其国内最普遍的误用 —— 把 SCL-90 的 9 个因子分当成「确诊了 9 类问题」，其因子结构稳定性本身在研究中受质疑。(evidence: [T02-S022, T02-S006])
- ❌ **不要把 C-SSRS 等风险评估工具当成「做完就免责」的清单**：没有任何工具能预测自杀；C-SSRS 的价值是「问到位 + 可记录 + 可交接」。它触发的是安全计划 + 立即转介 + 必要时危机热线/急诊 —— 风险是动态的，需反复评估。(evidence: [T02-S005])
- ❌ **不要用消费版 Zoom / 微信视频 / FaceTime 做远程治疗**：它们不是合规工具（无 BAA、无医疗级隐私保障）。在持照体系下用它们做治疗是直接的合规风险 —— 用 EHR 内置合规视频 / Doxy.me / Zoom for Healthcare。(evidence: [T02-S012, T02-S027])
- ❌ **不要把 BetterHelp / Talkspace 只当成「能接到来访者的渠道」来评估**：它的商业模式就是争议本身 —— FTC 已就 BetterHelp 把心理健康相关数据共享给广告平台作出执法令（退还 780 万美元 + 禁令）；治疗师按字数/时长低薪、转介费营销、算法派单、关系连续性弱、危机适配存疑都是已知问题。(evidence: [T02-S016, T02-S010])
- ❌ **不要把海外 EHR（SimplePractice 等）的选型逻辑照搬到中国大陆**：国内数据本地化合规、支付与医保结构、行业形态都不同，且无成熟本土对标产品。locale 是工具选型的根节点，不是细节。(evidence: [T02-S007])
- ❌ **不要把「修了 CE 学分 / 进了注册系统督导师名录」等同于「胜任某种治疗」**：学分和名录是最低门槛/身份锚点，不是能力证明。国内尤其要把注册系统当成对抗「21 天速成 / 山寨证书」噪音的工具，而不是胜任力的终极保证。(evidence: [T02-S020])
- ❌ **不要无测评资质就用 MMPI**（伦理与法律红线）：MMPI-2-RF/MMPI-3 的施测与解释多数地区要求研究生级训练 + 测评资质。无资质遇到需要它的个案 → 转介有资质的同行。(evidence: [T02-S021, T02-S024])
- ❌ **不要把循证清单（APA Div 12 / Cochrane / NICE）当成排他工具**：「不在清单上」不等于「无效」—— 动力学/人本取向的证据形态与 RCT 不同。清单回答「证据指向哪些选项」，不替代「这个来访者（含共病、文化、偏好）该用什么」的临床判断。(evidence: [T02-S004, T02-S014])
- ❌ **不要在未取得来访者明确知情同意的情况下用 AI scribe 处理会谈内容**：会谈内容是最敏感的健康信息；AI 记录是新增的伦理动作，不是默认可做的事。且治疗师对记录准确性的最终责任不能外包给 AI。(evidence: [T02-S003, T02-S007])

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **「工具 = 临床方法论的物化，不是 SaaS」**：测评量表、诊断系统、风险评估的选型逻辑是「信效度 + 临床定位 + 版权可得性 + 使用资质」，不是「功能/价格」。(出现于: T02-S001 / T02-S006 / T02-S005 / T02-S024)
- **「诊断 ≠ 个案概念化；筛查 ≠ 诊断；评估工具 ≠ 临床判断」**——「工具输出 ≠ 临床决策」是贯穿所有临床仪器的元原则。(出现于: T02-S001 / T02-S017 / T02-S022 / T02-S004)
- **「合规与伦理是工具选型的硬约束，不是加分项」**：远程视频要 BAA、记录要规范、AI 处理要知情同意、平台数据去向要尽调 —— 在持照体系下这些是准入条件。(出现于: T02-S003 / T02-S012 / T02-S016)
- **「公有领域 / 可得性是真实选型变量」**：PHQ-9（免费、可频繁重测）压倒 BDI-II（专有、需授权）成为基层默认，正是可得性决定的 —— 不是「哪个更准」单维度决定。(出现于: T02-S006 / T02-S024 / T02-S025)
- **「locale 决定工具栈，不是决定细节」**：执业基础设施层在中美之间几乎是「有 vs 基本没有」的差异 —— 不是同一套工具的本地化，是结构性不同。(出现于: T02-S007 / T02-S018 / intake warnings)

**显著的工具流派分裂**（候选 智识谱系条目）:
- **测量为本（measurement-based / 循证主义）派 vs 关系优先 / 过程取向派**：前者主张系统化测量同盟与结果（代表工具：ORS/SRS-FIT、PHQ-9、APA Div 12 清单；代表人物：Scott D. Miller，及与 Track 01 的 Beck/Linehan/Hayes 循证一脉关联），后者认为治疗的核心变量（治疗关系、过程、意义）难以也不应被量表化（与 Track 01 的精神动力学、人本-存在取向关联）。这不是「谁对」，是对「治疗中什么可被工具化」的根本分歧 —— 直接对应 intake warnings「流派之争没有干净答案」「共同要素 vs 具体技术」。
- **平台撮合 / 规模化派 vs 自主私人执业派**：BetterHelp/Talkspace 代表「把治疗做成可规模化 marketplace」；自建 EHR + 合规视频 + 自有转介代表「治疗师完整掌控关系、数据、合规」。分歧点是治疗关系与数据的归属、以及「可及性 vs 治疗严肃性/连续性」的取舍。
- **诊断分类之争（DSM vs ICD）**：与其说是工具竞争，不如说是两种诊断哲学（DSM 细颗粒症状计数 vs ICD-11 部分诊断的原型 + 临床判断）—— Phase 2 可作为「诊断语言不是中立的」心智模型候选。

**新兴工具信号**:
- 当前活跃 / 上升的新工具数：2（远程治疗大平台作为「未稳定形态」+ AI ambient scribe）。
- 出现 → 主流 速度估计：AI scribe 约 12–24 个月可能在 EHR 内成为标配（EHR 平台近 12 个月已密集上线），但「临床/合规是否被接受」可能更久；BetterHelp/Talkspace 的形态演化由监管节奏主导，不可预测。
- 共同信号：两个新兴条目的 decay risk 都是 high，且都与「隐私 / 知情同意 / 伦理」强耦合 —— 新兴工具在本领域的不确定性主要不是技术不确定性，是伦理与监管不确定性。

**冷僻 / 信号薄弱**:
- 必备层 5 个（≥3 ✅）；场景特化 7 个（≥5 ✅）；新兴 2 个（≥2 ✅）—— 三层门槛均达标。
- 但有几处**信号薄弱，需 Phase 2.8 诚实边界标注**：
  1. **本领域无「行业 survey / state-of-X report 显示采用率」类硬数据** —— 治疗师执业属私密，不公开晒工具栈，「≥80% 从业者用」类陈述是基于伦理守则要求 + vendor 描述 + 行业惯例推断，非实测采用率。
  2. **GitHub stars 这类成熟度信号在本领域几乎不适用** —— 工具是量表/诊断系统/专有 SaaS，没有开源社区指标；成熟度只能靠「发布年份 + 指南/监管采纳 + 版本维护」判断。
  3. **中国大陆 locale 的执业基础设施层证据最薄** —— 国内平台（简单心理/壹心理/KnowYourself/武志红心理/EAP）无可进 manifest 的一手 vendor docs，按行业生态描述处理；国内注册系统的相对权重需 wave 1（Track 05）交叉验证。
  4. **vendor docs 占 manifest 比例偏高**（27 条中约 17 条 surrogate_primary，多为 vendor docs / 行业协会）—— verified_primary 仅 4 条（WHO ICD、C-SSRS .edu、NICE gov、FTC gov）。Phase 2 提炼 mental model 时，vendor 一面之词的 claim 需 ≥2 source consensus，已在正文标注。
- **与其它 track 的待核对矛盾**：本 track 启动时 wave 1 未落盘 —— Track 04（canon）/05（sources）若点名了本文件未覆盖的工具（如某本 CBT 手册指定的特定工作表、某培训项目指定的量表），保留给 Phase 1.5 用户裁决。

---

> **调研边界声明**：本 track ~8min 时间盒内完成。candidates explored ≈ 20+（5 大类种子 + 各类内细分），retained 14（必备 5 / 场景特化 7 / 新兴 2）。manifest 27 条 source。决策树 9 节点。所有 maturity signal 带 `last checked: 2026-05-14`。wave 1 seed 未到位，本文件基于 intake 种子 + 临床领域常识校验，Phase 1.5 需用 wave 1 输出回灌交叉验证。
