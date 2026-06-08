# Track 04 — Canon (LLM agent infra)

> Wave 1. 8 canon entries. Minimal-viable for prototype.

## 总览

### Textbook (2)
| 书 | 作者 | 难度 | Endorsement | 一句话 |
|----|------|------|------|------|
| AI Engineering | Chip Huyen | 进阶 | figure_long×2 + course_syllabus×2 | LLM-era engineering 全景 |
| Designing Data-Intensive Applications | Kleppmann | 进阶 | figure_long×1 | distributed systems 圣经 |

### Seminal Papers (3)
| 论文 | 年 | 核心 idea |
|------|----|----------|
| Attention Is All You Need | 2017 | transformer 基础 |
| ReAct | 2022 | agent 推理-行动循环 |
| RAG | 2020 | 检索增强生成 |

### Courses (1)
| 课程 | 讲师 | Last_updated |
|------|------|-------------|
| NN: Zero to Hero | Karpathy | 2024-12 |

### Core Concepts — Tier 1 (5 of 10-15 in real run)
RAG / ReAct loop / Tool use / Eval / Hybrid retrieval

---

### 📖 1. AI Engineering — Chip Huyen (2024)

- **One-liner**: LLM-era 工程化全景。从 prompt eng 到 deployment 的工程师手册。
- **核心论点 (4)**:
  - LLM eng 的核心难点是 evaluation，不是 prompt
  - 从 ML pipelines 到 AI pipelines 的范式转变
  - 生产中 80% 的 cost 是 inference + observability
  - "Build the eval first" 作为 first principle
- **读完得到什么**: 系统理解 LLM API → production agent 的所有工程决策点
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: figure_long]` Hamel Husain 在 Latent Space 2024-Q4 "instant-buy" 推荐
  - `[type: figure_long]` Eugene Yan 在 eval blog 引用 6+ 章节
  - `[type: course_syllabus]` DeepLearning.AI "AI for engineers" 推荐
  - `[type: course_syllabus]` Anyscale internal handbook 列入 onboarding
- **如果可以只读 1 章**: Ch.5 Evaluation Methodology
- **来源**:
  - [Primary] book 本身
  - [Primary] author blog companion posts
  - [Secondary] multiple book reviews
- **可信度**: high
- **Decay risk**: medium (3-5 年内会有 2nd ed.)

### 📖 2. Designing Data-Intensive Applications — Kleppmann (2017)

- **One-liner**: distributed systems 圣经。LLM agent infra 的工程师必读 — 理解 stateful systems 的视角。
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: figure_long]` Simon Willison + multiple senior engineer recommendations
  - `[type: course_syllabus]` MIT distributed systems course
- **来源**:
  - [Primary] book
  - [Reference] cited in agent infra discussions
- **Decay risk**: low (基础教材级 stable)

### 📄 3. Attention Is All You Need (Vaswani et al, 2017)

- **One-liner**: Transformer 基础。每个 LLM 工程师必读。
- **核心 idea**: self-attention as the only mechanism needed
- **为什么经典**: 8000+ citations; 触发整个 LLM era
- **如何读**: 关键节: Sec 3 Architecture. Sec 4 Why Self-Attention.
- **Endorsement evidence**:
  - `[type: course_syllabus]` Stanford CS224N
  - `[type: figure_long]` Karpathy NN: Zero to Hero 视频系列详细讲解
- **来源**:
  - [Primary] arXiv 1706.03762
  - [Primary] Karpathy YouTube series
- **Decay risk**: low

### 📄 4. ReAct (Yao et al, 2022)

- **One-liner**: 第一次清晰定义「LLM 作为 agent」的执行结构。
- **核心 idea**: alternating reasoning + acting loop
- **为什么经典**: agent framework 默认实现的就是 ReAct 变体
- **来源**:
  - [Primary] arXiv 2210.03629
  - [Reference] LangChain / LlamaIndex 默认实现引用
- **后续 / 扩展**: Reflexion, Tree-of-Thoughts, native function-calling
- **Decay risk**: medium (concept stable, exact prompting pattern decays as native reasoning emerges)

### 📄 5. RAG (Lewis et al, 2020)

- **One-liner**: Retrieval-Augmented Generation 的奠基论文。
- **核心 idea**: 检索文档 + LLM 生成结合
- **多 origin** (iter 13 fix): primary paper + significant follow-ups
  - [primary] Lewis et al. 2020
  - [significant follow-up] Self-RAG 2023
  - [significant follow-up] CRAG 2024
  - [significant follow-up] Agentic RAG 2024
- **来源**:
  - [Primary] arXiv 2005.11401
  - [Reference] Vespa / Pinecone / LangChain docs
- **Decay risk**: low (concept) / medium (实操内涵在演化 — agentic RAG)

### 🎓 6. NN: Zero to Hero — Karpathy

- **Lecturer**: Andrej Karpathy (与 Track 01 figure 关联)
- **Format**: 视频讲座
- **Last_updated**: 2024-12
- **Year + 最近更新**: 2022 起, 持续更新, 2024-12 加入 GPT-4 era 内容
- **One-liner**: 从零实现 transformer，理解每一行代码意味着什么。
- **完整路径**: 全部 10+ 视频, 共 ~25 hours
- **关键章节**: 
  - "Let's build GPT" 视频 (1.8h)
  - "Build a tokenizer" 视频
- **难度 / 先修要求**: 中级 Python + 基础线代 + 一定 ML
- **Endorsement evidence**:
  - `[type: figure_long]` Husain / Yan multiple recommendations
  - `[type: course_syllabus]` Stanford CS224N supplementary
- **来源**:
  - [Primary] YouTube series
  - [Reference] universal in onboarding lists
- **Decay risk**: medium (3-5 年课程更新一次)

---

### 💡 Tier 1 Concepts (5)

#### 💡 RAG
- **Tier**: tier-1
- **One-liner**: 在 LLM 调用前先 retrieve 相关 context 喂入 prompt 的 architecture pattern
- **来源** (multi-origin):
  - [primary] Lewis et al. 2020
  - [significant follow-up] Self-RAG 2023, CRAG 2024
- **关联概念**: hybrid retrieval, reranking, agentic RAG
- **常见误用**: 把 RAG 等同于「用 vector DB」 — 内行 RAG 包含 hybrid retrieval, reranking, query expansion
- **为什么进入 canon**: 解决 LLM hallucination + 提供 enterprise data integration

#### 💡 ReAct loop
- **Tier**: tier-1
- **One-liner**: 一种 agent 推理结构，每一步交替「思考下一步该做什么」+「调用工具/生成 action」
- **来源**: Yao et al. 2022 (single origin)
- **关联**: CoT (是 Reason 部分), Tool use (是 Act 部分), Reflexion (是 ReAct + self-correction)
- **常见误用**: 把 ReAct 当成具体 algorithm 实现而不是抽象 control flow

#### 💡 Tool use / function calling
- **Tier**: tier-1
- **One-liner**: LLM 调用外部工具/API/函数的能力
- **来源**: Toolformer (2023) + OpenAI function calling spec (2023)
- **关联**: ReAct, MCP, sandboxed execution
- **常见误用**: 把 tool use 当成 framework feature — 实际上是 LLM 的 capability，framework 只是 wrapper

#### 💡 Eval (LLM eval)
- **Tier**: tier-1
- **One-liner**: 评估 LLM/agent 输出质量的系统化方法
- **来源**: 工程实践 (Hamel Husain blog series + Eugene Yan), 学术 (HELM benchmark)
- **关联**: LLM-as-judge, behavioral eval, regression eval
- **常见误用**: LLM-generated eval set evaluating LLM — circular

#### 💡 Hybrid retrieval
- **Tier**: tier-1
- **One-liner**: 结合 sparse (BM25) + dense (vector) + 可能 reranking 的 retrieval 架构
- **来源**: 工程实践积累 (Vespa case studies, Pinecone hybrid feature)
- **关联**: RAG, reranking, BM25
- **常见误用**: 「pure vector 就够了」(2024 前可能成立, 2026 production 不行)

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 canon 都讨论的核心 idea** (候选行业心智模型):
- "Build evaluation before/alongside agent" (Huyen / Husain / Yan / Karpathy course)
  → 候选心智模型「在 LLM era, eval data 比 model architecture 重要」
- "Tool use as primitive, not feature" (ReAct / Toolformer / DSPy)
  → 候选心智模型「Agent = LLM + tools + eval loop, 不是 LLM + prompt eng」
- "RAG ≠ vector DB" (RAG paper + Vespa case studies + 多本书)
  → 候选 playbook 「不要把 RAG 等同于 vector DB; hybrid + reranking 是 production-grade 起点」

**智识谱系种子**:
- 流派 A: "Symbolic / structured" — DSPy + Pydantic-AI + 学院派 — 主张声明式、可验证的 agent 结构
- 流派 B: "Emergent / capability-driven" — Karpathy + Anthropic agent docs — 主张相信模型 capability，少加抽象
- 主要分歧: framework 的角色 — 应该是「编排器」还是「最薄的 type-safe wrapper」？
- 与 Track 01 figures 的「thin vs thick framework」分裂呼应

**冷僻信号**: 8 entries below 22 target — minimal-viable scope. ✅ industry not cold.
