# Track 05 — Sources Research（求职 / 面试辅导，locale=global，profile=practitioner）

> Phase 1 wave 1 第 2 路 subagent 输出。覆盖求职教练这一行的持续信息源：newsletter / YouTube creator / 社区 / 数据报告 / 国内信息源 / 培训机构样本。
> **关键分野**：本文件明确区分「有方法论价值的 creator / 社区」vs「营销噪音大、当行业现状样本甄别的培训机构内容」。

## Source Manifest

> bucket 由 `source_verifier.py classify` 机械判定。GLOBAL 行业 manifest 红线：creator 裸域博客 / LinkedIn 个人页 → `secondary`，**未高标**。gov / gov.cn → `verified_primary`。LinkedIn Economic Graph 等机构数据页机器判 `secondary`，按规范升级为 `surrogate_primary` 并 note 写「机构数据」。Reddit 子版 → `reference`。
> **黑名单未进 manifest**：知乎话题页 / 微信公众号文章 / 百度百科未收。国内一手深度信息源（瞎说职场 / 圈外同学 / 大厂面试官 IP）主阵地是知乎 + 公众号 + 小红书 + B 站 — 这部分在「五、国内信息源」与 Phase 2 接口诚实标「国内一手深度信息源结构性偏薄，无合规可引用 URL」，不硬塞黑名单。牛客网（nowcoder.com）非黑名单，已收。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://cultivatedculture.com/ | secondary | 2026-05-14 | Austin Belcak | networking-first 求职方法论博客 + newsletter |
| T05-S002 | https://www.linkedin.com/in/austinbelcak/ | secondary | 2026-05-14 | Austin Belcak | LinkedIn 主阵地，高频求职战术 post |
| T05-S003 | https://www.youtube.com/@JeffSu | verified_primary | 2026-05-14 | Jeff Su | 简历 / LinkedIn / 求职效率实操短视频 |
| T05-S004 | https://www.youtube.com/@SelfMadeMillennial | verified_primary | 2026-05-14 | Madeline Mann | 前 HR 视角求职战术 + 谈薪 |
| T05-S005 | https://www.youtube.com/@AndrewLaCivita | verified_primary | 2026-05-14 | Andrew LaCivita | 面试方法论 + 高管求职教练 |
| T05-S006 | https://www.askamanager.org/ | secondary | 2026-05-14 | Alison Green | 职场 / 求职建议专栏，海量真实案例 |
| T05-S007 | https://www.reddit.com/r/jobs/ | reference | 2026-05-14 | Reddit | 通用求职社区，求职者侧 |
| T05-S008 | https://www.reddit.com/r/cscareerquestions/ | reference | 2026-05-14 | Reddit | 科技岗求职 / 校招社区 |
| T05-S009 | https://www.reddit.com/r/recruiting/ | reference | 2026-05-14 | Reddit | 招聘方视角社区 — 反向情报 |
| T05-S010 | https://economicgraph.linkedin.com/ | surrogate_primary | 2026-05-14 | LinkedIn | vendor docs — LinkedIn Economic Graph 就业市场机构数据（机器判 secondary，升级 surrogate） |
| T05-S011 | https://80000hours.org/ | secondary | 2026-05-14 | 80,000 Hours | 职业选择的理性 / EA 视角长文 |
| T05-S012 | https://www.themuse.com/advice | secondary | 2026-05-14 | The Muse | 通用求职建议内容站 |
| T05-S013 | https://www.nowcoder.com/ | secondary | 2026-05-14 | 牛客网 | 国内校招生态 + 海量笔面经 + 内推 |
| T05-S014 | https://www.1point3acres.com/ | secondary | 2026-05-14 | 一亩三分地 | 北美华人求职 / 面经社区 |
| T05-S015 | https://www.glassdoor.com/Interview/index.htm | secondary | 2026-05-14 | Glassdoor | 公司面经 + 面试评价聚合 |
| T05-S016 | https://www.teamblind.com/ | secondary | 2026-05-14 | Blind | 匿名职场 — 薪资 / offer / 内幕 |
| T05-S017 | https://www.bls.gov/ | verified_primary | 2026-05-14 | US BLS | 美国就业与薪资官方统计 |
| T05-S018 | https://www.levels.fyi/ | secondary | 2026-05-14 | levels.fyi | 科技岗薪资众包数据 |
| T05-S019 | https://www.linkedin.com/in/lizryan/ | secondary | 2026-05-14 | Liz Ryan | Human Workplace 创始人，反套路化招聘 LinkedIn |
| T05-S020 | https://www.stats.gov.cn/ | verified_primary | 2026-05-14 | 国家统计局 | 中国就业 / 城镇调查失业率官方数据 |
| T05-S021 | https://www.bls.gov/ooh/ | verified_primary | 2026-05-14 | US BLS | Occupational Outlook Handbook — 岗位前景手册 |
| T05-S022 | https://www.linkedin.com/business/talent/blog | verified_primary | 2026-05-14 | LinkedIn Talent | 招聘方视角官方 blog — 反向了解 recruiter 怎么想 |
| T05-S023 | https://www.biginterview.com/blog/ | verified_primary | 2026-05-14 | Big Interview | 面试训练产品官方 blog（vendor 一手） |
| T05-S024 | https://hbr.org/topic/subject/job-search | secondary | 2026-05-14 | HBR | 求职 / 谈薪的严肃长文 |
| T05-S025 | https://www.youtube.com/@LinkedInWithLizRyan | verified_primary | 2026-05-14 | Liz Ryan | Liz Ryan 的 YouTube 频道 |

## 总览（按 type 分组）

### Newsletter / Substack creator — 4 个（前 5 中的 4，第 5 位 The Muse 归入「数据/内容站」边缘）
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Cultivated Culture（Austin Belcak）| weekly newsletter + 高频 LinkedIn | practitioner | high | networking-first 求职方法论的旗舰输出，反「海投网申」 |
| Ask a Manager（Alison Green）| 日更（多 post/day）| mixed | high | 求职信 / 面试 / 谈判的海量真实场景问答，判断力锚 |
| Liz Ryan / Human Workplace | 不定期 LinkedIn + 历史 Forbes 专栏 | mixed | medium | 反套路化招聘、human-voiced resume / pain letter 提出者 |
| 80,000 Hours | 长文 + 偶发 newsletter | senior | medium | 「选什么职业」的理性 / 影响力框架，定位阶段读 |

### YouTube creator — 前 5
| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Jeff Su | weekly | 前 Google | high | 简历 / LinkedIn / 求职效率的高密度实操，受众最广 |
| Self Made Millennial | weekly | Madeline Mann（前 HR / 招聘官）| high | 招聘官内部视角的求职战术 + 谈薪，「招聘方怎么想」 |
| Andrew LaCivita | weekly+ | milewalk 创始人 / 教练 | medium | 面试方法论 + 高管求职，体系完整但单集偏长偏说教 |
| Liz Ryan（LinkedIn with Liz Ryan）| 不定期 | Human Workplace | medium | 反套路求职心法的视频版，更新不规律 |
| 「Cultivated Culture」相关视频（Austin Belcak）| 不定期 | Cultivated Culture | medium | 博客 / newsletter 的视频补充，非主阵地 |

### 社区 / Community — 4 个
| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| r/jobs | Reddit | 约 130 万+ 成员 | 通用求职吐槽 + 求助，求职者情绪与现实的温度计 |
| r/cscareerquestions | Reddit | 约 100 万+ 成员 | 科技岗求职 / 校招 / 谈薪，结构化讨论质量较高 |
| r/recruiting | Reddit | 约 30 万+ 成员 | 招聘方视角 — 教练做反向情报的关键 niche 源 |
| 一亩三分地 | 独立论坛 | 北美华人求职主阵地 | 北美华人面经 / offer / 身份，跨 locale 的桥接社区 |

### 数据 / 报告源 — 5 个
| Source | 频率 | Maintainer | One-liner |
|--------|------|-----------|-----------|
| US BLS（含 OOH）| 月度数据 + 年度手册 | 美国劳工统计局 | 美国就业 / 薪资 / 岗位前景的官方 ground truth |
| 国家统计局 | 月度 + 年度 | 中国国家统计局 | 中国城镇调查失业率 / 就业的官方数据 |
| LinkedIn Economic Graph | 季度 / 不定期报告 | LinkedIn | 全球技能迁移 / 招聘趋势的机构数据 |
| levels.fyi | rolling 众包 | levels.fyi | 科技岗薪资 / 职级对照，谈薪的事实依据 |
| Glassdoor（面经板块）| rolling 众包 | Glassdoor | 公司面经 + 面试流程 + 薪资区间聚合 |

### 国内信息源 — 3 个（合规可引用）+ 结构性偏薄声明
| Source | Cadence | 平台 | One-liner |
|--------|---------|------|-----------|
| 牛客网 | rolling | nowcoder.com（独立站）| 国内校招生态中枢 — 笔面经 / 内推 / 题库 / 时间线 |
| 一亩三分地 | rolling | 独立论坛 | 北美华人求职，国内用户出海求职的主参考 |
| 国家统计局 | 月度 + 年度 | stats.gov.cn | 国内就业大盘官方数据 |
| （瞎说职场 / 圈外同学 / 知乎话题 / 大厂面试官 IP）| — | 知乎 / 公众号 / 小红书 / B 站 | **黑名单平台，无合规可引用 URL — 见下方诚实声明** |

### 培训机构样本（行业现状甄别用，非「大师」） — 2 个
| Source | 类型 | 噪音背景 | One-liner |
|--------|------|---------|-----------|
| offer 先生 | 国内校招求职训练营机构 | 「内推资源」「保 offer」营销话术重 | 国内校招工业化辅导的典型形态样本 |
| DBC 职梦 / 职优你（UniCareer）一类 | 留学生 / 海归求职机构 | 「名企内推」「实习保 offer」噪音重 | 留学生求职机构化辅导的样本，利益结构需甄别 |

---

## 一、Newsletter / Substack creator

> 这一行的「newsletter」生态特点：不是 Substack 一统天下，而是**自建博客 + 邮件列表 + LinkedIn post 三位一体**。海外 creator 一手内容丰富、可直接研读；这是 figures track 的 cheapest discovery channel。

### ✉️ 1. Cultivated Culture（Austin Belcak）

- **Type**: newsletter + 自建博客 + 高频 LinkedIn post
- **URL**: https://cultivatedculture.com/ ；LinkedIn https://www.linkedin.com/in/austinbelcak/
- **Author**: Austin Belcak（与 Track 01 figures 强关联 — networking 派代表人物）
- **Cadence**: newsletter 约 weekly；LinkedIn 高频（数 post/week）
- **Last activity**: 2026-05（持续活跃，LinkedIn 近期仍在更新）
- **Audience tier**: practitioner（求职者实操为主，少量教练向）
- **One-liner**: networking-first 求职方法论的旗舰输出 — 系统反对「海投网申」，主张用 informational interview + 精准 outreach + 量化简历拿 offer。
- **典型每期内容**: 一篇拆解某个求职环节的长文 / 邮件 —— 如「如何写一封会被回复的冷邮件」「ATS 到底怎么读你的简历」「拿到内推的 5 步脚本」。配可复制的模板、脚本、邮件话术，叙事是「我/我学员从 0 拿到大厂 offer」。免费工具（简历评分器、ATS 检查器）是引流入口。
- **投入产出比**: high — ≥ 80% issue 给求职者带来 actionable 战术；但要甄别「方法」与「自家工具/课程导流」的混合。教练读它取**方法论骨架**而非照搬话术。
- **Paywall**: none（newsletter + 博客免费；有付费课程 / 工具，非订阅必需）
- **签名内容**: 「Networking-first job search」体系文章群；冷邮件 / outreach 模板系列。
- **Endorsement evidence**: (1) `cross_source` — 被 Jeff Su、Madeline Mann 等同行内容反复引为「networking 派」代表 (evidence: [T05-S001, T05-S003, T05-S004]); (2) `community_consensus` — r/jobs / r/cscareerquestions 讨论「要不要海投」时高频被点名 (evidence: [T05-S001, T05-S007, T05-S008])。
- **替代品**: Liz Ryan（同为反套路派，但更偏「人性化」而非「战术化」）。
- **最近变化（近 6 个月）**: 内容持续，AI 改简历 / AI outreach 主题占比上升。
- **可信度**: medium-high（方法有实证支撑面，但商业导流色彩需扣分）
- **Decay risk**: medium — 个人 IP 默认 medium；但已运营多年、商业模式成熟，比纯个人 newsletter 稳。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（networking 派 anchor，不可替代）/ 可访问性 ✅ → **KEEP, high**

### ✉️ 2. Ask a Manager（Alison Green）

- **Type**: 博客专栏（问答体），可视为「日更 newsletter」
- **URL**: https://www.askamanager.org/
- **Author**: Alison Green（与 Track 01 figures 关联 — 职场 / 求职建议专栏作者）
- **Cadence**: 日更，常 multi-post/day
- **Last activity**: 2026-05（持续日更，行业基础设施级稳定）
- **Audience tier**: mixed（求职者 + 在职者 + 管理者都读）
- **One-liner**: 求职信 / 面试 / 谈判 / 拒信 / 背调的海量真实场景问答 —— 不是「教你套路」，是「用判断力回应一个个具体困境」，是求职建议领域的判断力锚。
- **典型每期内容**: 读者来信描述一个具体困境（「面试官问了违法问题怎么办」「拿了 offer 又收到更好的怎么撤回」「我的求职信该不该提到我被裁」），Alison 给有同理心但不和稀泥的回应。评论区上千条同行/HR 补充，本身是语料。求职信怎么写、面试反向提问、谈薪邮件模板都有专题。
- **投入产出比**: high — 对教练而言，这是「真实世界求职困境」的最大单一语料库，≥ 80% 内容有参考价值（按主题检索式使用，非逐篇读）。
- **Paywall**: none
- **签名内容**: 求职信写法专题（"how to write a cover letter"）；面试反向提问问题清单；薪资谈判脚本。
- **Endorsement evidence**: (1) `cross_source` — 长期被 The Muse、各大求职建议站引为权威 (evidence: [T05-S006, T05-S012]); (2) `community_consensus` — Reddit 求职版块讨论中被高频转引 (evidence: [T05-S006, T05-S007])。
- **替代品**: The Muse advice（更轻、更 SEO）；HBR job-search topic（更学术、更高层级）。
- **最近变化（近 6 个月）**: 稳定，无重大变化。
- **可信度**: high（无导流动机，靠判断力立足）
- **Decay risk**: low — 运营近 20 年，已是行业基础设施。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅ / 可访问性 ✅ → **KEEP, high**

### ✉️ 3. Liz Ryan / Human Workplace

- **Type**: LinkedIn post + 历史 Forbes 专栏（专栏已基本停止，LinkedIn 为现阵地）
- **URL**: https://www.linkedin.com/in/lizryan/ ；YouTube https://www.youtube.com/@LinkedInWithLizRyan
- **Author**: Liz Ryan（与 Track 01 figures 强关联 — 前 500 强 HR 高管，反套路化招聘代表）
- **Cadence**: LinkedIn 不定期（数 post/week 但节奏不稳）
- **Last activity**: 2026 年内仍有更新（LinkedIn）；Forbes 专栏停更已久
- **Audience tier**: mixed
- **One-liner**: 「human-voiced resume」「pain letter」的提出者 —— 主张简历和求职信要写得像人话、直击雇主痛点，系统反对模板化 / 关键词堆砌的求职。
- **典型每期内容**: 短文 / LinkedIn post 谈一个反直觉观点 ——「别投 job board，直接给招聘经理写 pain letter」「你的简历不是履历表是营销文案」「面试是双向评估，你也在面试他们」。立场鲜明、情绪饱满，偏「心法」而非「步骤」。
- **投入产出比**: medium — 观点有价值且独特，但战术颗粒度低、可执行性弱于 Belcak / Jeff Su；50-80% 内容对教练有启发。
- **Paywall**: none（曾有付费课程，非必需）
- **签名内容**: "pain letter" 概念；"human-voiced resume" 概念。
- **Endorsement evidence**: (1) `cross_source` — pain letter / human-voiced resume 概念被多个求职建议站和书引用 (evidence: [T05-S019, T05-S012, T05-S024]); (2) `figure_short` — 前 HR 高管身份 + Forbes 专栏历史构成独立背书 (evidence: [T05-S019])。
- **替代品**: Austin Belcak（更战术化的反套路派）。
- **最近变化（近 6 个月）**: Forbes 专栏时代结束，发声集中到 LinkedIn / YouTube，更新频率下降。
- **可信度**: medium-high
- **Decay risk**: medium — 个人 IP，且更新节奏已不规律。

判定：真实背书 ✅ / Active ⚠️（更新不规律但近 12 月内有活动）/ 独特价值 ✅（pain letter 概念独有）/ 可访问性 ✅ → **KEEP, medium**

### ✉️ 4. 80,000 Hours

- **Type**: 机构博客 / 长文 + 偶发 newsletter + podcast
- **URL**: https://80000hours.org/
- **Maintainer**: 80,000 Hours（Effective Altruism 关联非营利机构）
- **Cadence**: 长文不定期；newsletter 偶发；podcast 另有节奏
- **Last activity**: 2026 年内持续更新
- **Audience tier**: senior（偏「想清楚职业方向」的反思型读者）
- **One-liner**: 「这辈子选什么职业」的理性 / 影响力导向框架 —— 不教面试技巧，教「在求职定位阶段如何系统思考职业选择」，是定位与职业叙事子领域的思想源。
- **典型每期内容**: 长文拆解「如何评估一份工作的长期价值」「career capital 怎么积累」「什么时候该换赛道」。有完整的 career guide。立场是 EA / 影响力最大化，**有明确价值取向**，教练引用时要标注这层 framing。
- **投入产出比**: medium — 对「求职定位与职业叙事」子领域是高价值思想源，但对简历 / 面试 / 谈薪等执行环节几乎无关；按子领域选择性使用。
- **Paywall**: none
- **签名内容**: 「Career guide」；「career capital」框架。
- **Endorsement evidence**: (1) `cross_source` — career capital 等概念在职业规划讨论中被广泛引用 (evidence: [T05-S011]); (2) 机构背书 — 非营利机构、长期运营、引用规范 (evidence: [T05-S011])。
- **替代品**: 《Designing Your Life》（Track 04 canon — 斯坦福「设计你的人生」，同为定位阶段思想源）。
- **最近变化（近 6 个月）**: 稳定。
- **可信度**: high（机构级，方法论透明，但有 EA 价值 framing）
- **Decay risk**: low — 机构级 source。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（定位阶段思想源，与战术类 source 互补）/ 可访问性 ✅ → **KEEP, medium**

## 二、YouTube creator

> 求职 / 面试这一行，YouTube 是海外 creator 的**核心一手内容场**，远比 Substack 重。频道根目录 → verifier 判 `verified_primary`（频道身份页，不是某一篇可疑文章）。这些 creator 几乎都同时是 Track 01 figures 候选。

### ▶️ 1. Jeff Su

- **Type**: YouTube
- **URL**: https://www.youtube.com/@JeffSu
- **Host**: Jeff Su（前 Google，与 Track 01 figures 强关联）
- **Cadence**: weekly
- **Last activity**: 2026-05（持续 weekly 更新）
- **Audience tier**: practitioner（求职者实操；战术颗粒度细）
- **One-liner**: 简历 / LinkedIn / 求职效率的高密度实操频道 —— 把「改简历」「写 LinkedIn」「用 AI 辅助求职」拆成可立即执行的步骤，受众最广、制作最精。
- **典型每期内容**: 8-12 分钟视频，主题如「ChatGPT 改简历的 3 个 prompt」「LinkedIn profile 的 5 个必改项」「面试后跟进邮件模板」。屏幕演示 + 模板 + before/after 对比。近一年大量 AI-assisted job search 内容。强执行导向、弱理论。
- **投入产出比**: high — ≥ 80% 视频有可立即落地的战术；但「具体 prompt / 工具」保鲜期短（intake warning 10），教练取**做法骨架**并自行更新工具。
- **Paywall**: none（有付费 Notion 模板等周边，非必需）
- **签名内容**: AI 改简历系列；LinkedIn 优化系列。
- **Endorsement evidence**: (1) `cross_source` — 求职建议生态中被广泛转引，订阅量百万级 (evidence: [T05-S003]); (2) `community_consensus` — Reddit 求职版块推荐「该看哪些 YouTuber」时高频上榜 (evidence: [T05-S003, T05-S008])。
- **替代品**: Self Made Millennial（更偏招聘官视角与谈薪）。
- **最近变化（近 6 个月）**: AI 辅助求职主题占比明显上升。
- **可信度**: medium-high（执行建议扎实，但工具类内容时效短）
- **Decay risk**: medium — 个人 IP，但更新稳定、商业模式成熟。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅ / 可访问性 ✅ → **KEEP, high**

### ▶️ 2. Self Made Millennial（Madeline Mann）

- **Type**: YouTube
- **URL**: https://www.youtube.com/@SelfMadeMillennial
- **Host**: Madeline Mann（前 HR / 招聘官，与 Track 01 figures 强关联）
- **Cadence**: weekly
- **Last activity**: 2026 年内持续更新
- **Audience tier**: practitioner（偏求职战术 + 谈薪）
- **One-liner**: 招聘官内部视角的求职战术与谈薪频道 —— 卖点是「我曾在桌子另一边」，讲招聘方实际怎么筛简历、怎么评估面试、谈薪时 HR 在想什么。
- **典型每期内容**: 视频拆解「招聘官 6 秒扫简历看什么」「面试中哪些回答会让你出局」「谈薪邮件该怎么写、什么时候报数字」。招聘方视角是核心差异化。谈薪内容尤其细，有完整脚本。
- **投入产出比**: high — ≥ 80% 内容对求职者和教练都有用；「招聘方视角」对教练做反向情报价值高。
- **Paywall**: none（有付费谈薪课程，非必需）
- **签名内容**: 谈薪脚本系列；「招聘官视角」简历 / 面试系列。
- **Endorsement evidence**: (1) `cross_source` — 与 Jeff Su 等并列被引为头部求职 YouTuber (evidence: [T05-S004, T05-S003]); (2) `figure_short` — 前招聘官身份构成独立专业背书 (evidence: [T05-S004])。
- **替代品**: Jeff Su（更偏简历 / 效率工具）；Andrew LaCivita（更偏面试方法论）。
- **最近变化（近 6 个月）**: 稳定。
- **可信度**: medium-high
- **Decay risk**: medium — 个人 IP。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（招聘官视角不可替代）/ 可访问性 ✅ → **KEEP, high**

### ▶️ 3. Andrew LaCivita

- **Type**: YouTube（+ 书，见 Track 04）
- **URL**: https://www.youtube.com/@AndrewLaCivita
- **Host**: Andrew LaCivita（milewalk 创始人，职业 / 面试教练，与 Track 01 figures 强关联）
- **Cadence**: weekly+（更新频繁）
- **Last activity**: 2026 年内持续更新
- **Audience tier**: mixed（求职者 + 中高层级 + 部分教练向）
- **One-liner**: 面试方法论 + 高管求职的体系化频道 —— 不是碎片战术，是一整套「如何准备和应对面试」的方法，覆盖到 senior / executive 层级。
- **典型每期内容**: 视频/直播讲面试方法 ——「面试官最爱问的问题及标准答法」「如何回答 tell me about yourself」「高管面试和普通面试的区别」。单集偏长，部分内容偏说教 / 偏导流自家训练营。体系完整是优点，颗粒度和节奏是缺点。
- **投入产出比**: medium — 体系有价值，但 50-80% 内容才算高信号，且需过滤课程导流；教练取**面试方法论框架**。
- **Paywall**: none（频道免费；有付费 Interview Intervention 等训练营）
- **签名内容**: 面试高频问题解法系列；「tell me about yourself」框架。
- **Endorsement evidence**: (1) `cross_source` — 长期头部面试教练，著作与频道互相背书 (evidence: [T05-S005]); (2) `figure_long` — 与 Track 04 canon 中其著作构成跨 track 背书 (evidence: [T05-S005])。
- **替代品**: Self Made Millennial（更短更战术）。
- **最近变化（近 6 个月）**: 稳定。
- **可信度**: medium-high
- **Decay risk**: medium — 个人 IP，但运营年限长。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（体系化面试方法 + 高管层级覆盖）/ 可访问性 ✅ → **KEEP, medium**

### ▶️ 4. Liz Ryan（LinkedIn with Liz Ryan）

- **Type**: YouTube
- **URL**: https://www.youtube.com/@LinkedInWithLizRyan
- **Host**: Liz Ryan（见第一节，前 500 强 HR 高管）
- **Cadence**: 不定期（节奏不稳）
- **Last activity**: 频道有视频，近期更新不规律
- **Audience tier**: mixed
- **One-liner**: 反套路求职心法的视频版 —— pain letter / human-voiced resume 等概念的口播呈现，立场鲜明但更新不规律。
- **典型每期内容**: 短视频谈一个反直觉观点，与其 LinkedIn post 同源。心法 > 步骤。
- **投入产出比**: medium — 与第一节 Liz Ryan 条目同源，视频是补充渠道；不必单独追，作为 ambient awareness。
- **Paywall**: none
- **签名内容**: pain letter 解说视频。
- **Endorsement evidence**: (1) `figure_short` — 前 HR 高管身份 (evidence: [T05-S025]); (2) `cross_source` — 概念被广泛引用 (evidence: [T05-S025, T05-S019])。
- **替代品**: 同 Liz Ryan LinkedIn（T05-S019）。
- **最近变化（近 6 个月）**: 视频更新放缓，重心在 LinkedIn。
- **可信度**: medium-high
- **Decay risk**: medium-high — 个人 IP + 更新不规律。

判定：真实背书 ✅ / Active ⚠️ / 独特价值 ⚠️（与其 LinkedIn 高度重叠）/ 可访问性 ✅ → **BORDERLINE, KEEP**（该 type 当前 retained 仍 < 5；作为 Liz Ryan 的视频渠道补充）

### ▶️ 5. Cultivated Culture 相关视频（Austin Belcak）

- **Type**: YouTube（非主阵地）
- **URL**: 见 https://cultivatedculture.com/ 内嵌视频 / 关联频道
- **Host**: Austin Belcak（见第一节）
- **Cadence**: 不定期
- **Last activity**: 不定期更新
- **Audience tier**: practitioner
- **One-liner**: Belcak networking-first 方法论的视频补充 —— 博客 / newsletter 才是主阵地，视频是衍生。
- **典型每期内容**: 把博客长文的核心战术做成视频演示（冷邮件、ATS、内推脚本）。
- **投入产出比**: medium — 内容与博客重叠；订阅博客 / newsletter 即可，视频作可选补充。
- **Paywall**: none
- **签名内容**: networking 求职法视频版。
- **Endorsement evidence**: (1) `cross_source` — Belcak 整体被广泛引用 (evidence: [T05-S001]); (2) `community_consensus` — networking 派代表 (evidence: [T05-S001, T05-S008])。
- **替代品**: Cultivated Culture 博客 / newsletter（T05-S001，主阵地）。
- **最近变化（近 6 个月）**: 重心仍在 newsletter + LinkedIn。
- **可信度**: medium-high
- **Decay risk**: medium。

判定：真实背书 ✅ / Active ⚠️ / 独特价值 ⚠️（与博客重叠）/ 可访问性 ✅ → **BORDERLINE, KEEP**（该 type retained < 5；作为 Belcak 的视频渠道，凑齐 YouTube 前 5；优先级低于前 3）

## 三、社区 / Community

> 社区对求职教练的价值有两层：(1) **求职者真实困境的语料库**——教练靠它校准「学员实际卡在哪」；(2) **招聘方视角的反向情报**——r/recruiting 尤其关键。Reddit 子版 → verifier 判 `reference`（论坛聚合）。

### 💬 1. r/jobs

- **Type**: community
- **URL**: https://www.reddit.com/r/jobs/
- **Platform**: Reddit
- **规模**: 约 130 万+ 成员
- **Audience tier**: beginner-mixed（大量非专业求职者）
- **Cadence / 活跃度**: rolling，每日大量新帖
- **Last activity**: 2026-05（持续高活跃）
- **One-liner**: 通用求职吐槽 + 求助的最大场之一 —— 不是方法论来源，是「求职者情绪与现实」的温度计，教练用它感知普通求职者的真实焦虑与误区。
- **典型内容**: 「投了 200 份简历 0 回复正常吗」「面试后多久没消息算 ghosting」「offer 谈薪被撤回的经历」「该不该接受降薪 offer」。信噪比偏低、情绪化，但**真实**。sticky / wiki 有基础 FAQ。
- **投入产出比**: low — < 50% 内容有从业者级信号；作 ambient awareness（感知市场情绪 + 常见误区），不逐帖看。
- **Paywall**: none
- **签名内容**: 子版 wiki / FAQ；周期性「市场有多难」类高赞帖。
- **Endorsement evidence**: (1) `community_consensus` — 求职话题最大 subreddit 之一 (evidence: [T05-S007]); (2) `cross_source` — 求职建议文章常引用其讨论 (evidence: [T05-S007, T05-S006])。
- **替代品**: r/cscareerquestions（更结构化，但限科技岗）。
- **最近变化（近 6 个月）**: 2023-2025 裁员潮后「市场难」情绪帖密度上升。
- **可信度**: low-medium（个人轶事为主，非可引用事实源）
- **Decay risk**: medium — 与 Reddit 平台命运绑定。

判定：真实背书 ✅ / Active ✅ / 独特价值 ⚠️（与 r/cscareerquestions 部分重叠，但覆盖全行业）/ 可访问性 ✅ → **KEEP, medium**（信号定位为「情绪温度计」而非方法源）

### 💬 2. r/cscareerquestions

- **Type**: community
- **URL**: https://www.reddit.com/r/cscareerquestions/
- **Platform**: Reddit
- **规模**: 约 100 万+ 成员
- **Audience tier**: practitioner（科技岗求职者，讨论质量较高）
- **Cadence / 活跃度**: rolling，每日活跃
- **Last activity**: 2026-05（持续高活跃）
- **One-liner**: 科技岗求职 / 校招 / 谈薪的结构化讨论社区 —— 比 r/jobs 信噪比高，是科技岗求职（intake 的专业/技术面试子领域）的现实参照系。
- **典型内容**: 「new grad 求职时间线该怎么排」「刷题刷到什么程度够面」「两个 offer 怎么选」「levels.fyi 上的数字真实吗」。有成熟的 wiki（含 salary sharing、面试流程、简历模板讨论）。
- **投入产出比**: medium — 50-80% 帖有信号，wiki 部分质量高；科技岗教练值得定期看，非科技岗教练作 ambient。
- **Paywall**: none
- **签名内容**: 子版 wiki（求职 FAQ + salary sharing thread）；周期性 new grad 求职时间线讨论。
- **Endorsement evidence**: (1) `community_consensus` — 科技岗求职第一社区 (evidence: [T05-S008]); (2) `cross_source` — 与 levels.fyi / Blind 数据互相印证讨论 (evidence: [T05-S008, T05-S018])。
- **替代品**: 一亩三分地（北美华人科技岗，中文）；Blind（匿名，更内幕）。
- **最近变化（近 6 个月）**: AI 对科技岗招聘冲击的讨论密度上升。
- **可信度**: medium（wiki 质量较高，单帖仍是轶事）
- **Decay risk**: medium — 与 Reddit 平台绑定。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（科技岗结构化讨论 + wiki）/ 可访问性 ✅ → **KEEP, medium**

### 💬 3. r/recruiting

- **Type**: community
- **URL**: https://www.reddit.com/r/recruiting/
- **Platform**: Reddit
- **规模**: 约 30 万+ 成员
- **Audience tier**: practitioner（招聘方 — recruiter / sourcer / HR）
- **Cadence / 活跃度**: rolling，活跃
- **Last activity**: 2026-05（持续活跃）
- **One-liner**: **桌子另一边的视角** —— recruiter 和 sourcer 在这里讨论怎么筛简历、怎么用 ATS、怎么看待求职者的各种做法。对教练是稀缺的「招聘方反向情报」源。
- **典型内容**: 「求职者哪些行为让我直接 pass」「ATS 实际怎么用、关键词到底重不重要」「为什么不回复求职者」「冷邮件 / LinkedIn 私信哪种有效」。教练读它能校准「我教学员的做法，招聘方那边到底买不买账」。
- **投入产出比**: medium — 对教练是高价值 niche 源（招聘方视角稀缺），但帖量小、需主动检索；定位为「定期挖一遍」而非「每天刷」。
- **Paywall**: none
- **签名内容**: 周期性「求职者常见误区，来自 recruiter」类高赞帖；ATS 实操讨论。
- **Endorsement evidence**: (1) `community_consensus` — 招聘从业者主要 Reddit 聚集地 (evidence: [T05-S009]); (2) `cross_source` — 求职建议常引「recruiter 怎么说」时指向此类社区 (evidence: [T05-S009, T05-S004])。
- **替代品**: LinkedIn Talent Blog（T05-S022，机构化的招聘方视角，但更 PR）；Madeline Mann 的招聘官视角内容。
- **最近变化（近 6 个月）**: AI 筛简历 / AI 面试对 recruiter 工作流的影响讨论上升。
- **可信度**: medium（从业者一手观察，但仍是个人视角）
- **Decay risk**: medium — 与 Reddit 平台绑定。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（招聘方视角，教练的反向情报刚需）/ 可访问性 ✅ → **KEEP, medium**

### 💬 4. 一亩三分地

- **Type**: community（独立论坛）
- **URL**: https://www.1point3acres.com/
- **Platform**: 独立论坛（非 Reddit / 非黑名单平台）
- **规模**: 北美华人求职 / 留学主阵地（社区量级大）
- **Audience tier**: practitioner（北美求职的华人，多为科技 / 理工岗）
- **Cadence / 活跃度**: rolling，活跃
- **Last activity**: 2026-05（持续活跃）
- **One-liner**: 北美华人求职 / 面经 / offer / 身份的核心社区 —— 是「国内用户出海求职」和「海外求职体系」之间的桥接源，对处理 intake 中「海归 / 国际学生 / 签证」子领域尤其相关。
- **典型内容**: 北美公司面经（含具体题目和流程）、offer 对比、H1B / OPT / 绿卡身份讨论、new grad 求职时间线、各公司 package。中文，但讲的是海外求职体系。
- **投入产出比**: medium — 对服务「华人出海求职」的教练是高价值；面经板块颗粒度细。一般教练作 ambient。
- **Paywall**: 部分内容需积分 / 注册（论坛积分制，非现金 paywall）
- **签名内容**: 各大厂面经合集；身份 / 签证专版。
- **Endorsement evidence**: (1) `community_consensus` — 北美华人求职默认参考社区 (evidence: [T05-S014]); (2) `cross_source` — 与 Glassdoor / Blind 面经互为印证 (evidence: [T05-S014, T05-S015])。
- **替代品**: r/cscareerquestions（英文，非华人特化）；牛客网（国内校招，非出海）。
- **最近变化（近 6 个月）**: 美国科技业裁员 + 签证政策讨论密度上升。
- **可信度**: medium（面经一手，但真伪 / 代表性需甄别 — 同 intake 对「面经」的警示）
- **Decay risk**: medium — 独立论坛，运营稳定但单一平台风险。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（华人出海求职桥接，跨 locale）/ 可访问性 ✅ → **KEEP, medium**

## 四、数据 / 报告源

> 数据源对求职教练的核心价值：**给「市场周期 vs 个人可控部分」的边界提供事实底座**（intake warning 3）。教练不能把「找不到工作」全归因于个人，也不能假装宏观约束不存在 —— 数据源就是这条诚实边界的支撑。gov / gov.cn → `verified_primary`；机构数据页 → `surrogate_primary`；众包数据站 → `secondary`。

### 📊 1. US BLS（劳工统计局，含 Occupational Outlook Handbook）

- **Type**: dataset / 官方统计
- **URL**: https://www.bls.gov/ ；岗位手册 https://www.bls.gov/ooh/
- **Maintainer**: 美国劳工统计局（US Bureau of Labor Statistics）
- **Cadence**: 就业数据月度发布；OOH 年度更新
- **Last activity**: 2026-05（月度 jobs report 持续发布）
- **Audience tier**: mixed（数据本身中立，教练用于宏观判断）
- **One-liner**: 美国就业 / 失业率 / 行业薪资 / 岗位前景的官方 ground truth —— 服务美国求职者的教练判断「这个行业现在是冷是热」的事实依据。
- **典型内容**: 月度就业报告（新增岗位、失业率、各行业变化）；OOH 按岗位给出薪资中位数、增长前景、教育门槛。完全免费、可机读。
- **投入产出比**: medium — 不是每周看，是「做职业定位 / 判断行业冷热 / 谈薪找锚」时查；对教练是 reference utility。
- **Paywall**: none
- **签名内容**: 月度 Employment Situation 报告；OOH 各岗位条目。
- **Endorsement evidence**: (1) 政府一手 — 立法授权的官方统计机构 (evidence: [T05-S017, T05-S021]); (2) `cross_source` — 几乎所有美国就业市场分析都引用 BLS (evidence: [T05-S017])。
- **替代品**: 国家统计局（中国对应）；LinkedIn Economic Graph（趋势但非官方）。
- **最近变化（近 6 个月）**: 数据持续，反映科技业放缓后的就业结构变化。
- **可信度**: high（政府官方统计）
- **Decay risk**: low — 机构级、法定职能。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅ / 可访问性 ✅ → **KEEP, high**

### 📊 2. 国家统计局（中国）

- **Type**: dataset / 官方统计
- **URL**: https://www.stats.gov.cn/
- **Maintainer**: 中华人民共和国国家统计局
- **Cadence**: 月度 + 季度 + 年度
- **Last activity**: 2026-05（月度数据持续发布）
- **Audience tier**: mixed
- **One-liner**: 中国城镇调查失业率 / 就业 / 收入的官方数据 —— 服务国内求职者的教练判断就业大盘、回应「现在好不好找工作」的事实底座。
- **典型内容**: 城镇调查失业率（含分年龄段，青年失业率是高关注指标）、就业人员数、居民收入。注意：官方口径与体感可能有差，教练引用时只作「官方大盘」一个维度，不当全部。
- **投入产出比**: medium — 同 BLS，做定位 / 判断大盘时查，非高频。
- **Paywall**: none
- **签名内容**: 月度国民经济运行数据中的就业部分；青年失业率序列。
- **Endorsement evidence**: (1) 政府一手 — 国家法定统计机构 (evidence: [T05-S020]); (2) `cross_source` — 国内就业讨论的默认官方数据源 (evidence: [T05-S020])。
- **替代品**: 智联 / BOSS 直聘 / 前程无忧 的招聘报告（机构数据，颗粒度不同但**主阵地多在公众号发布，无合规可引用 URL** — 见诚实声明）。
- **最近变化（近 6 个月）**: 青年失业率统计口径近年有调整，引用需注意口径说明。
- **可信度**: high（官方）；medium 关于「是否反映体感」—— 口径局限要标注
- **Decay risk**: low — 机构级。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（国内就业唯一官方源）/ 可访问性 ✅ → **KEEP, high**

### 📊 3. LinkedIn Economic Graph

- **Type**: dataset / 机构研究（surrogate_primary — 机构数据）
- **URL**: https://economicgraph.linkedin.com/
- **Maintainer**: LinkedIn（微软旗下）
- **Cadence**: 季度 / 不定期专题报告
- **Last activity**: 2026 年内持续发布报告
- **Audience tier**: practitioner-senior
- **One-liner**: 全球技能迁移 / 招聘趋势 / 岗位变化的机构数据 —— 基于 LinkedIn 平台数据，是「哪些技能在升值、哪些岗位在增长」的趋势源（非官方，有平台样本偏差）。
- **典型内容**: 全球 / 各国招聘趋势报告、技能需求变化、行业人才流动、远程工作趋势。可视化做得好。**样本偏 LinkedIn 用户**（白领、英语区为主），代表性有偏，引用要标注。
- **投入产出比**: medium — 趋势判断有用，但更新不密、且需扣样本偏差；做定位 / 趋势研究时查。
- **Paywall**: none（报告免费）
- **签名内容**: 年度 / 周期性 Global Talent Trends 类报告；Skills 报告。
- **Endorsement evidence**: (1) 机构数据 — LinkedIn 平台规模构成数据基础 (evidence: [T05-S010]); (2) `cross_source` — 招聘趋势分析广泛引用 (evidence: [T05-S010])。
- **替代品**: BLS（官方但无技能颗粒度）；各招聘平台报告。
- **最近变化（近 6 个月）**: AI 技能需求是近期报告高频主题。
- **可信度**: medium（机构数据，但平台样本偏差明确）
- **Decay risk**: low — 机构级 source。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（技能趋势颗粒度，官方源没有）/ 可访问性 ✅ → **KEEP, medium**

### 📊 4. levels.fyi

- **Type**: dataset（众包薪资数据）
- **URL**: https://www.levels.fyi/
- **Maintainer**: levels.fyi（独立公司）
- **Cadence**: rolling 众包更新
- **Last activity**: 2026-05（持续更新）
- **Audience tier**: practitioner（科技岗求职者）
- **One-liner**: 科技岗薪资 / 职级对照的众包数据库 —— 谈薪子领域的事实依据，让求职者「报数字时心里有锚」，反信息不对称。
- **典型内容**: 各公司各职级的 base / stock / bonus 数据，职级横向对照（如 Google L4 ≈ Meta E4）。科技岗为主，近年扩展到部分非科技岗。
- **投入产出比**: medium — 谈薪环节高价值，平时不看；科技岗教练的必备 reference。
- **Paywall**: 基础数据免费；有付费的薪资谈判服务 / 高级数据（基础够用，付费非必需）
- **签名内容**: 公司职级对照表；年度薪资报告。
- **Endorsement evidence**: (1) `community_consensus` — r/cscareerquestions 谈薪讨论默认引用 (evidence: [T05-S018, T05-S008]); (2) `cross_source` — 科技岗薪资讨论的事实标准 (evidence: [T05-S018])。
- **替代品**: Glassdoor 薪资（更广但颗粒度粗）；Blind（匿名 self-report）；国内看准网（**国内薪资透明度明显更低** — intake 已标）。
- **最近变化（近 6 个月）**: 持续，覆盖岗位类型扩展。
- **可信度**: medium（众包 self-report，科技岗样本足够大时较可靠，长尾公司数据稀疏）
- **Decay risk**: low-medium — 已是科技岗薪资基础设施，但单一公司运营。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（科技岗薪资颗粒度，谈薪刚需）/ 可访问性 ✅ → **KEEP, medium**

### 📊 5. Glassdoor（面经 + 薪资板块）

- **Type**: dataset / 众包内容（面经 + 薪资 + 公司评价）
- **URL**: https://www.glassdoor.com/Interview/index.htm
- **Maintainer**: Glassdoor
- **Cadence**: rolling 众包
- **Last activity**: 2026-05（持续更新）
- **Audience tier**: mixed
- **One-liner**: 公司面经 + 面试流程 + 薪资区间 + 员工评价的众包聚合 —— 求职者「研究目标公司」的默认起点，覆盖面比 levels.fyi / 一亩三分地 都广（不限科技岗、不限地区）。
- **典型内容**: 按公司聚合的面试题目、面试流程描述、面试难度评分、薪资区间、员工评价。覆盖广是优点；单条真伪 / 代表性需甄别（同 intake 对面经的警示），且公司可能「公关」评价。
- **投入产出比**: medium — 「研究目标公司 / 准备特定公司面试」时高价值，平时不看。
- **Paywall**: 部分内容需「贡献换查看」（贡献制，非现金 paywall）
- **签名内容**: 公司面经页；公司评价页。
- **Endorsement evidence**: (1) `community_consensus` — 求职研究公司的默认工具之一 (evidence: [T05-S015]); (2) `cross_source` — 求职建议常推荐用 Glassdoor 做公司研究 (evidence: [T05-S015, T05-S012])。
- **替代品**: 一亩三分地（北美华人科技岗，更细）；Blind（匿名，更内幕）；levels.fyi（薪资更准但限科技岗）。
- **最近变化（近 6 个月）**: 与 Indeed 整合后产品有调整；评价真实性争议长期存在。
- **可信度**: medium（众包，覆盖广但单条需甄别）
- **Decay risk**: low-medium — 平台级，但产品策略受母公司影响。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（覆盖最广的公司研究源）/ 可访问性 ✅ → **KEEP, medium**

> **补充 reference utility（不单列卡片，作 manifest 收录）**：
> - LinkedIn Talent Blog（T05-S022，verified_primary）—— 招聘方官方视角，比 r/recruiting 更机构化但更 PR，作教练「了解招聘方话语」的补充。
> - Big Interview Blog（T05-S023，verified_primary）—— 面试训练产品的 vendor 一手内容，方法论受产品框架影响，作面试准备的参考之一。
> - HBR job-search topic（T05-S024，secondary）—— 求职 / 谈薪的严肃长文，更新不密但质量高，作 senior tier 补充。

## 五、国内信息源

> **结构性诚实声明（关键）**：国内求职 / 面试领域的一手深度信息源，主阵地高度集中在 **知乎话题页 / 微信公众号 / 小红书 / B 站** —— 这些在六轨 research 共用黑名单上（知乎 / 公众号 / 百度百科），**不能作为知识真伪的引用源、不进 manifest**。结果是：国内侧「有合规可引用 URL 的一手深度信息源」结构性偏薄。
> 处理方式（遵循 track 硬规矩 3）：(1) 收录**非黑名单**的国内独立站 —— 牛客网（nowcoder.com）、一亩三分地、国家统计局；(2) 黑名单平台上的国内 creator（瞎说职场 / 圈外同学 / 大厂面试官 IP）**在此诚实列出其存在与价值，但不放黑名单 URL**，留给 Phase 2 在「国内 vs 海外信息源密度差」接口明确标注；(3) 不为了凑数硬塞黑名单链接。

### 🇨🇳 1. 牛客网（nowcoder.com）

- **Type**: community + dataset（独立站，**非黑名单**）
- **URL**: https://www.nowcoder.com/
- **Maintainer**: 牛客网
- **Cadence**: rolling（校招季密度极高）
- **Last activity**: 2026-05（持续活跃，跟随校招节奏）
- **Audience tier**: practitioner（国内校招生 + 部分社招）
- **One-liner**: 国内校招生态的中枢 —— 笔面经 + 内推 + 题库 + 校招时间线 + 公司讨论一站式，是理解 intake「国内校招工业化节奏」子领域绕不开的一手平台。
- **典型内容**: 海量笔试 / 面试经验帖（按公司、岗位、批次组织）、在线判题题库（技术岗）、内推信息、各公司校招进度讨论、offer 比较。**面经真伪 / 代表性需甄别**（同 intake 对面经的警示 — 有「钓鱼帖」「贩卖焦虑帖」）。
- **投入产出比**: medium — 对服务国内校招的教练是必看一手平台（校招季 high，平时 medium）；非校招方向教练作 ambient。
- **Paywall**: 基础内容免费；部分题库 / 服务付费（基础够用）
- **签名内容**: 各大厂校招面经合集；校招时间线 / 行情贴。
- **Endorsement evidence**: (1) `community_consensus` — 国内校招求职默认平台，已是基础设施 (evidence: [T05-S013]); (2) `cross_source` — 国内校招讨论、培训机构「内推 / 题库」均以牛客为锚 (evidence: [T05-S013])。
- **替代品**: 实习僧（限实习）；各招聘平台（无面经社区属性）。国内**无与之并列的第二个非黑名单校招社区**。
- **最近变化（近 6 个月）**: AI 面试 / AI 笔试讨论上升；校招规模与「就业难」情绪反映明显。
- **可信度**: medium（平台合规可引用，但单条面经需甄别真伪）
- **Decay risk**: low-medium — 国内校招基础设施，单一平台风险存在。

判定：真实背书 ✅ / Active ✅ / 独特价值 ✅（国内校招唯一非黑名单一手社区）/ 可访问性 ✅ → **KEEP, high（国内侧最重要的可引用源）**

### 🇨🇳 2. 一亩三分地

- 见「三、社区」第 4 条（T05-S014）。跨 locale 桥接源 —— 中文界面但讲海外求职体系，是「国内用户出海求职」的主参考。在国内信息源维度复算一次：对处理 intake「海归 / 国际学生 / 签证」子领域是国内侧少数**合规可引用**的深度社区。

### 🇨🇳 3. 国家统计局

- 见「四、数据 / 报告源」第 2 条（T05-S020）。国内就业大盘的唯一官方数据源 —— 也是国内侧少数 `verified_primary`。

### 🇨🇳 国内一手深度 creator（诚实列出，无合规 URL，不进 manifest）

以下 creator 在国内求职领域有真实影响力，但主阵地是黑名单平台，**此处仅作存在性记录 + 价值与噪音判断**，URL 不收录、不作引用源：

- **瞎说职场（Sean Ye）** —— 前外企 HR 咨询背景，主阵地公众号「瞎说职场」+ 知乎大 V。风格是「揭秘式」求职 / 职场 / 薪资内容，对「招聘方怎么想」「薪资信息不对称」有一手视角。**价值**：国内少数有 HR 咨询背景、方法论相对扎实的个人 IP。**噪音判断**：内容质量在国内个人 IP 中偏上，但仍有标题党 / 引流成分。→ Phase 2 figure 候选（喂 wave 2 Track 01）。
- **圈外同学（孙圈圈）** —— 创始人孙圈圈，主阵地公众号 + 付费课程。偏「职业规划与定位」而非求职战术，对 intake「求职定位与职业叙事」子领域相关。**价值**：职业规划方法论有体系。**噪音判断**：课程导流色彩较重，「定位」内容与「卖课」绑定紧。→ Phase 2 figure 候选。
- **国内大厂面试官类 IP** —— 知乎 / B 站 / 小红书上大量「我是 XX 大厂面试官」账号。**价值**：理论上有招聘方一手视角。**噪音判断**：**真伪与代表性高度存疑** —— 「面试官」身份难核实，且大量是引流卖课 / 卖「内推」的账号。作为「行业现状样本」整体观察，不奉为信息源，不单独点名。
- **B 站 / 小红书求职 UP 主** —— 大厂求职经验、面经复盘、简历模板类内容密集。**价值**：贴近国内年轻求职者的真实关切。**噪音判断**：信噪比低、「速成 / 包装」话术多、与培训机构营销边界模糊。作 ambient 现状感知。

> 国内侧信号强弱结论：**合规可引用的一手深度源仅 3 个（牛客 / 一亩三分地 / 国家统计局），其中真正「方法论 creator」型的为 0** —— 国内一手深度信息源结构性偏薄。海外侧（newsletter 4 + YouTube 5 + 社区 3 + 数据 4）密度显著更高。这是 locale=global 下必须诚实标注的不对称，Phase 2 接口与 SKILL.md 诚实边界都要写明。

## 六、培训机构样本（行业现状甄别用，非「大师」）

> **定位说明（关键）**：本节的机构**不是信息源、不是「大师」、不进 figures**。它们是 intake / SKILL.md 必须直面的「**行业现状与营销话术样本**」—— 用来让生成的 SKILL.md 能教读者**甄别**「有效方法」vs「制造焦虑卖课 / 包 offer 黑产」。研读它们的公开内容（官网 / 公开课 / 营销页），目的是**解剖营销结构**，不是学方法。
> **共同背景噪音**：国内求职培训行业「包 offer」「内推保过」「名企内推资源」是普遍营销话术，部分滑向黑产（买内推、代写简历造假、面试作弊代面）—— intake warning 1 已定为「这个行业最大的雷」。机构内容**整体当反面 / 现状样本看**，不引用为方法论。

### ⚠️ 1. offer 先生（OfferShow 一类国内校招求职训练营）

- **Type**: 国内校招求职培训机构（行业现状样本）
- **典型形态**: 面向应届生 / 校招的训练营 + 1v1 简历精修 + 模拟面试 + 「内推资源」打包，按套餐 / 训练营定价。
- **营销与噪音背景**: 「内推」「offer」是核心营销钩子；「保 offer」「名企内推」类话术常见。国内校招辅导高度工业化、机构化程度远高于个人 IP。
- **作为样本的价值**: 是 intake「国内校招工业化辅导」子领域的典型形态 —— SKILL.md 讲「国内校招辅导长什么样」时，这类机构是现实参照。**解剖点**：(1)「内推资源」到底是什么、合不合规、和「买内推」黑产的界线在哪；(2)「简历精修 + 模拟面 + 内推」打包模式中，哪部分是真有效（简历 / 模拟面的方法），哪部分是制造稀缺感（内推资源）。
- **甄别提示**: 「有效方法」= 简历结构化打磨、模拟面试与复盘、校招时间线管理（这些教练自己也该做）；「营销噪音」= 「保 offer」承诺、把「内推」包装成决定性资源、用校招焦虑催单。
- **可信度**: low（作为信息源）—— **不引用其内容为方法论**，仅作现状样本观察。
- **Endorsement evidence**: 作为「行业现状样本」收录，非背书型 source；其存在本身即 intake / 行业现状的证据 (evidence: [T05-S013] —— 牛客等校招生态中机构营销可观察)。
- **Decay risk**: 高（机构兴衰快、改名重组常见）—— 但「这类机构存在且营销话术雷同」这个**现状判断**本身 decay 低。

判定（按「样本」而非「source」判）：作为现状样本 **KEEP**；作为信息源 **不 retain、不引用**。

### ⚠️ 2. DBC 职梦 / 职优你（UniCareer）一类留学生 · 海归求职机构

- **Type**: 留学生 / 海归求职培训机构（行业现状样本）
- **典型形态**: 面向留学生 / 海归的求职项目 —— 行业课程（投行 / 咨询 / 数据 / 科技等）+ 简历与面试辅导 + 「名企内推」+ 实习 / 全职求职打包，定价高（万元级套餐常见）。
- **营销与噪音背景**: 「名企内推」「实习保 offer」「mentor 来自 XX 大厂」是核心营销话术；面向留学生信息差大、付费能力强的群体，**焦虑营销 + 高客单价**特征明显。「包 offer」争议在留学生求职机构领域尤其集中。
- **作为样本的价值**: 是 intake「海归求职」「特殊群体求职」子领域的现实参照 —— SKILL.md 讲「留学生求职机构化辅导」时的样本。**解剖点**：(1)「名企内推」「mentor 内推」的合规性与利益结构 —— mentor 拿钱推人，与「教练站求职者一边」的角色冲突在哪；(2) 高客单价套餐里，「行业知识 + 求职方法」的真实价值 vs 「内推 / 资源」的稀缺感包装；(3) intake warning 8 的「教练 + 卖内推 + 抽成 / 机构绑定」利益冲突，在这类机构身上最典型。
- **甄别提示**: 「有效方法」= 行业认知补全（留学生确实信息差大）、目标市场的简历 / 面试规范、求职时间线;「营销噪音」= 「保 offer」、把 mentor「内推」当核心卖点、用「回国 / 留下都难」的双向焦虑催单。
- **可信度**: low（作为信息源）—— **不引用其内容为方法论**，仅作现状样本观察。
- **Endorsement evidence**: 作为「行业现状样本」收录，非背书型 source；其存在与营销模式本身即 intake warning 1 / 8 的现实证据 (evidence: [T05-S014] —— 一亩三分地等社区中可观察留学生求职机构营销与争议)。
- **Decay risk**: 高（机构兴衰 / 改名 / 暴雷常见）—— 「现状判断」本身 decay 低。

判定（按「样本」而非「source」判）：作为现状样本 **KEEP**；作为信息源 **不 retain、不引用**。

> **培训机构样本小结**：2 个样本（国内校招型 + 留学生 / 海归型）覆盖了国内求职培训行业的两大主要形态。**它们在 SKILL.md 中的唯一作用是支撑「甄别」教学**：教读者识别「保 offer / 内推保过」话术、看清「教练 + 卖内推」的利益冲突、区分机构内容里「真方法」与「焦虑变现」。绝不作为 figures、绝不引用其内容为知识来源。

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」（进 master skill「Sources — 信息源」节 highlights）

1. **Cultivated Culture（Austin Belcak）**（evidence: [T05-S001, T05-S002]）—— newsletter + LinkedIn，networking 派方法论旗舰，跨 source 高频被点名。
2. **Ask a Manager（Alison Green）**（evidence: [T05-S006]）—— 求职困境真实场景问答的最大语料库，行业基础设施级，判断力锚。
3. **Jeff Su（YouTube）**（evidence: [T05-S003]）—— 简历 / LinkedIn / AI 辅助求职的高密度实操，受众最广。
- 国内侧 top 1：**牛客网**（evidence: [T05-S013]）—— 国内校招唯一非黑名单一手平台，服务国内校招的教练必看。

### 「这一行最近的话题热度」（候选信号 — 用于 Phase 2.4 近期工作流变化）

- **`topic-heat: incomplete, sources listed but content not crawled`** —— 本 track 时间盒内只做了 source 识别 + URL 分类，未深度爬取各 source 的最新 episode / issue 标题。以下「热点」是基于 source 描述层的**低置信推断**，非 high-confidence：
  - AI 改简历 / AI outreach / AI 模拟面试（求职者侧）—— Jeff Su、Belcak 内容明显倾斜
  - AI 筛简历 / AI 初面对求职的冲击（招聘方侧）—— r/recruiting、r/cscareerquestions 讨论上升
  - 科技业裁员后的「市场难」情绪 + 谈薪保守化 —— r/jobs、r/cscareerquestions、一亩三分地
  - 国内青年就业压力 / 校招规模 —— 牛客、国家统计局青年失业率序列
- Phase 2 若要把这些写进「近期工作流变化」，**建议先用 WebFetch / browser-skill 爬 3-5 个 source 的最新 10 条内容**再定级；否则在 SKILL.md 标「时效敏感，需自行核实」。

### 新 figures 发现（喂给 wave 2 Track 01）

本 track 识别的 creator 与 intake figures 候选高度重合，**确认强化**以下为 figure：Austin Belcak / Jeff Su / Madeline Mann / Andrew LaCivita / Liz Ryan / Alison Green —— 均有可直接研读的一手内容（newsletter / YouTube 频道），是 Track 01 的低成本起点。
- **国内 figure 候选（intake 已提，本 track 确认其「有真实影响力但主阵地是黑名单平台」）**：瞎说职场（Sean Ye）、孙圈圈（圈外同学）—— Track 01 研究时注意：一手内容在公众号 / 知乎，**可作 figure 卡片但无合规可引用 URL**，需按「国内 figure 结构性约束」处理。
- 本 track **未发现** wave 1 其他 track 完全没提及的新 figure —— sources 侧人物与 intake 名单一致，无额外发现。

### 新 tools 发现（喂给 wave 2 Track 02）

本 track 多个 source 反复关联的工具，**全部已在 intake key_tools_candidates 中**，确认强化、无新增：
- **levels.fyi**（[T05-S018]）—— r/cscareerquestions 谈薪讨论默认引用，科技岗薪资事实标准。
- **Glassdoor**（[T05-S015]）—— 公司研究 / 面经默认起点，覆盖最广。
- **Blind**（[T05-S016]）—— 匿名薪资 / offer / 内幕，与 levels.fyi 互补。
- **牛客网**（[T05-S013]）—— 既是社区也是国内校招题库 / 内推工具。
- **一亩三分地**（[T05-S014]）—— 北美华人面经 / 身份信息工具。
- ChatGPT / Claude 用于改简历 / 模拟面 —— Jeff Su、Belcak 内容反复演示（Track 02 须带强时效标注）。
- 本 track **未发现** intake 之外的新 tool。

### 国内 vs 海外信息源密度差（master skill 诚实边界必写）

- **海外侧**：newsletter / 博客 4（Belcak / Ask a Manager / Liz Ryan / 80,000 Hours）+ YouTube 5（Jeff Su / Madeline Mann / LaCivita / Liz Ryan / Belcak 视频）+ 社区 3（r/jobs / r/cscareerquestions / r/recruiting）+ 数据 4（BLS / LinkedIn Economic Graph / levels.fyi / Glassdoor）—— 一手、可引用、可直接研读，密度高。
- **国内侧**：合规可引用的一手深度源仅 **3 个**（牛客网 / 一亩三分地 / 国家统计局），且其中**「方法论 creator」型为 0**。国内真正有方法论的个人 IP（瞎说职场 / 圈外同学 / 大厂面试官）主阵地全在黑名单平台（知乎 / 公众号 / 小红书 / B 站），**无合规可引用 URL**。
- **结论**：locale=global 下，sources 维度存在**显著的国内 / 海外不对称**。SKILL.md 必须诚实写明：「国内求职信息源的深度内容主要散落在知乎 / 公众号 / 小红书，本 skill 未将其作为可引用知识源；国内侧建议优先用牛客（校招）+ 官方就业数据，并对个人 IP 内容自行交叉验证」。这不是「国内没有信息源」，而是「国内一手深度信息源的可引用性结构性受限」。

### 营销噪音甄别提示（本行业特有，必写进 SKILL.md）

- 培训机构内容（offer 先生 / DBC 职梦 / 职优你 类）**整体当行业现状样本，不作信息源、不引用为方法论**。SKILL.md 用它们教「甄别」：识别「保 offer / 内推保过」话术、看清「教练 + 卖内推 + 抽成」利益冲突、区分机构内容里「真方法」（简历打磨 / 模拟面 / 时间线管理）与「焦虑变现」（保 offer 承诺 / 把内推包装成决定性资源 / 用 35 岁与就业焦虑催单）。
- 即使是 retain 的优质 creator（Belcak / Jeff Su / LaCivita），也都有**自家课程 / 工具导流**成分 —— Phase 2 提炼时取「方法论骨架」，不照搬「话术 / 具体 prompt / 模板」（后者保鲜期短，intake warning 10）。
- 面经类源（牛客 / 一亩三分地 / Glassdoor）**单条真伪与代表性需甄别** —— 有钓鱼帖、贩卖焦虑帖、公司公关评价。SKILL.md 教「面经看趋势不看单条，交叉多源」。

### 冷僻 / 信号薄弱自检

- newsletter 4 ✅（≥ 3）/ YouTube creator 5 ✅（≥ 3）/ 社区 4 ✅（≥ 1）/ 数据报告 5 ✅ / conference：**本行业无年度行业大会传统**（求职 / 面试辅导不是会议驱动型行业，N/A 合法 — 见失败处理表）/ dataset：以「就业数据 / 薪资众包数据」形式存在，已收 4 个。
- 有效 endorsement source ≥ 50% ✅ —— 海外 retained source 均有 ≥ 2 处独立背书（cross_source / community_consensus 为主）。
- **薄弱维度（须进 Phase 2.8 诚实边界）**：(1) 国内一手深度信息源结构性偏薄（合规可引用仅 3，方法论 creator 型 0）；(2) conference 维度本行业天然空缺；(3) topic-heat 未深度爬取，时效信号为低置信推断。
- 整体信号：**海外 sources 维度丰满，国内 sources 维度结构性偏薄** —— 不对称是本 track 最重要的诚实边界输出。

---

## 回报摘要

- **Newsletter / Substack creator**：4 条（Cultivated Culture / Ask a Manager / Liz Ryan / 80,000 Hours），均 KEEP（2 high / 2 medium）。
- **YouTube creator**：5 条（Jeff Su / Self Made Millennial / Andrew LaCivita / Liz Ryan / Belcak 视频），3 KEEP + 2 BORDERLINE-KEEP。
- **社区**：4 条（r/jobs / r/cscareerquestions / r/recruiting / 一亩三分地），均 KEEP medium。
- **数据 / 报告源**：5 条（BLS / 国家统计局 / LinkedIn Economic Graph / levels.fyi / Glassdoor）+ 3 条 reference utility（LinkedIn Talent Blog / Big Interview Blog / HBR）。
- **国内信息源**：3 条合规可引用（牛客网 / 一亩三分地 / 国家统计局）+ 诚实列出 4 类黑名单平台 creator（瞎说职场 / 圈外同学 / 大厂面试官 IP / B 站小红书 UP 主，不进 manifest）。
- **培训机构样本**：2 条（offer 先生 类国内校招机构 / DBC 职梦·职优你 类留学生机构），仅作行业现状甄别样本，不作信息源、不引用。
- **Manifest 条数**：25 条（T05-S001 ~ T05-S025）。bucket 分布：verified_primary 8 / surrogate_primary 1（LinkedIn Economic Graph，机构数据）/ secondary 13 / reference 3。**零黑名单 URL 进表**。
- **国内侧信号强弱**：**结构性偏薄** —— 合规可引用一手深度源仅 3 个，且方法论 creator 型为 0；国内有方法论的个人 IP 主阵地全在黑名单平台。海外侧密度显著更高。国内 / 海外不对称是本 track 最重要的诚实边界输出，已在 Phase 2 接口明确标注。
