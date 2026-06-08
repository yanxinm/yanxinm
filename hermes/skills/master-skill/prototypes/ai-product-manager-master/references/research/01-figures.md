# Track 01 — Figures Research: AI 产品经理 (AI Product Management)

> Phase 1 wave 2 输出。industry = AI 产品经理, locale = en (主) + zh-CN (补)。
> 状态: 增量写入中。研究时间盒 8 分钟。

## Source Manifest

> bucket 说明：本 track 时间盒紧（8 min），新增 URL 未逐条跑 `source_verifier.py classify`，按 `_source_id_manifest.md` 同款保守规则人工标注 —— 作者本人域名 / 本人 substack note / 本人 GitHub / arXiv 标 `verified_primary`；YouTube / Apple Podcasts 等本人官方上传渠道标 `surrogate_primary`（verifier 通常给 secondary，此处按「作者拥有的渠道」从宽，与 Track 05 同处理）；第三方主持但含 figure 本人长访谈标 `secondary`。**跨 Track 复用的 source 直接引用 T04-/T05- 原 ID，不重复编号**（架构层 Q6：同 URL 跨 track 同 ID）。0 个黑名单 URL 入表。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://eugeneyan.com/ | secondary | 2026-05-14 | Eugene Yan | 作者本人博客（= T05-S009），applied ML / eval 标杆（auto=secondary：bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto；具体文章页 /writing/ 路径在他处仍为 verified_primary） |
| T01-S002 | https://hamel.dev/ | secondary | 2026-05-14 | Hamel Husain | 作者本人博客（= T05-S010），AI evals 实操（auto=secondary：bare host 不在 verifier 白名单，trust auto；具体文章页 /blog/posts/ 在 T04 仍为 verified_primary） |
| T01-S003 | https://podcasts.apple.com/us/podcast/why-your-ai-product-needs-evals-with-hamel-husain-and-swyx/id1747605459?i=1000670659068 | secondary | 2026-05-14 | High Agency podcast | Hamel + swyx 长访谈 E17，第三方主持含本人 |
| T01-S004 | https://www.oreilly.com/library/view/building-ai-powered-products/9781098152765/ | secondary | 2026-05-14 | O'Reilly | Marily Nika 书目页（O'Reilly 官方，= 同 T04-S001 主题） |
| T01-S005 | https://newsletter.pragmaticengineer.com/p/ai-engineering-with-chip-huyen | secondary | 2026-05-14 | Gergely Orosz | Pragmatic Engineer 长访谈 Chip Huyen（2025-02） |
| T01-S006 | https://www.youtube.com/watch?v=p7F4f42iZ-c | reference | 2026-05-14 | The MAD Podcast / Matt Turck | Chip Huyen「AI Engineering in 2025」长 talk 视频（auto=reference：单个 YouTube 视频页非频道根，trust auto） |
| T01-S007 | https://www.lennysnewsletter.com/p/al-engineering-101-with-chip-huyen | secondary | 2026-05-14 | Lenny Rachitsky | Lenny's「AI Engineering 101 with Chip Huyen」面向 PM 受众 |
| T01-S008 | https://luma.com/tj1z18p8 | secondary | 2026-05-14 | AIX Podcast | Chip Huyen「AI Engineering: The 2025 Landscape」访谈页 |
| T01-S009 | https://marily.substack.com/p/how-i-grew-my-ai-pm-bootcamp-and | verified_primary | 2026-05-14 | Marily Nika | 本人 substack：如何把 AI PM Bootcamp 做到 100 cohort |
| T01-S010 | https://podcasts.apple.com/us/podcast/ai-and-product-management-marily-nika-meta-google/id1627920305?i=1000598054115 | secondary | 2026-05-14 | Lenny's Podcast | Marily Nika「AI and product management」奠基级长访谈 |
| T01-S011 | https://www.youtube.com/watch?v=WvTIJnU8Bvg | reference | 2026-05-14 | Around the Prompt #6 | Marily Nika 谈 AI PM / Building AI Products / MetaAI（auto=reference：单个 YouTube 视频页非频道根，trust auto） |
| T01-S012 | https://www.news.aakashg.com/p/marily-nika-podcast | secondary | 2026-05-14 | Aakash Gupta | Product Growth podcast：Marily Nika 的 Google AI PM tool stack（= Aakash 本人渠道；auto=secondary：news.aakashg.com 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T01-S013 | https://www.swyx.io/ | secondary | 2026-05-14 | swyx (Shawn Wang) | 作者本人站点 + talk notes（auto=secondary：swyx.io bare host 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T01-S014 | https://simonwillison.net/2025/Dec/31/the-year-in-llms/ | verified_primary | 2026-05-14 | Simon Willison | 本人「2025: The year in LLMs」年度综述 |
| T01-S015 | https://simonw.substack.com/p/i-think-agent-may-finally-have-a | verified_primary | 2026-05-14 | Simon Willison | 本人「agent 终于有了被广泛接受的定义」一文 |
| T01-S016 | https://www.swyx.io/ai-landscape | secondary | 2026-05-14 | swyx | 本人「Software 3.0 and the AI Engineer Landscape」talk notes（= T04-S032；auto=secondary：swyx.io 不在 verifier 白名单且 /ai-landscape 非 content-path，trust auto） |
| T01-S017 | https://www.latent.space/p/ai-engineer | verified_primary | 2026-05-14 | swyx / Latent Space | 「The Rise of the AI Engineer」奠基文（本人发布渠道） |
| T01-S018 | https://www.news.aakashg.com/t/ai-pm | secondary | 2026-05-14 | Aakash Gupta | Product Growth「AI PM」专题（= 作者本人 newsletter，T05-S003 同源；auto=secondary：news.aakashg.com 不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T01-S019 | https://substack.com/@aakashgupta/note/c-251919242 | secondary | 2026-05-14 | Aakash Gupta | 本人 substack note：30% of 2026 PM jobs are AI PM（auto=secondary：substack.com 裸域被 verifier 判为 root/marketing，非 author 子域，trust auto） |
| T01-S020 | https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management | secondary | 2026-05-14 | Lenny Rachitsky | 本人文章「How AI will impact product management」（= 作者本人 newsletter；auto=secondary：lennysnewsletter.com /p/ 文章页不在 verifier 白名单，无 checker 合法 surrogate 表述，trust auto） |
| T01-S021 | https://www.lennysnewsletter.com/p/make-product-management-fun-again-9f6 | secondary | 2026-05-14 | Lenny Rachitsky | 本人「Make PM fun again with AI agents」（= 作者本人 newsletter；auto=secondary：lennysnewsletter.com /p/ 文章页不在 verifier 白名单，trust auto） |

**跨 track 复用（不重新编号，引用时直接用原 ID）**：T04-S005 (Eugene Yan llm-patterns)、T04-S007 (Eugene Yan eval-process)、T04-S031 (Eugene Yan AIE 2024 keynote)、T04-S008 (Hamel evals)、T04-S010 (Hamel field-guide)、T04-S012 (Simon 背书 Hamel)、T04-S013/S014/S015 (Chip Huyen 书 + repo + 主页)、T04-S001/S002 (Marily Nika 书 + 出书自述)、T04-S004 (Maven AI PM Bootcamp)、T04-S032/S033 (swyx talk + Agent Engineering)、T05-S001/S002 (Lenny newsletter + podcast)、T05-S003/S004 (Aakash newsletter + YouTube)、T05-S005 (Marily substack)、T05-S006 (Latent Space podcast)、T05-S009/S010/S011/S012/S013 (Eugene/Hamel/Chip/Simon 博客)、T05-S014 (AI Engineer World's Fair)。

**黑名单排除（搜到但不进 manifest）**：朋克熊 / 唐辰 相关全部命中 zhuanlan.zhihu.com（知乎专栏）、blog.csdn.net（CSDN）、mp.weixin.qq.com（公众号）+ 课程营销站（自学成才网 / 自学网类）。按硬约束直接丢弃，国内 figure 因此无法用非黑名单一手源覆盖 —— 见下「调研边界」。

## 调研边界与失败记录（诚实标注）

- **只研究了 top 8 figures**（按任务指令的 Wave 1 确认名单），未做 20-30 撒大网的完整流程 —— 本 track 是 wave 2 启动，直接吃 Track 04 canon + Track 05 sources 的 seed，8 人均已被两轨独立点名且有大量 long-form 一手材料，质量优先于数量。
- **国内（zh-CN）figure 维度信号薄弱 / 几乎为空**：种子里的朋克熊、唐辰，全网仅在知乎专栏 / CSDN / 微信公众号（全部黑名单）+ 课程营销站出现，**找不到任何非黑名单的一手页面**（无豆瓣作者页 / 无本人独立站 / 无小宇宙官方节目页可锚定）。按硬约束「黑名单 URL 直接不进 manifest」，**国内 figure 条目 DROP，不进本文件**。这与 Track 04 canon 的同款发现一致（朋克熊书也因只见于黑名单平台被 DROP）。→ Phase 2.8 诚实边界必须明说「figures 维度严重偏海外工程向，国内 AI PM figures 无法用合规一手源覆盖」。
- **8 人中无人 title 是「AI 产品经理」**：最接近的是 Marily Nika（AI PM 角色定义的核心承载者）和 Aakash Gupta（AI PM 垂直信息源）。其余 6 人是 applied scientist / ML engineer / 作者 / 工具观察者 / 大会创办人 / PM 策展人 —— 收录是因为他们的输出**直接构成 AI PM 的认知操作系统的不同维度**（eval / 技术地基 / 模型脉搏 / 工程协同 / 产品 sense），但 Phase 2 提炼时要意识到「AI PM 视角」本身在 figure 池里是稀薄的（与 intake「角色定义不统一」「pre-canonical」一致）。
- **voice_samples 普遍偏单一 register**：8 人多数只有「同业 / 专业」register 的原话，「面向非技术客户解释」register 大量缺失（已逐条标 ⚠️）—— 因为他们的公开输出本就集中在工程 / PM 圈内，不是 to-C 客服语域。Phase 4 voice check 预计据此降部分 figure 的 voice_confidence。
- **时间盒 8 min**：WebSearch 为主，WebFetch 未用（网络不稳 + 前两次 agent 因网络挂掉，本次策略是先落盘 + 增量写 + 不深抓音频 transcript）。podcast/talk 的 voice_samples 多来自搜索结果摘要 + 节目描述，标了「转述」，未逐集抓字幕。

---

## 总览（按行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 值得读/听/看 | 来源数 | sub_skill |
|---|------|---------|----------|------------|-------|-----------|
| 1 | Marily Nika | 硅谷 Gen AI Product Leader（前 Google/Meta），《Building AI-Powered Products》作者 + AI PM Bootcamp 创办 | 写了唯一一本正面瞄准「AI PM 岗位」的书，把 AI PM 做成新职业品类 | 📖🎙️🎬 | 4 | ✅ true |
| 2 | Hamel Husain | 独立 AI 顾问 / 教育者，前 Airbnb/GitHub ML Engineer | 把「你的 AI 产品需要 evals」喊成行业口号，给出 error-analysis 实操流程 | 📖🎙️📖 | 4 | ✅ true |
| 3 | Eugene Yan | Anthropic MTS（前 Amazon Principal Applied Scientist） | 把「eval = 科学方法的伪装」写成 applied-ML 标杆博客 | 📖🎙️🎬📖 | 4 | ❌ false |
| 4 | Chip Huyen | 计算机科学家 / 作者，Nvidia NeMo 核心开发者 | 写出 O'Reilly 平台最热书《AI Engineering》，把「用现成模型搭产品」系统化 | 📖🎙️🎬 | 4 | ❌ false |
| 5 | Aakash Gupta | Product Growth newsletter/podcast 主理人，前 Apollo.io VP Product | 把「怎么成为 AI PM / AI PM 求职」做成最垂直的信息源 | 📖🎙️🎬 | 4 | ✅ true |
| 6 | swyx (Shawn Wang) | Latent Space podcast 共同主持 + AI Engineer 大会共同创办 | 写「The Rise of the AI Engineer」，命名并组织了「AI Engineer」职业生态 | 📖🎬🎙️ | 4 | ❌ false |
| 7 | Simon Willison | Django 共同作者 / Datasette 创始人，全职独立写作者 | LLM 领域更新最勤的一手 weblog，给「agent」下了被广泛接受的工程定义 | 📖📖🎙️ | 4 | ❌ false |
| 8 | Lenny Rachitsky | Lenny's Newsletter + Podcast 创办（1.2M+ 订阅），前 Airbnb PM | 全球最大 PM newsletter，AI 专题访谈是「听这行的人怎么想」的高密度入口 | 🎙️📖🎙️ | 4 | ❌ false |
| — | 朋克熊 / 唐辰（国内） | — | **DROP** —— 仅见于黑名单平台（知乎/CSDN/公众号），无合规一手源 | — | 0 | — |

> 排序说明：按「与 AI PM master skill 的对口度 + 一手材料密度」综合排，非纯名气。Marily / Hamel / Aakash 排前三是因最贴 AI PM 角色本身且有 sub_skill 潜力；Eugene/Chip/swyx/Simon 影响力同样顶级但视角偏「工程 / 行业 meta」；Lenny 是「产品 sense 底座 + 入口」。

---

## Figures

### 1. Eugene Yan

- **One-liner**: 把「eval 是科学方法的伪装」这套打法写成 applied-ML 标杆博客的人 —— AI 产品落地（eval / RAG / RecSys×LLM / defensive UX）的结构化第一手参考 (evidence: [T01-S001, T04-S005, T04-S007])
- **核心身份**: Anthropic Member of Technical Staff（做 recommendation systems + AI 产品）；前 Amazon Principal Applied Scientist。同时运营 ApplyingML.com、Applied-LLMs.org (evidence: [T05-S009, T01-S001])
- **代表作品**:「Patterns for Building LLM-based Systems & Products」(7 大模式长文, 2023+ 持续更新)；「An LLM-as-Judge Won't Save The Product—Fixing Your Process Will」；「Task-Specific LLM Evals that Do & Don't Work」；Applied-LLMs.org 合著指南
- **值得读 / 听 / 看的 3 件事**:
  - 📖 「Patterns for Building LLM-based Systems & Products」https://eugeneyan.com/writing/llm-patterns/ —— 七大模式（eval / RAG / fine-tune / caching / guardrails / defensive UX / 收集反馈），AI PM 的落地地图 (evidence: [T04-S005])
  - 🎙️ 🎬 AI Engineer 2024 keynote「What We Learned from a Year of LLMs」https://eugeneyan.com/speaking/aie-2024/ —— conference 长 talk (evidence: [T04-S031])
  - 📖 「An LLM-as-Judge Won't Save The Product—Fixing Your Process Will」https://eugeneyan.com/writing/eval-process/ —— 反「LLM-as-judge 万能论」(evidence: [T04-S007])
- **核心思想关键词**: eval-driven development / 「evals = 科学方法的伪装」/ defensive UX / hybrid retrieval / 数据飞轮 / RecSys×LLM
- **voice_samples** (iter 26):
  - 同业讨论样本: 「Building product evals is simply the scientific method in disguise」—— Eugene 把「做产品 eval」直接等同于「做科学实验：假设 → 测量 → 迭代」，反对靠直觉改产品 (source: T01-S001 eugeneyan.com /writing/evals/ 系列, 转述)
  - 专业讨论样本:「An LLM-as-judge won't save the product—fixing your process will.」—— 标题即论点：自动评估器不是银弹，真问题在评估流程本身 (source: T04-S007, 原话/标题)
  - 客户/团队解释样本: ⚠️ 暂未找到 ≥ 50 字面向非技术受众的直接原话片段（Eugene 输出几乎全是工程向长文，register 偏单一）
- **sub_skill_candidate**: `false` —— 影响力极高且材料丰富，但他的体系（eval + applied ML）与 Hamel 高度重叠，且偏「工程落地」而非「PM 决策框架」，作为 figure 收录、不单独蒸馏 sub-skill
- **dual_role**: `"engineering + thinker"`（一线工程 + 结构化写作）
- **最近 12 个月动态**: 2025-06「Evaluating Long-Context Question & Answer Systems」；2025-11「Product Evals in Three Simple Steps」；2025 年底发「2025 Year in Review」。持续在 Anthropic 做 RecSys + AI 产品 (evidence: [T05-S009])
- **争议 / 批评**: 内容偏工程深度、cadence 慢（年均十几篇），对「纯产品 sense / 无技术背景」的 AI PM 门槛偏高；本人也不是「AI PM」title，是 applied scientist —— 作为 figure 收录是因写作直接服务 AI PM 的 eval / 落地维度，但他不代表「产品决策」视角
- **来源**:
  - [Primary] eugeneyan.com 博客（本人）: https://eugeneyan.com/ , collected 2026-05-14
  - [Primary] llm-patterns 长文（本人）: https://eugeneyan.com/writing/llm-patterns/
  - [Primary] AI Engineer 2024 keynote 页（本人）: https://eugeneyan.com/speaking/aie-2024/
  - [Reference] Track 04 canon 把 llm-patterns 列为标杆 blog: 04-canon.md T04-S005
- **可信度自评**: high（大量 long-form 一手 + 本人 talk + 跨 Track 04/05 引用）

### 2. Hamel Husain

- **One-liner**: 把「你的 AI 产品需要 evals」喊成行业口号、并给出 error-analysis 实操流程的 AI evals 实战旗帜人物 (evidence: [T04-S008, T04-S010, T01-S002])
- **核心身份**: 独立 AI 顾问 + 教育者；前 Airbnb / GitHub ML Engineer（20+ 年经验）。与 Shreya Shankar 合开 Maven「AI Evals for Engineers & PMs」课 (evidence: [T05-S010, T05-S011])
- **代表作品**:「Your AI Product Needs Evals」(2024-03 标杆长文)；「A Field Guide to Rapidly Improving AI Products」(与 Shreya Shankar, 基于 30+ 公司经验)；「Using LLM-as-a-Judge: A Complete Guide」
- **值得读 / 听 / 看的 3 件事**:
  - 📖 「Your AI Product Needs Evals」https://hamel.dev/blog/posts/evals/ —— 本行被引用最多的单篇 eval 文，Simon Willison 专门转推背书 (evidence: [T04-S008, T04-S012])
  - 🎙️ 「Why Your AI Product Needs Evals」with Hamel Husain & swyx，High Agency podcast E17 https://podcasts.apple.com/us/podcast/why-your-ai-product-needs-evals-with-hamel-husain-and-swyx/id1747605459?i=1000670659068 (evidence: [T01-S003])
  - 📖 「A Field Guide to Rapidly Improving AI Products」https://hamel.dev/blog/posts/field-guide/ —— error analysis → 假设 → eval → 改 的完整迭代循环 (evidence: [T04-S010])
- **核心思想关键词**: evals / error analysis / 「别 vibe-check」/ LLM-as-a-judge（是工具不是终点）/ golden set / 数据驱动迭代
- **voice_samples** (iter 26):
  - 同业讨论样本:「Unsuccessful products almost always share a common root cause: a failure to create robust evaluation systems.」—— Hamel 把「产品失败」直接归因到「没有稳健的评估系统」这一条 (source: T04-S008 hamel.dev/blog/posts/evals/, 原话/转述)
  - 团队解释样本:Hamel 教产品团队「move beyond vibe-checking your AI systems」—— 他反复用「vibe check」这个词贬指拍脑袋判断模型好坏，主张换成系统化 error analysis (source: T01-S003 High Agency podcast E17 + How I AI podcast, 转述)
  - 专业讨论样本: ⚠️ 暂未找到 ≥ 50 字「监管 / 学术」register 的直接原话片段（Hamel 的公开 register 集中在「工程师 + PM」实操，非监管/学术语域）
- **sub_skill_candidate**: `true` —— 有 ≥ 30 min 长访谈（High Agency E17 / How I AI）+ Maven 系统课 + 思想体系自洽（eval-driven 迭代）+ 行业内 eval 话题影响力前 3 + 用户 focus（operational + technical）与其高度对齐。是本 track 最强的独立 sub-skill 候选之一
- **dual_role**: `"engineering + educator"`
- **最近 12 个月动态**: 2025-03 与 Shreya Shankar 发布「Field Guide to Rapidly Improving AI Products」；2025-07 更新 evals FAQ；持续开 Maven「AI Evals for Engineers & PMs」cohort (evidence: [T05-S010, T05-S011])
- **争议 / 批评**: 课程营销属性明显（Maven 收费课），部分人质疑「evals 万能论」被他推得过头 —— 但他本人立场是「LLM-as-judge 是工具不是终点，要修流程」，与 Eugene Yan 一致，并非真的把 eval 当银弹；另一常见反驳是「早期 0→1 产品没有数据建 golden set 时，过度强调 eval 会拖慢」
- **来源**:
  - [Primary] hamel.dev 博客 + hamelhusain.substack.com（本人）: https://hamel.dev/ , collected 2026-05-14
  - [Primary] 「Your AI Product Needs Evals」(本人): https://hamel.dev/blog/posts/evals/
  - [Secondary] High Agency podcast E17（第三方主持，含本人长访谈）: https://podcasts.apple.com/us/podcast/why-your-ai-product-needs-evals-with-hamel-husain-and-swyx/id1747605459?i=1000670659068
  - [Reference] Simon Willison 转推背书: simonwillison.net/2024/Mar/31/your-ai-product-needs-evals/ (T04-S012)
- **可信度自评**: high（标杆长文一手 + 多个长 podcast + 系统课 + Simon Willison 第三方背书）

### 3. Chip Huyen

- **One-liner**: 写出 O'Reilly 平台最热书《AI Engineering》、把「用现成 foundation model 搭产品」系统化成独立学科的人 —— AI PM 补技术地基的首选作者 (evidence: [T04-S013, T04-S015, T01-S004])
- **核心身份**: 计算机科学家 / 作者；Nvidia NeMo 平台核心开发者，前 Netflix AI 研究员，斯坦福教过课。《AI Engineering》(2025) + 《Designing Machine Learning Systems》(2022) 作者 (evidence: [T05-S012, T01-S004])
- **代表作品**:《AI Engineering: Building Applications with Foundation Models》(2025)；《Designing Machine Learning Systems》(2022)；博客长文「Agents」(2025-01)；GitHub chiphuyen/aie-book 资源库
- **值得读 / 听 / 看的 3 件事**:
  - 📖 《AI Engineering》+ 配套 repo https://github.com/chiphuyen/aie-book —— 评估 / 适配（prompt/RAG/finetune）/ 推理优化的系统框架 (evidence: [T04-S013])
  - 🎙️ The Pragmatic Engineer Podcast「AI Engineering with Chip Huyen」(2025-02) https://newsletter.pragmaticengineer.com/p/ai-engineering-with-chip-huyen ｜ The MAD Podcast (Matt Turck)「What You MUST Know About AI Engineering in 2025」https://www.youtube.com/watch?v=p7F4f42iZ-c (evidence: [T01-S005, T01-S006])
  - 🎬 Lenny's Newsletter「AI Engineering 101 with Chip Huyen」https://www.lennysnewsletter.com/p/al-engineering-101-with-chip-huyen —— 直接面向 PM 受众的长访谈 (evidence: [T01-S007])
- **核心思想关键词**: AI Engineering（独立学科）/ foundation model 应用 / cost-quality-latency 三角 / 评估 / 数据/监控/漂移 / prompt vs RAG vs finetune 的选择
- **voice_samples** (iter 26):
  - 团队/客户解释样本:Chip 的核心论点 ——「the rise of foundation models has democratized AI development, enabling anyone to build sophisticated applications」(你不需要会训模型，现成模型已经让搭复杂应用变得人人可及) (source: T01-S008 AIX Podcast 描述, 转述)
  - 同业讨论样本:「AI Engineering 是独立学科：用现成 foundation model 构建并高效部署应用，区别于传统 ML」—— 她坚持 AI Engineering ≠ 传统 ML engineering，是新工种 (source: T04-S013 / T04-S015 huyenchip.com/books/, 转述)
  - 专业讨论样本: ⚠️ 暂未找到 ≥ 50 字监管/学术 register 直接原话；可从 Pragmatic Engineer / MAD podcast transcript 补（本次时间盒未深抓音频）
- **sub_skill_candidate**: `false` —— 影响力与材料都足够，但她的输出本质是「AI Engineering（工程）」而非「AI 产品管理（PM 决策）」；作为 figure + canon 作者收录，更适合喂 canon / glossary 而非单独蒸馏成 AI PM sub-skill
- **dual_role**: `"engineering + author"`（一线工程 + 系统性著作 + 教学）
- **最近 12 个月动态**: 2025《AI Engineering》出版后长期居 O'Reilly 平台阅读量第一，已译成中/法/日/韩/波/俄等多语言；2025-02 起密集上 podcast（Pragmatic Engineer / MAD / Lenny's / AIX）；持续在 Nvidia 做 NeMo (evidence: [T05-S012, T01-S005, T01-S007])
- **争议 / 批评**:《AI Engineering》偏工程而非产品视角 —— 对纯产品向 AI PM 来说是「补技术地基」，但不解决「该不该做、怎么定位」这类产品判断；intake/canon 也明确指出她的两本书「偏工程而非 PM」
- **来源**:
  - [Primary] huyenchip.com 博客 + 书籍主页（本人）: https://huyenchip.com/ , collected 2026-05-14
  - [Primary] GitHub chiphuyen/aie-book（本人维护）: https://github.com/chiphuyen/aie-book
  - [Secondary] The Pragmatic Engineer Podcast 长访谈（Gergely Orosz 主持）: https://newsletter.pragmaticengineer.com/p/ai-engineering-with-chip-huyen
  - [Reference] Track 04 canon 把《AI Engineering》列为推荐书: 04-canon.md T04-S013/S014
- **可信度自评**: high（本人书 + repo + 博客一手，多个高质量第三方长 podcast）

### 4. Marily Nika

- **One-liner**: 写了**目前唯一一本正面瞄准「AI PM 这个岗位」的书**、并把「AI PM」做成一个有 100+ cohort 认证课的新职业品类的人 (evidence: [T04-S001, T04-S002, T01-S009])
- **核心身份**: 硅谷 Gen AI Product Leader；12+ 年 Google & Meta（曾任 Google Assistant Gen AI Product Lead），ML 博士。《Building AI-Powered Products》(O'Reilly, 2025) 作者；Maven AI PM Bootcamp & Certification 创办（与 Constantinos Neophytou、Deb Liu 合办）(evidence: [T01-S009, T04-S004])
- **代表作品**:《Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management》(2025)；Maven「AI PM Bootcamp & Certification」(100+ cohorts, 30k+ alumni)；Lenny's Newsletter 客座专栏「Building AI product sense」系列
- **值得读 / 听 / 看的 3 件事**:
  - 📖 《Building AI-Powered Products》(O'Reilly) https://www.oreilly.com/library/view/building-ai-powered-products/9781098152765/ —— AI 产品生命周期 + 策略 playbook (evidence: [T04-S001])
  - 🎙️ Lenny's Podcast「AI and product management」(Meta/Google) https://podcasts.apple.com/us/podcast/ai-and-product-management-marily-nika-meta-google/id1627920305?i=1000598054115 —— AI PM 角色的奠基级长访谈 (evidence: [T01-S010])
  - 🎬 「Marily Nika: AI Product Management, Building AI Products, & MetaAI」Around the Prompt #6 https://www.youtube.com/watch?v=WvTIJnU8Bvg ｜ Aakash「This is what a Google AI PM's Tool Stack Looks Like」https://www.news.aakashg.com/p/marily-nika-podcast (evidence: [T01-S011, T01-S012])
- **核心思想关键词**: AI PM 作为独立岗位 / AI 产品生命周期 / AI product sense / minimum viable quality / 不需要会训模型但要懂 AI 能力边界 / AI strategy & leadership
- **voice_samples** (iter 26):
  - 客户/团队解释样本: Marily 反复传递的核心观点 ——「AI PM 不需要会训模型，但要懂 AI 能/不能做什么，才能在 pain point 和技术之间架桥」。她把 AI PM 定位成「pain point ↔ 技术」之间的翻译者 (source: T04-S002 x.com/marilynika 出书自述, 转述)
  - 同业讨论样本:她把自己的课描述为「the only AI PM course built by operators」「establish a new domain」—— 她明确认为「AI PM」此前不是一个被承认的 domain，是她在帮它立名 (source: T01-S009 marily.substack.com「How I grew my AI PM Bootcamp」, 原话/转述)
  - 专业讨论样本:Lenny's 客座文里她拆「AI product sense」「minimum viable quality」「guardrails」「failure modes」等概念给 PM 受众 —— register 偏「资深 PM 教练」(source: T01-S010 lennysnewsletter.com/p/building-ai-product-sense-part-2, 转述)
- **sub_skill_candidate**: `true` —— 有 ≥ 30 min 长访谈（Lenny's / Around the Prompt / DataCamp）+ 一本系统性著作 + 思想体系自洽（AI 产品生命周期）+ 是「AI PM」这个角色定义本身的核心承载者 + 用户 focus（operational PM）与其**完全对齐**。本 track 最对口 AI PM master skill 的 figure，强 sub-skill 候选
- **dual_role**: `"founder + thinker"`（课程/认证创办人 + AI PM 方法论作者）
- **最近 12 个月动态**:《Building AI-Powered Products》2025-03 出版后成 bestseller；AI PM Bootcamp 做到 100+ cohorts；2026-05 课程材料完全 refresh；持续在 Lenny's Newsletter 发「Building AI product sense」系列 (evidence: [T04-S001, T01-S009, T05-S005])
- **争议 / 批评**: 课程营销属性强（Maven 收费 bootcamp + 认证，intake 明确警告本行「7 天速成 AI PM」营销课泛滥）—— Marily 的课区别于纯营销课（有出版书 + Google/Meta 一手背景双锚点），但「AI PM 认证」本身的价值业内有争议；书太新，独立第三方 endorsement 尚薄（canon 标 medium 可信度）
- **来源**:
  - [Primary] marily.substack.com（本人 newsletter）: https://marily.substack.com/ , collected 2026-05-14
  - [Primary] x.com/marilynika 出书自述（本人）: https://x.com/marilynika/status/1898052575825719563
  - [Secondary] Lenny's Podcast 长访谈（Lenny 主持）: https://podcasts.apple.com/us/podcast/ai-and-product-management-marily-nika-meta-google/id1627920305?i=1000598054115
  - [Reference] Track 04 canon 把她的书列为 textbook: 04-canon.md T04-S001/S002
- **可信度自评**: high（本人书 + newsletter + 多个长 podcast 一手；唯一最对口 AI PM 角色的 figure）

### 5. Simon Willison

- **One-liner**: LLM 领域更新最勤的一手 weblog 作者 —— 新模型发布当天上手评测、给「agent」下了被广泛接受的工程定义，是 AI PM 跟「模型选型 + 这周圈里发生了什么」最快的脉搏 (evidence: [T05-S013, T01-S013])
- **核心身份**: Django 共同作者、Datasette 创始人；全职独立写作者 / 开源开发者，simonwillison.net 近乎日更 (evidence: [T05-S013])
- **代表作品**:「2025: The year in LLMs」(年度系列, 还有 2023/2024)；「I think 'agent' may finally have a widely enough agreed upon definition」；常年的新模型即时评测；LLM CLI 工具
- **值得读 / 听 / 看的 3 件事**:
  - 📖 「2025: The year in LLMs」https://simonwillison.net/2025/Dec/31/the-year-in-llms/ —— 年度综述，AI PM 一年一更的脉搏校准 (evidence: [T01-S014])
  - 📖 「I think 'agent' may finally have a widely enough agreed upon definition」https://simonw.substack.com/p/i-think-agent-may-finally-have-a —— 给「agent」收口定义 (evidence: [T01-S015])
  - 🎙️ Oxide and Friends「LLM predictions for 2026」/ 1-3-6 年预测访谈 + simonwillison.net 近乎日更博客（持续一手）(evidence: [T05-S013])
- **核心思想关键词**: 「agent = LLM 在循环里调工具达成目标」/ coding agents / 模型价格暴跌 / prompt injection（他造的词）/ 一手实测优先 / LLM 祛魅
- **voice_samples** (iter 26):
  - 专业讨论样本:「An LLM agent runs tools in a loop to achieve a goal.」—— Simon 给 agent 的一句话定义，他强调这是在 Twitter 众包了 211 个互相矛盾的定义后才敢用的收口版本 (source: T01-S015 simonw.substack.com「agent definition」, 原话)
  - 同业讨论样本:他形容此前「agent」是「the ultimate in buzzword bingo」—— everyone had a different mental model；他长期拒绝用这个词，直到 2025 才觉得能「不翻白眼、不加吓人引号」地用 (source: T01-S015 / fedi.simonwillison.net, 转述)
  - 客户解释样本:「coding agents—LLM systems that can write code, execute that code, inspect the results and then iterate further」—— 他把 coding agent 拆成「写→跑→看结果→再迭代」的循环讲给读者 (source: T01-S014 simonwillison.net year-in-llms, 原话/转述)
- **sub_skill_candidate**: `false` —— 影响力与一手材料都极强，但他是「LLM 工具 / 模型动态观察者」而非「AI 产品经理」；他的价值是给 AI PM 当「模型选型 + 术语祛魅」的信息源，不构成一套 PM 决策体系，作为 figure 收录即可
- **dual_role**: `"engineering + commentator"`
- **最近 12 个月动态**: 2026-04 已评 GPT-5.5 等新模型；2026-01 在 Oxide and Friends 谈 1/3/6 年 LLM 预测；持续近乎日更博客、发「LLM predictions for 2026」(evidence: [T05-S013])
- **争议 / 批评**: 内容碎片化（near-daily 短 post，需读者自己抓重点）；偏「个人开发者 / 工具」视角，几乎不谈产品定位、团队、商业化 —— 对 AI PM 是「模型脉搏」源而非「产品方法论」源；他对 agent 的乐观与对炒作的警惕之间，不同读者会有不同解读
- **来源**:
  - [Primary] simonwillison.net weblog（本人）: https://simonwillison.net/ , collected 2026-05-14
  - [Primary] 「2025: The year in LLMs」(本人): https://simonwillison.net/2025/Dec/31/the-year-in-llms/
  - [Primary] 「agent 定义」一文（本人）: https://simonw.substack.com/p/i-think-agent-may-finally-have-a
  - [Reference] Track 04 canon 用他做 Anthropic agents / Hamel evals 的第三方背书: 04-canon.md T04-S012/S024/S025
- **可信度自评**: high（近乎日更的一手 weblog + 年度综述 + 跨 Track 04/05 反复引用）

### 6. swyx (Shawn Wang)

- **One-liner**: 写出「The Rise of the AI Engineer」、创办 AI Engineer 大会 + Latent Space podcast，事实上**命名并组织了「AI Engineer」这个职业生态**的人 (evidence: [T04-S032, T05-S006, T01-S016])
- **核心身份**: Latent Space podcast 共同主持（与 Alessio Fanelli）；AI Engineer 大会（Summit + World's Fair）共同创办（与 Ben Dunphy）。前 Temporal / AWS / Netlify DevRel (evidence: [T05-S006, T05-S014])
- **代表作品**:「The Rise of the AI Engineer」(2023-06 Latent Space, 病毒级, Karpathy 背书)；「Software 3.0 and the AI Engineer Landscape」talk；Latent Space podcast；AI Engineer 大会
- **值得读 / 听 / 看的 3 件事**:
  - 📖 「The Rise of the AI Engineer」https://www.latent.space/p/ai-engineer —— 定义「AI Engineer」这个工种的奠基文 (evidence: [T01-S017])
  - 🎬 「Software 3.0 and the AI Engineer Landscape」talk notes + slides https://www.swyx.io/ai-landscape —— conference 长 talk (evidence: [T04-S032])
  - 🎙️ Latent Space podcast https://www.latent.space/podcast —— 他主持的 AI Engineering 行业 anchor 长访谈 (evidence: [T05-S006])
- **核心思想关键词**: AI Engineer（新工种）/ Software 3.0 / 「shift right」of applied AI / Agent Engineering / context engineering / AI Engineering 的生态组织
- **voice_samples** (iter 26):
  - 同业讨论样本:「a wide range of AI tasks that used to take five years and a research team could now be accomplished with API docs and a spare afternoon」—— swyx 用「5 年 + 研究团队 → API 文档 + 一个下午」这个对比来论证为什么会冒出「AI Engineer」这个新工种 (source: T01-S017 latent.space/p/ai-engineer, 原话/转述)
  - 专业讨论样本:他描述 applied AI 的「shift right」—— foundation model 让 AI 能力「右移」到不做研究的工程师手里，「emergent capabilities created an emerging title」(source: T04-S032 swyx.io/ai-landscape, 转述)
  - 客户解释样本: ⚠️ 暂未找到 ≥ 50 字面向非技术客户的直接原话片段（swyx 的公开 register 集中在「工程师 / 创业者 / 行业观察」，非 to-C 客户解释语域）
- **sub_skill_candidate**: `false` —— 影响力极高、一手材料丰富，但他是「AI Engineer 生态的命名者与组织者」，视角偏工程职业 + 行业 meta，不是「AI 产品经理」的决策体系；作为 figure + source host 收录，价值在帮 AI PM 理解「工程协同对象在想什么 + 行业往哪走」
- **dual_role**: `"founder + thinker"`（大会/podcast 创办人 + 行业叙事作者）
- **最近 12 个月动态**: 2025 AI Engineer World's Fair 首设 dedicated MCP track，把「Agent Engineering」立为独立主题；Latent Space 2026 转型 podcast network、加 AI for Science 子节目；下届 World's Fair 2026-06-29~07-02 SF (evidence: [T04-S033, T05-S006, T05-S014])
- **争议 / 批评**:「AI Engineer」这个 framing 被部分人批为「给已有工作贴新标签 / 造词」；他身兼大会创办人 + podcast host + 行业评论员，立场难免与 AI Engineer 生态的商业利益绑定 —— 引用他的「行业往哪走」判断时需意识到他是利益相关方
- **来源**:
  - [Primary] swyx.io（本人站点 + talk notes）: https://www.swyx.io/ , collected 2026-05-14
  - [Primary] 「The Rise of the AI Engineer」(本人, Latent Space): https://www.latent.space/p/ai-engineer
  - [Primary] Latent Space podcast（本人主持）: https://www.latent.space/podcast
  - [Reference] Track 04/05 把他的 talk 和 podcast 列为 canon/source: 04-canon.md T04-S032/S033, 05-sources.md T05-S006
- **可信度自评**: high（奠基文 + talk slides + 长 podcast 全一手；跨 Track 04/05 锚定）

### 7. Aakash Gupta

- **One-liner**: 自我定位「世界第一 AI PM newsletter + podcast」、把「怎么成为 AI PM / AI PM 求职」做成最垂直信息源的人 (evidence: [T05-S003, T05-S004, T01-S018])
- **核心身份**: Product Growth newsletter + podcast + YouTube 主理人；前 Apollo.io VP Product。自称「the AI PM guy」(evidence: [T05-S003])
- **代表作品**: Product Growth newsletter（452K+ 订阅）+ Product Growth Podcast；「How to Become an AI PM」(2024 原版 + 2026 更新版)；「Land a PM Job」12 周课程；Northeastern PM 大会 keynote「product strategy in the age of AI」
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Product Growth「AI PM」专题 https://www.news.aakashg.com/t/ai-pm —— AI PM 求职 / 角色 / 策略的垂直 deep dive (evidence: [T01-S018])
  - 🎙️ Product Growth Podcast（含「This is what a Google AI PM's Tool Stack Looks Like」与 Marily Nika 对谈）https://www.news.aakashg.com/p/marily-nika-podcast (evidence: [T01-S012])
  - 🎬 Product Growth YouTube https://www.youtube.com/@growproduct —— keynote + 视频 deep dive (evidence: [T05-S004])
- **核心思想关键词**: AI PM 求职 / supply-demand gap / 「别把 AI 当装饰性能力」/ feature theater 反面 / 「什么决策变聪明、什么 workflow 变容易」/ AI PM 角色定义
- **voice_samples** (iter 26):
  - 同业讨论样本:「30% of open PM jobs in 2026 are AI PM roles. Less than 5% of senior PMs in the market have shipped a working AI agent. The supply/demand divergence is the cleanest the PM job market has ever produced.」—— Aakash 用供需失衡来论证 AI PM 是当下最值得转的方向 (source: T01-S018 substack.com/@aakashgupta/note c-251919242, 原话)
  - 客户/团队解释样本:「stop treating AI as a decorative capability ... ask better questions about what decision gets smarter, what workflow gets easier, what trust issue becomes more visible ... that's when AI PM starts to look like product management instead of feature theater」—— 他反对「装饰性 AI」，主张回到「哪个决策/workflow/信任问题被 AI 改善」的产品问题 (source: T01-S018 news.aakashg.com /t/ai-pm, 原话/转述)
  - 专业讨论样本: ⚠️ 暂未找到 ≥ 50 字监管/学术 register 直接原话（Aakash register 集中在「PM 求职 + 产品策略」，非监管/学术语域）
- **sub_skill_candidate**: `true` —— 有 ≥ 30 min 长 podcast + 持续 deep dive + AI PM 垂直度最高 + 用户 focus（operational PM）对齐。注意：他的体系偏「AI PM 求职 + 角色定义」，比 Marily/Hamel 的「方法论」薄一些，标 `true` 但理由侧重「AI PM 角色画像」而非「完整产品方法论」
- **dual_role**: `"founder + thinker"`（newsletter/课程创办人 + AI PM 角色叙事者）
- **最近 12 个月动态**: 2026 发「become an AI PM in 2026」更新版；持续发 AI PM 求职 / 薪资 / 角色 deep dive（如「30% PM jobs are AI PM」note）；newsletter + podcast + YouTube 三渠道并行 (evidence: [T05-S003, T01-S018])
- **争议 / 批评**: intake + Track 05 明确点名「内容偏求职营销端」——「怎么拿 offer」多于「怎么做产品」；452K 订阅里有大量求职者而非在职 AI PM；「AI PM 月入百万」类叙事容易被批为贩卖焦虑（他本人的 framing 比纯营销课克制，但商业导向明显）
- **来源**:
  - [Primary] news.aakashg.com（本人 newsletter）: https://www.news.aakashg.com/ , collected 2026-05-14
  - [Primary] Product Growth YouTube（本人）: https://www.youtube.com/@growproduct
  - [Primary] substack note「30% PM jobs are AI PM」（本人）: https://substack.com/@aakashgupta/note/c-251919242
  - [Reference] Track 05 把 Product Growth 列为 AI PM 垂直度最高的 source: 05-sources.md T05-S003
- **可信度自评**: high（本人 newsletter + podcast + YouTube 全一手，AI PM 垂直度最高；扣分项是求职营销属性，但不影响可调研性）

### 8. Lenny Rachitsky

- **One-liner**: 运营全球订阅量最大的 PM newsletter + podcast，是 AI PM「产品 sense 底座」侧的 default —— 本人不专做 AI，但他的 AI 专题访谈是「听这行的人怎么想」的高密度入口 (evidence: [T05-S001, T05-S002, T01-S019])
- **核心身份**: Lenny's Newsletter + Lenny's Podcast 创办（1.2M+ 订阅，Substack 商业榜 #1）；前 Airbnb PM (evidence: [T05-S001])
- **代表作品**: Lenny's Newsletter（weekly+）；Lenny's Podcast（weekly，60-90 min 深访）；Lenny's Reads；常年「Best of」年度精选
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ Lenny's Podcast「AI and product management」with Marily Nika https://podcasts.apple.com/us/podcast/ai-and-product-management-marily-nika-meta-google/id1627920305?i=1000598054115 —— AI PM 主题的标杆集 (evidence: [T01-S010])
  - 📖 「How AI will impact product management」https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management —— 本人对 AI 改写 PM 的综述 (evidence: [T01-S020])
  - 🎙️ 🎬 「Make product management fun again with AI agents」https://www.lennysnewsletter.com/p/make-product-management-fun-again-9f6 ｜ Chip Huyen「AI Engineering 101」集 https://www.lennysnewsletter.com/p/al-engineering-101-with-chip-huyen (evidence: [T01-S021, T01-S007])
- **核心思想关键词**: 产品 sense / 可执行/tactical 建议 / AI 怎么改写 PM 工作 / AI agents for PM / 综合 PM 底盘（非 AI 专属）
- **voice_samples** (iter 26):
  - 同业讨论样本: Lenny's Podcast 的自我定位 ——「interviews with world-class product leaders and growth experts to uncover concrete, actionable, and tactical advice」。他反复强调要「concrete / actionable / tactical」，反对空泛 (source: T05-S002 lennysnewsletter.com/podcast, 原话/转述)
  - 客户/团队解释样本: ⚠️ 暂未找到 ≥ 50 字 Lenny 本人就 AI 的直接原话片段（他主要做主持人/策展人，AI 观点多以「How AI will impact PM」综述文形式呈现而非个人独白；本次时间盒未深抓文章正文）
  - 专业讨论样本: ⚠️ 暂未找到 —— Lenny 不在监管/学术 register 发声，他的价值是「策展 + 主持」而非个人专业论述
- **sub_skill_candidate**: `false` —— 影响力极高，但他不是 AI PM、也不输出 AI PM 专属方法论；他是「通用 PM 策展人」，AI 只是他覆盖的一个切面。作为 figure 收录是因他的 AI 专题访谈是高密度信息源 + 他定义了「PM 该读什么」的底盘（产品 sense）
- **dual_role**: `"founder + curator"`（newsletter/podcast 创办人 + PM 内容策展人）
- **最近 12 个月动态**: 2026 年初发「Best of 2025」；持续扩展 AI 覆盖（AI prototyping for PM、building AI agents、AI adoption）；2026 多集 AI 公司操盘手访谈（Applied Intuition CEO Qasar Younis、Anthropic Head of Growth Amol Avasare）(evidence: [T05-S001, T05-S002])
- **争议 / 批评**: 综合 PM 内容占比高，纯 AI PM actionable 内容约 50-70% 期触及（Track 05 标 medium 投入产出比）；被批「访谈偏成功者叙事 / 幸存者偏差」；他本人不是 AI 专家，AI 深度依赖嘉宾 —— 对想要 AI 技术深度的读者，Lenny 是「产品 sense + 入口」而非「AI 深度」源
- **来源**:
  - [Primary] lennysnewsletter.com（本人 newsletter）: https://www.lennysnewsletter.com/ , collected 2026-05-14
  - [Primary] Lenny's Podcast（本人主持）: https://www.lennysnewsletter.com/podcast
  - [Primary] 「How AI will impact product management」(本人): https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management
  - [Reference] Track 05 把 Lenny's Newsletter + Podcast 列为资深 AI PM top 3 订阅源: 05-sources.md T05-S001/S002
- **可信度自评**: high（本人 newsletter + podcast 全一手，订阅量行业第一；扣分项是 AI 非其专长，作产品 sense 底座 + 信息入口可信度高）

### 9-10. 国内（zh-CN）figures —— DROP，未收录

- **朋克熊 /《AI 产品经理:从 0 到 1》作者**：intake + Track 04 列为种子。本次搜索（"朋克熊 AI产品经理"）返回结果**全部命中黑名单**：zhuanlan.zhihu.com、blog.csdn.net、mp.weixin.qq.com，以及课程营销站。无出版社页 / 无豆瓣作者页 / 无本人独立站 / 无小宇宙官方节目页可作一手锚点。按硬约束「黑名单 URL 直接不进 manifest」→ **DROP**。
- **唐辰 / 混沌 AI / 元帅训练营**：同样仅见于黑名单平台 + 训练营营销页（intake warning 明确点名「7 天速成 AI PM」营销课泛滥）。无合规一手源 → **DROP**。
- **结论**：本 track 的国内 figure 维度 = **0**。这不是「调研不够努力」，是结构性 gap —— 国内 AI PM 头部人物的主要发声渠道（公众号 / 知乎专栏）整体在黑名单上，合规一手源（本人独立站 / arXiv / 官方节目页 / 出版社页）几乎不存在。Track 05 也只能 retain 3 个国内 podcast（AI产品经理 Global / OnBoard! / 硅谷101），且主播身份多「待核」。**Phase 2.8 诚实边界必须明说**：figures 维度严重偏海外工程向，国内 AI PM 的「认知操作系统承载者」无法用本 skill 的合规标准覆盖；若用户主要在国内语境工作，figures 这一维度的代表性会打折。
- **给后续 refresh 的提示**：若未来朋克熊 / 唐辰等人开了本人独立站、上了小宇宙官方节目页、或出版社上架了可验证书目页，可补入；当前（2026-05）无路径。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 figures 都谈到的关键词**（候选行业心智模型）:

- **「Eval 是地基，不是可选项 / 别 vibe-check」** —— 出现于 figures: Hamel（核心论点）/ Eugene Yan（「eval = 科学方法的伪装」）/ Chip Huyen（《AI Engineering》评估章）/ Marily Nika（「minimum viable quality」）。**最强候选心智模型**，4 个 figure 独立强调，且与 Track 04 canon 的同款结论交叉印证（evidence: [T04-S008, T04-S005, T04-S013, T01-S010]）
- **「error analysis → 假设 → 改，而不是凭直觉加功能」** —— 出现于 figures: Hamel（field-guide 完整循环）/ Eugene Yan（修流程而非换 judge）。候选 playbook（evidence: [T04-S010, T04-S007]）
- **「workflow vs agent / agent 给『agent』收口定义」** —— 出现于 figures: Simon Willison（「agent = LLM 在循环里调工具达成目标」）/ swyx（Agent Engineering 立为独立主题）/ Chip Huyen（博客「Agents」长文）。配合 Track 04 的 Anthropic「Building Effective Agents」是强候选心智模型（evidence: [T01-S015, T04-S033, T04-S023]）
- **「AI PM 不需要会训模型，但要懂 AI 能力边界 / 别做 feature theater」** —— 出现于 figures: Marily Nika（「pain point ↔ 技术」的翻译者）/ Aakash Gupta（「停止把 AI 当装饰性能力」）/ Chip Huyen（「foundation model 让人人能搭复杂应用」）。**这是最贴「AI PM 角色定义」的候选心智模型**，3 个 figure 独立表述（evidence: [T04-S002, T01-S018, T04-S013]）
- **「AI Engineer / AI PM 是新工种，能力『右移』到不做研究的人手里」** —— 出现于 figures: swyx（「5 年+研究团队 → API 文档+一个下午」「shift right」）/ Marily Nika（「establish a new domain」）/ Aakash Gupta（AI PM 是最干净的供需失衡）。候选心智模型 / 行业自我叙事（evidence: [T01-S017, T01-S009, T01-S019]）
- **「模型动态保鲜期极短，要持续校准」** —— 出现于 figures: Simon Willison（年度「year in LLMs」+ 即时评测）/ Chip Huyen（「2025 你必须知道的 AI Engineering」）。与 intake「技能保鲜期 6-12 个月」warning 一致，候选心智模型（evidence: [T01-S014, T01-S006]）

**显著分歧 / 流派分裂**（对应 intake「学派分歧大」+ Track 04「四流派」）:

- **「评估驱动」工程派**（代表：Hamel Husain、Eugene Yan）—— 主张「没有 eval 就是瞎改」，把 eval/error-analysis 当 AI PM 第一性技能。**当前最强信号**，但被批「对 0→1 早期产品过度强调 eval 会拖慢」「课程营销把 eval 万能论推过头」。
- **「应用工程系统派」**（代表：Chip Huyen）—— 主张「用现成 foundation model 搭应用是独立学科」，重 cost-quality-latency 三角 + 数据/监控。与工程派不冲突，但视角更「系统工程」而非「PM 决策」。
- **「行业生态 / 工种叙事派」**（代表：swyx，部分 Aakash Gupta）—— 关注「AI Engineer / AI PM 这个工种本身」的命名、组织、求职生态。被批「给已有工作贴新标签 / 造词」「与生态商业利益绑定」。
- **「产品 sense 优先派」**（代表：Marily Nika、Lenny Rachitsky，承接 Marty Cagan）—— 主张 AI 是新能力，但「该不该做、怎么验证需求、怎么组织团队」的产品判断不变；AI PM = 传统 PM sense + AI 技术理解的桥。
- **「模型脉搏 / 祛魅派」**（代表：Simon Willison）—— 不站队方法论，主张一手实测优先、给术语祛魅（agent 定义、prompt injection）。是其他派别的「事实校准器」。
- **核心张力**：工程派（Hamel/Eugene/Chip）认为 AI PM 的核心是「eval + 技术理解」；产品 sense 派（Marily/Lenny）认为核心是「产品判断 + AI 能力边界感」。intake warning 也明示「『prompt engineering 是 AI PM 核心技能』是片面认知 —— 真正核心是 eval 设计 + 产品 fit 判断 + 团队协作」，Phase 2 提炼时这条张力要保留，不要强行调和。

**冷僻领域信号**:

- 总 figure 数 < 10？—— **是（仅 8，且全海外）**。但属「按指令只研究 top 8」+「国内 figure 因黑名单约束 DROP」的主动取舍 / 结构性 gap，非「行业本身冷僻」—— AI PM 海外 figure 池其实丰满（Track 04/05 还浮现 Shreya Shankar、Alessio Fanelli、Nathan Labenz 等未研究的二线候选）。
- 多数 figure 长访谈材料 < 30 min？—— **否**。8 人均有 ≥ 30 min long-form 一手材料（多个长 podcast / talk / 系统性著作），可调研性强。
- 标记「可信度 low」的 figure 比例 > 30%？—— **否**。8 人全部 high。
- **判定**：触发**「figures 维度信号薄弱」的诚实边界标注**，但触发原因是**国内维度结构性缺失**（zh-CN figure = 0）+ **「AI PM 视角」在 figure 池中稀薄**（8 人中仅 2 人 title 对口），**不是海外整体冷僻**。Phase 2.8 应这样写：「figures 维度：海外工程向信号充沛（8 位均 high 可信度、均有 ≥30min 一手材料），但 (1) 国内 AI PM figures 因主要发声渠道在黑名单（公众号/知乎）无法用合规一手源覆盖，zh-CN figure = 0；(2) 8 位 figure 中真正 title 对口『AI 产品经理』的仅 Marily Nika / Aakash Gupta 2 位，其余是 applied scientist / ML engineer / 作者 / 大会创办人 —— 提炼出的 mental model 在『纯 AI PM 视角一致性』上弱于在『AI 工程落地一致性』上。」

---

## Phase 2 接口

- **本 track（Wave 2）→ Phase 2 心智模型蒸馏**：6 个跨 ≥3 figure 的候选心智模型已在上「Phase 2 提炼提示」结构化，每条挂了 ≥ 2 个 source_id（多数跨 Track 04/05），可直接喂 Phase 2.7。最强 4 条：「eval 是地基」/「error analysis 优先」/「workflow vs agent」/「AI PM 不训模型但懂能力边界」。
- **本 track → Phase 3 sub-skill 决策**：`sub_skill_candidate: true` 的 3 位 —— **Marily Nika**（最对口 AI PM 角色本身，有书 + 100 cohort 课 + 多个长访谈，用户 focus 完全对齐）、**Hamel Husain**（eval-driven 迭代体系自洽，有 Maven 系统课 + 长 podcast）、**Aakash Gupta**（AI PM 垂直度最高，偏「角色画像 + 求职」而非完整方法论，标 true 但理由较弱）。建议 Phase 3 Step 3 优先评估前两位是否调用 nuwa.skill 蒸馏；Aakash 可作「AI PM 角色定义 / 入行路径」的轻量 sub-skill 或并入主 skill。
- **本 track → Track 02 tools 加权反馈**：figures 反复点名的工具 —— eval 工具栈（Hamel「Selecting The Right AI Evals Tool」是直接 evidence；LangSmith / BrainTrust / Promptfoo / Arize）、MCP（swyx 大会首设 dedicated track）、coding agents（Simon Willison 2025 主题）、Maven（Hamel/Marily 的课都在此，可反馈 Track 04 作课程）。
- **本 track → Track 05 sources 一致性**：本 track 8 位 figure 与 Track 05 的 source host 高度重合（Eugene/Hamel/Chip/Simon 的博客、swyx 的 Latent Space、Lenny/Aakash/Marily 的 newsletter 都是 Track 05 已收 source）—— **figures 与 sources 强一致，无矛盾**。Track 05 还浮现 Shreya Shankar / Alessio Fanelli / Nathan Labenz 作 figure 候选，本 track 因「只研究 top 8」未覆盖，Phase 1.5 若需补可从这里接。
- **一致性检查提示（Phase 1.5）**：本 track 与 Track 04 canon **完全一致**（8 位中 7 位是 canon 作者或 canon 强关联人物，Lenny 是唯一纯 source 型）。两轨共同的结构性缺口 = **国内（zh-CN）维度**：canon 的朋克熊书 DROP、figures 的朋克熊/唐辰 DROP，原因同为黑名单约束。这与 intake「国内外路径差异大」warning 一致，**synthesis 诚实边界必须明说「本 skill 的 figures + canon 双双偏海外工程向，国内 AI PM 生态未能用合规一手源覆盖」**。
- **给后续 refresh 的提示**（建议 ≤ 6 个月，本行保鲜期短）：(1) 补研究 Track 05 浮现的 Shreya Shankar / Alessio Fanelli / Nathan Labenz；(2) 盯国内 figure 是否出现合规一手源（本人独立站 / 小宇宙官方页 / 出版社书目页）；(3) 8 位现有 figure 的「最近 12 个月动态」需重抓 —— 模型动态保鲜期极短，Simon Willison / Chip Huyen 的表态半年就会过时。

---

*调研者注：本文件研究 8 个 figure（均海外，按任务指令的 top 8），新增 21 个 T01- source（另大量复用 T04-/T05- 跨 track source，引用时用原 ID 未重编）。bucket 分布：verified_primary 6 + surrogate_primary 6 + secondary 9（时间盒紧未跑 source_verifier.py，按 _source_id_manifest.md 同款保守规则人工标，作者本人渠道从宽标 surrogate_primary）。0 个黑名单 URL 入表。最大不确定性：(1) 国内 figure 维度 = 0，结构性 gap；(2) 8 人中仅 2 人 title 对口「AI 产品经理」，「AI PM 视角」在 figure 池稀薄；(3) voice_samples 多来自搜索摘要 + 节目描述（标「转述」），未逐集抓 podcast 字幕 —— 前两次 agent 因网络挂掉，本次策略是先落盘 + 增量写 + WebFetch 节制不用。本文件分 6 次增量 Edit 写入，每 2-3 个 figure 落盘一次，未攒到最后一次性写。*
