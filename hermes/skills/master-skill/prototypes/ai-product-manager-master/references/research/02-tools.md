# Track 02 — Tools（工具地图 + 选型决策树）：AI Product Manager

> Phase 1 Wave 2 第 2 路 subagent。行业：AI Product Manager（LLM 应用 / 生成式 AI / Agent 产品 / Copilot 嵌入的产品经理实战）。locale=global。
> 调研日期：2026-05-14。时间盒 ~12 min。
> **时效硬声明**：工具栈是 master skill 衰减最快的部分（intake warning 明示「保鲜期 6-12 个月」）。每张卡片带 `last_checked` + maturity signal 具体日期。2024 年的工具范式（LangChain 经典 ReAct 抽象、RAG=vector DB 强绑定）2026 年已退潮 —— 逐条标 Decay risk。本次调研 GitHub stars 用 `api.github.com` 实拉（2026-05-13/14），vendor docs 按 SKILL.md 硬约束标 `surrogate_primary`（note 写明 "vendor docs"），不标 verified_primary。
> **冷僻协议未触发**：撒网 ~38 候选，retain 27（必备 8 / 场景特化 12 / 新兴 7）。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://platform.openai.com/docs | surrogate_primary | 2026-05-14 | OpenAI | vendor docs — OpenAI API / Responses API / Agents SDK |
| T02-S002 | https://docs.anthropic.com/en/docs | surrogate_primary | 2026-05-14 | Anthropic | vendor docs — Claude API / Agent SDK / Messages API |
| T02-S003 | https://ai.google.dev/gemini-api/docs | surrogate_primary | 2026-05-14 | Google | vendor docs — Gemini API（长 context / 多模态） |
| T02-S004 | https://github.com/BerriAI/litellm | verified_primary | 2026-05-14 | BerriAI | LiteLLM — 统一 100+ LLM provider 的 API gateway |
| T02-S005 | https://github.com/langchain-ai/langgraph | verified_primary | 2026-05-14 | LangChain | LangGraph — agent 编排（接棒 LangChain 的 agent story） |
| T02-S006 | https://github.com/langchain-ai/langchain | verified_primary | 2026-05-14 | LangChain | LangChain — 经典 orchestration，2026 退潮中 |
| T02-S007 | https://github.com/run-llama/llama_index | verified_primary | 2026-05-14 | LlamaIndex (Run-Llama) | LlamaIndex — RAG / 数据 ingestion 专用 |
| T02-S008 | https://github.com/stanfordnlp/dspy | verified_primary | 2026-05-14 | Stanford NLP | DSPy — 程序化 prompt 优化，替代手写 prompt |
| T02-S009 | https://github.com/langfuse/langfuse | verified_primary | 2026-05-14 | Langfuse (YC) | Langfuse — 开源 LLM observability + prompt 管理 + eval |
| T02-S010 | https://github.com/Arize-ai/phoenix | verified_primary | 2026-05-14 | Arize AI | Arize Phoenix — 开源 observability + eval |
| T02-S011 | https://github.com/promptfoo/promptfoo | verified_primary | 2026-05-14 | Promptfoo | Promptfoo — prompt / 模型对比 + CI eval（2026-03 被 OpenAI 收购） |
| T02-S012 | https://github.com/qdrant/qdrant | verified_primary | 2026-05-14 | Qdrant | Qdrant — Rust 写的开源 vector DB，过滤检索最快 |
| T02-S013 | https://github.com/pgvector/pgvector | verified_primary | 2026-05-14 | pgvector (Andrew Kane) | pgvector — Postgres 向量扩展，v1 默认起点 |
| T02-S014 | https://github.com/weaviate/weaviate | verified_primary | 2026-05-14 | Weaviate | Weaviate — 内建 hybrid search 的 vector DB |
| T02-S015 | https://github.com/chroma-core/chroma | verified_primary | 2026-05-14 | Chroma | Chroma — 轻量级嵌入式 vector DB，原型阶段首选 |
| T02-S016 | https://github.com/HumanSignal/label-studio | verified_primary | 2026-05-14 | HumanSignal | Label Studio — 开源标注 + AI eval，任务类型最广 |
| T02-S017 | https://github.com/argilla-io/argilla | verified_primary | 2026-05-14 | Argilla (Hugging Face) | Argilla — NLP/LLM 数据集 curation + RLHF 偏好数据 |
| T02-S018 | https://github.com/modelcontextprotocol/servers | verified_primary | 2026-05-12 | MCP / AAIF | MCP servers 官方仓库 — 85k stars，事实标准 |
| T02-S019 | https://github.com/Helicone/helicone | verified_primary | 2026-05-12 | Helicone | Helicone — AI gateway + observability + 成本控制 |
| T02-S020 | https://hamel.dev/blog/posts/eval-tools/ | verified_primary | 2026-05-14 | Hamel Husain | 「Selecting The Right AI Evals Tool」— eval 选型四准则一手 |
| T02-S021 | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation | surrogate_primary | 2026-05-14 | Anthropic | vendor docs — MCP 2025-12-09 捐给 Linux Foundation AAIF |
| T02-S022 | https://en.wikipedia.org/wiki/Model_Context_Protocol | secondary | 2026-05-14 | — | MCP 中立百科 — 采纳时间线 + 厂商支持交叉验证 |
| T02-S023 | https://thenewstack.io/why-the-model-context-protocol-won/ | secondary | 2026-05-14 | The New Stack | 「Why MCP Won」— 第三方分析 MCP 胜出原因 |
| T02-S024 | https://www.datadoghq.com/product/ai/llm-observability/ | surrogate_primary | 2026-05-14 | Datadog | vendor docs — Datadog LLM Observability + AI Guard |
| T02-S025 | https://www.statsig.com/ | surrogate_primary | 2026-05-14 | Statsig | vendor docs — 实验平台（2026-05 被 Amplitude 收编） |
| T02-S026 | https://inference.net/content/llm-evaluation-tools-comparison/ | secondary | 2026-05-14 | Inference.net | LLM eval 工具对比 — 「两层工具」实践模式 |
| T02-S027 | https://www.morphllm.com/llm-frameworks | secondary | 2026-05-14 | Morph | LLM 框架四象限分类 + provider SDK 优先论 |
| T02-S028 | https://www.marktechpost.com/2026/05/10/best-vector-databases-in-2026-pricing-scale-limits-and-architecture-tradeoffs-across-nine-leading-systems/ | secondary | 2026-05-14 | MarkTechPost | 9 个 vector DB 的定价 / scale / 架构对比 |
| T02-S029 | https://www.secondtalent.com/resources/pinecone-vs-weaviate-vs-qdrant-vs-pgvector/ | secondary | 2026-05-14 | Second Talent | vector DB 选型决策框架（按 use case） |
| T02-S030 | https://nearform.com/digital-community/prompt-management-systems-compared/ | secondary | 2026-05-14 | Nearform | prompt 管理系统对比（Langfuse / Helicone / PromptLayer） |
| T02-S031 | https://galileo.ai/blog/best-ai-guardrails-platforms | secondary | 2026-05-14 | Galileo | AI guardrails 平台对比（含 Lakera / NeMo Guardrails） |
| T02-S032 | https://www.herohunt.ai/blog/the-ultimate-ai-data-labeling-industry-overview/ | secondary | 2026-05-14 | HeroHunt | 数据标注行业总览（Surge / Scale / Argilla 格局） |
| T02-S033 | https://www.cloudzero.com/blog/llm-api-pricing-comparison/ | secondary | 2026-05-14 | CloudZero | LLM API 定价对比 — token economics 输入 |

> **黑名单合规**：搜索命中的知乎专栏 / 微信公众号 / CSDN / G2 / Capterra / Medium SEO 农场 URL 全部丢弃，未进 manifest（连 blacklisted 都不标）。`braintrust.dev/articles/*` 系列虽频繁出现在搜索结果，但属厂商自家 PR + SEO 内容（厂商对自身竞品的对比），按「工具厂商自家 PR 权重低」+ Medium 风格农场标题双重判定，**不进 manifest**；Braintrust 作为工具仍收录，证据走 Hamel 一手 (T02-S020) + 中立对比 (T02-S026)。

---

## 总览（按 tier 分组）

### 必备（8 个，≥ 80% 从业者用 / 行业基础设施）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| LLM Provider API（OpenAI / Anthropic / Gemini） | 一切的底座；AI PM 选型三角的「质量」轴 | low | T02-S001,S002,S003 |
| LiteLLM / provider SDK | 模型无关接入层；让换模型是「改参数」不是「重构」 | medium | T02-S004,S027,S033 |
| MCP（Model Context Protocol） | agent 连接外部工具的事实标准；已进 Linux Foundation | low-medium | T02-S018,S021,S022,S023 |
| 一个 eval 平台（LangSmith / Braintrust / Phoenix 三选一） | eval-driven 迭代的承载层；intake 点名「eval 是真核心」 | medium | T02-S020,S026,S009,S010 |
| 一个轻量 CI eval 框架（DeepEval / Promptfoo / RAGAS） | ship 前的回归门；与平台配对成「两层工具」 | medium-high | T02-S011,S020,S026 |
| Langfuse（或同类 observability） | LLM trace + prompt 管理 + 成本可见性 | medium | T02-S009,S030 |
| 一个 vector DB（pgvector 起步） | RAG 产品的检索层；v1 默认 pgvector | low-medium | T02-S013,S028,S029 |
| LangGraph / provider Agent SDK | agent 产品的编排层；2026 默认「最轻能跑的」 | high | T02-S005,S002,S001,S027 |

> **必备层 stars 阈值说明**：候选池有 stars 的 15 个工具，stars 中位数 ≈ 27.2k（langfuse）→ 必备阈值 ≈ 54k。纯靠 stars 跨线的只有 langchain (137k) / llama_index (49k 接近) / litellm (47k 接近)。**但本行必备层主体是 vendor API + 协议 + 方法论承载工具**，stars 不是它们的信号 —— 它们靠「≥ 3 独立 source 点名 + 行业 survey 采用率」入必备层（如 MCP：78% 企业 AI 团队生产环境有 MCP agent，evidence T02-S022）。这正是 SKILL.md「行业自适应基准」要避免的硬编码陷阱。

### 场景特化（12 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| DeepSeek / Qwen / GLM API | 成本敏感 / 国内合规 / 开源权重场景的 LLM 选择 | medium | T02-S033 |
| LlamaIndex | 复杂 RAG / 文档 ingestion 重的产品 | medium | T02-S007,S027 |
| DSPy | prompt 需要程序化优化、有 eval 集可优化时 | medium-high | T02-S008,S027 |
| Qdrant | 过滤检索吞吐瓶颈、要自托管时的 vector DB | low-medium | T02-S012,S028,S029 |
| Weaviate | 需要内建 hybrid search（关键词+向量一次查询） | low-medium | T02-S014,S029 |
| Chroma | 原型 / demo 阶段的嵌入式 vector DB | medium | T02-S015,S029 |
| Pinecone | 要零运维托管、可接受 recall 调优控制权少 | low-medium | T02-S028,S029 |
| Helicone | 把「成本可见性 + 多 provider gateway」放第一位 | medium | T02-S019,S030 |
| PromptLayer | 非技术 stakeholder（PM / copywriter）要独立改 prompt | medium | T02-S030 |
| Surge AI / Scale AI | RLHF / 大规模专业标注（frontier-model 级数据） | medium | T02-S032 |
| Argilla / Label Studio | 自托管标注 + 数据集 curation；error analysis 标注 | low-medium | T02-S016,S017,S032 |
| Datadog LLM Observability | 已用 Datadog 的团队，要 LLM trace 与 APM 关联 | medium | T02-S024 |

### 新兴 / 实验阶段（7 个，stability: experimental，6 个月后可能不存在 / 大变）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Claude Agent SDK | MCP-native 的 agent 开发 SDK；2025 起势 | high | T02-S002,S027 |
| OpenAI Agents SDK + Responses API | OpenAI 的 agent 编排栈，吸收了 Promptfoo | high | T02-S001,S011 |
| Google ADK（Agent Development Kit） | Google 的 agent 框架，跟 Gemini 绑定 | high | T02-S027 |
| CrewAI | 多 agent 角色编排（researcher/planner/executor 协作） | high | T02-S027 |
| Lakera Guard | 实时 AI 安全防火墙（prompt injection / 越权拦截） | high | T02-S031 |
| Datadog AI Guard | in-line guardrail，逐 prompt/输出/工具调用拦截 | high | T02-S024,S031 |
| Amplitude（前 Statsig）实验栈 | AI 产品的实验 / 灰度；2026-05 Statsig 被 Amplitude 收编后整合中 | high | T02-S025 |

---

## 工具卡片

### 1. LLM Provider API（OpenAI / Anthropic / Gemini）

- **One-liner**: AI 产品的底座 —— OpenAI（GPT-5 系，agentic terminal 强）、Anthropic（Claude Opus/Sonnet，复杂 coding + agent 强）、Gemini（最长 context + 最便宜的高质量选项）。AI PM「成本-质量-延迟三角」的「质量」轴就在这里选。
- **Tier**: 必备
- **Maintainer / Owner**: OpenAI / Anthropic / Google（各自 vendor）
- **License**: proprietary（API 服务，按 token 计费）
- **Maturity signals**:
  - 行业采用：frontier 三强是几乎所有 AI 产品的事实底座（evidence: [T02-S033]）
  - 模型迭代节奏：每几周一次新模型发布（GPT-5.5 / Claude Opus 4.7 / Gemini 3.1 Pro，2026-05 在榜）(evidence: [T02-S033])
  - Activity: healthy（持续高频发布）
- **不适合 / 替代方案**: 成本极敏感 / 国内合规 / 要开源权重 → 见场景特化层 DeepSeek/Qwen/GLM。**不要把单一 provider hardcode 进产品**（见避坑清单）。
- **生产案例**: 几乎所有 LLM 应用产品（ChatGPT / Claude / Perplexity / Notion AI / Cursor 等）—— 行业基础设施级，无需单一 case 佐证。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 中的 OpenAI/Anthropic 产品发布人（Aravind 等）关联。
- **近期变化** (近 12 个月): 模型版本号高频跳动（2026-05 已到 GPT-5.5 / Claude Opus 4.7 / Gemini 3.1 Pro 级别）；API 价格持续下行（输入 token 从 $0.10/M 到 $30/M 跨度）(evidence: [T02-S033])。
- **来源**:
  - [Primary] OpenAI docs: https://platform.openai.com/docs（collected: 2026-05-14, vendor docs）
  - [Primary] Anthropic docs: https://docs.anthropic.com/en/docs（vendor docs）
  - [Primary] Gemini API docs: https://ai.google.dev/gemini-api/docs（vendor docs）
  - [Secondary] CloudZero LLM API pricing: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- **可信度**: high
- **Decay risk**: low（「会有 frontier provider」这个事实稳定 3+ 年；但**具体哪个模型最强的排名 decay 是 high，6 个月必重校准** —— 卡片层稳定，模型选型层易变）

### 2. LiteLLM / provider SDK（模型无关接入层）

- **One-liner**: LiteLLM 用统一接口代理 100+ LLM provider；配合各家原生 SDK，让「换模型」从重构工程降级为改一个参数 —— 这是 2026 的架构共识。
- **Tier**: 必备
- **Maintainer / Owner**: BerriAI（LiteLLM）/ 各 vendor（provider SDK）
- **License**: open（LiteLLM，MIT 系）+ proprietary（vendor SDK 免费但闭源）
- **Maturity signals**:
  - GitHub stars: LiteLLM 46,951（2026-05-14 实拉）
  - First public release: 2023-07（repo created 2023-07-27）
  - Last commit: 当天活跃（pushed 2026-05-14）
  - Activity: healthy
- **不适合 / 替代方案**: 只用单一 provider 且确定不换 → 直接用该家 SDK，不必加 LiteLLM 抽象层。重度 agent 编排需求 → LiteLLM 之上还要 LangGraph / Agent SDK。
- **生产案例**: 行业普遍模式 ——「model-agnostic infrastructure is no longer optional」，hardcode provider 的应用面临「recurring migration projects」(evidence: [T02-S033], [T02-S027])。
- **近期变化** (近 12 个月): provider SDK 自身大幅变好，2026 共识是「新项目默认用最轻的能跑的 —— 通常就是 provider SDK」(evidence: [T02-S027])。
- **来源**:
  - [Primary] LiteLLM repo: https://github.com/BerriAI/litellm（collected: 2026-05-14）
  - [Secondary] Morph LLM frameworks: https://www.morphllm.com/llm-frameworks
  - [Secondary] CloudZero pricing: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- **可信度**: high
- **Decay risk**: medium（抽象层本身稳定；但 provider SDK 越做越好可能侵蚀 LiteLLM 的必要性）

### 3. MCP（Model Context Protocol）

- **One-liner**: 定义 AI 模型如何连接外部工具 / API / 数据的开放标准 —— agent 产品的「USB-C」。intake 未单列，但 Wave 1 Track 05/06 均点名应作核心收录。
- **Tier**: 必备
- **Maintainer / Owner**: Linux Foundation 旗下 Agentic AI Foundation（AAIF）—— 2025-12-09 起，不再是「Anthropic 的协议」(evidence: [T02-S021])
- **License**: open（开放标准 + 开源 SDK / servers）
- **Maturity signals**:
  - GitHub stars: modelcontextprotocol/servers 85,624（2026-05-12 实拉）
  - First public release: 2024-11（Anthropic 开源；repo created 2024-11-19）
  - 采用数据：97M 月度 SDK 下载（2026-03），78% 企业 AI 团队生产环境至少有一个 MCP-backed agent（2026-04）(evidence: [T02-S022])
  - Activity: healthy（快速演进）
- **典型使用场景** (场景特化视角，但已是必备协议):
  - agent 产品要接入外部工具 / 企业数据源 → 用 MCP server 而非各家私有协议
  - 跨厂商 agent 互操作 → MCP 是 OpenAI / Google / Microsoft / Anthropic 都原生支持的共同语言
- **不适合 / 替代方案**: 纯单 provider 闭环、不接外部工具的简单问答产品 → 用不上 MCP。早期（2024）各家私有 tool 协议 → 已被 MCP 收敛，不要再选私有协议（见避坑清单）。
- **生产案例**: Stripe / Vercel / 多个 Fortune 500 数据平台早期采用（evidence: [T02-S022]）；OpenAI 2025-03 在 Agents SDK / Responses API / ChatGPT desktop 全线接入；Google DeepMind 2025-04 确认 Gemini 支持。
- **维护者背景**: AAIF co-founder = Anthropic / Block / OpenAI；supporting = Google / Microsoft / AWS / Cloudflare / Bloomberg。
- **近期变化** (近 12 个月): 2025-12-09 捐给 Linux Foundation AAIF，与 Block 的 Goose、OpenAI 的 AGENTS.md 并列为 founding projects —— 从单厂商倡议变行业基础设施 (evidence: [T02-S021], [T02-S023])。
- **来源**:
  - [Primary] MCP servers repo: https://github.com/modelcontextprotocol/servers（collected: 2026-05-12）
  - [Primary] Anthropic 捐赠公告: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation（vendor docs）
  - [Secondary] Wikipedia MCP: https://en.wikipedia.org/wiki/Model_Context_Protocol
  - [Reference] The New Stack「Why MCP Won」: https://thenewstack.io/why-the-model-context-protocol-won/
- **可信度**: high
- **Decay risk**: low-medium（标准已机构化，「MCP 存在」很稳；但 intake/Track 06 标 `high` 因「新兴标准未定型」—— 折中为 low-medium：治理稳定但 spec 细节仍演进）

### 4. Eval 平台：LangSmith / Braintrust / Arize Phoenix（三选一）

- **One-liner**: eval-driven 产品迭代的承载层 —— LangSmith（LangChain/LangGraph 店首选）、Braintrust（单平台最完整，从数据集到 CI 门禁）、Phoenix（唯一深度覆盖 observability+eval 的开源 open-core）。intake + Track 04/05/06 都点名「eval 设计是 AI PM 真核心」。
- **Tier**: 必备（「有一个 eval 平台」是必备；具体选哪个是场景特化决策）
- **Maintainer / Owner**: LangChain（LangSmith，proprietary SaaS）/ Braintrust（proprietary）/ Arize AI（Phoenix，open-core）
- **License**: proprietary（LangSmith / Braintrust）/ open（Phoenix，Elastic License 系 open-core）
- **Maturity signals**:
  - GitHub stars: Arize-ai/phoenix 9,670（2026-05-14 实拉，open-core 部分）；LangSmith / Braintrust 闭源无 stars
  - First public release: Phoenix repo created 2022-11-09
  - Last commit: Phoenix 当天活跃（pushed 2026-05-14）
  - Activity: healthy
- **典型使用场景**:
  - 已在 LangChain/LangGraph 生态 → LangSmith 的 auto-instrumentation 省工（evidence: [T02-S026]）
  - 要「数据集管理 + 打分 + 生产监控 + CI release 门禁」一个平台搞定 → Braintrust（evidence: [T02-S026]）
  - 要 LangSmith 级 observability 但不要 vendor lock-in → Phoenix（evidence: [T02-S026]）
- **不适合 / 替代方案**: 用 custom orchestration / 直连 provider API / 混合框架栈 → LangSmith 原生支持弱，要额外 instrumentation 工作（evidence: [T02-S026]）。**注意 Hamel 警告**：eval 是方法论不是工具，工具只是承载，别让「premature tool outsourcing」替代 error analysis（evidence: [T02-S020]）。
- **生产案例**: Hamel Husain 与 LangSmith（Harrison Chase）/ Braintrust（Wayde Gilliam）/ Phoenix（SallyAnn DeLucia）分别做过深度对谈，三者都是真实生产工具（evidence: [T02-S020]）。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 中的 Hamel Husain（eval 圣经写作者）、Harrison Chase（LangChain 创办）关联。
- **近期变化** (近 12 个月): 「两层工具」分工成实践共识 —— 一个轻量 CI 框架（DeepEval/RAGAS/Promptfoo）+ 一个平台（Braintrust/LangSmith/Arize）(evidence: [T02-S026])。
- **来源**:
  - [Primary] Hamel「Selecting The Right AI Evals Tool」: https://hamel.dev/blog/posts/eval-tools/（collected: 2026-05-14 — 四准则一手）
  - [Primary] Arize Phoenix repo: https://github.com/Arize-ai/phoenix
  - [Secondary] Inference.net eval tools comparison: https://inference.net/content/llm-evaluation-tools-comparison/
- **可信度**: high
- **Decay risk**: medium（eval 平台层 fragmenting，每家都把「eval」收编成自家功能，Track 06 已标厂商错位包装；具体选型 12-18 个月会变）

### 5. CI Eval 框架：DeepEval / Promptfoo / RAGAS

- **One-liner**: ship 前的回归门 —— 轻量、跑得快、塞进 CI/CD。与「eval 平台」配对成「两层工具」：框架管 CI 门禁，平台管人工标注 + 回归追踪 + stakeholder dashboard。
- **Tier**: 必备（与 eval 平台是配对关系，不是二选一）
- **Maintainer / Owner**: Confident AI（DeepEval）/ Promptfoo（2026-03 起 OpenAI 旗下）/ Exploding Gradients（RAGAS）
- **License**: open（三者均开源）
- **Maturity signals**:
  - GitHub stars: promptfoo/promptfoo 21,245（2026-05-14 实拉）
  - First public release: Promptfoo 长期活跃项目
  - Last commit: Promptfoo 当天活跃（pushed 2026-05-14）
  - Activity: healthy
- **典型使用场景**:
  - prompt / 模型多方对比、要最快 time-to-insight → Promptfoo（evidence: [T02-S026]）
  - Python-native 工程团队的 CI eval → DeepEval（「DeepEval for CI evals + Braintrust for production traceability 正在成为工程主导 AI 产品团队的 de facto 标准」，evidence: [T02-S026]）
  - RAG pipeline 专项 eval → RAGAS
- **不适合 / 替代方案**: 需要人工标注 UI / stakeholder dashboard / 长期回归追踪 → 这是平台层的活，框架做不了（evidence: [T02-S026]）。
- **生产案例**: 「Python-native 团队越来越多用 DeepEval（CI）+ Braintrust（生产可追溯），成为工程主导 AI 产品团队 2026 de facto 标准」(evidence: [T02-S026])。
- **近期变化** (近 12 个月): **Promptfoo 2026-03 同意被 OpenAI 收购** —— 据报道仍保持开源（现行 license），但项目不再独立 (evidence: [T02-S026])。这是 AI PM 选型要警惕的「独立性变化」信号。
- **来源**:
  - [Primary] Promptfoo repo: https://github.com/promptfoo/promptfoo（collected: 2026-05-14）
  - [Primary] Hamel eval-tools（CI 框架 vs 平台分工逻辑）: https://hamel.dev/blog/posts/eval-tools/
  - [Secondary] Inference.net comparison: https://inference.net/content/llm-evaluation-tools-comparison/
- **可信度**: high
- **Decay risk**: medium-high（Promptfoo 被收购后路线不确定；CI eval 框架本身年轻、最佳实践仍演进）

### 6. Langfuse（LLM observability + prompt 管理 + eval）

- **One-liner**: 开源 LLM engineering 平台 —— trace、observability、prompt 管理、eval 一体，YC 背书。「截至 2025-10，Langfuse 在 prompt 管理领域 heads and shoulders above everyone else」。
- **Tier**: 必备（「有一个 observability/prompt 管理工具」是必备；Langfuse 是开源默认）
- **Maintainer / Owner**: Langfuse（YC 公司）
- **License**: open（MIT 核心，可完整自托管）
- **Maturity signals**:
  - GitHub stars: 27,193（2026-05-14 实拉）
  - First public release: 活跃开源项目（YC 出品）
  - Last commit: 当天活跃（pushed 2026-05-14T12:25Z）
  - Activity: healthy
- **典型使用场景**:
  - 复杂 agent 要 granular observability + best-in-class tracing → Langfuse（evidence: [T02-S030]）
  - 要完整自托管、不要 vendor lock-in 的 prompt 管理 → Langfuse（evidence: [T02-S030]）
- **不适合 / 替代方案**: 把「成本可见性 + 多 provider gateway」放第一位 → Helicone（gateway 型，但缺 eval 能力）。非技术 stakeholder 要独立改 prompt 部署 → PromptLayer（协作型，可视化编辑器 + 回滚）。
- **生产案例**: Nearform 对比测评中被列为 prompt 管理领域明确领先者（evidence: [T02-S030]）。
- **近期变化** (近 12 个月): 持续扩 agent observability 能力；prompt 管理领域竞争者（Helicone / PromptLayer / Laminar）增多但未撼动其位置 (evidence: [T02-S030])。
- **来源**:
  - [Primary] Langfuse repo: https://github.com/langfuse/langfuse（collected: 2026-05-14）
  - [Secondary] Nearform prompt management comparison: https://nearform.com/digital-community/prompt-management-systems-compared/
- **可信度**: high
- **Decay risk**: medium（开源 + 自托管降低 lock-in 风险；但 observability 赛道 fragmenting 快）

### 7. Vector DB：pgvector（v1 默认）+ Qdrant / Weaviate / Pinecone / Chroma

- **One-liner**: RAG 产品的检索层。2026 共识的选型路径：**v1 用 pgvector**（已在 Postgres 里、< 10M 向量、零额外成本）→ 用量真涨了再迁 Qdrant（过滤检索吞吐）/ Weaviate（hybrid search）/ Pinecone（零运维托管）。
- **Tier**: pgvector = 必备起点；其余 = 场景特化
- **Maintainer / Owner**: pgvector（Andrew Kane）/ Qdrant / Weaviate / Pinecone（proprietary SaaS）/ Chroma
- **License**: open（pgvector PostgreSQL License / Qdrant Apache 2.0 / Weaviate BSD / Chroma Apache 2.0）+ proprietary（Pinecone）
- **Maturity signals**:
  - GitHub stars（2026-05-14 实拉）：Chroma 27,953 / pgvector 21,282 / Qdrant 31,309 / Weaviate 16,179；Pinecone 闭源无 stars
  - First public release: pgvector repo created 2021-04-20 / Qdrant created 2020 系 / Weaviate created 2016-03-30
  - Last commit: 全部近期活跃（Qdrant pushed 2026-05-14；pgvector 2026-04-27）
  - Activity: healthy（全部）
- **典型使用场景**:
  - 已跑 Postgres、数据集 < 5-10M 向量、要向量与应用数据同库 → **pgvector**（最务实、零额外成本，evidence: [T02-S029]）
  - 要绝对最快的过滤检索、要自托管、Rust 栈 → **Qdrant**（1M 向量负载 1840 QPS，四者最高，evidence: [T02-S028][T02-S029]）
  - 要内建 hybrid search（关键词+向量一次查询）→ **Weaviate**（这一项做得比对比组里任何一个都好，evidence: [T02-S029]）
  - 要零运维、能接受 recall 调优控制权少、快速到生产 → **Pinecone**（evidence: [T02-S029]）
  - 原型 / demo 阶段、要嵌入式轻量 → **Chroma**
- **不适合 / 替代方案**: 数据集 > 10M 向量还硬用 pgvector → 该迁专用 vector DB（见决策树 B）。把 RAG 失败归咎于 vector DB → 错，RAG 失败 80% 在 chunking / 过时 embedding / 噪声源文档（Track 06 evidence）。
- **生产案例**: 「最常见模式：v1 用 pgvector 在已有 Postgres 库里，两周内 ship 到生产，监控查询延迟，用量真要求了再迁 Pinecone/Weaviate/Qdrant」(evidence: [T02-S029])。
- **近期变化** (近 12 个月): 长 context 模型（2M token）让「要不要做 RAG」的默认答案从「要」向「先试长 context」偏移（Track 04/06 警示）—— vector DB 不是消失，但「无脑上 vector DB」退潮。
- **来源**:
  - [Primary] pgvector repo: https://github.com/pgvector/pgvector（collected: 2026-05-14）
  - [Primary] Qdrant repo: https://github.com/qdrant/qdrant
  - [Primary] Weaviate repo: https://github.com/weaviate/weaviate
  - [Primary] Chroma repo: https://github.com/chroma-core/chroma
  - [Secondary] MarkTechPost 9-DB comparison: https://www.marktechpost.com/2026/05/10/best-vector-databases-in-2026-pricing-scale-limits-and-architecture-tradeoffs-across-nine-leading-systems/
  - [Secondary] Second Talent vector DB 选型: https://www.secondtalent.com/resources/pinecone-vs-weaviate-vs-qdrant-vs-pgvector/
- **可信度**: high
- **Decay risk**: low-medium（vector DB 作为品类稳定；具体选型受长 context 模型挤压，medium）

### 8. Agent 编排：LangGraph / provider Agent SDK

- **One-liner**: agent 产品的编排层。2026 的选型铁律：**默认用最轻的能跑的（通常是 provider SDK）**，感到真实痛点了再上框架。LangGraph 接棒了 LangChain 的 agent story。
- **Tier**: 必备（「有一个 agent 编排方案」是必备；具体选哪个看 decay 与场景）
- **Maintainer / Owner**: LangChain（LangGraph）/ OpenAI / Anthropic / Google（provider Agent SDK）
- **License**: open（LangGraph，MIT 系）+ proprietary（provider SDK 免费闭源）
- **Maturity signals**:
  - GitHub stars: langchain-ai/langgraph 32,032（2026-05-14 实拉）
  - First public release: LangGraph 2024 系（LangChain 衍生）
  - Last commit: 当天活跃（pushed 2026-05-13T22:20Z）
  - Activity: healthy
  - 框架开销基准：DSPy ~3.53ms < Haystack ~5.9ms < LlamaIndex ~6ms < LangChain ~10ms < LangGraph ~14ms（evidence: [T02-S027]）
- **典型使用场景**:
  - 多步 agent、要 stateful 图编排、已在 LangChain 生态 → LangGraph
  - 新项目、MCP-native 开发 → Claude Agent SDK（新兴层，high decay）
  - OpenAI 栈、要 Responses API 配套 → OpenAI Agents SDK（新兴层）
- **不适合 / 替代方案**: 简单 workflow（预定义路径就能解决）→ 不需要 agent 框架，直接 provider SDK + 几个函数。Anthropic「Building Effective Agents」明示「多数需求是 workflow 不是 agent」（Track 04 canon）。
- **生产案例**: LangGraph 34.5M 月度下载（via LangChain 生态数据，evidence: [T02-S027]）；CrewAI 被 DocuSign / IBM / PwC / PepsiCo 用于多 agent 编排（evidence: 见新兴层 CrewAI 卡片）。
- **维护者背景** (sub_skill_link): 与 Track 01 figures 中 Harrison Chase（LangChain/LangGraph 创办）关联。
- **近期变化** (近 12 个月): **2026 的核心退潮信号** —— 「LangChain 从 2023 的默认建 LLM app 方式，变成 2026 很多团队在 production 里主动移除的框架」(evidence: [T02-S027])。原因：provider SDK 变好了、LangGraph 接管 agent story、LlamaIndex/DSPy/Haystack 占走专用场景。
- **来源**:
  - [Primary] LangGraph repo: https://github.com/langchain-ai/langgraph（collected: 2026-05-14）
  - [Primary] Anthropic docs（Agent SDK）: https://docs.anthropic.com/en/docs（vendor docs）
  - [Primary] OpenAI docs（Agents SDK）: https://platform.openai.com/docs（vendor docs）
  - [Secondary] Morph LLM frameworks 四象限: https://www.morphllm.com/llm-frameworks
- **可信度**: high
- **Decay risk**: high（agent 框架层是整个工具栈衰减最快的 —— 2023 LangChain → 2026 provider SDK + LangGraph，下一轮 12 个月内大概率再变；新兴层的 Agent SDK 全部 high）

---

### 9. LangChain（经典 orchestration）—— 退潮工具，标注用

- **One-liner**: 2023 年「默认建 LLM app 的方式」，2026 被批「过度抽象」、被很多团队从 production 移除 —— 收录此卡片是为了**明确标注退潮**，让 AI PM 不要在 2026 还把它当默认。
- **Tier**: 退潮（不进三层 —— 既非必备、也非场景特化、也非新兴；保留作 intake 点名的「2024 退潮工具」案例）
- **Maintainer / Owner**: LangChain
- **License**: open（MIT）
- **Maturity signals**:
  - GitHub stars: langchain-ai/langchain 136,714（2026-05-14 实拉 —— stars 极高，但 stars ≠ production 健康度，这正是「stars 高但被移除」的典型）
  - Last commit: 当天活跃（pushed 2026-05-14）—— 仍维护，但定位变了
  - Activity: healthy（代码层）/ declining（作为「默认选择」的地位）
- **不适合 / 替代方案**: 2026 新项目不要默认 LangChain。agent → LangGraph / provider SDK；RAG → LlamaIndex；prompt 优化 → DSPy；最简单需求 → provider SDK 直连。早期实验 / 快速 prototype 仍可用，但要意识到 production 迁移成本。
- **近期变化** (近 12 个月): 定位从「通用默认」收缩为「early-stage 实验框架」；批评点 —— heavy abstraction、复杂 debugging、layered abstractions 学习曲线陡（evidence: [T02-S027]）。intake warning 明示：「2023 年的 LangChain 经典写法 2025 年被批为过度抽象」，本调研 2026 数据确认该趋势延续并加深。
- **来源**:
  - [Primary] LangChain repo: https://github.com/langchain-ai/langchain（collected: 2026-05-14）
  - [Secondary] Morph「LangChain 从默认到被移除」: https://www.morphllm.com/llm-frameworks
- **可信度**: high
- **Decay risk**: high（作为「默认选择」已 decay；作为「存在的工具」仍在）

### 10. DeepSeek / Qwen / GLM API（成本敏感 / 国内场景 LLM）

- **One-liner**: 成本敏感、国内合规、或要开源权重场景下的 LLM provider 选择 —— DeepSeek V3/R1、Qwen、GLM-5（Z.AI）在 2026 leaderboard 上是 frontier 之外的主力。
- **Tier**: 场景特化
- **Maintainer / Owner**: DeepSeek / 阿里（Qwen）/ 智谱 Z.AI（GLM）
- **License**: 混合（部分开源权重 + API 服务）
- **典型使用场景**:
  - 单用户经济模型算不过来、需要更低 token 单价 → DeepSeek 系
  - 国内合规要求（数据不出境 / 算法备案）→ 国内 provider
  - 要自托管开源权重做 fine-tune / 私有部署 → 开源权重模型
- **不适合 / 替代方案**: 要 frontier 级 agentic / 复杂 coding 能力 → 仍是 GPT-5 / Claude Opus / Gemini（必备层）。注意 a16z 等讨论过的 DeepSeek 安全话题（Wave 1 Track 05 提及）。
- **生产案例**: 2026-05 leaderboard 中 DeepSeek V4 与 GPT-5.5 / Claude Opus 4.7 同列被对比（evidence: [T02-S033]）。
- **近期变化** (近 12 个月): 国内模型持续逼近 frontier；价格战使「成本」轴选择更丰富。
- **来源**:
  - [Secondary] CloudZero LLM API pricing: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- **可信度**: medium（本次未深挖各家 vendor docs，主要靠对比文章）
- **Decay risk**: medium（模型迭代快，但「有低成本 / 国内选项」这个事实稳定）

### 11. LlamaIndex（复杂 RAG / 数据 ingestion）

- **One-liner**: RAG 专用框架 —— 比 LangChain 更深的 indexing / chunking / retrieval 能力，专攻数据 ingestion 重的产品。
- **Tier**: 场景特化
- **Maintainer / Owner**: LlamaIndex（Run-Llama）
- **License**: open（MIT）
- **Maturity signals**:
  - GitHub stars: 49,406（2026-05-14 实拉 —— 接近必备阈值 54k）
  - First public release: repo created 2022-11-02
  - Last commit: 近期活跃（pushed 2026-05-13）
  - Activity: healthy
- **典型使用场景**:
  - 产品核心是「把大量异构文档变成可检索知识」→ LlamaIndex 做 ingestion
  - 复杂 RAG（多源、需精细 chunking / 索引策略）→ 比 provider SDK 裸写省工
  - 常见组合：LlamaIndex 做数据 ingestion + LangGraph 做 workflow 编排（evidence: [T02-S027]）
- **不适合 / 替代方案**: 简单 RAG（单一知识源、chunking 不复杂）→ provider SDK + pgvector 直接写，不必上 LlamaIndex。要 agent 编排 → 那是 LangGraph 的活。
- **生产案例**: 「很多团队两者都用：LlamaIndex 做数据 ingestion，LangChain/LangGraph 做 workflow 编排」(evidence: [T02-S027])。
- **近期变化** (近 12 个月): 在框架四象限里稳定占住「RAG / 数据」专用位（evidence: [T02-S027]）。
- **来源**:
  - [Primary] LlamaIndex repo: https://github.com/run-llama/llama_index（collected: 2026-05-14）
  - [Secondary] Morph LLM frameworks: https://www.morphllm.com/llm-frameworks
- **可信度**: high
- **Decay risk**: medium（受长 context 模型挤压同 RAG；但 ingestion 能力仍有独立价值）

### 12. DSPy（程序化 prompt 优化）

- **One-liner**: 用程序化调优替代手写 prompt —— 当你有 eval 集、prompt 需要系统性优化而非手调措辞时用。框架开销最低（~3.53ms）。
- **Tier**: 场景特化
- **Maintainer / Owner**: Stanford NLP
- **License**: open（MIT）
- **Maturity signals**:
  - GitHub stars: 34,410（2026-05-14 实拉）
  - Last commit: 当天活跃（pushed 2026-05-13T23:13Z）
  - Activity: healthy
- **典型使用场景**:
  - 已有 golden set / eval 集，想让 prompt「被优化」而不是「被手调」→ DSPy
  - 多阶段 LLM pipeline，想程序化地联合优化各阶段 prompt
- **不适合 / 替代方案**: 没有 eval 集 → DSPy 优化无目标，先建 golden set（Track 04/06）。简单单次 prompt → 手写就够，DSPy 是过度工程。intake warning 提醒：prompt engineering 本就只是 AI PM 输出之一，DSPy 是「把这个输出自动化」的工具，不改变「eval 才是核心」。
- **生产案例**: 框架对比中 DSPy 被定位为「replaces manual prompt engineering with programmatic tuning」(evidence: [T02-S027])。
- **维护者背景** (sub_skill_link): Stanford NLP（与 Track 04 canon 的 Stanford CS324/CS336 同源机构）。
- **近期变化** (近 12 个月): 在「context engineering 取代 prompt engineering」的范式转移里，DSPy 是「程序化」一派的代表工具（Track 06 智识谱系线索）。
- **来源**:
  - [Primary] DSPy repo: https://github.com/stanfordnlp/dspy（collected: 2026-05-14）
  - [Secondary] Morph LLM frameworks: https://www.morphllm.com/llm-frameworks
- **可信度**: high
- **Decay risk**: medium-high（prompt 优化范式本身在快速演化；context engineering 主流化可能改变 DSPy 定位）

### 13. Helicone（AI gateway + 成本可见性）

- **One-liner**: AI gateway 为主 —— observability、analytics、成本节省（caching + 自动模型选择），prompt 管理是附带功能。把「成本可见性 + 多 provider gateway」放第一位时选它。
- **Tier**: 场景特化
- **Maintainer / Owner**: Helicone
- **License**: open（可自托管）
- **Maturity signals**:
  - GitHub stars: 5,660（2026-05-12 实拉）
  - First public release: repo created 2023-01-31
  - Last commit: 近期活跃（pushed 2026-05-12）
  - Activity: healthy
- **典型使用场景**:
  - 要快速上线成本可见性 + 多 provider 可观测性 → Helicone（evidence: [T02-S030]）
  - 想要 gateway 层 caching / 自动模型路由降本 → Helicone
- **不适合 / 替代方案**: 要跑 eval → Helicone 不具备 eval 能力（evidence: [T02-S030]），用 Langfuse / eval 平台。要 granular agent tracing → Langfuse 更强。要非技术 stakeholder 改 prompt → PromptLayer。
- **生产案例**: Nearform 对比测评定位其为「primarily an AI gateway」，prompt 管理非其重点（evidence: [T02-S030]）。
- **近期变化** (近 12 个月): gateway + observability 赛道竞争激烈（与 LiteLLM、各家 SDK 重叠）。
- **来源**:
  - [Primary] Helicone repo: https://github.com/Helicone/helicone（collected: 2026-05-12）
  - [Secondary] Nearform prompt management comparison: https://nearform.com/digital-community/prompt-management-systems-compared/
- **可信度**: medium-high
- **Decay risk**: medium（gateway 功能与 LiteLLM / provider SDK 重叠，定位需持续区分）

### 14. PromptLayer（非技术 stakeholder 的 prompt 协作）

- **One-liner**: 把 prompt 从代码里拿出来、放进受治理的中心化 registry —— 让 PM / copywriter 等非技术 stakeholder 不碰代码就能迭代 prompt 模板（可视化编辑器 + 版本控制 + 回滚）。
- **Tier**: 场景特化
- **Maintainer / Owner**: PromptLayer
- **License**: proprietary（自托管需 Enterprise license）
- **典型使用场景**:
  - 非技术 stakeholder 拥有 prompt 迭代、走代码部署流程拖慢他们 → PromptLayer（evidence: [T02-S030]）
  - 要把 prompt 变成可版本化 / 可治理 / 可安全部署的资产
- **不适合 / 替代方案**: 要自托管又不想买 Enterprise → Langfuse（开源自托管）。要 granular 复杂 agent observability → Langfuse。团队全是工程师、prompt 就在代码里管 → 不需要 PromptLayer。
- **生产案例**: Nearform 测评定位其为团队协作型，「让非技术 stakeholder 不碰 codebase 迭代 prompt 模板」(evidence: [T02-S030])。
- **近期变化** (近 12 个月): 在 prompt 管理赛道与 Langfuse / Helicone 形成「开源自托管 vs 协作治理」的差异化。
- **来源**:
  - [Secondary] Nearform prompt management comparison: https://nearform.com/digital-community/prompt-management-systems-compared/
- **可信度**: medium（本次未拉到 GitHub / vendor docs 一手，主要靠中立对比文）
- **Decay risk**: medium

### 15. Surge AI / Scale AI（RLHF / 大规模专业标注）

- **One-liner**: frontier-model 级数据标注的两大主力 —— Surge AI 是 LLM RLHF 的 go-to，Scale AI 偏多模态企业项目。AI PM 做数据飞轮 / fine-tune 时的标注供应商。
- **Tier**: 场景特化
- **Maintainer / Owner**: Surge AI / Scale AI（均为 proprietary 服务商）
- **License**: proprietary（标注服务）
- **Maturity signals**:
  - 市场数据：数据标注市场 2025 年 $4.89B → 预计 2030 年 $17.1B（28.4% CAGR）(evidence: [T02-S032])
  - Surge AI：2020 创办、bootstrapped、已过 $10 亿年营收且盈利（evidence: [T02-S032]）
  - Scale AI：Meta 2025-06 收购 49% 股权（估值 $29B）；但 OpenAI 和 Google 因竞争数据顾虑减少 / 终止与 Scale 的合同（evidence: [T02-S032]）
- **典型使用场景**:
  - LLM RLHF / 偏好数据、标注员需专门训练评估 AI 生成文本 → Surge AI（evidence: [T02-S032]）
  - 多模态企业级标注项目 → Scale AI（evidence: [T02-S032]）
- **不适合 / 替代方案**: 小规模 / 要自托管 / error analysis 标注 → Argilla / Label Studio（开源，见下卡片）。预算有限的早期产品 → 先用开源工具自标。
- **生产案例**: Surge AI 与 AI 研究团队紧密协作迭代 guidelines / rubrics，服务 frontier-model 合同（evidence: [T02-S032]）。
- **近期变化** (近 12 个月): **Scale AI 因 Meta 入股导致 OpenAI/Google 撤单** —— 这是 AI PM 选标注供应商时要警惕的「中立性 / 数据竞争」信号（evidence: [T02-S032]）。
- **来源**:
  - [Secondary] HeroHunt 数据标注行业总览: https://www.herohunt.ai/blog/the-ultimate-ai-data-labeling-industry-overview/
- **可信度**: medium（行业格局类信息，未拉 vendor 一手）
- **Decay risk**: medium（供应商格局受并购 / 数据竞争影响波动）

### 16. Argilla / Label Studio（开源标注 + 数据集 curation）

- **One-liner**: 自托管标注的开源选择 —— Label Studio 任务类型最广，Argilla（Apache 2.0，已属 Hugging Face）是 NLP/LLM 数据集 curation 的社区标准。AI PM 做 error analysis 标注、攒 golden set 时的免费工具。
- **Tier**: 场景特化
- **Maintainer / Owner**: HumanSignal（Label Studio）/ Hugging Face（Argilla）
- **License**: open（Label Studio Apache 2.0 系 / Argilla Apache 2.0）
- **Maturity signals**:
  - GitHub stars（2026-05-14 实拉）：HumanSignal/label-studio 27,311 / argilla-io/argilla 4,971
  - First public release: Label Studio repo created 2019-06-19 / Argilla created 2021-04-28
  - Last commit: Label Studio 当天活跃（pushed 2026-05-14）；Argilla 近期活跃（pushed 2026-04-27）
  - Activity: healthy（两者）
- **典型使用场景**:
  - error analysis：人工读 trace、标错误、归类失败模式（Track 06 核心动作）→ 这类标注用 Label Studio / Argilla 自托管
  - RLHF 偏好数据收集、SFT 指令数据集、NLP 标注 → Argilla（evidence: [T02-S032]）
  - 任务类型杂（图 / 文 / 音 / 视频混合）→ Label Studio 覆盖最广（evidence: [T02-S032]）
- **不适合 / 替代方案**: frontier-model 级大规模标注、要专业标注员队伍 → Surge AI / Scale AI。要标注与 eval 一体的 dashboard → eval 平台（Braintrust / LangSmith）自带标注 UI。
- **生产案例**: Argilla 作为「NLP 和 LLM 数据集 curation 的社区标准」被广泛用于 RLHF/SFT 数据准备（evidence: [T02-S032]）。
- **维护者背景** (sub_skill_link): Argilla 归属 Hugging Face（与 Track 05 sources 的 Hugging Face blog 同源）。
- **近期变化** (近 12 个月): Argilla 被 Hugging Face 收编后整合进 HF 生态。
- **来源**:
  - [Primary] Label Studio repo: https://github.com/HumanSignal/label-studio（collected: 2026-05-14）
  - [Primary] Argilla repo: https://github.com/argilla-io/argilla
  - [Secondary] HeroHunt 数据标注总览: https://www.herohunt.ai/blog/the-ultimate-ai-data-labeling-industry-overview/
- **可信度**: high
- **Decay risk**: low-medium（开源标注工具品类稳定）

### 17. Datadog LLM Observability（已用 Datadog 团队的 LLM 监控）

- **One-liner**: 把 LLM trace（输入/输出/延迟/token/错误）与 APM 关联的生产监控 —— 已经用 Datadog 的团队，要 LLM 可观测性与现有 infra 监控统一时选它。
- **Tier**: 场景特化
- **Maintainer / Owner**: Datadog
- **License**: proprietary（SaaS）
- **典型使用场景**:
  - 团队已重度用 Datadog APM，要 LLM trace 与现有监控同一个面板 → Datadog LLM Observability（evidence: [T02-S024]）
  - 要把 LLM trace 与 latency / cost / 安全评估关联、用 cluster 可视化看 drift → Datadog（evidence: [T02-S024]）
- **不适合 / 替代方案**: 没用 Datadog / 要开源自托管 → Langfuse / Phoenix。要专门的 prompt 管理 / eval 工作流 → 专用 eval 平台。
- **生产案例**: Datadog 自己用 LLM Observability 评估其 AI Guard 应用以「improve quality and control cost」(evidence: [T02-S024])。
- **近期变化** (近 12 个月): 2026 扩展了 agentic AI 监控能力（监控 Bedrock / OpenAI agents）；新增 AI Guard（in-line guardrail）—— 见新兴层卡片。
- **来源**:
  - [Primary] Datadog LLM Observability: https://www.datadoghq.com/product/ai/llm-observability/（vendor docs）
- **可信度**: medium（vendor docs 一面之词，未交叉验证）
- **Decay risk**: medium

---

### 18. Claude Agent SDK（新兴 / experimental）

- **One-liner**: Anthropic 的 agent 开发 SDK，MCP-native —— 2025 起势，「2026 MCP-native 开发的推荐选择」。
- **Tier**: 新兴｜**stability: experimental**（6 个月后可能大变）
- **Maintainer / Owner**: Anthropic
- **License**: proprietary（免费，闭源 SDK）
- **Maturity signals**:
  - 出现时间: 2025（Anthropic「Building agents with Claude Agent SDK」，Track 04 提及为 building-effective-agents 的后续）
  - 早期采用者: AI Engineer 生态 / Anthropic 开发者社区
  - Activity: healthy（Anthropic 持续推进）
- **典型使用场景**: 新项目、要 MCP-native、绑定 Claude 模型 → Claude Agent SDK（evidence: [T02-S027]）。
- **不适合 / 替代方案**: 要跨 provider → 用 LiteLLM + LangGraph。简单 workflow → provider SDK 直连。
- **近期变化** (近 12 个月): 是 Anthropic「简单可组合 > 复杂框架」理念（Track 04 canon「Building Effective Agents」）的工具化产物。
- **来源**:
  - [Primary] Anthropic docs: https://docs.anthropic.com/en/docs（vendor docs）
  - [Secondary] Morph LLM frameworks: https://www.morphllm.com/llm-frameworks
- **可信度**: medium｜**Decay risk**: high（新兴层默认 high — agent SDK 12 个月内大概率显著演进）

### 19. OpenAI Agents SDK + Responses API（新兴 / experimental）

- **One-liner**: OpenAI 的 agent 编排栈 —— Agents SDK + Responses API，2026-03 收购 Promptfoo 后把 eval 能力也纳进生态。
- **Tier**: 新兴｜**stability: experimental**
- **Maintainer / Owner**: OpenAI
- **License**: proprietary（SDK 免费闭源）
- **Maturity signals**:
  - 出现时间: 2025（OpenAI 2025-03 在 Agents SDK / Responses API 接入 MCP）
  - 早期采用者: OpenAI 栈开发者
  - Activity: healthy
- **典型使用场景**: 已在 OpenAI 栈、要 Responses API 配套的 agent 编排 → OpenAI Agents SDK。
- **不适合 / 替代方案**: 跨 provider → LiteLLM + LangGraph。要厂商中立的 eval → 别只用 OpenAI 收编后的 Promptfoo，配 DeepEval / Phoenix。
- **近期变化** (近 12 个月): **2026-03 收购 Promptfoo** —— OpenAI 把 eval 工具纳入自家生态（evidence: [T02-S026]）。
- **来源**:
  - [Primary] OpenAI docs: https://platform.openai.com/docs（vendor docs）
  - [Secondary] Inference.net comparison: https://inference.net/content/llm-evaluation-tools-comparison/
- **可信度**: medium｜**Decay risk**: high（新兴层默认 high）

### 20. Google ADK（Agent Development Kit）（新兴 / experimental）

- **One-liner**: Google 的 agent 开发框架，与 Gemini 绑定 —— 框架四象限里的 agent 编排新成员。
- **Tier**: 新兴｜**stability: experimental**
- **Maintainer / Owner**: Google
- **License**: proprietary（与 Gemini 生态绑定）
- **Maturity signals**:
  - 出现时间: 2025 系（Morph 框架对比中作为 agent 框架列出）
  - 早期采用者: Google Cloud / Gemini 开发者
  - Activity: healthy（推断，Google 持续投入）
- **典型使用场景**: 已在 Google Cloud / Gemini 栈、要 agent 编排 → Google ADK（evidence: [T02-S027]）。
- **不适合 / 替代方案**: 跨 provider / 不绑 Google → LangGraph 或 provider SDK。
- **近期变化** (近 12 个月): 与 CrewAI / Claude SDK / OpenAI SDK / LangGraph 并列为 2026 agent 框架选项（evidence: [T02-S027]）。
- **来源**:
  - [Secondary] Morph LLM frameworks: https://www.morphllm.com/llm-frameworks
- **可信度**: low-medium（本次仅一个二手 source 提及，未拉 vendor 一手）｜**Decay risk**: high

### 21. CrewAI（新兴 / experimental）

- **One-liner**: 专为多 agent 编排建的 Python 框架 —— 给 agent 分清晰角色（researcher / planner / executor），靠任务交接 + 共享 context 协作。
- **Tier**: 新兴｜**stability: experimental**
- **Maintainer / Owner**: CrewAI
- **License**: open（Python 框架）
- **Maturity signals**:
  - 出现时间: 2024 系
  - 早期采用者: **DocuSign / IBM / PwC / PepsiCo**（有名字的企业采用，evidence: [T02-S027]）
  - Activity: healthy
- **典型使用场景**: 产品需要「多个有不同角色的 agent 协作」（不是单 agent 链）→ CrewAI（evidence: [T02-S027]）。
- **不适合 / 替代方案**: 单 agent / 简单 workflow → 不需要多 agent 框架。要 stateful 图编排 → LangGraph。注意 Track 04 canon 警示：多数需求是 workflow 不是 agent，更不是 multi-agent。
- **生产案例**: DocuSign / IBM / PwC / PepsiCo 用 CrewAI 做多 agent 编排（evidence: [T02-S027]）。
- **近期变化** (近 12 个月): 在 multi-agent 这个细分占住位置。
- **来源**:
  - [Secondary] Morph LLM frameworks / LangChain alternatives 搜索: https://www.morphllm.com/llm-frameworks
- **可信度**: medium｜**Decay risk**: high（multi-agent 范式本身还在早期，「6 个月后可能不存在 / 大变」）

### 22. Lakera Guard（新兴 / experimental）

- **One-liner**: 实时 AI 安全防火墙 —— 一次 API 调用同时筛输入和输出，检测 prompt injection、越狱、PII 泄露、恶意链接，不用改现有代码。
- **Tier**: 新兴｜**stability: experimental**
- **Maintainer / Owner**: Lakera AI
- **License**: proprietary（API 服务）
- **Maturity signals**:
  - 出现时间: 2023+ 系（随 LLM 产品化兴起；intake key_tools 已列 Lakera 作模型监控类）
  - 早期采用者: AI 安全敏感的企业团队
  - Activity: healthy
- **典型使用场景**: AI 产品要防 prompt injection / 越狱 / PII 泄露、要 guardrails 但不想改应用代码 → Lakera Guard（evidence: [T02-S031]）。
- **不适合 / 替代方案**: 已用 Datadog → Datadog AI Guard（in-line）。要开源 guardrails → NeMo Guardrails（Galileo 对比中提及）。注意 Track 06 警示：guardrails 是独立校验层，不是 system prompt 里写一句话。
- **生产案例**: Galileo 的 guardrails 平台对比中作为实时 AI 安全 firewall 列出（evidence: [T02-S031]）。
- **近期变化** (近 12 个月): AI guardrails 成独立赛道，多个平台竞争（Galileo / Lakera / NeMo 等）。
- **来源**:
  - [Secondary] Galileo best AI guardrails platforms: https://galileo.ai/blog/best-ai-guardrails-platforms
- **可信度**: medium｜**Decay risk**: high（guardrails 赛道年轻、fragmenting）

### 23. Datadog AI Guard（新兴 / experimental）

- **One-liner**: in-line guardrail —— 实时分析每个 prompt / 模型输出 / 工具调用，在有害动作发生前拦截。Datadog 2026 新推。
- **Tier**: 新兴｜**stability: experimental**
- **Maintainer / Owner**: Datadog
- **License**: proprietary（SaaS）
- **Maturity signals**:
  - 出现时间: 2026（Datadog 2026 扩展 LLM Observability 时新增）
  - 早期采用者: Datadog 自身（dogfooding，evidence: [T02-S024]）
  - Activity: healthy
- **典型使用场景**: 已用 Datadog LLM Observability、要 guardrails 与监控数据同面板（content filter 触发时机与 latency/cost/trace 并排看）→ Datadog AI Guard（evidence: [T02-S024]）。
- **不适合 / 替代方案**: 没用 Datadog → Lakera Guard。
- **生产案例**: Datadog 自己用它在 security 应用做 in-line guardrail（evidence: [T02-S024]）。
- **近期变化** (近 12 个月): 2026 全新功能，与 GPU Monitoring / Sensitive Data Scanner 一起作为 Datadog AI 套件扩展。
- **来源**:
  - [Primary] Datadog LLM Observability: https://www.datadoghq.com/product/ai/llm-observability/（vendor docs）
  - [Reference] Galileo guardrails 对比: https://galileo.ai/blog/best-ai-guardrails-platforms
- **可信度**: medium｜**Decay risk**: high（2026 新功能，未沉淀）

### 24. Amplitude（前 Statsig）实验栈（新兴 / experimental）

- **One-liner**: AI 产品的实验 / 灰度 / 功能门控平台 —— Statsig 提供最先进的实验引擎（sequential testing / CUPED / switchbacks / flag-to-test 即时转换），2026-05 被 Amplitude 收编。
- **Tier**: 新兴｜**stability: experimental**（不是工具新，是「归属 + 整合状态」新 —— 2026-05 收购后整合中）
- **Maintainer / Owner**: Amplitude（2026-05 起；原 Statsig）
- **License**: proprietary（SaaS）
- **Maturity signals**:
  - 收购时间: 「Amplitude 2026-05 接管 Statsig 的品牌、客户、平台」(evidence: [T02-S025])
  - 早期采用者: 原 Statsig 客户基础
  - Activity: healthy（整合中）
- **典型使用场景**:
  - AI 产品要做 feature gating / progressive rollout / A/B（Track 06 术语）→ 实验平台
  - 要最先进的实验引擎（sequential / CUPED / switchback）→ Statsig 系（evidence: [T02-S025]）
  - 「AI 压缩发布周期后，控制 production 成了更难的问题 —— 什么到达用户、谁被暴露、出问题多快能响应」(evidence: [T02-S025])
- **不适合 / 替代方案**: 要成熟治理 + 企业级可靠性 → LaunchDarkly（「AI development 的 runtime control 平台」）。有专门数据科学团队、想用 SQL 定义 metric → Eppo（但 Eppo 是 analytics-only，要另配 feature flag 工具）。
- **生产案例**: Statsig 实验引擎被定位为「最先进的可用实验引擎」(evidence: [T02-S025])。
- **近期变化** (近 12 个月): **2026-05 Statsig 被 Amplitude 收编** —— 又一个 AI 产品 PM 要警惕的「工具独立性变化」案例（与 Promptfoo→OpenAI 同类信号）。
- **来源**:
  - [Primary] Statsig: https://www.statsig.com/（vendor docs）
- **可信度**: medium｜**Decay risk**: high（收购整合期，产品定位 / 定价 / 路线 12 个月内可能大变）

---

## 选型决策树

> 节点数 8（在 5-10 区间）。每个分支可追溯到 research 笔记证据。

### 决策树 A: 你的 AI 产品在哪个阶段，核心目标是什么？

#### Branch 1: 快速验证想法 / demo 阶段（POC）
→ **LLM**: 直接用一个 frontier provider API（OpenAI / Anthropic / Gemini），不要先想模型无关层（evidence: [T02-S001/S002/S003]）
→ **编排**: provider SDK 直连 —— 「默认用最轻的能跑的」(evidence: [T02-S027])
→ **RAG（如需要）**: Chroma（嵌入式、轻量）或直接长 context 塞文档先试
→ **eval**: 先做 error analysis（人工读 50-100 个失败样本），**还不需要买 eval 平台**（Hamel: 别 premature tool outsourcing，evidence: [T02-S020]）
→ **不推荐**: LangChain（heavy abstraction、学习曲线陡，2026 已退潮，evidence: [T02-S027]）；任何重 agent 框架；这阶段就上 Pinecone/Weaviate（过早）
→ 真实案例: 「最常见模式 —— v1 用 pgvector 在已有 Postgres 库里两周 ship 到生产」(evidence: [T02-S029])

#### Branch 2: 已有 PMF，要做 production-grade
##### Branch 2a: 主要瓶颈在「质量上不去 / 不知道改动有没有用」
→ **推荐**: 建「两层 eval 工具」—— 一个 CI 框架（DeepEval / Promptfoo / RAGAS）做 ship 前回归门 + 一个平台（Braintrust / LangSmith / Phoenix）做人工标注 + 回归追踪 + stakeholder dashboard（evidence: [T02-S026]）
→ 选平台的子分支：在 LangChain/LangGraph 生态 → LangSmith；要单平台最完整 → Braintrust；要开源不要 lock-in → Phoenix（evidence: [T02-S020][T02-S026]）
→ **替代 / 不推荐**: 只用一个工具想全包 —— 「经验团队一直收敛到需要两个工具」(evidence: [T02-S026])；只让 AI 自动生成 rubric 又自动打分（Hamel: stacking of abstractions 把缺陷藏在高分背后，evidence: [T02-S020]）
→ 真实案例: 「DeepEval（CI）+ Braintrust（生产可追溯）正在成为工程主导 AI 产品团队的 de facto 标准」(evidence: [T02-S026])

##### Branch 2b: 主要瓶颈在「RAG 检索质量 / 文档处理」
→ **推荐**: 数据 ingestion 复杂 → LlamaIndex 做 ingestion；vector DB 看规模 —— < 5-10M 向量且已用 Postgres → pgvector 继续撑；要最快过滤检索 → Qdrant；要 hybrid search → Weaviate（evidence: [T02-S029]）
→ **替代 / 不推荐**: 把 RAG 失败归咎于 vector DB 选错 —— 错，RAG 失败 80% 在 chunking / 过时 embedding / 噪声源文档（Track 06）；长 context 模型出来后还无脑上 vector DB —— 先评估「直接长 context」够不够（Track 04/06 警示）
→ 真实案例: 「v1 用 pgvector ship，监控查询延迟，用量真要求了再迁」(evidence: [T02-S029])

##### Branch 2c: 主要瓶颈在「成本 / 单用户经济模型算不过来」
→ **推荐**: 加模型无关层（LiteLLM）让换模型是改参数（evidence: [T02-S004][T02-S033]）；评估成本敏感 provider（DeepSeek / Qwen / GLM）；加 gateway 层 caching（Helicone）；接入成本可见性工具（Langfuse / Helicone）
→ **替代 / 不推荐**: 把单一 provider hardcode 进产品 —— 「model-agnostic infrastructure is no longer optional，hardcode 的应用面临 recurring migration projects」(evidence: [T02-S033][T02-S027])
→ 真实案例: 2026 API 价格跨度 $0.10–$30/M input token，选型空间大（evidence: [T02-S033]）

##### Branch 2d: 主要瓶颈在「agent 不可靠 / 多步任务失败」
→ **先问**: 这真的需要 agent 吗？还是预定义路径的 workflow 就够？（Anthropic「Building Effective Agents」: 多数需求是 workflow，Track 04 canon）
→ **如果确实要 agent**: 编排用 LangGraph（stateful 图）或 provider Agent SDK（MCP-native 用 Claude Agent SDK）；工具集成走 MCP 不走私有协议（evidence: [T02-S018][T02-S021]）；上 guardrails（Lakera Guard / Datadog AI Guard）
→ **替代 / 不推荐**: 默认 LangChain 经典抽象（2026 退潮，evidence: [T02-S027]）；不做 guardrails 只在 system prompt 写一句话（Track 06）；多 agent 框架（CrewAI）—— 只在「确实需要多角色协作」时才上，多数情况单 agent 甚至 workflow 就够
→ 真实案例: CrewAI 被 DocuSign / IBM / PwC / PepsiCo 用于多 agent 编排（evidence: [T02-S027]）

#### Branch 3: 规模化阶段，特定瓶颈
##### Branch 3a: 要建数据飞轮 / fine-tune，瓶颈在标注
→ **推荐**: 小规模 / error analysis 标注 → Argilla / Label Studio（开源自托管）；frontier 级大规模 RLHF → Surge AI；多模态企业项目 → Scale AI（evidence: [T02-S032]）
→ **替代 / 不推荐**: 选标注供应商不看中立性 —— Scale AI 因 Meta 入股导致 OpenAI/Google 撤单，是数据竞争信号（evidence: [T02-S032]）
→ 真实案例: Argilla 是「NLP/LLM 数据集 curation 社区标准」(evidence: [T02-S032])

##### Branch 3b: 要严肃做实验 / 灰度 / 监控
→ **推荐**: 实验引擎 → Statsig（现 Amplitude，最先进引擎）/ LaunchDarkly（runtime control + 治理）/ Eppo（有数据科学团队 + SQL metric）；LLM 监控 → 已用 Datadog 则 Datadog LLM Observability，否则 Langfuse / Phoenix（evidence: [T02-S024][T02-S025]）
→ **替代 / 不推荐**: 选了正在被收购整合的工具不评估风险（Statsig→Amplitude、Promptfoo→OpenAI 都是 2026 的独立性变化案例）
→ 真实案例: 「AI 压缩发布周期后，控制 production 成了更难的问题」(evidence: [T02-S025])

---

## 避坑清单

- ❌ **不要在 2026 还把 LangChain 当默认建 LLM app 的方式**：2023 的默认选择，2026「很多团队在 production 里主动移除」—— heavy abstraction、复杂 debugging、layered abstraction 学习曲线陡。新项目默认「最轻的能跑的」（通常是 provider SDK），感到真实痛点再上框架。(evidence: [T02-S027])
- ❌ **不要把 RAG 等同于 vector DB / 把 RAG 失败归咎于数据库选错**：RAG 是「检索→上下文组装→生成」三步管线，vector DB 只是可选一环；RAG 失败 80% 在 chunking / 过时 embedding / 噪声源文档。Pinecone 类厂商营销把「做 AI 必须有 vector DB」植入认知 —— Track 06 已标为厂商错位包装。(evidence: Track 06 / [T02-S029])
- ❌ **不要 premature tool outsourcing —— 别用 eval 平台替代 error analysis**：Hamel 明示「eval 是方法论不是工具，工具只是承载」；最高 ROI 是人工读失败样本做 error analysis，不是先买个塞满通用指标的 dashboard。(evidence: [T02-S020])
- ❌ **不要信「AI 自动生成 rubric 又自动打分」的全自动 eval**：Hamel 警告这种「stacking of abstractions 把缺陷藏在高分背后」—— 对承诺「无需人工验证的全自动」功能要深度怀疑。(evidence: [T02-S020])
- ❌ **不要只用一个 eval 工具想全包**：经验团队一直收敛到「两层工具」—— 一个轻量 CI 框架做门禁 + 一个平台做人工标注 / 回归追踪 / dashboard。想用单一工具覆盖全生命周期会在团队和应用变大时崩。(evidence: [T02-S026])
- ❌ **不要把单一 LLM provider hardcode 进产品**：模型每几周一版，hardcode 的应用面临「recurring migration projects」。加 LiteLLM / provider SDK 抽象层，让换模型是改参数不是重构。(evidence: [T02-S033][T02-S027])
- ❌ **不要在 agent 产品里还选私有 tool 协议**：MCP 已是事实标准（97M 月下载、78% 企业 AI 团队生产环境用、进了 Linux Foundation）—— 2024 的各家私有协议已被收敛，选私有协议是给自己挖迁移坑。(evidence: [T02-S018][T02-S021][T02-S022])
- ❌ **不要忽视工具的「独立性变化」信号**：2026 内 Promptfoo 被 OpenAI 收购、Statsig 被 Amplitude 收编、Scale AI 因 Meta 入股被 OpenAI/Google 撤单 —— 选型时要把「这工具还独立吗 / 厂商中立吗」纳入决策，不只看功能。(evidence: [T02-S026][T02-S025][T02-S032])
- ❌ **不要把所有 AI 需求都当 agent 来做**（更别当 multi-agent）：Anthropic「Building Effective Agents」明示多数需求是 workflow 不是 agent；agent 框架是整个工具栈衰减最快的层，过早投入 = 高 rotation cost。(evidence: Track 04 canon / [T02-S027])

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 source 都强调的「工具选型原则」（候选 playbook 规则）

- **「默认用最轻的能跑的，感到真实痛点再上框架」** —— 出现于 [T02-S027]（provider SDK 优先）、[T02-S029]（v1 用 pgvector 再迁）、[T02-S020]（别 premature tool outsourcing）。**强候选 playbook**：「如果是新 AI 产品 / 新需求 → 默认 provider SDK + pgvector + 先做 error analysis，不要一上来堆框架和平台」。
- **「工具是承载，方法论才是核心」** —— 出现于 [T02-S020]（Hamel: eval 是方法论不是工具）、[T02-S026]（两层工具是分工不是银弹）、Track 06（eval 平台厂商把 eval 收编成自家功能的错位包装）。候选 playbook：「如果在选 eval/observability 工具 → 先确认你的 error analysis / golden set 方法论清楚了，工具只是把它跑起来」。
- **「模型无关 / 协议标准化是架构底线」** —— 出现于 [T02-S033]、[T02-S027]（model-agnostic not optional）、[T02-S018][T02-S021]（MCP 成事实标准）。候选 playbook：「如果在做架构决策 → LLM 接入用 LiteLLM/SDK 抽象层，工具集成用 MCP，不 hardcode provider、不选私有协议」。
- **「工具的厂商归属 / 独立性是选型变量」** —— 出现于 [T02-S026]（Promptfoo→OpenAI）、[T02-S025]（Statsig→Amplitude）、[T02-S032]（Scale AI→Meta 入股后被撤单）。候选 playbook：「选型时把『这工具还独立吗、厂商中立吗』和功能并列评估」。

### 显著的工具流派分裂（候选 智识谱系条目）

- **厚框架派 vs 薄框架派**（thick vs thin framework）：
  - **厚框架派**（代表工具: LangChain 经典抽象、早期 multi-agent 框架）—— 主张用框架的抽象层 cover 复杂度。**2026 退潮**。
  - **薄框架派**（代表工具: provider SDK、LiteLLM、LangGraph 作为「轻」编排、Anthropic「简单可组合 > 复杂框架」）—— 主张默认最轻、按真实痛点加层。**2026 主流**。
  - 与 Track 01 关联：薄框架派代表人物 = Anthropic 工程团队（Building Effective Agents）、Hamel Husain（notebook-centric、skeptical of magic）；厚框架派 = 早期 Harrison Chase / LangChain 路线（注：LangChain 自己也用 LangGraph 转向了薄）。
  - 这与 Track 04 canon「智识谱系种子」第 3 流派「agent vs workflow 实用派」高度一致 —— 可合并为同一条谱系线。
- **方法论派 vs 工具派**（在 eval 维度）：
  - 方法论派（Hamel / Eugene Yan）—— eval 是方法论，工具只是 backend data store，核心是 error analysis + 人工标注。
  - 工具派（eval 平台厂商）—— 把「eval」收编成自家产品功能，倾向 AI 自动化 rubric + 打分。
  - 行业共识明显偏方法论派（Hamel 是该主题密度最高的一手源，跨 Track 04/05/06 反复出现）。

### 新兴工具信号

- **当前活跃 / 上升的新工具数**: 7（Claude Agent SDK / OpenAI Agents SDK / Google ADK / CrewAI / Lakera Guard / Datadog AI Guard / Amplitude-前 Statsig 实验栈）
- **出现 → 主流 速度估计**: ~12-18 个月（基于 MCP history pattern —— 2024-11 开源 → 2026 进 Linux Foundation 成事实标准，约 13 个月；agent SDK 类预计类似或更快，因为有 MCP 标准化铺路）
- **新兴层全部标 decay risk: high** —— 6 个月后这 7 个里大概率有 2-3 个会显著变化（被收购 / 被整合 / 被新方案取代），符合 intake「保鲜期 6-12 个月」。

### 冷僻 / 信号薄弱

- 必备层 8 个（≥ 3 ✅）；场景特化 12 个（≥ 5 ✅）；新兴 7 个（≥ 2 ✅）—— **三层都达标，不冷僻**。
- 必备层证据 ≥ 50% 采用率：MCP 有硬数据（78% 企业 AI 团队生产环境用）；eval 平台 / vector DB / provider API 靠「≥ 3 独立 source 点名 + 中立对比文 + Hamel 一手」，未引用单一行业 survey 的精确采用率百分比 —— **这是一个软肋**：本行没有公开的「AI PM 工具栈 state-of-X survey」，必备层采用率是「多源交叉推断」而非「survey 实测」。
- **不触发整体冷僻协议**，但 Phase 2.8 诚实边界应标注：「工具栈维度信号充足，但缺一个权威的 AI-PM-specific 工具采用率 survey，必备层采用率是多源推断；且工具层 decay 极快（新兴层全 high decay，agent 框架层尤其），按 6 个月重校准」。
- **locale gap**：本 track locale=global，国内工具（DeepSeek/Qwen/GLM）只在场景特化层一张合并卡片，且证据主要靠对比文章（国内 vendor docs 未深挖、公众号/知乎黑名单不收）—— 与 Track 04/05/06 一致的「国内信号偏薄」结构性 gap，非调研不足。

### 与其他 Track 的协作回传

- **→ Track 01 figures**：本 track 强化 / 浮现的 figures —— Harrison Chase（LangChain/LangGraph）、Hamel Husain（eval 选型四准则一手，已是 Track 01 候选）。维护者背景已在卡片标注。
- **→ Track 03 workflows**：工具的「典型使用场景」直接成为 SOP 步骤候选 —— 「两层 eval 工具」配置流程、「v1 pgvector 再迁」的 RAG 演进流程、「先问是 workflow 还是 agent」的 agent 决策门。
- **→ Phase 2.1 心智模型**：「厚框架 vs 薄框架」「方法论派 vs 工具派」两条流派分裂直接进心智模型候选清单。

---

## 质量自检

- [x] 候选数 ≥ 20：撒网 ~38，retain 27（必备 8 / 场景特化 12 / 新兴 7）
- [x] 三层都有内容：必备 8（≥ 3 ✅）/ 场景特化 12（≥ 5 ✅）/ 新兴 7（≥ 2 ✅）
- [x] 每个工具有 `last_checked` 日期 + 至少 1 个带具体日期的 maturity signal（GitHub stars 全部 2026-05-12/13/14 实拉）
- [x] 选型决策树 8 个节点（在 5-10 区间），每个分支挂 evidence
- [x] 避坑清单 9 条（≥ 5 ✅）
- [x] Decay risk 字段每个工具都标了
- [x] Phase 2 接口部分填了
- [x] 黑名单合规：知乎 / 公众号 / CSDN / G2 / Capterra / Medium SEO 农场 + braintrust.dev 厂商 PR 系列全部不进 manifest

**一手来源占比**：33 条 manifest 中 verified_primary 17 条（GitHub project roots 16 + Hamel 一手 blog `hamel.dev/blog` 1）、surrogate_primary 6 条（全是 vendor docs：OpenAI / Anthropic / Gemini / Datadog / Statsig / Anthropic MCP 公告）、secondary 10 条（中立对比文 8 + Wikipedia 1 + The New Stack 1）。**verified + surrogate_primary = 23/33 ≈ 70%**（≥ 50% ✅）。注意 surrogate_primary 全是 vendor docs（按 SKILL.md 硬约束标注 note="vendor docs"，未冒充 verified_primary）。纯二手对比文 8 条，且关键 claim（eval 选型 / LangChain 退潮 / 工具独立性变化 / vector DB 选型）都有 Hamel 一手或 GitHub 实拉 stars 数据交叉。

---

*调研者注：27 retained，38 explored。最大不确定性：(1) 本行无公开的「AI PM 工具栈采用率 survey」，必备层采用率靠多源交叉推断（MCP 是唯一有硬数据的）；(2) 工具层 decay 极快 —— 本文件 6 个月内必过期，新兴层和 agent 框架层尤其；(3) GitHub stars 已 2026-05 实拉，但闭源工具（LangSmith/Braintrust/Pinecone/PromptLayer/Datadog/Statsig）无 stars 信号，靠中立对比文定位；(4) 2026 多起工具收购（Promptfoo→OpenAI、Statsig→Amplitude、Scale AI 被 Meta 入股）使「独立性」成新选型变量，下次 refresh（建议 ≤ 6 个月）重点盯这些整合后果 + 是否出现 AI-PM-specific 工具 survey。*
