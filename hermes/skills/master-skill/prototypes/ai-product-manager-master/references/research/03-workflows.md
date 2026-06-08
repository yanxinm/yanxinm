# Track 03 — Workflows（SOP / 方法论 / pipeline）：AI Product Manager

> Phase 1 Wave 3 输出。行业：AI Product Manager（LLM 应用 / 生成式 AI / Agent 产品的产品经理实战）。locale=global。
> 调研日期：2026-05-14。时间盒 ~12 min。
> **强时效声明**：工作流是 master skill 衰减最快的部分（extraction-framework § 八）。本行 intake 明示技能保鲜期 6-12 个月。每个 workflow 卡强制带 `Last_updated` + 近期变化 + decay risk。本 track 多数 workflow 标 **medium-high decay** —— AI PM 这一行的 SOP 本身还在快速成型（角色 <3 年）。
> **Wave seed 说明**：Wave 1（canon / glossary / sources）贡献了充足 seed —— 尤其 04-canon 的「Anthropic 五种 workflow 模式」「Hamel field-guide error-analysis 循环」「eval-driven iteration」，06-glossary 末尾「工作流变化触发种子」直接给了 4 条 workflow 变化锚点，05-sources 的签名内容标题反复指向「coding agents 产品化 / 如何成为 AI PM / AI evals」。Wave 2（figures / tools）文件本次未生成（不在工作目录），按「seed 偏少加权 web search 兜底」处理，已用 WebSearch/WebFetch 补齐一手工程师长文。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://hamel.dev/blog/posts/field-guide/ | verified_primary | 2026-05-14 | Hamel Husain | 「A Field Guide to Rapidly Improving AI Products」(2025-03-24) — error-analysis 迭代循环标杆长文，多公司案例 |
| T03-S002 | https://www.anthropic.com/research/building-effective-agents | verified_primary | 2026-05-14 | Anthropic (Schluntz, Zhang) | 「Building Effective Agents」(2024-12) — workflow vs agent + 五模式 + 「先简单后复杂」build SOP |
| T03-S003 | https://eugeneyan.com/writing/eval-process/ | verified_primary | 2026-05-14 | Eugene Yan | 「An LLM-as-Judge Won't Save The Product—Fixing Your Process Will」— eval 流程 = 数据飞轮 |
| T03-S004 | https://eugeneyan.com/writing/llm-patterns/ | verified_primary | 2026-05-14 | Eugene Yan | 「Patterns for Building LLM-based Systems & Products」— eval / RAG / guardrails / defensive UX / collect-feedback 七模式 |
| T03-S005 | https://eugeneyan.com/writing/conf-lessons/ | verified_primary | 2026-05-14 | Eugene Yan | 「39 Lessons on Building ML Systems」— production / scaling / 执行经验 |
| T03-S006 | https://www.news.aakashg.com/p/ai-evals | secondary | 2026-05-14 | Aakash Gupta (Product Growth) | 「AI Evals for PMs」(updated 2026-04-21) — analyze/measure/improve 三步循环 + PM 常犯错 |
| T03-S007 | https://www.lennysnewsletter.com/p/evals-error-analysis-and-better-prompts | secondary | 2026-05-14 | Lenny / Hamel Husain | Hamel 在 Lenny 访谈 — trace → 归类 → binary eval → LLM-judge 校准 |
| T03-S008 | https://amankhan1.substack.com/p/how-ai-pms-and-ai-engineers-collaborate | verified_primary | 2026-05-14 | Aman Khan (Arize) | 「How AI PMs and AI Engineers Collaborate on Evals」— PM/工程师分工边界一手描述 |
| T03-S009 | https://humanloop.com/blog/ai-is-blurring-the-lines-between-pms-and-engineers | verified_primary | 2026-05-14 | Humanloop | 「AI Is Blurring the Line Between PMs and Engineers」— PM 直接写 prompt、边界模糊化 |
| T03-S010 | https://www.svpg.com/build-to-learn-vs-build-to-earn/ | secondary | 2026-05-14 | Marty Cagan (SVPG) | 「Build to Learn vs Build to Earn」— POC/原型「为学习而造」vs「为交付而造」的产品判断 |
| T03-S011 | https://www.proofofconcept.pub/p/how-product-discovery-changes-with | secondary | 2026-05-14 | David Hoang | 「How Product Discovery changes with AI」— 原型从「阶段」变「即时循环」，可行性问题转向「该不该存在」 |
| T03-S012 | https://www.braintrust.dev/articles/eval-driven-development | secondary | 2026-05-14 | Braintrust | 「Eval-Driven Development」— EDD 三阶段循环、golden set 作回归基线（vendor，需交叉验证） |
| T03-S013 | https://vercel.com/blog/eval-driven-development-build-better-ai-faster | verified_primary | 2026-05-14 | Vercel | 「Eval-driven development」— EDD = 质量是循环不是门、offline/online 配合 |
| T03-S014 | https://openai.com/index/evals-drive-next-chapter-of-ai/ | verified_primary | 2026-05-14 | OpenAI | 「How evals drive the next chapter in AI for businesses」— eval 作 ship 门（vendor 一手，需交叉验证） |
| T03-S015 | https://developers.openai.com/cookbook/examples/partners/eval_driven_system_design/receipt_inspection | verified_primary | 2026-05-14 | OpenAI | Cookbook「Eval Driven System Design - From Prototype to Production」— POC→生产的 eval 驱动 pipeline |
| T03-S016 | https://hamel.dev/blog/posts/evals-faq/ | verified_primary | 2026-05-14 | Hamel Husain | 「LLM Evals FAQ」— golden set 大小、binary vs Likert、judge 校准 75-90% 等操作细节 |
| T03-S017 | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/choose-ai-model | secondary | 2026-05-14 | Microsoft Learn | 「Choose the Right AI Model for Your Workload」— 模型选型决策维度（vendor 中立框架） |
| T03-S018 | https://www.oreilly.com/radar/a-field-guide-to-rapidly-improving-ai-products/ | secondary | 2026-05-14 | O'Reilly Radar | field-guide 的 O'Reilly 转载（第三方背书） |

> 黑名单合规：搜索命中的知乎专栏 / 微信公众号 / CSDN / Quora / G2 / Capterra / Medium 个人转述文 全部丢弃，未进 manifest。`artificialanalysis.ai` 模型对比页虽 verifier 给 secondary、信息有用，但属「持续刷新的榜单」不是 workflow 一手描述，未单独入表（其方法学已被 T03-S017 覆盖）。

---

## ⚠️ 调研边界与失败记录（诚实标注）

1. **Wave 2（figures / tools）文件缺失**：工作目录下只有 04/05/06 三个 Wave 1 文件，01-figures / 02-tools 未生成。按 SKILL「seed 偏少加权 web search 兜底」执行，已用 6 个一手工程师长文（Hamel ×3 / Eugene Yan ×3 / Anthropic / Vercel / OpenAI ×2 / Aman Khan / Humanloop）补齐。**与 Track 01/02 的交叉引用字段是基于 04-canon 已识别的 figures/tools 推断填的**，Phase 1.5 需与 Track 01/02 实际产出对齐。
2. **「想法 → POC → MVP → 生产 → 数据飞轮」五阶段的完整公开 SOP 不存在**：本行 <3 年，没有一篇一手长文从头到尾走完五阶段。本 track 的做法是**按阶段拆成 6 个独立 workflow**（scoping / POC / eval 体系搭建 / 迭代循环 / agent 产品化 / 数据飞轮），每个 workflow 用对应的一手长文做骨架。五阶段的「拼接」本身有推断成分。
3. **PM vs ML 工程师边界证据偏「eval 协作」单一场景**：最清晰的一手边界描述（T03-S008 / S009 / Hamel 在 Lenny 访谈 T03-S007）几乎都聚焦「谁写 prompt / 谁建 scorer」。其它边界（数据标注外包决策、法务介入时机、安全红队归属）证据较薄，已尽量标注。
4. **eval-driven 这一派证据强、但有「幸存者偏差」**：发声的全是 eval 派（Hamel / Eugene Yan / Shreya Shankar）+ eval 工具厂商（Braintrust / Arize / Humanloop）。「模型派」（等 frontier 模型自己变好、不重 eval）很少写 workflow 长文 —— 不代表他们不存在。矛盾已在卡片内保留。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 2 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 5. Agent 产品从 0 到可 ship | 出现真需要「LLM 自主决策多步」的需求 | 一个通过 pass^k 可靠性门、有失败回退 + 用户控制权设计的 agent 产品 | 2026-05-14 | skip 框架抽象 / optimize 工具文档 / add pass^k 门 + 沙箱测试 |
| 6. 搭数据飞轮 | MVP 上线、有真实流量，要把「用得多」变成「越用越好」的差异化 | 一个 production trace → 标注 → eval/finetune 数据 → 模型升级 的闭环 | 2026-05-14 | skip 早期不做 / optimize 自动采样路由 / add 飞轮 ROI 诚实评估 |

### Medium decay — 3 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. Scoping 一个 AI feature（想法阶段） | 业务方 / 用户洞察提出一个「能不能用 AI 做」的想法 | 一份明确「该不该做 + 技术上 prompt/RAG/finetune 哪条路 + 成功标准」的 scoping 文档 | 2026-05-14 | skip 过度市场调研 / optimize 用原型替代规格 / add 不确定性 + 成本约束判断 |
| 3. 从 0 搭起 eval 体系（POC→MVP 之间的前置门） | POC 跑通、要进入「认真迭代」阶段，但没有衡量「改动有没有用」的手段 | 一套 golden set + code-based check + 校准过的 LLM-judge + offline/online 双层 eval | 2026-05-14 | skip 通用 dashboard / optimize 自建 data viewer / add online eval + judge 校准 |
| 4. Eval-driven 迭代循环（MVP→生产的主循环） | eval 体系已建，产品质量需要持续往上推 | 每轮：一批被修复的 top failure mode + 更新的 prompt/context + 回归通过的 eval | 2026-05-14 | skip 加功能冲动 / optimize binary + 频率排序 / add error analysis 作前置 |

### Low decay — 1 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. POC / 原型验证（想法→POC） | scoping 通过，要快速验证「技术上 + 体验上 到底行不行」 | 一个「为学习而造」的可抛弃原型 + 一个明确的 go / pivot / kill 结论 | 2026-05-14 | skip 工程级代码质量 / optimize AI 原型工具并行造多版 / add 「该不该存在」desirability 判断 |

> 说明：6 个 workflow 全部偏 medium/high decay，**没有真正稳态的**。Workflow 2（POC 验证）标 low 是因为「为学习造可抛弃原型」这个产品判断本身是 Cagan 级别的稳定方法论（T03-S010），AI 只是把它的循环加快了——方法稳，工具变。这本身是 Phase 2.8 的强信号：本 skill 工作流模块 6 个月内大概率需要全面 update。

---

## 详细 Workflow 卡片

### 1. Scoping 一个 AI feature（「想法」阶段）

- **One-liner**: 把一个「能不能用 AI 做 X」的模糊想法，变成一份「该不该做 + 走哪条技术路 + 用什么标准判断成功」的可执行 scoping 文档 —— 从「业务诉求」状态到「团队可以开干」状态。
- **Trigger**: 业务方 / 用户研究 / 高管提出一个 AI 想法（"我们能不能加个 AI 助手 / 让它自动总结 / 加个 copilot"）。**业务触发**为主。 (evidence: [T03-S006, T03-S011])
- **Output**: 一份 scoping 文档，含：(a) 该不该做的判断（desirability + viability）(b) 技术路线初判（prompt-only / RAG / agent / 需要 finetune）(c) 成功标准（不是「准确率高」，是「在哪些 failure mode 上达到什么 pass 率」）(d) 成本约束（单用户 token 经济模型的粗算）(e) 风险分级（是否落入 EU AI Act 高风险）。 (evidence: [T03-S006, T03-S017])
- **入门 SOP（minimum viable steps）**:
  1. **澄清「真问题」**：把「加个 AI X」翻译成「用户的什么 pain point」。PM 主导。跳过 → 做出一个技术上能跑但没人要的功能（intake warning「prompt engineering 不是核心，产品 fit 判断才是」）。
  2. **判断该不该用 AI**：问「这个问题确定性规则能不能解 / 传统 ML 能不能解 / 真的需要生成式吗」。PM 主导。跳过 → 用 LLM 做了一件正则就能做的事，背上不必要的成本和不可靠性。
  3. **技术路线初判**：和工程师一起过一遍 prompt-only → RAG → agent → finetune 的阶梯，**默认从最便宜的假设起**（Anthropic「先简单后复杂」）。PM + ML 工程师共同。跳过 → 一上来设计 agent / 上 vector DB，过度工程（06-glossary「一遇到不准就喊 fine-tune」反模式）。 (evidence: [T03-S002])
  4. **定义成功标准**：把「好」拆成具体、二元可判的 failure mode + 目标 pass 率，而不是「准确率」。PM 主导（PM 是首席领域专家）。跳过 → 进入迭代后没有靶子，全凭 vibes。 (evidence: [T03-S006, T03-S008])
  5. **粗算成本约束**：token 单价 × 预期用户行为 × 留存 → 单用户成本能不能撑住定价。PM 主导。跳过 → MVP 做出来才发现单位经济模型为负，ship 不了（intake warning「成本控制是被忽视的硬技能」）。
  6. **风险分级**：判断是否落入监管高风险类别（EU AI Act / 中国生成式 AI 办法），决定要不要法务早期介入。PM 主导，法务确认。跳过 → 高风险产品做到一半被合规打回。 (evidence: [T03-S006] + 06-glossary 工作流变化种子)
- **资深路径（差异点）**:
  - **skip**：资深 AI PM 会**跳过冗长的市场调研 / 竞品功能清单**——他们知道在 AI 这一行「能不能建」已经不是瓶颈，desirability 才是，过度调研是拖延。 (evidence: [T03-S011])
  - **optimize**：资深人把「写 scoping 规格」**优化成「先做一个原型再写规格」**——原型比文档更快暴露真问题（与 Workflow 2 衔接）。 (evidence: [T03-S011])
  - **add**：资深人**额外做两件初学者忽略的事**：(1) 不确定性管理——明确写下「这个功能有哪些地方我们现在根本不知道行不行」，把它变成 POC 要回答的问题，而不是假装规格能写全；(2) 成本约束前置——在 scoping 阶段就把单用户经济模型摆上桌，而不是等 MVP。 (evidence: [T03-S006, T03-S015])
- **近期变化**（近 12 个月）：
  - **2025 年起，由 AI 原型工具（Gemini + Claude Code 类）成熟驱动**，原 step「写详细 PRD 再交工程师」越来越多被「PM 自己先撸个原型」替代——scoping 和 POC 的界线在模糊。 (evidence: [T03-S011])
  - **2026-08 起，由 EU AI Act 高风险条款落地驱动**，scoping 阶段新增「风险分级判定」为标准步骤（06-glossary 明确点出此触发）。
  - 触发事件类型：新工具 + 法规变化。
  - **稳态判断**：scoping 的「该不该做」内核（Cagan 式产品发现）稳定；但 AI 特有的「技术路线初判 + 成本约束 + 风险分级」三块是新增且在动。
- **典型耗时**: 入门 SOP 1-2 周；资深路径 2-4 天（用原型压缩）。
- **关键工具（与 Track 02 关联）**: AI 原型工具（Claude Code / v0 / Gemini，新兴-必备）；模型对比工具（artificialanalysis.ai 类，场景特化）；token 成本计算器（必备）。*注：Track 02 文件本次缺失，工具评级待对齐。*
- **关键人物（与 Track 01 关联）**: Marty Cagan 在《INSPIRED》+「Build to Learn vs Build to Earn」中谈产品发现底盘；David Hoang 在「How Product Discovery changes with AI」中详细谈 AI 时代 scoping 变化。*待与 Track 01 对齐。*
- **常见失败模式**:
  - **「从能力出发」而非「从问题出发」**：触发原因 = 被新模型能力诱惑（"GPT-5.5 能做这个，我们也加"）；怎么避免 = 强制 step 1 先写用户 pain point，能力是手段不是起点。（**CLI 自检项**：Did you start from a user pain point, or from a model capability you wanted to use? If the latter — stop and rewrite the problem statement.） (evidence: [T03-S006])
  - **规格写得像传统 PRD（确定性、可穷举）**：触发原因 = 用传统 PM 习惯套 AI；怎么避免 = 接受规格只能写到「已知的失败模式 + 待 POC 回答的未知」，剩下靠迭代涌现。（**CLI 自检项**：Does your spec pretend every edge case is knowable up front? AI specs emerge from output inspection — list what you DON'T know yet.） (evidence: [T03-S006])
  - **不算单用户经济模型就进 POC**：触发原因 = 课程不教、PM 觉得是工程的事；怎么避免 = scoping 文档强制一行「单用户/月预估 API 成本 vs 定价」。（**CLI 自检项**：Have you done a back-of-envelope token-cost-per-user-per-month estimate? If not, you may be scoping a product that can't ship.）
- **来源** (≥ 3):
  - [Primary] Anthropic「Building Effective Agents」技术路线「先简单后复杂」: https://www.anthropic.com/research/building-effective-agents（collected: 2026-05-14）
  - [Secondary] Aakash Gupta「AI Evals for PMs」PM 定义成功标准 = analyze 步: https://www.news.aakashg.com/p/ai-evals（updated 2026-04-21）
  - [Secondary] David Hoang「How Product Discovery changes with AI」: https://www.proofofconcept.pub/p/how-product-discovery-changes-with
  - [Reference] Marty Cagan「Build to Learn vs Build to Earn」: https://www.svpg.com/build-to-learn-vs-build-to-earn/
- **Last_updated**: 2026-05-14（基于 T03-S006 的 2026-04-21 更新 + T03-S011）
- **Decay risk**: **medium**——产品发现内核稳定，但 AI 特有的技术路线初判 / 成本 / 风险分级三块 12-18 个月会显著演进。

---

### 2. POC / 原型验证（「想法 → POC」）

- **One-liner**: 用一个「为学习而造、随时可抛弃」的原型，在投入真正工程资源前回答「技术上行不行 + 体验上用户要不要」—— 从「scoping 假设」状态到「go / pivot / kill 有依据」状态。
- **Trigger**: scoping 通过，存在「不实际做一个就不知道行不行」的关键不确定性。**技术 + 业务双触发**。 (evidence: [T03-S010, T03-S011])
- **Output**: 一个可抛弃原型 + 一个明确结论（go 进 MVP / pivot 换方向 / kill 砍掉）+ 一份「学到了什么」记录。 (evidence: [T03-S010])
- **入门 SOP（minimum viable steps）**:
  1. **明确这个 POC 要回答的问题**：是「技术可行性」还是「用户 desirability」还是「成本」？一个 POC 别想回答全部。PM 主导。跳过 → 造了个什么都证明不了的 demo。 (evidence: [T03-S010])
  2. **造「为学习」的原型，不是「为交付」**：明确这是 throwaway code，工程师不用写测试、不用考虑扩展性。PM + 工程师达成共识。跳过 → 把原型代码当 MVP 地基，背上技术债且不敢推翻。 (evidence: [T03-S010])
  3. **用真实约束喂原型**：合成数据要 ground 在真实业务规则 / 真实数据样本上，不能凭空编。PM + 领域专家。跳过 → demo 在假数据上很美，碰真数据就崩（06-glossary「demo-to-production gap」）。 (evidence: [T03-S001])
  4. **拿原型做真实用户/领域专家测试**：观察真人用，尤其看 desirability。PM 主导。跳过 → 技术跑通了，但没人要——AI 唯一不能自动解决的就是 desirability。 (evidence: [T03-S011])
  5. **下 go / pivot / kill 结论并记录学到什么**：PM 主导。跳过 → POC 变成「一直在 POC」，沉没成本拖着不决策。
- **资深路径（差异点）**:
  - **skip**：资深人**坚决跳过原型阶段的工程级代码质量**——不写测试、不做 code review、不上 CI。他们清楚 POC 代码的命运就是被删。初学者常因「都写了不如留着」而把原型偷偷转正。 (evidence: [T03-S010])
  - **optimize**：资深人用 AI 原型工具**把「串行迭代」优化成「并行造 3-5 个不同方向」**同时测——AI 让 10-20 个原型/周成为常态，不再依赖设计师 / 工程师排期。 (evidence: [T03-S011])
  - **add**：资深人**额外死磕 desirability 判断**——「能建」已经不稀缺，他们把 POC 的重心从「Can we build this?」转到「Should this exist?」，且知道这个问题只能靠看真人挣扎来答，合成 persona 替代不了。 (evidence: [T03-S011])
- **近期变化**（近 12 个月）：
  - **2025 年起，由 gen-AI 原型工具普及驱动**，原「POC 是一个独立阶段，要等工程排期」变成「原型是一个近乎即时的循环，PM 自己就能做」——POC 从「阶段」退化成「动作」。当前采用率：David Hoang / Cagan 系都在讲这个转变，海外资深 PM 圈已广泛采纳。 (evidence: [T03-S011])
  - 触发事件类型：新工具。
  - **稳态判断**：「为学习而造 vs 为交付而造」的产品判断是 Cagan 级稳定方法论，**近 12 个月无内核变化**；变的是工具让循环快了 10x。故此 workflow 标 low decay。
- **典型耗时**: 入门 SOP 1-2 周；资深路径 1 个下午到几天（AI 工具 + 并行）。
- **关键工具（与 Track 02 关联）**: Claude Code / v0 / Gemini（AI 原型，新兴-必备）；Figma（设计 surface，必备）；合成数据生成（场景特化）。
- **关键人物（与 Track 01 关联）**: Marty Cagan「Build to Learn vs Build to Earn」是这个 workflow 的方法论原点；David Hoang 谈 AI 时代的具体变化。*待与 Track 01 对齐。*
- **常见失败模式**:
  - **原型「悄悄转正」**：触发原因 = throwaway code 写得还行，舍不得删；怎么避免 = step 2 一开始就和工程师白纸黑字约定这是 throwaway。（**CLI 自检项**：Is your team treating the POC code as the MVP foundation? If yes — you skipped "build to learn"; the code should be deleted, not extended.） (evidence: [T03-S010])
  - **在假数据上做出漂亮 demo**：触发原因 = 真数据难拿，编一个快；怎么避免 = 合成数据强制 ground 在真实 listing / schedule / 业务规则上。（**CLI 自检项**：Is your demo running on invented data? Re-run it on real (or real-constrained synthetic) data before drawing any conclusion.） (evidence: [T03-S001])
  - **只验技术、不验 desirability**：触发原因 = 技术可行性好量化、用户要不要难量化；怎么避免 = step 4 强制至少看 3-5 个真人用原型。（**CLI 自检项**：Did a real user actually try this prototype, or only your team? "Can we build it" ≠ "should it exist".） (evidence: [T03-S011])
- **来源** (≥ 3):
  - [Primary] Marty Cagan「Build to Learn vs Build to Earn」: https://www.svpg.com/build-to-learn-vs-build-to-earn/
  - [Secondary] David Hoang「How Product Discovery changes with AI」: https://www.proofofconcept.pub/p/how-product-discovery-changes-with
  - [Primary] Hamel Husain field-guide（合成数据 ground 在真实约束）: https://hamel.dev/blog/posts/field-guide/（collected: 2026-05-14）
- **Last_updated**: 2026-05-14
- **Decay risk**: **low**——方法论内核（Cagan）极稳，变的是工具速度。这是本 track 唯一接近稳态的 workflow。

---

### 3. 从 0 搭起 eval 体系（POC → MVP 之间的前置门）

- **One-liner**: 在「认真迭代」开始之前，搭一套能客观回答「这次改动到底有没有让产品变好」的评估基础设施 —— 从「POC 跑通、全凭 vibes」状态到「每次改动都有可回归的度量」状态。这是 AI PM 区别于传统 PM **最硬核**的一段工作。
- **Trigger**: POC 通过、决定进 MVP，但团队没有任何衡量质量的客观手段，改 prompt 全靠「看几个 case 觉得行」（06-glossary「LGTM / vibes check」反模式）。**技术触发**。 (evidence: [T03-S001, T03-S006])
- **Output**: (a) 一个 golden set（30-50 个 PM + 领域专家共同确认的「最该答对」用例，带期望输出 + 专家 critique）(b) 一层 code-based check（regex / 结构校验 / 执行测试，最便宜）(c) 一个和人工标注校准过（75-90% 一致）的 LLM-as-judge (d) offline + online 双层 eval 接好。 (evidence: [T03-S001, T03-S006, T03-S016])
- **入门 SOP（minimum viable steps）**:
  1. **PM 亲自看 trace 做 error analysis**：阻塞 30 分钟，拉 10-20 个真实交互，逐条记「哪里对了、哪里错了」的开放式笔记。**PM 主导**（PM 是首席领域专家，这一步不能外包给工程师）。跳过 → 后面所有 eval 指标都是凭空想的、测不到真问题。 (evidence: [T03-S001, T03-S006, T03-S008])
  2. **自下而上归类成 failure mode**：让笔记里的 pattern 自然涌现，用 LLM 把笔记聚成 taxonomy，数每类频率。PM 主导。跳过 → 直接上「helpfulness / hallucination 通用 dashboard」，测的是噪声不是你的产品。 (evidence: [T03-S001, T03-S006])
  3. **建 golden set**：针对 top failure mode，PM + 领域专家共同确认 30-50 个「系统最该正确处理」的用例。合成数据按 features × scenarios × personas 三维度造，ground 在真实约束上。PM + 领域专家。跳过 → 没有回归基线，改 A 修好了不知道有没有弄坏 B。 (evidence: [T03-S001, T03-S016])
  4. **先建最便宜的 code-based check**：能用 regex / 结构校验 / 执行测试确定性判断的，绝不先上 LLM-judge。PM 提需求，工程师实现。跳过 → 一上来烧钱建 LLM-judge 评一个正则就能评的东西。 (evidence: [T03-S006])
  5. **建 LLM-as-judge 并和人工校准**：用 rubric 把 judge 和人工标注对齐到 75-90% 一致再 scale；用 binary pass/fail 不用 1-5 分。PM 定 rubric + 标注，工程师建 scorer。跳过 → 一个没校准的 judge 给的分等于没用，团队很快不信它。 (evidence: [T03-S007, T03-S016, T03-S008])
  6. **接上 offline + online 两层**：offline 作迭代默认引擎，online 对真实流量做 reality check（shadow / canary）。PM 定 online 指标，工程师接 production 数据管线。跳过 → 只有 offline 会过拟合 golden set；只有 online 改动反馈太慢。 (evidence: [T03-S012, T03-S013])
- **资深路径（差异点）**:
  - **skip**：资深人**坚决跳过「通用 eval dashboard」**——不建 helpfulness_score / toxicity_score 那种 10+ 通用指标的看板。他们知道那制造「在进步」的假象、分散注意力，真正的指标必须从 error analysis 自下而上长出来。 (evidence: [T03-S001, T03-S006])
  - **optimize**：资深人**把「用通用标注工具」优化成「花几小时自建一个 domain-specific data viewer」**——一键标注、全上下文一屏、热键导航。Hamel 原文：有 thoughtful viewer 的团队「迭代快 10x」。 (evidence: [T03-S001])
  - **add**：资深人**额外做两件事**：(1) judge 校准——初学者跳过「和人工对齐」直接用 LLM 打分，资深人坚持先校准到 90% 再 scale；(2) online eval 层——初学者只做 offline，资深人知道要配 online shadow/canary 做 reality check。 (evidence: [T03-S007, T03-S013, T03-S016])
- **近期变化**（近 12 个月）：
  - **2025 年起，由「eval-driven development」成为公认范式驱动**（对标 TDD），整个 AI 产品流程从「想法→POC→MVP→上线」插入「先建 eval 体系」为前置门，error analysis 成 AI PM 标准动作（06-glossary 工作流变化种子明确点出）。 (evidence: [T03-S003, T03-S012, T03-S013, T03-S014])
  - **2025 年内变化**：golden set 从「静态精选集」演进为「动态从 production 日志拉真实失败，每天加进 eval 套件」——offline eval 本身在和数据飞轮融合。 (evidence: [T03-S012, T03-S014])
  - 触发事件类型：标准更新（范式形成）+ 行业事件。
  - **稳态判断**：error analysis → golden set → judge 校准这套方法 2024-2026 较稳（Hamel 2024 的文 2026 仍是标杆）；但「eval 工具层」（LangSmith / Braintrust / Arize / Promptfoo）在 fragmenting，每家收编「eval」成自家产品——**方法稳、工具乱**。
- **典型耗时**: 入门 SOP 1-3 周；资深路径 1-2 周（自建 viewer 前期投入换后期 10x 速度）。
- **关键工具（与 Track 02 关联）**: LangSmith / Braintrust / Arize Phoenix / Promptfoo（eval 平台，必备但 fragmenting）；自建 data viewer（资深标配）；DeepEval（LLM-judge，G-Eval 范式实现）。Hamel「Selecting The Right AI Evals Tool」是选型 evidence 源。
- **关键人物（与 Track 01 关联）**: Hamel Husain（field-guide + evals-faq，这个 workflow 的圣经作者）；Eugene Yan（eval-process：eval 流程即数据飞轮）；Shreya Shankar（与 Hamel 合开 Maven evals 课，criteria drift 论文）。*待与 Track 01 对齐。*
- **常见失败模式**:
  - **跳过 error analysis 直接上指标 dashboard**：触发原因 = dashboard 看着专业、error analysis 像「手工活」；怎么避免 = 强制 PM 先花 30 分钟看 10-20 条 trace 再说。（**CLI 自检项**：Did you build a metrics dashboard before reading 20 real traces by hand? If yes — the dashboard is measuring noise, not your product.） (evidence: [T03-S001, T03-S006])
  - **LLM-judge 没校准就 scale**：触发原因 = 「让 GPT 打分」看着就能用；怎么避免 = 上线前必须验 judge 和人工标注 75-90% 一致。（**CLI 自检项**：Has your LLM-judge been calibrated against human labels to 75-90% agreement? An uncalibrated judge is worse than no judge — the team will stop trusting it.） (evidence: [T03-S007, T03-S016])
  - **过早把 eval 工具外包 / 过早全自动化**：触发原因 = vendor 营销「我们的 pre-built judge 开箱即用」；怎么避免 = 校准必须针对你自己的数据，早期保持高人工参与度。（**CLI 自检项**：Are you relying on a vendor's pre-built judge without validating it on your own data? Calibration is domain-specific — it can't be outsourced.） (evidence: [T03-S001, T03-S007])
  - **golden set 太大 / 当成训练数据**：触发原因 = 外行「数据越多越好」直觉；怎么避免 = golden set 小而精（30-50 个），是评估用不是训练用。（**CLI 自检项**：Is your golden set hundreds of examples or being used to train? Keep it 30-50, expert-curated, eval-only.） (evidence: [T03-S016])
- **来源** (≥ 3):
  - [Primary] Hamel Husain「A Field Guide to Rapidly Improving AI Products」: https://hamel.dev/blog/posts/field-guide/（collected: 2026-05-14）
  - [Primary] Hamel Husain「LLM Evals FAQ」（golden set 大小 / binary / judge 校准细节）: https://hamel.dev/blog/posts/evals-faq/（collected: 2026-05-14）
  - [Primary] Eugene Yan「An LLM-as-Judge Won't Save The Product—Fixing Your Process Will」: https://eugeneyan.com/writing/eval-process/（collected: 2026-05-14）
  - [Secondary] Aakash Gupta「AI Evals for PMs」: https://www.news.aakashg.com/p/ai-evals
  - [Primary] Vercel「Eval-driven development」: https://vercel.com/blog/eval-driven-development-build-better-ai-faster
- **Last_updated**: 2026-05-14
- **Decay risk**: **medium**——方法论内核 2024-2026 稳定，但工具层 fragmenting + golden set 与飞轮融合的趋势在动。

---

### 4. Eval-driven 迭代循环（MVP → 生产的主循环）

- **One-liner**: eval 体系建好后，每一轮迭代用「error analysis → 假设 → 改 → 重新 eval」的闭环把产品质量系统性往上推 —— 从「质量上不去、不知道动哪」状态到「每轮都有可度量提升」状态。这是 AI 产品 ship 之后的日常主循环。
- **Trigger**: eval 体系已建（Workflow 3 完成），产品质量需要持续改进；或 online eval 发现新的 production 失败。**技术触发**为主。 (evidence: [T03-S001, T03-S006])
- **Output**: 每轮产出：(a) 一批被定位并修复的 top failure mode (b) 更新的 prompt / context / 检索 / 偶尔模型切换 (c) 回归通过的 eval 套件 (d) 新增进 golden set 的 production 失败样本。 (evidence: [T03-S001, T03-S006, T03-S012])
- **入门 SOP（minimum viable steps）**:
  1. **Analyze（看数据找 failure mode）**：定期采样 production trace，PM 亲自读，定性识别这一轮最痛的 failure mode。PM 主导。跳过 → 凭直觉猜要改什么，大概率改错地方。 (evidence: [T03-S001, T03-S006])
  2. **频率排序定优先级**：用「这个 failure mode 出现多少次」而不是「我觉得这个重要」来排。PM 主导。跳过 → 花一周修一个一年出现两次的边角问题。 (evidence: [T03-S001, T03-S007])
  3. **对 top failure mode 做根因分析 + 提假设**：drill 进具体失败 pattern（Hamel 案例：日期处理 66% 失败），形成「改 X 应该能修好」的可验证假设。PM + 工程师 + 领域专家。跳过 → 不知道为什么错就乱改架构。 (evidence: [T03-S001])
  4. **Measure（针对性改 + 量化验证）**：按假设做最小改动——规格不清就改 prompt / context，泛化不行才动架构，**fine-tune 放最后**。在窄而具体的 binary 指标上量化前后（Hamel 案例：日期 33%→95%）。PM 主导改 prompt，工程师做架构/scorer。跳过 → 改完不知道有没有用，回到 vibes。 (evidence: [T03-S001, T03-S006])
  5. **Improve → 回归 → 循环回 Analyze**：跑全套 eval 确认没弄坏别的，把这次的 production 失败样本加进 golden set，回到 step 1。PM + 工程师。跳过 → 修 A 弄坏 B，eval 套件不增长就慢慢失效。 (evidence: [T03-S006, T03-S012])
- **资深路径（差异点）**:
  - **skip**：资深人在质量上不去时**第一反应是跳过「加功能」的冲动**——initake / Hamel 都强调，外行遇到瓶颈加功能，资深人先做 error analysis。「先 error analysis，再加功能」。 (evidence: [T03-S001])
  - **optimize**：资深人**把评估口径优化成 binary pass/fail + 频率计数**——不用模糊的 1-5 分（专家做二元判断更可靠），不靠「我觉得重要」（用频率）。 (evidence: [T03-S001, T03-S007, T03-S016])
  - **add**：资深人**额外把 error analysis 当成不可省的前置门**——初学者把迭代理解成「改 prompt 看效果」，资深人理解成「先系统看 50-100 个失败样本归类，再动手」。也额外用 Bryan Bischof 式「capability funnel」追踪进展，不只看 pass/fail。 (evidence: [T03-S001])
- **近期变化**（近 12 个月）：
  - **2025 年起，由 eval 工具成熟 + 范式普及驱动**，迭代循环从「offline 跑 golden set」扩成「offline 抓回归 + online shadow/canary 测真实流量 + online eval 镜像 offline rubric」的三件套。质量从「门」变成「循环」。 (evidence: [T03-S013])
  - **2025 年内**：top 团队开始「每天从 production 日志拉真实失败 → 自动路由模糊/高成本 case 给专家 → 加进 eval」，迭代循环和数据飞轮（Workflow 6）边界在融合。 (evidence: [T03-S012, T03-S014])
  - 触发事件类型：新工具 + 标准更新。
  - **稳态判断**：analyze→measure→improve 三步内核 2024-2026 稳定（Hamel 2024 / Aakash 2026 描述一致）；变的是 online 层的接入和飞轮融合。
- **典型耗时**: 入门 SOP 每轮 1-2 周；资深路径每轮 3-7 天（自建 viewer + 熟练 error analysis 提速）。这是一个**永不结束的循环**，不是一次性任务。
- **关键工具（与 Track 02 关联）**: eval 平台（LangSmith / Braintrust / Arize，必备）；自建 data viewer（资深标配）；trace / observability 工具（Datadog LLM Observability 类，必备）；A/B + canary（Statsig / LaunchDarkly，场景特化）。
- **关键人物（与 Track 01 关联）**: Hamel Husain（field-guide 的 analyze/measure/improve）；Aakash Gupta（把它整理成 PM 视角三步）；Eugene Yan（eval-process）；Bryan Bischof（capability funnel，被 Hamel 引用）。*待与 Track 01 对齐。*
- **常见失败模式**:
  - **瓶颈时加功能而不做 error analysis**：触发原因 = 加功能有「在推进」的感觉，error analysis 像在原地;怎么避免 = 把 error analysis 设成迭代的强制 step 1。（**CLI 自检项**：Is your response to "quality isn't improving" to add a feature? Stop — pull 50-100 failure samples and categorize first.） (evidence: [T03-S001])
  - **用 1-5 分而非 binary**：触发原因 = 觉得分数更「细腻」;怎么避免 = 改成 pass/fail，专家二元判断更可靠、更可回归。（**CLI 自检项**：Are your evals scored 1-5? Switch to binary pass/fail — Likert scores are noisy and hard to act on.） (evidence: [T03-S016])
  - **eval 套件不随 production 失败增长**：触发原因 = 建完 golden set 就不管了;怎么避免 = 每轮把新发现的 production 失败加进 golden set。（**CLI 自检项**：Has your golden set grown with newly discovered production failures? A static eval suite slowly stops catching real regressions.） (evidence: [T03-S012])
  - **判断「过早自动化」失去信任**：触发原因 = 想省人工;怎么避免 = 早期保持高人工参与，定期 recalibrate judge。（**CLI 自检项**：Did you fully automate evaluation early and now distrust the numbers? Re-introduce human review and recalibrate the judge.） (evidence: [T03-S001])
- **来源** (≥ 3):
  - [Primary] Hamel Husain「A Field Guide to Rapidly Improving AI Products」（analyze/measure/improve + capability funnel）: https://hamel.dev/blog/posts/field-guide/（collected: 2026-05-14）
  - [Secondary] Aakash Gupta「AI Evals for PMs」（三步循环 PM 视角）: https://www.news.aakashg.com/p/ai-evals
  - [Reference] Hamel Husain 在 Lenny's Newsletter 访谈（trace→归类→binary→judge）: https://www.lennysnewsletter.com/p/evals-error-analysis-and-better-prompts
  - [Primary] Eugene Yan「eval-process」: https://eugeneyan.com/writing/eval-process/
- **Last_updated**: 2026-05-14
- **Decay risk**: **medium**——三步内核稳定，online 层接入 + 飞轮融合在动。

---

### 5. Agent 产品从 0 到可 ship（high decay）

- **One-liner**: 当需求确实需要「LLM 自主决定用什么工具、多步执行」时，从「想做个 agent」到「一个通过 pass^k 可靠性门、有失败回退和用户控制权设计的 agent 产品」。
- **Trigger**: 出现一个**真的**需要 LLM 自主决策多步的需求（不是任何聊天机器人都叫 agent）。**技术 + 业务双触发**。 (evidence: [T03-S002])
- **Output**: 一个 agent 产品，含：(a) 经过沙箱大量测试的工具集 + 清晰工具文档 (b) 失败回退设计 (c) 用户控制权 / 可观测设计 (d) 通过 pass^k 多次运行稳定通过率门，而不是「demo 跑通一次」。 (evidence: [T03-S002] + 04-canon τ-bench)
- **入门 SOP（minimum viable steps）**:
  1. **先判断：真的需要 agent 吗**：过 workflow vs agent 的判断——多数需求其实是预定义路径的 workflow，agent 只在「路径无法预先定义」时才值得。PM 主导。跳过 → 把一个 routing workflow 做成 agent，无谓的不可靠 + 成本。 (evidence: [T03-S002])
  2. **能用 workflow 就用 workflow 五模式**：prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer，挑匹配的。PM + 工程师。跳过 → 重新发明 Anthropic 已经验证的模式。 (evidence: [T03-S002])
  3. **从 LLM API 直接起步，不先上框架**：很多模式几行代码就能实现；用框架也要懂底层。PM 认知 + 工程师实现。跳过 → 框架抽象遮住 prompt 和响应，debug 变难（intake「2023 LangChain 经典写法 2025 被批过度抽象」）。 (evidence: [T03-S002])
  4. **工具工程 = prompt 工程同等投入**：工具文档要写好、参数设计要「防呆」（Poka-yoke），跑大量样例输入找模型用工具时的错。PM 提需求 + 工程师实现。跳过 → agent 调工具频繁出错，根因是工具接口烂不是模型笨。 (evidence: [T03-S002])
  5. **沙箱里大量测试 + 加 guardrails**：在隔离环境跑大量 case，配 guardrails（tripwire 机制）。PM 定测试场景 + 工程师建。跳过 → 直接上生产，agent 越权 / 工具链被攻击。 (evidence: [T03-S002])
  6. **用 pass^k 而非单次 demo 作 ship 门**：上线标准是「同任务跑 k 次的稳定通过率」。PM 定门槛。跳过 → demo 美、生产崩（τ-bench：SOTA agent 零售域 pass^8 < 25%）。 (evidence: [T03-S002] + 04-canon τ-bench)
- **资深路径（差异点）**:
  - **skip**：资深人**跳过框架抽象层**，直接用 LLM API——他们知道复杂框架遮住 prompt/响应、让 debug 更难，「简单可组合 > 复杂框架」。 (evidence: [T03-S002])
  - **optimize**：资深人**把工具设计优化到和 prompt 同等投入**——写详细工具文档、用 Poka-yoke 防呆参数、跑大量样例找工具用错。初学者只调 prompt 不管工具接口。 (evidence: [T03-S002])
  - **add**：资深人**额外做两件事**：(1) pass^k 可靠性门——初学者「demo 跑通一次」就想 ship，资深人要求多次运行稳定通过率;(2) 失败回退 + 用户控制权设计——agent 一定会错，资深人在产品层设计可中断 / 可观测 / 可回退。 (evidence: [T03-S002] + 04-canon τ-bench / defensive UX)
- **近期变化**（近 12 个月）：
  - **2024-12 起，由 Anthropic「Building Effective Agents」发布驱动**，行业从 2023 年「LangChain 式重框架 ReAct」纠偏到「workflow vs agent 区分 + 简单可组合模式」。当前采用率：已成业界 agent 设计默认参考（Simon Willison 背书，AI Engineer 把 Agent Engineering 立为独立 track）。 (evidence: [T03-S002] + 04-canon)
  - **2024-11 起，由 MCP（Model Context Protocol）成事实标准驱动**，agent 工具集成从各家私有协议转向 MCP，PM 的工具选型决策树要改写（06-glossary 工作流变化种子明确点出）。 (evidence: 06-glossary)
  - 触发事件类型：行业事件（Anthropic 纠偏文）+ 新标准（MCP）。
  - **稳态判断**：**这是本 track decay 最快的 workflow**。workflow vs agent 区分较稳，但「怎么落地 agent」的工程共识 2023→2025 已大变，2026→2027 大概率再变（coding agent 形态、MCP 定型、reasoning 模型内化规划）。
- **典型耗时**: 入门 SOP 4-8 周；资深路径 2-4 周（复用 Anthropic 五模式 + 直接 API）。
- **关键工具（与 Track 02 关联）**: Anthropic SDK / OpenAI Assistants API（必备）；LangChain / LlamaIndex（场景特化，注意「过度抽象」争议）；MCP（新兴-快速成核心）；沙箱 / guardrails 工具（OpenAI Agents SDK guardrails 类，必备）；τ-bench（agent 可靠性评估）。
- **关键人物（与 Track 01 关联）**: Anthropic 工程团队（Erik Schluntz / Barry Zhang，「Building Effective Agents」作者）；Shunyu Yao（ReAct + τ-bench）；Simon Willison（agent 定义辨析 + 背书）；swyx（AI Engineer 把 Agent Engineering 立为主题）。*待与 Track 01 对齐。*
- **常见失败模式**:
  - **把不是 agent 的需求做成 agent**：触发原因 = 「agentic」是 2025-2026 最滥用前缀;怎么避免 = step 1 强制过 workflow vs agent 判断，默认假设是 workflow。（**CLI 自检项**：Can this task run on a predefined code path? If yes — build a workflow, not an agent. Most needs are workflows.） (evidence: [T03-S002])
  - **一上来上重框架**：触发原因 = 觉得框架「专业」;怎么避免 = 从 LLM API 直接起步，几行代码能实现的不上框架。（**CLI 自检项**：Did you reach for a framework before trying the raw LLM API? Many agent patterns are a few lines of code — frameworks obscure debugging.） (evidence: [T03-S002])
  - **工具文档糊弄、不做 Poka-yoke**：触发原因 = 觉得调 prompt 才是重点;怎么避免 = 工具工程投入对标 prompt 工程。（**CLI 自检项**：Did you spend as much effort on tool docs/interfaces as on prompts? Bad tool design — not a "dumb model" — causes most tool-call errors.） (evidence: [T03-S002])
  - **用单次 demo 作 ship 门**：触发原因 = demo 跑通了很兴奋;怎么避免 = ship 门改成 pass^k 多次运行稳定通过率。（**CLI 自检项**：Is your ship criterion "the demo worked"? Replace it with pass^k — run the same task k times and measure stable success rate.） (evidence: [T03-S002] + 04-canon τ-bench)
- **来源** (≥ 3):
  - [Primary] Anthropic「Building Effective Agents」: https://www.anthropic.com/research/building-effective-agents（collected: 2026-05-14）
  - [Primary] Hamel Husain field-guide（沙箱测试 + 合成数据，agent 同样适用）: https://hamel.dev/blog/posts/field-guide/（collected: 2026-05-14）
  - [Reference] 04-canon Track：ReAct (Yao 2023) + τ-bench (Yao/Sierra 2024) + Simon Willison 解读
- **Last_updated**: 2026-05-14
- **Decay risk**: **high**——本 track 衰减最快。intake 默认所有 LLM 时代 agent workflow 标 high；workflow vs agent 区分稳，落地工程 12 个月内大概率显著改写。

---

### 6. 搭数据飞轮（「生产 → 数据飞轮」，high decay）

- **One-liner**: MVP 上线、有真实流量之后，把「用户用得多」变成「产品越用越好」的自增强闭环 —— 从「有流量但没有差异化沉淀」状态到「production trace → 标注 → eval/finetune 数据 → 模型/产品升级 → 更好体验」转起来的飞轮。
- **Trigger**: MVP 上线、有稳定真实流量，要建立长期差异化（不只靠 frontier 模型本身）。**业务触发**为主。 (evidence: [T03-S003, T03-S004])
- **Output**: 一个转起来的闭环：(a) production 输入/输出/结果被系统化 log 成 trace (b) 按计划采样 + 自动路由模糊/高成本 case 给专家 (c) 专家判断回流进 eval + error analysis (d) 持续更新 prompt / 工具 / 模型 / finetune 数据集。 (evidence: [T03-S003, T03-S004, T03-S012])
- **入门 SOP（minimum viable steps）**:
  1. **设计反馈采集**：在产品里埋用户反馈机制（显式打分 / 隐式信号 / 编辑行为），从 day 1 就想好收什么。PM 主导。跳过 → 上线半年才发现没存到能用的信号，飞轮根本没燃料。 (evidence: [T03-S004])
  2. **系统化 log production trace**：把每次 query 的输入 / 输出 / 工具调用 / 结果完整 log。PM 定字段 + 工程师建管线。跳过 → 出了问题没法复盘，trace 当普通 log 扔了。 (evidence: [T03-S003])
  3. **按计划采样 + 路由给专家**：定期采样 production 日志，把模糊 / 高成本 / 失败 case 自动路由给领域专家标注。PM 定采样策略 + 工程师建路由。跳过 → 攒了一堆数据没人看，等于没攒。 (evidence: [T03-S003, T03-S012])
  4. **专家判断回流进 eval + finetune 数据集**：专家标注既喂 eval 套件（接 Workflow 4），也攒成 finetune 数据集。PM + 领域专家。跳过 → 标注成本花了但只用一次，不沉淀成可复用资产。 (evidence: [T03-S003, T03-S004])
  5. **用沉淀数据更新产品**：优先 prompt / context / 检索更新，够格了才 finetune;evals 和 finetune 数据是少数能跨模型/技术迁移的资产。PM 主导决策 + 工程师执行。跳过 → 飞轮转了但产品没真的变好，闭环断在最后一环。 (evidence: [T03-S003, T03-S004])
- **资深路径（差异点）**:
  - **skip**：资深人**在产品早期坚决跳过「建飞轮」**——没有足够真实流量时硬建飞轮是过度工程;他们先把 Workflow 3/4 做扎实，飞轮等流量起来再建。 (evidence: [T03-S003] + 04-canon 数据飞轮 disputed)
  - **optimize**：资深人**把「人工翻数据」优化成「按计划自动采样 + 自动路由模糊/高成本 case 给专家」**——靠组织纪律维持「采样→标注→改进 evaluator」的节奏，不靠某个人记得。 (evidence: [T03-S003, T03-S012])
  - **add**：资深人**额外做飞轮 ROI 的诚实评估**——初学者把 data flywheel 当万能护城河（融资 pitch 高频词），资深人 / a16z 清醒派知道「data moat 多半是空头支票」、多数飞轮没真转起来，会诚实评估「我们这个飞轮到底有没有产生可迁移的差异化资产」。 (evidence: 06-glossary data flywheel disputed + 04-canon)
- **近期变化**（近 12 个月）：
  - **2025 年起，由 eval 工具成熟驱动**，数据飞轮和 eval 迭代循环（Workflow 4）边界融合——「从 production 日志拉真实失败 → 路由专家 → 加进 eval」既是飞轮也是迭代。 (evidence: [T03-S012, T03-S014])
  - **2025 年内争议升温**：长 context 模型 + frontier 模型快速变强，「模型派」质疑私有数据飞轮的价值——a16z「The Empty Promise of Data Moats」。**矛盾保留**：飞轮派认为是核心差异化;模型派认为 frontier 升级会碾平多数私有数据优势。 (evidence: 06-glossary data flywheel disputed)
  - 触发事件类型：新工具 + 行业事件（模型能力跃迁引发的范式争论）。
  - **稳态判断**：飞轮的「采集→标注→改进」机械流程较稳;但「飞轮值不值得做 / 能不能形成护城河」这个**产品判断本身在剧烈争论中**，且 frontier 模型每次大升级都会重新洗牌。标 high decay。
- **典型耗时**: 入门 SOP 建起闭环 3-6 周;资深路径 2-4 周（复用 Workflow 3/4 的 eval 基础设施）。之后是**持续运营**，不是一次性。
- **关键工具（与 Track 02 关联）**: 用户反馈工具（Pendo / Sprig，必备但 AI 专属反馈尚不成熟）；trace / observability（Datadog LLM Observability，必备）；数据标注（Surge AI / Scale AI / Argilla / Label Studio，场景特化）；eval 平台（复用 Workflow 3）。
- **关键人物（与 Track 01 关联）**: Eugene Yan（llm-patterns「collect user feedback」+ eval-process「eval 流程即数据飞轮」）；Chip Huyen（《Designing ML Systems》的数据 / 漂移 / 监控观）；a16z（「data moat 多半空头支票」的清醒派代表）。*待与 Track 01 对齐。*
- **常见失败模式**:
  - **「收集了用户数据」就以为有飞轮**：触发原因 = 把「攒数据」等同于「飞轮」;怎么避免 = 检查是否真闭环回了模型/产品改进。（**CLI 自检项**：Does your "flywheel" actually close the loop back into model/product improvement, or are you just accumulating data nobody acts on?） (evidence: 06-glossary data flywheel)
  - **没从 day 1 设计反馈采集**：触发原因 = 上线时只想着功能;怎么避免 = scoping/MVP 阶段就定好收什么信号。（**CLI 自检项**：Did you design feedback capture before launch? Retrofitting it after months means you've lost the flywheel's fuel.） (evidence: [T03-S004])
  - **标注数据只用一次、不沉淀**：触发原因 = 没意识到 eval/finetune 数据是可迁移资产;怎么避免 = 专家标注同时喂 eval 套件 + finetune 数据集。（**CLI 自检项**：Are your expert annotations feeding both your eval suite AND a reusable finetune dataset? These are among the few assets that transfer across models.） (evidence: [T03-S003, T03-S004])
  - **把飞轮当万能护城河、不做 ROI 评估**：触发原因 = 融资叙事诱惑;怎么避免 = 诚实评估飞轮是否真产生可迁移差异化，接受「多数飞轮没转起来」。（**CLI 自检项**：Are you claiming "data flywheel" as a moat in pitches? Honestly assess whether it produces transferable differentiation — most flywheels never spin up.） (evidence: 06-glossary data flywheel disputed)
- **来源** (≥ 3):
  - [Primary] Eugene Yan「Patterns for Building LLM-based Systems & Products」（collect user feedback / data flywheel）: https://eugeneyan.com/writing/llm-patterns/（collected: 2026-05-14）
  - [Primary] Eugene Yan「eval-process」（eval 流程即数据飞轮）: https://eugeneyan.com/writing/eval-process/（collected: 2026-05-14）
  - [Secondary] Braintrust「Eval-Driven Development」（log→采样→路由专家→加进 eval）: https://www.braintrust.dev/articles/eval-driven-development
  - [Reference] 06-glossary data flywheel disputed（飞轮派 vs a16z 祛魅派）
- **Last_updated**: 2026-05-14
- **Decay risk**: **high**——机械流程较稳，但「飞轮值不值得做」的产品判断在剧烈争论，frontier 模型每次升级重洗牌。

---

## 贯穿全流程：AI PM 与 ML 工程师 / 数据 / 标注 / 法务的协作边界

> 这是 intake research_strategy_notes Track 03 明确要求「画清」的部分。本节不是独立 workflow，是 6 个 workflow 共用的协作底图。**证据偏「eval 协作」场景**（最清晰的一手描述都在那），其它边界尽量标注。

### AI PM ↔ ML / AI 工程师（证据最强）

| 维度 | AI PM 拥有 | ML / AI 工程师拥有 | evidence |
|------|-----------|-------------------|----------|
| **产品规格 / 成功标准** | PM 是首席领域专家，定义「AI 产品该做什么」的 spec、成功标准、failure mode 分类 | 工程师不定义产品该做什么 | [T03-S006, T03-S008] |
| **Prompt** | **PM + 领域专家写 prompt**，然后提交进 codebase（多个一手来源明确：「工程师不被允许改 prompt」） | 工程师支持 prompt 迭代的工具链，但不主导 prompt 内容 | [T03-S007, T03-S008, T03-S009] |
| **Error analysis / 看 trace** | PM 亲自做——拉真实交互、标对错、归类 failure mode | 工程师参与根因分析，但 error analysis 起点是 PM | [T03-S001, T03-S006, T03-S008] |
| **Eval 策略 + golden set** | PM 定 eval 策略、和领域专家共建 golden set、定 rubric、标注校准样本 | 工程师建 scorer、写复杂 evaluator、接 production 数据到 eval 管线 | [T03-S006, T03-S008] |
| **简单 vs 复杂改动** | PM 可直接调系统 prompt 等简单任务 | 工程师 tweak 工具调用 / 架构 / finetune 等复杂任务 | [T03-S006, T03-S008] |
| **基础设施** | PM 不碰 | 工程师建连接 production 数据和 eval loop 的基础设施 | [T03-S008] |

- **核心边界一句话**：「定义 AI 产品该做什么 + 用领域知识迭代 prompt + 拥有 eval 策略」是 PM 的;「建基础设施 + 复杂技术实现（工具调用 / 架构 / finetune / scorer）」是工程师的。是清晰但高度协作的分工。 (evidence: [T03-S008])
- **近期变化**：2025 年起，由 AI 让「PM 直接写 prompt / 撸原型」成为常态驱动，PM 和工程师的界线在**模糊化**——Humanloop 直接以此为题。但「模糊」不等于「没有」：模糊的是「谁动手」，清晰的是「谁对产品规格负责」。 (evidence: [T03-S009])
- **矛盾保留**：「AI PM 要不要会代码 / 懂模型」无定论——CS336 深水区路线 vs Andrew Ng 非技术路线（04-canon 已记），对应 intake「角色定义不统一」。本边界表是按「技术理解 + 产品 sense 双修的 AI PM」这一主流定义画的。

### AI PM ↔ 数据 / 标注

- **证据较薄**，从 workflow 3/6 推断：PM 定**标什么、采样策略、rubric**;领域专家 / 标注团队（内部或 Surge AI / Scale AI 外包）执行标注;PM 决定「标注外包还是内部做」（外包扩量但 rubric 必须 PM 定，且校准必须针对自家数据，不能外包判断）。 (evidence: [T03-S001, T03-S003] 推断)
- **关键 tell**：PM 不能把「定义什么是好」外包给标注供应商——校准是 domain-specific 的（06-glossary、T03-S001 反复强调「premature tool/judgment outsourcing」是反模式）。

### AI PM ↔ 法务 / 合规 / 安全

- **证据最薄**，从 Wave 1 + workflow 1 推断：
  - **法务**：PM 在 scoping 阶段做风险分级判定（是否落入 EU AI Act 高风险 / 中国生成式 AI 办法），高风险产品法务**早期**介入;日常「深度合规是法务的活，AI PM 更多是知道存在 + 触发判断」（06-glossary 明确）。 (evidence: 06-glossary + [T03-S006] 推断)
  - **安全 / 红队**：guardrails 设计 PM 提需求、工程师实现;红队（goal hijacking / 工具链攻击 / 越权探测）通常是专门安全角色，PM 定「哪些失败不可接受」的边界。证据不足以画细，**Phase 2.8 应标注此边界信号薄弱**。 (evidence: 06-glossary guardrails/red team 条目)

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 workflow 都包含的步骤（候选 playbook 通则）

- **「PM 亲自看 trace / 真实输出做 error analysis」** 出现于：Workflow 1（定义成功标准前先看）/ 3（step 1）/ 4（step 1 Analyze）/ 6（采样路由） → **强候选 playbook**「如果质量/方向不明 → 先 PM 亲自拉 10-50 个真实 trace 逐条标，再做任何决策」（4 个 workflow + intake 反复强调）
- **「先简单 / 最便宜的假设，验证了才加复杂度」** 出现于：Workflow 1（prompt→RAG→agent→finetune 阶梯）/ 3（code-based check 先于 LLM-judge）/ 4（改 prompt 先于改架构、finetune 最后）/ 5（LLM API 先于框架、workflow 先于 agent） → **强候选 playbook 兼心智模型**「如果遇到 AI 技术决策 → 默认从最便宜/最简单的假设起，只在验证不够时才升级」
- **「binary pass/fail + 频率排序，不靠 vibes / 不靠 1-5 分」** 出现于：Workflow 3（judge 用 binary）/ 4（binary + 频率定优先级）/ 5（pass^k 作门） → 候选 playbook「如果要判断 AI 质量 → 用二元判定 + 频率计数，不用模糊分数、不用『我觉得』」
- **「为学习而造 vs 为交付而造分清」** 出现于：Workflow 1（用原型替代规格）/ 2（throwaway POC）/ 5（沙箱大量测试） → 候选 playbook
- **「成本约束 / token 经济模型前置」** 出现于：Workflow 1（scoping 就算）/ 5（agent 二次方 token 增长）/ 6（高成本 case 路由） → 候选 playbook

### 入门 SOP 和资深路径之间最大的差距（候选心智模型）

- 入门 SOP 平均 5-6 步，资深路径几乎不「压缩步数」，而是**在同样步数里换打法 + 额外加 2-3 个初学者会跳的事**——这本身是强信号：**AI PM 这一行的资深差异不在「少做几步」，在「不跳过看似可省的硬步骤」（error analysis / judge 校准 / pass^k 门 / desirability 验证 / 飞轮 ROI 评估）**。
- 跨 6 个 workflow，资深「add」差异点高度集中在三类：(1) **不确定性管理**——明确写下「不知道什么」而非假装规格能写全;(2) **抵抗过早优化/自动化/外包**——judge 校准不能外包、不过早全自动化、飞轮不早建;(3) **诚实的现实校准**——pass^k 而非 demo、desirability 而非可行性、飞轮 ROI 而非护城河叙事。→ **候选心智模型**：「AI PM 的资深 = 对抗『看起来在推进』的假象，坚持做慢但对的硬步骤」。
- 资深「skip」差异点集中在：跳过传统 PM 惯性动作（冗长市场调研、工程级原型代码、通用 dashboard、重框架）——**候选心智模型**：「AI 时代『能不能建』不再是瓶颈，传统 PM 里围绕『降低构建风险』的动作很多可以砍」。

### 近期工作流变化的根本原因

- 触发变化的事件类型分布（6 个 workflow）：
  - **新工具驱动**：Workflow 1（AI 原型工具）/ 2（同）/ 3（eval 工具成熟）/ 4（online 层工具）/ 6（eval 工具）—— **5/6，主导驱动力**
  - **新标准 / 范式形成驱动**：Workflow 3（eval-driven development 成范式）/ 5（MCP）—— 2/6
  - **法规变化驱动**：Workflow 1（EU AI Act 高风险条款 2026-08）—— 1/6
  - **行业事件驱动**：Workflow 5（Anthropic 2024-12 agent 纠偏文）/ 6（frontier 模型跃迁引发飞轮价值争论）—— 2/6
- **主要驱动力 → Phase 2「外部驱动力」**：(1) **AI 原型 / eval 工具链成熟**——把 PM 能力边界外推（自己撸原型、自己建 eval），是最强外部驱动;(2) **eval-driven development 范式形成**——重塑整个产品流程;(3) **frontier 模型能力跃迁**——既是机会也持续推翻旧 workflow（尤其 agent / RAG / 飞轮）。

### 冷僻 / 信号薄弱

- workflow 数：**6**（≥ 4 ✅，不触发冷僻协议）
- 一手 source 占比：18 条 manifest 中 verified_primary **12 条 = 67%**（≥ 50% ✅）。一手集中在 Hamel ×3 / Eugene Yan ×3 / Anthropic / Vercel / OpenAI ×2 / Aman Khan / Humanloop。
- 资深差异点：6/6 workflow 都有 ≥ 2 处（实际多数 3 处，含 skip+optimize+add），**100% ≥ 2 处 ✅**
- 近期变化字段：6/6 都填了具体日期 + 触发事件（✅，无「稳态」填法——本行确实没有稳态 workflow）
- **但需在 Phase 2.8 诚实边界标注三点**：
  1. **「五阶段完整 SOP」是拼接的**：本行 <3 年，没有一手长文从「想法」走到「数据飞轮」，6 个 workflow 的串联有推断成分。
  2. **PM/工程师/数据/法务边界证据不均**：PM↔工程师边界证据强（多个一手），PM↔数据/标注 中等（推断为主），PM↔法务/安全/红队 **薄弱**——这块在 synthesis 要诚实降级。
  3. **eval 派幸存者偏差**：workflow 证据高度来自 eval 派（Hamel/Eugene Yan/Shreya）+ eval 工具厂商。「模型派」（少做 eval、等模型变好）几乎不写 workflow 长文——不代表不存在，矛盾已在 Workflow 6 保留。
  4. **decay 全员偏高**：6 个 workflow 无一稳态，最低也是 low（且 low 那个是「方法稳工具变」）。**强烈建议本 skill 工作流模块每 3-6 个月跑一次 update**——这是 SKILL.md Phase 0C 的首要刷新对象。

---

## Phase 2 接口

- **本 track（Wave 3）→ Phase 2.2（playbook）**：上「反复出现的步骤」5 条已结构化为候选 playbook，其中「先看 trace 再决策」「先简单后复杂」「binary + 频率」三条跨 ≥ 3 workflow，是高置信 playbook 种子。
- **本 track → Phase 2.4（workflow section）**：6 个 workflow 卡可直接组装成 SKILL.md 工作流节。建议组装顺序按「想法→POC→eval体系→迭代→agent→飞轮」的产品生命周期线，并在节首明确标「本节 decay 最快，6 个月内大概率需 update」。入门 SOP / 资深路径已分开写，可直接搬。
- **本 track → Phase 2.1（心智模型）**：本 track 浮现的候选心智模型——(1)「AI 时代『能不能建』不再是瓶颈，desirability 才是」(2)「资深 AI PM = 对抗『看起来在推进』的假象，做慢但对的硬步骤」(3)「先简单/最便宜的假设，验证了才升级复杂度」——前两个与 04-canon 的「Eval 是地基」「workflow vs agent 要分清」「AI 不可靠是常态」相互印证，跨 track 证据充足，够格升心智模型。
- **本 track → Phase 2.6（质量基准 + 反模式）**：每个 workflow 的「常见失败模式」（已写成 actionable、CLI-ready 的 yes/no 自检项）直接进反模式节。跨 workflow 高频反模式：「跳过 error analysis 上 dashboard」「demo 当 ship 门」「过早外包/自动化判断」「成本不算就开干」「把不是 agent 的做成 agent」。
- **本 track → Phase 2.8（诚实边界）**：见上「冷僻/信号薄弱」4 点——五阶段拼接 / 边界证据不均 / eval 派幸存者偏差 / decay 全员偏高。其中「decay 全员偏高」直接进 honesty section 作核心警告。
- **反馈给 Track 02（tools）**：本 track 反复出现但 intake key_tools 未单列或未明确评级的——**MCP**（Workflow 5 核心，06-sources 也强调）应作核心收录;**自建 data viewer**（Workflow 3/4 资深标配，Hamel 强调「迭代快 10x」）是一类「工具」但不是产品，Track 02 需决定怎么归类;**AI 原型工具**（Claude Code / v0，Workflow 1/2 必备）应进必备层。
- **反馈给 Track 01（figures）**：本 track 的 workflow 骨架几乎全部来自 Hamel Husain（3 个 workflow 的主来源）、Eugene Yan（2 个）、Anthropic 工程团队（1 个）——这三者应是 Track 01 的最高优先 figures。另：Aman Khan（Arize，PM/工程师边界一手描述）、Shreya Shankar（Hamel evals 课共同讲师 + criteria drift）是 Track 01 候选补充。
- **一致性检查提示（Phase 1.5）**：本 track 因 Wave 2 文件缺失，Track 01/02 关联字段是基于 04-canon 推断填的。若 Track 01/02 实际产出与此不符（尤其国内 figures / 国内工具栈），说明本 workflow 列表偏「海外工程向 eval 派」——与 intake「国内外路径差异大」「学派分歧大」一致，**需在 synthesis 诚实边界明说本 track 的 workflow 几乎全是海外一手、eval 派主导**。

---

*调研者注：本文件 18 个 source，verified_primary 12 + secondary 6，一手占比 67%。0 个黑名单 URL 入表。最大不确定性：(1) Wave 2（figures/tools）文件本次缺失，跨 track 关联字段为推断;(2)「想法→…→数据飞轮」五阶段的完整 SOP 在公开材料中不存在，6 workflow 的串联有拼接成分;(3) PM↔法务/安全边界证据薄弱;(4) 全部 6 个 workflow decay 偏高，本行 SOP 仍在快速成型。下次 refresh（强烈建议 ≤ 6 个月，最好 3 个月）重点：agent 产品化 workflow（decay 最快）、MCP 是否定型、eval 工具层是否收敛、EU AI Act 高风险条款 2026-08 落地后的 scoping workflow 实际变化、是否出现「模型派」的成体系 workflow 长文。*
