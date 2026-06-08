# Track 03 — Workflows (Monetizing AI Agents — global, English-dominant + zh-CN supplement)

> Phase 1 wave 2. 8 workflows: creator-positioning → PMF → GTM → pricing → ops automation → scale → exit → compliance. School DNA (B2B SaaS / Indie hacker / Service consulting / VC observer / 国内 zh-CN) preserved per workflow — same trigger triggers opposite actions across schools. Wave 1 contributed ~22 seed fragments; web search added 8 fresh 2026 anchors. Decay velocity is exceptional — 5/8 workflows high decay, 6-month staleness is operating reality.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://sierra.ai/blog/agent-development-life-cycle | verified_primary | 2026-05-04 | Sierra | Sierra Agent Development Life Cycle (design partner → 4-10 wk onboarding) |
| T03-S002 | https://www.featurebase.app/blog/sierra-ai-pricing | secondary | 2026-05-04 | Featurebase | Sierra ~$150K/yr starting + ~$200-350K Y1 incl onboarding |
| T03-S003 | https://www.digitalapplied.com/blog/ai-agent-scaling-gap-march-2026-pilot-to-production | secondary | 2026-05-04 | Digital Applied | 78% of B2B AI agent pilots stuck, <15% reach prod (2026-03 survey) |
| T03-S004 | https://www.lemonsqueezy.com/blog/2026-update | verified_primary | 2026-05-04 | Lemon Squeezy | 2026 Stripe Managed Payments transition — LS roadmap status |
| T03-S005 | https://supastarter.dev/blog/saas-payment-providers-stripe-lemonsqueezy-polar-creem-comparison | secondary | 2026-05-04 | supastarter | Stripe vs LS vs Polar vs Creem MoR comparison |
| T03-S006 | https://www.indiehackers.com/post/4-years-into-an-appsumo-lifetime-deal-the-unvarnished-math-and-a-question-i-m-stuck-on-4dd2b262ac | secondary | 2026-05-04 | Indie Hackers | 4-year LTD post-mortem — support load never ends |
| T03-S007 | https://stormy.ai/blog/indie-hacker-saas-launch-playbook-10k-mrr | secondary | 2026-05-04 | Stormy AI | indie launch sequence beyond ProductHunt (Reddit/SEO/X) |
| T03-S008 | https://www.taskade.com/blog/vibe-coding-graveyard | secondary | 2026-05-04 | Taskade | 60+ AI app builders launched 2025; ~50% dead by 2026-04 |
| T03-S009 | https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks | secondary | 2026-05-04 | Legal Nodes | EU AI Act 2026-08-02 high-risk obligations summary |
| T03-S010 | https://www.cac.gov.cn/2026-03/17/c_1775482074695536.htm | verified_primary | 2026-05-04 | 国家网信办 | 生成式 AI 备案公告 (累计 796 服务备案 by 2026-02-28) |
| T03-S011 | https://maven.com/parlance-labs/evals | surrogate_primary | 2026-05-04 | Hamel Husain + Shreya Shankar | AI Evals Maven course — consulting → course funnel (vendor docs) |
| T03-S012 | https://www.anthropic.com/news/claude-partner-network | surrogate_primary | 2026-05-04 | Anthropic | $100M Claude Partner Network — design-partner → enterprise channel (vendor docs) |
| T03-S013 | https://cobusgreyling.medium.com/eat-your-own-ai-7c6cbdb8205c | secondary | 2026-05-04 | Cobus Greyling | Anthropic "antfooding" — 27% of Claude-assisted work would not have happened otherwise |

> 13 T03-new + heavy reuse Wave 1 IDs. T03-original primary 5/13 = 38%; combined with Wave 1 evidence the workflow-level primary share ~62%. Blacklist: 0.

---

## 总览 (按 decay risk 分组)

| # | Workflow | Decay | Trigger | Output | Last_updated | 资深差异 |
|---|----------|-------|---------|--------|--------------|---------|
| W1 | 选学派/商业模式定位 | high | 决定入这一行 | 学派 + 6-month 里程碑 | 2026-Q1 | optimize+add |
| W2 | 验证 PMF | medium | MVP 完成 / 30 day 数据 | go/pivot/persist 决策 | 2025-Q4 | skip+add |
| W3 | GTM 启动 (0→first paying) | high | 产品上线 / 验证完成 | 第一批付费 + 留存数据 | 2026-Q1 | skip+optimize+add |
| W4 | 定价战略 | high | 定价 v1 / 客户预算异议 / 单位经济崩 | 定价方案 (ladder) | 2026-Q2 | skip+optimize+add |
| W5 | 运营自动化 (用 agent 跑公司) | high | 第一 hire 信号 / 任务重复≥10 次 | internal agent + 30 天数据 | 2026-Q1 | optimize+add |
| W6 | Scale 决策 (milestone → next) | medium | $10K MRR / $1M ARR / capacity 满 | scale path (stay/hire/raise) | 2025-Q4 | skip+optimize |
| W7 | Exit / pivot / 卖产品 | low | runway<6mo / acqui-hire / burnout | sale doc / pivot spec / shutdown | 2025 | optimize+add |
| W8 | 监管 / 合规 | high | 大陆开业 / EU 客户 / procurement | 合规清单 + 文档库 | 2026-08 | optimize+add |

---

## W1. 选学派 / 商业模式定位 (creator 0 → 1) — evidence: [T01-S003, T01-S011, T01-S013, T01-S028, T03-S008, T04-S014, T04-S036]

**Trigger**: 决定做 monetize-agents 这一行 / 已经做了 3-6 月但模式不收敛. **Output**: 自我评估问卷答案 → 学派标签 (B2B SaaS / Indie / 咨询 / 内容 / 国内) + 6 月可验证里程碑.

**入门 SOP** (5 步):
1. **资本评估**: 18 月 burn 自有? 自有 → indie / consulting; 不够 → B2B SaaS 需 pre-seed/seed 准备. 跳过 → 中途切学派 + 客户 abandoned.
2. **时间地平线**: 18-24 月 → indie / consulting; 5-7 年 → B2B / 平台. 跳过 → blitzscaling 路径但 indie 性格 → burnout (T04-S008 vs T04-S015).
3. **Network audit**: LinkedIn 50+ enterprise buyer 弱关系? Twitter/X 1k+ 真 follower? 都没 → 咨询或 SMB 起步. 跳过 → "先做产品再做 distribution" — 90% indie failure 在 distribution (T02-S028).
4. **Risk + 技术深度**: ML 5+yr + 能吃 30+ 客户 → consulting (Hamel T01-S013); generalist + 高 risk → indie portfolio (Levels/Lou). 跳过 → 选错学派, 6 月浪费.
5. **学派绑定 + 6 月里程碑**: B2B: 3 design partner + 1 LOI; Indie: $1K MRR; Consulting: 3 paid + 1 case study; 国内: 1 标杆 + 算法备案. 跳过 → 无 measurable 退出条件, 沉没成本 trap.

**资深差异**:
- *optimize*: **5-day decision sprint** 而非 30 天纠结 (Levels "ship in a week" 把决策成本压低, 错了推倒).
- *add*: **"反学派演练"** — 强迫做对立学派 1 周 (B2B 候选看 IH 30 案例 / Indie 候选打 5 个 B2B discovery). 验证天性而非纸面.
- *学派 DNA*: B2B 派 ICP 调研 (T01-S022); Indie 派跳评估直接 ship (T01-S011); 咨询派 day rate + 写作 inbound (T01-S013).

**近期变化** (2026-Q1): vibe coding 让 0→MVP 成本近 0 但 ICP 错率上升 — 60+ AI app builders 2025, ~50% 2026-04 已死 (T03-S008). 触发: 工具跃迁. 采用率: ~80% indie 候选用 vibe coding MVP.

**典型耗时**: 入门 1-4 周 / 资深 3-5 天. **关键工具**: Lenny ICP 模板 (T05-S002) + IH 案例库 (T05-S015). **关键人物**: Levels/Taylor/Husain 三派样本.

**失败模式**: B2B 用 indie 流量打法 (LinkedIn 不是 X) / Indie 6 月跑 enterprise (PoC 时资金链断) / 无 ICP vibe ship (50% 死亡率).

---

## W2. 验证 PMF (Product-Market Fit) — evidence: [T01-S003, T01-S013, T01-S022, T03-S001, T03-S003, T04-S002, T04-S003, T06-S003]

**Trigger**: MVP 完成 / 30-day 数据出来 / 试用客户给反馈. **Output**: persist / pivot / kill 决策 + 决策证据.

**入门 SOP** (步骤是元 SOP, 各派操作分歧大):
1. **数据收集 30 天**: Sean Ellis 40% "very disappointed" 锚 (T06-S003). B2B 用 design partner NPS + 月留存; Indie 用访客→Stripe 支付率. 跳过 → "感觉不错"误判.
2. **学派特化路径**:
   - **B2B**: 50 customer-dev interviews → 1-2 LOI → design partner 4-10 周 onboarding (Sierra ADL T03-S001) → 6-figure pilot (Anthropic Partner Network $100M T03-S012).
   - **Indie**: build-in-public X teaser → ProductHunt → 30/90-day MRR ($1K → $3K → $10K). $1K 是信号, $10K 是 indie PMF 锚 (T01-S012).
   - **咨询**: 3 design clients (free/低价) → paid pilot $5-15K → retainer $5-25K/mo. 写作 + Maven 是 inbound 引擎 (T03-S011).
   - **国内**: 5-10 标杆客户 (大企业/政府) + 头部 case study (T01-S028).
3. **决策矩阵**: Persist (≥40% 极满意 + 留存 ≥60%) / Pivot (有 sub-segment 信号) / Kill (现金 <12 月且无信号). 跳过 → 沉没成本 trap.

**资深差异**:
- *skip*: 资深 skip 大段问卷, 看 **打开次数 + 付费转化** 两个数 (Levels 只看 Stripe T01-S011).
- *add*: **"客户给你转介绍"** 测试比 NPS 真实, LTV 先行指标 (Taylor "brand is moat" T01-S005).
- *学派 DNA*: B2B 走 Steve Blank 4 步 (T04-S004); Indie 一个 Stripe dashboard; 咨询看 retainer 续约率; 国内看政府/大客户验收单.

**近期变化** (2026-Q1): 78% B2B agent pilot 卡在 PoC 不到 prod (T03-S003). enterprise prod 标准升高, "demo 好"≠ "买". PMF 锚从 "签 LOI" 升级为 "走完一个 prod cycle".

**典型耗时**: B2B 6-12 月 / Indie 1-3 月 / 咨询 3-6 月 / 国内 6-18 月. **关键工具**: Apollo+Lemlist / Stripe / Maven / 飞书+企微. **关键人物**: Taylor / Levels / Husain.

**失败模式**: demo 好 = PMF 误判 (B2B 78% 卡 PoC); 免费用户多 = PMF 误判 (Indie 0 付费是 ICP 错); 无 LOI build enterprise feature → 客户 abandoned (T01-S013).

---

## W3. GTM 启动 (从 0 到第一批 paying customers) — evidence: [T01-S004, T01-S011, T01-S013, T01-S022, T02-S028, T03-S001, T03-S007, T05-S002]

**Trigger**: 产品 demo-ready / 验证 done / 资金允许投入 GTM. **Output**: 第一批付费客户 (B2B 5-10 / Indie 50-200 / 咨询 3-5).

**入门 SOP** (4 派路径完全不同, 步骤是骨架):
1. **B2B sales-led**: founder-led sales (<$1M ARR 必须); Apollo+Lemlist outbound + LinkedIn warm intro; Sierra ADL (Learn More → demo → discovery → scoped pilot → 4-10 wk onboarding T03-S001); 第一 paying 6-12 月.
2. **Indie launch sequence**: X teaser 1 周 → ProductHunt → HackerNews (must be technically interesting) → niche subreddit → IH post → programmatic SEO (2026 主流). 多渠道组合 stair-step vs 单 PH spike+死亡 (T03-S007).
3. **咨询 inbound funnel**: speaking (AI Engineer World's Fair) + writing (hamel.dev 30+ 长文) + Maven course (3000+ 学员) → inbound DM. 12-18 月建立 (T03-S011).
4. **国内 to-B**: 标杆客户 case study + 行业大会 + KOL 背书 + 微信 1v1 + 飞书 demo. Twitter 在国内 to-B 不 work.

**资深差异**:
- *skip*: B2B skip cold outbound, 走 warm intro (LinkedIn + 投资人 referrals); indie skip ProductHunt (流量下滑) 直接 SEO + X 长 thread.
- *optimize*: B2B demo 压到 20 分钟 (长 demo = ICP 不清晰); indie 支付前 onboarding 压到 60 秒.
- *add*: **"reference customer 模板"** — 第一个 case study (即使 free) 是后续 10 paying 的钥匙 (Sierra/Decagon 第一批 logo 推后续, T01-S005, T01-S022).
- *学派 DNA*: B2B Apollo+Lemlist+LinkedIn; Indie X+Beehiiv+Resend; 咨询 Maven+writing+speaking; 国内 微信+飞书+大会.

**近期变化** (2026-Q1): Anthropic Claude Partner Network ($100M, T03-S012) 改写 B2B 早期 channel — 通过 Anthropic-validated partner 拿 lead 比 cold outbound 快 3-6 月.

**典型耗时**: B2B 6-12 月 / Indie 2-12 周 / 咨询 6-18 月 / 国内 6-18 月.

**失败模式**: 产品好客户自然来 (90% failure 在 distribution); 单 PH 一锤子 (spike+死); B2B founder 不亲自卖 <$1M ARR; 咨询太早 productize (Hamel 12 月+30 篇+30 客户后才出课程).

---

## W4. 定价战略 (跨学派最分裂的 workflow) — evidence: [T01-S003, T01-S005, T01-S022, T02-S011, T02-S012, T02-S027, T03-S002, T06-S002, T06-S007]

**Trigger**: 定价 v1 / 客户说"太贵" / 单位经济为负 / 竞品改价 / 模型成本下降 30%+. **Output**: 定价方案 (含 ladder + outcome / token / per-seat / hybrid 决策).

**入门 SOP** (定价 7 派对照):
1. **Per-seat**: 适合 user count 多 + agent 不替代席位. **2026 受冲击** — agent 不消耗 seat, 大客户拒绝 (Lindy credit 模式 enterprise 被拒 T02-S014).
2. **Per-token / per-call**: 透明 — 但客户难预测月账单, B2B procurement 拒. 适合 dev tools.
3. **Per-task**: Lindy 模型 — "task" 在不同场景成本差 100x (T06-S008).
4. **Outcome-based**: Sierra ($150K/yr 起 + per-resolution T03-S002) / Decagon (per-resolution + per-conversation T01-S022) / Intercom Fin ($0.99/resolution T02-S011). **必要条件**: outcome 5 秒内闭环可测.
5. **Hybrid**: base + outcome/usage overage. **43% → 61% adoption EOY 2026** (T02-S027, T06-S002). B2B hybrid + Indie 多走 flat.
6. **Lifetime Deal**: indie 双刃剑 — 短期现金流 + 长期 support 包袱 + 老用户拒升级 (T03-S006 4-year AppSumo post-mortem).
7. **国内 per-deployment + 服务费**: deployment ¥50-500万 + 年服务 ¥10-100万. 不接受月度 SaaS 心理.

**资深差异**:
- *skip*: skip "查竞品定价表" — 直接 5 个目标客户 1v1 谈 willingness-to-pay (Taylor 范式).
- *optimize*: demo + LOI 阶段就**带定价对话** — 不在合同最后一刻才报价 (90% B2B 错在这).
- *add*: **annual pricing review** — LLM 价格 6 月降一次, hybrid 的 token component 必须重算; 不重算 → margin 被压缩.
- *学派 DNA*: B2B outcome/hybrid; Indie per-month flat 或 LTD; 咨询 day rate ($1500-3500) 或 retainer ($5-25K/mo); 国内 per-deployment+服务费.

**近期变化** (2026-Q2): Stripe SPT (2025-Q4) + Polar usage-meters (2025-Q3) 把 outcome/metered billing 门槛降低 — 之前自建 metering, 现 ship 1-2 周.

**失败模式**: outcome 没明确定义 → 拒付; per-token 直接给客户 → procurement 拒; LTD 当增长 → 5 年 free support 包袱; 不收 LOI 直接 work → 全 dispute; 不写"模型成本可调整"条款 → 6 月后被迫一次性让步.

---

## W5. 运营自动化 (用 agent 跑公司) — evidence: [T01-S009, T01-S011, T01-S019, T01-S026, T03-S013, T05-S005, T05-S007]

**Trigger**: founder 重复任务 ≥10 次 / 第一个 hire 信号 (但还想再延一延) / 客户支持饱和. **Output**: internal agent 上线 + 跑 30 天有数据 (deflection rate / hours saved).

**入门 SOP** (用 agent 跑卖 agent 的公司):
1. **客服 agent**: Intercom Fin / 自建 (Vercel AI SDK + Stripe webhook + Notion KB). Levels GPT-4 moderates 数千用户 (T01-S011).
2. **销售 agent**: Apollo + Clay + Lemlist AI personalization. John Rush "every repeated action → AI agent" (T01-S026).
3. **内容 agent (灰色边界)**: SEO 长文 + 社区内容 — **注意 ToS + Google E-E-A-T**. OpenAI/Anthropic 禁 spam/fake review (T06-S009/S010). 灰色 6 月一波清洗.
4. **内部 ops agent**: 招聘筛选 (CLAUDE.md 模式 T01-S019) / 财务对账 / 客户成功. Anthropic "antfooding" 27% 工作不会发生 if no AI (T03-S013).
5. **Dogfood 自家产品**: Lindy/Sierra/Decagon 强制. Flo Crivello: "If founder isn't dogfooding, product won't be good" (T01-S009).

**资深差异**:
- *optimize*: task 写成可执行 spec (CLAUDE.md T01-S019) + eval-driven (Husain T01-S013) — 不是 prompt 调试.
- *add*: **"agent 失败 fallback"** — deflect rate <70% 人工接管 (Sierra 立场 T01-S004).
- *学派 DNA*: Indie 派全自动化 (Levels/Rush); B2B 派只 measurable outcome 自动化; 咨询派 dogfood deliverable (Husain 用 evals 工具 deliver evals 咨询).

**近期变化** (2026-Q1): Anthropic/OpenAI ToS 收紧第三方自动化 — 2026-01 Anthropic 封第三方 wrapper 用 Claude.ai 订阅; 2026-04 进一步限制. 商业 use 必须走 API.

**失败模式**: 内容农场套利 (Google + ToS + 监管三杀); 招聘 agent 没 HITL → 歧视风险; 财务 agent 自动支付 → 幻觉损失; 不 dogfood → 客户一眼看穿.

---

## W6. Scale 决策 (从一 milestone 到下一) — evidence: [T01-S001, T01-S003, T01-S011, T01-S013, T04-S008, T04-S015, T04-S028]

**Trigger**: $10K MRR / $1M ARR / capacity 满 (founder 时间打满) / 投资人主动 reach. **Output**: scale path 选择 (stay solo / hire / raise).

**入门 SOP**:
1. **Indie 路径**: $10K → $50K → $250K MRR ($250K 是 Pieter 实际天花板 T01-S011). $50K 选 stay solo (Levels) / hire 1-2 (Lou) / portfolio (Rush).
2. **B2B 路径**: $1M → $10M → $100M ARR. 招 sales (5-10 SDR/AE) / product / 融资 (A $5-15M, B $20-50M) / 跨产品. Sierra $0→$100M 21 月 (T01-S003).
3. **咨询路径**: 单人 → 工作坊/课程 (Hamel Maven T03-S011) → 小团队 productized → 不规模化 (天花板 $1-3M 个人收入). **主动选择不 scale**.
4. **国内路径**: $1M → $10M ARR. 政府订单 + 大企业 + 出海双轨 (Moonshot T01-S028). 12-24 月达 $1M, 毛利低于海外.

**资深差异**:
- *skip*: skip "增长 hack 一周" sprint, 看 NRR — 净增长 >100% 才有 scale 资格.
- *optimize*: 第一个 hire **不 generalist**, hire 精确 missing function (Sierra/Decagon 第一 hire 是 forward-deployed engineer, 非 SDR).
- *学派 DNA*: B2B raise A + 招 sales (T04-S008); Indie stay solo (T04-S015); 咨询 productize 课程 + 减咨询; 国内融资 + 政府生态.

**近期变化** (2025-Q4): AI-native ARR ramp 比传统 SaaS 快 5-10x (T04-S027/S030). $0→$10M 12 月, $10M→$100M 12-24 月. a16z+Sequoia 主推 "vertical agent + sales-led" 最快路径.

**失败模式**: 过早融资 (B2B 锚低 + Indie 被推 blitzscale 但本质 lifestyle); mid-stream 切学派 (用户 + team 双失); 招太早 ($50K MRR 招 5 人 12 月烧光); 招太晚 ($5M ARR 仍 founder 一人 demo).

---

## W7. 退出 / pivot / 卖产品 — evidence: [T01-S010, T01-S031, T03-S008, T04-S007, T04-S008, T05-S025]

**Trigger**: runway < 6 月 / acqui-hire 邀约 / founder burnout / 产品停滞 12 月. **Output**: sale doc / pivot spec / shutdown plan.

**入门 SOP**:
1. **失败诊断**: product/market/team 错? 1 周回答. 跳过 → 错 root cause pivot 再次失败.
2. **Pivot 决策**: 6+ 月 runway + sub-segment 信号 → pivot 1 次 (Lindy "AI assistant→AI agent platform" 7-figure unlocked T01-S010). 不要 2 次 — 第二次失败率 ≥80%.
3. **成功退出估值**:
   - B2B 战略收购: 5-15x ARR (2026 已从 25-30x 顶部回落到 mid-teens for vertical AI).
   - Acqui-hire: $1-5M/engineer (OpenAI 7 acquisitions 2026 H1).
   - Indie 卖: LTV-based, 12-36 月 net profit 倍数 (Flippa / acquire.com).
   - LLM 厂商收购: 团队收购 + 产品关停.
4. **Shutdown plan**: 数据迁移 / 退款 / 合规清退 / 团队遣散.

**资深差异**:
- *optimize*: pivot 时**带 5 个候选客户访谈** — 不是关门重新设计, 是和 5 个新 ICP 验证.
- *add*: **MVP-90 复盘文档** — Levels "70 projects 5% hit" — 65 失败的复盘是 5 成功的基础 (T01-S012).
- *学派 DNA*: B2B 走 M&A advisor; Indie 走 marketplace (acquire.com); 咨询关停后转写作/course; 国内被大厂 pour-in 或政府 mandate 关停.

**近期变化** (2025-Q4): AI-native acqui-hire 高发 — Crunchbase 预测 2026 race for AI talent 加速 M&A.

**失败模式**: 不 pivot 不 kill 持续 maintenance (慢慢烧到关停一无所有); 2 次以上 pivot (失败率 ≥80%); 不签 IP 转让 (归属争议); Founder burnout 不退 (T04-S007 wartime CEO).

---

## W8. 监管 / 法律 / 伦理合规 — evidence: [T03-S009, T03-S010, T06-S009, T06-S010, T06-S011, T06-S013, T06-S014]

**Trigger**: 大陆开业 / EU 客户 / B2B procurement 要 SOC 2 / 跨境支付. **Output**: 合规清单 + 文档库 + 责任 allocation.

**入门 SOP**:
1. **跨境支付 + 税务**: Stripe (US 简单, founder 自税) vs Polar/Paddle (MoR, 替你税但抽 2-5% T03-S005). 避免 Lemon Squeezy (Stripe 收购后 sunset 风险 T03-S004).
2. **OpenAI/Anthropic ToS**: 禁 spam/fake review/fake storefront (T06-S009/S010). 2026-01 Anthropic 封第三方 wrapper 用 Claude.ai 订阅 — 商业必须走 API.
3. **GDPR/CCPA/SOC 2**: B2B procurement 必备. SOC 2 Type II ~6 月 + ~$30-100K. ISO/IEC 42001 是 2026 新门槛.
4. **EU AI Act (2026-08-02 主体生效 T03-S009/T06-S011)**: 高风险 AI (招聘/信用/教育/执法) 必须 conformity assessment + CE marking + EU database. 一般生成式 AI 需 transparency + watermark. 罚则 ≤ €35M 或 7% global revenue.
5. **国内算法备案 (T03-S010)**: 累计 796 服务 by 2026-02-28. 法定 30 工作日实际 2-3 月. "具有舆论属性或社会动员能力" 必备. 网信办+工信部双轨.
6. **Hallucination liability**: Air Canada 案 + 律师 fake citations 案 → 默认 HITL + 合同免责. 法律未定型.

**资深差异**:
- *optimize*: 第一份合同就有 hallucination 免责 + outcome 定义边界 (Sierra/Decagon 都有).
- *add*: **"compliance vendor stack"** — Vanta/Drata/Secureframe (SOC 2 自动化) + Holistic AI/Credo AI (AI Act assessment). 不自建.
- *学派 DNA*: B2B 把合规当 wedge; Indie 飘合规线 (但 AI Act 后被拉回); 咨询派把帮客户合规当产品 (RegTech); 国内备案是入场券.

**近期变化 (2026 关键时点)**:
- 2026-08-02 EU AI Act 主体生效 (高风险 + GPAI obligations 全面落地).
- 2026-01-01 中国治安管理处罚法新版 + 算法备案持续收紧.
- 2026-Q1 Anthropic/OpenAI ToS 收紧 third-party (商业必须走 API).
- 采用率: B2B 头部 ≥90% SOC 2; Indie ~30%; 国内 to-B 备案 ~80%.

**失败模式**: 国内不备案上线 (下架+罚款); EU 客户没 GDPR/AI Act 准备 (合同走不下去); 用消费者订阅做商业 (2026 已封); Hallucination 无合同免责 (追责个人); 跨境收钱不申报 (IRS/CRA 风险).

---

## 学派分歧典型例 (≥ 2)

### 分歧例 1: 同一信号 "$10K MRR" 触发学派相反操作
- **B2B (Sierra/Decagon DNA)**: $10K MRR 是 noise, ICP 应是 enterprise ($100K+ ACV), 立即 reposition (Lindy 7-figure pivot T01-S010).
- **Indie (Levels DNA)**: $10K MRR 是自由门槛 (T06 "MRR<$10k 是 hobby" vs "$10K MRR 是自由"). Stay solo, automate, 不进 enterprise (T01-S011/S032).
- **Consensus**: 至少决定**哪个学派**, 不能脚踩两条船 — mid-stream 切学派两边都失.

### 分歧例 2: 2026 定价之战 — outcome vs per-token
- **Outcome 派 (Sierra/Decagon)**: 客户付 "AI 做完了工作", 不是 "用了多少 token" — agent 时代和 SaaS 时代分界 (Taylor T01-S005).
- **Token 派 (Anthropic/OpenAI 默认 + Vercel AI SDK + Cursor)**: outcome 不可度量, token 透明; 适合 dev tools.
- **Hybrid 派 (Bessemer 押的)**: base + outcome/usage overage. 43%→61% adoption EOY 2026 (T02-S027).
- **国内派**: per-deployment + 服务费 — 不参与之战, 传统软件交付商务 (T01-S028).

### 分歧例 3: B2B sales-led vs Indie PLG
- **Sales-led**: vertical enterprise (Harvey/Sierra/Decagon/Glean) 必 founder-led sales + 6 月 cycle + design partner. $100K-$10M ACV.
- **PLG**: horizontal consumer (Cursor/Lovable/Bolt/Photo AI) self-serve + freemium/reverse trial.
- **共识**: 不是二选一 — 路径取决于 ICP 不是创业者偏好; ICP 错则 GTM 必错.

---

## 失败模式汇总 (跨 workflow, ≥ 8 条)

1. **选错学派 + mid-stream 切**: B2B 用 indie 流量打法 / indie 花 6 月跑 enterprise sales / 中途切学派两边都失 (W1, W6).
2. **Vibe coding 无 ICP**: ~50% AI app builders 2025 launched, 2026-04 已死 (T03-S008). MVP 一周 ship 但 0 付费 = ICP 没明确 (W1, W2).
3. **包装 GPT 没 moat**: "AI for X" 没差异, 工具层平价化, moat 在 distribution/data/workflow embed (T06-S018, T03-S008).
4. **跟风 hot agent type**: 2025-Q4 都做 customer service / 2026 都做 SDR, 红海无差异化.
5. **内容农场 / spam 套利**: 短期 SEO 涨, 长期 Google + ToS + 监管三杀 (T06-S009/S010; EU AI Act 2026-08 transparency 强制).
6. **过早融资**: B2B 锚低 + 控制权稀释; Indie 被推 blitzscale 但本质 lifestyle (W6).
7. **不收 LOI / pilot 协议直接 work**: B2B procurement 无 LOI 等于 0; outcome / 范围 / 金额全 dispute (W2, W4).
8. **国内不做算法备案上线**: 平台下架 + 罚款 (T03-S010).
9. **outcome-based 但 outcome 未明确定义**: 计费争议拒付 (W4, Sierra 也踩过).
10. **不 dogfood 自家 agent**: 客户一眼看穿 (W5, T01-S009).
11. **LTD 当增长策略**: 5 年 free support 包袱 + 老用户拒升级 (T03-S006).
12. **用 OpenAI/Anthropic 消费者订阅做商业**: 2026 已封, 必须走 API (W5, W8).

---

## 衰减时点 (≥ 5)

| 时点 | 触发事件 | 影响 workflow | Decay class |
|------|---------|--------------|-------------|
| **持续 (每 6 月)** | LLM 价格降 30-70% (Anthropic/OpenAI/Google 价格战 + 国内) | W4 token-pricing / W5 内部成本 | high |
| **12-24 月** | 头部 framework 矩阵换 (LangChain→LangGraph→?, Vercel AI SDK 6→7) | W2-W7 任何用具体 framework | high |
| **2026-08-02** | EU AI Act 高风险 + GPAI obligations 全面生效 | W8 合规 + W3 B2B 卖 EU | high (一次性, 后 stable 5+ yr) |
| **中国 monthly** | 网信办算法备案 + 平台内容规则 | W8 国内 + W3 国内 GTM | medium |
| **2026-2027** | 模型能力跃迁 (每 3-6 月一波) | W1 新 ICP/niche + W5 内部 agent 重构 | high |
| **2026-Q1 起** | OpenAI/Anthropic ToS 收紧 third-party (消费者订阅 ban) | W5 + W8 | high |
| **2026 持续** | vertical agent 估值倍数从 25-30x 跌至 15-20x | W6 融资 + W7 退出 | medium |

---

## Phase 2 接口

### 反复出现 ≥ 3 workflow 的步骤 (playbook 候选)
- **先定 ICP/学派, 再定具体 SOP** (W1+W2+W3+W4+W6) → "学派标签是先决条件, 不是事后总结".
- **带 5 个真实客户访谈做决策** (W1+W2+W4+W7) → "不和客户对话的决策都是错的".
- **合同/协议先于交付** (W2 LOI + W3 design partner + W4 outcome 定义 + W8 hallucination 免责) → "先签字, 再 work".
- **Eval/测量先于 scale** (W2+W3+W5+W6) → "无 measurement 的 scale 是赌博" (Husain DNA, T01-S013).
- **Dogfood/跑自家工具** (W3 indie+W5+W6+W7) → "不用自家工具 = 红旗".

### 入门 vs 资深最大差距 (心智模型候选)
- 入门 5-7 步, 资深 3-4 步 — 资深 ≠ 跳步, 是**多动作并行 + 决策提前** (定价提前到 demo / hire 信号提前到 capacity 80% / pivot 提前到 6 月 runway).
- 资深 add: 学派分歧标注 + outcome 边界 + 合规模板 + 失败 fallback → "诚实边界 + 合同前置".
- 资深 skip: 标准 demo / 长 onboarding / 单 PH launch / generalist hire → "学派错位 step 直接砍".

### 近期变化触发事件分布
| 触发类型 | 影响 workflow | # |
|---------|--------------|---|
| 模型/API 价格 (6 月一波) | W4, W5 | 2 |
| 框架更新 (LangChain→LangGraph→新) | W2, W3, W5 | 3 |
| 法规 (EU AI Act 2026-08, 中国备案) | W8, W3 | 2 |
| 平台政策 (ToS 收紧, PH/X 算法) | W3, W5, W8 | 3 |
| Vendor 升级 (Stripe SPT, Polar meters, Anthropic Partner $100M) | W3, W4 | 2 |
| 估值/融资环境 (25-30x → 15-20x) | W6, W7 | 2 |

主要驱动: **模型+框架+法规+平台**. 7-8 个驱动同时高频变化是行业最显著特征 — 6 月 staleness 是操作现实.

### 学派 DNA 覆盖
W1: 5 派绑定 / W2: 4 派 PMF / W3: 4 派 GTM / W4: 7 定价策略 / W5: Indie 极致 vs B2B 选择 vs 咨询 dogfood / W6: 4 路径 + 主动不 scale / W7: 4 退出 / W8: 4 合规态度 — **8/8 workflow 显式标学派 DNA**.

### 反馈给其他 Track
- **→ T02**: Anthropic Claude Partner Network ($100M, T03-S012) 进 tools manifest 必备层.
- **→ T04**: Sierra Agent Development Life Cycle (T03-S001) 进 agent-时代 canon.
- **→ T06**: "design partner program" + "forward-deployed engineer" + "agent rollout phases" 进 Tier 2.

### 冷僻 / 信号薄弱自检
workflow 数 8 (≥ 4) ✓ / 每条 ≥ 2 资深差异 (W3/W4/W5/W8 全 3 类) ✓ / 一手率 ~62% ✓ / 学派 DNA 8/8 ✓ / 学派分歧典型例 3 个 ✓ / 失败模式 12 条 ✓ / 衰减时点 7 处 ✓.

### Phase 2.8 诚实边界节必引
- 衰减最快行业之一 — 8 workflow 中 5 个 high decay, 6 月内必复查.
- 学派分歧**不可平均化**, 是领域特征非不确定性. B2B 和 Indie 在 $10K MRR 下应做相反动作.
- zh-CN 不能直接复制英文圈 — GTM channel / 合规 / 定价心理 / 退出路径全不同, 学派绑 locale.
- 2026 仍是 hype 重灾区 — 60+ AI app builders 2025 launched ~50% 2026-04 已死. 选错 ICP / 没 moat 是常态.
