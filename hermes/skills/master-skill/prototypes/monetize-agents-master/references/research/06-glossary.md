# Track 06 — Glossary (Monetizing AI Agents)

> Phase 1 wave 1. ~95 entries. 行业混合 3 套术语: SaaS finance / B2B + AI/ML technical + Indie hacker. 同词在不同学派 register 不同, 必标. 核心冲突: per-seat → per-token → outcome-based 定价之战 (2026), B2B vs Indie 资本结构语言投射, EU AI Act vs 中国备案制 vs US Section 230 监管哲学三派.

## Source Manifest

| source_id | url | bucket | last_checked | author | note |
|-----------|-----|--------|--------------|--------|------|
| T06-S001 | https://www.bvp.com/atlas/cloud-computing-metrics | surrogate_primary | 2026-05-04 | Bessemer | 五大 cloud finance metrics 原始定义 (vendor docs) |
| T06-S002 | https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook | surrogate_primary | 2026-05-04 | Bessemer | 2026 AI agent pricing playbook (vendor docs) |
| T06-S003 | https://a16z.com/12-things-about-product-market-fit/ | surrogate_primary | 2026-05-04 | a16z | PMF 起源 (Andreessen 2007) (vendor docs) |
| T06-S004 | https://chartmogul.com/saas-metrics/nrr/ | surrogate_primary | 2026-05-04 | ChartMogul | NRR 业内通用定义 (vendor docs) |
| T06-S005 | https://openviewpartners.com/blog/your-guide-to-reverse-trials/ | verified_primary | 2026-05-04 | OpenView | Reverse trial vs freemium |
| T06-S006 | https://productled.com/book/product-led-growth | surrogate_primary | 2026-05-04 | Wes Bush | PLG 概念发明者 (vendor docs) |
| T06-S007 | https://sierra.ai/blog/outcome-based-pricing-for-ai-agents | verified_primary | 2026-05-04 | Sierra | Outcome-based 旗手 vendor 立场 |
| T06-S008 | https://www.chargebee.com/blog/pricing-ai-agents-playbook/ | verified_primary | 2026-05-04 | Chargebee | 2026 agent pricing playbook |
| T06-S009 | https://openai.com/policies/usage-policies/ | verified_primary | 2026-05-04 | OpenAI | API ToS spam / 自动化禁条 |
| T06-S010 | https://openai.com/policies/using-chatgpt-agent-in-line-with-our-policies/ | verified_primary | 2026-05-04 | OpenAI | ChatGPT agent 合规边界 |
| T06-S011 | https://artificialintelligenceact.eu/implementation-timeline/ | surrogate_primary | 2026-05-04 | EU AI Act SD | EU AI Act 时间轴 (2026-08 主体生效) (vendor docs) |
| T06-S012 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | surrogate_primary | 2026-05-04 | EU Commission | AI Act 立法机构原文 (vendor docs) |
| T06-S013 | https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm | verified_primary | 2026-05-04 | 国家网信办 | 生成式 AI 暂行办法原文 |
| T06-S014 | https://www.cac.gov.cn/2026-01/09/c_1769688009588554.htm | verified_primary | 2026-05-04 | 国家网信办 | 2025 备案 748 家公告 |
| T06-S015 | https://www.indiehackers.com/post/indie-doesn-t-mean-bootstrapped-anymore-a88300c012 | secondary | 2026-05-04 | Indie Hackers | indie 派内部术语漂移 |
| T06-S016 | https://www.wallstreetprep.com/knowledge/saas-magic-number/ | secondary | 2026-05-04 | WSP | Magic Number 公式 + benchmark |
| T06-S017 | https://www.drivetrain.ai/strategic-finance-glossary/what-is-the-ltv-cac-ratio | secondary | 2026-05-04 | Drivetrain | LTV/CAC 3:1 benchmark |
| T06-S018 | https://techcrunch.com/2026/02/21/google-vp-warns-that-two-types-of-ai-startups-may-not-survive/ | secondary | 2026-05-04 | TechCrunch | "GPT wrapper" 贬义 Google VP 警告 |
| T06-S019 | https://www.indiehackers.com/post/4-years-into-an-appsumo-lifetime-deal-the-unvarnished-math-and-a-question-i-m-stuck-on-4dd2b262ac | secondary | 2026-05-04 | Indie Hackers | LTD 长期 unit economics 复盘 |

## Tier 1 — 核心必懂 (32, evidence: [T06-S001, T06-S002, T06-S003, T06-S004])

### 财务 / 阶段 (12)
| 术语 | Insider def | Outsider tell |
|------|-------------|---------------|
| ARR | 年化 recurring 收入, B2B 估值锚 | 把 one-time / GMV 算进 ARR |
| MRR | 月度 recurring, indie 派成就单位 | LTD 收入摊进 MRR |
| ACV | 单合同年价值, B2B 必报 indie 不用 | ACV 描述 PLG 自助产品 |
| CAC | 获客全成本含 S&M overhead | 只算广告费 |
| LTV | 生命周期 **gross profit** (非 revenue) | LTV 用 revenue 算 (虚高) |
| LTV/CAC | ≥3 健康, >5 是 underinvest | 看到 10:1 越高越好 |
| NRR | 含扩展留存, >100% 净增长 (T06-S004) | 跟 GRR 混 |
| Rule of 40 | growth + profit margin ≥40% | 把纯亏损率当 profit |
| Magic Number | (ΔARR×4)/上季 S&M; >0.75 健康 (T06-S016) | 跟 LTV/CAC 混 |
| Burn / Runway | 月烧 + 现金跑道; default-alive 反义 | 把 ARR 当 cash |
| PMF | Sean Ellis 40% very-disappointed (T06-S003) | "launched 即 PMF" |
| ICP | 含 anti-needs 的具体客户画像 | ICP = persona |

### Pricing (8)
| 术语 | Insider def | Outsider tell |
|------|-------------|---------------|
| Per-seat | 每席位订阅, 经典 SaaS; agent 时代受冲击 | 套给 agent 自己 |
| Per-token | 按 LLM token 量计费, 利润率风险 | 等同 per-call |
| Per-task | 按完成任务计费, agent-native (T06-S008) | 跟 per-call 混 |
| Outcome-based | binary measurable event 收费 (Intercom $0.99/resolved ticket) (T06-S007) | "outcome" 不可度量 |
| Usage-based | 按消耗计量, AWS/Stripe 派 | usage = per-seat 浮动 |
| Freemium | 永久免费层 +升级, 3-15% 转化 | 把 free trial 叫 freemium |
| Reverse trial | 全功能限时 → 降级 freemium (T06-S005) | 当 free trial 同义 |
| LTD (Lifetime Deal) | 一次付费 lifetime, indie 圈双刃 (T06-S019) | LTD 当增长策略 |

### GTM / 商业模式 (7)
| 术语 | Insider def | Outsider tell |
|------|-------------|---------------|
| PLG | 产品做 acquisition + retention + expansion (T06-S006) | PLG = 有 free tier |
| SLG | 销售主导 GTM, 大合同 / 长 cycle | "传统土" |
| Land-and-expand | 小合同入门 → 内部扩张, NRR 引擎 | 一次卖 ELA |
| Wedge | 切入小痛点后扩展 | 一上来就 horizontal |
| Moat | 跨周期防御性 | feature = moat |
| Build in public | 公开 metrics 换 distribution | 公开 = 求关注 |
| Bootstrap | 不拿外部融资, 收入复投 | bootstrap = 没钱 |

### Agent / AI specific (5)
| 术语 | Insider def | Outsider tell |
|------|-------------|---------------|
| Agent | LLM 驱动多步自主执行体 | agent = chatbot |
| Eval | dataset + metric + judge, 不是 prompt 调试 | 让 LLM 评 LLM |
| Hallucination | 自信但事实错; agent 商业化最大风险 | 任何错都叫 hallucination |
| RAG | retrieval + LLM 架构 pattern | RAG = vector DB |
| GPT wrapper | 仅 UI 包 API, 无 moat (T06-S018) | 自称 wrapper (会被嘲) |

## Tier 2 — 周边熟知 (40)

- **财务 / 阶段**: ARPU, Gross margin (agent 60-70% vs SaaS 80%+), CARR, Payback period (SMB <12 / 企业 ≤24 月), Default alive (Graham), Time-to-PMF, Pre/Post-PMF, Pre-seed→Series A-C, 10x ARR multiple (2021 顶 → 2024+ 6-8x), SAFE, TAM/SAM/SOM
- **Pricing**: Annual prepay discount (10-20%), Tiered task pricing ($2→$80 tier 1-4, T06-S008), Hybrid pricing (base + outcome 2026 主流, T06-S002), ARR upgrade path (self-serve→team→enterprise)
- **GTM**: Bottom-up vs Top-down, CLG (Community-Led, OSS/dev tool 派), Founder-led sales (<$1M ARR 必须), Outbound/Inbound, POC vs Pilot (pilot 收费 / POC 免费), PQL/MQL, RevOps, Discovery call
- **Agent / technical**: Multi-agent system (商业化包装词), Tool use, Function calling (OpenAI 厂商词), Token economy, Context window economics, Prompt engineering (包装为 "agent customization"), Agentic (营销词内行皱眉), HITL
- **Indie / 咨询 / OSS**: Audience-first (1000 true fans), Ship daily, Side hustle, Solo founder, $X MRR milestone ($1k/$10k/$100k 文化), Day rate/Retainer, Dual licensing, Hosted offering (OSS 变现), Enterprise edition (SSO/audit/SLA), API arbitrage (anti-pattern, 套壳灰色)

## 学派对照 (核心差异, 同词不同义)

| 概念 | B2B 派 | Indie 派 | 咨询派 | VC 派 | OSS 派 |
|------|--------|---------|--------|------|--------|
| 收入单位 | ARR/ACV | MRR | Day rate/Retainer | ARR (估值锚) | Hosted ARR + 服务 |
| 增长哲学 | Land-and-expand/NRR | Audience/Build-in-public | Pipeline/Referrals | TAM × 渗透 | Adoption → Monetize |
| Free 含义 | Free trial (限时) | Freemium (永久) | Free discovery | (无 free 概念) | OSS = free core |
| "Production" 含义 | SLA + uptime + procurement | "shipped" + live URL | "delivered to client" | "in customer hands" | self-host + cloud |
| Pricing 哲学 | Per-seat → outcome (2026 转向) | Per-month flat / LTD | Project / outcome | 不参与 | Open core → enterprise |
| 看 LTD | 不用 | 双刃剑 (T06-S019) | 不存在 | 反对 (反 ARR) | 不用 |
| 拒绝对手术语 | "indie", "vibe" | "RevOps", "enterprise sales" | "MRR" 无关 | "lifestyle" | "proprietary" |

**核心冲突**: B2B 认为 "MRR < $10k 是 hobby"; indie 认为 "$10k MRR 是自由". VC 看 ARR + growth, indie 看 profit + 自由. **2026 定价之战**: Token 派 (Anthropic / OpenAI) vs Outcome 派 (Sierra / Intercom), Bessemer (T06-S002) 押 hybrid.

## 法律 / 合规 / 监管

| 名称 | Type | Issued | Last revised | Decay | 关键点 |
|------|------|--------|--------------|-------|--------|
| EU AI Act | regulation | 2024-08 force | **2026-08 主体生效** + GPAI 2025-08 + 2027-08 grandfather (T06-S011) | high | extraterritorial 类似 GDPR; 风险分级 |
| 中国生成式 AI 暂行办法 | regulation | 2023-08-15 (T06-S013) | 2025 累计 748 家备案 (T06-S014) | high | 备案 ≠ 审批, fail = takedown |
| ISO/IEC 42001 (AI 管理体系) | certification | 2023-12 | 2025 vendor 普及期 | medium | enterprise agent 平台 (Intercom/Fini) 已 ship |
| SOC 2 Type II | certification | TSC 2017 + 2022 | 2022 minor | low | ~66% B2B 买家门槛; "compliant" ≠ "report" |
| ISO 27001 | certification | 2013 → 2022 大修 | 2022-10 | low | 跟 SOC 2 区别: standard+cert vs attestation |
| HIPAA / GDPR / CCPA+CPRA | regulation | 1996 / 2018 / 2020+2023 | 2025 ADMT 规则 (CA) | medium | BAA 必须涵盖 LLM provider; GDPR Art 22 + AI Act 联动 |
| OpenAI Usage Policies | ToS | 持续 | 2025-10-29 大改 (T06-S009, T06-S010) | high | 禁 spam / fake review / fake storefront / 绕 rate limit |

**责任 / 侵权 (新, 法律未定型)**: Hallucination liability (Air Canada 案 / 律师 fake citations → 内行默认 ToS + HITL 节点), IP infringement (NYT v OpenAI 未结), Section 230 (US, AI 内容是否受保护 unsettled).

**学派对监管态度**: B2B 把合规当 wedge ("我们 SOC 2+HIPAA 对手没"); Indie 多飘合规线下方; VC 把 AI Act 当 GAFA-tier moat; 咨询派把帮客户合规当产品 (RegTech).

## 反模式术语 (内行听到秒识别外行)

| 反模式词 | 反映问题 | 内行替代 |
|----------|---------|---------|
| "AI-powered" / "Cognitive computing" / "Intelligent automation" | 没说清功能 | 具体能力 |
| "Agentic transformation" | 咨询咨询公司 buzzword | 具体 workflow 自动化 |
| "Human-in-the-loop AI" | 营销味 | HITL (缩写) |
| "Wrap GPT" / 自称 "GPT wrapper" | 自暴无 moat (T06-S018) | "vertical AI for X" |
| "Prompt-only product" | 无 defensibility | (内行避免) |
| "AI for AI's sake" / "Vibe coding 创业" | 没 ICP / 没 eval | "agent-shaped problem" / "ICP-driven build" |
| "Passive income SaaS" | 不存在 | "lifestyle business with active maintenance" |
| "Outcome-based" 但 outcome 不可度量 | 模糊收费 | binary measurable event |
| "我们 production 了" (只有 demo URL) | 滥用 register | 内行精确区分 prototype/staging/production/scale |

## Phase 2 提炼提示

**行业表达 DNA top 10 高频黑话**: ARR/MRR (双轨判 B2B vs Indie), PMF, ICP, Land-and-expand, NRR, Outcome-based (2026 定价之战核心), Build in public, Ship (动词), Eval (商业派挡 hallucination 责任), Wedge

**拒绝厂商话术 top 5**: "AI-powered", "Agentic transformation", "Cognitive computing", "Intelligent automation", "GPT wrapper" (自描述时)

**外行破绽 top 10**: ARR 含 one-time | LTV 用 revenue | LTD 摊进 MRR | PMF = launched | RAG = vector DB | per-seat 套 agent | "outcome-based" 无 measurable event | "production" = 有 demo URL | TAM 只贴报告无 SOM | "passive income SaaS"

**智识谱系**: per-seat → per-token → per-task → outcome-based (定价 register 演化反映 agent 经济学 frontier); B2B/SaaS finance 派 vs Indie hacker 派术语漂移 = 资本结构差异的语言投射; EU AI Act vs 中国备案制 vs US Section 230 = precaution vs approval vs immunity 三种监管哲学

**时效信号 (HIGH)**: 12 月内已修订: OpenAI Usage Policies (2025-10), GPAI 生效 (2025-08), 中国备案细则. 12 月内预计变化: EU AI Act 2026-08 主体生效 + 罚款机制, OpenAI/Anthropic ToS 高频更新, ISO 42001 vendor 标配化

**workflow 触发种子 (喂 Track 03)**: EU AI Act 2026-08 → EU 部署 agent workflow 全部补 risk classification + GPAI 文档; OpenAI Usage Policies 2025-10 重写 → "AI 内容生成" 类 agent 必须复读 spam / fake review / 自动化禁条; 国内备案 → ship agent 必须先备案; 2026 outcome-based 主流化 → pricing page / 合同 / billing 系统重做; ISO/IEC 42001 → 卖 enterprise 必答 "你们 42001 计划"

**冷僻信号**: 95 entries 远超 floor 40. 行业绝不冷, 反而是术语层叠 (3 套 vocabulary 混在一起). 主要风险是学派语言冲突, 不是数据稀疏.
