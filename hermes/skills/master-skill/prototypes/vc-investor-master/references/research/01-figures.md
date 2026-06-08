# Track 01 — Figures（风险投资人 / 行业大佬）

> Phase 1 wave 2 research output. Industry: Venture Capital — early-stage investor (GP / Partner / Principal). Locale: `global`（US 美元基金 / 国内美元基金 / RMB 基金 三路径）. Profile: `practitioner`.
> 调研日期窗口: 2026-05-14. 撒网 ~20 候选, retain 13.

## Source Manifest

> **GLOBAL 行业说明**: VC 行业一手内容大量发在作者裸域博客（avc.com / abovethecrowd.com / paulgraham.com）和 VC firm 官网 + Substack/Medium。`source_verifier.py classify` 对这些一律判 `secondary`，本 manifest 照判不上抬。例外: VC firm 官网当 vendor docs → `surrogate_primary`；Acquired.fm episode 路径 → verifier 判 `verified_primary`。黑名单（知乎/公众号/百度百科/LinkedIn 文章正文/Quora）一律不收。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://avc.com/2010/08/what-a-ceo-does/ | secondary | 2026-05-14 | Fred Wilson (USV) | AVC.com「What A CEO Does」— CEO 三件事框架 |
| T01-S002 | https://avc.com/2012/01/the-management-team-while-building-the-business/ | secondary | 2026-05-14 | Fred Wilson (USV) | AVC.com「The Management Team」— 投后管理团队判断 |
| T01-S003 | https://www.paulgraham.com/startupideas.html | secondary | 2026-05-14 | Paul Graham (YC) | PG essay「How to Get Startup Ideas」— notice 而非 think up |
| T01-S004 | https://pmarchive.com/guide_to_startups_part4.html | secondary | 2026-05-14 | Marc Andreessen archive | pmarca 存档「The Only Thing That Matters」PMF 论原文 |
| T01-S005 | https://a16z.com/ | surrogate_primary | 2026-05-14 | Andreessen Horowitz | VC firm 官网 — vendor docs，a16z 多策略平台型基金 |
| T01-S006 | https://www.acquired.fm/episodes/sequoia-capital | verified_primary | 2026-05-14 | Acquired Podcast | Sequoia 公司史深度集，含合伙人决策机制 |
| T01-S007 | https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone | verified_primary | 2026-05-14 | Acquired Podcast | Doug Leone 长访谈 — Sequoia 文化 + stewardship |
| T01-S008 | https://www.20vc.com/ | secondary | 2026-05-14 | Harry Stebbings (20VC) | GP 访谈 podcast，行业 default 嘉宾池 |
| T01-S009 | https://greylock.com/reid-hoffman/reid-hoffman-bear-market-blitzscaling/ | secondary | 2026-05-14 | Reid Hoffman (Greylock) | Greymatter「Bear Market Blitzscaling」— 下行期打法 |
| T01-S010 | https://www.khoslaventures.com/entrepreneurs/thought-provoking | secondary | 2026-05-14 | Khosla Ventures | KV 官网 thought-provoking 栏 — deep tech 投资哲学 |
| T01-S011 | https://www.bondcap.com/reports/tai | secondary | 2026-05-14 | Bond Capital (Mary Meeker) | Bond「Trends — AI」2025 报告页 — 宏观趋势 ground truth |
| T01-S012 | https://www.sequoiacap.com/ | surrogate_primary | 2026-05-14 | Sequoia Capital | VC firm 官网 — vendor docs，Moritz/Leone 老一辈范式 |
| T01-S013 | https://greylock.com/team/reid-hoffman/ | secondary | 2026-05-14 | Greylock Partners | Greylock 团队页 — Hoffman 投资 focus（网络效应 + AI） |
| T01-S014 | https://www.ycombinator.com/library | surrogate_primary | 2026-05-14 | Y Combinator | YC Startup Library — vendor docs，acceleration 派教材 |
| T01-S015 | https://en.wikipedia.org/wiki/All-In_(podcast) | secondary | 2026-05-14 | — | All-In Podcast 词条 — 网红 VC 派背景与商业化 |
| T01-S016 | https://time.com/7023237/vinod-khosla-interview/ | secondary | 2026-05-14 | TIME | TIME 专访 Khosla — All in on AI，contrarian bets |
| T01-S017 | https://www.allin.com/ | secondary | 2026-05-14 | All-In Podcast | All-In 官网 — Chamath/Sacks/Friedberg/Calacanis 主页 |
| T01-S018 | https://a16z.com/books/the-hard-thing-about-hard-things/ | secondary | 2026-05-14 | a16z (Ben Horowitz) | a16z 书页《The Hard Thing About Hard Things》 |
| T01-S019 | manifest:none | secondary | 2026-05-14 | — | 沈南鹏 红杉中国 — 公开长文本稀缺，名片型条目 |
| T01-S020 | https://book.douban.com/subject/35188914/ | verified_primary | 2026-05-14 | 张磊《价值》 | 《价值》(2020) 一手著作豆瓣书页 — 长期主义方法论 |
| T01-S021 | https://m.chinaventure.com.cn/news/80-20250328-385692.html | secondary | 2026-05-14 | 投中网 | 朱啸虎 2025 访谈「批量退出人形机器人」 |
| T01-S022 | https://www.chuangxin.com/blog/ai2-0-agi | verified_primary | 2026-05-14 | 创新工场 | 创新工场官博 — 李开复 AI 2.0 立论原文 |
| T01-S023 | manifest:none | secondary | 2026-05-14 | 徐小平 真格基金 | 徐小平早期天使 / 教育派 — 长素材不足，名片型条目 |
| T01-S024 | https://www.gsb.stanford.edu/faculty-research/case-studies | surrogate_primary | 2026-05-14 | Stanford GSB | 课程 / 案例库 — VC 学术框架，syllabus 推断 canon |
| T01-S025 | https://www.cls.cn/detail/1991592 | secondary | 2026-05-14 | 财联社 | 朱啸虎「中国 AI 爆发在应用端」访谈 |
| T01-S026 | https://m.thepaper.cn/newsDetail_forward_9255061 | secondary | 2026-05-14 | 澎湃新闻 | 张磊「不确定时间线坚守长期主义」专访 |
| T01-S027 | https://finance.sina.com.cn/money/bond/2024-08-01/doc-inchcxfw2727367.shtml | secondary | 2026-05-14 | 新浪财经 | 李开复从创新工场到零一万物的 AI 转型与全球野心 |
| T01-S028 | https://hbr.org/2016/04/blitzscaling | secondary | 2026-05-14 | Reid Hoffman / HBR | HBR「Blitzscaling」— 速度优先于效率的扩张论 |

## 总览（按行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 值得读/听/看 | 来源数 |
|---|------|---------|----------|------------|-------|
| 1 | Marc Andreessen | a16z 联创 GP | 把 VC 平台化（multi-strategy + 投后军队），PMF 论奠基 | 📖🎙️ | 4 |
| 2 | Ben Horowitz | a16z 联创 GP | operator 视角的 VC，「艰难」管理论 + founder-friendly 主张 | 📖🎙️ | 3 |
| 3 | Bill Gurley | Benchmark（已退休 GP） | concentrated 投资派旗手，估值纪律 + 反泡沫 memo | 📖🎙️🎬 | 4 |
| 4 | Fred Wilson | USV 联创 GP | thesis-driven 投资公开化，20 年长跑博客 AVC.com | 📖🎙️ | 3 |
| 5 | Paul Graham | YC 联创 | acceleration 派认知源头，把早期投资变成「批量教育」 | 📖🎬 | 3 |
| 6 | Reid Hoffman | Greylock 合伙人 | operator-investor 范式，blitzscaling 理论 | 📖🎙️ | 3 |
| 7 | Vinod Khosla | Khosla Ventures 创始人 | deep tech 大胆押注派，「敢冒险才有 outlier」 | 📖🎙️🎬 | 3 |
| 8 | Mary Meeker | Bond Capital 创始人 | Internet/AI Trends 报告 — 行业宏观趋势 ground truth | 📖🎙️ | 3 |
| 9 | Doug Leone / Michael Moritz | Sequoia 老一辈 GP | 「安静派」长期合伙制 + 机构化 VC 范式 | 🎙️🎬 | 3 |
| 10 | Chamath / Sacks / Calacanis 等 | All-In Pod 网红 VC | VC 个人品牌化 + 公开化的极端样本 | 🎙️ | 3 |
| 11 | 张磊 | 高瓴资本创始人 | 中国「长期主义」投资旗手，VC+PE 混合 | 📖🎙️ | 3 |
| 12 | 朱啸虎 | 金沙江创投主管合伙人 | 中国互联网早期王牌，犀利「快进快出」实战派 | 🎙️ | 3 |
| 13 | 李开复 | 创新工场董事长 | 中国 AI 早期投资 + 孵化派，技术背景 VC | 📖🎙️🎬 | 3 |

---

### 1. Marc Andreessen / 马克·安德森

- **One-liner**: a16z 联合创始人，把 VC 从「精品作坊」改造成「平台型机构」（multi-strategy 基金 + 大规模投后服务团队），并以「市场 > 团队 > 产品」的 PMF 论奠定一代早期投资判断框架。
- **核心身份**: Andreessen Horowitz (a16z) 联合创始人 & GP；前 Netscape 联合创始人（创业者出身的投资人）。
- **代表作品**: ① 经典 memo / essay《The Only Thing That Matters》(2007，pmarca 博客)；② a16z 平台化机构本身（招了大量市场、招聘、BD 团队，颠覆传统 VC 编制）；③《Why Software Is Eating the World》(2011, WSJ)。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《The Only Thing That Matters》— pmarca 存档原文 https://pmarchive.com/guide_to_startups_part4.html
  - 🎙️ a16z Podcast / 各类长访谈（Lex Fridman、Tim Ferriss 均有 2h+ 长谈）— 入口 https://a16z.com/
  - 🎬 ⚠️ 无单一标志性 conference talk，但长 podcast 访谈丰富，可替代
- **核心思想关键词**: 市场决定论（market wins）、product/market fit、software eating the world、VC 平台化（投后即产品）、技术乐观主义。
- **voice_samples**:
  - 客户解释样本（对创始人解释什么时候算 PMF）: 「PMF 没发生时你能感觉到 —— 客户没真正获得价值、口碑不传播、用量涨不快、销售周期太长、很多单子永远 close 不掉。PMF 发生时你也能感觉到 —— 产品被买走的速度跟你能造的一样快。」(source: T01-S004, 转述+压缩，原文为英文长段)
  - 同业讨论样本（对其他投资人讲优先级排序）: 「好团队遇上烂市场，市场赢；烂团队遇上好市场，市场赢。」(source: T01-S004, 原话转译，"when a great team meets a lousy market, market wins")
  - 监管 / 行业宏观样本（公开谈技术与社会）: 「软件正在吞噬整个世界」—— 把每个传统行业都重构为软件公司之争，是 a16z 投资 thesis 的总纲。(source: T01-S005, 推断 — 综合其 2011 WSJ 文与 a16z 官网定位)
- **sub_skill_candidate**: `true` — 有海量 30min+ 长访谈材料、思想体系自洽（市场决定论 + 平台化 VC）、行业影响力前 3、与「早期投资判断」focus 高度对齐。
- **dual_role**: `"founder + thinker"` — Netscape 创始人转 VC。
- **最近 12 个月动态**: 2024-2025 a16z 持续加码 AI（American Dynamism、AI infra 大额基金）；Andreessen 个人发表《Techno-Optimist Manifesto》后政治表态明显右转，2024 公开支持 Trump，引发行业对 a16z「政治化」的讨论。
- **争议 / 批评**: ① a16z 平台化被批评是「AUM 规模游戏」—— 管理费驱动而非 returns 驱动，concentrated 派（Benchmark）认为大基金摊薄了 carry 的意义；② PMF 论被批「事后诸葛」，难以在投资当下操作化；③ 个人政治表态被指损害 firm 中立性。
- **来源**:
  - [Primary] 《The Only Thing That Matters》: https://pmarchive.com/guide_to_startups_part4.html, collected 2026-05-14
  - [Secondary] a16z 官网（机构定位 / 投资 thesis）: https://a16z.com/
  - [Reference] Stanford EE204 课程引用 PMF 框架: http://web.stanford.edu/class/ee204/ProductMarketFit.html
- **可信度自评**: high — 一手 essay + 机构本身可直接观察，长访谈材料充足。

### 2. Ben Horowitz / 本·霍洛维茨

- **One-liner**: a16z 另一位联合创始人，以「operator 视角」定义了 founder-friendly 投资派 —— 主张押注 founder-CEO、陪跑「没有标准答案的艰难时刻」，而非把创始人换成职业经理人。
- **核心身份**: Andreessen Horowitz (a16z) 联合创始人 & GP；前 Opsware (Loudcloud) 联合创始人兼 CEO。
- **代表作品**: ①《The Hard Thing About Hard Things》(2014) —— 创业 / 投资界 management 圣经；②《What You Do Is Who You Are》(2019, 企业文化)；③ a16z「founder CEO 优先」投资原则的提出与制度化。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《The Hard Thing About Hard Things》— a16z 书页 https://a16z.com/books/the-hard-thing-about-hard-things/
  - 🎙️ a16z Podcast 多集 + 各播客长访谈（谈 CEO 心理建设、wartime vs peacetime CEO）
  - 🎬 ⚠️ 未找到单一标志性长 talk，但书 + 长 podcast 已足够建立框架
- **核心思想关键词**: founder-CEO 优先、wartime vs peacetime CEO、艰难时刻没有标准答案（the struggle）、CEO 心理建设、企业文化即「你是谁」。
- **voice_samples**:
  - 同业讨论样本（对投资人讲为何押 founder-CEO）: 「a16z 偏好 founder CEO —— 怎么成为一个 founder CEO，是这本书要讲的核心问题之一。」(source: T01-S018, 转述 — a16z 书页对全书主旨的概括)
  - 客户解释样本（对创业者讲管理的本质）: 「商学院不教的那些最难的问题 —— 怎么降级甚至开掉一个忠诚的老友、自己的心理怎么扛住整个公司都指望你、聪明人却是烂员工怎么办。」(source: T01-S018, 转述压缩，原文为英文)
  - 监管 / 行业样本（公开谈企业文化与边界）: 「你做什么，你就是谁」—— 文化不是墙上的价值观，是公司实际容忍和奖励的行为。(source: T01-S018, 推断 —《What You Do Is Who You Are》核心命题)
- **sub_skill_candidate**: `false` — 重要且影响力前 5，但其公开输出与 Andreessen 高度同源（同属 a16z thesis），独立成 sub-skill 会与「Marc Andreessen / a16z 平台派」大量重叠；建议在 a16z 派系下合并处理。
- **dual_role**: `"founder + thinker"` — Opsware CEO 转 VC，operator 经验是其投资视角的根。
- **最近 12 个月动态**: 2024-2025 随 a16z 整体在 AI 与 American Dynamism 加码；个人持续以「founder-CEO 优先」立场参与公开讨论；与 Andreessen 一同卷入 a16z 政治化争议。
- **争议 / 批评**: ① 「founder-friendly」被批是 a16z 抢 deal 的营销话术 —— 当 founder 与基金利益冲突时（如该不该卖公司），a16z 仍会施压；② operator 经验是否真能迁移成投资判断，业内有保留 —— 会管公司 ≠ 会选公司。
- **来源**:
  - [Primary] a16z 官方书页（作者本人机构发布）: https://a16z.com/books/the-hard-thing-about-hard-things/, collected 2026-05-14
  - [Secondary]《The Hard Thing About Hard Things》Goodreads 条目: https://www.goodreads.com/book/show/18176747-the-hard-thing-about-hard-things
  - [Reference] a16z 机构「founder CEO 优先」定位: https://a16z.com/
- **可信度自评**: medium — 一手书 + 机构定位可查，但缺少独立于 Andreessen 的、专门谈「投资判断」（而非「管理」）的长访谈，投资方法论部分需 Phase 2 与 a16z 整体合并提炼。

### 3. Bill Gurley / 比尔·格利

- **One-liner**: Benchmark 退休 GP，concentrated（高集中度、高 conviction）投资派的旗手 —— 以华尔街研究员的估值纪律和「平等合伙制」反对 VC 规模化，长期用《Above the Crowd》博客做反泡沫公开喊话。
- **核心身份**: Benchmark Capital 前 General Partner（投出 Uber、OpenTable、Zillow、Stitch Fix、GrubHub、Nextdoor）；前 CS First Boston 科技研究分析师（亚马逊 IPO 主分析师）。
- **代表作品**: ①《Above the Crowd》博客（1996 起，网络效应 / 平台 / 商业模式经济学的长文）—— 名篇《On the Road to Recap》《The Dangerous Seduction of the LTV Formula》《All Revenue Is Not Created Equal》；② Benchmark「平等合伙制」模式（4-5 人，经济与决策权完全平分，无 junior、无 leader）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《Above the Crowd》博客 https://abovethecrowd.com/ —— 尤其《On the Road to Recap》（论 2015-16 估值泡沫）、《The Dangerous Seduction of the LTV Formula》
  - 🎙️ Invest Like the Best / Acquired 等长访谈（谈 Benchmark 合伙制、估值周期、marketplace 经济学）
  - 🎬 多个 conference talk + 「Runnin' Down a Dream」长 talk（谈职业精进）
- **核心思想关键词**: 估值纪律 / 反泡沫、concentrated 高 conviction（少投、重投）、平等合伙制（small & flat）、marketplace 与网络效应经济学、LTV 公式的危险（不能掩盖单位经济学）、资本周期 pattern recognition。
- **voice_samples**:
  - 监管 / 行业宏观样本（公开谈估值泡沫）: 「私募市场的高估值是『纸面上』的 —— 复杂的清算优先权条款让 late-stage 投资人拿到了下行保护，普通员工的期权却没有。」(source: T01-S002, 转述 ——《On the Road to Recap》核心论点压缩)
  - 同业讨论样本（对投资人讲商业模式判断）: 「不是所有收入都生而平等」—— 同样的营收数字，背后留存、毛利、获客成本结构天差地别，要拆开看。(source: T01-S002, 转述，名篇标题《All Revenue Is Not Created Equal》)
  - 客户解释样本（对创业者 / LP 讲 LTV 陷阱）: 「LTV 公式有种危险的诱惑 —— 它让你用一个漂亮的终值掩盖掉获客成本越来越贵、留存越来越差的真相。」(source: T01-S002, 转述 ——《The Dangerous Seduction of the LTV Formula》)
- **sub_skill_candidate**: `true` — 有大量 30min+ 长访谈与系统性长博客、思想体系高度自洽（concentrated + 估值纪律 + 平等合伙制），是与 a16z 平台派直接对立的「另一极」，对「早期投资判断」focus 极具代表性。
- **dual_role**: `"analyst + investor"` — 华尔街研究员出身，估值与公开市场知识是其 pattern recognition 的独特来源。
- **最近 12 个月动态**: 2020 已宣布不再为 Benchmark 新基金募资（实质退休），但 2024-2025 仍高度活跃于公开讨论 —— 2026 年初出现在 Masters in Business 长访谈；持续就 AI 估值、政府与科技关系（其 2023「11 word answer」演讲批评监管俘获）发声。
- **争议 / 批评**: ① concentrated 派的「少投」在 AI 这种赢家通吃、需要广撒网才能押中的周期里，被质疑会系统性 miss 掉早期 outlier；② Gurley 长期看空高估值，2015 年后多次「泡沫预警」但市场继续涨了数年，被批「狼来了」；③ 平等合伙制难复制 —— 多数 firm 做不到，更像 Benchmark 的特例而非可推广范式。
- **来源**:
  - [Primary]《Above the Crowd》博客（作者本人长文）: https://abovethecrowd.com/, collected 2026-05-14
  - [Secondary] Masters in Business 长访谈报道: https://ritholtz.com/2026/03/mib-bill-gurley/
  - [Reference] Acquired 播客 Benchmark 合伙制深度集（引用其模式）: https://www.acquired.fm/episodes
- **可信度自评**: high — 一手长博客 + 多个长访谈，思想体系清晰可追溯。

### 4. Fred Wilson / 弗雷德·威尔逊

- **One-liner**: Union Square Ventures 联合创始人，把「thesis-driven 投资」从内部方法论公开化 —— 用一份 15-20 页白皮书锁定基金主题，并以 20 年、1000+ 篇的 AVC.com 博客把早期投资判断的日常思考全程公开。
- **核心身份**: Union Square Ventures (USV) 联合创始人 & 合伙人（投出 Twitter、Tumblr、Etsy、Coinbase、MongoDB 等）。
- **代表作品**: ① AVC.com 博客（2003 起，几乎日更，1000+ 篇）—— 系列名篇《What A CEO Does》《The Management Team》《The Pro-Rata Opportunity》；② USV 的「投资 thesis 白皮书」实践（每代基金先写主题论文，thesis 1.0「大网络」→ 后续演化）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《What A CEO Does》https://avc.com/2010/08/what-a-ceo-does/ —— CEO 只做三件事的经典框架；配套读《The Management Team》https://avc.com/2012/01/the-management-team-while-building-the-business/
  - 🎙️ Mixergy / Startups.com「Risky Business」等长访谈（谈 USV 的诞生与 thesis 演化）
  - 🎬 ⚠️ 未找到单一标志性长视频 talk，但 AVC.com 体量已远超任何 talk
- **核心思想关键词**: thesis-driven 投资（先写白皮书再投）、CEO 三件事（定愿景 / 招人 / 管现金）、pro-rata 与 reserve 策略、网络与协议（后期延伸到 crypto / web3）、长期公开写作即投资纪律。
- **voice_samples**:
  - 客户解释样本（对创业者 / 新人讲 CEO 到底干什么）: 「一位资深 VC 跟我说，CEO 只做三件事 —— 定整个公司的愿景与战略并讲给所有人听；招到、雇到、留住最好的人；确保账上永远有足够的钱。」(source: T01-S001, 转述 ——《What A CEO Does》原文框架)
  - 同业讨论样本（对投资人讲 thesis 的价值）: 「2003 年做 USV，我们第一件事就是写一份 15 到 20 页的 IT 风险投资白皮书 —— 这跟我 1996 年第一次做 VC 时『没有想法、没有 thesis』完全不同。」(source: T01-S013, 转述 — 综合其多次访谈对 USV 起源的描述)
  - 监管 / 行业样本（公开谈管理团队的市场信号）: 「在今天这个『几乎所有公司都还是半成品』的市场里，社区 / 创始 CEO 亲自做对外沟通是很好的信号 —— 它从一开始就为整个组织定下了面向客户的基调。」(source: T01-S002, 转述 ——《The Management Team》)
- **sub_skill_candidate**: `true` — AVC.com 提供了行业中罕见的「20 年连续公开思考」长素材，thesis-driven 体系自洽且可操作化，影响力前 5，与「早期投资判断 + 基金运营」focus 完全对齐。
- **dual_role**:（无明确双角色 —— 职业 VC 出身，但「20 年日更博客」本身是其独特的 thinker 身份载体）
- **最近 12 个月动态**: AVC.com 仍在更新（虽频率较巅峰期下降）；2024-2025 持续就 AI、climate（USV 已有 climate fund）、crypto 监管发声；USV 的 thesis 已从「大网络」演化到「拓宽 access to 知识 / 资本 / 健康 / well-being」。
- **争议 / 批评**: ① thesis-driven 在快速变化的周期里可能成为「思想牢笼」—— 主题写死后，对 thesis 外的 outlier（如 USV 早期对某些赛道的回避）会系统性错过；② USV 重仓 crypto（Coinbase 是巨大成功，但 2022 crypto 寒冬中 thesis 的稳健性受质疑）。
- **来源**:
  - [Primary] AVC.com《What A CEO Does》（作者本人长文）: https://avc.com/2010/08/what-a-ceo-does/, collected 2026-05-14
  - [Secondary] Mixergy USV 起源长访谈: https://mixergy.com/interviews/fred-wilson/
  - [Reference] AVC.com《The Management Team》: https://avc.com/2012/01/the-management-team-while-building-the-business/
- **可信度自评**: high — 一手长博客体量极大 + 多个长访谈，是本 track 可调研性最强的 figure 之一。

### 5. Paul Graham / 保罗·格雷厄姆

- **One-liner**: Y Combinator 联合创始人，把早期投资从「逐个谈判的精品 deal」改造成「批量、标准化、教育驱动」的加速器模式 —— spray-and-pray 派的认知源头，并用 paulgraham.com 的长 essay 定义了一代创业者与投资人的共同语言。
- **核心身份**: Y Combinator 联合创始人（已退出日常管理）；前 Viaweb 创始人（创业者出身）；高产 essayist。
- **代表作品**: ① YC 加速器模式本身（标准化 SAFE / 标准 deal terms / batch + Demo Day，把早期投资规模化）；② paulgraham.com essays —— 名篇《How to Get Startup Ideas》《Do Things That Don't Scale》《Startup = Growth》《How to Start a Startup》。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《How to Get Startup Ideas》https://www.paulgraham.com/startupideas.html —— 「notice 而非 think up」「live in the future」
  - 🎬《How to Start a Startup》Stanford CS183B 讲座（YC 与斯坦福合开的课，PG 主讲多节）
  - 🎙️ ⚠️ PG 极少上 podcast 长访谈，但 essays + 讲座视频已构成完整体系
- **核心思想关键词**: live in the future（站在未来看现在缺什么）、notice 而非 think up（好点子是「注意到」的）、organic ideas 优于 made-up ideas、do things that don't scale（早期就该做不可规模化的事）、startup = growth、batch + 标准化 deal terms。
- **voice_samples**:
  - 客户解释样本（对创业者讲怎么找点子）: 「找创业点子的方法不是去『想』创业点子，而是去找问题 —— 最好是你自己有的问题。你该用的动词不是『想出来』，而是『注意到』。」(source: T01-S003, 原话转译，"the verb you want to be using ... is not 'think up' but 'notice'")
  - 同业讨论样本（对投资人 / 创业者讲 organic vs made-up）: 「站到未来里去，然后造出那个『缺掉的东西』。好的创业点子对注意到它的人来说是『显而易见』的，但对缺乏那段语境浸泡的外人来说却是隐形的。」(source: T01-S003, 转述+部分原话，"Live in the future, then build what's missing")
  - 监管 / 行业样本（公开谈早期投资的本质）: YC 的整套设计 —— 标准 SAFE、batch、Demo Day —— 本质是「把早期投资从一对一谈判，变成可批量、可教育的流水线」，这是 spray-and-pray 派与 concentrated 派的根本分野。(source: T01-S014, 推断 — 综合 YC Library 定位)
- **sub_skill_candidate**: `true` — essays 体量大且可视为长素材、思想体系极其自洽（且影响一代人共同语言）、影响力前 3；但需注意 PG 的角色更偏「创业者教育」而非「基金运营」，Phase 2 提炼时其「投资判断」维度要侧重 YC 的 funnel 与标准化机制。
- **dual_role**: `"founder + thinker"` — Viaweb 创始人转加速器创办人 + essayist。
- **最近 12 个月动态**: PG 已基本退出 YC 日常，但 2024-2025 仍持续发 essays 与在 X 上高频表达（如关于 founder mode、关于 AI 对创业的影响）；2024 年《Founder Mode》一文引发广泛讨论。
- **争议 / 批评**: ① spray-and-pray 被 concentrated 派批为「稀释 conviction」—— 广撒网摊薄了每家公司的深度参与；② YC 标准化 terms 对创始人友好，但 Demo Day 的「集中融资剧场」被批人为推高早期估值、制造 FOMO；③ PG essays 影响力大，但被指「幸存者偏差」—— 用少数 outlier 反推普适规律。
- **来源**:
  - [Primary]《How to Get Startup Ideas》（作者本人 essay）: https://www.paulgraham.com/startupideas.html, collected 2026-05-14
  - [Secondary] YC Startup Library（机构对其方法的承载）: https://www.ycombinator.com/library
  - [Reference]《How to Start a Startup》Stanford CS183B 课程: 课程页见 https://www.ycombinator.com/library
- **可信度自评**: high — 一手 essays 极其丰富 + 公开讲座视频，体系完整可追溯。

### 6. Reid Hoffman / 里德·霍夫曼

- **One-liner**: Greylock 合伙人，operator-investor 范式的代表 —— 用 LinkedIn 创始人 + PayPal 黑帮的运营经验做投资，并以「闪电式扩张（blitzscaling）」理论系统化了「速度优先于效率」的网络效应公司打法。
- **核心身份**: Greylock Partners 合伙人（2009 年加入）；LinkedIn 联合创始人；早期投资 Facebook、Airbnb 等。
- **代表作品**: ①《Blitzscaling》(2018, 与 Chris Yeh 合著) + 同名斯坦福课程；②《The Start-up of You》《Masters of Scale》(书 + 同名 podcast)；③ Greylock 上「网络效应公司」的系统化投资 thesis。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《Blitzscaling》核心论文版 https://hbr.org/2016/04/blitzscaling —— 速度优先于效率的扩张框架
  - 🎙️ Masters of Scale podcast（Hoffman 主持，访谈大量创始人，提炼扩张规律）；Greymatter《Bear Market Blitzscaling》https://greylock.com/reid-hoffman/reid-hoffman-bear-market-blitzscaling/
  - 🎬 Stanford《Blitzscaling》课程（CS183C）系列长视频讲座
- **核心思想关键词**: blitzscaling（不确定环境下速度优先于效率）、网络效应（business 越多人用越值钱）、operator-investor（用运营经验做投资判断）、闪电式扩张的「下行期版本」（bear market blitzscaling — 仍要在关键处保速度）、systematic 押注 AI 网络效应。
- **voice_samples**:
  - 同业讨论样本（对投资人 / 创始人讲 blitzscaling 定义）: 「Blitzscaling 就是在不确定的环境里，优先选择速度而非效率 —— 关键是你怎么花资本（财务的、人力的、其他的）去换速度。」(source: T01-S028, 转述 — HBR 文核心定义)
  - 客户解释样本（对创业者讲下行期怎么办）: 「下行期不是不 blitzscale，而是要更精准地判断『哪些地方仍然值得用速度换位置，哪些地方该转向效率』。」(source: T01-S009, 转述 ——《Bear Market Blitzscaling》对谈主旨)
  - 监管 / 行业样本（公开谈为何押 AI）: 「我系统性地押注 AI，是因为我看到了下一代网络效应业务的潜力 —— AI 会造出新一代的网络效应公司。」(source: T01-S013, 转述 — Greylock 团队页对其 focus 的描述)
- **sub_skill_candidate**: `true` — 有《Blitzscaling》斯坦福课程 + Masters of Scale 大量长访谈、思想体系自洽（operator-investor + 网络效应 + blitzscaling），影响力前 5，与「早期投资判断」focus 对齐。
- **dual_role**: `"founder + thinker"` —— LinkedIn 创始人转 VC，operator 经验是其投资判断的核心来源。
- **最近 12 个月动态**: 2024-2025 投资 focus 高度集中于 AI（其判断 AI 会创造下一代网络效应业务）；2024 年与 Chris Yeh 在 Greymatter 录《Bear Market Blitzscaling》讨论下行期打法；个人持续以 AI 乐观派身份公开发声（出版《Superagency》谈 AI）。
- **争议 / 批评**: ① blitzscaling 在 2022-2024 寒冬中被广泛反思 —— 「速度优先于效率」被指助长了烧钱不计回报的文化，WeWork 等案例成为反例；② operator-investor 模式被质疑「光环效应」—— 名创始人的背书能拿到 deal，但不等于选 deal 更准；③ Masters of Scale 被批是「成功学叙事」，幸存者偏差明显。
- **来源**:
  - [Primary] Greymatter《Bear Market Blitzscaling》（Hoffman 本人对谈）: https://greylock.com/reid-hoffman/reid-hoffman-bear-market-blitzscaling/, collected 2026-05-14
  - [Secondary] HBR《Blitzscaling》文章: https://hbr.org/2016/04/blitzscaling
  - [Reference] Greylock 团队页（投资 focus）: https://greylock.com/team/reid-hoffman/
- **可信度自评**: high — 一手对谈 + 书 + 斯坦福课程视频，长素材充足。

### 7. Vinod Khosla / 维诺德·科斯拉

- **One-liner**: Khosla Ventures 创始人，deep tech「大胆押注」派的极端代表 —— 主张 VC 应主动接受高失败率去换 outlier，专门「发明一个传统 VC 不碰的品类」并把它做成可投资的赛道。
- **核心身份**: Khosla Ventures 创始人；前 Sun Microsystems 联合创始人；前 Kleiner Perkins 合伙人（创业者 + 老牌 VC 双重背景）。
- **代表作品**: ① Khosla Ventures 本身（专投 deep tech / clean energy / 前沿科技 — 含 OpenAI 的早期机构投资人）；②《Thought Provoking》系列长文 / 演讲（谈 contrarian thinking、AI、技术对社会的影响）；③ 经典论断「Venture assistance」（VC 应主动给公司装能力，而非只给钱）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Khosla Ventures《Thought Provoking》https://www.khoslaventures.com/entrepreneurs/thought-provoking
  - 🎙️ Moonfare "Deal Talk" / Acquired 等长访谈（谈非对称收益、失败容忍度）
  - 🎬 Collision / TIME 等 keynote + 长访谈（谈 AI 的社会冲击、为何 contrarian）https://time.com/7023237/vinod-khosla-interview/
- **核心思想关键词**: contrarian thinking（只有反共识才造出革命性公司）、非对称收益（最多亏 1 倍、可能赚 50 倍）、高失败率容忍 + 充分分散、发明新品类（invent a category VC 传统不碰的）、venture assistance（投后是主动装能力）、技术对社会的「improbable」冲击。
- **voice_samples**:
  - 同业讨论样本（对投资人 / LP 讲非对称收益）: 「风投有意思的地方在于你最多只会亏一倍钱。人们倒抽一口气，但你得看另一面 —— 如果你能赚 50 倍、只亏 1 倍，这是笔相当好的交易。」(source: T01-S016 / Moonfare, 原话转译)
  - 客户解释样本（对创业者讲为何要 contrarian）: 「只有反共识的思考才会带来真正革命性的公司 —— 如果一个想法所有人都觉得合理，它大概率已经不值得创业了。」(source: T01-S010, 转述 — KV「Thought Provoking」核心立场)
  - 监管 / 行业样本（公开谈风险偏好与失败）: 「我不介意单个项目失败的概率更大，只要每只基金里有足够的分散。当我们成功时，回报必须配得上这个风险。」(source: T01-S016, 原话转译，"I don't mind a larger probability of failure ... When we succeed, it has to be worth it")
- **sub_skill_candidate**: `true` — 有 30min+ 长访谈 + 系统性长文、思想体系自洽（contrarian + 非对称收益 + deep tech）、影响力前 5，是「大胆押注 / deep tech」流派的最清晰代表，与「早期投资判断」focus 对齐。
- **dual_role**: `"founder + investor"` —— Sun 创始人 + KP 合伙人，双重背景。
- **最近 12 个月动态**: 2024-2025 high-profile 地「all in on AI」—— KV 是 OpenAI 最早的机构投资人之一（2026 年初 Fortune 详述其在 Musk 退出后接盘的 contrarian bet）；2024 多次公开 keynote 谈 AI 对就业、社会的冲击，立场是激进技术乐观。
- **争议 / 批评**: ① 「高失败率换 outlier」对 LP 是高方差体验 —— 多数 LP 难以承受 KV 风格的波动；② Khosla 个人作风强势，被批对创始人「venture assistance」有时是「venture interference」；③ 早期重仓 clean energy（2010 年前后）多数失败，被指 contrarian 也可能只是「错得很贵」。
- **来源**:
  - [Primary] Khosla Ventures《Thought Provoking》（机构 / 本人长文）: https://www.khoslaventures.com/entrepreneurs/thought-provoking, collected 2026-05-14
  - [Secondary] TIME 专访「Why Vinod Khosla Is All In on AI」: https://time.com/7023237/vinod-khosla-interview/
  - [Reference] Fortune 报道 KV 的 OpenAI contrarian bet: https://fortune.com/2026/03/13/openai-original-vc-bet-how-vinod-khosla-stepped-in-after-elon-musk-balked/
- **可信度自评**: high — 一手长文 + 多个长访谈，思想体系清晰。

### 8. Mary Meeker / 玛丽·米克尔

- **One-liner**: Bond Capital 创始人，「Internet Trends → AI Trends」年度报告的作者 —— 不是靠 deal 风格出名，而是把宏观技术趋势做成全行业 VC 的共同 ground truth，是「数据驱动 thesis」派的标杆。
- **核心身份**: Bond Capital 创始人（growth-stage 基金）；前 Kleiner Perkins 合伙人；前 Morgan Stanley 分析师（「互联网女皇」，1995 互联网报告作者）。
- **代表作品**: ①《Internet Trends》年度报告（1995-2019，曾是全行业必读）；②《Trends — Artificial Intelligence》(2025, 340 页) —— 时隔多年的「复出」报告；③ Bond Capital（专注成长期、数据驱动）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《Trends — Artificial Intelligence》Bond 报告页 https://www.bondcap.com/reports/tai
  - 🎙️ 各类长访谈（围绕 AI Trends 报告，谈采用速度、成本曲线、闭源 vs 开源）
  - 🎬 ⚠️ 经典 Internet Trends 现场发布演讲（历年 Code Conference），AI Trends 时代以报告 + 访谈为主
- **核心思想关键词**: 数据驱动 thesis（用海量图表锚定趋势判断）、采用速度（ChatGPT 2 个月破亿 vs 历史对比）、成本曲线（AI 任务成本两年降 99.7%）、闭源 vs 开源的 17 个月时滞、资本密集型军备竞赛（Big Six 2024 投 2120 亿 infra）、对幻觉 / 偏见 / 监管滞后的审慎。
- **voice_samples**:
  - 监管 / 行业宏观样本（公开谈 AI 采用速度）: 「ChatGPT 两个月到 1 亿用户 —— TikTok 用了 9 个月，Instagram 2.5 年，Google 搜索花了十几年才达到 ChatGPT 现在每周的使用量。」(source: T01-S011, 转述 —《Trends — AI》核心数据点)
  - 同业讨论样本（对投资人讲成本与竞争结构）: 「让 AI 完成一项任务的成本，过去两年掉了 99.7%；但 Big Six 在 2024 年砸了 2120 亿美元做 AI 基础设施，同比涨 63% —— 这是一场围绕算力和芯片的资本密集型军备竞赛。」(source: T01-S011, 转述)
  - 客户解释样本（对 LP / 创业者讲该警惕什么）: 「速度惊人，但要对幻觉、偏见、错误信息和滞后的监管保持警惕 —— 下一波用户可能直接跳过传统 App，用 AI 原生的多模态 agent。」(source: T01-S011, 转述)
- **sub_skill_candidate**: `false` — 影响力极大且报告是行业 ground truth，但其公开输出是「年度趋势报告 + 配套访谈」，缺少持续的、关于「早期投资判断 / 基金运营日常」的长访谈体系；作为「宏观 thesis 输入源」比作为「可蒸馏的投资方法论」更合适，建议归入 Track 05（信息源）加权而非独立 sub-skill。
- **dual_role**: `"analyst + investor"` —— 卖方分析师出身，报告体例是其投资判断的载体。
- **最近 12 个月动态**: 2025 年 6 月发布 340 页《Trends — Artificial Intelligence》，被广泛视为「互联网女皇的复出」，重新成为全行业 AI 趋势的参照系；围绕该报告做了一轮密集长访谈。
- **争议 / 批评**: ① Internet Trends 报告「图表多、判断少」—— 被批是「趋势的搬运工」而非「judgment 的提供者」，对一线 deal 判断帮助有限；② Bond 作为 growth-stage 基金，与「早期投资」focus 存在 stage 错配；③ 复出的 AI 报告被部分人指「太晚、太追热点」，少了 1995 互联网报告的前瞻锐度。
- **来源**:
  - [Primary] Bond《Trends — Artificial Intelligence》报告页（机构 / 本人发布）: https://www.bondcap.com/reports/tai, collected 2026-05-14
  - [Secondary] DeepLearning.AI The Batch 对 AI Trends 报告的报道: https://www.deeplearning.ai/the-batch/venture-capitalist-mary-meeker-revives-her-trend-reports-with-a-deep-dive-into-the-ai-boom
  - [Reference] Policy Commons 收录的 Trends — AI: https://policycommons.net/artifacts/21019554/trends_artificial_intelligence-1/21919986/
- **可信度自评**: medium — 一手报告权威且可查，但「投资判断」维度的长访谈素材不足，可信度的限制在于其角色更偏「趋势作者」而非「deal practitioner」。

### 9. Doug Leone / Michael Moritz — Sequoia 老一辈

- **One-liner**: Sequoia Capital 两位前掌门，「安静派 + 机构化」VC 范式的代表 —— 不靠个人品牌，靠「长青合伙制 + stewardship（受托而非占有）」把一家 VC 做成可跨代传承的机构，是与 All-In 网红派完全相反的一极。
- **核心身份**: Doug Leone — Sequoia 前 Managing Partner / Global Managing Partner（1988 加入，2022 交棒 Roelof Botha）；Michael Moritz — Sequoia 前 Partner（投出 Google、Yahoo、PayPal；记者出身）。
- **代表作品**: ① Sequoia 的机构化设计本身 —— Spartan 文化（无豪华办公室、开放工位、站立办公桌）、平等不计个人功劳、Sequoia Capital Fund（常青基金结构）；② 老一辈口述的「市场聚焦 / 创始人优先 / 主动倾听 / 合伙重于投资 / 纪律」五条核心价值。
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ Acquired《Sequoia Capital Part II (with Doug Leone)》https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone —— Leone 亲口讲文化与传承
  - 🎙️ Invest Like the Best《Doug Leone — Lessons From A Titan》(Patrick O'Shaughnessy)
  - 🎬 Stanford 等「Lessons in Leadership from Doug Leone」讲座
- **核心思想关键词**: stewardship over ownership（受托而非占有 — 把机构留给下一代时要更好）、长青 / 跨代合伙制、Spartan 文化（不靠排场）、不计个人功劳（"we" 而非 "I"，「我们都站在彼此肩膀上」）、市场聚焦 + 创始人优先 + 纪律。
- **voice_samples**:
  - 同业讨论样本（Leone 讲为何不卖 Sequoia 股份）: 「卖掉 Sequoia 的一部分，意味着里面的人会更有钱 —— 但留给下一代去分的那块饼，会更小。」(source: T01-S007, 转述 — Acquired 访谈对 stewardship 的表述)
  - 监管 / 行业样本（Leone 讲机构传承观）: 「我不喜欢『个人功劳』这种说法。我们都站在彼此的肩膀上 —— Michael 站在 Don 的肩上，我站在 Mike 的肩上，这是一个集体的『我们』。」(source: T01-S007, 原话转译，"We're all standing on each other's shoulders")
  - 客户解释样本（讲 Sequoia 的 Spartan 文化）: 「我们的办公空间就反映了公司的哲学 —— 合伙人没有豪华办公室、没有名贵艺术品，所有投资人共用开放工位、用站立办公桌。」(source: T01-S007, 转述)
- **sub_skill_candidate**: `false` — 影响力顶级、长访谈材料也够（Acquired + Invest Like the Best），但两人均已交棒退出日常、近 12 个月几乎无新公开输出；作为「机构化 VC 范式」的历史样本极有价值，但不满足「当前 active」与「持续思想输出」标准，建议作为 Phase 2「VC 流派」中的「机构派」代表合并处理，不单独蒸馏。
- **dual_role**: Moritz = `"journalist + investor"`（记者出身）；Leone = 职业 VC（意大利移民、工程师出身）。
- **最近 12 个月动态**: 两人均已退出 Sequoia 日常 —— Leone 2022 交棒 Roelof Botha，Moritz 更早淡出且 2023 与 Sequoia 关系疏远（卸任 Sequoia Heritage 等）；近 12 个月几乎无围绕 VC 方法论的新公开长输出。Sequoia 本身 2024 完成全球拆分（美国 / 欧洲 Sequoia 与红杉中国、印度/东南亚 Peak XV 各自独立）。
- **争议 / 批评**: ① 「安静派」在 2020s 的注意力经济里被认为「吃亏」—— 不做个人品牌，导致顶级 deal 越来越被网红 VC 的 inbound 抢走；② Sequoia 2021-2022 高点的若干大额 growth 投资（如 FTX）严重 mark down，stewardship 叙事受冲击；③ 全球拆分本身被解读为「机构化范式」在地缘政治下的被动收缩。
- **来源**:
  - [Primary] Acquired《Sequoia Capital Part II (with Doug Leone)》（Leone 本人长访谈）: https://www.acquired.fm/episodes/sequoia-capital-part-ii-with-doug-leone, collected 2026-05-14
  - [Secondary] Sequoia 官网 Doug Leone 主页: https://sequoiacap.com/people/doug-leone/
  - [Reference] Acquired《Sequoia Capital》（机构史，引用 Moritz 时代）: https://www.acquired.fm/episodes/sequoia-capital
- **可信度自评**: medium — 一手长访谈充足，但「当前 active」不满足（均已退出日常），定位为历史范式样本。

### 10. Chamath Palihapitiya / David Sacks / Jason Calacanis — All-In Pod 网红 VC

- **One-liner**: All-In Podcast 四主持（Chamath / Sacks / Friedberg / Calacanis），「VC 个人品牌化 + 公开化」的极端样本 —— 把投资人变成媒体 IP，是「公开多」的天花板，也是 intake 反复警告「公开形象 ≠ 投资能力」的最佳观察对象。
- **核心身份**: Chamath Palihapitiya — Social Capital 创始人（SPAC 浪潮核心人物）；David Sacks — Craft Ventures 联创、前 PayPal COO（2025 起任白宫 AI & Crypto Czar）；Jason Calacanis — LAUNCH / 天使投资人（早期投 Uber 著称）；David Friedberg — The Production Board。
- **代表作品**: ① All-In Podcast 本身（科技 / 经济 / 政治 / 扑克，行业流量天花板）+ All-In Summit（2025 票价约 $7,500）；② 各自的早期投资记录（Calacanis 早期 Uber 是经典案例）；③ Chamath 的 SPAC 实践（2020-2021 把多家公司 SPAC 上市，后多数破发）。
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ All-In Podcast https://www.allin.com/ —— 每周更新，含大量即时 VC 视角与行业八卦
  - 🎬 All-In Summit 各场 keynote（YouTube）
  - 📖 ⚠️ 无系统性著作 —— 这是该群体的特征：高流量、低沉淀，与 Gurley / Wilson 的长博客形成鲜明对比
- **核心思想关键词**: VC 即媒体 IP（个人品牌驱动 deal flow）、宏观叙事先行（从利率 / 地缘 / 政策推导投资）、SPAC 与另类流动性路径（Chamath）、defense tech / American Dynamism、公开表达的政治化（Sacks 入白宫是顶点）。
- **voice_samples**:
  - 同业讨论样本（节目对宏观与投资关系的典型口吻）: 「我们四个『besties』每周聊的是所有跟经济、科技、政治、社会有关的事 —— 还有扑克。」(source: T01-S015, 转述 — All-In 自我定位)
  - 监管 / 行业样本（近期节目主题反映的判断）: 近期 All-In 反复讨论「几十年的全球化和国防工业整合，让美国供应链变脆弱了 —— 风投支持的国防公司正在打破传统模式」。(source: T01-S015, 转述 — Wikipedia 词条对近期 episode 主题的概括)
  - 客户解释样本: ⚠️ 暂未找到该群体面向「创业者解释投资逻辑」的 ≥ 30 字结构化原话片段 —— 其公开内容以宏观评论 / 行业八卦为主，少有把 deal 判断翻译给创始人的样本。
- **sub_skill_candidate**: `false` — 流量影响力极大，但**正是 intake warning #2/#6 的活样本**：公开内容是个人品牌营销与宏观评论，缺少系统性、可操作化的「早期投资判断方法论」沉淀；蒸馏成 sub-skill 会把「网红人设」误当「投资 OS」。建议 Phase 2 把该群体作为「公开形象 vs 实际工作 gap」的反面教材引用，不单独成 skill。
- **dual_role**: 多为 `"founder/operator + investor + media"` —— 但「media」这一层在此群体里权重异常高。
- **最近 12 个月动态**: 2025 David Sacks 出任白宫 AI & Crypto Czar（VC 直接进入政策核心，行业标志性事件）；All-In 2025 推出 The Besties All-In Tequila 等周边、Summit 持续扩大并更偏政治议程；Chamath 的 SPAC 标的多数已破发，SPAC 叙事退潮。
- **争议 / 批评**: ① 「公开多 ≠ 投得好」的最直接案例 —— Chamath 的 SPAC 标的（Clover、SoFi 等）大面积破发，被批用流量收割散户；② 节目被指日益「政治频道化」，投资讨论被党派立场稀释；③ Sacks 入白宫引发「利益冲突」质疑（手握 Craft Ventures 投资组合却管 AI/Crypto 政策）；④ Calacanis 的「早期投 Uber」被反复引用，但其整体投资记录的 power-law 真实分布并不透明。
- **来源**:
  - [Primary] All-In Podcast 官网（该群体本人持续输出）: https://www.allin.com/, collected 2026-05-14
  - [Secondary] All-In (podcast) Wikipedia 词条（背景与商业化）: https://en.wikipedia.org/wiki/All-In_(podcast)
  - [Reference] Shortform 对 All-In 各集的摘要索引: https://www.shortform.com/podcast/all-in-with-chamath-jason-sacks-friedberg
- **可信度自评**: medium — 一手输出体量巨大且持续 active，但「投资方法论」维度的可信度本质偏 low（输出性质是评论 / 品牌而非 deal 方法论），此 medium 是「作为现象样本」的可信度，不是「作为投资导师」的可信度。

### 11. 张磊 / Zhang Lei

- **One-liner**: 高瓴资本创始人，中国「长期主义」投资旗手 —— 把 VC/PE 混合的「长期结构性价值投资」体系化，主张「做时间的朋友」「与伟大格局观者同行」，是国内一级市场最具理论自觉的 GP 之一。
- **核心身份**: 高瓴资本（Hillhouse Capital）创始人兼 CEO；早期重仓腾讯、京东，后期横跨 VC（早期）与 buyout（如百丽私有化），跨一级二级。
- **代表作品**: ①《价值：我对投资的思考》(2020) —— 国内 VC/PE 领域少有的、由顶级 GP 亲笔的体系性著作；② 高瓴的「重仓中国 + 长期持有」实践（腾讯、京东、百济神州等）；③「高瓴公式」（价值 = 选择 × 努力，其中选择是 0/1，努力是后面的若干个 9）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖《价值》(2020) —— 豆瓣书页 https://book.douban.com/subject/35188914/（一手著作，完整阐述长期主义方法论）
  - 🎙️ 围绕《价值》出版的多场长访谈（澎湃、新浪财经等）https://m.thepaper.cn/newsDetail_forward_9255061
  - 🎬 ⚠️ 公开 conference talk 较少 —— 张磊本人相对低调，主要靠著作 + 出版期访谈
- **核心思想关键词**: 长期主义 / 做时间的朋友（把时间和信念投入能长期产生价值的事）、长期结构性价值投资（反套利 / 反投机 / 反零和 / 反博弈）、与伟大格局观者同行（押注 founder 的格局而非短期数字）、从发现价值到创造价值、第一性原理、复利（时间创造复利价值）。
- **voice_samples**:
  - 监管 / 专业讨论样本（公开谈价值投资的本质）: 「长期结构性价值投资的核心是反套利、反投机、反零和游戏、反博弈思维 —— 基于对公司基本面的深度研究，而不是市场的短期波动来做决策。」(source: T01-S020, 转述 ——《价值》核心论点)
  - 客户解释样本（对创业者 / LP 解释「时间的朋友」）: 「时间会创造复利的价值。有些好企业的竞争优势今天还看不出来，明天可能稍露端倪，要到更长期才会完全显现 —— 所以要做时间的朋友。」(source: T01-S020, 转述 ——《价值》对时间的四维阐述)
  - 同业讨论样本（对投资人讲选择与努力）: 「真正的投资有且只有一条标准 —— 是否在创造真正的价值，这个价值是否有益于社会的整体繁荣。」(source: T01-S026, 转述 — 出版期专访)
- **sub_skill_candidate**: `true` —《价值》提供了完整、自洽、可操作化的一手长素材，思想体系（长期主义 + 结构性价值投资）在国内一级市场影响力前 3，与「早期投资判断 + 基金运营」focus 对齐；是国内派系中理论化程度最高的代表。
- **dual_role**: `"founder + thinker"` —— 高瓴创始人 + 体系性著作作者；同时是横跨 VC/PE 的 hybrid investor。
- **最近 12 个月动态**: 张磊与高瓴近年明显低调，公开发声大幅减少；高瓴 2022-2024 经历中概 / 地产 / 教育多重冲击后转向（加码新能源、医疗、出海），但张磊本人 2024-2025 的新公开长输出稀缺 —— 这是其卡片可调研性的主要限制。
- **争议 / 批评**: ① 「长期主义」在 2022-2024 中概与 RMB 退出难的环境下被质疑「长期主义还是被套牢的修辞」；② 高瓴体量过大，VC（早期）业务被 buyout / 二级稀释，「早期投资判断」不再是其主战场；③ 《价值》被部分业内人士批评「偏理念、轻操作」—— 哲学浓度高，但 deal 层面的可复制方法偏少。
- **来源**:
  - [Primary]《价值》(2020) —— 张磊亲笔著作: https://book.douban.com/subject/35188914/, collected 2026-05-14
  - [Secondary] 澎湃新闻「在不确定的时间线里坚守长期主义」专访: https://m.thepaper.cn/newsDetail_forward_9255061
  - [Reference] 财富中文网《评〈价值〉：企业家精神的回归与重构》: https://www.fortunechina.com/zhuanlan/c/2024-12/04/content_460457.htm
- **可信度自评**: medium — 一手著作权威且体系完整，但「最近 12 个月动态」薄弱（张磊近年低调），时效性是主要扣分项。

### 12. 朱啸虎 / Zhu Xiaohu

- **One-liner**: 金沙江创投主管合伙人，中国互联网早期王牌投资人 —— 以「算账、要商业化、快进快出」的犀利实战风格著称，是国内 VC 里少数高频公开、且公开内容直接谈 deal 判断（而非纯人设）的 figure。
- **核心身份**: 金沙江创投（GSR Ventures）主管合伙人；早期投出滴滴、饿了么、小红书、ofo 等互联网代表项目。
- **代表作品**: ① 互联网移动时代的早期 deal 记录（滴滴、饿了么、小红书）；② 大量公开访谈中沉淀的「商业化第一原则」方法论；③ 2025 年「批量退出人形机器人公司」的公开表态 —— 一次罕见的、把基金真实减仓决策公开化的事件。
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ 投中网《金沙江朱啸虎：我们正批量退出人形机器人公司》https://m.chinaventure.com.cn/news/80-20250328-385692.html
  - 🎙️ 财联社《朱啸虎：中国 AI 的爆发点在应用场景端》https://www.cls.cn/detail/1991592
  - 🎬 ⚠️ 无系统性著作 / 长 talk —— 主要靠高频财经媒体访谈，单篇较短，需多篇拼合
- **核心思想关键词**: 商业化第一原则（创业本质是做生意、要算账）、「壁垒在 AI 之外」（AI 应用的壁垒在技术之外 — 更懂用户 / 更懂产品 / 渠道）、勇于承认没壁垒（AI 应用创业者别忽悠技术壁垒）、硬指标导向（付费意愿 / 销售周期 / 留存率）、快进快出（商业路径不清就批量退出）、中国机会在应用端。
- **voice_samples**:
  - 同业讨论样本（对创业者讲 AI 应用的壁垒）: 「今天的 AI 应用创业者要勇于承认自己没有壁垒 —— 有任何技术壁垒都是骗人的、都是忽悠人的。所有应用都是靠底层模型提供能力，壁垒只能建在 AI 之外。」(source: T01-S025, 转述 — 财联社 / 证券时报访谈，接近原话)
  - 客户解释样本（对创业者讲投资判断标准）: 「创业的本质依然是做生意，要算账 —— 我关注的是你能不能商业化、谁来付钱、销售周期多长、留存率怎么样。」(source: T01-S025, 转述 — 多篇访谈一致表述)
  - 监管 / 行业样本（公开谈具身智能 / 减仓决策）: 「具身智能现在特别火，但我觉得商业路径还是不清，尤其是人形机器人 —— 我们正批量退出人形机器人公司。」(source: T01-S021, 转述 — 投中网，接近原话)
- **sub_skill_candidate**: `true` — 虽无长著作，但公开访谈密度高、且内容直接是「deal 判断方法论」（商业化第一原则、硬指标导向），在国内互联网早期投资影响力前 5，与「早期投资判断」focus 高度对齐；可调研性的限制是「需多篇短访谈拼合」而非单一长素材。
- **dual_role**:（无 —— 职业 VC，但「敢公开真实减仓决策」使其公开内容比多数同行更接近实际工作）
- **最近 12 个月动态**: 2025 年 3 月公开表态「批量退出人形机器人公司」，引发创投圈关于「具身智能是否过热」的大讨论，也招致「只投 400 万、过河拆桥」的反弹；2024-2025 持续输出「AI 应用为王、壁垒在 AI 之外、中国机会在应用端」的判断，是当下国内 VC 中最 active 的公开发声者之一。
- **争议 / 批评**: ① 「批量退出人形机器人」被批短视 / 不够 patient capital，与「VC 应陪长期硬科技」的主张冲突；② 「快进快出、算账优先」风格被指更适合互联网模式创新，对需要长周期的 deep tech 可能系统性低配；③ ofo 等项目的失败也常被用来质疑其判断的稳定性；④ 高频公开发声本身被部分同行视为「带节奏 / 影响赛道估值」。
- **来源**:
  - [Primary] 投中网朱啸虎访谈「批量退出人形机器人」（其本人公开表态）: https://m.chinaventure.com.cn/news/80-20250328-385692.html, collected 2026-05-14
  - [Secondary] 财联社《朱啸虎：中国 AI 的爆发点在应用场景端》: https://www.cls.cn/detail/1991592
  - [Reference] 证券时报《朱啸虎：AI 应用创业者要勇于承认自己没有壁垒》: https://stcn.com/article/detail/1628298.html
- **可信度自评**: high — 公开访谈密度高、时效性强（2025 最新表态）、内容直接是 deal 方法论；唯一限制是无单一长素材，靠多篇拼合。

### 13. 李开复 / Kai-Fu Lee

- **One-liner**: 创新工场董事长兼 CEO，中国 AI 早期投资 + 孵化派代表 —— 技术背景出身的投资人（前 Google/微软高管 + AI 研究者），主张「VC + 孵化」双轮，并在 AI 2.0 浪潮中亲自下场创办零一万物。
- **核心身份**: 创新工场（Sinovation Ventures）董事长兼 CEO；零一万物（01.AI）创始人兼 CEO（2023 创办）；前 Google 大中华区总裁、前微软全球副总裁、卡内基梅隆 AI 博士。
- **代表作品**: ① 创新工场的「VC + 孵化」模式（早期投资 + 自建项目，AI Institute 输出技术与团队）；②《AI 未来》(AI Superpowers, 2018) —— 中美 AI 竞争的畅销著作；③ 零一万物 Yi 系列大模型（亲自下场做 AI 2.0 平台）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 创新工场官博《李开复筹组新公司定名零一万物 — 打造 AI 2.0 全新平台》https://www.chuangxin.com/blog/ai2-0-agi（一手立论）；另有《AI 未来》(2018) 著作
  - 🎙️ 新浪财经《从创新工场到零一万物：李开复的 AI 转型与全球野心》https://finance.sina.com.cn/money/bond/2024-08-01/doc-inchcxfw2727367.shtml
  - 🎬 大量公开 keynote（TED、达沃斯、各 AI 大会）—— 李开复是国内 figure 中演讲材料最丰富的之一
- **核心思想关键词**: AI 2.0（以大模型为突破、贯穿技术-平台-应用的革命）、「比移动互联网大十倍的平台机会」、VC + 孵化双轮（投资 + 自建）、技术背景投资人（懂技术才判得准 AI deal）、中美 AI 竞争格局、AI-first 应用生态。
- **voice_samples**:
  - 监管 / 行业宏观样本（公开谈 AI 2.0 的判断）: 「以大语言模型为突破的 AI 2.0 正在掀起技术、平台到应用多个层面的革命 —— AI 2.0 时代将诞生比移动互联网大十倍的平台机会。」(source: T01-S022, 转述 — 创新工场官博，接近原话)
  - 客户解释样本（对创业者 / 生态讲机会在哪）: 「大模型公司的多元化会催生一波从 AI 2.0 模型、到 AI 2.0 基础设施、到 AI 2.0 全新应用的创新生态 —— 一旦中国有了真正原生、高质量的大模型，高质量有创意的应用会百花齐放。」(source: T01-S022, 转述)
  - 同业讨论样本（讲为何亲自下场）: 「零一即 01，代表数字世界，从零到一乃至宇宙万物 —— 寓意『零一智能，万物赋能』。」李开复从「投资人」转为「亲自带队创办」，本身是其判断「AI 2.0 是十年级机会」的最强信号。(source: T01-S027, 转述+推断 — 新浪财经报道)
- **sub_skill_candidate**: `true` — 有著作 +《AI 未来》+ 海量 keynote 长视频、思想体系自洽（AI 2.0 + VC/孵化双轮 + 技术背景判断）、国内 AI 早期投资影响力前 5，与「早期投资判断」focus 对齐。注意：其重心 2023 后部分转向「创业者」（零一万物），Phase 2 提炼时「投资人」与「创业者」两个身份要区分。
- **dual_role**: `"researcher + investor + founder"` —— AI 研究者 + VC + （2023 起）大模型创业者，三重身份叠加。
- **最近 12 个月动态**: 2024-2025 重心明显在零一万物 —— 2024 年 5 月发布千亿参数 Yi-Large 闭源模型（LMSYS 一度与 GPT-4o 并列）；同时创新工场持续在 AI 赛道投资 / 孵化；2024 下半年零一万物战略有调整（外媒报道其收缩预训练、转向应用与商业化），反映 AI 2.0 创业的现实压力。
- **争议 / 批评**: ① 「VC + 孵化」双轮被质疑利益冲突 —— 既当裁判（投资人）又当运动员（自建项目 / 零一万物）；② 零一万物 2024 的战略收缩被部分人解读为「李开复对 AI 2.0 机会判断过于乐观」的回调；③ 高频上 keynote、出畅销书，与朱啸虎类似，也面临「公开 IP ≠ 投资业绩」的质疑；④ 创新工场早期 AI 项目的实际退出回报透明度有限。
- **来源**:
  - [Primary] 创新工场官博《零一万物 — 打造 AI 2.0 全新平台》（其本人 / 机构发布）: https://www.chuangxin.com/blog/ai2-0-agi, collected 2026-05-14
  - [Secondary] 新浪财经《从创新工场到零一万物：李开复的 AI 转型与全球野心》: https://finance.sina.com.cn/money/bond/2024-08-01/doc-inchcxfw2727367.shtml
  - [Reference] 界面新闻《李开复最快独角兽诞生：零一万物估值超 70 亿》: https://www.jiemian.com/article/10346783.html
- **可信度自评**: high — 一手机构博客 + 著作 + 海量 keynote，长素材充足；唯一注意点是 2023 后身份从「投资人」向「创业者」偏移。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 figures 都谈到的关键词（候选行业心智模型）

- **市场 / 赛道决定论**（market wins）— 「市场 > 团队 > 产品」「与伟大格局观者同行」「赛道商业化第一原则」 (出现于 figures: Marc Andreessen / 张磊 / 朱啸虎；evidence: [T01-S004, T01-S020, T01-S025])
- **power-law / 非对称收益**— 「最多亏 1 倍、可能赚 50 倍」「高失败率 + 充分分散」「头部 1-2 个 deal 决定 fund return」 (出现于 figures: Vinod Khosla / Bill Gurley / Marc Andreessen；evidence: [T01-S016, T01-S002, T01-S005])
- **conviction 集中度 vs 广撒网**（流派核心分歧，见下）— 几乎每个 figure 都被迫站队 (出现于 figures: Bill Gurley / Paul Graham / Vinod Khosla / 朱啸虎；evidence: [T01-S002, T01-S003, T01-S016, T01-S021])
- **thesis-driven / 主题先行**— 「先写 15-20 页白皮书」「AI 2.0 是十倍机会」「contrarian 才造革命公司」 (出现于 figures: Fred Wilson / 李开复 / Vinod Khosla；evidence: [T01-S013, T01-S022, T01-S010])
- **投后即产品 / venture assistance**— 「a16z 平台化」「CEO 三件事」「venture assistance 主动装能力」「founder-CEO 优先」 (出现于 figures: Marc Andreessen / Fred Wilson / Vinod Khosla / Ben Horowitz；evidence: [T01-S005, T01-S001, T01-S010, T01-S018])
- **founder 判断 / founder-CEO 优先**— 「押 founder 格局」「founder-CEO 优先」「operator-investor」 (出现于 figures: Ben Horowitz / 张磊 / Reid Hoffman；evidence: [T01-S018, T01-S020, T01-S013])
- **单位经济学纪律 / 算账**— 「LTV 公式的危险」「不是所有收入生而平等」「要算账、看付费意愿和留存」 (出现于 figures: Bill Gurley / 朱啸虎；evidence: [T01-S002, T01-S025]) — 仅 2 源但极硬，建议 Phase 2 与 Track 04 canon 交叉补强
- **周期意识 / 速度 vs 效率**— 「blitzscaling」「bear market blitzscaling」「估值周期 pattern recognition」「快进快出」 (出现于 figures: Reid Hoffman / Bill Gurley / 朱啸虎；evidence: [T01-S028, T01-S002, T01-S021])
- **长期主义 / 复利 / 时间**— 「做时间的朋友」「stewardship 留给下一代」「长期持有」 (出现于 figures: 张磊 / Doug Leone / Fred Wilson；evidence: [T01-S020, T01-S007, T01-S013])

### 显著分歧 / 流派分裂

1. **Concentrated 高 conviction 派**（少投、重投、深度参与；代表: Bill Gurley / Benchmark、Doug Leone / Sequoia 老一辈）**vs Spray-and-pray 加速器派**（广撒网、标准化 terms、batch + 教育；代表: Paul Graham / YC、部分 All-In 天使风格）。这是本行业最根本的方法论分歧 —— 同一个早期 deal，两派给完全相反的「该不该投、投多少、投后管多深」答案。
2. **平台化大基金派**（multi-strategy、大投后军队、AUM 规模；代表: Marc Andreessen + Ben Horowitz / a16z）**vs 平等合伙小基金派**（small & flat、经济与决策权平分、拒绝规模化；代表: Bill Gurley / Benchmark）。分歧点在「VC 的规模化是进步还是摊薄 carry 意义」。
3. **Thesis-driven 主题先行派**（先写白皮书 / 锁定赛道；代表: Fred Wilson / USV、Vinod Khosla deep tech、李开复 AINative）**vs 机会驱动 / founder 驱动派**（不预设主题，跟着最强 founder 走；代表: Sequoia 老一辈的「市场聚焦 + 创始人优先」更偏后者）。
4. **operator-investor 派**（用运营 / 创业经验做投资判断；代表: Reid Hoffman、Ben Horowitz、雷军式、李开复技术背景）**vs analyst-investor 派**（用研究 / 估值 / 数据纪律做判断；代表: Bill Gurley 华尔街研究员出身、Mary Meeker 卖方分析师出身）。
5. **公开品牌化派**（VC 即媒体 IP；代表: All-In 四人组、朱啸虎高频发声、李开复 keynote）**vs 安静派**（不做个人品牌、靠机构与口碑；代表: Doug Leone / Michael Moritz、相对低调的张磊）。**这条分裂特别重要** —— intake warning #2/#6 明确指出「公开形象 ≠ 投资能力」，Phase 2 必须把「公开多 ≠ 投得好」写进诚实边界，All-In 群体是最佳反面教材。
6. **海外 vs 国内路径分裂**（不是流派而是结构差异）：海外（a16z / YC / Benchmark / Sequoia / USV / Greylock）退出靠 IPO / M&A、生态成熟、长博客 / podcast 沉淀厚；国内（张磊 / 朱啸虎 / 李开复）面对 RMB 退出难 + 中美脱钩 + IPO 收紧，公开内容更碎片化、长素材稀缺，且更多 figure 本身是「创业者-投资人」双身份（雷军、李开复）。Phase 2 必须按 locale 分章。

### 冷僻领域信号 — 结论：本 track 不冷僻，但有结构性偏斜

- 总 figure 数：retain 13（远超 floor 10）→ **不触发冷僻协议**。
- 长访谈材料 < 30 min 的 figure 比例：约 3/13（Mary Meeker、Doug Leone/Moritz 已退出、All-In 群体的「方法论」素材）—— 低于 30% 阈值，可接受。
- 标「可信度 low」的 figure 比例：0/13（最低为 medium）—— 不触发。
- **但有三个结构性偏斜，Phase 2 必须在「诚实边界」节明示**：
  1. **海外厚、国内薄**：海外 10 张卡（8 张独立卡 = Marc Andreessen / Ben Horowitz / Bill Gurley / Fred Wilson / Paul Graham / Reid Hoffman / Vinod Khosla / Mary Meeker，+ Doug Leone & Michael Moritz 合 1 张，+ All-In 四人组合 1 张）一手长素材普遍充足；国内仅 3 张（张磊 / 朱啸虎 / 李开复）retain，**沈南鹏、徐小平、雷军、阎焱因公开长素材不足未 retain**（沈南鹏 / 徐小平降为名片型 manifest 条目 S019/S023）。国内 VC 的真实方法论沉淀在闭门场合，公开可得的远薄于海外。
  2. **manifest 一手占比天然偏低**：按 GLOBAL 行业规则，作者裸域博客（avc.com / abovethecrowd.com / paulgraham.com）+ VC firm 官网 + Substack/Medium 一律判 `secondary`，本 track manifest 28 条中仅 4 条 `verified_primary`（2 条 Acquired episode + 豆瓣《价值》书页 + 创新工场官博）+ 4 条 `surrogate_primary`（a16z 官网 / Sequoia 官网 / YC Library / Stanford GSB，均标 vendor docs / syllabus）。**这不是调研不力，是行业内容分发的结构性特征** —— Phase 4 item 13（URL 一手机械验证 ≥ 50%）对本行业应按 GLOBAL 规则放宽理解，「内容一手性」≠「verifier bucket」。
  3. **「公开内容 vs 实际工作」gap 是本行业头号陷阱**：intake warning #2 反复强调。多数 figure 的公开输出（博客 / podcast / 著作）是给 LP 看的市场推广或个人品牌，不是 deal team 真实工作。Phase 2 蒸馏 mental model 时，要优先采用「figure 谈具体判断标准 / 具体陷阱」的样本（如 Gurley 的 LTV 陷阱、朱啸虎的硬指标、Wilson 的 CEO 三件事），而非「figure 谈宏大叙事」的样本。

### 给其他 Track 的反馈信号

- → **Track 04 (canon)**：figures 高频指向的一手文本已识别 ——《The Hard Thing About Hard Things》(Horowitz)、《Blitzscaling》(Hoffman)、《价值》(张磊)、Gurley《Above the Crowd》名篇（On the Road to Recap / LTV Formula / All Revenue Is Not Created Equal）、Andreessen《The Only Thing That Matters》、PG essays（How to Get Startup Ideas 等）、Wilson AVC.com（What A CEO Does）。建议 canon track 优先收。
- → **Track 05 (sources)**：figures 常驻 / 自办的 podcast 已识别 —— Acquired（深度公司史）、All-In、Masters of Scale（Hoffman 自办）、Invest Like the Best（Doug Leone 等访谈）、Moonfare Deal Talk；国内投中网 / 财联社 / 澎湃是国内 figure 公开发声的主要载体。
- → **Track 06 (academic)**：Stanford 出现两次（CS183B《How to Start a Startup》、《Blitzscaling》CS183C / Stanford GSB 案例库），Stanford 是 VC 学术 + 业界结合的枢纽，建议 academic track 以 Stanford GSB / CS183 系列为锚。
- **矛盾保留**：本 track 未深入 Track 02 工具，若工具 track 发现某关键工具的开发者是重要 figure 而本 track 未收，留给 Phase 1.5 裁决。

---

**调研收口**：20 候选撒网（海外 12 + 国内 8），retain 13（海外 10 = 8 张独立卡 + Moritz/Leone 合 1 张 + All-In 群体合 1 张；国内 3 = 张磊/朱啸虎/李开复）。未 retain：沈南鹏 / 徐小平 / 雷军 / 阎焱（公开长素材不足，沈/徐降为 manifest 名片条目）、Sam Altman（已转 OpenAI CEO，VC 身份非当前主业）。Manifest 28 条（verified_primary 4 / surrogate_primary 4 / secondary 20 / blacklisted 0）。一手内容占比按「实际作者一手文本」算约 75%（多数 secondary bucket 实为作者裸域博客 / 本人著作 / 本人机构博客，是 GLOBAL 行业内容分发特征所致），按 verifier bucket 机械算 verified+surrogate = 8/28 ≈ 29%。无黑名单 URL。可信度分布：high 9 / medium 4 / low 0。
