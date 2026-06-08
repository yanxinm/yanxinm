# Track 06 — Glossary（术语 + 标准 + 法规）— 风险投资人 / 早期投资人(VC investor)

> Phase 1 wave 1 第 3 路 subagent 输出。行业:Venture Capital — GP / Partner / Principal 视角。locale=`global`,profile=`practitioner`。
> 输出供 Phase 2 整合进生成 skill 的 [Glossary] 节 + 「行业表达 DNA」节(outsider-tell 提取)。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.sec.gov/education/capitalraising/building-blocks/accredited-investor | verified_primary | 2026-05-14 | SEC | accredited investor 官方定义 + 2020 修订 |
| T06-S002 | https://www.sec.gov/resources-small-businesses/exempt-offerings/regulation-d-offerings | verified_primary | 2026-05-14 | SEC | Reg D 506(b)/506(c) 豁免发行官方页 |
| T06-S003 | https://www.sec.gov/files/rules/final/2020/33-10824.pdf | verified_primary | 2026-05-14 | SEC | 2020-08 accredited investor 定义修订终稿 33-10824 |
| T06-S004 | https://www.law.cornell.edu/uscode/text/26/1202 | verified_primary | 2026-05-14 | Cornell LII | 26 USC §1202 QSBS 法条原文(立法机构原文镜像) |
| T06-S005 | https://www.npc.gov.cn/ | verified_primary | 2026-05-14 | 全国人大 | 中国立法机构原文站 |
| T06-S006 | https://www.gov.cn/zhengce/content/202307/content_6892836.htm | verified_primary | 2026-05-14 | 国务院 | 《私募投资基金监督管理条例》2023 国务院令 |
| T06-S007 | https://www.csrc.gov.cn/ | verified_primary | 2026-05-14 | 证监会 | 私募基金监管主管机关 |
| T06-S008 | https://www.amac.org.cn/ | verified_primary | 2026-05-14 | 中基协(AMAC) | 私募基金备案 / 自律管理机构(法定授权) |
| T06-S009 | https://ilpa.org/ | surrogate_primary | 2026-05-14 | ILPA | 行业协会 — LP 利益代表组织 |
| T06-S010 | https://ilpa.org/reporting-template/ | surrogate_primary | 2026-05-14 | ILPA | 行业协会 — Reporting Template 标准 |
| T06-S011 | https://nvca.org/ | surrogate_primary | 2026-05-14 | NVCA | 行业协会 — 美国 VC 行业协会 + 标准 term sheet 文件 |
| T06-S012 | https://www.ycombinator.com/documents | surrogate_primary | 2026-05-14 | Y Combinator | SAFE 原创发行方 — 标准 SAFE 文档(vendor docs) |
| T06-S013 | https://carta.com/learn/ | surrogate_primary | 2026-05-14 | Carta | vendor docs — cap table / 估值术语 |
| T06-S014 | https://en.wikipedia.org/wiki/Carried_interest | secondary | 2026-05-14 | — | carried interest 入门定义 |
| T06-S015 | https://en.wikipedia.org/wiki/SAFE_(financial_instrument) | secondary | 2026-05-14 | — | SAFE 入门定义 |
| T06-S016 | https://www.investopedia.com/terms/p/pre-moneyvaluation.asp | secondary | 2026-05-14 | Investopedia | pre/post-money 入门定义 |
| T06-S017 | https://corpgov.law.harvard.edu/ | verified_primary | 2026-05-14 | Harvard Law School Forum | 法学院公司治理论坛 — VC term / 法规长稿 |
| T06-S018 | https://www.sec.gov/files/exploring-accredited-investors-june-2025.pdf | verified_primary | 2026-05-14 | SEC | 2025-06 SEC staff report — accredited investor 现状数据 |
| T06-S019 | https://ilpa.org/resources-tools/resource-library/ilpa-reporting-template-v-2-0/ | surrogate_primary | 2026-05-14 | ILPA | 行业协会 — Reporting Template v2.0(2025-01 发布) |
| T06-S020 | https://www.thetaxadviser.com/issues/2025/nov/qsbs-gets-a-makeover-what-tax-pros-need-to-know-about-sec-1202s-new-look/ | secondary | 2026-05-14 | The Tax Adviser (AICPA) | QSBS OBBBA 2025 修订解读 |
| T06-S021 | https://www.amac.org.cn/businessservices/businessguidelines/ | verified_primary | 2026-05-14 | 中基协(AMAC) | 私募基金登记备案办法 / 自律规则 |

---

## Tier 1 — 核心必懂术语(目标 30-50)

> 入行第一周必须秒懂的词。VC 黑话密度极高,Tier 1 集中在「基金经济学 + deal 结构 + 投资判断」三类。

### 1. Power law — 幂律

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: VC 回报分布的根本规律 —— 一支基金的绝大部分回报(常说 80%+)来自 1-2 个 outlier deal,其余多数 deal 回本或归零;因此投资逻辑是「不怕投错,怕错过」(can't lose more than 1x, can make 100x)。
- **Definition (outsider-friendly)**: 风投赚钱不是靠「平均每个项目小赚」,而是靠极少数项目赚到几十上百倍,覆盖掉一大堆亏损。
- **Etymology**: 数学中的幂律分布;Sebastian Mallaby 2022 年 VC 行业史书名即《The Power Law》。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行说「分散投资降低风险」—— 内行知道在 power law 里过度分散反而稀释掉 outlier 的影响,真正的风险是 portfolio 里没有一个 fund-returner。
  - `usage_tell`: 外行把它当「二八定律」泛泛而谈;内行用它推导出具体的 portfolio construction(check size / reserve / 集中度)和「miss 比 loss 更致命」的决策准则。
- **关联术语**: fund-returner、anti-portfolio、portfolio construction、outlier
- **是否被错位包装**: 未见显著厂商收编 —— 这是行业共识概念而非产品概念。
- **可信度**: high / **Decay risk**: low

### 2. Carry / carried interest — 附带权益(业绩分成)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: GP 从基金利润中分到的比例,行业标准 20%(头部基金可到 25-30%),通常在 LP 收回本金(有时还要过 hurdle / preferred return)之后才开始计提;是 GP 真正的「上行收入」,但兑现要等基金生命周期 7-10 年。
- **Definition (outsider-friendly)**: 基金赚钱后,管理人能分走的那部分利润(典型 20%),不是工资,要等很多年项目退出了才拿得到。
- **Etymology**: 源自中世纪地中海航运的「commenda」利润分成;现代 PE/VC 沿用 "carried interest"。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 carry 是 GP 的主要日常收入 —— 内行知道日常工资来自 management fee,carry 是「期权」性质,且很多基金 7-10 年都没等到 carry。
  - `pronunciation_tell`: 行内只说 "carry",几乎不说全称 "carried interest";开口说全称的多半是外人或律师。
  - `usage_tell`: 外行混淆 carry 和 GP commitment(carry 是「分利润」,GP commitment 是「自己掏钱投进基金」)。
- **关联术语**: management fee、hurdle rate / preferred return、GP commitment、waterfall / distribution waterfall、vesting
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high(evidence: [T06-S014]) / **Decay risk**: low

### 3. Management fee — 管理费

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: GP 每年从基金规模中收取的运营费,行业标准 2%/年(投资期按 committed capital,投资期后常 step-down 到按 invested/NAV);是 GP 的「确定性工资来源」,也是「2 and 20」里的 2。
- **Definition (outsider-friendly)**: 不管投得好不好,管理人每年都能从基金总额里收取的固定费用(典型 2%),用来发工资、付办公室。
- **Etymology**: 私募基金 "2 and 20" 费率结构的「2」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为「2% 不多」—— 内行算的是 10 年累计(2%×10≈20% 的基金规模被费用吃掉),且这是旱涝保收的部分,LP 对 fee 极度敏感。
  - `usage_tell`: 外行说「VC 靠管理费就能躺赚」忽略了大基金才有规模效应,小基金 2% 根本养不活团队。
- **关联术语**: carry、2 and 20、committed capital、step-down、fee offset
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 4. GP / LP — General Partner / Limited Partner(普通合伙人 / 有限合伙人)

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: GP = 管理基金、做投资决策、承担无限责任的一方(就是「VC 本人 / VC 机构」);LP = 出钱的人(养老金、捐赠基金、family office、FoF、主权基金等),只承担出资额内的有限责任,不参与投资决策。
- **Definition (outsider-friendly)**: GP 是「管钱投项目的人」,LP 是「把钱交给 GP 的金主」。
- **Etymology**: 美国 Limited Partnership(有限合伙)法律结构的两类合伙人;VC 基金几乎都用 LP 结构设立。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「VC」当成一个人;内行清楚 VC 是一个 GP-LP 双层结构,GP 自己也要向 LP「募资 + 汇报 + 被考核」。
  - `usage_tell`: 外行说「VC 的钱」—— 内行知道那是 LP 的钱,GP 只是受托管理(fiduciary duty)。
  - `register_tell`: 把 LP 简单等同于「投资人」会让对方觉得你没分清 GP/LP/founder 三层。
- **关联术语**: capital call、commitment、fund-of-funds、fiduciary duty、GP commitment
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 5. DPI / TVPI / IRR / MOIC — 基金回报四件套

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: 衡量基金业绩的核心指标。**DPI**(Distributions to Paid-In)= 已分配现金 / LP 实缴,"现金回家了多少",LP 最认。**TVPI**(Total Value to Paid-In)= (已分配 + 账面剩余价值)/ 实缴,含未退出部分。**MOIC**(Multiple on Invested Capital)= 总价值 / 投入,倍数口径。**IRR**(Internal Rate of Return)= 年化内部收益率,考虑时间价值,但易被早期 markup 和 capital call 节奏操纵。
- **Definition (outsider-friendly)**: 一组判断基金赚没赚钱的指标 —— 有的看「实际拿回多少现金」,有的看「账面值多少」,有的看「年化收益率」。
- **Etymology**: 私募基金标准业绩口径,ILPA 等机构在 reporting 标准中统一定义。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行只看 IRR 高就觉得基金牛 —— 内行知道 "IRR 是 paper,DPI 才是 real",一支 IRR 漂亮但 DPI 低的基金可能只是 markup 好看、没真退出。
  - `pronunciation_tell`: TVPI 念 "T-V-P-I",MOIC 多念 "mo-ick" 一个词;DPI 念字母。
  - `usage_tell`: 外行把 TVPI 和 DPI 混用 —— 内行强调 "TVPI - DPI = 还没落袋的部分",成熟基金最终 TVPI 会收敛到 DPI。
- **关联术语**: markup、vintage year、J-curve、NAV、ILPA Reporting Template
- **是否被错位包装**: Carta / 各 fund admin 工具会把指标做成 dashboard,但定义本身未被收编。
- **可信度**: high(evidence: [T06-S019]) / **Decay risk**: low

### 6. Pre-money vs post-money valuation — 投前估值 vs 投后估值

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: post-money = pre-money + 本轮新投入金额;投资人拿到的股权比例 = 投资额 / post-money。是 term sheet 谈判第一性参数 —— founder 习惯报 pre-money,investor 心里算 post-money 和自己的 ownership %。
- **Definition (outsider-friendly)**: 投前估值是「投钱之前公司值多少」,投后估值是「投钱之后公司值多少」,两者差额就是这轮投进去的钱。
- **Etymology**: 股权融资标准概念。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行(和很多 founder)说「估值 1000 万」却不指明 pre 还是 post —— 内行第一反应必问 "pre or post?",因为同一个数字 pre/post 对应的稀释完全不同。
  - `usage_tell`: SAFE / 可转债时代尤其坑:post-money SAFE 的「估值上限」是 post 口径,founder 容易低估累积稀释。
- **关联术语**: dilution、cap table、SAFE、option pool shuffle、ownership %
- **是否被错位包装**: 未见厂商收编(但 SAFE 文档版本变化影响理解,见 SAFE 条)。
- **可信度**: high(evidence: [T06-S016]) / **Decay risk**: low

### 7. SAFE — Simple Agreement for Future Equity(未来股权简单协议)

- **Type**: term + acronym + standard
- **Tier**: tier-1
- **Definition (insider)**: YC 2013 年发明、2018 年改为 post-money 版本的早期融资工具 —— 不是债(无利息、无到期日),而是「未来某轮股权融资 / 退出时按 cap 或 discount 转股」的权利凭证;美国种子轮事实标准,因为快、便宜、不用定价。
- **Definition (outsider-friendly)**: 一份「现在给钱、以后再换成股份」的简易协议,创业者早期融资常用,不用马上谈估值。
- **Etymology**: Y Combinator 2013 推出取代可转债;2018 从 pre-money SAFE 改版为 post-money SAFE(YC 官方标准文档)。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 SAFE 当「可转债(convertible note)」—— 内行知道 SAFE 不是债务、没有利息和 maturity,法律和稀释逻辑都不同。
  - `pronunciation_tell`: 念 "safe"(像「安全」),不念字母 "S-A-F-E"。
  - `usage_tell`: 外行不分 pre-money / post-money SAFE —— 内行知道 post-money SAFE 把稀释风险更多压给 founder,且多个 SAFE 叠加时 "SAFE pile-up" 的累积稀释要专门建模。
- **关联术语**: convertible note、priced round、valuation cap、discount、pre/post-money、MFN clause
- **是否被错位包装**: SAFE 本身是 YC 的标准文档(非营利发布),但部分平台把「用我们的工具发 SAFE」包装成「标准化融资」,SAFE 文本本身仍是 YC 版本(evidence: [T06-S012, T06-S015])。
- **可信度**: high / **Decay risk**: low-medium(YC 偶尔更新模板)

### 8. Convertible note — 可转换债券(可转债)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 早期融资用的债权工具 —— 有利息、有到期日(maturity),在下一轮股权融资时按 valuation cap / discount 转为股权;在 SAFE 普及前是种子轮主流,现仍用于桥轮(bridge)和对债务条款敏感的场景。
- **Definition (outsider-friendly)**: 早期投资人先以「借钱」形式给钱,将来公司融资时这笔钱自动变成股份。
- **Etymology**: 传统可转债结构在创投早期融资的应用。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行和 SAFE 混为一谈 —— 内行强调 convertible note 是「真的债」,到期不转股理论上要还钱,公司清算时排在股权前面。
  - `usage_tell`: 外行忽略 maturity date 的杀伤力 —— 内行知道到期没融到下一轮会触发尴尬的展期 / 违约谈判。
- **关联术语**: SAFE、bridge round、valuation cap、discount、priced round、interest rate
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 9. Priced round — 定价轮(股权轮)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 真正确定每股价格、发行优先股、签完整 term sheet 的融资轮(对应 Seed priced / Series A/B/C…);相对 SAFE / convertible note 的「不定价」工具,priced round 要做完整法律文件、估值、cap table 重整。
- **Definition (outsider-friendly)**: 这一轮融资明确给公司定了价、确定了每股多少钱,投资人直接拿到股份(而不是「以后再转股」的凭证)。
- **Etymology**: 与 "unpriced"(SAFE/note)相对的行业用语。
- **常见误用 (outsider-tell)**:
  - `usage_tell`: 外行以为「Series A」就是金额大小 —— 内行知道关键差异是「priced(定价、发优先股、有 board)」vs「unpriced」,以及公司是否到了能撑起定价的成熟度。
  - `register_tell`: 把所有早期融资都叫 "round" 而不分 priced/unpriced,会显得不熟 deal 结构。
- **关联术语**: term sheet、preferred stock、SAFE、Series A、lead investor
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 10. Liquidation preference — 清算优先权

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 优先股投资人在公司清算 / 被收购 / 退出时,先于普通股拿回钱的权利;标准是 "1x non-participating"(先拿回 1 倍投资额,然后在「拿优先回报」和「按比例分」之间二选一)。倍数 >1x 或 "participating"(拿完优先额还参与分剩余)对 founder 更不利,是 term sheet 里仅次于估值的核心条款。
- **Definition (outsider-friendly)**: 公司卖掉或清算时,投资人有权先拿回自己的钱(甚至好几倍),剩下的才轮到创始人和员工。
- **Etymology**: 优先股(preferred stock)标准权利。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行只盯估值,忽略 liq pref —— 内行知道「高估值 + 2x participating preference」可能比「低估值 + 1x non-participating」对 founder 更差,exit 时谁先拿钱、拿多少全看这条。
  - `usage_tell`: 外行混淆 "participating" 和 "non-participating" —— 内行一听 "participating preferred" 就知道是「双重分钱(double dip)」,在 down exit 时极伤普通股。
- **关联术语**: participating preferred、preferred stock、down round、waterfall、cap table、preference stack
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 11. Anti-dilution — 反稀释条款(full ratchet / weighted average)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 当公司后续以更低价格融资(down round)时,保护早期优先股投资人的条款。**Full ratchet**:把早期投资人的转换价直接调到新低价(对 founder 最狠)。**Weighted average**(broad/narrow-based):按融资规模加权调整,行业主流、相对温和。
- **Definition (outsider-friendly)**: 如果公司之后以更低估值融资,这条款会自动给老投资人补偿股份,免得他们的股份「被稀释贬值」。
- **Etymology**: 优先股标准保护条款。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为反稀释「保护所有人」—— 内行知道它只保护拿了这条款的优先股投资人,补偿的股份恰恰来自 founder 和员工的进一步稀释。
  - `usage_tell`: 外行不分 full ratchet 和 weighted average —— 内行一看 full ratchet 就知道这是「掠夺性条款」,正常 deal 几乎都是 broad-based weighted average。
- **关联术语**: down round、liquidation preference、pay-to-play、weighted average、cap table
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 12. Pro-rata rights — 按比例跟投权

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 投资人在被投公司后续轮次中「按现有持股比例追加投资以维持 ownership %」的权利;是早期投资人锁定 winner 上行的关键工具,也是 reserve 资金的主要用途。
- **Definition (outsider-friendly)**: 投资人有权在公司下一轮融资时继续按比例投钱,这样股份比例不会被新投资人稀释掉。
- **Etymology**: term sheet / 投资人权利协议标准条款。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 pro-rata 是「义务」—— 内行知道它是「权利(option)」,而且在 power law 下「行使 winner 的 pro-rata」比首投更重要。
  - `usage_tell`: 外行忽略 "super pro-rata"(超比例)和 "pro-rata 被 cut" 的博弈 —— 在热门轮里 lead 可能不让小投资人行使 pro-rata。
- **关联术语**: follow-on、reserve、ownership %、power law、information rights、SPV
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 13. Cap table — 股权结构表(capitalization table)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 记录公司所有股权 / 期权 / SAFE / 可转债持有人及其比例的总表;尽调必查,因为 cap table「干不干净」(创始人股权是否合理、有没有僵尸股东、option pool 够不够)直接决定可投性。
- **Definition (outsider-friendly)**: 一张列出「公司股份归谁、各占多少」的表。
- **Etymology**: "capitalization table" 缩写;Carta 等工具把它软件化后成为日常词。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 cap table 就是「股东名单」—— 内行看的是 fully-diluted 口径(把所有期权、SAFE、可转债都转股后的真实比例)和「这张表健不健康」。
  - `usage_tell`: 外行说 "clean cap table" 当套话 —— 内行有具体红线:创始人股权过度稀释、早期天使占比畸高、大量 dead equity、option pool 不足都叫「不干净」。
- **关联术语**: fully-diluted、option pool、dilution、SAFE、Carta、dead equity
- **是否被错位包装**: Carta 把 cap table 管理软件化,营销中常把「Carta = cap table」绑定;但 cap table 是通用概念(evidence: [T06-S013])。
- **可信度**: high / **Decay risk**: low

### 14. Option pool / ESOP — 期权池 / 员工持股计划

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 预留给员工的股权激励池(美国常说 option pool,典型 10-20%);term sheet 谈判焦点之一,因为「pool 通常从 pre-money 里划」—— 即由 founder 单方稀释,所谓 "option pool shuffle",是投资人压实际估值的隐形手段。
- **Definition (outsider-friendly)**: 公司预留一批股份用来发给员工做激励;这批股份从哪里出、占多少,是融资谈判的关键点。
- **Etymology**: ESOP = Employee Stock Ownership Plan;VC 语境多指期权池。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 option pool 是「公司额外发的股份」—— 内行知道 pool 放在 pre-money 意味着 founder 被额外稀释,这是「真实 pre-money 比报价低」的关键调整项。
  - `usage_tell`: 外行把美国 option pool 和中国「员工持股平台 / 期权」直接等同 —— 内行知道两地法律结构、税务、行权机制差异很大。
- **关联术语**: option pool shuffle、pre-money valuation、dilution、cap table、vesting、ESOP
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 15. Term sheet — 投资条款清单

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 投资人发给公司的「不具法律约束力的」核心条款摘要(估值、金额、liq pref、board、protective provisions、pro-rata 等),签了 term sheet 才进正式法律文件和最终尽调;NVCA 发布有行业 model term sheet。
- **Definition (outsider-friendly)**: 投资人和公司就「这笔投资怎么投」达成的一页纸要点清单,后面才据此签正式合同。
- **Etymology**: 行业标准文件;NVCA(美国 VC 协会)维护 model 版本。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为签了 term sheet 钱就到账 —— 内行知道 term sheet 多数条款 non-binding,真正约束的常只有 exclusivity / no-shop 和保密,后面还有 confirmatory diligence 能黄。
  - `usage_tell`: 外行只看「估值 + 金额」两个数 —— 内行知道 control terms(board 构成、protective provisions)和 economic terms(liq pref、anti-dilution)同样决定 deal 好坏。
- **关联术语**: liquidation preference、board seat、protective provisions、no-shop、NVCA model documents、definitive agreements
- **是否被错位包装**: 未见厂商收编(NVCA model docs 是协会标准,evidence: [T06-S011])。
- **可信度**: high / **Decay risk**: low

### 16. Board seat / board observer — 董事席位 / 董事观察员

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 投资人在被投公司董事会的正式席位(有投票权、有 fiduciary duty)或观察员席位(列席、看材料、无投票权);board 构成(founder / investor / independent 各几席)是 control 条款核心,决定关键决策(融资、卖公司、换 CEO)谁说了算。
- **Definition (outsider-friendly)**: 投资人在公司董事会里的位子 —— 有的是正式董事(能投票),有的只是观察员(能旁听但不投票)。
- **Etymology**: 公司治理标准结构。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 board seat 就是「话语权大」—— 内行知道 board member 对公司(全体股东)负有 fiduciary duty,不能只代表自家基金利益,这与「投资人立场」常有张力。
  - `usage_tell`: 外行混淆 board seat 和 board observer —— 内行清楚 observer 是「信息权」不是「控制权」,seed 阶段投资人很多只拿 observer。
- **关联术语**: protective provisions、fiduciary duty、information rights、control terms、independent director
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 17. Down round / bridge round — 折价轮 / 过桥轮

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: **Down round** = 后一轮估值低于前一轮,触发反稀释、打击士气、稀释 founder。**Bridge round** = 在两轮正式融资之间的小额过桥融资(常用 SAFE / note),给公司续命到下一个里程碑;2022-2024 寒冬期两者都大量出现。
- **Definition (outsider-friendly)**: down round 是「这轮估值比上一轮还低」的融资;bridge round 是「在两次大融资之间补一笔小钱续命」。
- **Etymology**: 行业周期用语,2022 年后高频。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行觉得 down round = 公司要完 —— 内行知道寒冬期 down round 常态化,关键看「桥到哪里」、有没有 inside-led、structure 多狠。
  - `usage_tell`: 外行把所有「续命融资」都叫 bridge —— 内行区分 "bridge to round"(桥到下一轮)和 "bridge to nowhere"(没有明确终点的桥,危险信号)。
- **关联术语**: anti-dilution、recap、cram-down、structured round、inside round、runway
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: medium(用语随周期热度变化)

### 18. Deal flow / deal sourcing — 项目流 / 项目源

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: deal flow = 一个投资人 / 基金能看到的项目数量与质量;deal sourcing = 主动获取项目的方法(network、inbound、outbound、scout、accelerator funnel、AI 工具)。"proprietary deal flow"(别人看不到的独家项目流)被认为是基金的核心 alpha 来源之一。
- **Definition (outsider-friendly)**: deal flow 是「投资人手上有多少项目可看」,deal sourcing 是「怎么找到这些项目」。
- **Etymology**: 行业核心运营用语。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为「看的项目越多越好」—— 内行知道 deal flow 是「量 × 质」,而且最稀缺的是 "access"(能不能挤进顶级 founder 的那一轮)而非单纯数量。
  - `usage_tell`: 外行把 deal sourcing 当「销售线索」—— 内行知道顶级 deal 是「被 founder 选」而不是「投资人挑」,sourcing 一半是 sourcing、一半是 winning。
- **关联术语**: proprietary deal flow、access、scout、inbound/outbound、conviction、winning the deal
- **是否被错位包装**: AI sourcing 工具厂商(Glasswing 等)倾向把「用我们的工具 = 有 deal flow」包装化;内行强调 sourcing ≠ winning。
- **可信度**: high / **Decay risk**: low

### 19. Due diligence (DD) — 尽职调查(尽调)

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 投资前对一家公司的系统性核查 —— 早期 VC 的 DD 重点是 founder(reference call)、market(TAM、时机)、product、competition、cap table 干净度、关键法律风险;早期 DD 「轻」(信息少、靠判断),晚期 DD 「重」(财务、法律、商业全面铺开)。
- **Definition (outsider-friendly)**: 投资人在掏钱前对公司做的背景核查 —— 查团队、查市场、查产品、查法律。
- **Etymology**: 源自美国证券法 "due diligence defense";泛化为投资核查流程。
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 行内常缩成 "DD" 或 "diligence",很少念全 "due diligence"。
  - `semantic_tell`: 外行以为 DD 是「查账」—— 内行知道早期 VC 的 DD 70% 是 founder judgment 和 market call,财务尽调反而最轻(种子期没多少财务可查)。
  - `usage_tell`: 外行把 "reference call"(背调电话)当可有可无 —— 内行视其为早期 DD 的核心,且讲究做 "off-list references"(绕开 founder 给的名单)。
- **关联术语**: reference call、confirmatory diligence、founder-market fit、red flag、conviction
- **是否被错位包装**: expert call network 厂商(Tegus / AlphaSense / GLG)把「专家访谈 = diligence」包装化;内行知道 expert call 只是 DD 的一块。
- **可信度**: high / **Decay risk**: low

### 20. Thesis-driven investing — 主题驱动投资 / 投资主题

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 基金事先形成对某个 sector / stage / 技术趋势的明确观点(thesis),并据此主动筛选和争取 deal,而非被动 react;USV、a16z 是代表。与之相对的是 "spray-and-pray"(广撒网)和纯机会主义。
- **Definition (outsider-friendly)**: 投资机构先想清楚「我看好哪个方向、为什么」,再围绕这个判断去找项目,而不是什么火投什么。
- **Etymology**: Fred Wilson(USV)等长期博客推广的概念。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 thesis 当「投资标准清单」—— 内行知道 thesis 是一个有因果结构的「关于世界会怎么变」的论断,而且要能被证伪、会演化。
  - `usage_tell`: 外行说「我的 thesis 是投好团队」—— 内行会觉得这不是 thesis(太泛),真正的 thesis 是有具体方向和时间窗的判断。
  - `register_tell`: 滥用 "thesis" 一词(每个 deal 都说有 thesis)在行内会显得是 buzzword 堆砌。
- **关联术语**: spray-and-pray、sector focus、conviction、anti-thesis、pattern matching
- **是否被错位包装**: 未见厂商收编(但 "thesis" 被很多基金当营销词过度使用)。
- **可信度**: high / **Decay risk**: low

### 21. Founder-market fit — 创始人-市场契合度

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 创始人与所做市场之间的「天然匹配」—— 独特的领域经验、人脉、洞察或动机,使这个团队比别人更可能在这个市场赢;早期 VC 在「还没有 product-market fit 可看」时,founder-market fit 是核心下注依据。
- **Definition (outsider-friendly)**: 这个创始人是不是「最适合做这件事的人」—— 有没有别人没有的经验、资源或执念。
- **Etymology**: 由 "product-market fit"(PMF)衍生。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把它当「创始人简历好不好」—— 内行看的是「这个特定的人 × 这个特定的市场」的化学反应,名校大厂背景不等于 founder-market fit。
  - `usage_tell`: 外行混淆 founder-market fit 和 product-market fit —— 前者是「投资时」判断人的,后者是「投资后」验证产品的。
- **关联术语**: product-market fit、conviction、founder judgment、unfair advantage、why-now / why-you
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 22. TAM / SAM / SOM — 市场规模三件套

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: **TAM**(Total Addressable Market)= 理论总市场;**SAM**(Serviceable Addressable Market)= 产品/地域能覆盖的部分;**SOM**(Serviceable Obtainable Market)= 现实能拿到的份额。VC 真正关心的不是 deck 上的 TAM 数字,而是「这个市场会不会长大、能不能长出一家大公司」。
- **Definition (outsider-friendly)**: 一组估算「这个生意的市场到底有多大」的指标 —— 从理论上限到现实能拿到的份额。
- **Etymology**: 战略 / 创投通用 market sizing 框架。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行(和不少 founder)把 TAM 算成一个超大数字当卖点 —— 内行对「top-down 万亿 TAM」高度警惕,更信 "bottoms-up"(从单位经济和获客一层层算上来)和 "market timing"。
  - `pronunciation_tell`: TAM 念 "tam"、SAM 念 "sam"、SOM 念 "som",都按词读不拼字母。
  - `usage_tell`: 外行用 TAM 论证「市场够大所以值得投」—— 内行知道 VC 真正问的是 "why now" 和「这个市场能不能支撑 power-law outcome」。
- **关联术语**: bottoms-up vs top-down、why-now、market timing、unit economics
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 23. Unit economics — 单位经济模型

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 单个「单位」(一个客户 / 一笔订单)层面的盈亏结构,核心是 LTV(客户生命周期价值)、CAC(获客成本)、毛利、payback period;VC 用它判断「这个生意规模化之后是否真的赚钱」,寒冬期权重大幅上升。
- **Definition (outsider-friendly)**: 算「做成一单 / 服务一个客户」到底是赚是亏 —— 收入减去获客和服务成本。
- **Etymology**: 经济学 "unit cost" 在 SaaS / 消费创投的应用。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 unit economics 当「整体财务报表」—— 内行专指「拆到单客户/单订单」的颗粒度,以及它会不会随规模改善。
  - `usage_tell`: 外行说 "LTV/CAC 3 倍就健康" 当公式套 —— 内行会追问 CAC 怎么算(含不含 organic)、LTV 假设的留存曲线靠不靠谱、payback 多久。
- **关联术语**: LTV、CAC、burn rate、payback period、cohort、gross margin
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 24. Burn rate / runway — 烧钱速度 / 现金跑道

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: burn rate = 公司每月净消耗现金的速度(gross burn = 总支出,net burn = 支出减收入);runway = 现有现金 ÷ net burn = 还能撑几个月。VC 投后第一组监控数字,"18 个月 runway" 是常见经验阈值。
- **Definition (outsider-friendly)**: burn rate 是「每月烧多少钱」,runway 是「按这个速度还能活几个月」。
- **Etymology**: 飞机「跑道」比喻。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行说 "burn" 不分 gross/net —— 内行默认追问 "gross or net burn?",因为有收入的公司两者差很大。
  - `usage_tell`: 外行把 runway 当固定数 —— 内行知道 runway 是动态的(取决于 burn 和能不能融到下一轮),寒冬期讲究 "default alive"(靠现有钱就能活到盈利)vs "default dead"。
- **关联术语**: default alive / default dead、unit economics、bridge round、follow-on、reserve
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 25. Follow-on / reserve — 追加投资 / 预留资金

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: follow-on = 对已投公司在后续轮次的追加投资;reserve = 基金在 portfolio construction 时为 follow-on 预留的资金(常与首投 1:1 或更高)。"reserve strategy" 决定能否在 winner 上加注 —— power law 下这往往是回报放大的关键。
- **Definition (outsider-friendly)**: follow-on 是「对已经投过的公司继续追加投钱」,reserve 是「基金专门留出来做这件事的钱」。
- **Etymology**: portfolio construction 标准术语。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为基金的钱都用来投新项目 —— 内行知道一支基金常把 40-60% 留作 reserve,follow-on 决策(在哪个 winner 上加注)比首投更影响最终回报。
  - `usage_tell`: 外行把 follow-on 当「救济差公司」—— 内行原则是 "double down on winners",follow-on 给强者不给弱者(避免 "throwing good money after bad")。
- **关联术语**: reserve、portfolio construction、pro-rata、power law、check size、recycling
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 26. Dry powder — 待投资金(干火药)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 已经募集到但尚未投出 / 尚未 capital call 的资金。行业层面「dry powder 多」意味着潜在买盘充足;基金层面 "running out of dry powder" 意味着没钱投新 deal、也很难给老 portfolio 续命。
- **Definition (outsider-friendly)**: 基金手里「已经募到但还没花出去」的钱。
- **Etymology**: 军事用语「保持火药干燥」= 留有余力。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 dry powder 当「基金的现金余额」—— 内行知道 LP 的钱是「承诺(committed)」而非已到账,dry powder 是「还能 call 来投的额度」。
  - `usage_tell`: 媒体说「行业有数千亿 dry powder 所以会繁荣」—— 内行知道 dry powder 多不等于会投出去,GP 在不确定期会「坐在火药上」。
- **关联术语**: committed capital、capital call、deployment pace、vintage year
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 27. Vintage year — 基金成立年份(年份)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 一支基金开始投资的年份;因为投资环境强周期,基金回报高度受 vintage 影响(2009-2012 vintage 普遍好,2021 vintage 普遍承压),LP 做 portfolio 时刻意跨 vintage 分散。
- **Definition (outsider-friendly)**: 基金是哪一年开始投的 —— 就像红酒年份,入场时点很大程度决定了最终收成。
- **Etymology**: 借自葡萄酒 "vintage"。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行比较两支基金回报不看 vintage —— 内行知道跨 vintage 比 IRR/TVPI 几乎没意义,必须同 vintage、同策略 benchmark。
  - `usage_tell`: 外行以为「好 GP 任何年份都好」—— 内行知道 vintage timing 的影响经常盖过 GP skill,2021 入场的顶级基金也普遍 markdown。
- **关联术语**: J-curve、benchmark、IRR、vintage diversification、deployment pace
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 28. Anti-portfolio — 反投资组合(错过的好项目)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 一家基金「看过但没投、后来大成」的项目清单;Bessemer Venture Partners 公开自己的 anti-portfolio 使之成为行业文化符号。它的存在提醒:在 power law 里 "miss"(错过 Google)比 "loss"(投错一个归零)代价大得多。
- **Definition (outsider-friendly)**: 投资机构「曾经有机会投、却拒绝了,后来变成大公司」的遗憾名单。
- **Etymology**: Bessemer Venture Partners 创造并公开的概念。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 anti-portfolio 当「投资失败案例」—— 内行清楚它恰恰相反:是「没投但应该投」的清单,反映的是「错过」这种 VC 特有的、比亏钱更痛的失败模式。
  - `usage_tell`: 外行用它论证「VC 眼光不行」—— 内行用它说明 VC 决策的不对称性:错过的成本无上限,投错的成本封顶 1x。
- **关联术语**: power law、miss vs loss、conviction、pattern matching、FOMO
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 29. GP commitment — GP 出资承诺(跟投)

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: GP 自己投入基金的资金(传统经验值约基金规模的 1-2%,近年 LP 要求趋高);是 "skin in the game" 的体现,LP 尽调 GP 时必看 —— GP 自己掏多少真金白银决定利益对齐程度。
- **Definition (outsider-friendly)**: 基金管理人自己往基金里投的钱 —— 用来证明「我和 LP 是一条船」。
- **Etymology**: GP-LP 协议标准条款,有时写作 "GP commit"。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行混淆 GP commitment 和 carry —— 前者是「GP 投进去的本金(有亏损风险)」,后者是「GP 分到的利润」。
  - `usage_tell`: 外行只看百分比 —— 内行还看「这笔钱对这个 GP 个人是不是真的肉疼」(现金出资 vs management fee waiver 抵充,意义不同)。
- **关联术语**: skin in the game、carry、management fee waiver、LP due diligence、alignment
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 30. Capital call / distribution — 资本召集 / 分配

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: capital call(drawdown)= GP 在有 deal 时向 LP「叫款」,LP 不是一次性打满钱,而是按 commitment 分批响应;distribution = 基金退出后向 LP 返还现金 / 股票。两者节奏决定 LP 的现金流体验和 IRR。
- **Definition (outsider-friendly)**: capital call 是「基金要用钱了,通知 LP 把承诺的钱打进来」;distribution 是「项目退出赚钱了,把钱分还给 LP」。
- **Etymology**: 私募基金标准资金流转机制。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 LP「一次性把钱交给基金」—— 内行知道是「承诺额度 + 分批 call」,LP 要管理自己的 "unfunded commitment" 流动性。
  - `usage_tell`: 外行不知道「LP 错过 capital call(default)」的严重后果 —— 内行清楚 LP default 条款很狠(可没收已投份额)。
- **关联术语**: committed capital、drawdown、DPI、unfunded commitment、recycling、LP default
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 31. SPV — Special Purpose Vehicle(特殊目的载体)

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 为「单笔投资」临时设立的法律实体,把多个小投资人的钱归集起来投一家公司(deal-by-deal,而非 blind pool 基金);AngelList 把 SPV / Roll Up Vehicle 流程产品化后,SPV 成为 syndicate 和 solo GP 的标配工具。
- **Definition (outsider-friendly)**: 为「投某一个具体项目」专门成立的小型投资实体,把一群人的钱凑起来投进去。
- **Etymology**: 金融通用 "special purpose vehicle";VC 语境特指单 deal 投资载体。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 SPV 和「基金」混为一谈 —— 内行知道 SPV 是 single-deal(投资人事先知道投哪家),基金是 blind pool(投资人把钱交给 GP 自由配置),两者的费率、决策权、风险完全不同。
  - `usage_tell`: 外行以为做 SPV = 做 VC —— 内行知道 SPV syndicate 没有 fund 的 portfolio construction、reserve、track record 连续性。
- **关联术语**: syndicate、blind pool fund、Roll Up Vehicle、AngelList、solo GP、deal-by-deal
- **是否被错位包装**: AngelList 把 SPV 设立产品化,营销中常把 "SPV = 轻量做基金";内行强调 SPV ≠ fund(evidence: [T06-S015] 仅作 SAFE 对照,SPV 定义为行业通用知识)。
- **可信度**: high / **Decay risk**: low

### 32. Fund-of-funds (FoF) — 母基金

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 投资于其他 VC 基金(而非直接投公司)的基金;作为 LP 的一类,FoF 帮 LP(尤其中小机构 / family office)分散到多支 GP,但叠加一层 fee;在中国「母基金」尤其是政府引导基金 / 国资 LP 的重要形态。
- **Definition (outsider-friendly)**: 一种「投资基金的基金」—— 它不直接投创业公司,而是把钱分给一批 VC 去投。
- **Etymology**: "fund of funds" 标准结构。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把 FoF 当「更大的 VC」—— 内行知道 FoF 是 LP 角色,它的「投资标的」是 GP 而非 startup,核心能力是 GP selection 和 access。
  - `usage_tell`: 外行忽略 "double layer of fees"(两层费率)—— 内行知道 FoF 必须靠 GP selection 的超额收益覆盖掉额外那层 fee。
- **关联术语**: LP、政府引导基金、GP selection、access、double fee layer、endowment
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: low

### 33. Secondary — 二手份额转让 / 老股转让

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 二级交易 —— 可指 LP 把基金份额转让给别的 LP(LP secondary),也可指股东(创始人 / 早期投资人 / 员工)在不通过公司新融资的情况下出售老股(direct secondary);在 IPO 窗口收紧的年代,secondary 成为关键流动性出口。
- **Definition (outsider-friendly)**: 不通过公司上市或新融资,而是把「已经持有的股份 / 基金份额」卖给别人来变现。
- **Etymology**: 相对「一级市场(primary,公司新发股份)」的「二级(secondary)」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行只把「上市 / 被收购」当退出 —— 内行知道 secondary 是越来越重要的「部分流动性」工具,尤其 2022 年后公司晚上市。
  - `usage_tell`: 外行不分 LP secondary 和 direct secondary —— 内行清楚一个是「转基金份额」,一个是「转公司股权」,定价逻辑和买方完全不同。
- **关联术语**: liquidity、IPO window、direct secondary、LP secondary、tender offer、continuation fund
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: medium(随 IPO 周期变化)

### 34. Investment memo / IC memo — 投资备忘录 / 投委会备忘录

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 投资人为推动一个 deal 过 Investment Committee(IC,投委会)而写的内部文档 —— 包含 thesis、team、market、风险、deal 条款、回报建模、为什么投 / 为什么不投;是 VC 把判断「落到纸面、接受同僚 challenge」的核心载体。
- **Definition (outsider-friendly)**: 投资人写给自己团队的「我为什么建议投这家公司」的内部分析文档。
- **Etymology**: 行业内部流程文件;IC = Investment Committee。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 memo 是「给 founder / LP 看的」—— 内行知道 IC memo 是「对内」的,核心价值是逼自己写下 "what would have to be true" 和 risk,并留档供日后复盘。
  - `usage_tell`: 外行把 memo 当 deck 的复述 —— 内行的好 memo 会明确写「反方观点」和「这笔投资可能怎么死」。
- **关联术语**: Investment Committee、conviction、pre-mortem、what-would-have-to-be-true、deal partner
- **是否被错位包装**: Notion / Coda 等被当 memo 工具营销,但 memo 是流程概念非产品概念。
- **可信度**: high / **Decay risk**: low

### 35. 对赌协议 / VAM — Valuation Adjustment Mechanism(估值调整机制)

- **Type**: term(中国语境核心)
- **Tier**: tier-1
- **Definition (insider)**: 中国一级市场常见条款 —— 投融资双方就「公司未来业绩 / 上市与否」约定,若未达标则创始人 / 公司向投资人补偿(股权或现金),常与回购条款绑定;在 RMB 基金里几乎是标配,海外 priced round 反而很少用 earnout 式对赌。
- **Definition (outsider-friendly)**: 中国投资里常见的「业绩承诺」条款 —— 公司没达到约定目标,创始人就要按约定补偿投资人。
- **Etymology**: "Valuation Adjustment Mechanism" 直译;中文「对赌」是俗称。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行(尤其只懂美元 VC 的人)以为「VC 全球都一样」—— 内行知道对赌 + 回购是中国 RMB 基金特色,美元 VC 体系几乎不用,因为它把「股权投资」做成了「类债」。
  - `usage_tell`: 外行把对赌当「投资人欺负创始人」—— 内行知道它也是 LP(尤其国资)压给 GP 的风控要求向下传导的结果。
- **关联术语**: 回购条款、估值倒挂、RMB 基金、liquidation preference、earnout
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: medium(监管 + 司法判例在演化)

### 36. 回购条款 — Redemption / repurchase right(赎回 / 回购权)

- **Type**: term(中国语境核心)
- **Tier**: tier-1
- **Definition (insider)**: 投资人有权在约定条件(如未在期限内上市、对赌未达标)下要求公司 / 创始人按约定价格(本金 + 年化)买回其股份;在中国 RMB 基金里极普遍,2023-2024 年「回购潮 / 回购诉讼」成为行业重大议题,海外 VC 体系基本不用。
- **Definition (outsider-friendly)**: 投资人有权在特定情况下要求创始人或公司「按约定价格把股份买回去」,相当于给投资退出上了保险。
- **Etymology**: "redemption right" 的中国实践;中文「回购」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为 VC 是「纯股权、亏了认栽」—— 内行知道中国 RMB 基金的回购条款让创始人个人承担「类债」连带责任,这是中外 VC 最大的体感差异之一。
  - `usage_tell`: 外行不知道「回购权能不能真执行」是另一回事 —— 内行清楚 2023 年后大量回购走到诉讼/执行,创始人个人连带是火药桶。
- **关联术语**: 对赌协议、估值倒挂、RMB 基金、LP default、清算优先权
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: high(监管表态 + 司法判例 12 月内可能显著变化)

### 37. 人民币基金 / 美元基金 — RMB fund / USD fund

- **Type**: term(中国语境核心)
- **Tier**: tier-1
- **Definition (insider)**: 按募资和投资币种划分的两类基金。**美元基金**:LP 多为海外机构,投 VIE / 离岸架构,退出靠美股 / 港股,2022 后受中美脱钩 + 中概收紧冲击。**人民币基金**:LP 多为国资 / 引导基金 / 上市公司,受中基协备案监管,退出靠 A 股,普遍带对赌 + 回购,且有强返投 / 招商诉求。同一家机构常「双币运作」。
- **Definition (outsider-friendly)**: 中国的 VC 分两种 —— 用美元募资投资的,和用人民币募资投资的,两者的金主、规则、退出路径都不一样。
- **Etymology**: 中国创投市场的币种分类惯例。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行把「中国 VC」当一个整体 —— 内行知道美元基金和 RMB 基金几乎是两个行业:LP 类型、监管、架构、条款、退出全不同。
  - `usage_tell`: 外行忽略 RMB 基金的「返投比例 / 招商引资」诉求 —— 内行知道引导基金 LP 常要求 GP 把一定比例投回当地,这直接改变 sourcing 逻辑。
- **关联术语**: VIE、QFLP、中基协备案、引导基金、对赌协议、双 GP
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: medium-high

### 38. 估值倒挂 — Valuation inversion / down round (in PRC context)

- **Type**: term(中国语境核心)
- **Tier**: tier-1
- **Definition (insider)**: 公司后一轮(或二级 / 上市)估值低于前一轮投资人的成本,导致老股东账面浮亏;2022-2024 在中国一级市场大面积出现,直接触发回购条款、LP 不满、GP 募资困难的连锁反应。
- **Definition (outsider-friendly)**: 公司现在的估值比之前投资人进入时还低,早期投资人「投亏了」。
- **Etymology**: 中文行业用语,对应海外 "down round" 但语义更强调「老股东浮亏」。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行以为「估值跌了再涨回来就行」—— 内行知道在带回购条款的 RMB 基金里,估值倒挂会直接触发刚性回购义务,不是账面问题而是现金问题。
  - `usage_tell`: 外行把估值倒挂只当「公司问题」—— 内行知道它同时是「GP 问题」(影响 DPI、影响下一支基金募资)。
- **关联术语**: down round、回购条款、对赌协议、markdown、DPI
- **是否被错位包装**: 未见厂商收编。
- **可信度**: high / **Decay risk**: medium

---

## Tier 2 — 周边熟知术语(目标 30-70)

> 资深从业者熟知、但入行第一周不一定全懂的词。覆盖 deal 结构细节、基金运营、LP 关系、退出、中国特色。

### 39. Hurdle rate / preferred return — 门槛收益率 / 优先回报

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: LP 在 GP 开始拿 carry 之前必须先拿到的最低年化回报(PE 常见 8%,VC 不少基金无 hurdle);设了 hurdle,GP 要先让 LP「保本 + 优先收益」才分利润。
- **Definition (outsider-friendly)**: 基金管理人分利润之前,投资人(LP)必须先拿到的「保底收益率」。
- **Etymology**: PE/VC waterfall 标准条款。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为所有 VC 基金都有 8% hurdle —— 内行知道很多早期 VC 基金不设 hurdle(因为 J-curve 太长),hurdle 主要是 PE / 成长期惯例。
- **关联术语**: carry、waterfall、catch-up、J-curve
- **可信度**: high / **Decay risk**: low

### 40. Distribution waterfall / catch-up — 分配瀑布 / GP 追补

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金退出现金在 LP 和 GP 之间分配的顺序规则:一般是「先还 LP 本金 → 还 LP preferred return → GP catch-up(GP 追补到约定 carry 比例)→ 此后按 80/20 分」。European(whole-fund)waterfall 对 LP 更友好,American(deal-by-deal)对 GP 更友好。
- **Definition (outsider-friendly)**: 一套规定「基金赚的钱按什么先后顺序分给 LP 和 GP」的规则。
- **Etymology**: PE/VC 基金分配标准结构。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为「20% carry」就是 GP 简单拿走 20% —— 内行知道要看 waterfall 是 European 还是 American、有没有 catch-up、有没有 clawback,实际到手差别很大。
- **关联术语**: carry、hurdle rate、clawback、European vs American waterfall
- **可信度**: high / **Decay risk**: low

### 41. Clawback — 回拨 / 追回条款

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 如果 GP 在基金早期多拿了 carry、但基金最终整体回报不达标,GP 须把多拿的部分退还给 LP 的机制;deal-by-deal(American)waterfall 下尤其重要。
- **Definition (outsider-friendly)**: 如果管理人之前分多了利润、但基金最后没那么赚,要把多拿的钱退回来。
- **Etymology**: LPA 标准保护条款。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行忽略 clawback —— 内行知道它是 American waterfall 下 LP 的关键安全网,且执行起来(GP 把钱花了怎么追)是真实痛点。
- **关联术语**: distribution waterfall、carry、American waterfall、LP protection
- **可信度**: high / **Decay risk**: low

### 42. J-curve — J 曲线

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金生命周期里净值 / 现金回报的典型轨迹 —— 早期因为 management fee 和未退出,IRR/DPI 为负或低,后期 winner 退出后陡升,形似字母 J;LP 据此理解「前几年难看是正常的」。
- **Definition (outsider-friendly)**: 基金一开始账面是亏的(交了费、还没退出),要到后期才转正、上扬,曲线像字母 J。
- **Etymology**: 曲线形状命名。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行看到基金前 3 年回报难看就判断 GP 不行 —— 内行知道这是 J-curve 的正常段,要看 vintage 同期 benchmark。
- **关联术语**: vintage year、IRR、DPI、TVPI、markup
- **可信度**: high / **Decay risk**: low

### 43. Markup / markdown — 估值上调 / 下调

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 被投公司在新一轮融资(或公允价值评估)后,GP 对其持仓账面价值的上调(markup)/ 下调(markdown);markup 推高 TVPI / IRR 但「未落袋」,是 paper gain;2022-2024 大面积 markdown。
- **Definition (outsider-friendly)**: 公司估值变了,基金就把它持有的这部分股权的「账面价值」往上或往下调。
- **Etymology**: 公允价值会计实践。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行把 markup 当「赚到了」—— 内行强调 "markups aren't returns",只有 distribution / DPI 才是真回报。
- **关联术语**: TVPI、IRR、NAV、fair value、DPI
- **可信度**: high / **Decay risk**: low

### 44. NAV — Net Asset Value(基金净值)

- **Type**: term + acronym
- **Tier**: tier-2
- **Definition (insider)**: 基金当前持仓的公允价值合计(扣除负债);近年衍生出 "NAV loan / NAV financing" —— GP 用基金 NAV 做抵押借钱,用于给 portfolio 续命或提前给 LP 分配,是 2023 后争议话题。
- **Definition (outsider-friendly)**: 基金现在所有持仓加起来值多少钱。
- **Etymology**: 通用基金会计术语。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行不知道 "NAV loan" —— 内行知道它是 LP 在尽调时会专门盘问的新型杠杆工具。
- **关联术语**: markup、NAV loan、DPI、fair value
- **可信度**: high / **Decay risk**: medium

### 45. Recycling — 资金回收再投资

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金把早期退出 / 收回的本金不分给 LP,而是「再投出去」以提高资金利用率(扩大有效投资本金超过 committed capital);LPA 里有 recycling 上限和时间窗约定。
- **Definition (outsider-friendly)**: 基金把早期赚回来的钱不急着分,而是再拿去投新项目。
- **Etymology**: 基金运营术语。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为基金「投完一遍 committed capital 就没了」—— 内行知道 recycling 能让有效投资额超过 100% commitment。
- **关联术语**: committed capital、capital call、distribution、deployment pace
- **可信度**: high / **Decay risk**: low

### 46. Portfolio construction — 投资组合构建

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金在「投多少家、每家投多少(check size)、留多少 reserve、集中还是分散、按什么 stage/sector 配」上的整体设计;它是把 power law 数学转成具体行动的环节,不同学派(concentrated vs spray-and-pray)在这里分野。
- **Definition (outsider-friendly)**: 基金事先规划「这支基金一共投几家、每家投多少、怎么搭配」。
- **Etymology**: 借自资产配置 "portfolio construction"。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为 VC「看到好项目就投」—— 内行知道有 portfolio construction 约束,check size、数量、reserve 都是事先算好的数学。
- **关联术语**: power law、check size、reserve、concentration、ownership target
- **可信度**: high / **Decay risk**: low

### 47. Check size — 单笔投资额

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金单笔投资的金额;由基金规模 ÷ 计划投资数量 ÷ (1 + reserve 倍数)倒推而来,"check size discipline"(不乱开超出规划的支票)是基金纪律的体现。
- **Definition (outsider-friendly)**: 基金投一个项目通常出多少钱。
- **Etymology**: "writing a check" 的口语化。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为 check size 随项目大小随意定 —— 内行知道它是 portfolio construction 倒推出来的硬约束,乱开支票会破坏整支基金的数学。
- **关联术语**: portfolio construction、ownership target、reserve、fund size
- **可信度**: high / **Decay risk**: low

### 48. Ownership target — 目标持股比例

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金希望在一家公司初次投资后持有的股权比例(早期 VC 常见 10-20%);因为 power law 下「一个 winner 要能 return the fund」,ownership % 太低则即便投中独角兽也对基金回报贡献有限。
- **Definition (outsider-friendly)**: 基金希望在一家公司里占多少股份。
- **Etymology**: portfolio construction 术语。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行只关心「投没投中」—— 内行知道「投中且占够比例」才算数,ownership 是回报放大的乘数。
- **关联术语**: power law、fund-returner、check size、pro-rata、dilution
- **可信度**: high / **Decay risk**: low

### 49. Fund-returner — 能还本整支基金的项目

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 单凭这一个项目的退出回报,就能把整支基金的本金赚回来(1x)甚至更多的公司;VC 投每个 deal 时的隐含问题是 "can this return the fund?",答案为否的 deal 在 power law 框架下逻辑上不该投。
- **Definition (outsider-friendly)**: 一个「光靠它一家就能让整支基金回本」的项目。
- **Etymology**: power law 框架的行业用语。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行用「这个项目能赚 3 倍」评价 deal —— 内行问的是「它能不能 return the fund」,3 倍 check 对大基金可能毫无意义。
- **关联术语**: power law、ownership target、outlier、portfolio construction
- **可信度**: high / **Decay risk**: low

### 50. Cohort — 同期群(留存分析)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 按「同一时间加入」分组的用户 / 客户群,用来看留存、复购、LTV 随时间的演化;VC 做 product DD 时靠 cohort 曲线判断「用户留不留得住」,比单看 MAU 总数可靠得多。
- **Definition (outsider-friendly)**: 把「同一批进来的用户」单独拎出来,看他们随时间还剩多少在用。
- **Etymology**: 流行病学 "cohort";被 SaaS / 增长分析广泛采用。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行看「总用户增长」就觉得产品好 —— 内行要 cohort retention curve,因为漏桶式增长(拉新快、流失也快)会被总数掩盖。
- **关联术语**: retention、LTV、unit economics、churn、product-market fit
- **可信度**: high / **Decay risk**: low

### 51. Participating preferred — 参与分配优先股

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 一种 liq pref 结构 —— 投资人先拿回优先清算额,然后还按比例参与剩余分配("double dip");相对 non-participating(只能二选一)对 founder/普通股更不利,行业主流是 non-participating,participating 在弱势 deal / down round 才出现。
- **Definition (outsider-friendly)**: 一种对投资人特别有利的优先股:退出时先拿回本金,再跟大家一起分剩下的钱。
- **Etymology**: 优先股条款变体。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行不知道 "participating" 这个词的杀伤力 —— 内行一听就知道是「双重分钱」,会算它在不同 exit 估值下对普通股的侵蚀。
- **关联术语**: liquidation preference、non-participating、down round、cap (on participation)
- **可信度**: high / **Decay risk**: low

### 52. Protective provisions — 保护性条款(否决权)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 优先股投资人对特定重大事项(再融资、卖公司、改章程、增发、举债等)的否决权;属于 control terms,即使投资人股权比例不高,protective provisions 也能给他在关键决策上的「刹车」。
- **Definition (outsider-friendly)**: 投资人对公司一些重大决定的「否决权」—— 没他同意,这些事做不了。
- **Etymology**: 优先股标准条款。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为「小股东说了不算」—— 内行知道 protective provisions 让小比例投资人也能卡住卖公司、再融资等关键动作。
- **关联术语**: board seat、control terms、term sheet、preferred stock、veto right
- **可信度**: high / **Decay risk**: low

### 53. Information rights — 信息权

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 投资人定期获取公司财务报表、运营数据、董事会材料的合同权利;早期(尤其 SAFE / 小额)投资人常没有 board seat,information rights 是他们了解 portfolio 公司的主要正式通道。
- **Definition (outsider-friendly)**: 投资人有权定期拿到公司的财务和经营数据。
- **Etymology**: 投资人权利协议标准条款。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为投了就能随时问公司要数据 —— 内行知道这是要写进合同的具体权利,且小额投资人常被「information rights threshold」挡在外面。
- **关联术语**: board observer、pro-rata、major investor、reporting、SAFE
- **可信度**: high / **Decay risk**: low

### 54. Pay-to-play — 跟投义务条款

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: down round / 困难轮里的条款 —— 老投资人若不按比例继续投钱,就会被「惩罚」(优先股转普通股、失去反稀释保护等);2022-2024 寒冬里 pay-to-play 重新高频出现。
- **Definition (outsider-friendly)**: 困难融资轮里的规定:老投资人不继续跟着投钱,就会失去一部分原有的优先权利。
- **Etymology**: 行业周期条款。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 pay-to-play 当「鼓励跟投」—— 内行知道它本质是「惩罚不跟投者」,是寒冬期 inside round 的强制工具。
- **关联术语**: down round、recap、cram-down、anti-dilution、bridge round
- **可信度**: high / **Decay risk**: medium

### 55. Recap / cram-down — 资本重组 / 强制重组

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: recapitalization = 在公司困难时重整 cap table(常大幅压低估值、清零或大幅稀释老股东与员工);cram-down = 用极不利条款「硬塞」给不配合的老股东的重组;都是寒冬期 distressed 场景词。
- **Definition (outsider-friendly)**: 公司很困难时,推倒重来重新分配股权 —— 老股东和员工的股份往往被大幅压缩。
- **Etymology**: 公司金融 / 破产法术语在创投的应用。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行把 recap 当普通融资 —— 内行知道 recap 通常意味着「老股东被洗」,是公司困境信号。
- **关联术语**: down round、pay-to-play、washout round、liquidation preference、bridge to nowhere
- **可信度**: high / **Decay risk**: medium

### 56. Valuation cap / discount — 估值上限 / 折扣(SAFE & note 条款)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: SAFE / convertible note 转股时保护早期投资人的两个机制 —— **cap**:转股估值不超过某上限;**discount**:按下一轮价格打折转股;两者通常取对投资人更有利的一个。cap 太高 ≈ 早期风险没被补偿。
- **Definition (outsider-friendly)**: SAFE / 可转债里给早期投资人的两种「优惠」:一个限定换股时的最高估值,一个给换股价格打折。
- **Etymology**: SAFE / note 标准条款。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行只谈「投了多少钱」不谈 cap —— 内行知道 SAFE 的 cap 才是隐含估值,cap 谈不好等于早期风险白担。
- **关联术语**: SAFE、convertible note、pre/post-money、MFN clause、priced round
- **可信度**: high / **Decay risk**: low

### 57. MFN clause — Most Favored Nation(最惠条款)

- **Type**: term + acronym
- **Tier**: tier-2
- **Definition (insider)**: SAFE / note 里的条款 —— 若公司之后给别的投资人更优条款,本投资人有权「升级」到那个更优条款;早期投资人用它防止「后来者拿到更好的 cap」。
- **Definition (outsider-friendly)**: 早期投资人的「保底」条款:以后谁拿到更好的条件,我自动也升级到那个条件。
- **Etymology**: 借自国际贸易 "most favored nation"。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行没听过 MFN —— 内行在多张 SAFE 叠加时会专门追踪谁有 MFN、最优条款是哪份。
- **关联术语**: SAFE、valuation cap、convertible note、side letter
- **可信度**: high / **Decay risk**: low

### 58. Vesting / cliff — 股权 / 期权归属 / 悬崖期

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 创始人和员工股权 / 期权按时间(典型 4 年)逐步「归属」的安排,常带 1 年 "cliff"(满 1 年才一次性归属第一批,之后按月);VC 尽调时会看创始人股权有没有 vesting —— 没 vesting 的 founder equity 是 cap table 红旗。
- **Definition (outsider-friendly)**: 股份不是一次到手,而是按工作年限慢慢「赚到」,通常满一年才解锁第一批。
- **Etymology**: 雇员激励法律结构。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为创始人股权天然「全是自己的」—— 内行要求创始人股权也上 vesting,否则联合创始人早走会留下 dead equity。
- **关联术语**: cliff、dead equity、option pool、cap table、founder departure
- **可信度**: high / **Decay risk**: low

### 59. Accelerator / incubator — 加速器 / 孵化器

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 以「小额资金 + 标准条款 + 几个月集中辅导 + Demo Day」批量投早期公司的机构(YC、Techstars 为代表);对 VC 而言,accelerator 既是 deal sourcing 漏斗,也定义了一种「spray-and-pray + 教育」的投资学派。
- **Definition (outsider-friendly)**: 成批帮早期创业公司「打基础」的机构 —— 给点钱、给三个月辅导,最后办路演日。
- **Etymology**: YC(2005)开创的模式。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 accelerator 和 VC 基金混为一谈 —— 内行知道 accelerator 是「批量、标准化、早到不能再早」的模式,与 thesis-driven 基金逻辑相反。
- **关联术语**: Demo Day、spray-and-pray、deal flow、Y Combinator、SAFE
- **可信度**: high / **Decay risk**: low

### 60. Scout program — 侦察员计划

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: VC 基金给一批「scout」(常是创始人、运营者、社群里有 access 的人)小额资金,让他们以基金名义投极早期 deal,扩大基金触角;Sequoia scout program 是知名先例。
- **Definition (outsider-friendly)**: VC 找一批「眼线」,给他们小钱去投很早期的项目,帮基金更早发现好苗子。
- **Etymology**: Sequoia 等基金的运营创新。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为 scout 是「基金员工」—— 内行知道 scout 多是外部人,核心价值是他们的 access 和 network,不是 due diligence 能力。
- **关联术语**: deal sourcing、access、proprietary deal flow、syndicate、solo GP
- **可信度**: high / **Decay risk**: low

### 61. Lead investor / co-investor — 领投方 / 跟投方

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: lead = 在一轮里出价、谈 term sheet、通常拿 board seat、做主要 DD 的投资人;co-investor / follower = 跟着 lead 的条款进来、出资但不主导的投资人。"can you lead?" 是 founder 对 VC 的关键一问。
- **Definition (outsider-friendly)**: 领投方是「定条款、做主导」的那个投资人,跟投方是「跟着一起投」的。
- **Etymology**: syndicated round 的角色分工。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为「谁投得多谁是 lead」—— 内行知道 lead 是「定价 + 谈条款 + 拿 board + 扛 DD」的角色,金额未必最大。
- **关联术语**: term sheet、board seat、syndicate、price-setter、co-invest
- **可信度**: high / **Decay risk**: low

### 62. Co-invest — 共同投资(LP 直投权)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: GP 给 LP 在某个具体 deal 上「在基金之外额外直接投资」的机会,通常 no fee / no carry 或低费率;大 LP 把 co-invest 权当作选 GP 的重要筹码(能降低综合费率)。
- **Definition (outsider-friendly)**: 基金管理人允许大 LP 在某个具体项目上「额外再单独投一笔」,而且费用很低。
- **Etymology**: GP-LP 关系实践。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 co-invest 和 SPV 混 —— 内行知道 co-invest 特指「给 LP 的 deal 旁挂额度」,是 LP 谈判的核心诉求之一。
- **关联术语**: LP、SPV、fee offset、blended fee rate、deal-by-deal
- **可信度**: high / **Decay risk**: low

### 63. Side letter — 补充协议(LP 单独条款)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金与个别 LP 单独签的、对主 LPA 做个性化补充的协议(MFN、co-invest 优先、费率折扣、特定合规要求等);大 LP / 锚定 LP 常靠 side letter 拿到比小 LP 更好的条款。
- **Definition (outsider-friendly)**: 基金和某个 LP 私下单独签的「附加条款」,给这个 LP 一些主合同之外的特别待遇。
- **Etymology**: 私募基金法律实践。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为所有 LP 条款一样 —— 内行知道 side letter 让 LP 之间条款差异巨大,且 side letter 也常带 MFN。
- **关联术语**: LPA、MFN clause、anchor LP、co-invest、fee discount
- **可信度**: high / **Decay risk**: low

### 64. LPA — Limited Partnership Agreement(有限合伙协议)

- **Type**: term + acronym
- **Tier**: tier-2
- **Definition (insider)**: 定义基金一切规则的核心法律文件 —— 费率、carry、waterfall、投资范围、GP 权责、key person 条款、期限、clawback 等;GP-LP 谈判的主战场,fundraising 的「合同层」。
- **Definition (outsider-friendly)**: 一份规定基金「怎么运作、怎么收费、怎么分钱」的核心合同。
- **Etymology**: 有限合伙法律结构的主文件。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 LPA 当「formality」—— 内行知道 LPA 里的 key person、no-fault divorce、investment restrictions 等条款是 LP 真正的控制手段。
- **关联术语**: side letter、key person clause、waterfall、carry、fund term
- **可信度**: high / **Decay risk**: low

### 65. Key person clause — 关键人物条款

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: LPA 里规定:若指定的关键 GP(们)离开 / 不再投入足够时间,基金需暂停投资期(key person event),LP 可决定后续;它绑定「LP 投的是这几个人」这一事实。
- **Definition (outsider-friendly)**: 合同里写明「如果某几个核心管理人离开,基金就要暂停投资」。
- **Etymology**: LPA 标准 LP 保护条款。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为 LP 投的是「机构」—— 内行知道 key person 条款承认「LP 投的是特定的人」,GP 团队动荡会直接触发条款。
- **关联术语**: LPA、GP turnover、no-fault divorce、investment period、succession
- **可信度**: high / **Decay risk**: low

### 66. Anchor LP — 锚定 LP / 基石 LP

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 在 fundraising 早期就承诺大额、帮基金「起盘」的 LP;anchor 的背书能带动其他 LP,但 anchor 通常要价(更好的 side letter、co-invest、费率折扣甚至 GP 经济分成)。
- **Definition (outsider-friendly)**: 在募资最早期就承诺投一大笔、帮基金「站住脚」的 LP。
- **Etymology**: fundraising 实践用语。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为「有钱就能当 anchor」—— 内行知道 anchor 的价值一半是钱、一半是背书信号,而且 anchor 往往要走「最好的条款」。
- **关联术语**: side letter、first close、fundraising、co-invest、GP economics
- **可信度**: high / **Decay risk**: low

### 67. First close / final close — 首次关账 / 最终关账

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 基金募资是分批的:first close = 第一批 LP 资金到位、基金可以开始投;final close = 募资结束、基金总规模锁定。两次 close 之间可继续招 LP,后进 LP 常需补 "equalization"(利息补偿)。
- **Definition (outsider-friendly)**: 基金募资不是一次募满 —— 先「首关」就能开工,最后「终关」锁定总规模。
- **Etymology**: 私募基金募集流程术语。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为基金「募满才能投」—— 内行知道 first close 后就能投,且后进 LP 要做 equalization。
- **关联术语**: anchor LP、equalization、fund size、capital call、placement agent
- **可信度**: high / **Decay risk**: low

### 68. Placement agent — 募资中介 / FA(基金端)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 帮 GP 对接 LP、协助 fundraising 的中介机构(收 fee,常按募集额百分比);新基金 / 二线基金更依赖 placement agent,顶级基金往往不需要。
- **Definition (outsider-friendly)**: 帮基金管理人「找金主、拉投资」的中介。
- **Etymology**: 资本市场中介术语。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 placement agent 和「投行 / FA(帮公司融资的)」混 —— 内行知道这里特指「帮基金募 LP」的中介。
- **关联术语**: fundraising、LP、anchor LP、fund-of-funds、first close
- **可信度**: high / **Decay risk**: low

### 69. Tender offer / continuation fund — 要约收购 / 接续基金

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 流动性工具。**Tender offer**:公司 / 投资人组织一次集中按统一价格收购员工 / 早期股东老股的安排。**Continuation fund / continuation vehicle**:GP 把基金里仍想长期持有的优质资产「卖给」自己新设的接续基金,给老 LP 流动性、给新 LP 入场,2022 后大热但有利益冲突争议。
- **Definition (outsider-friendly)**: tender offer 是「集中按统一价格回购老股」;continuation fund 是「GP 把好资产转到一支新基金,让老投资人能套现、新投资人能进来」。
- **Etymology**: tender offer 是证券法术语;continuation fund 是 secondary 市场创新。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行没听过 continuation fund —— 内行知道它是 2022 后 IPO 荒里的关键工具,且 GP 同时当买卖双方有 conflict,LP 会盯估值公允性。
- **关联术语**: secondary、liquidity、IPO window、conflict of interest、LP secondary
- **可信度**: high / **Decay risk**: medium

### 70. Write-off / write-down — 减记 / 清零(项目层面)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: GP 把某个被投公司的持仓价值减记到 0(write-off,公司基本死了)或大幅下调(write-down);在 power law 业务里,portfolio 里大量 write-off 是「正常」的,不是失败信号 —— 只要 winner 够大。
- **Definition (outsider-friendly)**: 把投进去的某家公司「按账面归零」或大幅调低 —— 承认这笔投资基本亏了。
- **Etymology**: 会计术语。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为 write-off 多 = GP 不行 —— 内行知道 power law 下高 write-off 率是设计内的,关键看有没有 fund-returner。
- **关联术语**: power law、markdown、portfolio construction、loss ratio、anti-portfolio
- **可信度**: high / **Decay risk**: low

### 71. Conviction — 信念 / 笃定度

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 投资人对一个 deal「敢不敢重注、敢不敢逆共识」的内在确信程度;VC 文化里 "high conviction" 是褒义(愿意在别人看不懂时下重注),"low conviction check"(只是 FOMO 跟一手)是贬义。
- **Definition (outsider-friendly)**: 投资人对一个项目「到底有多笃定」—— 是真心重注,还是只是怕错过随便跟一笔。
- **Etymology**: VC 文化用语。
- **常见误用 (outsider-tell)**: `register_tell`: 外行把 "conviction" 当口头禅乱用 —— 内行用它特指「能不能逆共识 + 敢不敢加注 ownership」,而非泛泛的「我看好」。
- **关联术语**: thesis、anti-portfolio、FOMO、ownership target、contrarian
- **可信度**: high / **Decay risk**: low

### 72. Pattern matching — 模式匹配

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 投资人基于过往见过的成功 / 失败案例,对新项目做快速类比判断;是 VC 高效筛选的工具,但也是行业自我批评的靶子 —— pattern matching 会系统性复制偏见(只投「长得像上一个成功创始人」的人)。
- **Definition (outsider-friendly)**: 投资人靠「这看起来像我以前见过的成功 / 失败案例」来快速判断新项目。
- **Etymology**: 借自机器学习 / 认知科学。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 pattern matching 当褒义「经验丰富」—— 内行知道它是双刃剑,行业内部对「pattern matching 固化偏见、错过 non-obvious founder」有持续反思。
- **关联术语**: founder-market fit、conviction、anti-portfolio、bias、contrarian
- **可信度**: high / **Decay risk**: low

### 73. Spray-and-pray — 广撒网投资策略

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 投很多家、每家小额、不深度参与、靠组合里出 winner 的策略(YC / 部分 accelerator 模式);与 "concentrated"(投少、投重、深度参与)学派相对,是 VC 内部长期路线之争的一极。
- **Definition (outsider-friendly)**: 「广撒网」策略 —— 投很多家公司、每家投一点,赌总会有几个跑出来。
- **Etymology**: 行业俚语(略带贬义,但 YC 派会正面使用)。
- **常见误用 (outsider-tell)**: `register_tell`: 外行用 "spray-and-pray" 一定是贬义 —— 内行知道它是一个有数学依据的正经策略选择(power law + 大数定律),与 concentrated 各有逻辑。
- **关联术语**: concentrated、portfolio construction、accelerator、power law、index strategy
- **可信度**: high / **Decay risk**: low

### 74. Solo GP / solo capitalist — 独立 GP

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 一个人(而非合伙团队)独立募资、独立决策的基金管理人(Elad Gil、Lachy Groom 为代表);2020 年后兴起,靠个人品牌 + 速度 + 不用 partnership 投票,与传统 partnership-based 基金形成对照。
- **Definition (outsider-friendly)**: 「一个人开的 VC 基金」—— 募资和投资决策都靠他自己,不靠合伙人团队。
- **Etymology**: 2020 年前后的行业新形态,"solo capitalist" 由 Nikhil Trivedi 等推广。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行把 solo GP 等同 angel investor —— 内行知道 solo GP 是「一个人管一支机构化基金(有 LP、有 carry、有 fund 结构)」,不是用自己钱投的天使。
- **关联术语**: partnership、SPV、syndicate、personal brand、decision speed
- **可信度**: high / **Decay risk**: medium

### 75. Up-or-out — 升职或走人(职业路径)

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: VC 机构(尤其 associate / principal 层)常见的职业逻辑 —— 在限定年限内要么升上去(principal → partner),要么离开;Associate 走到 Partner 的比例极低,这是行业真实就业结构,与公开的「励志叙事」差距大。
- **Definition (outsider-friendly)**: VC 机构里初级岗位的「潜规则」:几年内升不上去就得走人。
- **Etymology**: 借自咨询 / 投行 / 律所的 "up or out" 文化。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为「进了 VC 就一路做到 Partner」—— 内行知道 associate 多是 2-3 年合约角色,up-or-out 是常态,Partner 席位极稀缺。
- **关联术语**: associate、principal、partner、carry vesting、track record
- **可信度**: high / **Decay risk**: low

### 76. Capital efficiency — 资本效率

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 公司「用多少钱换来多少进展 / 收入 / 估值」的效率;2022 后从「增长不惜代价」转向「capital-efficient growth」,VC 评估和投后辅导都把它当核心指标。
- **Definition (outsider-friendly)**: 公司「花钱花得值不值」—— 同样的进展,用的钱越少越好。
- **Etymology**: 财务 / 运营术语,2022 后在创投高频化。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把它和「省钱」划等号 —— 内行指的是「单位资本产出」的效率,该花的关键投入还是要花。
- **关联术语**: burn rate、unit economics、default alive、growth at all costs、runway
- **可信度**: high / **Decay risk**: medium

### 77. Bridge to nowhere — 通向无处的过桥

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: 一笔过桥融资续了命,但公司并没有清晰的下一个里程碑 / 下一轮路径 —— 钱烧完还是回到原点;是 VC 评估是否参与 bridge round 时的核心警惕信号。
- **Definition (outsider-friendly)**: 一笔「续命钱」,但续完之后公司依然没有明确的出路。
- **Etymology**: 行业俚语,与 "bridge to round" 相对。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把所有 bridge 都看成救援 —— 内行第一句问 "bridge to what?",分辨 bridge to round vs bridge to nowhere。
- **关联术语**: bridge round、runway、default dead、pay-to-play、down round
- **可信度**: high / **Decay risk**: low

### 78. Demo Day — 路演日

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: accelerator(YC 等)在一期结束时组织被投公司集中向 VC 群体路演的活动;对 VC 是高强度 sourcing 场,但也因「FOMO 驱动、估值被哄抬、决策时间被压缩」受内行诟病。
- **Definition (outsider-friendly)**: 加速器毕业时,把这一期的创业公司集中起来,向一屋子投资人做路演。
- **Etymology**: YC 开创的形式。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行把 Demo Day 当「优质项目集市」—— 内行知道它是 FOMO + 时间压缩的环境,很多老练 VC 反而刻意「Demo Day 之前就下手」或「之后冷静再看」。
- **关联术语**: accelerator、FOMO、Y Combinator、deal flow、spray-and-pray
- **可信度**: high / **Decay risk**: low

### 79. QFLP — 合格境外有限合伙人

- **Type**: term + acronym(中国语境)
- **Tier**: tier-2
- **Definition (insider)**: 中国部分城市试点的制度,允许合格境外机构以外币出资、经审批换汇投资于境内人民币私募基金 / 项目;是境外资本进入中国一级市场的合规通道之一,各试点城市细则不同。
- **Definition (outsider-friendly)**: 一种让海外机构「合规地把外币换成人民币、投到中国项目」的试点制度。
- **Etymology**: "Qualified Foreign Limited Partner",中国地方金融试点政策。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为外资进中国一级市场只有「美元基金 / VIE」一条路 —— 内行知道 QFLP 是另一条(换汇投 RMB 资产),且高度依赖地方试点政策。
- **关联术语**: RMB 基金、美元基金、VIE、中基协备案、外资准入
- **可信度**: medium / **Decay risk**: medium-high(地方试点政策常变)

### 80. 双 GP — Dual-GP structure(中国语境)

- **Type**: term(中国语境)
- **Tier**: tier-2
- **Definition (insider)**: 中国 RMB 基金常见结构 —— 一支基金由两个 GP 共同管理,典型组合是「有投资能力的 GP」+「有募资能力 / 国资背景 / 地方资源的 GP」;由中国 LP 结构(大量国资 / 引导基金)和返投诉求催生。
- **Definition (outsider-friendly)**: 中国一支基金常由两家管理机构合管 —— 一家擅长投资,另一家擅长募资或有政府资源。
- **Etymology**: 中国创投市场结构性产物。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行以为基金都是「一个 GP」—— 内行知道中国 RMB 基金「双 GP」普遍,是 LP 生态(国资主导)倒逼出来的结构。
- **关联术语**: RMB 基金、引导基金、返投、中基协备案、GP commitment
- **可信度**: medium / **Decay risk**: medium

### 81. 引导基金 — Government guidance fund(中国语境)

- **Type**: term(中国语境)
- **Tier**: tier-2
- **Definition (insider)**: 中国各级政府设立、作为 LP 出资于市场化子基金的母基金;通常带「返投比例」「招商引资」「让利」等政策诉求,是当下中国 RMB 基金最重要的 LP 类型,深刻改变 GP 的 sourcing 和投资逻辑。
- **Definition (outsider-friendly)**: 政府设立的、专门去当 LP 投资各家 VC 基金的「母基金」,但通常附带「把钱投回本地」之类的条件。
- **Etymology**: 中国产业政策与创投结合的产物。
- **常见误用 (outsider-tell)**: `semantic_tell`: 外行把 LP 想成「纯财务投资人」—— 内行知道中国引导基金 LP 带强政策诉求(返投 / 招商),GP 拿这笔钱意味着接受非纯财务约束。
- **关联术语**: RMB 基金、母基金、返投、双 GP、中基协备案
- **可信度**: medium / **Decay risk**: medium

### 82. Series A crunch / graduation rate — A 轮断层 / 晋级率

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: graduation rate = 从某一轮成功融到下一轮的公司比例;"Series A crunch" 特指「拿了种子轮但融不到 A 轮」的大量公司堆积现象,寒冬期尤其明显,是 seed 投资人评估自己 portfolio 健康度的关键漏斗指标。
- **Definition (outsider-friendly)**: 拿到种子轮的公司里,只有一部分能成功融到 A 轮 —— 中间这道坎就是「A 轮断层」。
- **Etymology**: 行业漏斗分析用语。
- **常见误用 (outsider-tell)**: `usage_tell`: 外行以为「拿到种子轮就上岸了」—— 内行盯 graduation rate,知道 seed → A 的淘汰率很高,寒冬期更狠。
- **关联术语**: graduation rate、bridge round、down round、power law、loss ratio
- **可信度**: high / **Decay risk**: medium

---

## Standards / Regulations / Certifications（标准 / 法规 / 框架)

> VC 是「中度监管行业」:对 GP 自身,主要约束在「向谁募资(证券法豁免)+ 基金登记备案 + 信息披露」;对 deal 层面,法规决定能不能投、用什么结构、税务怎么算。**地域差异巨大**,按 US / 行业协会 / 中国分列。**认证**:VC 行业基本无强制执业认证(美国 GP 多持 Series 65/82 等仅在特定情形需要;CFA 是加分非门槛)—— 本节 Certification 类基本 **N/A**。

### R1. SEC accredited investor — 合格投资者定义(美国)

- **Type**: regulation
- **Geographic-specific**: US
- **Definition (insider)**: 美国证券法下界定「谁可以投私募(包括 VC 基金)」的门槛。个人:近两年年收入 > 20 万美元(与配偶合计 > 30 万)且预期持续,或净资产 > 100 万美元(不含主要住所);2020 年修订新增「持有特定专业证照(如 Series 7/65/82)」也可认定。机构 LP 另有标准。GP 募资时必须确保 LP 符合此定义(或 qualified purchaser)。
- **Definition (outsider-friendly)**: 美国法律规定的「够格投私募基金 / 创业公司的人」的财富 / 收入 / 专业资格门槛。
- **Etymology / 来源**: SEC,Securities Act Reg D 体系。
- **是否被错位包装**: 无 —— 这是硬法规。
- **变化历史**:
  - 1982:确立 20 万 / 100 万门槛(沿用至今未按通胀调整)
  - 2020-08:SEC 终稿 33-10824,新增「专业知识 / 证照 / 关系」可认定路径(evidence: [T06-S001, T06-S003])
  - 2025:仍有《Fair Investment Opportunities for Professional Experts Act》等扩大定义的立法在国会推进,SEC 2025-06 发布 staff report(evidence: [T06-S018]);**核心收入 / 净资产数字截至 2026-05 未变**
- **Source**: [verified_primary] T06-S001、T06-S003、T06-S018
- **可信度**: high / **Decay risk**: medium(立法在推进,12-24 月内门槛或资格路径可能变)

### R2. Regulation D — Reg D 私募发行豁免(美国)

- **Type**: regulation
- **Geographic-specific**: US
- **Definition (insider)**: 让 GP 募集基金(以及创业公司融资)可以「不向 SEC 注册」的核心豁免规则。**Rule 506(b)**:可向无限多 accredited investor + 最多 35 个非 accredited,但**不得公开宣传(no general solicitation)**。**Rule 506(c)**:**可以公开宣传**,但所有投资人必须是 accredited 且 GP 须采取合理步骤**核实**。绝大多数 VC 基金走 506(b)。还需在募资后 15 天内提交 **Form D**。
- **Definition (outsider-friendly)**: 美国法律里让基金 / 创业公司「私下募资不用走上市那套注册流程」的豁免规则。
- **Etymology / 来源**: SEC,Securities Act of 1933 项下。
- **是否被错位包装**: 无。
- **变化历史**:
  - 1982:Reg D 确立
  - 2013(JOBS Act 落地):新增 506(c),首次允许私募「公开宣传」(代价是强制核实 + 全员 accredited)
  - 长期稳定,近 5 年无重大改动 → 不进时间轴,仅记 issued
- **Source**: [verified_primary] T06-S002
- **可信度**: high / **Decay risk**: low

### R3. Qualified purchaser / Investment Company Act 3(c)(1) & 3(c)(7) — 合格购买人 / 投资公司法豁免(美国)

- **Type**: regulation
- **Geographic-specific**: US
- **Definition (insider)**: 决定 VC 基金能容纳多少 LP、不被当成「注册投资公司」的豁免。**3(c)(1)**:LP 须为 accredited investor,人数上限通常 100(或 venture capital fund 在某些口径下 250)。**3(c)(7)**:LP 须全为 "qualified purchaser"(个人通常 ≥ 500 万美元投资资产),人数上限实际由 ≤ 2000 持有人触发注册的红线约束。基金选 3(c)(1) 还是 3(c)(7) 直接决定 LP 名单结构。
- **Definition (outsider-friendly)**: 一组规则,决定一支基金最多能有多少投资人、这些投资人得多有钱,才不用被当成「公募基金」来监管。
- **Etymology / 来源**: SEC,Investment Company Act of 1940。
- **是否被错位包装**: 无。
- **变化历史**: 1940 确立;长期稳定,近年无重大改动 → 不进时间轴。
- **Source**: [verified_primary] T06-S001(SEC 投资者教育,关联说明)
- **可信度**: high / **Decay risk**: low

### R4. QSBS / Section 1202 — 合格小型企业股票税收优惠(美国)

- **Type**: regulation
- **Geographic-specific**: US
- **Definition (insider)**: 美国税法 26 USC §1202 —— 符合条件的小型企业原始股,持有满一定年限后出售,资本利得可按比例免联邦税;对 VC、天使、创始人是重大税务利好,投资和退出结构设计都会围绕「保住 QSBS 资格」。
- **Definition (outsider-friendly)**: 美国税法的一项优惠 —— 投早期小公司的股票,持有够久再卖,赚的钱可以免一部分(或全部)联邦税。
- **Etymology / 来源**: Internal Revenue Code §1202;立法机构原文(Cornell LII 镜像)。
- **是否被错位包装**: 无。
- **变化历史**:
  - 1993:§1202 设立(初始 50% 排除)
  - 2009-2010:排除比例提高,2015 起对符合条件股票 **100% 排除** 制度化(持有 ≥ 5 年)
  - **2025-07-04:One Big Beautiful Bill Act(OBBBA)重大修订** —— 对 2025-07-04 之后取得的 QSBS:引入**阶梯持有期**(持有 ≥ 3 年 50%、≥ 4 年 75%、≥ 5 年 100%);单纳税人单发行人**排除上限从 1000 万 → 1500 万美元**(2027 起按通胀调整);公司**总资产门槛从 5000 万 → 7500 万美元**。2025-07-04 之前取得的股票适用旧规则(evidence: [T06-S004, T06-S020])
- **Source**: [verified_primary] T06-S004;[secondary] T06-S020
- **可信度**: high / **Decay risk**: medium(刚大改,后续 IRS 细则 / 州层面跟进会持续,需 12 月内复查)

### R5. ILPA Reporting Template + ILPA Principles — 机构 LP 协会报告模板与原则(行业标准)

- **Type**: standard(行业协会自律标准,非法规)
- **Geographic-specific**: global(以美国为中心,被全球 LP/GP 广泛参考)
- **Definition (insider)**: ILPA(Institutional Limited Partners Association)是代表 LP 利益的全球行业协会。其 **Reporting Template** 把 GP 给 LP 的费用 / 费率 / carry / 现金流报告标准化;**ILPA Principles**(基金治理与对齐最佳实践,3.0 版)是 LP 谈 LPA 条款的事实参照系。两者**不是强制法规**,但已成行业「软标准」—— LP 普遍要求 GP 遵循。
- **Definition (outsider-friendly)**: 一个代表「基金出资人(LP)」的协会发布的「基金该怎么向我们汇报、该怎么治理」的行业通用标准。
- **Etymology / 来源**: ILPA(行业协会,surrogate_primary)。
- **是否被错位包装**: 无(本身就是中立标准制定方)。
- **变化历史**:
  - 2016:ILPA Reporting Template 首版发布
  - 2019:ILPA Principles 3.0 发布
  - **2024 全年开发、2025-01 发布 Reporting Template v2.0**(QRSI 季度报告标准倡议):费用 / 开支 / carry 披露更细,取消分层报告;**对仍在投资期的基金自 2026 Q1、新基金自 2026-01-01 起替代 2016 版**(evidence: [T06-S009, T06-S010, T06-S019])
- **Source**: [surrogate_primary] T06-S009、T06-S010、T06-S019
- **可信度**: high / **Decay risk**: medium(v2.0 刚落地,2026 进入采用期,GP 报告 workflow 直接受影响)

### R6. NVCA Model Legal Documents — 美国 VC 协会标准法律文件(行业标准)

- **Type**: standard(行业协会标准文件)
- **Geographic-specific**: US
- **Definition (insider)**: NVCA(National Venture Capital Association)维护的一套开源标准 VC 交易文件(Term Sheet、Stock Purchase Agreement、Investors' Rights Agreement、Voting Agreement 等);是美国 priced round 的事实模板,大幅降低 deal 法律成本,「按 NVCA 文件改」是行业惯用语。
- **Definition (outsider-friendly)**: 美国 VC 行业协会免费发布的「标准投资合同模板」,大家做 deal 基本在它上面改。
- **Etymology / 来源**: NVCA(行业协会,surrogate_primary)。
- **是否被错位包装**: 无。
- **变化历史**: 长期维护,定期小幅更新(条款随市场惯例微调);无单次重大「版本跃迁」→ 仅记「持续更新」,不进时间轴。
- **Source**: [surrogate_primary] T06-S011
- **可信度**: high / **Decay risk**: low-medium

### R7. SAFE(YC 标准文档)— 未来股权简单协议(行业事实标准)

- **Type**: standard(单一机构发布、被行业广泛采纳的事实标准)
- **Geographic-specific**: US(为主,被全球早期融资借鉴)
- **Definition (insider)**: 见 Tier 1 #7。作为「标准」看:YC 把 SAFE 文本开源、免费,使其成为美国种子轮事实标准。**关键版本变化**:2013 年首发(pre-money SAFE),**2018 年改版为 post-money SAFE** —— 这一改把「多个 SAFE 叠加的稀释不确定性」从投资人转移给 founder,是 deal 结构哲学的一次实质转变。
- **Definition (outsider-friendly)**: YC 免费发布、被广泛使用的标准早期融资协议模板。
- **Etymology / 来源**: Y Combinator(vendor 一手,surrogate_primary)。
- **是否被错位包装**: SAFE 文本本身是 YC 开源标准;部分融资平台把「在我们平台发 SAFE」营销为增值服务,但文本仍是 YC 版本(evidence: [T06-S012, T06-S015])。
- **变化历史**:
  - 2013:pre-money SAFE 首发,取代 convertible note
  - **2018:改版为 post-money SAFE**(当前默认版本)
- **Source**: [surrogate_primary] T06-S012;[secondary] T06-S015
- **可信度**: high / **Decay risk**: low(已稳定多年,YC 偶有模板微调)

### R8. 《私募投资基金监督管理条例》— 私募基金行政法规(中国)

- **Type**: regulation
- **Geographic-specific**: CN
- **Definition (insider)**: 中国 **2023 年由国务院出台、2023-09-01 起施行** 的私募基金领域**首部行政法规**(此前主要靠部门规章和自律规则)。明确私募基金募集、投资、运作、退出的基本规则,提高私募基金的法律层级,与证监会监管、中基协自律形成「法规—规章—自律」三层。RMB 基金 GP 的合规底座。
- **Definition (outsider-friendly)**: 中国第一部专门管「私募基金(含 VC)」的行政法规,规定了基金怎么募、怎么投、怎么运作。
- **Etymology / 来源**: 国务院令(立法 / 行政法规原文,verified_primary)。
- **是否被错位包装**: 无。
- **变化历史**:
  - 2023-07 公布、**2023-09-01 施行**(首部行政法规,是中国私募监管「升格」的标志性事件)(evidence: [T06-S006])
  - 配套:证监会《私募投资基金监督管理办法》及中基协自律规则陆续更新
- **Source**: [verified_primary] T06-S005、T06-S006、T06-S007
- **可信度**: high / **Decay risk**: medium(配套规则仍在陆续出台 / 修订)

### R9. 中基协私募基金登记备案 — AMAC fund registration & filing(中国)

- **Type**: regulation / standard(法定授权的自律登记备案制度)
- **Geographic-specific**: CN
- **Definition (insider)**: 中国证券投资基金业协会(AMAC / 中基协)对私募基金管理人**登记**、私募基金产品**备案**的制度 —— RMB 基金 GP 必须先在中基协完成管理人登记、每支基金须备案,否则不能合规募投。中基协 2023 年起《私募投资基金登记备案办法》及配套指引大幅提高门槛(实缴资本、专业人员、高管资质等)。是 RMB 基金「能不能开门」的硬性前置。
- **Definition (outsider-friendly)**: 中国的私募基金管理人和每支基金都必须在行业协会「登记 / 备案」过,才能合法募资和投资。
- **Etymology / 来源**: AMAC(中基协,法定授权自律组织,verified_primary)。
- **是否被错位包装**: 无。
- **变化历史**:
  - 2014 起:中基协承担登记备案职能
  - **2023-05-01:《私募投资基金登记备案办法》施行**,登记 / 备案门槛与材料要求显著提高
  - 配套指引(管理人登记、产品备案、关联交易等)持续更新(evidence: [T06-S008, T06-S021])
- **Source**: [verified_primary] T06-S008、T06-S021
- **可信度**: high / **Decay risk**: medium(配套指引常更新)

### R10.（认证类）VC 行业执业 / 团队认证 — 基本 N/A

- **Type**: certification
- **状态**: **N/A — VC 行业没有「准入级」执业认证**。
- **说明**:
  - 美国:GP / 投资人**无强制执业证书**;只有在从事特定受监管活动(如经纪自营、对外推介收费)时才可能需要 FINRA Series 7 / 63 / 65 / 82 等,这是「特定活动触发」而非「入行门槛」。CFA、MBA(尤其 Stanford GSB / HBS)是简历加分项,**不是资质门槛**。
  - 中国:RMB 基金从业者需通过**基金从业资格考试**(中基协)才能登记为相关从业人员 —— 这更接近「从业登记前置」而非国际意义上的专业认证;高管另有资质要求(见 R9)。
  - 结论:Phase 2 在 [Glossary] 节应明确报告「VC 行业 Certification 维度:美国基本 N/A(活动触发型证照除外),中国有基金从业资格作为登记前置」。
- **Source**: [verified_primary] T06-S008(中基协,从业资格 / 高管资质关联);[verified_primary] T06-S001(SEC,美国无入行证照,关联)
- **可信度**: high / **Decay risk**: low

---

## 总览表

### Tier 1 — 核心必懂(38 个)

| 术语 | Type | Insider def(一句) | Outsider tell | Last_updated |
|------|------|---------------------|---------------|--------------|
| Power law | term | 80%+ 回报来自 1-2 个 outlier,miss 比 loss 致命 | 当二八定律泛泛用;不知它推导出 portfolio 数学 | 2026-05-14 |
| Carry / carried interest | term | GP 分到的利润(标准 20%),7-10 年后才兑现 | 误当日常收入;混淆 GP commitment | 2026-05-14 |
| Management fee | term | 每年从基金规模收 2%,GP 确定性工资来源 | 觉得「2% 不多」;不算 10 年累计 | 2026-05-14 |
| GP / LP | term+acronym | GP 管钱投项目,LP 出钱;双层受托结构 | 把 VC 当一个人;说「VC 的钱」 | 2026-05-14 |
| DPI/TVPI/IRR/MOIC | acronym | 基金回报四指标,DPI 是真现金、IRR 是 paper | 只看 IRR;混 TVPI 和 DPI | 2026-05-14 |
| Pre/post-money | term | post = pre + 本轮投入,决定 ownership % | 报估值不说 pre 还是 post | 2026-05-14 |
| SAFE | term+acronym+standard | YC 发明的不定价早期融资工具,非债 | 当成可转债;不分 pre/post-money SAFE | 2026-05-14 |
| Convertible note | term | 有息有到期日的早期债权工具,转股 | 和 SAFE 混;忽略 maturity 杀伤力 | 2026-05-14 |
| Priced round | term | 定价、发优先股、签完整 term sheet 的轮次 | 以为 Series A 只是金额大小 | 2026-05-14 |
| Liquidation preference | term | 退出时优先股先拿钱,标准 1x non-participating | 只盯估值忽略 liq pref | 2026-05-14 |
| Anti-dilution | term | down round 时保护早期投资人(ratchet/加权) | 不分 full ratchet 和 weighted average | 2026-05-14 |
| Pro-rata rights | term | 按比例追投维持 ownership %,是权利非义务 | 当成义务;不懂行使 winner pro-rata 更重要 | 2026-05-14 |
| Cap table | term | 全部股权/期权/SAFE 持有人比例总表 | 当成股东名单;不看 fully-diluted | 2026-05-14 |
| Option pool / ESOP | term+acronym | 员工期权池,常从 pre-money 划(隐形压估值) | 不知 pool 放 pre-money 意味 founder 被额外稀释 | 2026-05-14 |
| Term sheet | term | 不具约束力的核心条款摘要,签了才进正式文件 | 以为签了钱就到账;只看估值金额 | 2026-05-14 |
| Board seat / observer | term | 董事席位(投票+fiduciary)/ 观察员(列席) | 当成「话语权」;不知 board 对全体股东负责 | 2026-05-14 |
| Down round / bridge round | term | 折价轮 / 两轮间过桥融资,寒冬期高频 | 觉得 down round = 要完;不分 bridge 去哪 | 2026-05-14 |
| Deal flow / sourcing | term | 能看到的项目量×质 / 获取项目的方法 | 以为越多越好;把 sourcing 当销售线索 | 2026-05-14 |
| Due diligence (DD) | term+acronym | 投前系统核查,早期 70% 是 founder judgment | 念全称;以为是查账;忽视 reference call | 2026-05-14 |
| Thesis-driven investing | term | 事先形成 sector/趋势观点并主动筛选 deal | 当成投资标准清单;滥用 "thesis" | 2026-05-14 |
| Founder-market fit | term | 创始人与市场的天然匹配,早期核心下注依据 | 当成简历好不好;混 product-market fit | 2026-05-14 |
| TAM/SAM/SOM | acronym | 市场规模三件套,VC 真正问的是 why-now | 算超大 TAM 当卖点;按字母拼读 | 2026-05-14 |
| Unit economics | term | 单客户/单订单层面盈亏,寒冬期权重大涨 | 当成整体财报;LTV/CAC 套公式不追假设 | 2026-05-14 |
| Burn rate / runway | term | 每月烧钱速度 / 还能活几个月 | burn 不分 gross/net;runway 当固定数 | 2026-05-14 |
| Follow-on / reserve | term | 对已投公司追投 / 基金为此预留的钱 | 以为钱都投新项目;follow-on 救差公司 | 2026-05-14 |
| Dry powder | term | 已募未投的钱 | 当成现金余额;以为多就会投出去 | 2026-05-14 |
| Vintage year | term | 基金开始投资的年份,强周期影响回报 | 跨 vintage 比回报;以为好 GP 任何年份都好 | 2026-05-14 |
| Anti-portfolio | term | 看过没投却大成的清单,提醒 miss > loss | 当成失败案例;用来论证 VC 眼光差 | 2026-05-14 |
| GP commitment | term | GP 自己投入基金的钱(约 1-2%),skin in game | 混淆 carry;只看百分比不看是否肉疼 | 2026-05-14 |
| Capital call / distribution | term | GP 向 LP 分批叫款 / 退出后返还现金 | 以为 LP 一次性打满钱 | 2026-05-14 |
| SPV | term+acronym | 单 deal 投资载体,AngelList 产品化 | 和基金混;以为做 SPV = 做 VC | 2026-05-14 |
| Fund-of-funds (FoF) | term+acronym | 投基金的基金,LP 角色,叠加一层 fee | 当成更大的 VC;忽略双层 fee | 2026-05-14 |
| Secondary | term | 转基金份额 / 转老股,IPO 荒里的流动性出口 | 只把上市/收购当退出;不分 LP/direct secondary | 2026-05-14 |
| Investment memo / IC memo | term | 推动 deal 过投委会的对内分析文档 | 以为给 founder/LP 看;当成 deck 复述 | 2026-05-14 |
| 对赌协议 / VAM | term(CN) | 业绩/上市未达标则补偿,RMB 基金标配 | 以为 VC 全球一样;不知中国把股权做成类债 | 2026-05-14 |
| 回购条款 | term(CN) | 投资人有权要求按本金+年化买回股份 | 以为 VC 纯股权;不知创始人个人连带 | 2026-05-14 |
| 人民币基金 / 美元基金 | term(CN) | 两类基金 LP/监管/架构/退出全不同 | 把「中国 VC」当整体;忽略返投诉求 | 2026-05-14 |
| 估值倒挂 | term(CN) | 后轮估值低于前轮成本,触发回购连锁 | 以为账面问题;不知触发刚性回购现金义务 | 2026-05-14 |

### Tier 2 — 周边熟知(44 个)

| 术语 | Type | Insider def(一句) | Last_updated |
|------|------|---------------------|--------------|
| Hurdle rate / preferred return | term | GP 拿 carry 前 LP 须先拿到的最低年化(VC 常无) | 2026-05-14 |
| Distribution waterfall / catch-up | term | 退出现金在 LP/GP 间的分配顺序规则 | 2026-05-14 |
| Clawback | term | GP 早期多拿 carry、基金最终不达标须退还 | 2026-05-14 |
| J-curve | term | 基金净值早期为负、后期陡升的 J 形轨迹 | 2026-05-14 |
| Markup / markdown | term | 持仓账面价值上调/下调,markup 非真回报 | 2026-05-14 |
| NAV | term+acronym | 基金持仓公允价值合计,衍生 NAV loan | 2026-05-14 |
| Recycling | term | 把早期收回的本金再投出去提高资金利用率 | 2026-05-14 |
| Portfolio construction | term | 投几家/每家多少/留多少 reserve 的整体设计 | 2026-05-14 |
| Check size | term | 单笔投资额,由基金规模倒推 | 2026-05-14 |
| Ownership target | term | 初投后希望持有的股权比例(早期 10-20%) | 2026-05-14 |
| Fund-returner | term | 单凭它退出就能还本整支基金的项目 | 2026-05-14 |
| Cohort | term | 按同期加入分组看留存/LTV 的分析单位 | 2026-05-14 |
| Participating preferred | term | 优先股先拿优先额再参与分剩余(double dip) | 2026-05-14 |
| Protective provisions | term | 优先股对重大事项的否决权(control term) | 2026-05-14 |
| Information rights | term | 定期获取财务/运营数据的合同权利 | 2026-05-14 |
| Pay-to-play | term | 不跟投就被惩罚(转普通股等),寒冬期高频 | 2026-05-14 |
| Recap / cram-down | term | 困境时重整 cap table,老股东常被洗 | 2026-05-14 |
| Valuation cap / discount | term | SAFE/note 转股时保护早期投资人的两机制 | 2026-05-14 |
| MFN clause | term+acronym | 后来者拿到更优条款则本投资人自动升级 | 2026-05-14 |
| Vesting / cliff | term | 股权按时间逐步归属,常带 1 年 cliff | 2026-05-14 |
| Accelerator / incubator | term | 小额+标准条款+辅导+Demo Day 批量投早期 | 2026-05-14 |
| Scout program | term | 给外部 scout 小额资金以基金名义投极早期 | 2026-05-14 |
| Lead investor / co-investor | term | 领投定条款拿 board / 跟投跟条款进 | 2026-05-14 |
| Co-invest | term | GP 给 LP 在具体 deal 上基金外额外投的机会 | 2026-05-14 |
| Side letter | term | 基金与个别 LP 单签的个性化补充协议 | 2026-05-14 |
| LPA | term+acronym | 定义基金一切规则的核心法律文件 | 2026-05-14 |
| Key person clause | term | 关键 GP 离开则基金暂停投资期 | 2026-05-14 |
| Anchor LP | term | 募资早期承诺大额、帮基金起盘的 LP | 2026-05-14 |
| First close / final close | term | 募资分批:首关可开工,终关锁定规模 | 2026-05-14 |
| Placement agent | term | 帮 GP 对接 LP、协助 fundraising 的中介 | 2026-05-14 |
| Tender offer / continuation fund | term | 集中回购老股 / GP 把好资产转入接续基金 | 2026-05-14 |
| Write-off / write-down | term | 把被投公司持仓减记到 0 或大幅下调 | 2026-05-14 |
| Conviction | term | 敢不敢逆共识重注的内在确信程度 | 2026-05-14 |
| Pattern matching | term | 基于过往案例快速类比,双刃剑(固化偏见) | 2026-05-14 |
| Spray-and-pray | term | 投多家小额不深参与,与 concentrated 相对 | 2026-05-14 |
| Solo GP / solo capitalist | term | 一个人独立募资+决策的机构化基金 | 2026-05-14 |
| Up-or-out | term | 限定年限内升不上去就走人,Partner 席位稀缺 | 2026-05-14 |
| Capital efficiency | term | 用多少钱换多少进展,2022 后核心指标 | 2026-05-14 |
| Bridge to nowhere | term | 续了命但无清晰下一里程碑的过桥 | 2026-05-14 |
| Demo Day | term | accelerator 毕业时集中向 VC 路演 | 2026-05-14 |
| QFLP | term+acronym(CN) | 让境外机构换汇投境内 RMB 资产的试点制度 | 2026-05-14 |
| 双 GP | term(CN) | 一支基金由两 GP 合管(投资+募资/资源) | 2026-05-14 |
| 引导基金 | term(CN) | 政府设立、当 LP 的母基金,带返投诉求 | 2026-05-14 |
| Series A crunch / graduation rate | term | 从一轮融到下一轮的比例 / 种子→A 的断层 | 2026-05-14 |

### Standards / Regulations / Certifications 时间轴(仅近 5 年内有显著变化的进表)

| 名称 | Issued | Last revised | Decay | 影响 workflow |
|------|--------|--------------|-------|---------------|
| SEC accredited investor | 1982 | 2020-08(新增专业资格路径);2025 立法推进中 | medium | 募资合规、LP 资格核实 |
| QSBS / §1202 | 1993 | **2025-07-04 OBBBA**(阶梯持有期、上限 1000万→1500万、资产门槛 5000万→7500万) | medium | 投资结构设计、退出税务规划 |
| ILPA Reporting Template | 2016 | **2025-01 v2.0**(2026 起替代旧版) | medium | GP 给 LP 的季度报告 |
| 《私募投资基金监督管理条例》 | **2023-09 施行**(首部行政法规) | 配套规则陆续出 | medium | RMB 基金全流程合规 |
| 中基协登记备案办法 | 2014 起 | **2023-05 新办法施行**(门槛大幅提高) | medium | RMB 基金管理人登记、产品备案 |
| 回购条款相关司法/监管口径 | — | 2023-2024 回购诉讼潮,口径仍在演化 | high | 中国 deal 条款设计、退出执行 |
| — 长期稳定不进表 — | | | | Reg D(1982,506(c) 2013)、3(c)(1)/3(c)(7)(1940)、NVCA Model Docs(持续微调)、SAFE(2018 改 post-money 后稳定) |

---

## 行业「外行破绽」高亮（outsider-tell top 10)

> 最容易在一句话里暴露「没真做过 VC」的误用。Phase 2.5 表达 DNA 节直接素材。

| # | 误用(外行说法) | 内行实际意思 / 反应 | 出现频率 |
|---|----------------|---------------------|---------|
| 1 | 「这家公司估值 1000 万」(不说 pre/post) | 内行第一反应必问 "pre or post?" —— 不指明 pre/post,稀释算不出来 | 极高 |
| 2 | 「VC 的钱」「VC 投了我」(把 VC 当一个人) | 内行清楚是 LP 的钱、GP 受托管理;VC 是 GP-LP 双层结构,GP 自己也要向 LP 募资和被考核 | 极高 |
| 3 | 只看 IRR 高就说基金牛 | "IRR 是 paper,DPI 才是 real" —— IRR 能被 markup 和 capital call 节奏操纵,没 DPI 等于没真退出 | 高 |
| 4 | 把 SAFE 当「可转债 / 一种债」 | SAFE 不是债:无利息、无到期日、清算顺序不同;说 "SAFE 利息" 直接露馅 | 高 |
| 5 | 谈 deal 只看「估值 + 金额」两个数 | 内行同时看 control terms(board、protective provisions)和 economic terms(liq pref、anti-dilution);"participating preferred" 一出现就警觉 | 高 |
| 6 | 「VC 就是分散投资降低风险」 | power law 下过度分散稀释 outlier;真正的风险是 portfolio 里没有一个 fund-returner —— miss 比 loss 致命 | 高 |
| 7 | 把 Demo Day / 看的项目多 当「优质 deal 多」 | 内行知道最稀缺的是 access(能不能挤进顶级 founder 那一轮),sourcing ≠ winning;Demo Day 是 FOMO + 时间压缩环境 | 中高 |
| 8 | 以为「签了 term sheet 钱就到账」 | term sheet 多数条款 non-binding,后面还有 confirmatory diligence 能黄,真正约束的常只有 no-shop | 中高 |
| 9 | 把「中国 VC」当一个整体谈 | 美元基金和 RMB 基金几乎是两个行业:LP 类型、监管、架构、对赌/回购条款、退出路径全不同 | 中高(谈中国市场时) |
| 10 | 把 carry 当 GP 的日常收入 / 把 management fee 当「躺赚」 | 日常工资来自 management fee,carry 是 7-10 年后才兑现的「期权」;2% 看似不多但 10 年累计吃掉约 20% 基金规模 | 中高 |

**补充破绽(register / pronunciation 类)**:
- 开口念全称 "carried interest""due diligence" 而不用 "carry""DD" —— 多半是外人或律师
- TAM/SAM/SOM 按字母拼读(应念 "tam/sam/som");SAFE 念字母 "S-A-F-E"(应念 "safe")
- 滥用 "thesis""conviction""high conviction" 当口头禅 —— 内行用这两个词有具体所指(可证伪的方向判断 / 敢逆共识重注)
- 把 SPV / syndicate 等同于「基金」,把 solo GP 等同于「天使投资人」—— 暴露不懂基金结构
- 把 markup 当「赚到了」—— "markups aren't returns"

---

## 行业拒绝的厂商话术（vendor-speak rejection top 5)

> VC 从业者会本能反感、视为「外行 / 营销味」的厂商包装。拒绝这些 → 反映行业的价值观与反模式。Phase 2.5 表达 DNA 反例版素材。**注:本节为 Phase 2 表达 DNA 候选,每条已尽量挂可追溯 source;无法挂硬 source 的「行业体感」类已标注,Phase 2 须二次校验,不污染 master skill。**

| # | 厂商 / 营销话术 | 行业为何拒绝 | 关联 source |
|---|----------------|--------------|------------|
| 1 | 「用 AI sourcing 工具 = 拥有 deal flow / 拥有 alpha」 | 内行的共识是 sourcing ≠ winning —— 顶级 deal 是被 founder 选,工具能扩大「看到」的量,但拿不到「access」和 conviction;把工具等同于能力是典型外行营销 | 行业体感(对照 Tier 1 #18 deal flow / sourcing 的 insider def);Phase 2 须二次校验 |
| 2 | 「在我们平台一键发 SAFE = 标准化 / 省律师的融资」 | SAFE 文本本身就是 YC 免费开源标准,平台把「填表」包装成增值;且多张 SAFE 叠加的累积稀释才是真问题,一键工具反而掩盖 post-money SAFE 的稀释风险 | evidence: [T06-S012, T06-S015](SAFE 是 YC 开源标准这一事实) |
| 3 | 「Carta = cap table」「我们的工具 = 你的股权管理」 | cap table 是通用财务概念,不属于任何厂商;内行看的是「cap table 健不健康(fully-diluted 口径、有没有 dead equity)」,这是判断不是软件功能 | 对照 Tier 1 #13 cap table;evidence: [T06-S013](Carta 作 vendor docs,定义须 ≥2 源,不采信一面之词) |
| 4 | 把「专家访谈 / expert call = 完成 diligence」 | expert call network(Tegus / AlphaSense / GLG)只是 DD 的一块;早期 VC 的 DD 70% 是 founder judgment 和 market call,off-list reference call 才是核心,买几个专家电话不等于做了尽调 | 对照 Tier 1 #19 DD 的 insider def;Phase 2 须二次校验 |
| 5 | 「数据平台覆盖全市场 deal,用我们就掌握行业全貌」 | 公开 deal 数据(PitchBook / Crunchbase / IT 桔子)系统性偏头部、偏后期,种子 / 早期天使 deal 大量缺失;内行知道「公开数据是冰山一角」,把数据库当 ground truth 是外行 | 对照 intake warnings(数据透明度极差);行业体感,Phase 2 须二次校验 |

**补充被反感的话术(register 层)**:
- GP 个人品牌营销里的「7 步进入 VC」「人人都能做天使投资」—— 与行业真实就业结构(up-or-out、Partner 席位极稀缺)直接冲突
- 把「公开发声多 / LinkedIn 粉丝多」包装成「投资能力强」—— 内行清楚「个人 brand 优秀 ≠ 投资业绩好」,self-promotion 是工作之一但不是 track record
- 厂商把「VC 决策」描述成「数据驱动的客观流程」—— 内行知道早期投资本质是 high-uncertainty judgment,过度「客观化 / 流程化」的叙事是营销

---

## Phase 2 提炼提示

### 「行业表达 DNA」直接素材(喂给 Phase 2.5 expression-DNA 提炼)

**高频黑话 top 10**(入行即用、密度最高):
1. power law / fund-returner —— 一切 portfolio 决策的底层语言
2. carry / management fee / "2 and 20" —— GP 收入结构的口头语
3. DPI / TVPI / IRR("IRR 是 paper,DPI 是 real")
4. pre / post-money("pre or post?" 是反射性追问)
5. SAFE / convertible note / priced round —— 早期融资工具三件套
6. liq pref / anti-dilution / participating preferred —— term sheet 谈判语言
7. deal flow / sourcing / access / "sourcing ≠ winning"
8. thesis / conviction / "high conviction" —— 投资判断的价值观词
9. dry powder / runway / burn / "default alive vs default dead"
10. 中国特色:对赌 / 回购 / 估值倒挂 / 人民币基金 vs 美元基金 / 引导基金 / 双 GP

**行业拒绝的厂商话术 top 5**(拒绝 → 反映行业「价值观 + 反模式」):
1. 「AI sourcing 工具 = 拥有 deal flow / alpha」(反模式:混淆「看到」和「拿到」)
2. 「一键发 SAFE = 标准化融资」(反模式:工具掩盖累积稀释)
3. 「Carta = cap table」(反模式:把判断当软件功能)
4. 「专家访谈 = 完成 diligence」(反模式:买电话替代 founder judgment)
5. 「数据平台 = 行业全貌」(反模式:把偏头部的冰山一角当 ground truth)
+ register 层:「7 步进 VC / 人人能做天使」「公开多 = 投得好」「VC 是数据驱动的客观流程」

**外行破绽 top 10**(insider-only spotting tells,见上「外行破绽高亮」表):
报估值不说 pre/post / 把 VC 当一个人 / 只看 IRR / SAFE 当债 / deal 只看两个数 / 「分散降风险」 / 看的项目多 = deal 好 / 签 term sheet 就到账 / 把中国 VC 当整体 / carry 当日常收入。

### 「智识谱系」线索(喂给 Phase 2.7 智识谱系)

- **融资工具的演变暗示 deal 哲学转向**:convertible note(2013 前主流)→ SAFE pre-money(2013)→ **SAFE post-money(2018)** —— 一步步把「累积稀释的不确定性」从投资人转移给 founder,反映早期融资从「投资人扛风险」向「founder 扛风险 + 简化优先」的哲学迁移。
- **学派之争的「条款层」硬件**:thesis-driven(a16z/USV)vs spray-and-pray(YC/accelerator)vs concentrated(Benchmark)vs solo GP —— 这四派在 portfolio construction、check size、ownership target、是否拿 board 上有可观测的条款差异,是流派之争最硬的落点。
- **报告标准的演进**:ILPA Reporting Template 2016 → v2.0(2025) —— 从「分层、粗口径」到「取消分层、费用/carry 高度颗粒化」,反映 LP-GP 权力关系向「LP 要求更高透明度」倾斜。
- **中美范式分叉**:美国 VC = 纯股权 + NVCA 标准文件 + IPO/M&A 退出;中国 RMB 基金 = 股权 + 对赌/回购(类债化)+ 引导基金 LP(政策诉求)+ A 股退出 —— 同名「VC」实为两套范式,Phase 2 必须按 locale 分章。

### 「时效性」信号(喂给 Phase 2.8 诚实边界)

**过去 12 个月内有修订 / 重大变化的法规 · 标准(共 3 条核心)**:
1. **QSBS / §1202** —— 2025-07-04 OBBBA 重大修订(阶梯持有期、上限 1000万→1500万、资产门槛 5000万→7500万)。**预计 12 月内继续变**:IRS 配套细则、州层面跟进。
2. **ILPA Reporting Template v2.0** —— 2025-01 发布,2026 进入强制采用期。**预计 12 月内**:GP 报告 workflow 实际切换、行业采用细节落地。
3. **中国回购条款司法 / 监管口径** —— 2023-2024 回购诉讼潮后口径仍在演化。**预计 12 月内大概率继续变**(decay risk: high)。

**24 月内可能演化**:SEC accredited investor 定义(多项扩大定义的立法在国会推进)、中国《私募基金监督管理条例》配套规则、QFLP 地方试点细则。

### 「工作流变化触发」种子(喂给 wave 3 Track 03)

近 12 月修订的标准 / 法规 + 它们影响的 workflow 假设:
- **QSBS 2025 修订** → 影响「投资结构设计」和「退出税务规划」workflow:阶梯持有期意味着持有期决策更精细,GP 给 portfolio 公司的退出建议假设要更新。
- **ILPA Reporting Template v2.0(2026 采用)** → 影响「GP 给 LP 的季度报告」workflow:费用 / carry 披露颗粒度要求提升,fund admin 流程和工具配置要调整。
- **中国《私募基金监督管理条例》(2023-09)+ 中基协登记备案新办法(2023-05)** → 影响「RMB 基金设立 / 管理人登记 / 产品备案」workflow:门槛和材料要求提高,新基金 setup 流程变重。
- **回购诉讼潮(2023-2024)** → 影响「中国 deal 条款设计 + 退出执行」workflow:回购条款的谈判、执行、与创始人个人连带相关的风险评估成为新的工作环节。

### 冷僻 / 信号薄弱评估

- 总术语数:**82**(Tier 1 = 38,Tier 2 = 44)—— 远超 floor 40,**不触发冷僻协议**。
- Tier 1 = 38 ≥ 15 ✅;Tier 1 + Tier 2 = 82 ≥ 40 ✅。
- Tier 1 术语 **全部** 填了 outsider-tell ✅;Tier 2 术语 **全部** 填了 outsider-tell(usage/semantic/register 类)✅,远超「50%」要求。
- Standards / Regulations 全部带 issued + last revised 日期字段 ✅。
- **结论:glossary 维度信号充足**。VC 是术语极厚的行业,但需注意 intake warnings 提示的两点 ——(a)公开术语体系成熟,但「实际工作中怎么用 / 怎么博弈」的深度内容仍偏精英化、半公开;(b)中国 RMB 基金部分术语(QFLP / 双 GP / 引导基金)的 source 厚度弱于美国术语,Phase 2 按 locale 分章时应标注「中国特色术语 source 多为监管 / 协会原文,实操细节公开度低于美国」。

### 与其他 Track 的协作提示

- **→ Track 01 (figures)**:Fred Wilson(thesis-driven)、Bill Gurley(concentrated)、Brad Feld(《Venture Deals》= term sheet 圣经)、Scott Kupor(《Secrets of Sand Hill Road》= 基金运营)在长博客 / 书中反复澄清本 glossary 的核心术语,可双向印证;figures 拒绝的厂商话术与本 track「厂商话术拒绝」节互证。
- **→ Track 02 (tools)**:Carta(cap table / 估值)、AngelList(SPV / RUV)、PitchBook/Crunchbase/IT 桔子(deal data)、Tegus/AlphaSense/GLG(expert call)、Affinity/Attio(CRM)直接对应本 track 的术语与「厂商话术拒绝」条目。
- **→ Track 04 (canon)**:《Venture Deals》《Secrets of Sand Hill Road》《The Power Law》是本 glossary 大量术语的第一手定义来源,canon Tier 1 概念与本 track Tier 1 高度重合。
- **→ Track 03 (workflows)**:见上「工作流变化触发种子」。

---

> **本 track 自检**:候选 ≥ 40 ✅(82);5 类分布合理 ✅(term/acronym 厚,regulation 中等,standard 中等,certification 标注 N/A);Tier 1 ≥ 15 ✅(38),Tier 1+2 ≥ 40 ✅(82);Tier 1 全填 outsider-tell ✅,Tier 2 全填 ✅;Standards/Regulations 全带日期 ✅;disputed 术语:本 track 未出现需并列两派定义的术语(中美差异已按 geographic-specific 分别记录,非 disputed);Phase 2 接口五项(表达 DNA / 智识谱系 / 时效信号 / workflow 触发 / 冷僻信号)全部填写 ✅。Manifest:21 条 source(verified_primary 11、surrogate_primary 6、secondary 4,无 blacklisted)。
