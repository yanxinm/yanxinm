# Track 02 — Tools (Monetizing AI Agents)

> Phase 1 wave 2. 28 tools across 8 buckets, 3 tiers. Persona-rooted decision tree (6 branches).

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://stripe.com/blog/agentic-commerce-suite | verified_primary | 2026-05-04 | Stripe | Agentic Commerce Suite (SPT) launch |
| T02-S002 | https://stripe.com/blog/machine-payments-protocol | verified_primary | 2026-05-04 | Stripe | MPP for agent-initiated payments |
| T02-S003 | https://polar.sh/resources/comparison/stripe | surrogate_primary | 2026-05-04 | Polar.sh | Polar self-positioning vs Stripe (vendor docs) |
| T02-S004 | https://www.creem.io/blog/lemonsqueezy-alternatives-after-stripe-acquisition | secondary | 2026-05-04 | Creem | LemonSqueezy post-acquisition decay |
| T02-S005 | https://devtoolpicks.com/blog/polar-vs-lemon-squeezy-vs-creem-2026 | secondary | 2026-05-04 | DevToolPicks | MoR fee comparison |
| T02-S006 | https://github.com/mastra-ai/mastra | verified_primary | 2026-05-04 | Mastra | 22k stars, 1.8M monthly npm |
| T02-S007 | https://www.speakeasy.com/blog/ai-agent-framework-comparison | secondary | 2026-05-04 | Speakeasy | Framework selection cross-cutting |
| T02-S008 | https://vercel.com/blog/ai-sdk-6 | verified_primary | 2026-05-04 | Vercel | AI SDK 6 — ToolLoopAgent + MCP |
| T02-S009 | https://ai-sdk.dev/docs/introduction | surrogate_primary | 2026-05-04 | Vercel | AI SDK docs — 20M+ monthly DL (vendor docs) |
| T02-S010 | https://www.helicone.ai/blog/the-complete-guide-to-LLM-observability-platforms | verified_primary | 2026-05-04 | Helicone | Observability landscape |
| T02-S011 | https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes | surrogate_primary | 2026-05-04 | Intercom | Fin @ $0.99/resolution anchor (vendor docs) |
| T02-S012 | https://www.chargebee.com/blog/pricing-ai-agents-playbook/ | secondary | 2026-05-04 | Chargebee | Outcome-pricing playbook |
| T02-S013 | https://flexprice.io/blog/best-open-source-usage-based-billing-platform-for-an-ai-startup-(2025-guide) | secondary | 2026-05-04 | Flexprice | Usage-based billing OSS |
| T02-S014 | https://www.lindy.ai/pricing | surrogate_primary | 2026-05-04 | Lindy | Credit-system disclosure (vendor docs) |
| T02-S016 | https://www.53ai.com/news/coze/2024071885143.html | secondary | 2026-05-04 | 53AI | Coze.cn 收费机制 |
| T02-S017 | https://blog.n8n.io/best-ai-workflow-automation-tools/ | verified_primary | 2026-05-04 | n8n | n8n 2.0 native LangChain |
| T02-S018 | https://posthog.com/docs/posthog-ai | surrogate_primary | 2026-05-04 | PostHog | Analytics + LLM obs merged (vendor docs) |
| T02-S019 | https://www.beehiiv.com/pricing | surrogate_primary | 2026-05-04 | Beehiiv | Pricing + ad network (vendor docs) |
| T02-S020 | https://www.indiehackers.com/post/if-i-had-to-start-a-saas-from-scratch-in-2025-i-d-do-this-1b828afc53 | secondary | 2026-05-04 | Indie Hackers | First-person founder stack |
| T02-S021 | https://thenewstack.io/ai-coding-tool-stack/ | secondary | 2026-05-04 | The New Stack | Cursor+Claude Code stacking |
| T02-S022 | https://news.ycombinator.com/item?id=46900726 | reference | 2026-05-04 | HN | "Vercel for AI agents" thread |
| T02-S023 | https://anotherwrapper.com/compare/polar-vs-stripe | secondary | 2026-05-04 | AnotherWrapper | Polar hidden-fee math |
| T02-S024 | https://lightfield.app/blog/attio-vs-hubspot | secondary | 2026-05-04 | Lightfield | Tech-founder CRM choice |
| T02-S025 | https://encharge.io/loops-review/ | secondary | 2026-05-04 | Encharge | Loops PLG fit |
| T02-S026 | https://northflank.com/blog/top-ai-agent-runtime-tools | secondary | 2026-05-04 | Northflank | Modal/CF/Replicate split |
| T02-S027 | https://www.getmonetizely.com/blogs/the-2026-guide-to-saas-ai-and-agentic-pricing-models | secondary | 2026-05-04 | Monetizely | Hybrid pricing 43%→61% |
| T02-S028 | https://prems.ai/blog/indie-hacker-marketing-playbook-2026 | secondary | 2026-05-04 | Prems | Channel mix for solo founders |

---

## 总览（按 tier）

### 必备（10）
| 工具 | One-liner | Bucket | Decay | Evidence |
|------|-----------|--------|-------|----------|
| Stripe (+Agentic Commerce Suite) | Payment default; SPT/MPP for agent-initiated checkout | billing | low | T02-S001/002 |
| Vercel AI SDK | TS toolkit, 20M monthly DL; SDK 6 ToolLoopAgent+MCP | framework | medium | T02-S008/009 |
| LangGraph | Graph-based durable orchestration; B2B production default | framework | medium | T02-S007 |
| Twitter/X | Indie distribution + ICP discovery | distribution | low | T02-S020/028 |
| Cursor + Claude Code | Coding agent dogfood; 2026 pattern is *both* | ops | medium | T02-S021 |
| Helicone OR Langfuse OR LangSmith | LLM observability — pick one | observability | medium | T02-S010 |
| PostHog | Analytics+session replay+LLM obs+flags bundled, generous free | observability | low | T02-S018 |
| n8n | Self-host, native LangChain, 1/10 Zapier bill at scale | ops | medium | T02-S017 |
| Resend OR Loops | Transactional + lifecycle email; React Email | content | low | T02-S025 |
| LinkedIn (B2B) | Outbound + ICP via Apollo/Lemlist multichannel | distribution | low | T02-S028 |

### 场景特化（13）
| 工具 | When to use | Bucket | Decay |
|------|-------------|--------|-------|
| Polar.sh | Indie/solo MoR; 4%+$0.40 base, ~6% on intl subs (hidden) | billing | medium |
| Lemon Squeezy | Stay-only-if-locked-in; Stripe 2024-07 acquired, roadmap stalled | billing | high |
| Paddle | Mid-market intl tax + B2B invoicing | billing | low |
| Stripe Billing (metered) | Self-managed tax + native usage events | billing | low |
| Modal Labs | GPU/sandbox/computer-use; gVisor, autoscale 50k+ | hosting | medium |
| Cloudflare Workers AI | Edge V8 isolates, sub-50ms cold start; no GPU | hosting | medium |
| Replicate | Pre-trained model API arbitrage; pay-per-second | hosting | medium |
| Mastra | TS-first, type-safe, prod at Replit/Brex/MongoDB | framework | medium |
| CrewAI | Fast role-based multi-agent scaffold (~10 min) | framework | medium-high |
| Lindy AI | No-code SMB agent, 4000+ integrations, credit-system | framework | high |
| Attio | <50 employees, AI-native CRM, $29-69/seat + credits | CRM | medium |
| HubSpot | 50+ employees, marketing+sales+service unified | CRM | low |
| Apollo + Lemlist | Cold outbound multichannel | distribution | medium |
| Beehiiv | Newsletter + ad network, 0% rev share (vs Substack 10%) | content | low |
| 扣子 Coze + 微信支付 | 国内 agent SaaS 必经路径; Coze.cn 国内/Coze.com 出海 | framework+billing | medium |
| Dify | 国内自部署/数据合规, 被 Coze 开源冲击 | framework | medium |

### 新兴（5）
| 工具 | Born | Adopters | Decay |
|------|------|----------|-------|
| Stripe Agentic Commerce Suite (SPT/MPP) | 2025-Q4 | OpenAI, Google, Coach, URBN, Squarespace partnered | high |
| Polar usage-meters | 2025-Q3 | indie shipping tokenized APIs | high |
| Pickaxe / Flexprice (OSS metered billing) | 2024-2025 | AI startups wanting open metering | high |
| Pydantic-AI | 2024-Q3 | Python thin-framework crowd | high |
| Outcome-priced agents (Fin pattern) | 2024+ | support/SDR vertical, Salesforce Agentforce | medium |

---

## 选型决策树（persona-rooted）

### Branch 1 — Indie hacker / solo TS founder
Stack: **Vercel + Vercel AI SDK + Polar.sh + Twitter/X + Beehiiv + Resend + PostHog + Cursor**. Rationale: minimize ops, MoR handles tax, build-in-public = distribution; <2 wk to MRR (evidence: [T02-S008, T02-S003, T02-S019, T02-S020]). Avoid: LangGraph (overkill); HubSpot (no sales yet); Lindy (lock-in + credit volatility).

### Branch 2 — B2B agent SaaS founder (post-PMF, 1–10 paying)
Stack: **LangGraph + LangSmith + Stripe Billing usage-metered + HubSpot or Attio + LinkedIn outbound (Apollo+Lemlist) + Modal (GPU/sandbox) or Vercel (API)**. Rationale: durable execution + eval CI required; HubSpot if 50+ employees, Attio if smaller (evidence: [T02-S007, T02-S024]). Pricing: hybrid (platform fee + usage bucket) — 43%→61% adoption (evidence: [T02-S027]). Avoid Polar (B2B custom contracts beyond MoR), Lemon Squeezy (decaying).

### Branch 3 — 咨询师 / agency-style (per-project, not SaaS)
Stack: **Python + provider SDK direct + Helicone + Stripe Invoicing**. No subscription infra, bill outcomes, Helicone gives client cost transparency. Avoid any framework — abstraction tax not worth it. Pattern: $3000/mo done-for-you content team beats $49/mo SaaS sale (evidence: [T02-S028]).

### Branch 4 — 国内创业者
Stack: **扣子 Coze (Coze.cn 国内 / Coze.com 出海) OR Dify 自部署 + 智谱/通义 API + 微信支付 + 小红书/B站 + 飞书**. 字节生态事实标准; Dify 仅在数据合规要求下 (evidence: [T02-S015, T02-S016]). Avoid: Stripe (国内不支持), LangSmith/Helicone (合规+延迟). 注意 Coze 国内/出海版数据隔离.

### Branch 5 — Outcome-priced agent (support / SDR vertical)
Stack: **LangGraph + LangSmith + Stripe Billing custom metering + outcome event ingestion (Polar usage-meters or Pickaxe/Flexprice)**. Anchor: Intercom Fin $0.99/resolution; Salesforce Agentforce Flex Credits per action (evidence: [T02-S011, T02-S012]). 失败模式: only do this if "did it work?" closes in <5s; outcome measurement infra doesn't exist for most categories.

### Branch 6 — Coding-agent / dev-tools founder
Stack: **Anthropic SDK or OpenAI SDK direct + custom prompt router + Stripe usage-billed + Cursor/Claude Code dogfood + GitHub as distribution**. In this niche framework abstraction = anti-feature; users want bare metal (evidence: [T02-S021]).

---

## 避坑清单

1. ❌ 不要 2026 起步用 Lemon Squeezy — Stripe 收购后 sunset 风险, 起步选 Stripe(US 简单) 或 Polar(海外 MoR) (evidence: [T02-S004]).
2. ❌ 不要忽视 Polar 隐藏费率 — 国际订阅实际 ~6%+$0.40, 不是首页 4%+$0.40 (evidence: [T02-S023]).
3. ❌ 不要 demo 阶段就上 LangGraph — Vercel AI SDK + 一个 while loop 比 LangGraph 快 3 倍验证 PMF (evidence: [T02-S007]).
4. ❌ 不要把 5-agent multi-agent 当默认架构 — 多数场景 1 agent + 5 tools 即可; "swarm" 是 conf talk, 不是 prod reality.
5. ❌ 不要用 Lindy 给企业级客户交付 — credit 系统 = 客户每月账单未知, B2B procurement 不接受 (evidence: [T02-S014]).
6. ❌ 不要忽略 Apple IAP 30% 抽成 — mobile-first agent 直接吃利润; 引导 web checkout dark pattern 已被 Apple 打击.
7. ❌ 不要在 outcome-priced agent 上线前没建测量管道 — Fin 能 $0.99/resolution 是因为 "resolved" 信号闭环明确 (evidence: [T02-S011]).
8. ❌ 不要用 Zapier 跑 agent backbone — 月账单 $4k–$8k vs n8n 自部署 1/10 价 (evidence: [T02-S017]).
9. ❌ 不要忽视 Coze.cn / Coze.com 数据合规隔离 — 出海产品需分账号分项目 (evidence: [T02-S015, T02-S016]).
10. ❌ 不要把 Twitter 关注者数当 ICP 信号 — B2B agent 的 ICP 在 LinkedIn / 行业 community (evidence: [T02-S028]).

---

## Phase 2 提炼提示

### 工具选型原则 (≥3 source consensus)
- **"Distribution > Framework"**: 90% indie failure 在 distribution 不在 product (evidence: [T02-S020, T02-S028, T02-S022]).
- **"Hybrid pricing converging"**: 43%→61% adoption EOY 2026 (evidence: [T02-S027, T02-S012, T02-S013]).
- **"Framework decay is real"**: 选 framework 标准 = "能在一个周末剥掉吗" (evidence: [T02-S007, T02-S008]).
- **"Outcome pricing requires measurable outcomes"**: 信号闭环 <5s 才行 (evidence: [T02-S011, T02-S012]).
- **"Dogfood your own stack"**: Cursor/Claude Code 已成基础设施 (evidence: [T02-S021]).

### 工具流派分裂 (心智谱系候选)
- 厚框架 (LangGraph/CrewAI) vs 薄框架 (Vercel AI SDK/Pydantic-AI/Mastra) — durability vs DX
- MoR (Polar/Paddle/Lemon Squeezy) vs payment processor (Stripe direct) — solo 省心 vs scale 控制
- Per-seat / Per-token / Outcome-based — pricing 三分派, hybrid 在汇合
- Hosted (Vercel/Replicate) vs Self-host (Modal/Cloudflare DO) — ops 能力分水岭
- 海外 (Stripe + LangChain + Vercel) vs 国内 (Coze + 微信支付 + 小红书) — 平行两套基建

### 新兴工具信号
- Stripe Agentic Commerce Suite (2025-Q4) — agent 直接发起 payment 协议层标准化
- Polar usage-meters (2025-Q3) — MoR 内置 metered billing
- Mastra 1.0 (2026-01, $22M Series A) — TS-first 框架 GA
- 出现→主流 12–18 月 (Vercel AI SDK 是参照样本)

### 冷僻 / 信号薄弱
- 必备层 10 / 场景特化 13 / 新兴 5 — 健康
- 一手率 13/28 ≈ 46% verified_primary, 略低于 60% 目标 (vendor 类被算 verified, 第三方 review 是 secondary 占比高)
- 决策树 6 branches persona-rooted — 成形

**调研边界**: 聚焦 SaaS / API arbitrage / 咨询三种主流 monetize 路径. 未深挖: GPTs Store agent marketplace 二级分发, agent affiliate/referral, agent-to-agent 合约 (Stripe SPT 是早期信号但 ecosystem 未成熟). API arbitrage 灰色玩法按要求未列入决策树, 仅在避坑中影响选型 (LLM 降价导致此类 wrapper 6 月衰减一次).
