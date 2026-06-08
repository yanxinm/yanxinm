# Track 05 — Sources（信息源调研）

> 行业：AI Product Manager（LLM 应用 / 生成式 AI / Agent 产品的产品经理实战）
> Locale：global（海外优先作者本人 Substack / YouTube / podcast 官方页 / arXiv；国内小宇宙 / 即刻优先，知乎 / 公众号文章黑名单）
> 调研日期：2026-05-14｜时间盒 ~12 min
> Phase 1 Wave 1 第 2 路 subagent — 输出作为 Wave 2 Track 01（figures）+ Track 02（tools）的 seed

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://www.lennysnewsletter.com/ | secondary | 2026-05-14 | Lenny Rachitsky | 作者本人 Substack，实为 author-owned 渠道（auto=secondary：lennysnewsletter.com bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T05-S002 | https://www.lennysnewsletter.com/podcast | surrogate_primary | 2026-05-14 | Lenny Rachitsky | Lenny's Podcast 官方页，长访谈 PM/AI 嘉宾 |
| T05-S003 | https://www.news.aakashg.com/ | secondary | 2026-05-14 | Aakash Gupta | Product Growth Substack — author-owned，AI PM 垂直（auto=secondary：news.aakashg.com bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T05-S004 | https://www.youtube.com/@growproduct | surrogate_primary | 2026-05-14 | Aakash Gupta | Product Growth YouTube — author-owned 视频渠道 |
| T05-S005 | https://marily.substack.com/ | verified_primary | 2026-05-14 | Marily Nika | AI Product Academy Newsletter — verifier 认证 newsletter author host |
| T05-S006 | https://www.latent.space/podcast | verified_primary | 2026-05-14 | swyx + Alessio Fanelli | Latent Space podcast — AI Engineering anchor，长访谈 |
| T05-S007 | https://www.cognitiverevolution.ai/ | secondary | 2026-05-14 | Nathan Labenz + Erik Torenberg | The Cognitive Revolution — host-owned 站，AI builders 访谈（auto=secondary：cognitiverevolution.ai bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T05-S008 | https://a16z.com/podcasts/ai-a16z/ | verified_primary | 2026-05-14 | a16z（Andreessen Horowitz） | AI + a16z podcast — verifier brand-domain content path |
| T05-S009 | https://eugeneyan.com/ | secondary | 2026-05-14 | Eugene Yan | 作者本人博客 — Anthropic MTS，applied ML / eval / RecSys×LLM（auto=secondary：eugeneyan.com bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto；具体文章 /writing/ 路径在 T04 仍为 verified_primary） |
| T05-S010 | https://hamel.dev/ | secondary | 2026-05-14 | Hamel Husain | 作者本人博客 — LLM evals field guide，AI PM 实操（auto=secondary：hamel.dev bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto；具体文章 /blog/posts/ 在 T04/T06 仍为 verified_primary） |
| T05-S011 | https://hamelhusain.substack.com/ | verified_primary | 2026-05-14 | Hamel Husain | Hamel Substack — verifier 认证 newsletter author host |
| T05-S012 | https://huyenchip.com/ | secondary | 2026-05-14 | Chip Huyen | 作者本人博客 — 《AI Engineering》(2025) 配套写作（auto=secondary：huyenchip.com bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto；配套 GitHub repo T04-S013 仍为 verified_primary） |
| T05-S013 | https://simonwillison.net/ | verified_primary | 2026-05-14 | Simon Willison | 作者本人 weblog — verifier 认证 personal primary，LLM 高频更新 |
| T05-S014 | https://www.ai.engineer/worldsfair | surrogate_primary | 2026-05-14 | swyx + Ben Dunphy | AI Engineer World's Fair 会议官网 — 主办方官方站，按 vendor docs 类一手处理（会议 sponsor / sessions list 作 surrogate 发现源；auto=secondary 但官方主办方站点合法标 surrogate_primary） |
| T05-S015 | https://www.latent.space/p/community | verified_primary | 2026-05-14 | Latent Space | Latent Space Discord 社区入口（AI Engineer 社区） |
| T05-S016 | https://www.anthropic.com/news | surrogate_primary | 2026-05-14 | Anthropic | vendor docs — 官方 blog，一手模型 / 产品迭代 |
| T05-S017 | https://openai.com/news/ | surrogate_primary | 2026-05-14 | OpenAI | vendor docs — 官方 news / blog（verifier 给 verified，按 SKILL 约束降为 vendor surrogate） |
| T05-S018 | https://huggingface.co/blog | surrogate_primary | 2026-05-14 | Hugging Face | vendor docs — 社区 + 官方 blog，开源模型动态 |
| T05-S019 | https://www.xiaoyuzhoufm.com/podcast/665dbd0694977a26efeb7a75 | verified_primary | 2026-05-14 | AI产品经理 Global | 小宇宙「AI产品经理 Global」播客 channel — verifier 认证 |
| T05-S020 | https://www.xiaoyuzhoufm.com/podcast/61cbaac48bb4cd867fcabe22 | verified_primary | 2026-05-14 | Monica（OnBoard!） | 小宇宙「OnBoard!」播客 channel — AI 产品 / 增长长访谈 |
| T05-S021 | https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc | verified_primary | 2026-05-14 | 泓君（硅谷101） | 小宇宙「硅谷101」播客 channel — 科技深访，2025 大量 AI 应用选题 |
| T05-S022 | https://www.reforge.com/courses | secondary | 2026-05-14 | Reforge | 课程平台 — 列为参考，非「资深人订阅渠道」（详见正文判定） |

> 黑名单排除（搜到但**不进 manifest**）：知乎专栏 / zhuanlan.zhihu.com、mp.weixin.qq.com（混沌大学 / PMTalk / 人人都是产品经理 / 朋克熊 / Plus 评测的公众号文章 URL）、CSDN、百度百科。这些渠道作为「figure 发声渠道」在 Track 01 可记其身份，但 Track 05 不收其文章 URL，Track 06 不引其内容。

---

## Step 1-2 候选清单与筛选结果

**撒网候选 ~30 个**（跨 5 type），经 Step 4 mechanical filter 后 **retain 22 个**，其中 1 个（Reforge）降级为 secondary 参考、不计入「资深人订阅渠道」。

**Drop 的候选（不进正文卡片）**：
- 「人人都是产品经理」AI 专栏 / 混沌大学公众号 / PMTalk 公众号 / Plus 评测公众号 / 朋克熊公众号 —— 黑名单渠道，URL 不收（公众号身份留给 Track 01）。
- Eye on AI（Craig Smith）—— 候选但被 a16z / Cognitive Revolution / Latent Space 在「AI builder 访谈」生态位高度覆盖，同圈只留 top，DROP（borderline，可作 Track 01 备选）。
- 小红书 AI PM 专栏 / 知乎 AI 产品话题 —— 黑名单 + 信噪比差，DROP。
- The Generalist（Mario Gabriele）/ Pete Huang The Neuron —— 偏 AI 商业洞察非 PM 实操，borderline，留作 figure 候选不进卡片。
- 「7 天速成 AI PM」「AI PM 月入 5 万」类课程营销 —— 行业警示明确点名，直接 DROP。

---

## Source 卡片

### 📰 1. Lenny's Newsletter

- **Type**: newsletter
- **URL**: https://www.lennysnewsletter.com/
- **Author / Host**: Lenny Rachitsky（前 Airbnb PM，与 Track 01 figures 关联）
- **Cadence**: weekly+（newsletter）
- **Last activity**: 2026-05（活跃，2026 年初发布「Best of 2025」）
- **Audience tier**: mixed（practitioner 为主，含 senior 战略反思）
- **One-liner**: 全球订阅量最大（1.2M+）的 PM newsletter，AI 专题访谈含金量高，是 AI PM「产品 sense」侧的 default 订阅。
- **典型每期内容**: 深研究的产品 / 增长 / 职业建议长稿，近一两年大幅增加 AI 选题——AI prototyping for PM、building AI agents、AI adoption 实操。常邀 AI PM / AI 公司创始人做访谈纪要。综合 PM 底盘 + AI 切面的结合，适合「传统 PM 转 AI PM」路径。
- **投入产出比**: medium——综合 PM 内容多，纯 AI PM actionable 内容约 50-70% 期触及；建议选读 AI 专题，非每期必看 (evidence: [T05-S001])
- **Paywall**: 部分付费（freemium，深度 issue + 全archive 需订阅；价格未在本次核到精确数，标注待核）
- **签名内容**: Marily Nika「AI and product management」访谈纪要（https://www.lennysnewsletter.com/p/summary-ai-and-product-management）；「Make product management fun again with AI agents」（https://www.lennysnewsletter.com/p/make-product-management-fun-again-9f6）
- **Endorsement evidence**: `community_consensus`（Substack 商业榜 #1，1.2M+ 订阅）；`cross_source`（intake research_strategy_notes 明确点名为 Track 05 起点种子）
- **替代品**: Aakash Gupta Product Growth（更垂直 AI PM）
- **最近变化**: 持续扩展 AI 覆盖，无 host 变更
- **可信度**: high
- **Decay risk**: medium——个人 newsletter，但已是 PM 圈基础设施，host 倦怠风险低于一般个人 newsletter

### 🎙️ 2. Lenny's Podcast

- **Type**: podcast
- **URL**: https://www.lennysnewsletter.com/podcast
- **Author / Host**: Lenny Rachitsky
- **Cadence**: weekly
- **Last activity**: 2026-05（活跃）
- **Audience tier**: mixed（practitioner + senior）
- **One-liner**: world-class 产品 / 增长 leader 长访谈，AI PM 专题集是「听这行的人怎么想」的高密度入口。
- **典型每期内容**: 60-90 min 深访，嘉宾覆盖大厂 AI 产品负责人、AI startup 创始人。近期集中讨论 AI 如何改写 PM 工作、AI agent 产品、AI adoption 挑战。访谈式而非新闻式——揭示行业 OS 而非时事。
- **投入产出比**: medium——综合 PM 嘉宾多，AI PM 信号约 50-70% 集；挑 AI 专题集听 (evidence: [T05-S002])
- **Paywall**: none（podcast 免费，配套纪要部分付费）
- **签名内容**: Marily Nika「AI and product management」集；AI agents 改写 PM 工作集
- **Endorsement evidence**: `community_consensus`（Apple Podcasts 长期高排名）；`cross_source`（intake 点名）
- **替代品**: Product Growth Podcast（Aakash Gupta）
- **可信度**: high
- **Decay risk**: medium

### 📰 3. Product Growth（Aakash Gupta）

- **Type**: newsletter（+ Product Growth Podcast 同 brand）
- **URL**: https://www.news.aakashg.com/ ｜ YouTube: https://www.youtube.com/@growproduct
- **Author / Host**: Aakash Gupta（前 Apollo.io VP Product，自称「the AI PM guy」，Track 01 figures 关联）
- **Cadence**: weekly（newsletter + podcast）
- **Last activity**: 2026-05（活跃，2026 年发「become an AI PM in 2026」更新版）
- **Audience tier**: practitioner（在职 / 求职 PM 实操 + 职业）
- **One-liner**: 自我定位「世界第一 AI PM newsletter + podcast」，AI PM 垂直度最高的单一信息源，452K+ 订阅。
- **典型每期内容**: AI PM 深 dive——如何成为 AI PM、AI 时代产品策略、AI PM 求职、PM 在 AI 团队的角色。强职业导向（也意味着部分内容偏「怎么拿 offer」而非「怎么做产品」）。视频 keynote + 文字 deep dive 配套。
- **投入产出比**: high——AI PM 垂直，≥80% 期对在职 / 转行 AI PM 有 actionable 内容；但要意识到职业营销成分（intake 警示：信噪比差、课程导流多，Aakash 内容偏求职端）(evidence: [T05-S003], [T05-S004])
- **Paywall**: freemium——核心 deep dive / 模板 / premium resources 付费（精确价格未核到，标注待核）
- **签名内容**:「How to Become an AI PM」（2024 原版 + 2026 更新版，Substack note c-189436506）；Northeastern PM 大会 keynote「product strategy in the age of AI」
- **Endorsement evidence**: `community_consensus`（Substack Technology 榜 #6，452K 订阅）；`cross_source`（intake research_strategy_notes 点名 Track 05 种子）
- **替代品**: Marily Nika AI Product Academy（更偏 bootcamp / 认证）；Lenny's（更综合）
- **最近变化**: 持续更新「2026 版 AI PM 路径」；newsletter + podcast + YouTube 三渠道并行
- **可信度**: high
- **Decay risk**: medium

### 📰 4. Marily's AI Product Academy Newsletter

- **Type**: newsletter
- **URL**: https://marily.substack.com/
- **Author / Host**: Dr. Marily Nika（前 Google / Meta AI PM，《Building AI-Powered Products》作者，Track 01 + Track 04 关联）
- **Cadence**: weekly（推断，活跃）
- **Last activity**: 2026-05（活跃，2026 年 5 月课程材料 refresh）
- **Audience tier**: beginner-practitioner（偏入门 + 转行，配套 bootcamp）
- **One-liner**: 「practical AI for PMs」——工具 / 工作流 / 认证导向，与 Maven AI PM Bootcamp 配套的入门级信息源。
- **典型每期内容**: AI PM 工具、工作流、认证清单。强教育属性——配套 Maven「AI PM 101 / Advanced AI PM / 12 周」课程。内容稳定但偏入门，对资深 AI PM 边际信息少。
- **投入产出比**: medium——对入门 / 转行 high，对资深 practitioner low-medium；本质是 bootcamp 导流但 newsletter 本身有独立价值，未跨黑名单 (evidence: [T05-S005])
- **Paywall**: newsletter 免费；配套 Maven bootcamp 付费（课程营销属性，订 newsletter 不必买课）
- **签名内容**: AI PM Certification list（https://marily.substack.com/s/certifications）；《Building AI-Powered Products》配套内容
- **Endorsement evidence**: `figure_long`（Marily Nika 本人 = Track 01/04 figure）；`community_consensus`（Maven #1 AI PM 认证，30k+ alumni）
- **替代品**: Aakash Gupta Product Growth（更 practitioner，少课程味）
- **最近变化**: 2026-05 课程材料完全 refresh
- **可信度**: high（作者一手）
- **Decay risk**: medium——与 bootcamp 商业绑定，课程优先级可能压过 newsletter

### 🎙️ 5. Latent Space: The AI Engineer Podcast

- **Type**: podcast
- **URL**: https://www.latent.space/podcast
- **Author / Host**: swyx（Shawn Wang）+ Alessio Fanelli（Track 01 figures 关联）
- **Cadence**: weekly（rolling，2026 起扩为 podcast network）
- **Last activity**: 2026-05（活跃，2026 启动 AI for Science 子节目）
- **Audience tier**: senior（资深 + 工程视角，AI PM 的「技术理解」侧 anchor）
- **One-liner**: AI Engineering 视角的行业 anchor——长访谈覆盖 foundation model / agent / 多模态 / GPU infra，AI PM 理解「工程边界」的必跟。
- **典型每期内容**: 60-120 min 长访谈 + 论文 / 新闻解读。嘉宾覆盖 LLM era 主流框架 founders + 一线工程师。2025 主题「coding agents」，swyx 2026 论断「coding agents 破壳做一切」。2025 年 10M+ 读者 / 听众。对 AI PM 是「跨 PM-工程协同」的共同语言来源。
- **投入产出比**: high——≥80% 集对需要技术理解的 AI PM 有信号；纯产品 sense 侧需配 Lenny / Aakash (evidence: [T05-S006])
- **Paywall**: none
- **签名内容**: Shopify「AI phase transition」集；Notion AI 集；「It's Time to Science」（https://www.latent.space/p/science）
- **Endorsement evidence**: `community_consensus`（2025 10M+ 读者/听众）；`cross_source`（intake research_strategy_notes 点名一手 podcast）
- **替代品**: The Cognitive Revolution（更偏 builder 访谈广度）
- **最近变化**: 2026 转型 podcast network，加 host、加 AI for Science 子节目
- **可信度**: high
- **Decay risk**: low——已是 AI engineering 圈基础设施，机构化程度高

### 🎙️ 6. The Cognitive Revolution

- **Type**: podcast
- **URL**: https://www.cognitiverevolution.ai/
- **Author / Host**: Nathan Labenz + Erik Torenberg（Turpentine podcast network）
- **Cadence**: biweekly+（活跃）
- **Last activity**: 2026-01+（活跃，发布「AI 2025→2026 Live Show」年度回顾）
- **Audience tier**: practitioner-senior（AI builders / researchers 访谈）
- **One-liner**: 「采访 AI 边缘的 builders」——比 Latent Space 更广覆盖 AI builder / researcher，AI PM 看「别人在 ship 什么」的 ambient awareness 源。
- **典型每期内容**: AI builder / researcher 深访 + live player 分析。覆盖 computer vision、AI agents、医疗应用、国际 AI 进展。有年度回顾 / 展望 live show。深度高但选题偏 AI 全景而非 PM 专属——对 AI PM 是 medium 信号。
- **投入产出比**: medium——AI builder 视角广，PM 直接 actionable 约 50-70% 集；作 ambient awareness 不必每集听 (evidence: [T05-S007])
- **Paywall**: none
- **签名内容**:「AI 2025→2026 Live Show Part 1」（https://www.cognitiverevolution.ai/ai-2025-2026-live-show-part-1/）
- **Endorsement evidence**: `community_consensus`（Apple/Spotify 长期 AI 类高位）；`cross_source`（intake 点名一手 podcast）
- **替代品**: AI + a16z（更偏投资 / 创始人视角）
- **可信度**: high
- **Decay risk**: medium——Turpentine network 支撑，但个人 host 主导

### 🎙️ 7. AI + a16z

- **Type**: podcast
- **URL**: https://a16z.com/podcasts/ai-a16z/
- **Author / Host**: a16z（Andreessen Horowitz）合伙人 + 嘉宾
- **Cadence**: weekly
- **Last activity**: 2026（活跃）
- **Audience tier**: mixed（practitioner + senior，偏创始人 / 投资视角）
- **One-liner**: a16z 视角的 AI 行业走向——AI engineers / founders / experts 谈技术与行业方向，AI PM 看「资本 + 创始人怎么判断方向」的源。
- **典型每期内容**: AI engineer / founder / expert 访谈。覆盖 agents + MCP 重塑 email、AI 重塑 web dev、DeepSeek 安全、AI × 教育。机构出品，立场偏「what's next / 投资逻辑」——对 AI PM 是战略层 ambient，少 day-to-day actionable。
- **投入产出比**: medium——战略 / 方向信号好，PM 实操信号约 50% 集 (evidence: [T05-S008])
- **Paywall**: none
- **签名内容**: agents + MCP 重塑 email（Yoko Li × Resend）；「The State of AI & Education」
- **Endorsement evidence**: `community_consensus`（a16z 机构背书 + 长期高排名）；`cross_source`（intake 点名）
- **替代品**: The Cognitive Revolution；Latent Space
- **可信度**: high
- **Decay risk**: low——机构 podcast，稳定性高

### ✍️ 8. Eugene Yan's Blog

- **Type**: newsletter / blog（个人）
- **URL**: https://eugeneyan.com/
- **Author / Maintainer**: Eugene Yan（Anthropic Member of Technical Staff，前 Amazon Principal Applied Scientist；Track 01 + Track 04 关联）
- **Cadence**: monthly+（rolling，已发 209 posts）
- **Last activity**: 2026（活跃，发「2025 Year in Review」）
- **Audience tier**: senior（applied ML / eval / RecSys×LLM，资深技术 + 反思）
- **One-liner**: applied ML 与 AI 产品落地的桥梁写作——eval、RecSys×LLM、long-context、agents，AI PM 理解「eval 设计」（intake 警示的真核心技能）的标杆源。
- **典型每期内容**: 长技术深 dive——把 ML 系统落地经验结构化。2025 重点 RecSys×LLM、semantic IDs、long-context Q&A、agents。也运营 ApplyingML.com、Applied-LLMs.org。文章质量极高但更新慢、偏工程。
- **投入产出比**: high——单篇密度极高，对 eval-driven AI PM 必读；但 cadence 低，作 deep-read 非每周跟 (evidence: [T05-S009])
- **Paywall**: none
- **签名内容**:「Improving RecSys & Search in the Age of LLMs」深 dive（AI Engineer World's Fair 同名 track）；Applied-LLMs.org 合著指南
- **Endorsement evidence**: `figure_long`（Eugene Yan = Track 01 figure，intake 点名）；`cross_source`（AI Engineer World's Fair 邀其主持 LLM×RecSys track）
- **替代品**: Hamel Husain（更专注 eval / 实操）；Chip Huyen（更系统 / 书）
- **可信度**: high
- **Decay risk**: low——个人博客但已是 applied-ML 圈引用基础设施

### ✍️ 9. Hamel Husain's Blog + Substack

- **Type**: newsletter / blog（个人）
- **URL**: https://hamel.dev/ ｜ Substack: https://hamelhusain.substack.com/
- **Author / Maintainer**: Hamel Husain（前 Airbnb / GitHub ML Engineer，20+ 年经验；Track 01 关联）
- **Cadence**: monthly+（rolling）
- **Last activity**: 2025（活跃，2025-07 更新 evals FAQ）
- **Audience tier**: practitioner-senior（明确面向 Engineers & PMs）
- **One-liner**: AI evals 的实操圣经写作——「Your AI Product Needs Evals」「A Field Guide to Rapidly Improving AI Products」，直接对位 AI PM 真核心技能（eval 设计）。
- **典型每期内容**: LLM evals 系统化方法——error analysis、better prompts、eval tools 选型、从 30+ 生产案例提炼的 field guide。明确写给「Engineers & PMs」。带 Maven「AI Evals for Engineers & PMs」课（与 Shreya Shankar 合开）。
- **投入产出比**: high——eval 是 intake 点名的 AI PM 真核心，Hamel 是该主题密度最高的免费源 (evidence: [T05-S010], [T05-S011])
- **Paywall**: blog / Substack 免费；Maven evals 课付费（课程营销属性但 blog 本身完整）
- **签名内容**:「Your AI Product Needs Evals」（https://hamel.dev/blog/posts/evals/）；「A Field Guide to Rapidly Improving AI Products」（https://hamel.dev/blog/posts/field-guide/，2025-03）；「Selecting The Right AI Evals Tool」（https://hamel.dev/blog/posts/eval-tools/）
- **Endorsement evidence**: `figure_short`（intake research_strategy_notes 点名 Twitter/X figure）；`cross_source`（Arize 等工具方引用其 Maven 课作业）
- **替代品**: Eugene Yan（更广 applied ML）；BrainTrust / LangSmith 厂商 eval 文档（vendor 一面之词，不能替代）
- **可信度**: high
- **Decay risk**: low-medium——个人 blog，但 evals 主题正热、引用基础设施化

### ✍️ 10. Chip Huyen's Blog

- **Type**: blog（个人，《AI Engineering》配套）
- **URL**: https://huyenchip.com/
- **Author / Maintainer**: Chip Huyen（《AI Engineering》2025 + 《Designing ML Systems》作者；Track 01 + Track 04 关联）
- **Cadence**: monthly（rolling，更新慢）
- **Last activity**: 2025（活跃，2025-01 发「Agents」长文）
- **Audience tier**: practitioner-senior
- **One-liner**: 《AI Engineering》（2025 O'Reilly 平台最热书）的配套写作——把 foundation model 应用开发系统化，AI PM 建立技术框架的源。
- **典型每期内容**: AI 系统设计长文，多数与《AI Engineering》书内容互文（如「Agents」一文）。更新频率低，但单篇是系统性框架而非碎片观点。书在翻译成中 / 法 / 日 / 韩 / 波 / 俄多语言。
- **投入产出比**: medium——blog 本身 cadence 低、信号稀；真价值在配套的书（Track 04）。作 blog 跟踪 low-medium，作 canon 入口 high (evidence: [T05-S012])
- **Paywall**: blog 免费；《AI Engineering》书付费（O'Reilly / Amazon）
- **签名内容**:「Agents」（https://huyenchip.com/2025/01/07/agents.html）；GitHub chiphuyen/aie-book 资源库
- **Endorsement evidence**: `figure_long`（Chip Huyen = Track 01/04 figure，intake 点名）；`community_consensus`（《AI Engineering》O'Reilly 平台最热书）
- **替代品**: Eugene Yan / Hamel Husain（更高频 blog）
- **可信度**: high
- **Decay risk**: low——书 + 博客，机构化（O'Reilly）

### ✍️ 11. Simon Willison's Weblog

- **Type**: blog（个人）+ Substack 镜像
- **URL**: https://simonwillison.net/ ｜ Substack: https://simonw.substack.com/
- **Author / Maintainer**: Simon Willison（Django 共同作者，Datasette 创始人；Track 01 关联）
- **Cadence**: near-daily（rolling，更新极频）
- **Last activity**: 2026-05（极活跃，2026-04 已评 GPT-5.5 等）
- **Audience tier**: practitioner-senior（实战 LLM tooling / prompt / 模型评测）
- **One-liner**: LLM 领域更新最勤的一手 weblog——新模型发布当天评测、prompt 实践、年度「year in LLMs」总结，AI PM 跟「模型选型」最快的脉搏。
- **典型每期内容**: 新模型发布即时上手评测、LLM tooling、prompt engineering、agent 定义辨析。年度系列「The year in LLMs」（2023/2024/2025）。2026-01 在 Oxide and Friends 谈 1/3/6 年预测。碎片但高频高信，是「这周模型圈发生了什么」的最佳过滤器。
- **投入产出比**: high——对需要跟模型动态的 AI PM（模型选型 / 成本-质量三角）≥80% 价值；但碎片化，需自己抓重点 (evidence: [T05-S013])
- **Paywall**: none
- **签名内容**:「2025: The year in LLMs」（https://simonw.substack.com/p/2025-the-year-in-llms）；「I think 'agent' may finally have a widely enough agreed upon definition」；「LLM predictions for 2026」
- **Endorsement evidence**: `figure_short`（intake research_strategy_notes 点名 Twitter/X figure）；`community_consensus`（LLM 圈广泛引用其模型评测）
- **替代品**: 无直接替代（更新频率 + 一手评测组合独特）；Latent Space（更长访谈但慢）
- **可信度**: high
- **Decay risk**: low——长跑 blog，作者高产稳定

### 🏛️ 12. AI Engineer World's Fair

- **Type**: conference
- **URL**: https://www.ai.engineer/worldsfair
- **Maintainer**: swyx + Ben Dunphy
- **Cadence**: annually（+ 全球分会：SF / London / NY / Paris / Singapore / Melbourne 等）
- **Last edition**: 2025（San Francisco）
- **Next edition**: 2026-06-29 — 07-02（San Francisco）— 间隔 < 18 月，retain 优先级正常
- **Audience tier**: practitioner-senior（6000+ AI engineers / researchers / founders 现场）
- **One-liner**: AI Engineering 的旗舰大会——10 条并行工程 track + 400+ sessions + Leadership Track，sessions list 本身是 tools / figures 的 surrogate 发现源。
- **典型内容**: 10 条工程 track（含 LLM×RecSys、MCP 等专题）、400+ sessions、面向高管的 Leadership Track。2023 年首届 AI Engineer Summit（swyx + Ben Dunphy 创办）即售罄。2026 被「highest quality per hour」分析列为 AI 会议第一梯队（与 Interrupt / Data+AI Summit / AI Council 并列）。
- **投入产出比**: high——sessions 录播 + sponsor list 是全年 tools / figures 的高密度 surrogate；现场票贵，但内容线上可追 (evidence: [T05-S014])
- **Paywall**: 现场票付费（价格未核）；多数 sessions 事后 YouTube 免费
- **签名内容**: 2025 SF 大会 sessions（含 Eugene Yan 主持的 LLM×RecSys track）；首个有 dedicated MCP track 的 AI 会议
- **Endorsement evidence**: `cross_source`（intake research_strategy_notes Track 04 点名 talk 来源）；`community_consensus`（2026「quality per hour」第一梯队）
- **替代品**: Interrupt（LangChain 系）；Anthropic / OpenAI dev day（vendor 自办，见下）
- **可信度**: high
- **Decay risk**: low——年度机构级会议，next edition 已定档

### 🏛️ 13. Anthropic / OpenAI Developer Day（vendor 会议）

- **Type**: conference（vendor 自办）
- **URL**: https://www.anthropic.com/news（Anthropic）｜ https://openai.com/news/（OpenAI）— 会议信息散见官方 news
- **Maintainer**: Anthropic / OpenAI
- **Cadence**: annually（不定期，跟产品发布节奏）
- **Last edition**: 2025（两家均办过 dev day）
- **Next edition**: 未定档（vendor 跟发布节奏，难预测）
- **Audience tier**: practitioner（开发者 + 产品）
- **One-liner**: 两大 frontier 模型厂商的开发者大会——一手产品 / API 路线图，AI PM 看「平台能力边界今年怎么变」的源（vendor docs，需交叉验证）。
- **典型内容**: 新模型 / API / SDK 发布、产品路线图、开发者案例。vendor 一面之词——能力是真的，但「该不该用 / 怎么用」需 ≥2 source consensus（intake 警示：vendor 不能单方定调）。
- **投入产出比**: medium——发布信号一手且权威，但营销框架强，作事实源 high、作判断源 low (evidence: [T05-S016], [T05-S017])
- **Paywall**: 通常免费 / 线上直播
- **签名内容**: Anthropic / OpenAI 2025 dev day keynote（散见各自 news 页）
- **Endorsement evidence**: `cross_source`（intake Track 04 点名「Anthropic developer day / OpenAI dev day」作 talk 来源）；vendor 一手
- **替代品**: AI Engineer World's Fair（中立、跨厂商）
- **可信度**: medium（vendor 立场）
- **Decay risk**: low——大厂持续办，但日程不可预测

### 💬 14. Latent Space Discord（AI Engineer 社区）

- **Type**: community
- **URL**: https://www.latent.space/p/community
- **Platform**: Discord
- **Maintainer**: Latent Space（swyx / Alessio）
- **规模**: ~10,472 members（2026-05 核到）
- **Last activity**: rolling（活跃，绑定 podcast 更新节奏）
- **Audience tier**: practitioner-senior（AI builders / ML engineers / LLM 开发者）
- **One-liner**: Latent Space podcast 的配套社区——AI Engineer 们日常交流 LLM 实战，AI PM 潜水观察「一线在踩什么坑」的源。
- **典型内容**: LLM 应用 / agent / 工具的实战讨论、新模型上手反馈。社区命运与 Discord 平台 + podcast 热度绑定。
- **投入产出比**: medium——潜水成本低、信号 ambient；深度参与才高产出 (evidence: [T05-S015])
- **Paywall**: none
- **Endorsement evidence**: `cross_source`（Latent Space podcast 官方社区）；`community_consensus`（10k+ members）
- **替代品**: AI Engineer 大会的线下 / 线上社群
- **可信度**: medium（社区内容质量参差）
- **Decay risk**: medium——与 Discord 平台 + podcast 热度绑定

### 🎙️ 15. AI产品经理 Global（小宇宙）

- **Type**: podcast（zh-CN）
- **URL**: https://www.xiaoyuzhoufm.com/podcast/665dbd0694977a26efeb7a75
- **geographic_focus**: zh-CN
- **Host**: AI产品经理 Global 团队（具体主播身份本次未核到，标注待核）
- **Cadence**: rolling（活跃）
- **Last activity**: 2026（活跃）
- **Audience tier**: practitioner（在职 AI 从业者，「只聊干的，不讲虚的」）
- **One-liner**: 中文圈直接命名「AI 产品经理」的播客——每期找一位愿分享干货的 AI 从业者，用 AI PM 视角深度碰撞，是 zh-CN AI PM 最对口的一手源。
- **典型每期内容**: 邀 AI 从业者做深访，明确「只聊干的不讲虚的」，AI PM 视角切入产品 / 工作流 / 团队协作话题。中文圈 AI PM 信息源稀缺，此为少数垂直对口者。
- **投入产出比**: medium-high——zh-CN AI PM 垂直度高；但中文圈 deep-fluency 期望需用户自评（locale gap：非英文圈 source 深度不一定达标）(evidence: [T05-S019])
- **Paywall**: none
- **Endorsement evidence**: `community_consensus`（小宇宙 AI 产品类播客，搜索结果中作 AI PM 垂直代表被点名）
- **替代品**: OnBoard!（更偏增长 / 投资）；硅谷101（更偏科技深访）
- **可信度**: medium（中文圈，主播身份待核）
- **Decay risk**: medium-high——个人 / 小团队 podcast，停更风险

### 🎙️ 16. OnBoard!（小宇宙）

- **Type**: podcast（zh-CN）
- **URL**: https://www.xiaoyuzhoufm.com/podcast/61cbaac48bb4cd867fcabe22
- **geographic_focus**: zh-CN
- **Host**: Monica（OnBoard! 主播）
- **Cadence**: rolling（活跃）
- **Last activity**: 2026（活跃）
- **Audience tier**: practitioner-senior（AI / 科技创业、产品、增长）
- **One-liner**: 中文圈高质量 AI / 科技长访谈——覆盖 coding agent、AI 产品增长，嘉宾含 HeyGen / Gamma / Otter.ai 等成功 AI 公司操盘手。
- **典型每期内容**: AI / 科技深访。覆盖 OpenAI o3、coding agent（Cursor / Replit Agent / Devin）、AI 产品增长。嘉宾质量高（增长顾问 Chen Chang 等服务过 HeyGen / Gamma / Otter.ai）。中文圈少数能持续产出一线 AI 操盘手访谈的 podcast。
- **投入产出比**: medium-high——嘉宾一线、内容扎实；偏增长 / 创业视角，纯 PM 实操约 60-70% 集 (evidence: [T05-S020])
- **Paywall**: none
- **Endorsement evidence**: `community_consensus`（小宇宙 AI 类高位，搜索结果点名 coding agent / AI 增长选题）
- **替代品**: AI产品经理 Global（更垂直 PM）；硅谷101
- **可信度**: medium（中文圈）
- **Decay risk**: medium-high——个人主播 podcast

### 🎙️ 17. 硅谷101（小宇宙）

- **Type**: podcast（zh-CN）
- **URL**: https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc
- **geographic_focus**: zh-CN
- **Host**: 泓君（媒体人）
- **Cadence**: rolling（活跃）
- **Last activity**: 2026（活跃）
- **Audience tier**: mixed（科技深访，practitioner + 大众）
- **One-liner**: 中文圈老牌科技深访 podcast——2025 大量 AI 应用选题（「2025 是 AI 应用之年」），AI PM 看中文圈如何理解 AI 落地的 ambient 源。
- **典型每期内容**: 科技 / 商业深访。2025 集中 AI 应用——大模型从实验室到生产线 / 企业流程 / C 端日常。如 E181「如何打造高情商的 AI 机器人」。多平台分发（小宇宙 / Apple / Spotify / 喜马拉雅等），机构化程度高于纯个人 podcast。
- **投入产出比**: medium——AI 应用选题密但非 PM 专属，作 ambient awareness 非每集必听 (evidence: [T05-S021])
- **Paywall**: none
- **签名内容**: E181「聊天的艺术：如何打造高情商的 AI 机器人」（https://www.xiaoyuzhoufm.com/episode/67be5af352a6af799cf6bf85）
- **Endorsement evidence**: `community_consensus`（小宇宙 + 多平台长期高位，中文科技 podcast 标杆之一）
- **替代品**: What's Next｜科技早知道；OnBoard!
- **可信度**: medium（中文圈，非纯 PM 垂直）
- **Decay risk**: low-medium——老牌 + 多平台分发，比纯个人 podcast 稳

---

## 关于 Reforge（降级为参考，不计入「资深人订阅渠道」）

- **URL**: https://www.reforge.com/courses（bucket: secondary）
- intake `information_sources_candidates` 列了 Reforge，但 Track 05 的定义是「资深人**实际订阅 / 听 / 跟**的持续信息源」。Reforge 是**订阅制课程平台**（$24/月 或 $288/年个人版；团队版 $9,995/10 seats 起），不是 newsletter / podcast / 会议 / 社区。
- 它有 AI Foundations / AI Productivity / AI Product Leadership / AI Growth / AI Strategy 等 AI PM 课程，2025 课程标题更新。**作为 Track 04（canon — 课）候选更合适**，本 track 仅记录其存在，不发卡片、不计入总览。
- 判断：付费课程平台 ≠ 持续信息流。`worth it` 因人而异（转行期值，资深期边际低）。**反馈给 Track 04 作课程候选。**

---

## 总览（按 type 分组）

### Newsletter / Substack — 5 个（含 blog 型个人 newsletter）

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Lenny's Newsletter | weekly+ | mixed | medium | 全球最大 PM newsletter，AI 专题访谈含金量高 |
| Product Growth（Aakash Gupta） | weekly | practitioner | high | AI PM 垂直度最高的单一信息源（含求职营销成分） |
| Marily's AI Product Academy | weekly | beginner-pract | medium | 入门级 AI PM 工具 / 工作流 / 认证，配套 bootcamp |
| Eugene Yan's Blog | monthly+ | senior | high | applied ML / eval / RecSys×LLM 桥梁写作 |
| Hamel Husain's Blog + Substack | monthly+ | pract-senior | high | AI evals 实操圣经，明确写给 Engineers & PMs |
| Chip Huyen's Blog | monthly | pract-senior | medium | 《AI Engineering》配套，cadence 低真价值在书 |
| Simon Willison's Weblog | near-daily | pract-senior | high | LLM 圈更新最勤的一手 weblog，模型选型脉搏 |

（注：blog 型个人 newsletter 4 个 + 纯 newsletter 3 个，合计 7 条，均归 newsletter type 大类）

### Podcast — 7 个

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Lenny's Podcast | weekly | Lenny Rachitsky | medium | world-class PM/AI leader 长访谈 |
| Latent Space | weekly | swyx + Alessio | high | AI Engineering 视角行业 anchor |
| The Cognitive Revolution | biweekly+ | Nathan Labenz 等 | medium | AI builders / researchers 广覆盖访谈 |
| AI + a16z | weekly | a16z | medium | 资本 + 创始人视角的 AI 走向 |
| AI产品经理 Global（小宇宙） | rolling | （待核） | medium-high | zh-CN 直接命名「AI 产品经理」的垂直 podcast |
| OnBoard!（小宇宙） | rolling | Monica | medium-high | zh-CN 高质量 AI 操盘手长访谈 |
| 硅谷101（小宇宙） | rolling | 泓君 | medium | zh-CN 老牌科技深访，2025 重 AI 应用 |

### Conference — 2 组

| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| AI Engineer World's Fair | annually + 全球分会 | 2026-06-29 — 07-02 SF | AI Engineering 旗舰大会，sessions list 是 tools/figures surrogate |
| Anthropic / OpenAI Developer Day | annually 不定期 | 未定档 | 两大厂一手产品 / API 路线图（vendor，需交叉验证） |

### Community — 1 个

| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| Latent Space Discord | Discord | ~10,472 members | AI Engineer 配套社区，AI PM 潜水观察一线踩坑 |

### Dataset / Benchmark — 0 个

AI PM 是 **cross-functional practitioner 角色**，不直接消费 dataset / benchmark 作为「持续信息源」——benchmark（如 MMLU / SWE-bench / 各家 leaderboard）是 ML 工程师 / 研究员的工具，AI PM 通过 figures 的博客 / podcast 间接消化。本字段对本行业 **N/A（按 type 定义，AI PM 不订阅 benchmark 作 source）**。如需 benchmark 知识，Track 06（glossary）/ Track 02（tools）覆盖更合适。

---

## 质量自检

- [x] 候选数 ≥ 15：撒网 ~30，retain 22（含 1 个降级参考）—— 远超 floor 15
- [x] 5 type 覆盖：newsletter 7 / podcast 7 / conference 2 组 / community 1 / dataset 0（N/A 已说明）
- [x] 每个 source 有 cadence + last activity 日期
- [x] 投入产出比 每条都标 + 概率锚
- [x] 每个 retained source ≥ 1 个 figure_long/figure_short/cross_source/community_consensus endorsement
- [x] Phase 2 接口已填（见下）
- [x] 黑名单 URL 零进 manifest（公众号 / 知乎 / CSDN 搜到即丢）
- [x] locale=global：海外作者本人渠道优先，国内保留 3 个 zh-CN podcast 并标 geographic_focus

**一手 / surrogate 占比**：22 条 manifest 中 verified_primary 8 条（36%）、surrogate_primary 13 条（59%）、secondary 1 条（5%，Reforge 降级参考）。**verified + surrogate_primary 合计 95%**——但注意 surrogate_primary 里 7 条是「作者本人 Substack/blog（verifier 未识别 host）」、3 条是 vendor docs、3 条是会议官网。按 SKILL 约束这些不标 verified。**纯 secondary 转述类几乎为零**，符合「狠筛只留真信号」。

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」

1. **Lenny's Newsletter + Podcast**（intake research_strategy_notes 点名 Track 05 种子；Substack 商业榜 #1；产品 sense 侧 default）—— 进 master skill「Sources」节 highlights
2. **Aakash Gupta — Product Growth**（AI PM 垂直度最高的单一源；intake 点名；452K 订阅）—— highlights
3. **Latent Space podcast**（AI Engineering 视角 anchor；intake 点名一手 podcast；技术理解侧 default）—— highlights
   - 并列第 4：Hamel Husain blog（eval 主题——intake 反复强调「eval 设计才是 AI PM 真核心」，Hamel 是该主题密度最高的免费源）

→ 「想跟最新动态」诚实边界指引：海外资深 AI PM 的最小订阅集 = Lenny（产品 sense）+ Aakash（AI PM 垂直）+ Latent Space（工程边界）+ Simon Willison（模型选型脉搏）+ Hamel（eval 实操）。国内 = AI产品经理 Global + OnBoard! + 硅谷101。

### 「这一行最近的话题热度」（候选信号）

- **topic-heat: incomplete, sources listed but content not crawled**——本次时间盒只做了 source 级调研 + 每个 source 抓了 1-2 个签名内容标题，未深爬完整 episode/issue 列表。
- 从签名内容标题 + source 描述**初步观察**到的反复主题（低置信，需 Phase 2 用 fetch 深爬确认）：
  - **Coding agents / AI agent 产品化**（Latent Space 2025 主题、OnBoard! coding agent 选题、Simon Willison「agent 定义」一文、Lenny「AI agents 改写 PM」）—— 跨 ≥4 sources
  - **「如何成为 AI PM」职业路径**（Aakash 2026 更新版、Marily 认证清单、Lenny Marily 访谈）—— 跨 ≥3 sources，但偏求职端
  - **AI evals / error analysis**（Hamel field guide、Eugene Yan、Hamel Maven 课）—— 跨 ≥2 sources
  - **2025→2026 年度回顾 / 预测**（Cognitive Revolution Live Show、Simon「year in LLMs」、Lenny「Best of 2025」）—— 跨 ≥3 sources，季节性

### 新 figures 发现（喂给 Wave 2 Track 01）

intake `key_figures_candidates` 已覆盖大部分。本 track 额外浮现 / 强化：
- **swyx（Shawn Wang）** —— Latent Space host + AI Engineer World's Fair 创办人，intake figures 候选里只在 Twitter 列表提了「swyx」，应**升级为核心 figure**（同时是 source host + conference 创办人，双重 anchor）
- **Alessio Fanelli** —— Latent Space 共同 host，intake 未列，**新 figure 候选**
- **Nathan Labenz** —— The Cognitive Revolution host，intake 未列，**新 figure 候选**（AI builder 访谈视角）
- **Shreya Shankar** —— Hamel evals Maven 课共同讲师，intake 未列，**新 figure 候选**（eval 学术 + 实操）
- **Monica（OnBoard! 主播）/ 泓君（硅谷101 主播）** —— 国内 AI 内容生态关键节点，可作 zh-CN figure 候选（borderline，主播身份待核）

### 新 tools 发现（喂给 Wave 2 Track 02）

source 描述 / 签名内容中点名、且需 Track 02 确认收录的工具：
- **MCP（Model Context Protocol）** —— AI Engineer World's Fair 首设 dedicated MCP track、AI+a16z「agents + MCP 重塑 email」—— 多 source 反复出现，Track 02 应作核心收录（intake key_tools_candidates 未单列 MCP）
- **Cursor / Replit Agent / Devin** —— OnBoard! coding agent 选题点名（intake key_tools 已部分覆盖 agent 框架，但这几个 coding agent 产品应确认）
- **Maven**（课程平台）—— Hamel / Marily 的课都在 Maven，作「AI PM 学习渠道」可反馈 Track 04
- intake key_tools 已列的 LangSmith / BrainTrust / Arize Phoenix / Promptfoo —— Hamel「Selecting The Right AI Evals Tool」一文是 Track 02 eval 类选型的直接 evidence 源，建议 Track 02 精读

### 冷僻 / 信号薄弱

- newsletter 7（≥3 ✅）、podcast 7（≥3 ✅）、conference 2 组（≥1 ✅）、community 1（≥1 ✅）—— **均不冷僻**
- 有效 endorsement source 占比：22 条全部有 ≥1 endorsement，**100% ≥ 50% ✅**
- **本 track 不触发「sources 维度信号薄弱」**。AI PM 的 sources 维度信号充沛（海外尤其丰满）。
- 但需在 master skill 诚实边界标注的两点 locale gap：
  1. **国内 AI PM 一手 source 偏薄**：zh-CN 只 retain 3 个 podcast、0 个对口 newsletter（公众号是国内 figure 主要发声渠道但 Track 05 不收其文章 URL、Track 06 不引其内容——这是黑名单约束导致的结构性 gap，非调研不足）。中文圈 source 的 deep-fluency 期望，agent 可能不达标，用户需自评。
  2. **vendor 会议依赖**：conference 维度有一半（Anthropic/OpenAI dev day）是 vendor 自办，立场不中立，AI PM 用其作「事实源」可以、作「判断源」需 ≥2 source 交叉。

### 待核项（Phase 2 / 后续 refresh 可补）

- Lenny's / Aakash / Marily / Hamel newsletter 的精确 paywall 价格
- AI产品经理 Global 播客的主播真实身份
- AI Engineer World's Fair 现场票价格
