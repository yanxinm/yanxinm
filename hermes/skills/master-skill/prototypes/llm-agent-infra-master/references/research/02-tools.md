# Track 02 — Tools (LLM agent infra)

> Wave 2. 8 tools across 3 tiers. Minimal-viable for prototype.

## 总览

### 必备 (3)
| Tool | One-liner | Decay | Sources |
|------|-----------|-------|---------|
| LangChain / LangGraph | Agent framework default; orchestration substrate | medium | 4 |
| OpenAI / Anthropic SDK | Native LLM API access; foundation | low | 3 |
| LangSmith / LangFuse | Observability + eval; production indispensable | medium | 3 |

### 场景特化 (3)
| Tool | When to use | Decay | Sources |
|------|------------|-------|---------|
| Vespa | Production-scale hybrid retrieval (>100M docs) | low | 3 |
| Pinecone | Hosted RAG, low-ops | medium | 3 |
| DSPy | Programmatic prompt optimization | medium | 3 |

### 新兴 (2)
| Tool | Born | Adopters | Decay |
|------|------|----------|-------|
| Pydantic-AI | 2024-Q3 | growing thin-framework crowd | high |
| Browser Use | 2024-Q4 | early agent-browser teams | high |

---

### 1. LangChain / LangGraph

- **Tier**: 必备
- **One-liner**: Agent framework default. LangGraph (graph-based, post-2025) replaces the older chain-based abstraction.
- **Maintainer**: LangChain Inc.
- **License**: MIT
- **Maturity signals**:
  - GitHub stars: 90k (2026-05-02, last_checked)
  - First public release: 2022-10
  - Last commit: < 24h
  - Activity: healthy
- **典型使用场景**: any agent project at the orchestration layer; especially graph-based multi-step or HITL flows
- **不适合 / 替代方案**: bare-prototyping (overkill — use native SDK); pure single-LLM-call apps (use ai-sdk)
- **生产案例**: Klarna AI assistant, multiple YC companies (URL placeholder)
- **维护者背景**: 与 Track 01 figure Harrison Chase 直接关联
- **近期变化**: 2025-Q1 chains → graphs pivot; LangSmith eval focus
- **来源**:
  - [Primary] LangChain blog + Interrupt keynote (2025-04, last_checked 2026-05-02)
  - [Primary] HN reaction threads
  - [Secondary] Multiple comparison articles
- **可信度**: high
- **Decay risk**: medium (12-24mo: 30% chance of significant abstraction shift; LangGraph itself may pivot)

### 2. OpenAI / Anthropic SDK (combined entry)

- **Tier**: 必备
- **One-liner**: Native LLM API access. The foundation everyone builds on top of.
- **License**: MIT (clients) / proprietary (services)
- **Maturity signals**:
  - OpenAI SDK stars: 25k+ (2026-05)
  - Anthropic SDK stars: 5k+ (2026-05)
  - Both actively maintained, multiple releases per quarter
- **典型使用场景**: any production agent
- **生产案例**: every production agent ever
- **来源**:
  - [Primary] official docs
  - [Primary] release notes
  - [Reference] universally cited
- **Decay risk**: low (foundational; specific APIs evolve but SDKs persist)

### 3. LangSmith / LangFuse

- **Tier**: 必备
- **One-liner**: Observability + eval suites. Production-indispensable for any non-trivial agent.
- **Maintainers**: LangChain (LangSmith proprietary) / LangFuse Inc. (open-source)
- **典型使用场景**: trace pipeline, eval CI, replay, regression detection
- **生产案例**: most YC AI companies adopt one of these in first 3 months post-PMF
- **近期变化**: LangFuse adoption rising 2025-Q3+ (open-source preference + cost)
- **来源**:
  - [Primary] respective docs
  - [Primary] case studies on launch blogs
  - [Secondary] HN comparisons
- **Decay risk**: medium (tool competition active)

### 4. Vespa

- **Tier**: 场景特化
- **One-liner**: Production-grade hybrid retrieval engine. For >100M docs + complex filtering + hybrid sparse-dense.
- **Maintainer**: Vespa.ai (Yahoo open-source spinoff)
- **License**: Apache 2.0
- **Maturity signals**:
  - GitHub stars: 6.0k (2026-05-02, last_checked)
  - First release: 2017
  - Activity: healthy
- **典型使用场景**: production retrieval at scale; hybrid (BM25 + vector); tensor-based reranking
- **不适合**: prototyping → use Chroma; hosted preference → use Pinecone
- **生产案例**: Spotify search, Yahoo Mail
- **来源**:
  - [Primary] Vespa docs + Spotify engineering blog
  - [Secondary] benchmark articles
  - [Reference] LangChain integration docs
- **Decay risk**: low (infrastructure-class, multi-year stable)

### 5. Pinecone

- **Tier**: 场景特化
- **One-liner**: Hosted vector DB. Default for low-ops RAG up to mid scale.
- **License**: proprietary
- **Maturity signals**: market leader, hosted, billing-scaling
- **典型使用场景**: hosted RAG, <10M docs, no ops team
- **不适合**: hybrid retrieval (limited compared to Vespa), >100M docs scale
- **生产案例**: many YC W23-W25 companies as default RAG choice
- **来源**:
  - [Primary] Pinecone docs
  - [Secondary] benchmark blog comparisons
  - [Reference] tutorials universally
- **Decay risk**: medium (vector DB market still consolidating)

### 6. DSPy

- **Tier**: 场景特化
- **One-liner**: Programmatic prompt optimization. Compiler-style approach to prompts.
- **Maintainer**: Stanford NLP / Princeton
- **License**: Apache 2.0
- **Maturity signals**:
  - GitHub stars: 19k (2026-05-02)
  - Active research-driven development
- **典型使用场景**: when prompt-eng becomes a bottleneck; want to optimize programmatically
- **生产案例**: increasing 2025; emerging beyond academic
- **来源**:
  - [Primary] DSPy paper + docs
  - [Primary] Latent Space podcast episode
  - [Secondary] HN threads
- **Decay risk**: medium (could be subsumed if model native-reasoning gets good enough)

### 7. Pydantic-AI

- **Tier**: 新兴
- **One-liner**: Type-first thin agent framework. Born in the post-LangChain critique era.
- **Maintainer**: Pydantic team
- **License**: MIT
- **Maturity signals**:
  - GitHub stars: 7k (2026-05-02)
  - Released 2024-Q3, active development
- **典型使用场景**: when you want type safety + minimal abstraction; "the thinnest framework that gives you Pydantic-grade DX"
- **来源**:
  - [Primary] Pydantic-AI docs
  - [Primary] Pydantic team blog announcement
  - [Reference] HN launch thread
- **Decay risk**: high (12mo: 40%+ chance of significant API change; new framework still finding shape)

### 8. Browser Use

- **Tier**: 新兴
- **One-liner**: Agent-browser automation library. Plays in the Anthropic Computer Use space.
- **Maturity signals**:
  - GitHub stars: 8k (2026-05-02, fast growing)
  - Released 2024-Q4
- **典型使用场景**: agent that needs to interact with web pages; alternative to Stagehand
- **来源**:
  - [Primary] repo readme + examples
  - [Secondary] X agent-engineer adoption posts
- **Decay risk**: high (12mo: 50%+ — browser-agent space has 3+ competing libs, consolidation likely)

---

## 选型决策树 (vector retrieval, sample slice)

```
你只是 prototyping (dev-time)?
→ Chroma (zero ops)

上线了, 量级 <10M docs, 无 ops 团队?
→ Pinecone (hosted)

量级 >100M docs OR 需要 hybrid sparse-dense?
→ Vespa
→ 替代: Qdrant (self-host but lighter than Vespa)

agent 需要 in-process embedded retrieval?
→ Chroma + LangChain integration
```

## 避坑清单

1. **不要用 LangChain 做 demo 后强行 production-grade 化**: 「demo works in 1 day, prod needs 6 weeks」是这一行的常态
2. **不要把 Pinecone 当 RAG 的全部**: hybrid retrieval (BM25 + vector + reranking) 才是 production-grade RAG
3. **不要在 dev 阶段强行选 Vespa**: 运维成本与 dev 阶段不匹配
4. **不要 wholesale 买 framework 的「multi-agent orchestration」**: 5 个 agent 协作的真实需求很少；多数场景是 1 agent + 5 tools
5. **不要忽略 LangSmith / LangFuse 的 trace dump 大小**: high-volume production 跑 1 周可能产生 TB 级 trace，不存就丢了，存就要分层

## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的「工具选型原则」**:
- "Framework decay risk" → 选 framework 的标准是「能在一个周末剥掉吗」
- "Production reality vs demo" → demo 跑通 ≠ production-ready
- "Hybrid retrieval > pure vector" → 现代 RAG 不是 vector DB

**显著的工具流派分裂**:
- 厚框架 (CrewAI / AutoGen) vs 薄框架 (Pydantic-AI / 直接 SDK) — current visible main split
- Hosted RAG (Pinecone) vs Self-host RAG (Vespa / Qdrant) — splits along team-ops capability

**新兴工具信号**: 2 emerging (Pydantic-AI, Browser Use). Emergence-to-mainstream: 12-18mo (Cline 是参考样本).

**冷僻信号**: 8 tools is below 18 target — minimal-viable scope. ✅ industry not cold (real industry-wide tool count would be 30+).
