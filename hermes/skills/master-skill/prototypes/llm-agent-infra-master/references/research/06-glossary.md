# Track 06 — Glossary (LLM agent infra)

> Wave 1. 15 entries. Minimal-viable for prototype.

## 总览

### Tier 1 — 核心必懂 (10)
| 术语 | Type | Insider def | Outsider tell |
|------|------|------|------|
| RAG | term + acronym | retrieval+LLM pattern | 念 R-A-G; 等同 vector DB |
| ReAct | term + acronym | reason-act loop | 当成具体 algorithm 不是 control flow |
| Tool use | term | LLM 调外部能力 | 当 framework feature 不是 model capability |
| Eval | term | systematic LLM testing | 当成 prompt 调试不是 dataset 工程 |
| Hybrid retrieval | term | sparse+dense+reranking | 「pure vector 就够」 |
| LLM | acronym | large language model | 等同 ChatGPT |
| HITL | acronym | human-in-the-loop | 当作 afterthought 不是 design choice |
| MCP | acronym + standard | Anthropic protocol | 跟 OpenAI function calling 混用 |
| Trace | term | structured agent execution log | 等同 plain log |
| In production | register marker | 真上线运营状态 | 任何 demo 都说 "in production" |

### Tier 2 — 周边熟知 (3)
Sandboxed execution / Streaming generation / Speculative decoding

### Standards (1)
MCP

### Regulations (1)
EU AI Act

---

### 1. RAG (Retrieval-Augmented Generation)

- **Type**: term + acronym (multi-type)
- **Tier**: tier-1
- **Definition (insider)**: 在 LLM 调用前先 retrieve 相关 context 喂入 prompt 的 architecture pattern. 实操上是 retrieval pipeline + LLM call 的组合
- **Definition (outsider-friendly)**: AI 回答问题时先查资料再回答的方法
- **Etymology**: Lewis et al. 2020 paper "Retrieval-Augmented Generation"
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 把 RAG 等同于「用 vector DB」— 内行 RAG 包含 hybrid retrieval, reranking, query expansion
  - `pronunciation_tell`: 念 "R-A-G" (三个字母) 而不是 "rag" (一个音节)
- **关联术语**: hybrid retrieval, reranking, vector DB, embedding, agentic RAG
- **是否被错位包装**: Pinecone/Weaviate/Chroma 经常营销为「the RAG database」(source: Pinecone homepage 2025-Q4)
- **Source**: Lewis 2020 / Vespa engineering blog
- **可信度**: high
- **Decay risk**: low (concept stable)

### 2. ReAct (Reason + Act)

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: agent 推理结构, 交替「思考下一步该做什么」+「调用工具/生成 action」
- **Etymology**: Yao et al. 2022 (single origin)
- **常见误用**:
  - `semantic_tell`: 把 ReAct 当成具体 algorithm 实现, 不是抽象 control flow
- **关联术语**: CoT, Tool use, Reflexion
- **Source**: arXiv 2210.03629
- **Decay risk**: medium (concept stable, prompt patterns decay)

### 3. Tool use / function calling

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: LLM 调用外部工具/API/函数的能力
- **常见误用**:
  - `semantic_tell`: 把 tool use 当 framework feature, 实际上是 LLM 的 capability
- **关联**: ReAct, MCP, sandboxed execution
- **Etymology**: Toolformer 2023 + OpenAI function calling 2023

### 4. Eval (LLM eval)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 评估 LLM/agent 输出质量的系统化方法; 通常包含 dataset + metric + automated judge + human validation
- **常见误用**:
  - `semantic_tell`: 用 LLM 生成的 eval set 评估 LLM (循环)
  - `register_tell`: 外行说 "eval" 通常指 prompt-tweaking; 内行说 "eval" 是 dataset + CI

### 5. Hybrid retrieval

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: sparse (BM25) + dense (vector) + 可能 reranking 的 retrieval 架构
- **常见误用**:
  - `semantic_tell`: "pure vector 就够" — 2024 前可成立, 2026 production 不行
- **关联**: RAG, reranking, BM25

### 6. LLM (Large Language Model)

- **Type**: acronym + term
- **Tier**: tier-1
- **Definition (insider)**: 大语言模型, 通常指 transformer 架构的 ≥1B 参数模型
- **常见误用**:
  - `semantic_tell`: LLM = ChatGPT (LLM 是 model class, ChatGPT 是产品)

### 7. HITL (Human-in-the-loop)

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: 在 agent 执行链路中引入人类审核 / 确认 / 干预的设计
- **常见误用**:
  - `semantic_tell`: 把 HITL 当作 afterthought, 不是 design choice from day 1
  - `register_tell`: 外行说「Human-in-the-loop AI」(过于市场化), 内行说 "HITL" (缩写专业)

### 8. MCP (Model Context Protocol)

- **Type**: acronym + standard
- **Tier**: tier-1
- **Definition (insider)**: Anthropic 2024-Q4 提出的 client-server protocol, 让 LLM 客户端 plug-and-play 不同的 tool / context 提供方
- **Etymology**: Anthropic blog post 2024-11
- **常见误用**:
  - `semantic_tell`: 把 MCP 跟 OpenAI Function Calling 混用 (不同 layer)
- **变化历史**: 2024-11 v0.1 → 2025-Q2 v0.2 → 2025-Q4 LangChain/OpenAI native support
- **Source**: anthropic.com docs

### 9. Trace (in agent observability)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 一个 agent 完整执行路径的结构化记录, 跨越多个 tool calls / sub-agents / LLM hops
- **常见误用**:
  - `semantic_tell`: 把 trace 跟「log」混用 — log 是平铺文本, trace 是结构化 hierarchical span tree
- **关联**: span, observability, eval, replay

### 10. "In production" (register marker)

- **Type**: term (register marker — language fingerprint)
- **Tier**: tier-1
- **Definition (insider)**: 真正在 production 运营的状态. 内行精确区分: prototype / staging / production / scale
- **常见误用**:
  - `register_tell`: 外行随便说「我们的 X 在 production」, 实际可能只是有 demo URL
  - `semantic_tell`: 「production-ready」 ≠ "in production" (前者是声明, 后者是事实)

### 11-13. Tier 2 — 简短

- **Sandboxed execution** (term, tier-2): isolated environment for agent code execution; e.g., E2B, Modal Functions
- **Streaming generation** (term, tier-2): incremental token output as model generates
- **Speculative decoding** (term, tier-2): inference acceleration via draft model

### 14. EU AI Act

- **Type**: regulation
- **Tier**: tier-1
- **Definition (insider)**: 全球首个 comprehensive AI 监管框架。按风险分级 (banned / high-risk / limited / minimal)
- **Etymology**: EU Parliament 2024-03 adoption, 2024-08 force, 2026-08 fully apply (Tier 1)
- **常见误用**:
  - `semantic_tell`: 「AI Act 只管 EU 内的公司」(extraterritorial 类似 GDPR)
- **变化历史**: 2024-03 → 2024-08 → 2026-08 (Tier 1) → 2027-08 (Tier 2)
- **Decay risk**: high (实施细则在 active 演化)

### 15. China 生成式 AI 暂行办法

- **Type**: regulation
- **Tier**: tier-2
- **Definition**: 中国 2023-08 公布的生成式 AI 服务管理办法, 备案制 + 安全评估 + 内容合规
- **Etymology**: 国家网信办 2023-08-15
- **变化历史**: 2023-08 暂行 → 2025-Q4 实施细则更新
- **Decay risk**: high

---

## Phase 2 提炼提示

**行业表达 DNA 直接素材** (喂给 Phase 2.5):

高频黑话 top 10:
1. RAG (单音节)
2. ReAct (双音节, "ree-act")
3. eval
4. trace
5. ship (动词)
6. in production
7. spaghetti agent (吐槽词)
8. thin / thick framework
9. eval-driven
10. agent-shaped problem (Willison 自创)

行业拒绝的厂商话术 top 5:
1. AI-powered
2. Cognitive computing
3. Intelligent automation
4. Agentic transformation
5. Human-in-the-loop AI (用 HITL 缩写代替)

外行破绽 top 10:
1. 念 "R-A-G" 而不是 "rag"
2. LLM = ChatGPT
3. 「在 production」滥用
4. RAG = vector DB
5. fine-tune 一下就好
6. agent vs assistant 混用
7. 「让 AI 自动做 X」(missing eval/trust layer)
8. ReAct 当具体 algorithm
9. tool use 当 framework feature
10. HITL 当 afterthought

**智识谱系线索**:
- MCP vs vendor function-calling: open-protocol vs proprietary 流派
- ISO/IEC 42001 + EU AI Act + self-governance: regulation-first vs innovation-first

**时效性信号**:
- 12 个月内已修订: EU AI Act 实施细则、MCP v0.2、各 model provider tool-use API
- 12 个月内预计变化: MCP 大版本、EU AI Act fully-apply Tier 1 (2026-08), 中国备案制度细则
→ master skill 时效衰减信号: HIGH

**workflow 触发种子** (喂给 Track 03 review):
- EU AI Act 2026-08 fully apply → "在 EU 部署 agent" workflow 大改
- MCP 大版本 → 任何 agent client implementation 都要重写

**冷僻信号**: 15 entries below 26 target — minimal-viable scope. ✅ industry not cold.
