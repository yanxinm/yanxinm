# ai-product-manager — Phase 0 Intake

> 自动模式 by 2h 蒸馏 cron (2026-05-13 第 2 轮)
> Canonical pipeline 输入:`skill/prototypes/ai-product-manager-master/intake.json`

## 1. 行业定义

**中文**:AI 产品经理 — LLM 应用 / 生成式 AI / Agent 产品 / Copilot 嵌入式 AI 的产品经理实战(跨模型评估 / 工作流设计 / 产品-工程协同 / 成本-质量-延迟三角)

**English**:AI Product Manager — practitioner role at intersection of traditional PM and LLM/generative-AI application engineering: scoping, eval-driven iteration, prompt + RAG + agent design, model selection, cost-quality tradeoffs, multimodal product surfaces.

**Industry type**:`cross_functional_practitioner`
**Locale**:`global`(海外路径 + 国内路径都需覆盖,职责差异大)
**Profile**:`practitioner`(在职 AI PM / 想转岗的传统 PM / 想 hire AI PM 的领导者)
**Focus**:`operational` 为主 + `technical` 为辅

## 2. 核心子领域候选(Phase 1 调研维度)

1. **LLM 应用产品** — 对话助手 / Copilot / agent / 工作流嵌入式 AI
2. **Eval-driven 产品迭代** — offline eval / golden set / 在线 A/B / 人工标注 / 自动评估器
3. **Prompt + Context 工程** — system prompt / few-shot / chain-of-thought / context window 设计
4. **RAG 产品设计** — 向量库 / 检索质量 / 引用展示 / 上下文新鲜度
5. **Agent 产品** — 工具调用 / 多步推理 / 失败回退 / 用户控制权
6. **多模态产品** — 图 / 视频 / 音频 / 跨模态 — 用户预期 + 延迟
7. **模型选型与切换** — 成本 vs 质量 vs 延迟三角
8. **AI 数据飞轮** — 用户反馈 → 数据 → 模型升级 → 产品差异化
9. **AI 失败 + 安全** — 幻觉 / 越狱 / 偏见 / 用户信任修复
10. **AI 产品 GTM** — 差异化定位 / 定价 / 教育用户 / 处理炒作
11. **AI 团队协作** — PM + ML 工程师 + 数据 + 标注 + 法务 + 安全的协作模式

## 3. 关键人物候选

> 注:列出的是公开作品 / 公开身份明确的人物。SKILL.md 中引用必须基于他们公开发表的具体内容,不能传话。

**海外**:
- **Marily Nika** — 前 Google / Meta AI PM,著《Building AI-Powered Products》,AI PM Bootcamp 创办
- **Aakash Gupta** — Product Growth newsletter,频繁覆盖 AI PM
- **Lenny Rachitsky** — Lenny's Newsletter,综合 PM 含 AI 访谈
- **Linus Lee** — Notion AI 早期 PM / 研究员,公开写作
- **Pete Huang** — The Generalist newsletter,AI 商业洞察
- **Hilary Mason** — 数据 / AI 产品历史人物(Cloudera / Accel)
- **OpenAI / Anthropic 高管圈** — Mira Murati / Kevin Weil / Aravind Srinivas / Olivia Pichet

**国内**:
- **朋克熊** — 《AI 产品经理:从 0 到 1》作者
- **唐辰** — 混沌 AI / 元帅训练营创办
- **Plus**(公众号)— AI 工具评测
- **凡人小北** — 知乎 AI 产品高赞答主
- **字节 / 月之暗面 / 智谱 AI PM 圈**(具体人物需 Phase 1 一手核实)

## 4. 关键工具候选

| 类别 | 工具(2025 default choice) |
|------|----------------------------|
| LLM API | OpenAI / Anthropic / Google Gemini / DeepSeek / Qwen / GLM / Moonshot |
| Eval 平台 | LangSmith / BrainTrust / Arize Phoenix / OpenAI Evals / Promptfoo |
| Prompt 管理 | LangFuse / PromptLayer / Helicone / Pezzo |
| RAG / Vector DB | Pinecone / Weaviate / Qdrant / Chroma / pgvector |
| 数据标注 | Surge AI / Scale AI / Argilla / Label Studio |
| 实验 / A/B | Statsig / Eppo / LaunchDarkly + LD AI / Optimizely |
| Agent 框架 | LangChain / LlamaIndex / DSPy / Mastra / Anthropic SDK / OpenAI Assistants API |
| 模型监控 | Datadog LLM Observability / Lakera / Whylabs |
| 用户反馈 | Pendo / Sprig / Hotjar(AI 专属反馈尚未成熟) |

## 5. 信息源候选(Phase 1 Track 05)

**Newsletter / Blog(一手)**:
- Lenny's Newsletter + Lenny's Podcast(综合 PM,AI 专题访谈)
- Aakash Gupta — Product Growth
- AI PM Bookclub(Marily Nika 系)
- Reforge(收费但有 AI PM 课程)
- Eugene Yan / Chip Huyen / Hamel Husain / Simon Willison 个人博客

**Podcast**:
- Latent Space
- The Cognitive Revolution
- a16z AI
- Eye on AI
- Lenny's Podcast

**Twitter / X**:
- Karpathy / Aravind / Simon Willison / swyx / Hamel Husain / Eugene Yan

**国内**:
- 即刻 AI 产品圈 / 小红书 AI PM 专栏 / 知乎 AI 产品话题
- 公众号:混沌大学 / PMTalk / 人人都是产品经理 AI 专栏 / Plus 评测 / 朋克熊
- 飞书文档行业模板

**书**:
- 《Building AI-Powered Products》(Marily Nika)
- 《Inspired》(Marty Cagan,PM 基础课)
- 《AI 产品经理:从 0 到 1》(朋克熊,国内入门)

**学术 / 业界结合**:
- ArXiv:eval / RAG / agent 选读
- Stanford CS324 / CS324H 课件

## 6. 警示与边界(写入 SKILL.md 诚实边界)

1. **角色定义严重不统一**:同一职位「AI 产品经理」可指 (1) 传统 PM + AI 项目 (2) 技术 PM (PM + ML 工程能力) (3) 模型评估专员 + PM (4) AI 应用业务负责人。SKILL.md 必须先讲清楚,避免读者期望落空。
2. **技能保鲜期极短**(6-12 个月):GPT-4 时代 prompt 工程心法在 GPT-4o / Claude 3.5 时代多数过时;RAG 在 2M token 长 context 模型下重要性下降;agent 框架 2023 经典写法 2025 被批为「过度抽象」。
3. **信噪比极差**:大量「7 天速成 AI PM」「AI PM 月入 5 万」营销课,真知识被掩埋。研究时狠筛课程导流 + speculative blog。
4. **学派分歧大**,同问题不同派给完全不同建议:
   - 模型派(frontier 模型上做轻应用,等模型升级 cover)
   - 工作流派(AI 嵌入现有 SaaS 工作流,核心价值在 workflow)
   - Agent 派(LLM + tools + memory 自主决策)
   - 数据飞轮派(差异化在私有数据 + RLHF + fine-tune)
5. **国内外路径差异大**:海外 AI PM 偏「产品 sense + 一定技术理解」;国内常被推到「PM + 部分工程 + 部分销售」全能岗,职责范围大但深度受限。
6. **「Prompt engineering 是 AI PM 核心」是片面认知**:真正核心是 (a) eval 设计 (b) 产品 fit 判断 (c) 团队协作 — prompt 工程只是输出之一。
7. **工资 / 招聘 / 晋升信息不透明**:2024-2025 海外 80k-400k USD,国内 50w-150w RMB,同 title 同公司差异极大。SKILL.md **避免给具体数字**。
8. **成本控制是被忽视的硬技能**:多数 AI PM 课程不教「token 单价 × 用户行为 × 留存 → 单用户经济模型」,但这是产品能不能 ship 的硬约束。

## 7. 与现有 skill 的去重

| 邻近 skill | 重叠 | 评估 |
|-----------|------|------|
| llm-agent-infra | ~20% | 都涉及 RAG / agent / eval,但视角完全不同:infra 是 SRE / 工程师怎么搭,AI-PM 是 PM 怎么决定该 ship 什么 / 怎么 ship |
| monetize-agents | ~15% | 都涉及 GTM 但 monetize 重商业模式,AI-PM 重产品本身 |

**结论**:独立 skill 可行。

## 8. 调研工时估算

| 轨道 | 强度 | 备注 |
|------|------|------|
| Track 01 figures | medium | 海外 + 国内合计 12-15 核心人物 |
| Track 02 tools | heavy | 10 大类工具,每类 3-5 个 + 选型 rationale |
| Track 03 workflow | heavy | 端到端 5-stage workflow,每阶段 5-10 动作 |
| Track 04 canon | medium | 3-4 本书 + 5-8 篇 blog + 3-4 个 talk |
| Track 05 sources | medium-heavy | 海外 4-5 newsletter+podcast + 国内 3-4 公众号 |
| Track 06 academic | medium | 5-8 篇论文 + 2-3 个课件 |

**预估总工时**:30-40h 高质量调研 + 12-16h synthesis(单人估算,可并行)

## 9. 下一步

1. 用户如需修正 intake.json,直接编辑 `skill/prototypes/ai-product-manager-master/intake.json`
2. 后续 cron / 手动 → 进入 **Phase 0.5**(目录 + Track 模板)→ **Phase 1**(6 轨调研 swarm)
3. 调研产出落到 `skill/prototypes/ai-product-manager-master/research/`
4. **本轮 cron 只完成 Phase 0**;Phase 1 留给后续

---

**Phase 0 status**:`done` — intake.json + intake.md 双产出
**Cron 第 2 轮**:2026-05-13 16:xx local(8873c713)
