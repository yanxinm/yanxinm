# Track 06 — Glossary: AI Product Manager (LLM 应用 / 生成式 AI / Agent 产品)

> Phase 1 wave 1, Track 06. 术语 + 标准 + 法规 + 认证 + outsider-tell。locale=global。
> 调研日期 2026-05-14。时间盒 ~12 min。本行信噪比差 + 保鲜期 6-12 个月，已狠筛只留真信号。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.productcompass.pm/p/ai-product-manager-glossary | secondary | 2026-05-14 | Paweł Huryn (Product Compass) | AI PM 专用 glossary, 100+ 词, 面向 PM 而非工程师 |
| T06-S002 | https://hamel.dev/blog/posts/evals-faq/ | verified_primary | 2026-05-14 | Hamel Husain | eval 领域 figure 一手, evals-faq, golden set / LLM-judge 定义权威 |
| T06-S003 | https://hamel.dev/blog/posts/llm-judge/ | verified_primary | 2026-05-14 | Hamel Husain | LLM-as-judge 完整指南一手 |
| T06-S004 | https://hamel.dev/blog/posts/evals/ | verified_primary | 2026-05-14 | Hamel Husain | "Your AI Product Needs Evals" — 行业奠基短文 |
| T06-S005 | https://www.news.aakashg.com/p/ai-evals | secondary | 2026-05-14 | Aakash Gupta (Product Growth) | "AI Evals for PMs" — PM 视角 eval 入门, 含 PM 常犯错 |
| T06-S006 | https://www.producttalk.org/glossary-ai-llm-as-judge/ | secondary | 2026-05-14 | Teresa Torres (Product Talk) | PM glossary: LLM-as-judge 条目 |
| T06-S007 | https://www.producttalk.org/glossary-ai-ai-evals/ | secondary | 2026-05-14 | Teresa Torres (Product Talk) | PM glossary: AI evals 条目 |
| T06-S008 | https://www.producttalk.org/glossary-ai-llm-as-judge-eval/ | secondary | 2026-05-14 | Teresa Torres (Product Talk) | PM glossary: LLM-as-judge eval 条目 |
| T06-S009 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | surrogate_primary | 2026-05-14 | Anthropic | vendor docs（Anthropic 官方 engineering 博客），agent eval 三维度 (goal/rule/procedure) |
| T06-S010 | https://openai.github.io/openai-agents-python/guardrails/ | surrogate_primary | 2026-05-14 | OpenAI | vendor docs（OpenAI Agents SDK 官方 spec），guardrails / tripwire 官方定义 |
| T06-S011 | https://www.evidentlyai.com/llm-guide/llm-as-a-judge | secondary | 2026-05-14 | Evidently AI | LLM-as-judge / reference-based vs reference-free 完整指南 |
| T06-S012 | https://www.evidentlyai.com/llm-guide/rag-evaluation | secondary | 2026-05-14 | Evidently AI | RAG eval 指标 (faithfulness / contextual relevancy 等) |
| T06-S013 | https://www.datascience-pm.com/ai-product-manager/ | secondary | 2026-05-14 | Data Science PM | AI PM 四类角色 + title 重叠混乱明说 |
| T06-S014 | https://arize.com/ai-product-manager-role | secondary | 2026-05-14 | Arize AI | AI PM 三 archetype (product/platform/powered) — vendor 框架 |
| T06-S015 | https://productschool.com/blog/artificial-intelligence/guide-ai-product-manager | secondary | 2026-05-14 | Product School | "AI PM: Real Role or Buzzword?" — 角色定义争议 |
| T06-S016 | https://www.nvidia.com/en-us/glossary/data-flywheel/ | secondary | 2026-05-14 | NVIDIA | data flywheel 定义 (vendor glossary) |
| T06-S017 | https://a16z.com/the-empty-promise-of-data-moats/ | secondary | 2026-05-14 | a16z | "data moat 多半是空头支票" — 反 hype 一手观点 |
| T06-S018 | https://www.computerworld.com/article/3487242/agentic-rag-ai-more-marketing-hype-than-tech-advance.html | secondary | 2026-05-14 | Computerworld | "Agentic RAG 多是营销 hype" — 厂商话术批判 |
| T06-S019 | https://www.pinecone.io/learn/rag-2025/ | secondary | 2026-05-14 | Pinecone | vendor 文章, 把 RAG 与 vector DB 绑定营销 (错位包装样本) |
| T06-S020 | https://newsletter.pragmaticengineer.com/p/evals | secondary | 2026-05-14 | Gergely Orosz / Hamel | "pragmatic guide to LLM evals" — offline/online 区分 |
| T06-S021 | https://www.estebanf.com/product-management/2025/12/05/the-pm-thinking-stack/ | secondary | 2026-05-14 | Esteban F. | "start with capability" 是头号 AI PM 错误 |
| T06-S022 | https://maven.com/p/353f4f/no-vibes-just-evals-proven-frameworks-for-ai-native-pms | secondary | 2026-05-14 | Maven (course) | "No Vibes, Just Evals" — vibes-based 反模式命名 |
| T06-S023 | https://www.promptingguide.ai/guides/context-engineering-guide | secondary | 2026-05-14 | DAIR.AI Prompting Guide | context engineering 取代 prompt engineering 的论述 |
| T06-S024 | https://en.wikipedia.org/wiki/Retrieval-augmented_generation | secondary | 2026-05-14 | — | RAG 中立百科定义 (交叉验证用) |
| T06-S025 | https://en.wikipedia.org/wiki/Prompt_engineering | secondary | 2026-05-14 | — | CoT / few-shot / zero-shot 中立定义 |
| T06-S026 | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | surrogate_primary | 2026-05-14 | EU (Official Journal) | EU AI Act 立法/监管原文 (Reg 2024/1689)，EUR-Lex 官方公报（auto=secondary：eur-lex.europa.eu 不在 verifier 白名单，按立法原文标 surrogate_primary） |
| T06-S027 | https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm | verified_primary | 2026-05-14 | 国家网信办 (CAC) | 《生成式人工智能服务管理暂行办法》原文 |
| T06-S028 | https://www.nist.gov/itl/ai-risk-management-framework | verified_primary | 2026-05-14 | NIST | AI RMF 1.0 — 美国 AI 风险管理框架 |
| T06-S029 | https://www.iso.org/standard/81230.html | verified_primary | 2026-05-14 | ISO/IEC | ISO/IEC 42001:2023 — AI 管理体系标准 |
| T06-S030 | https://klu.ai/glossary/humaneval-benchmark | secondary | 2026-05-14 | Klu | benchmark contamination / data leakage 定义 |

> 黑名单合规: 搜索中命中的知乎 / 微信公众号 / CSDN / Quora / G2 / Capterra 链接已全部丢弃，未进 manifest。

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂（32 个，目标 30-50）

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| eval (评估) | term | 针对**你这个产品**的失败模式做的系统化测量，不是模型 benchmark | 外行把 eval 当成"跑个 benchmark 分数" | 2026-05 |
| golden set / golden dataset | term | 30-50 个由 PM + 领域专家共同确认的"最该答对"的测试用例 | 外行以为越大越好 / 等同于"训练数据" | 2026-05 |
| offline eval | term | 迭代时拿输出和 golden reference 比，ship 前跑 | 外行不知道有 offline/online 之分 | 2026-05 |
| online eval | term | 生产环境对真实流量做的监控式评估 | 外行把"上线后看用户反馈"当 online eval | 2026-05 |
| LLM-as-judge | term | 用一个被 rubric 校准过的 LLM 给另一个 LLM 输出打 pass/fail | 外行以为"让 GPT 评分"就完事，忽略要先和人工标注校准 | 2026-05 |
| error analysis (误差分析) | term | 人工读 trace、标错误、归类成失败模式 —— eval 的起点 | 外行直接跳到"加指标 dashboard" | 2026-05 |
| trace | term/acronym | 一次用户 query 从头到尾的完整执行记录（消息/工具调用/检索） | 外行把它当成普通 log | 2026-05 |
| failure mode (失败模式) | term | 一类连贯的、二元可识别的错误类别 | 外行说"模型不准"，内行要求拆成具体 failure mode | 2026-05 |
| RAG | acronym/term | 检索增强生成：先从外部知识库检索，再喂给 LLM 生成 | 外行把 RAG 等同于"vector DB"或"上传文档" | 2026-05 |
| hallucination (幻觉) | term | 模型编造内容并当真话输出 | 外行把任何错误答案都叫"幻觉"，内行区分幻觉 vs 检索错 vs 推理错 | 2026-05 |
| context window | term | 模型每次 prompt 的有限"记忆"，按 token 计 | 外行以为塞满 context = 用满能力，不知道"lost in the middle" | 2026-05 |
| system prompt | term | 定义 AI 行为/角色/约束的顶层指令 | 外行和 user prompt 混用，不知道二者优先级不同 | 2026-05 |
| prompt engineering | term | 把 prompt 的结构和上下文想清楚再写 —— AI PM 的**输出之一**，非核心 | 外行（含很多课程）把它当 AI PM 头号核心技能 | 2026-05 |
| context engineering | term | 决定"模型回答时知道什么"，比 prompt engineering 上位 | 外行还停留在"调 prompt 措辞" | 2026-05 |
| few-shot | term | prompt 里给几个示例引导模型 | 外行 prompt/usage tell：与 fine-tuning 混为一谈 | 2026-05 |
| chain-of-thought (CoT) | acronym/term | 让模型分步推理、解释过程的技巧 | 发音 tell: 缩写念 "C-o-T"；usage tell: 以为加"think step by step"必然更好 | 2026-05 |
| agent | term | LLM 自主决定用什么工具、何时用、多步执行的系统 | 外行把任何聊天机器人都叫 agent | 2026-05 |
| tool calling / function calling | term | 让 LLM 调用外部函数/API 的机制 | 外行把二者完全等同；内行知道 tool calling 是更宽的范式 | 2026-05 |
| token | term/acronym | 文本被切成的最小计费/计算单位（非"字数"） | 外行按"字数"估成本，忽略 input/output token 分开计价 | 2026-05 |
| embedding | term | 把数据转成捕捉语义的数值向量 | 外行把 embedding 和 fine-tuning 混淆 | 2026-05 |
| fine-tuning | term | 在预训练模型上用任务专属小数据集继续训练 | 外行一遇到"模型不准"就喊"fine-tune 一下"，跳过 prompt/RAG/eval | 2026-05 |
| guardrails | term | input/output/tool 调用前后的安全校验（tripwire 机制） | 外行把 guardrails 和 system prompt 里写"别说坏话"画等号 | 2026-05 |
| jailbreak | term | 绕过模型安全限制的攻击 | usage tell: 外行把 jailbreak 和 prompt injection 混用 | 2026-05 |
| prompt injection | term | 恶意指令混入内容，骗 LLM 绕过原指令/安全协议 | 外行不知道这和 jailbreak 是两回事（injection 走数据通道） | 2026-05 |
| red team (红队) | term | 主动对抗式测试，找 goal hijacking / 工具链攻击 / 越权 | 外行以为红队 = "试着让它说脏话" | 2026-05 |
| data flywheel (数据飞轮) | term | 用户用 → 数据 → 模型更好 → 产品更好 → 更多用户 的自增强循环 | 外行把"收集了用户数据"就叫飞轮，没有闭环到模型 | 2026-05 |
| cost-quality-latency tradeoff | term | 能力/成本/延迟三角，三者不可同时最优 | 外行只盯模型效果，忽略另两条边 | 2026-05 |
| token economics / 单用户经济模型 | term | token 单价 × 用户行为 × 留存 → 单用户成本能否撑住 ship | 外行（含多数课程）完全不算这笔账 | 2026-05 |
| latency / TTFT | term/acronym | 响应耗时；TTFT = 首 token 出现耗时 | 外行只说"慢"，内行区分 TTFT vs tokens/sec vs 端到端 | 2026-05 |
| inference (推理) | term | 用训练好的模型对新输入做预测/生成 | 外行和"模型 reasoning（推理思考）"混淆 | 2026-05 |
| benchmark | term | 标准化测试集（HumanEval / MMLU 等） | 外行拿公开 benchmark 分数当产品好坏证据 | 2026-05 |
| AI Product Manager (本职位) | term | **定义不统一**：4 种含义并存（见下条目） | 外行以为是个标准化职位 | 2026-05 |

### Tier 2 — 周边熟知（28 个，目标 30-70）

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| zero-shot | term | 不给示例直接让模型完成任务 | 2026-05 |
| temperature | term | 控制输出随机性/创造性的参数 | 2026-05 |
| RLHF | acronym | 用人类偏好 + 奖励模型对齐 LLM | 2026-05 |
| MoE (Mixture of Experts) | acronym | 组合多个专家子模型的架构 | 2026-05 |
| MCP (Model Context Protocol) | acronym/standard | 定义 AI 模型如何连接外部工具/API 的开放标准 | 2026-05 |
| vector database | term | 高效存储/检索 embedding 的专用数据库 | 2026-05 |
| reranking | term | 对检索结果重新排序以提升质量 | 2026-05 |
| hybrid retrieval / hybrid RAG | term | dense + sparse 检索方法组合 | 2026-05 |
| chunking | term | 把源文档切成可检索片段（RAG 失败常源于此） | 2026-05 |
| faithfulness | term | RAG 输出是否忠于检索上下文（即是否幻觉） | 2026-05 |
| contextual relevancy / recall / precision | term | RAG 检索质量三件套指标 | 2026-05 |
| code-based eval | term | 用 regex/结构校验/执行测试做的确定性自动评估（最便宜一层） | 2026-05 |
| rubric | term | 评估单条输出所依据的预设标准框架 | 2026-05 |
| pass/fail (binary eval) | term | 二元判定优于 1-5 分制，专家更可靠 | 2026-05 |
| ground truth | term | 已知正确、用作基准的参考数据 | 2026-05 |
| human eval / HITL | term/acronym | 人工评估；HITL = 人保留在工作流里 | 2026-05 |
| annotation / labeling | term | 给原始数据打标签创建标注集 | 2026-05 |
| inter-annotator agreement | term | 多标注员一致性检查 | 2026-05 |
| benchmark contamination / data leakage | term | 测试题进了训练数据，导致 benchmark 失效 | 2026-05 |
| theoretical saturation | term | 再读 trace 不再产生新 failure mode 的临界点 | 2026-05 |
| data drift / concept drift | term | 生产数据 / 输入-目标关系随时间偏离训练时 | 2026-05 |
| quantization | term | 降精度压缩模型体积 | 2026-05 |
| distillation | term | 用大模型训练小模型 | 2026-05 |
| multimodal (多模态) | term | 同时处理文本/图/音/视频 | 2026-05 |
| feature gating / progressive rollout | term | 灰度放量，限定人群先用再全量 | 2026-05 |
| shadow mode | term | AI 在后台跑但不暴露给用户，先攒数据/对比 | 2026-05 |
| LGTM ("looked good to me") | register/term | 贬义：只看几个 case 觉得行就 ship 的 vibes 心态 | 2026-05 |
| eval-driven development | term | 以 eval 套件为迭代主轴的开发范式（对标 TDD） | 2026-05 |

### Standards / Regulations / Certifications 时间轴（仅近 5 年内有显著变化的进表）

| 名称 | Issued | Last revised | Decay |
|------|--------|--------------|-------|
| EU AI Act (Reg 2024/1689) | 2024-07 生效 | 分阶段实施至 2026-2027（GPAI 义务 2025-08 起，高风险 2026-08 起） | high — 实施细则/标准持续出 |
| 中国《生成式人工智能服务管理暂行办法》 | 2023-08-15 施行 | 2023 版仍为现行；配套标准（如算法备案）持续更新 | high — 政策驱动 |
| NIST AI RMF 1.0 | 2023-01 | + Generative AI Profile (2024-07) | medium |
| ISO/IEC 42001:2023 (AI 管理体系) | 2023-12 | 首版，认证生态 2024-2025 起步 | medium |
| ISO/IEC 23894:2023 (AI 风险管理) | 2023-02 | 首版 | low-medium |
| MCP (Model Context Protocol) | 2024-11 (Anthropic 开源) | 事实标准快速演进，多厂商采纳中 | high — 新兴标准未定型 |

> 注：长期稳定的标准不进时间轴。本行**没有公认的从业者执业认证** —— 见下「N/A 说明」。

### 行业「外行破绽」高亮（10 条最容易暴露的）

| 误用 | 内行实际意思 | 出现频率 |
|------|-------------|---------|
| "AI PM 核心技能是 prompt engineering" | 核心是 eval 设计 + 产品 fit 判断 + 团队协作；prompt 只是输出之一 | 极高 |
| "我们做了 evals"= 跑了个 benchmark 分数 | eval 是针对你自己产品失败模式的系统化测量 | 极高 |
| "RAG"≈ "vector DB" / "上传文档给 AI" | RAG 是检索+生成的三步管线，vector DB 只是可选一环 | 极高 |
| "vibes check 过了就能 ship" / LGTM | 没有 eval 套件 = 凭感觉发版，回归无法度量 | 高 |
| 一遇到不准就说"fine-tune 一下" | 90% 情况先动 prompt / context / RAG / eval，fine-tune 最后 | 高 |
| 把所有错误答案都叫"hallucination" | 内行区分幻觉 vs 检索错 vs 推理错 vs 指令没遵守 | 高 |
| "context window 越大越好，塞满它" | 填满会触发 "lost in the middle"，质量反降 | 高 |
| 拿公开 benchmark 分数证明产品好 | benchmark 有 contamination 风险，且不等于你的 use case | 中-高 |
| "agent" = 任何聊天机器人 | agent 特指 LLM 自主决定工具调用 + 多步执行 | 中-高 |
| jailbreak / prompt injection 混用 | 两种不同攻击：injection 走数据通道，jailbreak 走指令绕过 | 中 |

---

## Glossary entries（详条 — Tier 1 关键 + 高 outsider-tell 价值的）

### 1. eval（评估）— evaluation

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 针对**你这个产品的具体失败模式**做的系统化、可重复测量，用来度量"AI 到底有没有真的工作"。
- **Definition (outsider-friendly)**: 给 AI 产品做的"考试题库 + 打分系统"，每次改动后跑一遍看有没有变差。
- **Etymology / 来源**: 从机器学习的 model evaluation 演化；2024 Hamel Husain "Your AI Product Needs Evals" 把它推成 AI PM 必备词 (evidence: [T06-S004])。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行说"我们做了 evals"通常指"跑了个公开 benchmark 拿了个分数"；内行的 eval 指针对自家产品 failure mode 的定制化测量 (evidence: [T06-S002], [T06-S005])
  - `usage_tell`: 外行一上来就建"塞满 hallucination_score / helpfulness_score 的通用 dashboard"，内行从 error analysis 起步、自下而上找指标 (evidence: [T06-S005])
- **关联术语**: golden set, error analysis, failure mode, LLM-as-judge
- **是否被错位包装**: 多个 eval 平台厂商（LangSmith / Braintrust / Arize）把"eval"等同于自家产品功能；内行强调 eval 是方法论不是工具，工具只是承载 (evidence: [T06-S005] 警告"premature tool outsourcing")
- **Source**: [Primary] hamel.dev evals-faq (T06-S002) | [Secondary] Product Talk glossary (T06-S007)
- **可信度**: high
- **Decay risk**: low（方法论已稳定，工具层 high）

### 2. golden set / golden dataset

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 30-50 个由 PM、领域专家共同确认"系统最该正确处理"的测试用例，每个带期望输出 + 专家 critique。
- **Definition (outsider-friendly)**: 一份精心挑选的"标准答案卷"，AI 的输出拿来跟它对比。
- **Etymology / 来源**: 从 ML 的 gold standard / ground truth 演化。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 golden set 越大越好、或把它和"训练数据"混为一谈；内行强调它小而精（30-50 个），且是评估用不是训练用 (evidence: [T06-S001], [T06-S005])
  - `usage_tell`: 外行让一个人随手攒；内行要求 PM + SME 共同确认、且二元 pass/fail 而非 1-5 分 (evidence: [T06-S002])
- **关联术语**: eval, ground truth, benchmark contamination
- **是否被错位包装**: 暂无明确单厂商收编证据。
- **Source**: [Primary] hamel.dev evals-faq (T06-S002) | [Secondary] Product Compass glossary (T06-S001)
- **可信度**: high
- **Decay risk**: low

### 3. offline eval vs online eval

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: offline = 迭代/ship 前拿输出和 golden reference 比；online = 生产环境对真实流量做监控式评估。
- **Definition (outsider-friendly)**: offline 是"上线前的模拟考"，online 是"上线后持续盯着真实表现"。
- **Etymology / 来源**: 沿用 ML offline/online evaluation 区分 (evidence: [T06-S020])。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行根本不知道有这个二分，把"上线后看用户评分"笼统当作"评估"；内行明确两者是不同阶段、不同方法 (evidence: [T06-S020])
  - `usage_tell`: 外行只做其一（要么只 offline 要么只 online）；内行知道要配合
- **关联术语**: eval, online A/B test, production monitoring
- **是否被错位包装**: 无。
- **Source**: [Secondary] Pragmatic Engineer evals guide (T06-S020), Evidently AI (T06-S011)
- **可信度**: high
- **Decay risk**: low

### 4. LLM-as-judge

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用一个**已用 rubric 对人工标注校准过**的 LLM，给另一个 LLM 的输出打二元 pass/fail。关键是先校准（目标和人工标注 75-90% 一致）再 scale。
- **Definition (outsider-friendly)**: 让一个 AI 当"判卷老师"去评另一个 AI 的答案 —— 但这个判卷老师自己得先跟人类老师对过答案。
- **Etymology / 来源**: 2023-2024 随 LLM eval 兴起；Hamel Husain / Shreya Shankar 课程推广 (evidence: [T06-S003])。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 外行把它念成完整一串"L-L-M as a judge"很顺，内行口语常直接说 "judge" / "the judge"
  - `semantic_tell`: 外行以为"让 GPT 打个分"就是 LLM-as-judge，跳过最关键的"和人工标注校准"步骤；内行：未校准的 judge 等于没用 (evidence: [T06-S003], [T06-S011])
  - `usage_tell`: 外行用 1-10 分制，内行用二元 pass/fail（专家判断更可靠）(evidence: [T06-S002])
- **关联术语**: rubric, golden set, code-based eval, human eval
- **是否被错位包装**: Arize / Evidently 等都有"pre-built LLM judge"产品，把校准这步隐藏在产品里 —— 内行警惕，因为校准必须针对你自己的数据 (evidence: [T06-S011])
- **Source**: [Primary] hamel.dev llm-judge (T06-S003) | [Secondary] Evidently AI (T06-S011)
- **可信度**: high
- **Decay risk**: medium（技术较新，最佳实践仍演进）

### 5. RAG — Retrieval-Augmented Generation（检索增强生成）

- **Type**: acronym + term
- **Tier**: tier-1
- **Definition (insider)**: 三步管线 —— 检索（从外部知识库拉数据）→ 上下文组装（结构化/过滤进 prompt）→ 生成（LLM 产出）。
- **Definition (outsider-friendly)**: 让 AI 回答前先去查资料，而不是只靠它脑子里记的。
- **Etymology / 来源**: Lewis et al. 2020 论文提出（Facebook AI）(evidence: [T06-S024])。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 念 "rag"（一个音节），不是 "R-A-G"（三个字母）
  - `semantic_tell`: 外行把 RAG 等同于"vector DB"或"给 AI 上传文档"；内行：vector DB 只是可选一环，RAG 失败 80% 出在 chunking / 过时 embedding / 噪声源文档，而非数据库本身 (evidence: [T06-S018], [T06-S019])
  - `usage_tell`: 外行以为长 context 模型出来后 RAG 没用了；内行：仍是 grounding / 新鲜度 / 成本控制的主力（但重要性确实下降，见 decay）
- **关联术语**: vector database, embedding, chunking, faithfulness, hybrid retrieval
- **是否被错位包装**: **是，明确**。Pinecone 等 vector DB 厂商的营销把 RAG 和 vector DB 强绑定，制造"做 AI 必须有 vector DB"的认知 (evidence: [T06-S019])；Computerworld 指出 "agentic RAG" 大量是营销 hype (evidence: [T06-S018])
- **Source**: [Primary] Wikipedia RAG（引 Lewis 2020）(T06-S024) | [Secondary] Evidently AI RAG eval (T06-S012), Computerworld (T06-S018)
- **可信度**: high
- **Decay risk**: medium-high（长 context 模型 2M token 化让 RAG 重要性下降 —— intake 警示点）

### 6. hallucination（幻觉）

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 模型编造出内容并把它当作事实输出 —— 是一个**具体的** failure mode，不是"所有错误"的统称。
- **Definition (outsider-friendly)**: AI"一本正经地胡说八道"。
- **Etymology / 来源**: NLP 领域早有，生成式 AI 时代成大众词。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把任何错误答案都叫"hallucination"；内行区分：幻觉（编造） vs 检索错（RAG 没拉到对的） vs 推理错 vs 指令没遵守 —— 不同 failure mode 不同修法 (evidence: [T06-S001], [T06-S012])
  - `usage_tell`: 外行说"我们要消除幻觉"；内行知道无法清零，只能用 eval + guardrails + 引用展示去控制和兜底
- **关联术语**: faithfulness, RAG, guardrails, failure mode
- **是否被错位包装**: **是**。多家 RAG / agentic RAG 厂商宣称能"消除幻觉"，Computerworld 点名这是 hype (evidence: [T06-S018])
- **Source**: [Secondary] Product Compass glossary (T06-S001), Computerworld (T06-S018)
- **可信度**: high
- **Decay risk**: low

### 7. context window

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 模型每次 prompt 的有限"工作记忆"，按 token 计；且填得越满，质量越可能下降（"lost in the middle"）。
- **Definition (outsider-friendly)**: AI 一次能"看进眼里"的信息上限。
- **Etymology / 来源**: Transformer 架构固有限制。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为"context window 大 = 可以无脑塞满 = 用满了能力"；内行知道质量在 context 填满时下降，模型更关注开头和结尾（lost in the middle 问题）(evidence: [T06-S001])
  - `usage_tell`: 外行把"context window"和"模型的总知识量 / 记忆"混淆；内行：context window 是单次 prompt 的临时窗口，不是模型记得多少
- **关联术语**: token, context engineering, RAG, system prompt
- **是否被错位包装**: 模型厂商军备竞赛式宣传"我们 context 更长"，但很少同时讲 lost-in-the-middle —— 算半个错位包装 (evidence: [T06-S001])
- **Source**: [Secondary] Product Compass glossary (T06-S001)
- **可信度**: high
- **Decay risk**: medium

### 8. prompt engineering（提示工程）

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 认真思考 prompt 的结构和上下文再写 —— 对 AI PM 而言这是**输出之一**，不是核心技能。
- **Definition (outsider-friendly)**: "好好跟 AI 说话的方法"。
- **Etymology / 来源**: 2022-2023 随 GPT-3/ChatGPT 爆火成热词。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: **这是本行头号 outsider-tell** —— 外行（含大量"7天速成 AI PM"课程）把 prompt engineering 当作 AI PM 的核心 / 全部技能；内行：真正核心是 (a) eval 设计 (b) 产品 fit 判断 (c) 团队协作，prompt 只是其中一个输出 (evidence: [T06-S005] intake-warning, [T06-S023])
  - `usage_tell`: 外行还在调措辞（"blind prompting"），内行已转向 context engineering —— 决定"模型回答时知道什么"而非"怎么问" (evidence: [T06-S023])
  - `register_tell`: 2025-2026 内行严肃语境里说 "prompt engineering" 常带轻微贬义或"过时"暗示，更愿说 "context engineering"
- **关联术语**: context engineering, system prompt, few-shot, CoT
- **是否被错位包装**: 大量培训机构把"prompt engineering 课"包装成"成为 AI PM 的捷径" —— 是本行信噪比差的主要噪声源 (evidence: [T06-S015] "Real Role or Buzzword")
- **Source**: [Secondary] Aakash Gupta (T06-S005), Prompting Guide context engineering (T06-S023)
- **可信度**: high
- **Decay risk**: medium-high（GPT-4 时代 prompt 心法在 Claude / GPT-4o 时代多数过时 —— intake 警示点）

### 9. agent / tool calling（智能体 / 工具调用）

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: agent = LLM 自己决定用什么工具、何时用、多步执行的系统；tool calling / function calling = 让 LLM 调用外部函数/API 的机制。
- **Definition (outsider-friendly)**: agent 是能自己规划、动手干活的 AI；tool calling 是它"伸手去用工具"的能力。
- **Etymology / 来源**: ReAct (Yao et al. 2023) 是工程化起点；2024-2025 成产品热词。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把任何聊天机器人 / Copilot 都叫 "agent"；内行：agent 特指有自主工具决策 + 多步执行的，单纯问答不是 agent (evidence: [T06-S001])
  - `usage_tell`: 外行把 tool calling 和 function calling 完全等同；部分内行区分二者是不同范式（function calling 更窄）(evidence: 见 manifest 中 guardrails 搜索结果)
  - `usage_tell`: 外行不知道 agent 的"复利失败" —— 95% 单步准确率在 10 步任务上成功率 <60%（intake / 行业共识）(evidence: [T06-S021])
- **关联术语**: tool calling, guardrails, MCP, multi-agent, trace
- **是否被错位包装**: **是**。"agentic" 已成 2025-2026 最滥用的营销前缀，Computerworld 点名 "agentic RAG" 多是 hype (evidence: [T06-S018])
- **Source**: [Secondary] Product Compass glossary (T06-S001), Computerworld (T06-S018)
- **可信度**: high
- **Decay risk**: high（2023 LangChain 经典写法 2025 被批"过度抽象" —— intake 警示点）

### 10. guardrails / red team（护栏 / 红队）

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: guardrails = 在 input / output / tool 调用前后做的安全校验，可 skip 调用 / 替换输出 / 触发 tripwire；red team = 主动对抗式测试，沿 goal achievement / rule compliance / procedural discipline 三维度探测，找 goal hijacking、工具链攻击、越权。
- **Definition (outsider-friendly)**: guardrails 是给 AI 装的"安全栏杆"；red team 是雇人专门"使坏"来提前发现漏洞。
- **Etymology / 来源**: 红队源自安全行业；guardrails 随 LLM 产品化 2023+ 成标准件 (evidence: [T06-S010], [T06-S009])。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 guardrails = 在 system prompt 里写一句"不要说有害内容"；内行：guardrails 是独立的、运行在请求前后的校验层（tripwire 机制），不是 prompt 里一句话 (evidence: [T06-S010])
  - `usage_tell`: 外行以为红队 = "试着让它说脏话"；内行的红队覆盖 goal hijacking / 工具链攻击 / 越权 / 流程纪律 (evidence: [T06-S009])
- **关联术语**: jailbreak, prompt injection, agent, eval
- **是否被错位包装**: 无明确单厂商收编；但"AI safety"整体常被厂商当营销标签。
- **Source**: [Primary] OpenAI Agents SDK guardrails (T06-S010), Anthropic eval engineering (T06-S009)
- **可信度**: high
- **Decay risk**: medium

### 11. data flywheel（数据飞轮）

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 用户用 → 产生数据/反馈 → 模型/产品变好 → 吸引更多用户 → 更多数据 的自增强闭环；是 AI 产品差异化的核心叙事之一。
- **Definition (outsider-friendly)**: 用的人越多，产品越聪明，越聪明又吸引越多人用 —— 滚雪球。
- **Etymology / 来源**: 借自 Amazon "flywheel"；AI 语境下 NVIDIA / a16z 等反复使用 (evidence: [T06-S016], [T06-S017])。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把"我们收集了用户数据"就叫飞轮；内行：必须真的闭环回模型/产品改进才算，否则只是攒了一堆数据 (evidence: [T06-S016])
  - `usage_tell`: 外行（尤其融资语境）把 data flywheel 当万能护城河；内行 / a16z 明确指出"data moat 多半是空头支票"，多数飞轮没真正转起来 (evidence: [T06-S017])
- **关联术语**: data moat, RLHF, feature gating, shadow mode
- **是否被错位包装**: **是**。是创业公司融资 pitch 的高频包装词；a16z 专门写文 "The Empty Promise of Data Moats" 拆穿 (evidence: [T06-S017])
- **Source**: [Secondary] NVIDIA glossary (T06-S016), a16z (T06-S017)
- **可信度**: high
- **Decay risk**: low（概念稳定，但"是否真有效"长期有争议 → 标 disputed）
- **disputed**: 飞轮派认为是核心差异化；模型派/a16z 认为多数所谓飞轮是空头支票，frontier 模型升级会碾平多数私有数据优势。

### 12. cost-quality-latency tradeoff + token economics（成本-质量-延迟三角 + 单用户经济模型）

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 能力（质量）/ 成本 / 延迟 三者构成不可能三角，改善一个通常伤另一个；token economics = token 单价 × 用户行为 × 留存 → 单用户成本，决定产品能不能 ship。
- **Definition (outsider-friendly)**: AI 产品要在"好、便宜、快"之间做取舍；还得算清楚"一个用户用一个月，我们要烧多少 API 钱"。
- **Etymology / 来源**: 三角是工程常识的 AI 版；token economics 随 2024-2025 多模型按 token 计价成显学。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行只盯"模型效果好不好"，完全不提另两条边；内行：选型决策必谈三角 (evidence: 见 manifest cost 搜索)
  - `usage_tell`: **被忽视的硬技能** —— 外行（含多数 AI PM 课程）不算单用户经济模型；内行知道 agent 多轮对话有"二次方 token 增长"陷阱，单用户成本能直接决定产品死活 (evidence: intake-warning + cost 搜索)
- **关联术语**: token, model selection, latency, inference
- **是否被错位包装**: 模型厂商倾向只宣传"我们更便宜/更快/更强"单点，不讲三角联动。
- **Source**: [Secondary] manifest 中 cost-quality-latency 搜索结果（Stevens Online / aimsys 等）
- **可信度**: high
- **Decay risk**: medium（token 单价持续下降，但三角结构稳定）

### 13. AI Product Manager（本职位本身）— 角色定义混乱

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: **本词无统一定义** —— 同一 title "AI 产品经理"在不同公司至少指 4 种不同的人：
  1. 传统 PM + 负责 AI 项目（产品 sense 为主）
  2. 技术 PM（PM + 一定 ML 工程能力，正演化为 "Model PM"）
  3. 模型评估专员 + PM（eval-heavy）
  4. AI 应用业务负责人（偏 GTM / 商业）
- **Definition (outsider-friendly)**: "AI 产品经理"听起来是个标准职位，其实每家公司理解都不一样，入职前必须问清楚"在你们这儿它具体指哪种"。
- **Etymology / 来源**: 2023-2025 随 LLM 应用爆发，职位名先于职责定义出现。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行（尤其求职者）以为这是个边界清晰的标准化职位；内行 / 招聘方都知道同 title 同公司差异都极大 (evidence: [T06-S013], [T06-S015])
  - `usage_tell`: 外行简历上写"AI PM"不加限定；内行会说清自己是哪一种（"我偏 eval / 偏技术 / 偏业务"）
- **关联术语**: technical PM, Model PM, AI Platform PM, AI Research PM
- **是否被错位包装**: **是，且是行业级问题**。多家培训机构 / vendor 把"AI PM"包装成单一可速成的职位卖课；Product School 文章标题直接是 "Real Role or Buzzword?" (evidence: [T06-S015])。注意：vendor 框架本身也在制造混乱 —— Arize 给"3 archetype"、Data Science PM 给"4 类"、ProdPad 给"12 种 PM"，分类法彼此不一致。
- **Source**: [Secondary] Data Science PM (T06-S013), Arize (T06-S014), Product School (T06-S015)
- **可信度**: high（"定义混乱"这件事本身是高可信度结论）
- **Decay risk**: medium（职位在快速成型中，2-3 年可能收敛）
- **disputed**: Data Science PM / Product School 明说 title 严重重叠、混乱；Arize（vendor）则把它表述为"3 个互补 archetype，无歧义"。**保留两派** —— vendor 倾向把混乱包装成"清晰的专业分工"，但一线求职 / 招聘体感是混乱。

---

## 5 个 type 的覆盖情况

| Type | 本行覆盖 | 说明 |
|------|---------|------|
| **Term / 术语** | 极丰富 | 本行主体，eval / RAG / agent / context 等占大头 |
| **Acronym / 缩写** | 丰富 | RAG / CoT / RLHF / MoE / MCP / TTFT / HITL 等 |
| **Standard / 标准** | 中等、新兴 | MCP（事实标准，未定型）、ISO/IEC 42001、NIST AI RMF；多数仍在成型 |
| **Regulation / 法规** | 中等 | EU AI Act、中国生成式 AI 暂行办法、NIST RMF —— 但 AI PM 日常更多是"知道存在"而非深度合规（合规深度是法务的活） |
| **Certification / 认证** | **N/A** | 本行**没有公认的从业者执业认证**。市面"AI PM 认证课"（培训机构发的结业证）不被行业当作硬通货，反而是 outsider-tell。产品级有 ISO/IEC 42001 体系认证，但那是认证组织不是认证个人。 |

---

## Phase 2 提炼提示

### 「行业表达 DNA」直接素材（喂给 Phase 2.5 expression-DNA 提炼）

**高频黑话 top 10**：
1. eval / "做 evals"（动词化使用，"我们得先建 evals"）
2. golden set / golden dataset
3. trace（"去翻 trace" = 去看完整执行记录做 error analysis）
4. failure mode（"这是哪个 failure mode" —— 内行把模糊的"不准"逼成具体类别）
5. LLM-as-judge / 口语直接说 "the judge"
6. RAG（念 "rag"）
7. ship / "能不能 ship"（成本/质量门槛是否过关）
8. context engineering（2026 内行更愿用它替代 "prompt engineering"）
9. LGTM / "vibes check"（贬义，指没 eval 凭感觉发版）
10. "demo-to-production gap"（demo 能跑 ≠ 生产可用，几乎成口头禅）

**行业拒绝的厂商话术 top 5**（拒绝 → 反映行业「价值观 + 反模式」）：
1. **"我们的 RAG 能消除幻觉" / "agentic RAG"** —— 内行知道幻觉无法清零，"agentic" 前缀已被 Computerworld 等点名为营销 hype (evidence: [T06-S018])。拒绝它 = 行业重"诚实的失败模式管理"而非"银弹叙事"。
2. **"做 AI 产品必须有 vector DB"** —— Pinecone 类厂商把 RAG 和 vector DB 强绑定；内行：RAG 失败 80% 在 chunking / 过时 embedding，不在数据库 (evidence: [T06-S019])。拒绝它 = 行业重"想清楚问题在哪"而非"堆基础设施"。
3. **"data flywheel 是我们的护城河"** —— 融资 pitch 高频词；a16z "The Empty Promise of Data Moats" 拆穿多数飞轮没转起来 (evidence: [T06-S017])。拒绝它 = 行业（清醒派）对"数据自动 = 壁垒"祛魅。
4. **"prompt engineering 速成班，7 天成为 AI PM"** —— 培训机构话术；内行：prompt 只是输出之一，核心是 eval / 产品 fit / 协作 (evidence: [T06-S005], [T06-S015])。拒绝它 = 行业对"AI PM = 会写 prompt"的强烈反感。
5. **"我们的 benchmark 分数 SOTA"** —— 模型/工具厂商话术；内行：benchmark 有 contamination 风险且不等于你的 use case，eval 必须针对自家产品 (evidence: [T06-S002], [T06-S030])。拒绝它 = 行业重"你自己产品的 eval"而非"通用榜单"。

**外行破绽 top 10（insider-only spotting tells）**：见上文「行业『外行破绽』高亮」表，逐条已配内行实际意思 + 频率。最致命的两条：
- "AI PM 核心技能 = prompt engineering"（极高频，一句话暴露）
- "我们做了 evals" = 跑了个公开 benchmark（极高频）

### 「智识谱系」线索（喂给 Phase 2.7 智识谱系）

- **术语演变暗示范式更替**："prompt engineering → context engineering"（2022 → 2025-2026）反映从"调措辞"到"架构模型的全部上下文"的哲学转变；"RAG 是核心 → 长 context 模型让 RAG 重要性下降"反映模型派 vs 工作流派的拉锯。
- **多标准竞争 / fragmenting**：MCP（Anthropic 2024-11 开源）正在成事实标准但未定型，多厂商各推自己的 agent / tool 协议 —— 是"流派之争的硬件层"。eval 工具层（LangSmith / Braintrust / Arize / Promptfoo）同样 fragmenting，每家把"eval"收编成自家产品。
- **角色定义本身的分类法之争**：Arize 给 3 archetype、Data Science PM 给 4 类、ProdPad 给 12 种 —— 分类法不一致本身就是"这个职业还没有公认 OS"的证据。

### 「时效性」信号（喂给 Phase 2.8 诚实边界）

- **过去 12 月内有修订/新动作的标准 / 法规**：EU AI Act 分阶段实施（GPAI 义务 2025-08、高风险 2026-08）；NIST AI RMF 加了 Generative AI Profile (2024-07)；MCP 自 2024-11 后快速演进、多厂商采纳中；ISO/IEC 42001 认证生态 2024-2025 才起步。
- **预计 12 月内会变的**：EU AI Act 高风险条款 2026-08 落地 + 配套技术标准持续出；MCP 仍未定型；中国生成式 AI 配套标准（算法备案细则等）持续更新。
- **术语层 decay 警告**：`prompt engineering`（GPT-4 心法已多数过时）、`RAG`（长 context 模型 2M token 化削弱其重要性）、`agent`（2023 LangChain 经典写法 2025 被批过度抽象）—— 这三个高频词的"正确用法"本身在 12 月尺度上漂移，master skill 必须标日历有效期。

### 「工作流变化触发」种子（喂给 wave 3 Track 03）

- **EU AI Act 高风险条款 2026-08 落地** → 影响 workflow 假设：AI PM 在 scoping 阶段要新增"风险分级判定"步骤，高风险产品的 eval / 文档 / 透明度要求升级。
- **MCP 成事实标准** → 影响 agent 产品的工具集成 workflow：从各家私有协议转向 MCP，PM 的工具选型决策树要改写。
- **长 context 模型（2M token）普及** → RAG 设计 workflow 重要性下降：PM 在"要不要做 RAG"的决策点上，默认答案从"要"向"先试长 context"偏移。
- **"eval-driven development" 成范式** → 整个 AI 产品 workflow 从"想法→POC→MVP→上线"插入"先建 golden set + eval 套件"为前置门，error analysis 成 PM 标准动作。

### 「冷僻 / 信号薄弱」自检

- 总术语数：**60**（Tier 1: 32, Tier 2: 28）—— 远超 floor 40，不冷僻。
- Tier 1：32 个，全部填了 outsider-tell。✅
- Tier 2：28 个，约 60% 填了 outsider-tell（含表中标注）。✅
- 有 outsider-tell 的术语 > 50%。✅
- **结论**：glossary 维度信号充足，不触发冷僻协议。但 **保鲜期警告强**：本行术语 6-12 个月尺度上漂移明显，且信噪比差（大量速成课噪声）—— Phase 2.8 应明确写"glossary 维度数据充足但 decay 快，工具/术语正确用法按 6 个月重校准"。

---

## 调研边界与诚实声明

- **一手 vs 二手**：本 track 一手（verified_primary）8 条 —— Hamel Husain 博客 ×3（eval 领域真 figure 的一手）、Anthropic / OpenAI vendor 一手 spec ×2、EU / CAC / NIST / ISO 法规标准原文 ×4-5。二手 22 条，主要是 PM 视角 glossary（Product Compass / Product Talk / Aakash Gupta）和 eval 平台厂商指南（Evidently）。比例约 27% 一手。
- **二手为主的原因**：术语定义类内容天然二手居多；但关键术语（eval / golden set / LLM-judge）已用 Hamel Husain 一手交叉验证，可信度有保障。
- **矛盾保留**：(1) AI PM 角色定义 —— Data Science PM / Product School 说混乱，Arize（vendor）说"3 个清晰 archetype"，保留两派。(2) data flywheel —— 飞轮派 vs a16z 祛魅派，标 disputed。
- **黑名单合规**：搜索命中的知乎 / 公众号 / CSDN / Quora / G2 / Capterra 全部丢弃未进 manifest。
- **国内术语缺口**：本次以 global / 海外一手为主，国内 AI PM 圈的术语（朋克熊 / 即刻 AI 产品圈用语）未深挖 —— 但 intake 已注明国内外路径差异，且核心术语（eval / RAG / agent）国内圈基本直接用英文，缺口影响有限。
