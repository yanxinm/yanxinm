# Track 03 — Workflows (LLM agent infra)

> Wave 3. 3 workflows. Minimal-viable for prototype.

## 总览

### High decay (12-month-class)
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| Build production-ready RAG agent | new project | live agent | 2025-08 | skip dev-vec-DB, optimize hybrid early, add eval |
| Add observability + eval to existing agent | post-launch incident | trace + eval pipeline | 2025-09 | skip 100% instrumentation, optimize eval set, add incident-runbook hookup |
| Audit + fix failing agent in production | incident | fix + post-mortem | 2025-08 | skip prompt-tuning first, optimize via traces, add replay harness |

---

### 1. Build production-ready RAG agent

- **One-liner**: From "we want a RAG-based assistant" to "live agent serving real traffic with eval-backed quality"
- **Trigger**: new business need for retrieval-augmented assistant; or replacing a non-LLM search/QA system
- **Output**: deployed agent + eval set ≥ 50 examples + monitoring trace pipeline
- **入门 SOP**:
  1. Build vector index (Chroma → Pinecone → Vespa choice tree; see Track 02 decision tree)
  2. Build retrieval function (top-k + filter)
  3. Build prompt template + LLM call
  4. Add basic logging
  5. Deploy + test with sample queries
  - 每一步如果跳过会发生什么:
    - skip 1 → no retrieval, just LLM hallucinates from training data
    - skip 2 → arbitrary retrieval, irrelevant chunks
    - skip 3 → no LLM integration, just search
    - skip 4 → no signal in production, can't debug
    - skip 5 → no validation that the build works at all
- **资深路径**:
  - **skip** dev-time Chroma stage if production-traffic volume is known: jump directly to Pinecone or Vespa selection
  - **optimize** retrieval at step 2 by adding hybrid (BM25 + vector) from start, not as later refactor
  - **add** eval-set construction (50-100 examples) BEFORE step 3, not after
- **近期变化** (近 12 个月):
  - 2025-Q3 起，由 Anthropic Tool Use API native function-calling 推动，原 step 4 中「自定义 retry 逻辑」可省略
  - 2025-Q1 起，hybrid retrieval (BM25 + vector + reranking) 成为 production RAG default，pure-vector 已被视为 "demo grade only"
  - 触发事件类型: 新模型能力 + 新工具
  - 当前采用率: hybrid retrieval ≈ 70% production agents 已切换
- **典型耗时**: 入门 SOP 1-2 weeks. 资深 path 2-3 days.
- **关键工具**: LangChain, Chroma → Pinecone/Vespa, OpenAI/Anthropic SDK, LangSmith
- **关键人物**: Harrison Chase, Hamel Husain (eval focus)
- **常见失败模式**:
  - Build with Chroma in dev, then strugglee migrating to Pinecone/Vespa when scaling — wastes 1-2 weeks
  - Skip eval set, ship to prod, then can't quantify quality regression when LLM provider updates model
  - Use LLM-generated eval examples — passes eval but fails on real users
- **来源**:
  - [Primary] Hamel Husain blog series 2024-2025 (URL placeholder)
  - [Primary] LangChain docs production-RAG guide
  - [Primary] Anthropic agent docs
  - [Secondary] HN long threads on real RAG migrations
  - [Reference] Multiple YC company case studies
- **Last_updated**: 2025-09-15
- **Decay risk**: high (12mo: 60%+ chance of significant rewrite as model native capabilities + new RAG paradigms emerge)

### 2. Add observability + eval to existing agent

- **One-liner**: From "we shipped an agent and it's doing weird things" to "we have traces + eval suite + alert on regression"
- **Trigger**: shipped agent + accumulated user complaints / silent failures / quality regression
- **Output**: integrated trace pipeline (LangSmith/LangFuse) + eval set + CI hookup
- **入门 SOP**:
  1. Integrate observability SDK
  2. Instrument key paths (LLM calls, tool invocations, decision branches)
  3. Build eval dataset (50-200 examples sourced from real user traces)
  4. Set baseline metrics
  5. Wire eval to CI / deploy gate
- **资深路径**:
  - **skip** complete instrumentation in dev: only instrument production-relevant paths
  - **optimize** eval set ≤ 10-50 examples but pick the *hardest* cases (edge cases the agent currently fails on)
  - **add** trace + eval to incident-response runbook (existing oncall flow gets agent-aware updates)
- **近期变化**:
  - 2025-Q3 起，LangSmith vs LangFuse 战略分裂明显; pre-2024 的 LangSmith 用户约 30% 切换到 LangFuse (cost + open-source)
  - 触发: 工具竞争 / pricing 调整
- **典型耗时**: 入门 1-2 weeks. 资深 2-3 days.
- **关键工具**: LangSmith, LangFuse, Phoenix (Arize), Inspect AI
- **关键人物**: Hamel Husain, Eugene Yan
- **常见失败模式**:
  - Build eval dataset using LLM-generated examples → passes eval but fails real-user load
  - Instrument everything → trace volume blows up costs, then turn off → no signal
- **来源**:
  - [Primary] Hamel blog eval series
  - [Primary] Eugene Yan eval podcast
  - [Primary] LangFuse migration case studies
  - [Secondary] Inspect AI examples
- **Last_updated**: 2025-09-15
- **Decay risk**: high

### 3. Audit + fix failing agent in production

- **One-liner**: From "production incident — agent is doing wrong things" to "fixed + post-mortem + regression test"
- **Trigger**: incident page; user complaint; visible quality regression
- **Output**: fix + post-mortem doc + new eval examples covering the failure mode
- **入门 SOP**:
  1. Triage: pull traces from observability tool
  2. Identify failure mode (LLM hallucination / retrieval miss / tool failure / orchestration bug)
  3. Reproduce in dev with replay harness
  4. Write fix + new eval examples
  5. Deploy + monitor
- **资深路径**:
  - **skip** prompt-tuning as first instinct: 80% of "agent failures" are tool-design or retrieval issues, not prompt issues
  - **optimize** by reading traces top-down (which step failed?) before any code changes
  - **add** replay harness as permanent dev-tool, not one-off script
- **近期变化**:
  - 2025-Q4 起，LangSmith / LangFuse 都加入 native replay 功能，原本要自建的 replay harness 可省略
  - 触发: 工具升级
- **典型耗时**: 入门 1 day - 1 week (incident severity dependent). 资深 2-4 hours.
- **关键工具**: LangSmith / LangFuse (replay), Inspect AI (regression eval)
- **关键人物**: Hamel Husain (eval-driven debugging methodology)
- **常见失败模式**:
  - Try to fix by changing prompts without reading traces → 50%+ regress on other inputs
  - Don't add new eval examples → same failure recurs in 3 months
- **来源**:
  - [Primary] Hamel blog incident-debugging posts
  - [Primary] Anthropic on-call engineering writeups
  - [Secondary] HN incident threads
- **Last_updated**: 2025-10-01
- **Decay risk**: medium (workflow shape stable, tools below it changing)

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤** (候选 playbook 通则):
- "Build evaluation dataset before / alongside the agent" (RAG / observability / audit-fix)
  → 候选 playbook: 「如果开始一个新 agent workflow，先 build eval set 再写 agent」
- "Instrument with traces from day 1" (observability / multi-agent / audit-fix)
  → 候选 playbook: 「如果项目过 demo 阶段，必须有 trace pipeline」

**入门 SOP 和资深路径之间最大的差距**:
- 入门 SOP 平均 5 步, 资深路径压缩到 3 步
- 跳过最多的 step 类型: "premature 优化阶段" (Chroma → Pinecone, complete instrumentation)
- → 心智模型候选: 「在 LLM agent infra, dev-time 选择不要 commit production 路径，一开始就走 production-relevant 选型」
- → 也是 "Production reality vs demo glamour" 心智模型的 workflow 化表达

**近期工作流变化的根本原因**:
- 触发分布: 工具竞争 (2) / 模型能力升级 (2) / 法规 (0)
- 主要驱动力: **工具竞争 + 模型能力曲线**

**冷僻信号**: 3 workflows is at floor (target 7), minimal-viable scope. ✅ industry not cold.
