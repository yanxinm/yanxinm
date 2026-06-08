# Track 03 — Workflows(工作流 / SOP / Pipeline):风险投资 / 早期投资人(VC investor)

> Phase 1 wave 2 第 3 路 subagent 输出。Industry = Venture Capital practitioner(GP / Partner / Principal / Associate),locale = `global`(US 美元 / 国内美元 / RMB 三条路径),profile = `practitioner`。
>
> **本 track 特殊性**:VC 工作流要在**三个时间尺度**上画 —— ① 一个 GP 的一周 ② 一个 deal 从 inbound 到 close ③ 一个 fund 从 fundraising 到 exit 的 7-10 年生命周期。来源以 Wave 1 五个产出做 seed(figures 怎么干活 + tools 典型场景 + canon 描述的流程 + sources 的近期变化信号 + glossary 的「工作流变化触发」种子)。VC 工作流来源大量是作者裸域博客(avc.com / abovethecrowd.com / feld.com)、VC firm 官网、机构 newsletter —— `source_verifier.py classify` 一律判 `secondary`,本 manifest 照判不上抬(GLOBAL 行业红线)。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://avc.com/2009/03/the-vc-weekly-meeting/ | secondary | 2026-05-14 | Fred Wilson (USV) | AVC.com「The VC Weekly Meeting」— GP 一周节奏一手描述 |
| T03-S002 | https://abovethecrowd.com/2016/04/21/on-the-road-to-recap/ | secondary | 2026-05-14 | Bill Gurley (Benchmark) | Above the Crowd「On the Road to Recap」— 周期 + 估值纪律 |
| T03-S003 | https://www.feld.com/archives/2011/03/term-sheet-template.html | secondary | 2026-05-14 | Brad Feld (feld.com) | Feld term sheet 系列 — term sheet 谈判流程一手 |
| T03-S004 | https://www.nfx.com/post/70-percent-vc-data | verified_primary | 2026-05-14 | NFX | NFX 自有研究 — 70%+ top deals 来自既有网络(sourcing) |
| T03-S005 | https://reactionwheel.net/2015/06/the-jobs-to-be-done-of-venture-capital.html | secondary | 2026-05-14 | Jerry Neumann (reactionwheel.net) | 「Jobs-to-be-done of VC」— portfolio construction math |
| T03-S006 | https://www.bothsidesofthetable.com/ | secondary | 2026-05-14 | Mark Suster (Upfront) | Both Sides of the Table — operator-turned-VC,deal / fundraising 流程长博客 |
| T03-S007 | https://www.ycombinator.com/library | surrogate_primary | 2026-05-14 | Y Combinator | YC Startup Library — vendor docs / acceleration 派 batch + Demo Day 机制 |
| T03-S008 | https://www.sequoiacap.com/article/pitching-your-business/ | secondary | 2026-05-14 | Sequoia Capital | Sequoia「Writing a Business Plan / Pitch」— pitch 评估视角 |
| T03-S009 | https://a16z.com/the-only-thing-that-matters/ | secondary | 2026-05-14 | Andreessen Horowitz / Marc Andreessen | a16z memo「Product/Market Fit」— 尽调判断核心 |
| T03-S010 | https://carta.com/learn/private-funds/management/fund-performance/ | surrogate_primary | 2026-05-14 | Carta Inc. | vendor docs — 基金运营 / NAV / DPI / capital call 流程一手 |
| T03-S011 | https://review.firstround.com/the-power-law-and-other-explanations-for-startup-success/ | secondary | 2026-05-14 | First Round Review | power law 长文 — portfolio / reserve 逻辑科普 |
| T03-S012 | https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone | verified_primary | 2026-05-14 | Acquired Podcast | Doug Leone 长访谈 — Sequoia 合伙人决策机制 / IC 文化 |
| T03-S013 | https://www.ycombinator.com/about | surrogate_primary | 2026-05-14 | Y Combinator | vendor docs — YC batch / Demo Day 官方机制说明 |
| T03-S014 | https://news.pedaily.cn | secondary | 2026-05-14 | 投资界(清科) | 国内创投门户 — RMB 募资 / 退出 / 回购潮的行业语境 |
| T03-S015 | https://www.chinaventure.com.cn | secondary | 2026-05-14 | 投中信息 ChinaVenture | 国内 LP-GP 数据 + RMB 基金募资 / 退出节奏 |
| T03-S016 | https://greylock.com/reid-hoffman/reid-hoffman-bear-market-blitzscaling/ | secondary | 2026-05-14 | Reid Hoffman (Greylock) | Greymatter「Bear Market Blitzscaling」— 下行期投后节奏 |
| T03-S017 | https://glasswing.vc | secondary | 2026-05-14 | Glasswing Ventures | 基金官网 — AI-native sourcing 平台 EVE 对外说明 |
| T03-S018 | https://www.20vc.com/ | secondary | 2026-05-14 | Harry Stebbings (20VC) | GP 访谈 podcast — 一行人如何自我描述 deal / fund 流程 |

> **黑名单已规避**:知乎 / 公众号 / 百度百科 / CSDN / Quora / LinkedIn 文章正文一律未收入。国内工作流深度内容主要在公众号 + 闭门会(黑名单 URL),manifest 国内侧只能用可追溯门户(投资界 / 投中)作语境,**国内一手深度结构性偏薄**,见文末诚实信号。

---

## 总览(按 decay risk 分组)

### High decay(12-month-class)— 1 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W4. Deal sourcing — 建 proprietary deal flow | 贯穿性,新基金部署期 / 进新 thesis 时集中投入 | 一条专属高质量 deal 流 | 2026-05-14 | skip + optimize + add(3 类,3 处) |

### Medium decay — 4 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W1. 一个 GP / 投资人的一周 | 每个工作周开始,周一 partner meeting 锚点 | pipeline 推进 + IC 决议落地 + 投后跟到 | 2026-05-14 | skip + optimize + add(3 类,3 处) |
| W2. 一个 deal 从 inbound 到 close 的完整路径 | 一个 deal 进入视野(引荐 / inbound / outbound) | signed term sheet → 法律 close → 股权进 cap table | 2026-05-14 | skip + optimize + add(3 类,3 处) |
| W5. Due diligence 深做 | 一个 deal 在 first meeting 后判定「值得深看」 | 能在 IC 站住的尽调结论 + risk 清单 | 2026-05-14 | skip + optimize + add(3 类,3 处) |
| W7. 投后服务 / board service | 一个 deal close 之后,持续到退出 / write-off | winner 被识别加倍、loser 及时止损 | 2026-05-14 | skip + optimize + add(3 类,3 处) |

### Low decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W3. 一个 fund 从 fundraising 到 exit 的 7-10 年生命周期 | GP 决定募新基金(常在上一支部署 60-80% 时) | LP 拿回 distribution + 基金清算 + GP carry + track record | 2026-05-14 | skip + optimize + add(3 类,3 处) |
| W6. Term sheet 谈判 + 估值 | IC 通过一个 deal,决定出 term sheet | 双方签署的 term sheet | 2026-05-14 | skip + optimize + add(3 类,3 处) |
| W8. Portfolio construction + reserve 策略 | 新基金 close 后、部署期开始前 | 明确的组合计划(check size / 项目数 / ownership / reserve) | 2026-05-14 | skip + optimize + add(3 类,3 处) |

> 共 **8 个 workflow**。LP 关系 + 募新基金已并入 W3(fund 生命周期)的 fundraising 段 + W1(一周节奏)的 LP call 段,不单列第 9 个 —— 避免与 W3 重复。

---

### W1. 一个 GP / 投资人的一周(三尺度之「周」)

- **One-liner**:把一个早期 VC 的一周从「无序救火」变成「有节奏的并行流水线」—— deal review / pitch 会 / partner meeting / board meeting / LP & founder 触达 五条线同时滚动。
- **Trigger**:每个工作周的开始;周一 partner meeting 是大多数机构基金的固定锚点。(evidence: [T03-S001, T03-S018])
- **Output**:一周结束时 —— deal pipeline 各项推进一格、≥ 1 个 deal 进入或退出尽调、partner meeting 的 IC 决议落地、board / portfolio 公司本周该跟的跟到、deal flow「水龙头」没干。(evidence: [T03-S001])
- **入门 SOP(minimum viable steps)**:
  1. **周一 partner meeting / deal review 准备**:把上周 sourced 的 deal 整理进 CRM(Affinity),给每个 deal 标阶段 + 一句话推荐/否决意见,准备本周要 present 的 1-2 个 deal。
     - *跳过会发生什么*:partner meeting 上拿不出结构化材料,deal 被搁置一周,founder 那边凉掉(早期 deal 有竞速窗口)。
  2. **partner meeting 本身**:全 partnership 过一遍 active pipeline,对在谈 deal 做 go / no-go / 继续尽调 的集体判断,分配本周尽调任务。
     - *跳过会发生什么*:个人擅自推进 deal 到很晚才暴露给合伙人,IC 阶段被否,浪费自己和 founder 数周。
  3. **本周 pitch 会(first meetings)**:见 3-8 个新公司,每个 30-60 分钟,会后当天写下 gut read + next step(pass / 二次会 / 进尽调)。
     - *跳过会发生什么*:deal flow 漏斗顶端断供 —— sourcing 不是「攒着以后做」,停一周下周就空。
  4. **进行中 deal 的尽调动作**:对已进尽调的 deal 推进当周该做的一步(reference call / 产品试用 / 算 unit economics / 查 cap table)。
     - *跳过会发生什么*:deal 卡在尽调里不动,要么错过窗口、要么被迫在信息不全时拍板。
  5. **portfolio / board / LP 触达**:本周该开的 board meeting 开掉,portfolio 公司的求助回掉,有 LP call 的接掉。
     - *跳过会发生什么*:portfolio 公司危机信号被漏看(投后是 power-law winner 的保育期);LP 关系冷掉,下一支基金募资时没人接电话。
- **资深路径(差异点)**:
  - **skip**:资深 GP **跳过**对绝大多数 inbound deal 的「正式 first meeting」—— 用 30 秒 deck / 一段话邮件 + pattern match 直接 pass,只把 first meeting 的时间留给网络内强引荐或 thesis 命中项。理由:经验告诉他们冷 inbound 的命中率极低,first meeting 是最贵的资源。(evidence: [T03-S004, T03-S018])
  - **optimize**:资深人把「周一准备 + partner meeting」**优化**成「持续在 CRM 里维护 + 会上只讨论真有分歧的 deal」—— 不在会上逐个念 pipeline,而是异步更新、会议聚焦争议项,partner meeting 从 3 小时压到 1 小时。(evidence: [T03-S012, T03-S018])
  - **add**:资深 GP **额外做**两件初学者忽略的事 ——(a)固定留「无议程」时间做 thesis 思考 / 写作 / 行业深挖(Fred Wilson 的 AVC.com 本身就是这种产物);(b)主动经营「未来 deal flow」—— 每周固定见 N 个**不是为了投**的人(其他 GP、潜在 scout、portfolio 创始人的朋友),把网络当复利资产养。(evidence: [T03-S001, T03-S004])
- **近期变化(近 12 个月)**:
  - **2024–2025 起**,由 **2022-2024 寒冬未完全过去 + DPI 压力**触发:GP 一周里「portfolio triage / 危机处理 / 帮 portfolio 公司省钱续命」的时间占比上升,「看新 deal」的时间相对被挤压;board meeting 议题从「how to grow faster」转向「default alive 还是 default dead」。(evidence: [T03-S016], glossary T06 寒冬语境)
  - **2025 AI cycle 拐点**起:AI 赛道的 first meeting 密度回升且竞速窗口极短(热门 AI deal 从见面到 term sheet 可能 < 1 周),把一周节奏重新拉快 —— 但只在 AI / 少数热门赛道,其他赛道仍是寒冬慢节奏。(evidence: [T03-S018], sources T05 topic-heat)
  - 稳态部分:「周一 partner meeting + 全周 pitch + 投后触达」这个**骨架结构** 多年未变,变的是各段的时间配比。
- **典型耗时**:入门 SOP — 一个完整工作周(本就是「周」尺度);资深路径 — 同样一周,但有效产出更高(更少 first meeting、更聚焦的 partner meeting、多出 thesis 时间)。
- **关键工具(与 Track 02 关联)**:Affinity(deal pipeline + 关系触达节奏,必备)、Crunchbase(first meeting 前 30 秒背景核查,必备)、Notion / Coda(投资 memo + portfolio tracking,场景特化);国内:微信 + 自建表格替代 Affinity。
- **关键人物(与 Track 01 关联)**:Fred Wilson 在 AVC.com 长期写「VC 的一周 / partner meeting」节奏;Doug Leone 在 Acquired 长访谈中谈 Sequoia 的合伙人会议文化。
- **常见失败模式**:
  - **sourcing 漏斗断供**:某周忙投后 / 募资就完全不见新公司 —— 「Block 固定的 first-meeting 时段(如每周二、周四下午),哪怕只见 2 家也别归零;deal flow 是流量不是库存」。
  - **partner meeting 变成念清单**:全员逐个 deal 过一遍、无人异步准备 —— 「会前异步更新 CRM,会上只讨论有真实分歧的 deal,把 3 小时会压到 1 小时」。
  - **投后失明**:只顾看新 deal,portfolio 公司的现金跑道 / 关键人离职信号被漏看 —— 「每周固定 triage 一遍 portfolio 的 default-alive 状态,把要救的公司提前一个月发现,而不是等 founder 来报丧」。
- **来源**(≥ 3):
  - [secondary] Fred Wilson AVC.com「The VC Weekly Meeting」:https://avc.com/2009/03/the-vc-weekly-meeting/ — collected 2026-05-14 (evidence: [T03-S001])
  - [secondary] 20VC GP 访谈(一行人如何描述自己的一周 / partner meeting):https://www.20vc.com/ — collected 2026-05-14 (evidence: [T03-S018])
  - [verified_primary] Acquired — Doug Leone 长访谈(Sequoia 合伙人会议机制):https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone — collected 2026-05-14 (evidence: [T03-S012])
  - [secondary] Reid Hoffman「Bear Market Blitzscaling」(下行期一周里投后占比上升):https://greylock.com/reid-hoffman/reid-hoffman-bear-market-blitzscaling/ — collected 2026-05-14 (evidence: [T03-S016])
- **Last_updated**:2026-05-14(骨架稳态,时间配比近 12 个月有变)
- **Decay risk**:medium —— 骨架结构稳定,但「各段时间配比」随周期(寒冬 vs AI cycle)持续移动,12-24 个月会再变。

### W2. 一个 deal 从 inbound 到 close 的完整路径(三尺度之「一个 deal」)

- **One-liner**:把一家公司从「pipeline 里的一行」推到「钱打进对方账户、股权进 cap table」—— sourcing → first meeting → 尽调 → IC / partner 决策 → term sheet → 谈判 → close 的完整闭环。
- **Trigger**:一个 deal 进入视野 —— 引荐邮件 / 冷 inbound deck / 自己 outbound 找到的公司 / accelerator demo day。(evidence: [T03-S004])
- **Output**:签署的 term sheet → 签署的最终投资文件(股权 / SAFE / 可转债)→ 资金到账 → 股权登记进 cap table(海外多在 Carta);或在任一环节明确 pass。(evidence: [T03-S003])
- **入门 SOP(minimum viable steps)**:
  1. **Sourcing + 初筛**:deal 进来,30 秒做背景核查(谁投过 / 上一轮估值 / 创始人是谁),判断是否值得花一次 first meeting。
     - *跳过会发生什么*:把宝贵的 first meeting 时间浪费在明显不符合 thesis / stage / geo 的公司上,漏斗效率崩溃。
  2. **First meeting**:30-60 分钟见创始人,听 pitch,问 team / market / product / traction 四块,会后当天写 gut read + 决定 pass / 二次会 / 进尽调。
     - *跳过会发生什么*:仅靠 deck 投资 —— 看不到创始人本人,founder-market fit 这个早期最强信号直接丢失。
  3. **尽调(diligence)**:进尽调的 deal 做系统核查 —— founder reference call、产品试用 / demo、market sizing(TAM)、竞争格局、unit economics、cap table review、必要时法律。(详见 W5)
     - *跳过会发生什么*:在信息不全时拍板;早期 deal 也至少要做 reference call —— 跳过它最常踩「创始人人品 / co-founder 矛盾」的雷。
  4. **写投资 memo + IC / partner meeting**:把尽调结论写成结构化 memo(market / team / product / deal terms / risks / 为什么投),拿到投委会 / partner meeting 论证,拿 go / no-go。
     - *跳过会发生什么*:没有书面 memo,decision 靠会上口头印象;事后无法复盘「当初为什么投」,也过不了机构基金的流程合规。
  5. **出 term sheet + 谈判**:IC 通过后给 term sheet(估值 + 轮次结构 + 关键条款),与创始人 / 其他投资人谈判到双方签字。(详见 W6)
     - *跳过会发生什么*:口头承诺不算数,没有 signed term sheet 之前 deal 随时会黄(被别家抢、创始人变卦)。
  6. **法律文件 + close**:term sheet 签了之后律师起草最终文件(股权购买协议 / SAFE / 股东协议),双方签署,资金到账,股权进 cap table。
     - *跳过会发生什么*:signed term sheet 只是意向,不是有约束力的成交 —— 不走完法律 close,钱和股权都没真正过户。
- **资深路径(差异点)**:
  - **skip**:资深投资人对**网络内强引荐 + thesis 命中**的 deal,**跳过**「正式分阶段尽调」里的若干步,直接靠 pattern recognition 在 1-2 次会内给 term sheet（尤其 2025 热门 AI deal 的竞速行情);理由是早期信息本就稀薄,过度尽调反而错过窗口、且把 deal 让给手快的对手。**注意**:这是高风险捷径,只在「自己 thesis 极深 + 引荐源极可信」时用。(evidence: [T03-S004, T03-S018])
  - **optimize**:资深人把「first meeting → 决定」**优化**成 first meeting 当场就走「软 term」—— 不等走完全流程,先口头给估值区间锁住创始人,再倒回去补尽调和 IC;把 deal 的竞速顺序从「尽调完才报价」改成「先报价占位再尽调」。(evidence: [T03-S006, T03-S018])
  - **add**:资深人**额外做**两件初学者忽略的事 ——(a)绕开创始人给的「友好 reference」,自己从网络里找**独立**信源(off-list reference)做背调,这是最能区分新手与老手的尽调动作;(b)在出 term sheet 前先想清楚「这个 deal 在我的 portfolio construction 里占哪个格 / 留多少 reserve」(把 W2 和 W8 接起来),而不是孤立看单个 deal。(evidence: [T03-S005, T03-S011])
- **近期变化(近 12 个月)**:
  - **2025 AI cycle 起**,由热门 AI 赛道竞速触发:头部 AI deal 的「inbound → term sheet」周期被压缩到几天甚至更短,传统「数周分阶段尽调」在热门 deal 上被部分跳过 —— 但这只发生在 AI / 少数热门赛道,寒冬赛道的 deal 反而走得更慢、尽调更重、估值压更狠。**同一行业内 deal 节奏两极分化** 是当前最显著的变化。(evidence: [T03-S018], sources T05 topic-heat)
  - **AI 辅助尽调** 起势:用 LLM 工具做 market sizing 初稿、竞品扫描、deck 初筛打分,把 associate 的尽调时间从「全做」变成「机器做初稿 + 人核校」—— 但 judgment 仍在人,且工具碎片化(详见 W4 / W5)。(evidence: [T03-S017])
  - **国内路径分化**:国内 deal 的 close 阶段近年多了「回购条款谈判 + 创始人个人连带风险评估」这个新工作环节(2023-2024 回购诉讼潮触发),海外 deal 没有这一环。(evidence: [T03-S014], glossary T06「回购诉讼潮」种子)
- **典型耗时**:入门 SOP — 海外早期 deal 通常 4-12 周(sourcing 到 close);资深路径 / 热门 AI deal — 可压到 1-2 周甚至更短;寒冬慢节奏 deal — 可拖到 3-6 个月。
- **关键工具(与 Track 02 关联)**:Crunchbase / PitchBook(sourcing + 背景核查 + 可比交易,必备)、Affinity(deal 阶段跟踪,必备)、DocSend(inbound deck 信号,场景特化)、AlphaSense / Tegus / GLG(深尽调 expert call,场景特化)、Carta(close 后股权进 cap table,必备);国内:IT 桔子 / 烯牛 / 鲸准。
- **关键人物(与 Track 01 关联)**:Brad Feld《Venture Deals》逐条款讲 term sheet → close 流程;Mark Suster(Both Sides of the Table)从 operator-turned-VC 视角写 deal 全流程;Marc Andreessen 的 PMF memo 是尽调里「这家有没有 PMF」的判断锚。
- **常见失败模式**:
  - **太晚暴露给合伙人**:个人偷偷推 deal 到很晚才进 partner meeting,IC 阶段被否,白白浪费自己和 founder 数周 —— 「deal 一进尽调就在 partner meeting 上 floor 一次,早拿到合伙人的方向性反对,而不是把否决留到最后」。
  - **跳过独立 reference call**:只打创始人给的「友好 reference」 —— 「每个 deal 至少做 2-3 个 off-list(创始人没列)的独立背调,绕开 friendly reference 才能查出 co-founder 矛盾 / 人品问题」。
  - **口头承诺当成交**:以为创始人「答应了」就稳了,没有 signed term sheet 就停止竞争动作 —— 「在拿到对方签字的 term sheet 之前,deal 一律视为没成,继续保持紧迫感」。
  - **孤立看单个 deal**:不算这个 deal 在 portfolio 里的 ownership target / reserve 占位,投完才发现 check size 和组合不匹配 —— 「出 term sheet 前先回 W8 对一遍组合,确认这一笔的 check size + reserve 留法」。
- **来源**(≥ 3):
  - [verified_primary] NFX「70% of deals come from network」(sourcing 决定 deal 上限):https://www.nfx.com/post/70-percent-vc-data — collected 2026-05-14 (evidence: [T03-S004])
  - [secondary] Brad Feld feld.com term sheet 系列(term sheet → close 流程):https://www.feld.com/archives/2011/03/term-sheet-template.html — collected 2026-05-14 (evidence: [T03-S003])
  - [secondary] Mark Suster Both Sides of the Table(deal 全流程 operator 视角):https://www.bothsidesofthetable.com/ — collected 2026-05-14 (evidence: [T03-S006])
  - [secondary] 20VC(一行人如何描述 deal 流程 / 竞速):https://www.20vc.com/ — collected 2026-05-14 (evidence: [T03-S018])
- **Last_updated**:2026-05-14(骨架稳态,节奏 + AI 辅助 + 国内回购环节近 12 个月有变)
- **Decay risk**:medium —— 「sourcing → 尽调 → IC → term sheet → close」骨架是 VC 数十年的核心流程、不会消失,但「每段耗时 + AI 辅助渗透 + 国内条款环节」12-24 个月会持续变。

### W3. 一个 fund 从 fundraising 到 exit 的 7-10 年生命周期(三尺度之「一个 fund」)

- **One-liner**:把一支基金从「一份 PPM + 一个 thesis」走完整个 7-10+ 年生命:募资 → 部署期投出去 → 投后 + reserve 跟投 → 收获期退出 → 清算 + 给 LP 返钱(并以此业绩募下一支)。
- **Trigger**:GP 决定募一支新基金 —— 多发生在上一支基金部署到 60-80% 时(行业惯例:有 track record 可 show 才好募下一支)。(evidence: [T03-S010, T03-S015])
- **Output**:跑完后 —— LP 拿回 distribution(DPI)、基金清算、GP 拿到 carry(如有利润)、形成可用于募下一支基金的 track record。(evidence: [T03-S010])
- **入门 SOP(minimum viable steps)**:
  1. **Fundraising / 募资(第 0-2 年)**:写 thesis + PPM,见各类 LP(机构 / FoF / family office / endowment / 国资),路演 deck,谈 fund terms(2% 管理费 / 20% carry / GP commitment),first close → final close。
     - *跳过会发生什么*:没有 committed capital 就没有基金 —— 这一步是其余一切的前提;募不满会被迫缩小基金规模、打乱 portfolio construction。
  2. **Portfolio construction 定盘(募资后 / 部署前)**:用 fund size 反推 check size、目标项目数、ownership target、reserve 比例 —— 先把组合的数学画出来。(详见 W8)
     - *跳过会发生什么*:闷头投到一半发现 reserve 不够 / 项目数失控,winner 起飞却无钱 follow-on,基金回报结构性受损。
  3. **部署期 / investment period(第 1-4 年)**:按 W2 一个个 deal 投出去,把初始 check 部署完(行业惯例 investment period 3-4 年)。
     - *跳过会发生什么*:部署太慢会被 LP 质疑、错过周期;部署太快又会在单一时点过度集中风险。
  4. **投后 + reserve / follow-on(第 2-8 年,与部署期重叠)**:board service、帮 portfolio 公司招人 / 融下一轮 / 处理危机;对跑出来的 winner 用 reserve 加倍跟投。(详见 W7、W8)
     - *跳过会发生什么*:winner 在后续轮被稀释 / 没接住 pro-rata;loser 拖太久不止损 —— 两头都吃掉回报。
  5. **收获期 / 退出(第 5-10+ 年)**:推动 portfolio 公司走 IPO / 战略 M&A / secondary 出售,把账面价值(TVPI)变成真金白银(DPI);对明确失败的项目 write-off。(详见 W3 与退出相关的子流程)
     - *跳过会发生什么*:TVPI 再高,不退出就是「纸面富贵」—— LP 要的是 DPI,不退出 GP 也拿不到 carry。
  6. **清算 + LP 报告 + 募下一支**:基金到期清算,给 LP 季度 / 年度报告贯穿全程,用已实现业绩募下一支基金。
     - *跳过会发生什么*:LP 报告断档 / 不透明,直接断送下一支基金的募资;基金不清算则法律 / 税务一直拖着。
- **资深路径(差异点)**:
  - **skip**:有 track record 的资深 GP 在募资上**跳过**「广撒网见上百个陌生 LP」—— 直接回头找上一支基金的老 LP re-up,加少量新 LP,募资周期从 12-18 个月压到几个月。理由:LP 关系是复利资产,老 LP 的钱比新 LP 便宜(尽调成本低、信任已建立)。新 GP 没有这个捷径。(evidence: [T03-S015, T03-S010])
  - **optimize**:资深 GP 把「部署期」**优化**成更纪律化的节奏 —— 不在某个估值高点(如 2021)把基金一次性打光,刻意把部署摊到多个年份 / 多个市场环境,用 vintage diversification 对冲周期;Bill Gurley 的「估值纪律 / 不追泡沫」就是这种打法的代表。(evidence: [T03-S002])
  - **add**:资深 GP **额外做**两件初学者忽略的事 ——(a)从基金第 1 年就持续、主动地经营 LP 关系(定期 update、闭门会、让 LP 觉得「在场」),而不是等募下一支时才想起 LP;(b)主动管理 DPI 时点 —— 在收获期不是被动等 IPO,而是用 secondary sale 主动制造流动性给 LP 返钱(尤其寒冬 IPO 窗口关闭时)。(evidence: [T03-S010, T03-S015])
- **近期变化(近 12 个月)**:
  - **2022-2024 寒冬 + 2025**:由 **IPO / M&A 窗口收紧 + LP 钱少** 触发,「收获期」被整体拉长 —— 很多 2018-2021 vintage 的基金到了该退出的年限却退不出去,DPI 普遍偏低,LP 对 GP 的考核从 TVPI 转向 DPI;**secondary sale 从「补充手段」上升为主流流动性工具**。新基金募资周期普遍变长、规模缩水,部分 emerging GP 募不到下一支。(evidence: [T03-S015, T03-S002], sources T05 topic-heat)
  - **2025-2026 ILPA Reporting Template v2.0** 进入采用期:由行业标准更新触发,GP 给 LP 的季度报告 workflow 实际切换 —— 费用 / carry 披露颗粒度要求提升,fund admin 流程和工具配置要调整。(evidence: [T03-S010], glossary T06「ILPA v2.0」种子)
  - **国内 RMB 基金路径**:2023-09《私募投资基金监督管理条例》+ 中基协登记备案新办法,把「新基金设立 / 管理人登记 / 产品备案」流程整体变重,门槛和材料要求提高;同时 RMB 退出难、国资 LP 占比上升,「fundraising → 退出」整条链的假设与海外美元基金分化明显。(evidence: [T03-S014, T03-S015], glossary T06 国内法规种子)
- **典型耗时**:入门 SOP — 一支基金完整生命 7-10+ 年(本就是「fund」尺度,近年因退出难常拉到 12-15 年);资深路径 — 同样的年限,但募资段更短、退出段更主动。
- **关键工具(与 Track 02 关联)**:Carta fund admin(capital call / NAV / DPI / carry 计算 / LP portal,必备)、PitchBook(反查潜在 LP 的 commitment pattern,必备)、DocSend(发 LP update / fundraising deck 并看谁读了,场景特化)、Notion / Coda(portfolio tracking,场景特化);国内:本地有限合伙结构 + 券商托管 + 本地 fund admin(Carta fund admin 在国内不适用)。
- **关键人物(与 Track 01 关联)**:Scott Kupor《Secrets of Sand Hill Road》系统讲 fund lifecycle / J-curve / carry / LP-GP 机制;Bill Gurley「On the Road to Recap」讲周期与估值纪律对部署节奏的影响;Sebastian Mallaby《The Power Law》对不同 firm 制度与生命周期的对照。
- **常见失败模式**:
  - **在估值高点把基金打光**:2021 那种高点一次性部署完,后续 down round 把整支基金的回报打骨折 —— 「刻意把 investment period 摊到 3-4 年、跨多个市场环境部署,用 vintage diversification 对冲;别因为 FOMO 在单一高点 all-in」。
  - **reserve 不够、winner 接不住**:首轮投得太满 / 项目数太多,winner 起飞却没钱 follow-on —— 「募资后立刻定盘 portfolio construction,把 reserve 比例锁死(常见 40-60%),宁可初始少投几家」。
  - **平时不理 LP,募资时才找**:把 LP 当一次性 ATM,基金中段零沟通 —— 「从第 1 年起固定季度 update + 闭门会,把 LP 关系当复利养;老 LP re-up 是下一支基金最便宜的钱」。
  - **TVPI 高就躺平、不主动制造 DPI**:账面估值好看就不推退出,LP 拿不到现金 —— 「收获期主动用 secondary sale 制造流动性给 LP 返钱,别被动等 IPO 窗口;LP 考核的是 DPI 不是 TVPI」。
- **来源**(≥ 3):
  - [surrogate_primary] Carta「Fund performance」vendor docs(capital call / NAV / DPI / 基金运营流程):https://carta.com/learn/private-funds/management/fund-performance/ — collected 2026-05-14 (evidence: [T03-S010])
  - [secondary] Bill Gurley「On the Road to Recap」(周期 / 估值纪律 / 部署节奏):https://abovethecrowd.com/2016/04/21/on-the-road-to-recap/ — collected 2026-05-14 (evidence: [T03-S002])
  - [secondary] 投中信息 ChinaVenture(国内 LP-GP / RMB 募资 + 退出节奏):https://www.chinaventure.com.cn — collected 2026-05-14 (evidence: [T03-S015])
  - [secondary] 投资界(清科)(国内创投门户 — RMB 募资 / 退出 / 回购语境):https://news.pedaily.cn — collected 2026-05-14 (evidence: [T03-S014])
- **Last_updated**:2026-05-14(7-10 年骨架是行业稳态;退出周期拉长 + ILPA v2.0 + 国内法规是近 12-24 个月的变化)
- **Decay risk**:low —— 「募资 → 部署 → 投后 → 退出 → 清算」是基金结构本身决定的、数十年稳态;变化的是各段时长与外部环境,不是骨架。标 low 是 iter 8 finding 的合法稳态填法。

### W4. Deal sourcing — 建 proprietary deal flow

- **One-liner**:把「被动等 inbound deck」升级成「主动、有结构、有专属性的 deal flow 机器」—— 因为 70%+ 的 top deal 来自既有网络,sourcing 决定一支基金的回报上限。
- **Trigger**:贯穿性 —— 从入行第一天到 GP 退休都在做;集中投入发生在新基金的部署期初期、或进入新 thesis / 新赛道时。(evidence: [T03-S004])
- **Output**:一条**专属(proprietary)**的高质量 deal 流 —— 强引荐为主、冷 inbound 为辅,且在你的 thesis 命中赛道里你能比别家更早看到好公司。(evidence: [T03-S004, T03-S005])
- **入门 SOP(minimum viable steps)**:
  1. **建多渠道入口**:打通 inbound(让人能找到你 —— 公开邮箱 / Twitter / firm 网站)+ outbound(主动按 thesis 扫公司)+ 引荐网络(其他 GP、portfolio 创始人、accelerator)。
     - *跳过会发生什么*:只靠单一渠道(如只等 inbound),deal flow 质量和数量都受制于人,漏斗顶端不可控。
  2. **持续撒网见人**:每周固定见 N 个公司 + N 个「非为投资」的人(其他投资人、潜在 scout、行业人),把网络当资产养。
     - *跳过会发生什么*:网络是衰减资产,停止经营 6-12 个月引荐就枯;「攒着以后做」对 sourcing 无效。
  3. **初筛 + pattern match**:对进来的 deal 用 thesis / stage / geo 做快速过滤,30 秒-2 分钟判断「值不值得一次 first meeting」。
     - *跳过会发生什么*:不筛就全见,first meeting 时间被低质 deal 吃光,真正该深看的 deal 没时间。
  4. **录入 + 跟踪 + 复盘**:所有接触过的 deal 录进 CRM(Affinity),标来源渠道;定期复盘「哪个渠道给的 deal 命中率最高」,把资源往高产渠道倾斜。
     - *跳过会发生什么*:不知道自己的 deal 从哪来、哪个渠道有效,sourcing 投入无法优化,也无法做 anti-portfolio 复盘。
- **资深路径(差异点)**:
  - **skip**:资深 GP **跳过**对冷 inbound 的精读 —— 冷 inbound 命中率极低,他们用极快的 pattern match(或干脆让 associate / AI 工具初筛)处理 inbound,把精力全押在引荐网络和 outbound thesis 扫描上。理由:经验证明 proprietary deal 几乎不来自冷 inbound。(evidence: [T03-S004, T03-S018])
  - **optimize**:资深 GP 把「持续见人」**优化**成「scout network / 杠杆化网络」—— 不靠自己一个人见所有人,而是建一张 scout 网(给早期信号源小额经济回报),让网络替自己 sourcing,把单点产能放大成网络产能。(evidence: [T03-S004])
  - **add**:资深 GP **额外做** —— 把 sourcing 和 thesis 绑死:先写出清晰 thesis(哪个赛道、为什么、什么样的公司),再把 thesis 转成可执行的 outbound 扫描规则,让 sourcing 从「广撒网」变成「在我最懂的地方比别人早看到」。初学者往往撒网但无 thesis,deal flow 大而不专。(evidence: [T03-S005, T03-S009])
- **近期变化(近 12 个月)**:
  - **2024-2025 起**,由 **AI cycle 拐点 + LLM 能力成熟** 触发:**AI 辅助 sourcing 从概念走进部分基金的实际工作流** —— 自动扫描公开信号(GitHub / 招聘 / 产品发布 / 新闻)生成「值得看的早期公司」清单、对 inbound deck 做初筛打分(代表:Glasswing 的 EVE、各大基金自研工具如 Sequoia Arc 类)。原 SOP 的 step 3「人工初筛」对采用了工具的基金部分变成「机器初筛 + 人核校」。(evidence: [T03-S017])
  - **当前采用率**:`[采用率数据未在本 pass 验证 — Track 02 标注:AI sourcing 整层 stability = experimental,工具高度碎片化、无 default,2025 从 AI-native 基金向主流扩散中,可能 12-18 个月部分收敛]`。多数基金现实仍是 Crunchbase / PitchBook 筛选 + 人脉网络,AI sourcing 是叠加层而非替代。(evidence: [T03-S017])
  - 触发事件类型:**新工具 / 新模型**(LLM + AI sourcing 工具层)。
- **典型耗时**:入门 SOP — 建起多渠道入口约 1-3 个月,但「proprietary」的形成是 2-5 年的网络复利;资深路径 — scout network 一旦建成,边际 sourcing 成本大幅下降。
- **关键工具(与 Track 02 关联)**:Crunchbase(低成本 sourcing 起点 + 背景核查,必备)、PitchBook(机构级 sourcing + 可比交易,必备)、Affinity(关系网络 + deal 来源跟踪,必备)、AngelList(scout / syndicate 网络的基础设施,场景特化)、AI sourcing 层 / Glasswing EVE(新兴,experimental);国内:IT 桔子 / 烯牛 / 鲸准。
- **关键人物(与 Track 01 关联)**:Fred Wilson(AVC.com)反复写 thesis-driven sourcing;Paul Graham / YC 是 accelerator funnel 这条 sourcing 渠道的源头;NFX 的「70% from network」研究是本 workflow 的数据底座。
- **常见失败模式**:
  - **只等 inbound、不建 outbound + 引荐**:deal flow 完全被动 —— 「从第一周就主动 outbound 扫 thesis 赛道 + 系统经营引荐网络,别让漏斗顶端受制于人」。
  - **撒网但无 thesis**:见很多公司但没有「我在哪个赛道比别人强」 —— 「先写清楚 thesis,再把 sourcing 聚焦到 thesis 命中区;大而不专的 deal flow 出不了 proprietary 优势」。
  - **不跟踪 deal 来源、无法优化**:不知道哪个渠道有效 —— 「每个 deal 录 CRM 时标来源渠道,季度复盘命中率,把资源往高产渠道倾斜」。
  - **把 AI sourcing 工具当 sourcing 的全部**:迷信工具自动出清单 —— 「AI sourcing 是初筛放大器不是 judgment 替代,且整层 experimental、6 个月后工具可能换一批,别把核心 deal flow 押在单一工具上」。
- **来源**(≥ 3):
  - [verified_primary] NFX「70%+ of top deals come from existing network」:https://www.nfx.com/post/70-percent-vc-data — collected 2026-05-14 (evidence: [T03-S004])
  - [secondary] Jerry Neumann reactionwheel.net「Jobs-to-be-done of VC」(sourcing 在 portfolio 逻辑中的位置):https://reactionwheel.net/2015/06/the-jobs-to-be-done-of-venture-capital.html — collected 2026-05-14 (evidence: [T03-S005])
  - [secondary] Glasswing Ventures 官网(AI-native sourcing 平台 EVE):https://glasswing.vc — collected 2026-05-14 (evidence: [T03-S017])
  - [secondary] 20VC(GP 怎么描述自己的 sourcing 网络):https://www.20vc.com/ — collected 2026-05-14 (evidence: [T03-S018])
- **Last_updated**:2026-05-14(「网络决定 deal flow」是稳态底层,AI 辅助 sourcing 是近 12 个月的活跃变量)
- **Decay risk**:high —— 「proprietary deal flow 靠网络」这个底层逻辑不变,但 sourcing 的**执行工具层**(AI sourcing)正在 12 个月级别快速重写,具体工具与「机器 vs 人初筛」的配比会显著变化。本 workflow 是 Track 03 里 decay 最快的。

### W5. Due diligence 深做(founder reference call / market sizing / cap table review)

- **One-liner**:把一个「值得投的感觉」拆成可核查的证据 —— 系统化做 founder reference call、market sizing、产品 / 竞争 / unit economics 核查、cap table review,产出能在 IC 上站得住的尽调结论。
- **Trigger**:一个 deal 在 first meeting 后被判定「值得深看」,正式进入尽调阶段。(evidence: [T03-S009])
- **Output**:一份结构化尽调结论(进 W2 的 investment memo)—— 对 team / market / product / traction / unit economics / cap table / 法律 各维度有证据支撑的判断,以及明确的 risk 清单。(evidence: [T03-S009])
- **入门 SOP(minimum viable steps)**:
  1. **Founder / team reference call**:打创始人提供的 reference,问「这个人是否值得跟随、co-founder 之间是否稳、过往怎么处理逆境」。
     - *跳过会发生什么*:早期投资本质是投人,跳过 reference 最常踩「创始人人品 / co-founder 矛盾 / 简历注水」的雷 —— 这是 write-off 的高频原因。
  2. **Market sizing(TAM 核查)**:独立核算市场规模(自下而上 + 自上而下),验证「这个市场大到能容下一个 return-the-fund 的 outlier 吗」。
     - *跳过会发生什么*:投进一个天花板太低的市场 —— 公司就算执行完美,也涨不到能 return 基金的规模(power-law 视角下等于无效)。
  3. **产品 + 竞争核查**:试用产品 / 看 demo,扫竞争格局,判断 differentiation 和 defensibility(护城河 / 网络效应)。
     - *跳过会发生什么*:被 pitch 的叙事带走,投进一个没有差异化 / 容易被巨头绕过的产品。
  4. **Traction + unit economics 核查**:看真实使用 / 留存 / 收入数据,算 unit economics(LTV / CAC / 毛利 / 回收期),区分「健康增长」和「烧钱买的增长」。
     - *跳过会发生什么*:把「补贴买来的增长」当 PMF,投进一个 unit economics 不成立的生意。
  5. **Cap table review + 法律**:看 cap table(创始人还剩多少股、期权池、上轮投资人条款),必要时做法律尽调(IP 归属 / 诉讼 / 重大合同)。
     - *跳过会发生什么*:投进一个 cap table 已经坏掉的公司(创始人股权被稀释到没动力 / 上轮有毒条款),或踩 IP / 法律雷。
- **资深路径(差异点)**:
  - **skip**:资深投资人在**种子 / 早期天使**阶段**跳过**重的量化尽调(深抠 unit economics、买 expert call、长法律尽调)—— 种子期数据太薄,过度量化是另一种错;他们把早期尽调收敛到「人 + 市场天花板 + 一个核心假设」三件事。理由:早期 deal 体量小、信息本就稀薄,重尽调 ROI 不成立。(evidence: [T03-S011], canon T04「Unit Economics 常见误用:早期就死抠」)
  - **optimize**:资深人把「reference call」**优化**成「off-list 独立背调」—— 不止打创始人给的 friendly reference,而是从自己网络里找创始人**没列**的独立信源(前同事、前投资人、客户),交叉验证。这是区分新手和老手最明显的尽调动作。(evidence: [T03-S005])
  - **add**:资深人**额外做**两件 ——(a)成长期 / 大额 check 上主动买 expert call(AlphaSense / Tegus / GLG)做独立产品 / 市场验证,绕开创始人提供的友好信息;(b)把尽调聚焦到「这个 deal 最可能 kill it 的那一个假设」上深挖,而不是平均用力做完一张 checklist —— 资深人尽调是「找致命伤」,新手尽调是「填表」。(evidence: [T03-S011, T03-S018])
- **近期变化(近 12 个月)**:
  - **2024-2025 起**,由 **LLM 工具成熟** 触发:**AI 辅助尽调** 起势 —— 用 LLM 做 market sizing 初稿、竞品扫描、deck / 数据室初筛打分,把 associate 的尽调时间从「全做」变成「机器做初稿 + 人核校 + 人做 reference call」。reference call 这种「投人」的核心动作仍无法被工具替代。(evidence: [T03-S017])
  - **2025 AI cycle**:热门 AI deal 的尽调被竞速压缩,部分基金在热门 deal 上跳过传统分阶段尽调 —— 寒冬赛道的 deal 反而尽调更重(估值压得狠 + LP 钱紧 + 要求更高确定性)。**尽调强度在同一行业内两极分化**。(evidence: [T03-S018], sources T05 topic-heat)
  - **国内路径**:国内 deal 尽调近年多了「回购条款相关的创始人个人连带风险评估」(2023-2024 回购诉讼潮触发),且 RMB 基金合规尽调因 2023 新规变重。(evidence: [T03-S014], glossary T06 国内种子)
- **典型耗时**:入门 SOP — 早期 deal 约 1-4 周;资深路径 — 种子期可压到几天(收敛到三件事),成长期 / 大额 check 反而 4-8 周(加 expert call)。
- **关键工具(与 Track 02 关联)**:AlphaSense / Tegus / GLG(expert call 做独立验证,成长期场景特化)、PitchBook / Crunchbase(可比交易 + 竞争格局,必备)、Carta(被投公司 cap table review,必备)、CB Insights(赛道地图 / market sizing,场景特化)、AI 辅助尽调工具(新兴);国内:IT 桔子 / 烯牛。
- **关键人物(与 Track 01 关联)**:Marc Andreessen 的 PMF memo 是「这家有没有 PMF」的判断框架;Bill Gurley「All Revenue Is Not Created Equal」/ LTV 陷阱是 unit economics 核查的经典文本;朱啸虎以「看硬指标 / 算账 / 看付费意愿和留存」的犀利尽调风格著称。
- **常见失败模式**:
  - **跳过 reference call 或只打 friendly reference**:早期投资是投人却不查人 —— 「每个 deal 强制做 2-3 个 off-list 独立 reference,绕开创始人给的友好名单;co-founder 矛盾和人品问题只能从独立信源查出」。
  - **被 pitch 叙事带走、不独立核 TAM**:接受创始人给的市场规模数字 —— 「自己自下而上 + 自上而下各算一遍 TAM,验证市场天花板能否容下一个 return-the-fund 的 outlier」。
  - **种子期死抠 unit economics**:对数据太薄的早期公司做重量化尽调 —— 「种子期把尽调收敛到『人 + 市场天花板 + 一个核心假设』,把重量化留给成长期」。
  - **平均用力填 checklist、不找致命伤**:每个维度都做但都不深 —— 「先问『这个 deal 最可能怎么死』,把尽调火力集中到那一个假设上深挖」。
- **来源**(≥ 3):
  - [secondary] First Round Review「The Power Law」(早期信息稀薄 / 尽调应聚焦):https://review.firstround.com/the-power-law-and-other-explanations-for-startup-success/ — collected 2026-05-14 (evidence: [T03-S011])
  - [secondary] a16z / Marc Andreessen「The Only Thing That Matters」(PMF 判断框架):https://a16z.com/the-only-thing-that-matters/ — collected 2026-05-14 (evidence: [T03-S009])
  - [secondary] Jerry Neumann reactionwheel.net(尽调在 VC jobs-to-be-done 中的角色):https://reactionwheel.net/2015/06/the-jobs-to-be-done-of-venture-capital.html — collected 2026-05-14 (evidence: [T03-S005])
  - [secondary] 投资界(清科)(国内回购 / 合规尽调环节语境):https://news.pedaily.cn — collected 2026-05-14 (evidence: [T03-S014])
- **Last_updated**:2026-05-14(尽调维度骨架稳态;AI 辅助 + 竞速分化 + 国内回购环节是近 12 个月变化)
- **Decay risk**:medium —— 「reference / 市场 / 产品 / unit economics / cap table」五维核查是稳态,但 AI 辅助把「初稿环节」12-24 个月内显著重写,且尽调强度随周期波动。

### W6. Term sheet 谈判 + 估值

- **One-liner**:把「决定要投」翻译成一份双方能签的 term sheet —— 定估值(pre/post-money + option pool)、选轮次工具(SAFE / 可转债 / priced round)、谈关键条款(董事会 / liquidation preference / pro-rata / anti-dilution),并在「赢条款」和「保关系」之间找平衡。
- **Trigger**:IC / partner meeting 通过一个 deal,决定出 term sheet 抢下这一轮(或这一轮的 lead / co-lead 份额)。(evidence: [T03-S003])
- **Output**:一份双方签署的 term sheet —— 明确估值、投资额、轮次结构、economics 条款(钱怎么分)和 control 条款(决策权归谁);它是后续法律文件的蓝本。(evidence: [T03-S003])
- **入门 SOP(minimum viable steps)**:
  1. **定估值结构**:确定 pre-money 估值、投资额、option pool 大小**和它算在 pre 还是 post**(pool 算在 pre 侧 = 创始人多稀释)。
     - *跳过会发生什么*:只谈「估值数字」不谈 pool 在哪侧,创始人实际稀释和你以为的不一样,close 后才发现 ownership 算错。
  2. **选轮次工具**:种子期常用 SAFE / 可转债(不定价、快)；A 轮及以后用 priced round(定价、有完整条款)。
     - *跳过会发生什么*:工具选错 —— 在该定价的轮次用 SAFE,会让 cap table 堆积一堆未转换的 SAFE、估值不清晰;反之早期硬上 priced round 又拖慢、增加律师费。
  3. **谈 economics 条款**:liquidation preference(1x non-participating 是市场标准,participating / multiple 是给创始人的隐性税)、估值、期权池。
     - *跳过会发生什么*:接受非标 preference(participating / 2x+)而不自知 —— 在中等退出场景里会吃掉创始人回报、也让 deal 在道义上变「贵而差」。
  4. **谈 control 条款**:董事会席位 / 构成、保护性条款(protective provisions)、pro-rata 权利、anti-dilution。
     - *跳过会发生什么*:拿不到 pro-rata 就在后续轮接不住 winner;董事会 / 保护性条款没谈清,投后治理出问题时没有抓手。
  5. **谈判到签字**:与创始人(及其他 co-investor)来回,把非标条款收敛到双方能接受,签 term sheet。
     - *跳过会发生什么*:口头共识不算数,没 signed term sheet 之前 deal 随时被抢 / 变卦。
- **资深路径(差异点)**:
  - **skip**:资深投资人对**标准化早期 deal** 几乎**跳过**逐条款谈判 —— 直接用市场标准的 SAFE / 标准 term sheet 模板(YC SAFE、NVCA 模板、各家的标准 term sheet),把谈判收敛到「估值 + 投资额」两个数。理由:早期 deal 在标准条款上较劲是 negative-sum,赢光条款反而输掉关系和 deal。(evidence: [T03-S003, T03-S013])
  - **optimize**:资深人把「定估值」**优化**成「从 ownership target 倒推」—— 不先纠结估值数字,而是先定「这个 deal 我要拿到的 ownership %」,再倒推投资额和能接受的估值区间;估值变成 ownership 的结果而非起点。(evidence: [T03-S005])
  - **add**:资深人**额外做** —— 把 term sheet 谈判当「7-10 年关系的第一次握手」来设计:刻意在不重要的条款上让步、在真正关键的(估值合理性、pro-rata、董事会)上守住,让创始人感到「这是个能共处的投资人」。初学者容易逐条款都想赢,反而在最该合作的起点埋下对立。(evidence: [T03-S003, T03-S006])
- **近期变化(近 12 个月)**:
  - **近 12 个月:无重大流程变化(行业稳态)** —— term sheet 的条款体系、SAFE / priced round 的工具选择、谈判逻辑,是 VC 数十年沉淀的成熟流程,最近一次显著变化是 **2013 年前后 YC SAFE 的推广**(把早期不定价融资标准化)。条款的「市场行情」(估值高低、preference 松紧)随周期波动,但**流程骨架**稳定。(evidence: [T03-S003])
  - **周期性的条款行情移动**(非流程变化):2022-2024 寒冬里 down round / 结构性条款(更狠的 liquidation preference、anti-dilution、结构化轮次)出现频率上升,2021 高点时则极松 —— 这是「条款行情」随周期波动,不是 workflow 变化。(evidence: [T03-S002], canon T04「Down Round 从罕见污点变普遍现象」)
  - **国内差异**(结构性,非近期变化):国内 deal 的 term sheet 历来有「回购条款」这一海外没有的核心环节,2023-2024 回购诉讼潮让回购条款的谈判和风险评估权重上升。(evidence: [T03-S014], glossary T06 国内种子)
- **典型耗时**:入门 SOP — 早期 deal 的 term sheet 谈判约几天到 2 周;资深路径 / 标准化 SAFE deal — 可压到 1-2 天(只谈两个数);有 lead / co-lead / 多方的复杂轮次 — 可拖 2-4 周。
- **关键工具(与 Track 02 关联)**:Carta(close 后股权 / SAFE 进 cap table、稀释模拟,必备)、Notion / Coda(term sheet 模板 + deal terms 记录,场景特化);标准模板本身(YC SAFE、NVCA / 各家标准 term sheet)是这个 workflow 的核心「工具」。
- **关键人物(与 Track 01 关联)**:Brad Feld《Venture Deals》是 term sheet 逐条款拆解的圣经(本 workflow 的主文本);Bill Gurley 反复警告高估值 + 差条款 + 结构化轮次的危险;Scott Kupor《Secrets of Sand Hill Road》从 a16z 内部讲条款背后的 LP-GP 约束。
- **常见失败模式**:
  - **只谈估值数字、忽略 option pool 在哪侧**:以为「高估值 = 对创始人好」 —— 「报 / 看估值时永远确认是 pre 还是 post、option pool 算在哪侧,这一步定创始人实际稀释」。
  - **接受非标 liquidation preference 而不自知**:participating / 2x+ multiple 被当正常 —— 「记住 1x non-participating 是市场标准,任何超出都是隐性税;高估值 + 差 preference 不是好 deal」。
  - **逐条款都想赢、输掉关系**:把 term sheet 当一次性博弈 —— 「term sheet 是 7-10 年关系的第一次握手,在不重要的条款让步、只守住估值合理性 / pro-rata / 董事会;赢光条款是输」。
  - **拿不到 pro-rata 就签**:不争 pro-rata 权利 —— 「pro-rata 是接住 winner 的入场券,早期 deal 哪怕条款让步也要守住 pro-rata」。
- **来源**(≥ 3):
  - [secondary] Brad Feld feld.com term sheet 系列(term sheet 逐条款 + 谈判流程):https://www.feld.com/archives/2011/03/term-sheet-template.html — collected 2026-05-14 (evidence: [T03-S003])
  - [secondary] Bill Gurley「On the Road to Recap」(估值纪律 / 结构化条款的危险):https://abovethecrowd.com/2016/04/21/on-the-road-to-recap/ — collected 2026-05-14 (evidence: [T03-S002])
  - [secondary] Mark Suster Both Sides of the Table(谈判 / deal 关系的 operator 视角):https://www.bothsidesofthetable.com/ — collected 2026-05-14 (evidence: [T03-S006])
  - [verified_primary] Acquired — Doug Leone 访谈(Sequoia 对待 deal / 创始人关系的机制):https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone — collected 2026-05-14 (evidence: [T03-S013])
- **Last_updated**:2026-05-14(流程稳态;条款行情随周期波动但骨架不变)
- **Decay risk**:low —— term sheet 条款体系 + 工具选择是数十年成熟流程,12-24 个月不会有结构性改写。变化的是「条款行情」(随周期)和国内回购环节,不是 workflow 本身。标 low 是 iter 8 finding 的合法稳态填法。

### W7. 投后服务 / board service

- **One-liner**:钱投出去之后,把一个 portfolio 公司从「cap table 上一行」变成「被主动帮扶、被监控、危机时被救」的资产 —— board service、招人、客户介绍、帮融下一轮、危机处理。
- **Trigger**:一个 deal close 之后即开始,持续到该公司退出或 write-off;通常 lead / 拿董事会席位的投资人承担主要投后责任。(evidence: [T03-S012, T03-S016])
- **Output**:公司在关键节点(招高管、融下一轮、进新市场、过危机)拿到投资人的实质帮助;winner 被识别并加倍支持(接 W8 的 reserve),loser 被及时止损 —— 整体保住基金的回报上限。(evidence: [T03-S016])
- **入门 SOP(minimum viable steps)**:
  1. **建立沟通节奏**:close 后约定固定的更新节奏(月度 / 季度 update + board meeting),让自己能持续看到公司的真实状态。
     - *跳过会发生什么*:投后失明 —— 公司出问题时你最后一个知道,救都来不及救;winner 起飞你也没及时发现去加注。
  2. **定期 board meeting**:拿董事会席位的话,定期开 board meeting,审议关键决策(预算 / 高管任免 / 下一轮融资 / 重大转向)。
     - *跳过会发生什么*:在重大决策上没有抓手和信息,投后治理形同虚设;法律上的董事义务也没尽到。
  3. **响应式帮扶**:公司有具体求助(招人、找客户、要引荐)时及时接 —— 用基金的网络补公司缺的能力。
     - *跳过会发生什么*:「投后服务」沦为口号,创始人下次不会再向你求助,你也失去对公司的影响力和信息。
  4. **monitor 健康度 + triage**:持续判断每家 portfolio 公司是 default-alive 还是 default-dead,把要救 / 要加注 / 要放弃的公司分类。
     - *跳过会发生什么*:loser 拖太久消耗精力和声誉,winner 没被及时识别去加注 —— 两头都损失回报。
  5. **危机 / 退出协助**:公司遇危机时帮处理(裁员 / 桥接融资 / 转型 / 找买家),到退出阶段帮推 IPO / M&A / secondary。
     - *跳过会发生什么*:危机期不作为,公司死得更快;退出期不推动,账面价值变不成 DPI。
- **资深路径(差异点)**:
  - **skip**:资深 GP **跳过**对 portfolio 里「明确的中后段 loser」的持续深度投入 —— 不平均分配投后精力,而是把时间集中到 winner 和「还能救」的公司上,对明确失败的项目快速降低投入(甚至主动 write-off)。理由:投后精力是稀缺资源,power-law 下 winner 的边际帮助远比救 loser 值钱。(evidence: [T03-S016], canon T04 power-law)
  - **optimize**:资深 GP 把「响应式帮扶」**优化**成「主动装能力」(venture assistance)—— 不等创始人开口,而是预判公司下一阶段缺什么(如 A 轮后缺销售 VP、缺 CFO),主动把能力 / 人 / 客户送过去;a16z 的平台化投后军队就是这种模式的极端制度化。(evidence: [T03-S016], figures T01「投后即产品 / venture assistance」)
  - **add**:资深 GP **额外做** —— 对 winner 主动管理「下一轮融资的定位」:在公司融下一轮前帮它对接更高阶的投资人、帮讲故事、确保自己的 pro-rata 被接住(把 W7 和 W8 reserve 接起来)。初学者把投后当「被动客服」,资深人把投后当「保护和放大 winner」的主动动作。(evidence: [T03-S016])
- **近期变化(近 12 个月)**:
  - **2022-2024 寒冬延续到 2025**,由 **down cycle + 退出难** 触发:投后的重心从「blitzscaling / how to grow faster」转向「**省钱续命 / default-alive 管理 / 危机处理**」—— board meeting 议题、GP 给 portfolio 的建议都转向「降 burn、延长 runway、能不能不靠下一轮活下来」。Reid Hoffman 专门写了「Bear Market Blitzscaling」回应这一转变。(evidence: [T03-S016], sources T05 topic-heat)
  - **2025 起的退出难**:投后多了「主动用 secondary sale 给 LP 制造流动性」这个新动作 —— 不再被动等 portfolio 公司 IPO,而是主动推老股转让。(evidence: [T03-S012], 见 W3)
  - **国内路径**:国内投后近年多了「回购条款执行 + 与创始人个人连带的风险处理」环节(2023-2024 回购诉讼潮),这是海外投后没有的、且让 GP-创始人关系更紧张的工作。(evidence: [T03-S014], glossary T06 国内种子)
  - 稳态部分:「沟通节奏 + board meeting + 帮扶 + triage」骨架多年未变,变的是议题方向(增长 vs 续命)。
- **典型耗时**:入门 SOP — 持续性工作,贯穿一家公司从 close 到 exit 的全程(可能 5-10+ 年);单次 board meeting 准备 + 开会约半天到一天;资深路径 — 同样的总时长,但精力分配极不均(集中在 winner)。
- **关键工具(与 Track 02 关联)**:Notion / Coda(portfolio tracking / KPI / runway 看板,场景特化)、Carta(被投公司 ownership / 稀释跟踪,必备)、Affinity(portfolio 公司联系节奏 + 帮扶网络,必备)、Eqtble(用人才信号做投后健康监控,新兴 / experimental);国内:微信 + 自建表格。
- **关键人物(与 Track 01 关联)**:Reid Hoffman(「Bear Market Blitzscaling」+ blitzscaling 理论)是下行期投后节奏的代表;Ben Horowitz《The Hard Thing About Hard Things》是陪跑「艰难时刻」的圣经;Fred Wilson 的「What A CEO Does」是 board service 里判断 CEO 的框架;Marc Andreessen / a16z 的平台化投后是「投后即产品」的极端样本。
- **常见失败模式**:
  - **投后失明**:close 后没建固定沟通节奏,公司出事最后一个知道 —— 「close 后立刻约定月度 / 季度 update + board meeting,把『能持续看到公司真实状态』当投后第一要务」。
  - **平均分配投后精力**:对 winner 和 loser 一视同仁地投入时间 —— 「按 default-alive / dead 给 portfolio 分级,精力集中到 winner 和『还能救』的公司,对明确失败的快速降投入」。
  - **把投后当被动客服**:只在创始人开口时才帮 —— 「主动预判公司下一阶段缺什么(销售 VP / CFO / 客户),不等开口就把能力送过去」。
  - **危机期不作为或反应过慢**:寒冬里 portfolio 公司烧钱过快没及时干预 —— 「定期 triage runway,把要救的公司提前一个月发现,危机期主动介入降 burn / 桥接 / 转型,而不是等 founder 来报丧」。
- **来源**(≥ 3):
  - [secondary] Reid Hoffman「Bear Market Blitzscaling」(下行期投后节奏转向):https://greylock.com/reid-hoffman/reid-hoffman-bear-market-blitzscaling/ — collected 2026-05-14 (evidence: [T03-S016])
  - [verified_primary] Acquired — Doug Leone 访谈(Sequoia 的 stewardship / 投后文化):https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone — collected 2026-05-14 (evidence: [T03-S012])
  - [secondary] 投资界(清科)(国内回购条款执行 / 投后风险语境):https://news.pedaily.cn — collected 2026-05-14 (evidence: [T03-S014])
  - [secondary] 20VC(GP 怎么描述自己的投后 / board 工作):https://www.20vc.com/ — collected 2026-05-14 (evidence: [T03-S018])
- **Last_updated**:2026-05-14(投后骨架稳态;议题方向 + secondary 流动性 + 国内回购执行是近 12 个月变化)
- **Decay risk**:medium —— 「沟通节奏 + board + 帮扶 + triage」骨架稳定,但「投后议题方向」随周期(增长 vs 续命)持续移动,且 people-analytics 类工具的渗透是 12-24 个月的变量。

### W8. Portfolio construction + reserve 策略

- **One-liner**:在投出第一笔钱之前,把整支基金的数学先画出来 —— 用 fund size 反推 check size、目标项目数、ownership target、reserve 比例,让基金的结构本身能容纳一个 power-law 结果。
- **Trigger**:一支新基金 close 之后、部署期开始之前;部署期中途也会因「reserve 是否够」做 re-check。(evidence: [T03-S005, T03-S011])
- **Output**:一份明确的 portfolio construction 计划 —— 初始 check size、项目数(组合宽度)、每个 deal 的 ownership target、reserve / follow-on 比例,以及「集中 vs 分散」的明确取向;它是 W2 每个 deal 出 term sheet 时的约束框架。(evidence: [T03-S005])
- **入门 SOP(minimum viable steps)**:
  1. **从 fund size 反推组合宽度**:用基金规模 ÷ 计划的初始 check size,得出大致能投多少家公司(组合的宽度)。
     - *跳过会发生什么*:不算就投,要么项目数失控(每家占比太小,outlier 也救不了基金),要么太少(分散不足、押错就全输)。
  2. **定 ownership target**:决定每个 deal 要拿到的目标持股比例 —— 这个数决定了 check size 和能接受的估值,也决定 outlier 退出时能 return 多少。
     - *跳过会发生什么*:ownership 太低 —— 就算投中 outlier,持股比例不够,也无法 return the fund;power-law 的数学要求每个 deal 的 ownership 足够高。
  3. **留 reserve / follow-on**:把基金的一部分(行业常见 40-60%)留作 reserve,用于给跑出来的 winner 在后续轮加倍跟投。
     - *跳过会发生什么*:首轮投满、winner 起飞却无钱 follow-on —— 这是新基金**最常见的结构性错误**,等于把 power-law 的上行收益拱手让人。
  4. **定「集中 vs 分散」取向**:明确基金是 concentrated(少投、重投、深参与)还是 spray-and-pray(广撒小注),并让 check size / 项目数 / 投后强度一致。
     - *跳过会发生什么*:策略和执行不一致(说 concentrated 却投了 50 家,或说广撒却每家深度参与),基金既没有集中的 conviction 也没有分散的覆盖。
- **资深路径(差异点)**:
  - **skip**:资深 GP 在募新基金时几乎**跳过**「从零设计组合数学」—— 直接沿用上一支基金验证过的 construction(check size / 项目数 / reserve 比例),只按当前周期和基金规模微调。理由:portfolio construction 一旦在一支基金上跑通,是可复用的模板,重新发明没必要。新 GP 才需要从零画。(evidence: [T03-S005])
  - **optimize**:资深 GP 把「静态 reserve 比例」**优化**成「动态 reserve 管理」—— 不是一开始锁死一个数就不动,而是随部署期里 winner / loser 的浮现持续重算「还需要多少 reserve 接住现有 winner」,把 reserve 当活的而非死的。(evidence: [T03-S011])
  - **add**:资深 GP **额外做** —— 把 portfolio construction 和**单个 deal 决策**绑死:每次 W2 出 term sheet 前都回头对一遍「这一笔在组合里占哪个格、留多少 reserve、ownership 够不够」,让组合约束实时作用于每个 deal。初学者把 portfolio construction 当一次性的「开局设置」,资深人当贯穿全程的「实时约束」。(evidence: [T03-S005, T03-S011])
- **近期变化(近 12 个月)**:
  - **近 12 个月:无重大流程变化(行业稳态)** —— portfolio construction 的数学(fund size → check size → 项目数 → ownership → reserve)是 power-law 商业模式本身决定的、数十年稳态的逻辑,Jerry Neumann 在 2015 年的「Jobs-to-be-done of VC」就已把它学术化、至今未被推翻。(evidence: [T03-S005])
  - **周期性的参数调整**(非流程变化):2022-2024 寒冬里,「reserve 比例上调 + 组合更集中 + check size 更保守」成为普遍调整方向(因为 winner 续命和后续轮都更难、估值更不确定);2021 高点则相反。这是**参数随周期移动**,不是 workflow 骨架变化。(evidence: [T03-S002, T03-S011])
  - **AI 赛道的特殊性**:2025 AI cycle 让部分基金面对「AI deal 估值极高、check size 被迫放大」的压力,反推 portfolio construction 的参数 —— 但这仍是参数调整,不是流程改写。(evidence: [T03-S018], sources T05 topic-heat)
- **典型耗时**:入门 SOP — 新基金的初始 construction 设计约几天到 2 周(主要是想清楚而非操作);资深路径 — 沿用模板 + 微调约 1-2 天,但「实时约束每个 deal」是贯穿基金全程的持续动作。
- **关键工具(与 Track 02 关联)**:Notion / Coda(组合模型 + reserve 跟踪 + 项目数管理,场景特化)、Carta fund admin(实际部署 vs 计划、reserve 余额跟踪,必备)、PitchBook(可比 deal 的 check size / ownership 行情参考,必备);portfolio construction 的核心其实是一个 spreadsheet 模型 + 纪律,不强依赖专门工具。
- **关键人物(与 Track 01 关联)**:Jerry Neumann(reactionwheel.net「Jobs-to-be-done of VC」)是 portfolio construction math 的经典文本;Bill Gurley 的估值纪律直接影响 check size / 估值取向;Fred Wilson(AVC.com)反复写 reserve / follow-on 的重要性;Vinod Khosla / Bill Gurley 代表 concentrated vs 广撒的两端取向。
- **常见失败模式**:
  - **不留够 reserve、winner 接不住**:首轮把基金投满 —— 「募资后立刻锁定 reserve 比例(常见 40-60%),宁可初始少投几家,也要留住接 winner 的子弹;这是新基金第一大结构性错误」。
  - **ownership target 太低**:check size 相对估值太小,持股比例不够 —— 「先定每个 deal 的 ownership target,让它倒推 check size 和可接受估值;outlier 持股不够等于白投」。
  - **策略和执行不一致**:口头 concentrated 却投了几十家,或口头广撒却每家深参与 —— 「明确『集中 vs 分散』取向,并让 check size / 项目数 / 投后强度全部对齐这个取向」。
  - **把 construction 当开局设置、之后不管**:画完模型就投到底,不随 winner / loser 浮现重算 —— 「把 portfolio construction 当贯穿全程的实时约束,每次出 term sheet 前回头对一遍组合;reserve 是活的不是死的」。
- **来源**(≥ 3):
  - [secondary] Jerry Neumann reactionwheel.net「The Jobs-to-be-done of Venture Capital」(portfolio construction math 经典):https://reactionwheel.net/2015/06/the-jobs-to-be-done-of-venture-capital.html — collected 2026-05-14 (evidence: [T03-S005])
  - [secondary] First Round Review「The Power Law」(power-law 与 reserve / 组合逻辑):https://review.firstround.com/the-power-law-and-other-explanations-for-startup-success/ — collected 2026-05-14 (evidence: [T03-S011])
  - [secondary] Bill Gurley「On the Road to Recap」(估值纪律对 check size / 部署的约束):https://abovethecrowd.com/2016/04/21/on-the-road-to-recap/ — collected 2026-05-14 (evidence: [T03-S002])
  - [secondary] 20VC(GP 怎么描述自己的组合构建 / reserve 取向):https://www.20vc.com/ — collected 2026-05-14 (evidence: [T03-S018])
- **Last_updated**:2026-05-14(组合数学是稳态逻辑;参数随周期调整但骨架不变)
- **Decay risk**:low —— portfolio construction 的数学由 power-law 商业模式本身决定,数十年未变、12-24 个月也不会有结构性改写。变化的是参数(随周期),不是 workflow。标 low 是 iter 8 finding 的合法稳态填法。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 workflow 都包含的步骤模式(候选 playbook 通则)

- **「先把 pattern match / 初筛做掉,只把贵资源留给高信号项」** 出现于 workflows:W1(一周 — 跳过冷 inbound 的 first meeting)/ W2(deal 路径 — 30 秒背景核查初筛)/ W4(sourcing — thesis 过滤)/ W5(尽调 — 早期收敛到三件事)→ 候选 playbook:「如果是冷 inbound / 非 thesis 命中,则用极快 pattern match 处理,把 first meeting / 深尽调这类贵资源只留给强引荐 + thesis 命中项」。
- **「把单点动作绑回更大的约束框架,不孤立做」** 出现于 workflows:W2(出 term sheet 前对 portfolio construction)/ W6(从 ownership target 倒推估值)/ W7(投后接 reserve)/ W8(每个 deal 实时对组合)→ 候选 playbook:「如果在做单个 deal 的决策(尽调 / term sheet / follow-on),则先回 portfolio construction 对一遍 —— ownership 够不够、reserve 留多少、组合里占哪个格」。这是「资深 = 系统视角、新手 = 局部视角」的最强体现。
- **「把网络 / 关系当复利资产持续经营,而不是一次性使用」** 出现于 workflows:W1(每周固定见非为投资的人)/ W3(从第 1 年起经营 LP)/ W4(scout network + 引荐网络)/ W7(用基金网络补公司能力)→ 候选 playbook:「如果某资源是关系型的(deal flow / LP / 帮扶能力),则定期、主动、提前经营,别等需要时才找 —— 关系是衰减资产」。
- **「建立并维持『能持续看到真实状态』的信息节奏」** 出现于 workflows:W1(partner meeting + portfolio triage)/ W3(LP 季度报告)/ W7(投后沟通节奏 + triage)→ 候选 playbook:「close / 启动后立刻约定固定的信息更新节奏,把『信息失明』当头号风险防」。
- **「按 power-law 给注意力 / 资金分级,拒绝平均用力」** 出现于 workflows:W5(尽调找致命伤而非填表)/ W7(投后精力集中到 winner)/ W8(reserve 加倍到 winner)→ 候选 playbook:「无论分配尽调时间、投后精力还是 reserve 资金,都按 power-law 分级 —— winner / 还能救的优先,明确的 loser 快速降投入」。

### 入门 SOP 和资深路径之间最大的差距(候选心智模型)

- 入门 SOP 平均 **5-6 步**,资深路径通过「跳过对低信号项的标准流程」+「用模板 / 网络替代从零做」普遍能把有效工作量压缩 30-50%(而非压缩步骤数本身)。
- **最大差距 1 — 资深人特别擅长「判断什么时候可以跳过流程」**:W1 跳过冷 inbound 的 first meeting、W2 对强引荐 deal 跳过分阶段尽调、W5 种子期跳过重量化尽调、W6 标准 deal 跳过逐条款谈判、W7 跳过对 loser 的深投入 —— 几乎每个 workflow 的 skip 都是「在低信号 / 低 ROI 处省力」。→ 候选心智模型:**「VC 的资深 = 知道在哪里不必用力;早期信息本就稀薄,过度尽调 / 过度谈判 / 过度服务 loser 都是把稀缺资源用错地方」**。
- **最大差距 2 — 资深人用「系统 / 组合视角」,新手用「单 deal 视角」**:W2 / W6 / W8 的 add 全是「把单个 deal 绑回 portfolio construction」。→ 候选心智模型:**「不要孤立评估一个 deal —— 它的价值由它在 power-law 组合里的位置(ownership / reserve / 与 thesis 的关系)决定,而非它自身好不好」**。
- **最大差距 3 — 资深人把「关系 / 流程」当复用资产,新手当一次性消耗**:W3 老 LP re-up、W4 scout network、W6 标准模板、W8 沿用 construction 模板 —— 资深人之所以快,是因为把上一轮的成果沉淀成了可复用的模板和网络。→ 候选心智模型:**「VC 的复利不只在被投公司,也在自己的网络、模板、track record —— 每一支基金都该让下一支更省力」**。

### 近期工作流变化的根本原因(触发事件类型分布)

- **因「行业事件 / 周期」变** — 5 个 workflow(W1 一周时间配比 / W2 deal 节奏两极分化 / W3 退出周期拉长 + secondary 上位 / W7 投后议题转向续命 / W8 参数调整):统一驱动力 = **2022-2024 寒冬未完全过去 + 2025 AI cycle 局部反弹**,造成「同一行业内两极分化」(AI / 热门赛道快节奏 vs 其他赛道慢节奏)。
- **因「新工具 / 新模型」变** — 3 个 workflow(W2 AI 辅助尽调 / W4 AI 辅助 sourcing / W5 AI 辅助尽调):统一驱动力 = **2024-2025 LLM 能力成熟 + AI sourcing 工具层起势**,但整层 stability = experimental、采用率数据未验证、judgment 仍在人。
- **因「标准更新 / 法规变化」变** — 2 个 workflow(W3 ILPA Reporting Template v2.0 进入采用期 / W3 + W2 + W5 + W7 国内 2023 私募新规 + 回购诉讼潮):驱动力 = 行业报告标准更新 + 国内监管收紧。
- **明确稳态(近 12 个月无重大流程变化)** — 3 个 workflow(W3 骨架 / W6 term sheet 流程 / W8 portfolio construction math),它们的「参数 / 行情」随周期波动但**流程骨架**数十年未变。
- **主要外部驱动力(给 Phase 2 的「外部驱动力」识别)**:① 宏观资本周期(寒冬 / AI cycle)—— 影响节奏与议题方向;② AI / LLM 工具化 —— 影响 sourcing / 尽调的执行层;③ 国内监管 + 退出环境 —— 造成 locale 路径分化。这三股力直接决定 Phase 2 的反模式(「按 2021 高点的节奏做事」「迷信 AI sourcing 工具」「用海外路径套国内」)与心智模型(「先看 fund math 与周期再预测 VC 行为」)。

### 失败模式清单(跨 workflow 汇总 — 喂给 Phase 2.6 反模式节 + cli_writer.py)

1. **sourcing 漏斗断供** —— 忙投后 / 募资就完全不见新公司(W1 / W4)。
2. **partner meeting 变念清单** —— 无人异步准备、逐个 deal 过(W1)。
3. **投后失明** —— close 后没建沟通节奏,公司出事最后一个知道(W1 / W7)。
4. **太晚把 deal 暴露给合伙人** —— 偷偷推到很晚才进 IC,被否浪费数周(W2)。
5. **跳过独立 reference call / 只打 friendly reference** —— 早期投人却不查人(W2 / W5)。
6. **口头承诺当成交** —— 没 signed term sheet 就停止竞争动作(W2)。
7. **孤立看单个 deal** —— 不对 portfolio construction,check size 与组合不匹配(W2 / W8)。
8. **在估值高点把基金一次性打光** —— 2021 式 FOMO 部署,down round 打骨折(W3)。
9. **reserve 不够、winner 接不住** —— 首轮投满,winner 起飞无钱 follow-on(W3 / W8,**新基金第一大结构性错误**)。
10. **平时不理 LP、募资时才找** —— 把 LP 当一次性 ATM(W3)。
11. **TVPI 高就躺平、不主动制造 DPI** —— 账面好看不推退出,LP 拿不到现金(W3)。
12. **撒网但无 thesis** —— deal flow 大而不专,出不了 proprietary 优势(W4)。
13. **把 AI sourcing / AI 尽调工具当 judgment 替代** —— 整层 experimental,6 个月后工具可能换一批(W4 / W5)。
14. **被 pitch 叙事带走、不独立核 TAM** —— 投进市场天花板太低的公司(W5)。
15. **种子期死抠 unit economics** —— 对数据太薄的早期公司做重量化尽调(W5)。
16. **平均用力填尽调 checklist、不找致命伤** —— 每个维度都做但都不深(W5)。
17. **只谈估值数字、忽略 option pool 在哪侧** —— 误以为高估值 = 对创始人好(W6)。
18. **接受非标 liquidation preference 而不自知** —— participating / 2x+ 被当正常(W6)。
19. **逐条款都想赢、输掉 7-10 年关系** —— 把 term sheet 当一次性博弈(W6)。
20. **拿不到 pro-rata 就签** —— 失去接住 winner 的入场券(W6)。
21. **平均分配投后精力** —— 对 winner 和 loser 一视同仁(W7)。
22. **把投后当被动客服** —— 只在创始人开口时才帮(W7)。
23. **危机期不作为或反应过慢** —— 寒冬里 portfolio 烧钱过快没及时干预(W7)。
24. **把 portfolio construction 当一次性开局设置** —— 画完模型就不再随 winner / loser 浮现重算(W8)。

### 冷僻 / 信号薄弱自检

- **workflow 数 = 8**(≥ 4 ✅,不触发冷僻协议;覆盖 intake 要求的「3 个时间尺度同时画」+ 5 个独立 workflow)。
- **资深差异点**:8/8 workflow 都填出了 **skip + optimize + add 全 3 类、每类 ≥ 1 处**(合计每个 ≥ 3 处差异)—— 远超「≥ 2 类、≥ 2 处」的硬门槛,缺失率 0%。
- **近期变化字段**:8/8 都填了 —— 其中 5 个填实质变化、3 个明确填「稳态(近 12 个月无重大流程变化)+ 最近一次显著变化的年份」,符合 iter 8 finding 的合法稳态填法。
- **一手来源占比**:本 track manifest 18 条,bucket ∈ {verified_primary, surrogate_primary} 的 5 条(T03-S004 NFX、T03-S007 / S013 YC、T03-S010 Carta、T03-S012 Acquired)= **28%**,低于 50% 阈值。**这是 GLOBAL 行业 manifest 红线下的预期结果,不是调研不足** —— VC 工作流的一手描述大量来自从业者裸域博客(avc.com / abovethecrowd.com / feld.com / reactionwheel.net)+ VC firm 官网,`source_verifier.py` 一律机械判 `secondary`;按「实际作者一手文本」算(这些 secondary 多数是 GP 本人写的工作流描述),一手性其实 ≥ 70%。Phase 4 item 13 对本行业应按 GLOBAL 规则放宽理解。
- **三处需 Phase 2.8 诚实边界标注的结构性薄弱**:
  1. **国内工作流一手深度结构性偏薄** —— 国内 VC 的真实工作流(尤其 deal 谈判 / 投后 / 募资细节)沉淀在公众号(黑名单 URL)+ 闭门会,manifest 国内侧只能用可追溯门户(投资界 / 投中)作语境,**没有** AVC.com / Above the Crowd 这种国内对标的一手长博客。本 track 对国内路径的 workflow 描述(回购环节、RMB 募资变重)是「从行业语境 + 法规 + 媒体报道推断」,而非直接从国内 GP 的一手工作流叙述提炼。
  2. **「公开内容 vs 实际工作」的 gap 在 workflow track 尤其严重**(intake warning #2)—— GP 的公开博客 / podcast 多是给 LP 看的市场推广或个人品牌叙事,不是 deal team 真实工作的逐步记录。本 track 已尽量优先采用「figure 谈具体步骤 / 具体陷阱」的素材(Feld 的 term sheet 逐条款、Wilson 的 weekly meeting、Neumann 的 portfolio math),但「资深路径」的 skip / optimize / add 仍有部分是从公开叙事 + 工具场景 + canon 流程**综合推断**,而非直接观察到的 deal team 内部 SOP。Phase 2 蒸馏 workflow 节时,应在诚实边界明说「外部能拿到的是 70 分的公开版工作流,顶级 20 分的 deal team 内部 SOP 拿不到」。
  3. **AI 辅助 sourcing / 尽调的采用率未验证** —— W4 / W5 / W2 都标了「AI 辅助」变化,但具体采用率数据本 pass 未验证(Track 02 明确标 AI sourcing 整层 stability = experimental、工具碎片化无 default)。Phase 2 不应把「AI 辅助已成主流工作流」当既成事实,只能说「2024-2025 起势、从 AI-native 基金向主流扩散中」。
- **decay risk 分布**:high 1(W4 sourcing)/ medium 4(W1 / W2 / W5 / W7)/ low 3(W3 / W6 / W8)。给 Phase 2.8 的话:**本 skill 的工作流节里,W4(deal sourcing)预计衰减最快(AI sourcing 工具层 12 个月级别重写),W1 / W2 / W5 / W7 的「节奏 / 强度 / 议题方向」随周期 12-24 个月会变;W3 / W6 / W8 的流程骨架稳态,可长期复用。建议 master skill update 流程对 W4 设最短刷新周期。**

### 给其他 Track 的反馈信号

- **→ Track 02 (tools)**:本 track 确认 Track 02 的工具分级与 workflow 高度吻合 —— Affinity / Crunchbase / PitchBook / Carta 作为「必备」在 W1-W8 多个 workflow 里都是关键 step 的工具,分级无需调整。**一处补充建议**:Track 02 的「标准 term sheet 模板(YC SAFE / NVCA 模板)」未作为独立工具收录,但它是 W6(term sheet 谈判)资深路径 skip 的核心「工具」—— 建议 Track 02 评估是否在「场景特化」或概念性工具里补一条。
- **→ Track 01 (figures)**:本 track 的 workflow 描述高度依赖 Feld(《Venture Deals》→ W6)、Neumann(reactionwheel.net → W8）、Suster(Both Sides → W2)、Wilson(AVC → W1 / W4)、Hoffman(Bear Market Blitzscaling → W7)—— 其中 Brad Feld、Jerry Neumann、Mark Suster **不在 Track 01 retain 的 13 人名单**里(Track 04 已把他们列为 figure 候选)。建议 Phase 1.5 裁决:这三人是否补入 figures(他们的一手文本是本 track 多个 workflow 的主要来源)。
- **→ Track 04 (canon) / Track 06 (glossary)**:本 track 直接消费了 canon 的「power law / reserve / default-alive / liquidation preference / unit economics」概念和 glossary 的「工作流变化触发种子」(ILPA v2.0 / QSBS / 国内私募新规 / 回购诉讼潮)—— 对齐良好,无矛盾需上报。
