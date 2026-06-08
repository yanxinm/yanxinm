# Synthesis Candidates (raw) — AI Product Manager

> Phase 2 Step 0 输出。扫描 6 轨 research 的「Phase 2 接口」段 + 「Phase 2 提炼提示」段汇集。
> industry_type = `cross_functional_practitioner`,公开内容丰富,门槛按「标准 / 技术」类(≥ 12-15)。
> 汇集日期:2026-05-14。

## 候选心智模型 (target 15-30)

| # | Candidate | 出现于 tracks | 出现 figures / 来源数 | 类型 | 备注 |
|---|-----------|-------------|----------------------|------|------|
| C1 | Eval 是地基不是可选项 / 别 vibe-check | 01,03,04,06 | Hamel/Eugene/Chip/Marily + canon 5+ 源 | cross-track,极强 | 4 figure + canon 5+ 源 + glossary 头号黑话。最强候选 |
| C2 | 先 error analysis 再加功能(PM 亲自看 trace) | 01,03,04 | Hamel/Eugene + 4 个 workflow | cross-track | workflow 1/3/4/6 都含;canon 点名 |
| C3 | workflow vs agent 要分清,多数需求是 workflow | 01,02,03,04,06 | Simon/swyx/Chip/Anthropic | cross-track,强 | Anthropic 奠基文 + Simon 背书 + 5 个 track |
| C4 | AI PM 不需会训模型,但要懂 AI 能力边界 / 别做 feature theater | 01,04 | Marily/Aakash/Chip | cross-track | 最贴「AI PM 角色定义」;3 figure |
| C5 | 先简单 / 最便宜的假设,验证了才升级复杂度 | 02,03,04 | 跨 4 workflow + 选型树 + Anthropic | cross-track,强 | prompt→RAG→agent→finetune 阶梯;tool 选型同构 |
| C6 | AI 不可靠是常态,用 UX + eval 消化而非假装可靠 | 04,03 | Eugene defensive UX / τ-bench / Hamel | cross-track | pass^k 现实 + defensive UX |
| C7 | cost-quality-latency 三角 + 单用户 token 经济模型 | 04,06,03 | Chip / intake / glossary | cross-track | intake 点名「被忽视硬技能」 |
| C8 | 工具是临时承载,方法论 / 能力曲线才是永恒 | 02,01,04 | Hamel / Anthropic / 厚薄框架之争 | cross-track | LangChain 退潮 + eval 工具 fragmenting;排他性强 |
| C9 | 模型动态保鲜期极短,要持续校准(日历有效期) | 01,02,03,06 | Simon/Chip + 全 track decay | cross-track | intake「保鲜期 6-12 月」;所有 track 都标 decay |
| C10 | 数据飞轮 = 差异化(但多半是空头支票,disputed) | 04,06,03 | Eugene / a16z / NVIDIA | cross-track,disputed | 飞轮派 vs a16z 祛魅派,保留分歧 |
| C11 | 资深 AI PM = 对抗「看起来在推进」的假象,做慢但对的硬步骤 | 03 | 6 个 workflow 资深 add 高度集中 | single-track 强信号 | error analysis / judge 校准 / pass^k 门都不能跳 |
| C12 | binary pass/fail + 频率排序,不靠 vibes / 不靠 1-5 分 | 03,04,06 | workflow 3/4/5 + G-Eval + glossary | cross-track | 可能降 playbook |
| C13 | AI 时代「能不能建」不再是瓶颈,desirability 才是 | 03 | workflow 1/2 资深差异 + David Hoang | single-track | 「能力右移」的产品侧表述 |
| C14 | 能力「右移」到不做研究的人手里(AI Engineer / AI PM 新工种) | 01 | swyx / Marily / Aakash | single-track | 行业自我叙事,排他性偏弱 → 可能降 glossary |
| C15 | model-agnostic / 协议标准化是架构底线(不 hardcode provider、用 MCP) | 02 | tool 选型树 + 避坑 + MCP 多源 | single-track | 可能降 playbook(架构规则) |
| C16 | AI PM 角色定义不统一(4 种含义),先问「在你公司是哪种」 | 06,01 | glossary 详条 + Data Science PM / Arize | cross-track | 不是「思维框架」是「角色诊断」,可能进诚实边界 / 谱系而非心智模型 |
| C17 | prompt engineering 不是核心,只是输出之一 | 06,01 | glossary 头号 outsider-tell + intake | cross-track | 是 C4/C1 的反面;可能并入 C4 或进反模式 |
| C18 | judge / eval 工具 / 标注的判断不能外包(校准 domain-specific) | 02,03,06 | Hamel / workflow 3 / glossary | cross-track | 可能降 playbook(是 C1 + C8 的推论) |

## 候选 playbook 规则 (target 10-20)

| # | Pattern | 来源 |
|---|---------|------|
| P1 | 质量 / 方向不明 → PM 先亲自拉 10-50 个真实 trace 逐条标,再做任何决策 | T03 接口(4 workflow);T04 |
| P2 | 遇 AI 技术决策 → 默认从最便宜假设起(prompt→RAG→agent→finetune),验证不够才升级 | T03 接口;T04;T02 选型树 |
| P3 | 判断 AI 质量 → binary pass/fail + 频率计数,不用模糊分 / 不用「我觉得」 | T03 接口;T06;T04 G-Eval |
| P4 | 新 AI 产品 / 新需求 → 默认 provider SDK + pgvector + 先做 error analysis,不堆框架和平台 | T02 接口(强候选) |
| P5 | 选 eval / observability 工具 → 先确认 error analysis / golden set 方法论清楚,工具只是跑起来 | T02 接口;T03 |
| P6 | 做架构决策 → LLM 接入用 LiteLLM/SDK 抽象,工具集成用 MCP,不 hardcode provider、不选私有协议 | T02 接口;T02 避坑 |
| P7 | 新 AI 需求 → 先问「这是预定义路径的 workflow,还是真需 LLM 自主决策的 agent」,默认假设 workflow | T04 接口;T02 选型树 2d |
| P8 | 要 ship agent → 上线标准是「多次运行的稳定通过率 pass^k」,不是「demo 跑通一次」 | T04 接口;τ-bench |
| P9 | 模型选型 → 先明确 cost / quality / latency 哪个是硬约束,再倒推;且必算单用户 token 经济模型 | T04 接口;T06;T03 |
| P10 | LLM-as-judge → 上线前必和人工标注校准到 75-90% 一致,binary 不用 1-5 分 | T03 workflow 3;T06;Hamel |
| P11 | golden set → 小而精(30-50 个),PM + 领域专家共建,是评估用不是训练用 | T03;T06;Hamel evals-FAQ |
| P12 | POC 阶段 → 明确「为学习而造」,throwaway code 不写测试 / 不上 CI,验证完该删不该转正 | T03 workflow 2;Cagan |
| P13 | scoping 一个 AI feature → 强制从用户 pain point 起(不从模型能力起),并在文档里写下「我们现在不知道什么」 | T03 workflow 1 |
| P14 | 选型时 → 把「这工具还独立吗 / 厂商中立吗」和功能并列评估(Promptfoo→OpenAI、Statsig→Amplitude 信号) | T02 接口;T02 避坑 |
| P15 | RAG 检索质量差 → 别归咎 vector DB 选错,先查 chunking / 过时 embedding / 噪声源文档(80% 在这) | T02 选型树 2b;T06 |
| P16 | 质量上不去 → 第一反应是抵抗「加功能」冲动,先做 error analysis | T03 workflow 4 资深 skip |

## 候选工具流派分裂 (智识谱系)

| # | Split | A 派代表 | B 派代表 |
|---|-------|---------|---------|
| S1 | 厚框架 vs 薄框架 (thick vs thin) | LangChain 经典抽象 / 早期 multi-agent 框架(2026 退潮) | provider SDK / LiteLLM / LangGraph 作轻编排 / Anthropic「简单可组合 > 框架」(2026 主流) |
| S2 | 方法论派 vs 工具派 (eval 维度) | Hamel / Eugene Yan(eval 是方法论,工具是 backend) | eval 平台厂商(把 eval 收编成自家功能 + AI 自动 rubric) |
| S3 | 工程派 vs 产品 sense 派 (AI PM 核心是什么) | Hamel/Eugene/Chip(核心 = eval + 技术理解) | Marily/Lenny 承接 Cagan(核心 = 产品判断 + AI 能力边界感) |
| S4 | 模型派 vs 工作流派 vs agent 派 vs 数据飞轮派 (intake 四流派) | 模型派(等 frontier 升级 cover 一切)/ agent 派(LLM+tools+memory 自主) | 工作流派(价值在 workflow 非模型)/ 数据飞轮派(差异化在私有数据) |
| S5 | RAG 必要性之争 | RAG 论文系 / vector DB 厂商(RAG 是默认武器) | Simon Willison(长 context 2M token 削弱 RAG 部分场景) |
| S6 | AI PM 要不要会代码 / 懂模型 | CS336 深水区路线(技术 PM) | Andrew Ng「Generative AI for Everyone」非技术路线 |
| S7 | 行业生态 / 工种叙事派 vs 实务派 | swyx / 部分 Aakash(命名、组织 AI Engineer / AI PM 工种) | 被批「给已有工作贴新标签 / 造词」 |

## 候选反模式

| # | Anti-pattern | 来源 |
|---|-------------|------|
| A1 | 跳过 error analysis 直接上指标 dashboard(测的是噪声) | T03;T06 |
| A2 | 「我们做了 evals」= 跑了个公开 benchmark 分数 | T06 outsider-tell 极高频 |
| A3 | LLM-judge 没和人工校准就 scale(没校准 = 没用) | T03;T06 |
| A4 | demo 当 ship 门 / 在假数据上做漂亮 demo(demo-to-production gap) | T03;T06 |
| A5 | 一遇到不准就喊「fine-tune 一下」(跳过 prompt/RAG/eval) | T06 outsider-tell;T03 |
| A6 | 把所有错误答案都叫「hallucination」(不拆 failure mode) | T06 |
| A7 | 「context window 越大越好,塞满它」(触发 lost in the middle) | T06 |
| A8 | 把 RAG 等同于 vector DB / 把 RAG 失败归咎数据库选错 | T02 避坑;T06 |
| A9 | 把所有 AI 需求都当 agent 做(更别当 multi-agent) | T02 避坑;T04 |
| A10 | 2026 还把 LangChain 经典抽象当默认建 app 的方式 | T02 避坑 |
| A11 | premature tool outsourcing(用 eval 平台替代 error analysis) | T02 避坑;T03 |
| A12 | 不算单用户 token 经济模型就进 POC / ship | T03;T06;intake |
| A13 | 「从能力出发」而非「从问题出发」(被新模型能力诱惑) | T03 workflow 1;T06-S021 |
| A14 | 把 AI 当装饰性能力 / feature theater | T01 Aakash |
| A15 | prompt engineering 速成班「7 天成为 AI PM」 / AI PM = 会写 prompt | T06;intake |
| A16 | 把单一 LLM provider hardcode 进产品 | T02 避坑 |
| A17 | POC 代码「悄悄转正」当 MVP 地基 | T03 workflow 2 |
| A18 | 信「AI 自动生成 rubric 又自动打分」的全自动 eval | T02 避坑 |
| A19 | golden set 当训练数据 / 越大越好 | T06;T03 |
| A20 | 用通用 eval dashboard(helpfulness_score / toxicity_score 10+ 通用指标) | T03 资深 skip |

## 候选时效信号 (诚实边界用)

| # | Signal | 来源 | Decay 强度 |
|---|--------|------|-----------|
| D1 | 工具栈层:agent 框架层衰减最快(新兴 7 个全 high decay) | T02 | 极高(3-6 月) |
| D2 | 工作流:6 个 workflow 无一稳态,最低 low 也是「方法稳工具变」 | T03 | 高(3-6 月) |
| D3 | 术语层:prompt engineering / RAG / agent 三高频词「正确用法」12 月尺度漂移 | T06 | 高 |
| D4 | EU AI Act 高风险条款 2026-08 落地 + 配套标准持续出 | T06 | 高(政策驱动) |
| D5 | MCP 自 2024-11 后快速演进、未定型 | T02,T06 | 高(新兴标准) |
| D6 | 工具厂商独立性变化:Promptfoo→OpenAI、Statsig→Amplitude、Scale AI←Meta | T02 | 高 |
| D7 | 模型版本号高频跳动(2026-05 已 GPT-5.5 / Claude Opus 4.7 / Gemini 3.1 Pro);具体「哪个模型最强」decay 极高 | T02,T01 | 极高 |
| D8 | 心智模型 / 智识谱系 / canon 衰减慢(1-2 年) | extraction-framework | 低 |

## 候选信源 / 结构性失衡 (诚实边界用)

| # | Gap | 来源 |
|---|-----|------|
| G1 | 国内(zh-CN)figures = 0;朋克熊 / 唐辰只在黑名单源(知乎/CSDN/公众号)被 DROP — 结构性 gap | T01,T04 |
| G2 | 8 figure 中仅 Marily / Aakash 2 人 title 对口「AI 产品经理」,「AI PM 视角」在 figure 池稀薄 | T01 |
| G3 | 一手率实测 52.2%(159 条 / 83 first-hand),刚过 50% 线 | 全 track 汇总 |
| G4 | 本行 pre-canonical(<3 年),无三方共识 AI-PM textbook;canon 重心落在工程向 blog + paper | T04 |
| G5 | 五阶段「想法→POC→MVP→生产→飞轮」完整 SOP 不存在,6 workflow 串联有推断成分 | T03 |
| G6 | PM↔工程师边界证据强,PM↔数据/标注 中等,PM↔法务/安全/红队 薄弱 | T03 |
| G7 | eval 派幸存者偏差:发声全是 eval 派 + eval 工具厂商,「模型派」少写 workflow 长文 | T03 |
| G8 | 缺权威 AI-PM-specific 工具采用率 survey,必备层采用率是多源推断 | T02 |
| G9 | 国内工具(DeepSeek/Qwen/GLM)只一张合并卡片,vendor docs 未深挖 | T02 |
| G10 | voice_samples 多来自搜索摘要 + 节目描述(标「转述」),未逐集抓 podcast 字幕 | T01 |

## 候选 Agentic Protocol 维度

| # | 维度 | 推导自哪个 mental model |
|---|------|----------------------|
| AP1 | 模型能力近 3-6 月迭代轨迹 + 该层会不会被模型 native 化 | C8 工具临时性 + C9 保鲜期 |
| AP2 | eval / error analysis 现状诊断(有没有 golden set、judge 校准没) | C1 eval 是地基 + C2 error analysis |
| AP3 | workflow vs agent 边界判定(这需求真需要 agent 吗) | C3 workflow vs agent + C5 先简单 |
| AP4 | 单用户 token 经济模型 + cost-quality-latency 硬约束定位 | C7 三角 + 经济模型 |
| AP5 | 学派语境定位(用户 / 公司在模型派 / 工作流派 / agent 派 / 飞轮派哪一派) | C10 数据飞轮 disputed + S4 四流派 |
| AP6 | AI PM 角色类型 + 协作边界诊断(在这家公司 AI PM 是 4 种里哪种) | C4 角色定义 + C16 角色不统一 |
| AP7 | 失败模式 / 可靠性现实校准(pass^k、demo-to-production gap、defensive UX) | C6 AI 不可靠是常态 + C11 对抗假象 |

> 候选数统计:心智模型 18 + playbook 16 + 流派分裂 7 + 反模式 20 + 时效 8 + 失衡 10 + Agentic 维度 7。
> 心智模型候选 18 ≥ 15(技术 / 标准类门槛),playbook 候选 16 ≥ 10 —— **不触发冷僻协议,不需补 research**。下一步走三重验证收敛到 3-7 心智模型 + 5-10 playbook。
