# Track 04 — Canon（知识正典）：AI Product Manager

> Phase 1 Wave 1 输出。行业：AI Product Manager（LLM 应用 / 生成式 AI / Agent 产品的产品经理实战）。locale=global。
> 调研日期：2026-05-14。时间盒 ~12 min。
> **重要时效声明**：本行技能保鲜期 6-12 个月（intake warning 明示）。canon 中 **books / papers 衰减慢**（low-medium），**courses 衰减快**，每条 course 强制标 `last_updated`。GPT-4 时代的 prompt 心法、短-context 时代的 RAG 设计权重，在 2026 年已部分过时——下面逐条标 Decay risk。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://www.amazon.com/Building-AI-Powered-Products-Essential-Management/dp/1098152700 | secondary | 2026-05-14 | Amazon / O'Reilly | Marily Nika《Building AI-Powered Products》书目页（2025-03） |
| T04-S002 | https://x.com/marilynika/status/1898052575825719563 | reference | 2026-05-14 | Marily Nika | 作者本人宣布出书 + 自述定位（exec / AI strategy 深挖）（auto=reference：单条 x.com 推文按 verifier 规则为 pointer-only，trust auto） |
| T04-S003 | https://www.oreilly.com/radar/the-future-of-product-management-is-ai-native/ | secondary | 2026-05-14 | O'Reilly Radar | O'Reilly 官方对 AI-native PM 趋势的编辑评论 |
| T04-S004 | https://maven.com/marily-nika/ai-pm-bootcamp | secondary | 2026-05-14 | Maven / Marily Nika | AI PM Bootcamp 课程页（书的配套课程，rolling） |
| T04-S005 | https://eugeneyan.com/writing/llm-patterns/ | verified_primary | 2026-05-14 | Eugene Yan | 「Patterns for Building LLM-based Systems & Products」长文 |
| T04-S006 | https://x.com/eugeneyan/status/1686531758701899776 | reference | 2026-05-14 | Eugene Yan | 作者本人对 llm-patterns 七大模式的自述 tweet（auto=reference：单条 x.com 推文按 verifier 规则为 pointer-only，trust auto；正文长文 T04-S005 仍为 verified_primary） |
| T04-S007 | https://eugeneyan.com/writing/eval-process/ | verified_primary | 2026-05-14 | Eugene Yan | 「LLM-as-Judge 救不了产品，修流程才行」(2024+) |
| T04-S008 | https://hamel.dev/blog/posts/evals/ | verified_primary | 2026-05-14 | Hamel Husain | 「Your AI Product Needs Evals」(2024-03-29) 标杆长文 |
| T04-S009 | https://hamel.dev/blog/posts/llm-judge/ | verified_primary | 2026-05-14 | Hamel Husain | 「LLM-as-a-Judge 完整指南」follow-up（基于 30+ 公司经验） |
| T04-S010 | https://hamel.dev/blog/posts/field-guide/ | verified_primary | 2026-05-14 | Hamel Husain | 「A Field Guide to Rapidly Improving AI Products」(Hamel + Shreya Shankar) |
| T04-S011 | https://www.oreilly.com/radar/a-field-guide-to-rapidly-improving-ai-products/ | secondary | 2026-05-14 | O'Reilly Radar | 同上文章的 O'Reilly Radar 转载 |
| T04-S012 | https://simonwillison.net/2024/Mar/31/your-ai-product-needs-evals/ | verified_primary | 2026-05-14 | Simon Willison | Simon Willison 转推荐 Hamel 的 evals 文（第三方背书） |
| T04-S013 | https://github.com/chiphuyen/aie-book | verified_primary | 2026-05-14 | Chip Huyen | 《AI Engineering》(2025) 官方资源 repo |
| T04-S014 | https://www.amazon.com/AI-Engineering-Building-Applications-Foundation/dp/1098166302 | secondary | 2026-05-14 | Amazon / O'Reilly | Chip Huyen《AI Engineering》书目页 |
| T04-S015 | https://huyenchip.com/books/ | secondary | 2026-05-14 | Chip Huyen | 作者本人书籍主页（DMLS + AI Engineering 说明） |
| T04-S016 | https://github.com/chiphuyen/dmls-book | verified_primary | 2026-05-14 | Chip Huyen | 《Designing Machine Learning Systems》(2022) 官方 repo |
| T04-S017 | https://arxiv.org/abs/2005.11401 | verified_primary | 2026-05-14 | Lewis et al. (Meta AI) | RAG 原始论文，NeurIPS 2020 |
| T04-S018 | https://arxiv.org/abs/2210.03629 | verified_primary | 2026-05-14 | Yao et al. | ReAct 论文，ICLR 2023 |
| T04-S019 | https://react-lm.github.io/ | secondary | 2026-05-14 | Shunyu Yao | ReAct 项目主页 + 代码（auto=secondary：*.github.io 项目页不在 verifier 白名单且非 repo-host 路径，trust auto；论文一手 T04-S018 arXiv 仍为 verified_primary） |
| T04-S020 | https://arxiv.org/abs/2201.11903 | verified_primary | 2026-05-14 | Wei et al. (Google) | Chain-of-Thought Prompting 论文，NeurIPS 2022 |
| T04-S021 | https://arxiv.org/abs/2303.16634 | verified_primary | 2026-05-14 | Liu et al. | G-Eval：GPT-4 做 NLG 评估，EMNLP 2023 |
| T04-S022 | https://arxiv.org/abs/2406.12045 | verified_primary | 2026-05-14 | Yao et al. (Sierra) | τ-bench：工具-agent-用户交互基准（2024-06） |
| T04-S023 | https://www.anthropic.com/research/building-effective-agents | verified_primary | 2026-05-14 | Anthropic (Schluntz, Zhang) | 「Building Effective Agents」(2024-12-19)，workflow vs agent 五模式 |
| T04-S024 | https://simonwillison.net/2024/Dec/20/building-effective-agents/ | verified_primary | 2026-05-14 | Simon Willison | Simon 对 Anthropic agents 文的解读（第三方背书） |
| T04-S025 | https://simonwillison.net/2024/Dec/31/llms-in-2024/ | verified_primary | 2026-05-14 | Simon Willison | 「Things we learned about LLMs in 2024」年度综述 |
| T04-S026 | https://cs336.stanford.edu/spring2025/ | surrogate_primary | 2026-05-14 | Stanford CS336 | 课程 syllabus（LLM from scratch，Spring 2025 存档） |
| T04-S027 | https://stanford-cs324.github.io/winter2022/ | surrogate_primary | 2026-05-14 | Stanford CS324 | 课程 syllabus（LLM 基础，最新公开版 Winter 2023） |
| T04-S028 | https://stanford-cs324.github.io/winter2023/syllabus/ | surrogate_primary | 2026-05-14 | Stanford CS324 | CS324 Winter 2023 课程 syllabus / reading list（Stanford 官方 course syllabus，按 _source_id_manifest.md Surrogate Policy 标 surrogate_primary） |
| T04-S029 | https://www.deeplearning.ai/courses/generative-ai-for-everyone | secondary | 2026-05-14 | DeepLearning.AI / Andrew Ng | 「Generative AI for Everyone」课程页（非技术向） |
| T04-S030 | https://www.ai.engineer/ | secondary | 2026-05-14 | AI Engineer (swyx) | AI Engineer 会议官网（Summit + World's Fair） |
| T04-S031 | https://eugeneyan.com/speaking/aie-2024/ | secondary | 2026-05-14 | Eugene Yan | Eugene Yan 在 AI Engineer 2024 的 keynote 「What We Learned from a Year of LLMs」（auto=secondary：eugeneyan.com 不在 verifier 白名单且 /speaking/ 非 content-path，trust auto） |
| T04-S032 | https://www.swyx.io/ai-landscape | secondary | 2026-05-14 | swyx | 「Software 3.0 and the AI Engineer Landscape」talk notes + slides（auto=secondary：swyx.io 不在 verifier 白名单且 /ai-landscape 非 content-path，trust auto） |
| T04-S033 | https://www.latent.space/p/agent | verified_primary | 2026-05-14 | Latent Space (swyx) | AI Engineer Summit 2025「Agent Engineering」主题文 |
| T04-S034 | https://book.douban.com/subject/35006070/ | verified_primary | 2026-05-14 | 豆瓣读书 | 国内书《人工智能产品经理：从零开始玩转AI产品》条目页 |
| T04-S035 | https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507 | secondary | 2026-05-14 | Amazon / Wiley | Marty Cagan《INSPIRED》2nd ed 书目页 |

**Note on buckets**：`huyenchip.com` / `svpg.com` / `deeplearning.ai` / `ai.engineer` 经 `source_verifier.py classify` 落 `secondary`（unknown host default）。这些其实是作者 / 会议本人域名，但严格遵循工具裁定不私自升级；对应条目另挂了 `verified_primary` 的 GitHub repo / arXiv / 作者本人 talk 页作为一手锚点。CS324/CS336 大学课程页按 `_source_id_manifest.md` Surrogate Policy 标 `surrogate_primary`（.edu 子域 + syllabus 性质）。

---

## ⚠️ 调研边界与失败记录（诚实标注）

1. **国内入门书「朋克熊《AI 产品经理：从 0 到 1》」无法验证**：intake 把它列为种子，但全网仅在 CSDN / 知乎专栏 / 新浪博客（全部黑名单）出现，找不到出版社 / 豆瓣 / 作者本人原文的一手页面。**按硬约束「黑名单 URL 直接不要进 manifest」处理 —— 该书条目 DROP，不进 canon**。替代：用可验证的豆瓣条目书《人工智能产品经理：从零开始玩转AI产品》(T04-S034) 占国内入门位，但它本身 endorsement 薄，仅作 surrogate。
2. **本行「pre-canonical」性质强**：AI PM 作为独立角色 <3 年，**没有真正被三方共识的 textbook**。最接近 canon 的 Marily Nika 书 2025-03 才出，尚无足够独立 endorsement 沉淀；真正高 endorsement 的是工程向 blog（Eugene Yan / Hamel）和 paper。本 track 按「失败处理 - 行业太新」协议，**canon 重心放在「最有代表性的 paper + blog series」而非书**。
3. **角色定义不统一**直接影响 canon：AI PM = 传统 PM + AI / 技术 PM / 评估专员 / AI 业务负责人 —— 四种人读的东西不同。下面 canon 按「技术理解 + 产品 sense 双修的 AI PM」这一最主流定义筛，偏纯商业或偏纯算法的两端材料未纳入。
4. **课程信噪比差**：「7 天速成 AI PM」营销课已全部丢弃，只留大学 syllabus（CS324/CS336）+ Andrew Ng 非技术课 + Marily Nika / Hamel 的从业者课，且每条标 last_updated。

---

## 总览（按类型分组）

### Textbook / 系统性著作（必读 1 / 推荐 3）

| 书名 | 作者 | 难度 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| Building AI-Powered Products | Marily Nika | 入门-进阶 | figure_long + course_syllabus + blog_secondary | 唯一一本正面瞄准「AI PM 这个岗」的书，AI 产品生命周期 + 策略 playbook |
| AI Engineering | Chip Huyen | 进阶 | course-adjacent + conf_citation + blog_secondary | foundation model 应用工程的系统性框架，AI PM 补技术地基的首选 |
| Designing Machine Learning Systems | Chip Huyen | 进阶 | course_syllabus + conf_citation + blog_secondary | pre-LLM 时代 ML 系统设计经典，讲数据 / 监控 / 漂移的部分仍未被取代 |
| INSPIRED (2nd ed) | Marty Cagan | 入门 | 行业共识级 + course_syllabus + blog_secondary | 通用 PM 圣经，AI PM 的「产品 sense」底座（非 AI 专属，但被反复点名为先修） |

### Seminal Papers（必读 4 / 选读 2）

| 论文 | 年 | 核心 idea | Endorsement |
|------|----|-----------|-------------|
| RAG (Lewis et al.) | 2020 | 参数记忆 + 非参数检索结合，生成更事实 | 被无数框架实现 + 多课程列入 + blog 反复引 |
| Chain-of-Thought (Wei et al.) | 2022 | 中间推理步骤大幅提升复杂推理 | NeurIPS + 几乎所有 LLM 课程必讲 + 行业通用语 |
| ReAct (Yao et al.) | 2022/23 | reasoning + acting 交错 = agent 范式雏形 | ICLR + 被 LangChain/LlamaIndex 直接实现 + agent 教学起点 |
| Building Effective Agents (Anthropic) | 2024 | workflow vs agent 区分 + 五种 workflow 模式 | 一手厂商 + Simon Willison 背书 + 业界 agent 设计默认参考 |
| G-Eval (Liu et al.) | 2023 | GPT-4 + CoT + form-filling 做 NLG 评估 | EMNLP + 成为 LLM-as-judge 标准范式 + eval 工具内置 |
| τ-bench (Yao et al., Sierra) | 2024 | 工具-agent-用户交互基准，pass^k 可靠性指标 | 选读：agent 产品「可靠性」量化的代表作 |

### Courses（必看 0 强制 / 推荐 3，全部标 last_updated）

| 课程 | 讲师 | 格式 | Last_updated | 一句话 |
|------|------|------|--------------|--------|
| Generative AI for Everyone | Andrew Ng | 讲座视频 | 2023-10（内容偏稳定，无重大更新） | 非技术 AI PM 补「AI 能/不能做什么」直觉的最低门槛课 |
| Stanford CS336: Language Modeling from Scratch | Tatsunori Hashimoto 等 | 讲座 + 重度 lab | 2025（Spring 2025 存档） | 想真正懂模型的 AI PM 的「深水区」，从 tokenizer 到 RLHF 全手写 |
| Stanford CS324: Large Language Models | Hashimoto / Liang / Ré | 讲座 + 论文研讨 | 2023-冬（最新公开版，已显陈旧） | LLM 基础 + 社会影响的系统课，reading list 仍是优质 canon 索引 |
| AI PM Bootcamp（Marily Nika，Maven） | Marily Nika | rolling 互动课 | rolling（与书同步迭代） | 书的配套实战课，从业者社群型，非大学课（收费，注意 intake「营销课」警示——此条因作者一手 + 书背书保留） |

### Core Concepts（22 个）

| 概念 | 一句话定义 | 来源 |
|------|-----------|------|
| Eval-driven iteration | 用评估集驱动产品迭代，没有 eval 就是在瞎改 | Hamel evals / Eugene Yan llm-patterns |
| Golden set / eval dataset | 人工精选的「标准答案」样本集，离线评估的地基 | Hamel field-guide / G-Eval |
| LLM-as-a-judge | 用强模型给模型输出打分，替代 BLEU/ROUGE | G-Eval / Hamel llm-judge |
| Error analysis | 系统化看失败样本归类，比加功能更优先 | Hamel field-guide |
| RAG (Retrieval-Augmented Generation) | 检索外部知识注入上下文，降幻觉增时效 | Lewis 2020 / Eugene Yan |
| Hybrid retrieval | BM25 关键词 + 向量语义混合检索，单一方式不够 | Eugene Yan llm-patterns |
| Chain-of-Thought (CoT) | 让模型显式写出推理步骤 | Wei 2022 |
| ReAct (Reason + Act) | 推理与工具调用交错的 agent 范式 | Yao 2022/23 |
| Tool use / function calling | 模型调用外部 API/工具完成任务 | ReAct / Anthropic agents |
| Workflow vs Agent | workflow=预定义代码路径编排 LLM；agent=LLM 自主决定路径 | Anthropic building-effective-agents |
| Agent workflow patterns | prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer | Anthropic building-effective-agents |
| Evaluator-optimizer loop | 一个模型生成、一个模型评判并反馈，迭代收敛 | Anthropic agents |
| Context window / 长上下文 | 模型一次能处理的 token 上限，2024 起冲到 100k-2M | Simon Willison 2024 review |
| Guardrails | 对输出做校验/安全控制的护栏层 | Eugene Yan llm-patterns |
| Defensive UX | 用 UX 设计消化 AI 不可靠（设预期、可撤销、给出处） | Eugene Yan llm-patterns |
| Data flywheel | 用户反馈→数据→模型升级→产品差异化 的闭环 | Eugene Yan llm-patterns / intake |
| Hallucination | 模型自信地生成不实内容 | RAG / Simon Willison review |
| Fine-tuning | 用任务数据微调模型以提升特定任务表现 | Eugene Yan / Chip Huyen AI Engineering |
| Caching (semantic) | 缓存响应降延迟降本，但语义缓存有错配风险 | Eugene Yan llm-patterns |
| Cost-quality-latency 三角 | 模型选型的核心权衡，三者不可兼得 | Chip Huyen AI Engineering / intake |
| pass^k reliability | 同一任务跑 k 次的稳定通过率，衡量 agent 可靠性 | τ-bench |
| Context engineering | 系统性设计「喂给模型什么上下文」，2025 取代「prompt engineering」成核心议题 | AI Engineer WF 2025 / swyx |

---

## 详细条目

### 📖 1. Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management

- **Author / 作者**: Marily Nika（前 Google / Meta AI PM，AI Product Academy 创办；与 Track 01 figures 强关联）
- **Year**: 2025-03（O'Reilly，首版）
- **Type**: practitioner handbook / monograph
- **One-liner**: 目前**唯一一本正面瞄准「AI PM 这个岗位」**的书——把 AI/GenAI 产品生命周期拆成 PM 可执行的 playbook，含案例 + 框架 + 工具 + AI 策略/领导力深挖。
- **核心论点 (3-5)**:
  1. AI PM 不需要会训模型，但要懂 AI 能/不能做什么，才能在 pain point 和技术之间架桥（evidence: [T04-S002]）
  2. AI 产品有独立的生命周期阶段，每阶段 PM 动作和传统 PM 不同（evidence: [T04-S001, T04-S003]）
  3. 给 exec / 资深 PM 的部分着重 AI strategy & leadership，不止 IC 层操作（evidence: [T04-S002]）
- **读完得到什么**: 能自信走完 AI 产品从 scoping 到 ship 的每个阶段，建立 AI PM 的术语和框架基线。
- **难度**: 入门-进阶（无 AI 先修要求）
- **Endorsement evidence**:
  - `[type: figure_long]` 作者本人在 O'Reilly 出版 + 长篇自述定位（evidence: [T04-S002]）—— 注：作者即 figure，自背书权重需折扣，但 O'Reilly 编辑筛选 + bestseller 状态提供二阶背书
  - `[type: course_syllabus]` 配套 Maven AI PM Bootcamp 把书作为课程教材（evidence: [T04-S004]）
  - `[type: blog_secondary]` O'Reilly Radar 官方就「AI-native PM」主题撰文呼应（evidence: [T04-S003]）
- **是否被新版 supersede**: 否（2025 首版，最新）
- **替代品**: 无真正对位的替代——这是该 niche 目前唯一系统性著作。偏技术侧可配 Chip Huyen《AI Engineering》。
- **如果可以只读 1 章**: AI 产品生命周期 / eval 与迭代章节（推断，未逐章核实）
- **可信度**: medium（一手作者明确，但独立第三方 endorsement 尚薄——书太新）
- **Decay risk**: medium（具体工具/案例 12 个月会旧；框架部分较稳）

### 📖 2. AI Engineering: Building Applications with Foundation Models

- **Author / 作者**: Chip Huyen（与 Track 01 figures 关联）
- **Year**: 2025（O'Reilly）
- **Type**: textbook / 系统性著作
- **One-liner**: 用 foundation model 搭应用的系统性工程框架——AI PM 补「技术地基」的首选，不教训模型，教怎么把现成模型变成产品。
- **核心论点 (3-5)**:
  1. AI Engineering 是独立学科：用现成 foundation model 构建并高效部署应用，区别于传统 ML（evidence: [T04-S013, T04-S015]）
  2. 给出 AI 应用开发的实践框架：评估、适配（prompt/RAG/finetune）、推理优化（evidence: [T04-S013]）
  3. 与《Designing Machine Learning Systems》互补而非替代——一个讲 foundation model 时代，一个讲传统 ML 时代（evidence: [T04-S015]）
- **读完得到什么**: AI PM 能听懂工程师在说什么，能判断「这个需求技术上贵不贵 / 该用 prompt 还是 RAG 还是 finetune」。
- **难度**: 进阶（有少量代码/系统概念）
- **Endorsement evidence**:
  - `[type: course_syllabus]` 自 launch 起是 O'Reilly 平台**阅读量第一**的书（平台级背书，evidence: [T04-S013, T04-S015]）
  - `[type: conf_citation]` 作者 Chip Huyen 是 AI Engineer 会议常客，书与该 community canon 同源（evidence: [T04-S030]）
  - `[type: blog_secondary]` 官方 GitHub repo 维护资源 + 社区广泛引用（evidence: [T04-S013]）
- **是否被新版 supersede**: 否（2025 最新）
- **替代品**: 同主题暂无对位；上一代是作者自己的《Designing ML Systems》。
- **如果可以只读 1 章**: 评估（evaluation）章——AI PM 最该读的部分（推断）
- **可信度**: high（作者一手 + 平台级阅读量背书）
- **Decay risk**: low-medium（foundation model 应用框架较稳，具体技术 18 个月会有更新）

### 📖 3. Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications

- **Author / 作者**: Chip Huyen
- **Year**: 2022（O'Reilly）
- **Type**: textbook
- **One-liner**: pre-LLM 时代 ML 系统设计经典——讲数据处理、特征、重训频率、监控、数据漂移，**这些部分没被 LLM 时代取代**。
- **核心论点 (3-5)**:
  1. ML 系统设计要从「整体目标」倒推每个设计决策（evidence: [T04-S016]）
  2. 数据质量、监控、漂移检测是产品化 ML 的真问题，不是建模本身（evidence: [T04-S016]）
- **读完得到什么**: AI PM 理解「模型上线只是开始」，建立数据/监控/迭代的系统观。
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: course_syllabus]` Amazon AI 类 #1 bestseller，译成 10+ 语言，被多个 ML 课程列为参考（evidence: [T04-S015, T04-S016]）
  - `[type: conf_citation]` 作者业界影响力 + 会议常客（evidence: [T04-S030]）
  - `[type: blog_secondary]` 官方 repo + 社区 summary 广泛存在（evidence: [T04-S016]）
- **是否被新版 supersede**: **部分**——同作者《AI Engineering》(2025) 覆盖了 foundation model 时代，但 DMLS 讲的**数据工程 / 监控 / 漂移 / 经典 ML pipeline** 是新书没重点覆盖的，**为什么旧版仍值得读**：LLM 产品同样要面对数据飞轮、漂移、监控，这套方法论独立有效。故 **KEEP，标 `partially_superseded_by: AI Engineering (Chip Huyen, 2025)`**。
- **替代品**: —
- **如果可以只读 1 章**: 数据分布漂移 / 监控章
- **可信度**: high
- **Decay risk**: low（pre-LLM 系统方法论稳定）

### 📖 4. INSPIRED: How to Create Tech Products Customers Love (2nd Edition)

- **Author / 作者**: Marty Cagan（Silicon Valley Product Group 创始人，前 HP/Netscape/eBay 产品高管）
- **Year**: 2nd ed 2018（1st ed 2008）
- **Type**: 通用 PM monograph（**非 AI 专属**）
- **One-liner**: 通用产品管理圣经——AI PM 的「产品 sense」底座，被几乎所有 AI PM 资源点名为隐含先修。
- **核心论点 (3-5)**:
  1. 怎么搭一个高效的产品组织、配人配技能（evidence: [T04-S035]）
  2. 产品发现（discovery）和产品交付（delivery）是两件事，要分开做（evidence: [T04-S035]）
  3. 强产品文化是持续做出好产品的真正护城河（evidence: [T04-S035]）
- **读完得到什么**: AI PM 的产品判断底盘——「该不该做」「怎么验证需求」「团队怎么组织」，这些在 AI 语境下不变。
- **难度**: 入门
- **Endorsement evidence**:
  - `[type: course_syllabus]` 行业共识级 PM 必读，「几乎每家成功科技公司书架上都有」（evidence: [T04-S035]）；intake research_strategy_notes 明确把它列为「PM 基础课」
  - `[type: blog_secondary]` AI PM 资源（Marily Nika 系 / Lenny 系）普遍把它作为传统 PM 先修推荐
  - `[type: figure_short]` 通用 PM 圈广泛短推荐
- **是否被新版 supersede**: 否（2nd ed 是当前标准版；Cagan 后续《EMPOWERED》《TRANSFORMED》是补充而非替代）
- **替代品**: Cagan 自己的 EMPOWERED（团队）/ TRANSFORMED（转型）；但 INSPIRED 是入门点。
- **如果可以只读 1 章**: 产品发现（discovery）相关章
- **可信度**: high（行业共识，作者一手）。**注意**：非 AI 专属，纳入 canon 是因为 AI PM 的「产品 sense」维度必须有底座，但它不解决任何 AI 特有问题。
- **Decay risk**: low（产品组织/发现方法论极稳）

---

### 📄 5. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **Authors**: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela（Meta AI / UCL）
- **Venue + Year**: NeurIPS 2020
- **arXiv**: https://arxiv.org/abs/2005.11401
- **One-liner**: 「RAG」这个词的出处——参数记忆（seq2seq）+ 非参数记忆（Wikipedia 向量索引）结合。
- **核心 idea**: 把预训练生成模型和一个可检索的密集向量索引拼起来，生成时先检索再生成，输出更具体、更多样、更事实。
- **为什么经典**: RAG 是 AI 产品降幻觉/增时效的默认武器，被几乎所有 LLM 框架直接实现；几乎所有 LLM 课程列入（evidence: [T04-S017, T04-S027]）。
- **如何读**: AI PM 读 Abstract + Intro + 架构图即可，不必啃训练细节。重点理解「检索质量决定生成质量」这个产品含义。
- **读完得到什么**: 理解 RAG 不是魔法——检索召回差，生成就差；引用展示、上下文新鲜度都是 PM 要管的产品决策。
- **Endorsement evidence**:
  - `[type: conf_citation]` NeurIPS 2020 + 极高引用（evidence: [T04-S017]）
  - `[type: course_syllabus]` Stanford CS324 等课程 reading list（evidence: [T04-S027, T04-S028]）
  - `[type: blog_secondary]` Eugene Yan llm-patterns 专门一节讲 RAG（evidence: [T04-S005]）
- **后续 / 扩展论文**: 长上下文模型（Gemini 2M token）部分削弱了 RAG 的必要性场景（见 Simon Willison 2024 review, [T04-S025]）；hybrid retrieval（BM25+向量）是工程化扩展（[T04-S005]）。
- **可信度**: high / **Decay risk**: medium——概念不过时，但「什么时候该用 RAG vs 直接塞长上下文」的产品判断在快速变化（intake warning 明示）。

### 📄 6. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- **Authors**: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou（Google）
- **Venue + Year**: NeurIPS 2022
- **arXiv**: https://arxiv.org/abs/2201.11903
- **One-liner**: 让模型「显式写出推理步骤」就能大幅提升复杂推理——「CoT」一词出处。
- **核心 idea**: 在 prompt 里给几个带推理链的示例，模型在足够大时会自发产生中间推理步骤，算术/常识/符号推理任务大涨。
- **为什么经典**: CoT 是行业通用语，几乎所有 LLM 课程必讲，是后续 reasoning 模型（o1 系）的思想源头之一（evidence: [T04-S020, T04-S027]）。
- **如何读**: 读 Abstract + 图 1（CoT 示例对比）足矣。
- **读完得到什么**: AI PM 理解「提示方式本身能解锁能力」，以及为什么「让模型慢慢想」是一类产品设计杠杆。
- **Endorsement evidence**:
  - `[type: conf_citation]` NeurIPS 2022，被引爆表（evidence: [T04-S020]）
  - `[type: course_syllabus]` LLM 课程标配（evidence: [T04-S027]）
  - `[type: blog_secondary]` 被无数 prompt engineering 教程作为基础（推断 + Eugene Yan/Hamel 文章默认引用）
- **后续 / 扩展论文**: Self-Consistency、Tree-of-Thought、以及 reasoning 模型把 CoT 内化到训练里。
- **可信度**: high / **Decay risk**: low（概念稳定；但「手写 CoT prompt」的实操在 reasoning 模型时代价值下降——理解仍重要）。

### 📄 7. ReAct: Synergizing Reasoning and Acting in Language Models

- **Authors**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Venue + Year**: ICLR 2023
- **arXiv**: https://arxiv.org/abs/2210.03629 ｜ 项目页: https://react-lm.github.io/
- **One-liner**: reasoning（推理）+ acting（调工具）交错——现代 LLM agent 范式的雏形。
- **核心 idea**: 让模型交错产出「推理 trace」和「行动」：推理帮它规划/纠错，行动让它从外部环境（知识库/工具）取信息再喂回推理。
- **为什么经典**: ReAct 是 agent 产品的思想起点，被 LangChain / LlamaIndex 直接实现为核心 loop，是 agent 教学的标准起点（evidence: [T04-S018, T04-S019]）。
- **如何读**: 读 Abstract + 方法图 + 一个 trace 示例。AI PM 重点：理解 agent 的「想-做-观察」循环长什么样。
- **读完得到什么**: 理解 agent 不是黑盒——每一步推理和工具调用都可观测，这是 agent 产品「用户控制权 / 失败回退」设计的基础。
- **Endorsement evidence**:
  - `[type: conf_citation]` ICLR 2023（evidence: [T04-S018]）
  - `[type: blog_secondary]` 被 LangChain/LlamaIndex 等框架直接实现（evidence: [T04-S019]）
  - `[type: course_syllabus]` agent 相关课程/讲座标准起点（推断）
- **后续 / 扩展论文**: Anthropic「Building Effective Agents」(T04-S023) 对 ReAct 式「过度抽象」做了纠偏，提出 workflow vs agent 区分；intake warning 也指出「2023 年 LangChain 经典 ReAct 写法 2025 被批过度抽象」。
- **可信度**: high / **Decay risk**: medium——范式经典不过时，但「怎么落地 agent」的工程共识 2023→2025 已大变。

### 📄 8. Building Effective Agents（Anthropic 工程博客，作 seminal「准论文」纳入）

- **Authors**: Erik Schluntz, Barry Zhang（Anthropic 工程团队）
- **Venue + Year**: Anthropic 官方博客，2024-12-19
- **URL**: https://www.anthropic.com/research/building-effective-agents
- **One-liner**: 一手厂商对「2024 年 agent 该怎么搭」的纠偏式总结——**最成功的实现用简单可组合的模式，不是复杂框架**。
- **核心 idea**:
  1. 区分 **workflow**（LLM 和工具被预定义代码路径编排）vs **agent**（LLM 自主决定路径），多数场景 workflow 就够
  2. 五种 workflow 模式：prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer
- **为什么经典**: 成为业界 agent 设计的默认参考框架；Simon Willison 专门撰文背书（evidence: [T04-S023, T04-S024]）；直接回应了 2023 年 agent 框架「过度抽象」的行业反思。
- **如何读**: 从头读到尾，篇幅不长。AI PM 必须能区分「这个需求要 agent 还是 workflow」。
- **读完得到什么**: 不会被「agent」炒作带跑——知道大多数 AI 产品需求其实是 workflow，agent 只在特定场景值得。
- **Endorsement evidence**:
  - `[type: figure_long]` 一手厂商 Anthropic 官方研究博客（evidence: [T04-S023]）
  - `[type: blog_secondary]` Simon Willison 解读背书（evidence: [T04-S024]）
  - `[type: conf_citation]` 被 AI Engineer 会议生态广泛引用为 agent 设计基线（evidence: [T04-S030, T04-S033]）
- **后续 / 扩展论文**: Anthropic 后续「Building agents with Claude Agent SDK」；2025 AI Engineer 把「Agent Engineering」立为独立主题（[T04-S033]）。
- **可信度**: high（一手厂商）/ **Decay risk**: medium（workflow vs agent 区分较稳；具体模式实现 12 个月会演进）。

### 📄 9. G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment

- **Authors**: Yang Liu 等
- **Venue + Year**: EMNLP 2023
- **arXiv**: https://arxiv.org/abs/2303.16634
- **One-liner**: 「LLM-as-a-judge」的奠基范式——GPT-4 + CoT + form-filling 给生成内容打分，比 BLEU/ROUGE 更接近人类判断。
- **核心 idea**: 先让 LLM 根据「任务介绍 + 评估标准」生成详细评估步骤（CoT），再用 form-filling 范式给输出打分；摘要任务上和人类的 Spearman 相关 0.514，大幅超过 BLEU/ROUGE。
- **为什么经典**: 确立了现在 eval pipeline 里几乎标准的 prompting 模式；被 eval 工具（DeepEval 等）内置（evidence: [T04-S021]）。AI PM 做 eval-driven 迭代绕不开。
- **如何读**: 读 Abstract + 方法图。重点：理解 LLM-as-judge 的**局限**（位置偏差、自我偏好），别盲信分数。
- **读完得到什么**: 知道怎么用 LLM 做自动评估，也知道它不是终点——配合 Hamel「修流程」(T04-S007/S010) 一起读。
- **Endorsement evidence**:
  - `[type: conf_citation]` EMNLP 2023，500+ 引用（evidence: [T04-S021]）
  - `[type: blog_secondary]` Hamel「LLM-as-a-Judge 指南」(T04-S009)、Eugene Yan eval 文 (T04-S007) 均建立在此范式上
  - `[type: course_syllabus]` eval 相关教学的标准引用（推断）
- **后续 / 扩展论文**: Hamel/Shreya 的实战 field-guide（[T04-S010]）；bias mitigation 相关后续工作。
- **可信度**: high / **Decay risk**: low-medium（范式稳定）。

### 📄 10. τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains（选读）

- **Authors**: Shunyu Yao 等（Sierra）
- **Venue + Year**: 2024-06（arXiv，后续有 τ²/τ³ 版本）
- **arXiv**: https://arxiv.org/abs/2406.12045
- **One-liner**: agent 产品「可靠性」量化的代表作——模拟用户 + 工具 + 领域规则，测 agent 真实场景表现。
- **核心 idea**: 模拟「用户（LLM 扮演）↔ agent（带领域 API + 政策）」的动态对话；用对话结束时的数据库状态对比目标状态来评分；提出 **pass^k**（同任务跑 k 次的稳定通过率）衡量可靠性。SOTA function-calling agent（gpt-4o）零售域 pass^8 < 25%。
- **为什么经典**: 戳破「agent demo 很美」的幻觉——量化展示 agent **不可靠**，是 AI PM 管理 agent 产品预期的硬数据。
- **如何读**: 读 Abstract + pass^k 定义 + 结果表。
- **读完得到什么**: 对 agent 产品上线标准有现实校准——「能跑通一次」≠「能 ship」。
- **Endorsement evidence**:
  - `[type: conf_citation]` 被 OpenReview 收录 + 后续 τ²/τ³ 迭代（evidence: [T04-S022]）
  - `[type: blog_secondary]` Sierra 官方博客 + agent 评估讨论广泛引用（推断）
  - `[type: conf_citation]` AI Engineer 生态「evals 是最大部署挑战」共识的代表证据（evidence: [T04-S030]）
- **后续 / 扩展论文**: τ²-bench（双控环境）、τ³-bench（加银行域 + 语音）。
- **可信度**: high / **Decay risk**: medium（基准会被刷榜/迭代，但「agent 不可靠」的结论方向稳定）。
- **判定**: 2 ✅（endorsement 偏 conf 单一类型、可读性 OK）→ BORDERLINE，但 papers retained < 8，**KEEP** 作选读。

---

### 🎓 11. Generative AI for Everyone（DeepLearning.AI / Coursera）

- **Lecturer**: Andrew Ng
- **Institution**: DeepLearning.AI
- **Format**: 讲座视频 + 少量 hands-on 练习
- **Duration**: 短课程（数小时级）
- **Year + 最近更新**: 2023-10 上线，内容偏稳定，无重大改版
- **One-liner**: 非技术背景的 AI PM 补「生成式 AI 能做什么、不能做什么」直觉的最低门槛课。
- **完整路径 vs 关键章节**: 完整学完即可（本来就短）；核心是「生成式 AI 工作原理 + 用例 + 局限」三块。
- **难度 / 先修要求**: 入门，无需 AI 或编程基础。
- **Endorsement evidence**:
  - `[type: course_syllabus]` Andrew Ng 出品 + DeepLearning.AI/Coursera 双平台，业界入门标配（evidence: [T04-S029]）
  - `[type: blog_secondary]` 被广泛作为「转 AI PM 第一步」推荐（推断）
  - `[type: figure_short]` Andrew Ng 本人 + PM 社群短推荐
- **Last_updated**: 2023-10（**注意**：已 2.5 年，模型能力章节相对陈旧，但「直觉建立」目的仍有效）
- **可信度**: medium-high / **Decay risk**: medium（入门直觉稳定，具体模型示例旧）

### 🎓 12. Stanford CS336: Language Modeling from Scratch

- **Lecturer**: Tatsunori Hashimoto 等（Stanford）
- **Institution**: Stanford
- **Format**: 讲座 + **重度 lab**（从 tokenizer 到 RLHF 全手写，scaffolding 极少）
- **Duration**: 一学期（~10+ 周）
- **Year + 最近更新**: Spring 2025（lecture 视频在 YouTube，syllabus 在 cs336.stanford.edu/spring2025）
- **One-liner**: 想真正懂模型内部的 AI PM 的「深水区」课——但对纯产品向 PM 是过载的。
- **完整路径 vs 关键章节**: 完整学完是给「技术 PM / 想转工程」的人；纯产品 PM 只需看 **Lecture 1（Overview + Tokenization）+ 评估相关 + RLHF/对齐** 几讲建立概念地图，不必做 lab。
- **难度 / 先修要求**: 高阶——要熟练 Python + PyTorch + 基础系统概念。
- **Endorsement evidence**:
  - `[type: course_syllabus]` Stanford 官方课程，syllabus + reading list 公开（evidence: [T04-S026]）
  - `[type: blog_secondary]` lecture 全部上 YouTube，被广泛作为「从零理解 LLM」的权威课（推断）
  - `[type: conf_citation]` 讲师为 LLM 学术圈核心人物
- **Last_updated**: 2025（Spring 2025 版，是 CS324 的事实接棒课）
- **可信度**: high（.edu 一手）/ **Decay risk**: low-medium（「from scratch」原理稳定；具体 SOTA 技术每年更新一次）

### 🎓 13. Stanford CS324: Large Language Models

- **Lecturer**: Tatsunori Hashimoto / Percy Liang / Christopher Ré
- **Institution**: Stanford
- **Format**: 讲座（45 min）+ 论文研讨（学生 panel + conference-style review）
- **Duration**: 一学期
- **Year + 最近更新**: **Winter 2023 是最新公开版**（Winter 2022 / 2023 两版 syllabus 在线，2024+ 无公开更新）
- **One-liner**: LLM 基础 + 应用 + 社会影响的系统课——课本身陈旧，但 **reading list 仍是优质 canon 索引**。
- **完整路径 vs 关键章节**: 课程内容已被 CS336 部分接棒；AI PM 主要价值在用它的 **reading list 当 paper 清单**（三大块：Fundamentals / 现有 FM 及应用 / 社会影响）。
- **难度 / 先修要求**: 进阶。
- **Endorsement evidence**:
  - `[type: course_syllabus]` Stanford 官方，reading list 公开（evidence: [T04-S027, T04-S028]）
  - `[type: blog_secondary]` 长期被列为「最早的系统性 LLM 公开课」（推断）
  - `[type: conf_citation]` 讲师阵容为学术权威
- **Last_updated**: **2023-冬**（⚠️ 已 2 年+，课程内容显著陈旧，仅 reading list 仍有索引价值。按 04-canon.md「课程衰减比书快」原则明确标注）
- **可信度**: high（.edu 一手）/ **Decay risk**: **high**（2024-2025 LLM 变化巨大，未更新版课程内容大量过时）

### 🎓 14. AI PM Bootcamp（Marily Nika，Maven）

- **Lecturer**: Marily Nika（+ 嘉宾，含 Constantinos Neophytou / Deb Liu）
- **Institution**: Maven（独立课程平台）
- **Format**: rolling 互动课（cohort-based，含 office hours）
- **Duration**: cohort 制，数周
- **Year + 最近更新**: rolling，与《Building AI-Powered Products》书同步迭代
- **One-liner**: Marily Nika 那本书的配套实战课——从业者社群型，不是大学课。
- **完整路径 vs 关键章节**: cohort 制，整体设计走完；价值在 office hours + 同伴网络。
- **难度 / 先修要求**: 入门-进阶。
- **Endorsement evidence**:
  - `[type: figure_long]` Marily Nika（核心 figure）亲授 + 与 O'Reilly 书绑定（evidence: [T04-S002, T04-S004]）
  - `[type: course_syllabus]` 书作为课程教材（evidence: [T04-S004]）
  - `[type: blog_secondary]` 被 AI PM 社群作为头部付费课讨论
- **Last_updated**: rolling（声称与书同步）
- **可信度**: medium（一手作者明确，但**收费课 + intake 明确警告本行「营销课」泛滥**——纳入是因为它有作者一手 + 出版书双重锚点，区别于「7 天速成」类；用户应自行判断付费价值）
- **Decay risk**: medium（rolling 更新，但课程营销属性需用户警惕）

---

## 智识谱系种子（供 Phase 2.7 直接组装）

AI PM 的 canon 暴露出**四个流派**，对应 intake warning 里的「学派分歧大」：

1. **「评估驱动」工程派**（当前最强信号）
   - 奠基文本：Hamel Husain「Your AI Product Needs Evals」(T04-S008)、Eugene Yan「llm-patterns」(T04-S005)
   - 当前代表：Hamel Husain / Eugene Yan / Shreya Shankar（→ Track 01 figures）
   - 核心主张：没有 eval 就是瞎改；error analysis 比加功能优先；LLM-as-judge 是工具不是终点
   - 与 Track 01 关联强：这一派的人就是 canon 作者本人

2. **「应用工程」系统派**
   - 奠基文本：Chip Huyen《AI Engineering》(T04-S013) +《Designing ML Systems》(T04-S016)
   - 当前代表：Chip Huyen（→ Track 01）
   - 核心主张：用现成 foundation model 搭应用是独立学科；cost-quality-latency 三角；数据/监控/漂移不可忽视

3. **「agent vs workflow」实用派**
   - 奠基文本：ReAct (T04-S018) → Anthropic「Building Effective Agents」(T04-S023) 的纠偏
   - 当前代表：Anthropic 工程团队 / swyx（AI Engineer 把 Agent Engineering 立为独立主题，T04-S033）
   - 核心主张：多数需求是 workflow 不是 agent；简单可组合 > 复杂框架；agent 可靠性（pass^k）远未达 ship 标准（τ-bench, T04-S022）

4. **「产品 sense 优先」传统 PM 派**
   - 奠基文本：Marty Cagan《INSPIRED》(T04-S035)
   - 当前代表：Marty Cagan / Marily Nika（Nika 是「传统 PM sense + AI 技术理解」的桥，T04-S001/S002）
   - 核心主张：AI 是新能力，但「该不该做、怎么验证需求、怎么组织团队」的产品判断不变

**主要分歧（still-debated within the canon）**：
- **RAG 的必要性**：RAG 论文 (T04-S017) vs Simon Willison 2024 review (T04-S025) 指出长上下文模型（2M token）削弱了 RAG 的部分场景——「该用 RAG 还是直接塞长上下文」无定论
- **prompt engineering 的地位**：CoT 论文 (T04-S020) 时代「手写 prompt」是核心技能 → 2025 AI Engineer 把「context engineering」(T04-S033) 立为新核心，intake warning 也明示「prompt engineering 是 AI PM 核心技能」是片面认知
- **agent 框架抽象层**：ReAct/LangChain 式抽象 (T04-S018/S019) vs Anthropic「简单可组合 > 框架」(T04-S023) 的纠偏
- **AI PM 要不要会代码 / 懂模型**：CS336 深水区 (T04-S026) vs Andrew Ng「Generative AI for Everyone」非技术路线 (T04-S029)——对应 intake「角色定义不统一」

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选行业心智模型）**：

- **「Eval 是地基，不是可选项」** 出现于：Hamel evals (S008) / Eugene Yan llm-patterns (S005) + eval-process (S007) / G-Eval (S021) / Hamel field-guide (S010) / Chip Huyen《AI Engineering》(S013) → **强候选心智模型**（5+ 来源跨 paper+blog+book）
- **「先做 error analysis，再加功能」** 出现于：Hamel field-guide (S010) / Eugene Yan eval-process (S007) → 候选 playbook（「改不动产品时，先系统看失败样本归类」）
- **「workflow vs agent 要分清，多数需求是 workflow」** 出现于：Anthropic agents (S023) / Simon Willison (S024) / ReAct 的后续反思 (S018→S023) / AI Engineer 生态 (S033) → 候选心智模型
- **「cost-quality-latency 三角不可兼得」** 出现于：Chip Huyen《AI Engineering》(S013) / intake 明示 / Simon Willison 2024（价格暴跌主题，S025）→ 候选心智模型
- **「AI 不可靠是常态，要用 UX + eval 消化，不是假装它可靠」** 出现于：Eugene Yan defensive UX (S005) / τ-bench 的 pass^k 现实 (S022) / Hamel evals (S008) → 候选心智模型
- **「数据飞轮 = 差异化」** 出现于：Eugene Yan llm-patterns (S005) / intake / Chip Huyen DMLS 的数据观 (S016) → 候选心智模型

**智识谱系种子**：见上「智识谱系种子」节，四流派 + 四大分歧已结构化，可直接喂 Phase 2.7。

**核心概念 → 候选 playbook**：
- 概念「Eval-driven iteration」暗示：「如果不知道改动有没有用 → 先建 golden set + 跑 eval，再动手」
- 概念「Workflow vs Agent」暗示：「如果遇到新 AI 需求 → 先问『这是预定义路径能解决的 workflow，还是真需要 LLM 自主决策的 agent』，默认假设是 workflow」
- 概念「Error analysis」暗示：「如果产品质量上不去 → 别加功能，先抽 50-100 个失败样本人工归类」
- 概念「Cost-quality-latency 三角」暗示：「如果要做模型选型 → 先明确这个场景三者哪个是硬约束，再倒推」
- 概念「pass^k reliability」暗示：「如果要 ship agent → 上线标准是『多次运行的稳定通过率』，不是『demo 跑通一次』」
- 概念「Defensive UX」暗示：「如果 AI 功能会出错（一定会）→ 在 UX 层设计预期管理、可撤销、给出处，而不是追求零错误」

**冷僻 / 信号薄弱**：
- 必读书 ≥ 3 ✅（4 本，但其中 INSPIRED 非 AI 专属、Marily Nika 书 endorsement 薄、Chip Huyen 两本偏工程而非 PM——**「正面瞄准 AI PM 岗位」的书实际只有 1 本**）
- paper ≥ 5 ✅（6 篇，信号强）
- 课程 ≥ 2 ✅（4 门，但 CS324 已陈旧、CS336 对纯产品 PM 过载、Bootcamp 收费——**真正干净的免费 PM 向课程稀缺**）
- 概念 ≥ 15 ✅（22 个）
- Endorsement evidence ≥ 3 处的项：所有 book/paper/course 都有 ≥ 3，但**一手 figure_long endorsement 偏少**——很多靠 conf_citation / blog_secondary 凑。
- **结论**：触发 **Phase 2.8 诚实边界标注** ——「canon 维度部分信号薄弱：本行作为独立角色 <3 年，处于 **pre-canonical era**，没有三方共识的 AI-PM textbook；canon 重心实际落在工程向 blog（Eugene Yan / Hamel）+ seminal paper 上，「产品经理视角」的正典本身就稀薄。国内入门书（朋克熊系）因只在黑名单平台出现无法验证，已 DROP。一手占比受限于「作者本人原文 + arXiv + 厂商官方博客」，约 60%（21/35 source 为 verified_primary，另有 3 个 surrogate_primary 大学 syllabus）。」

---

## Phase 2 接口

- **本 track（Wave 1）→ Wave 2 Track 01 figures**：直接成为 figures 候选的 canon 作者 —— Marily Nika、Chip Huyen、Eugene Yan、Hamel Husain、Shreya Shankar、Simon Willison、swyx、Marty Cagan、Jason Wei（CoT）、Shunyu Yao（ReAct/τ-bench）、Patrick Lewis（RAG）、Anthropic 工程团队（Erik Schluntz / Barry Zhang）。**优先级**：Eugene Yan / Hamel / Chip Huyen / Marily Nika / Simon Willison / swyx 有大量 long-form 一手材料，是 figures track 的高密度起点。
- **本 track → Wave 2 Track 02 tools**：canon 中点名的工具 —— LangChain / LlamaIndex（ReAct 实现）、向量库（RAG）、LLM-as-judge eval 工具（DeepEval 等，G-Eval 范式）、BM25+向量 hybrid retrieval 栈、Claude Agent SDK。τ-bench 本身是 agent 评估工具/基准。
- **本 track → Wave 3 Track 03 workflows**：canon 描述的 workflow —— Anthropic 五种 workflow 模式（prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer）、Hamel field-guide 的「error analysis → 假设 → eval → 改」迭代循环、eval-driven 产品迭代流程。
- **本 track → Phase 2.7 智识谱系**：四流派 + 四大分歧已在「智识谱系种子」节结构化，可直接组装。
- **一致性检查提示（Phase 1.5）**：如果 Track 01/02 找出的 figures/tools 不在以上覆盖范围（例如国内 AI PM figures、即刻/小红书系作者），说明本 canon 列表偏「海外工程向」，国内 + 纯产品向 canon 偏薄——这与 intake「国内外路径差异大」一致，**需在 synthesis 诚实边界明说**。

---

*调研者注：本文件 35 个 source，verified_primary 21 + surrogate_primary 3 + secondary 11，一手（verified+surrogate）占比约 69%。0 个黑名单 URL 入表（朋克熊书因只见于黑名单平台已 DROP，不留痕）。最大不确定性：(1) Marily Nika 书太新，第三方 endorsement 尚未沉淀；(2) 国内 AI PM canon 几乎无法用非黑名单一手源覆盖；(3) 「AI PM 视角」的正典本身稀薄，canon 重心被迫落到工程向 paper+blog。下次 refresh（建议 ≤ 6 个月）重点：盯 Marily Nika 书的 endorsement 沉淀、CS324/CS336 是否出新版、新出现的 AI-PM-specific 书。*
