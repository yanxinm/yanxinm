# Track 03 — Workflows (中国保险经纪人 — 当前工作流)

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T03-S001 | https://book.douban.com/subject/35595538/ | verified_primary | 2026-05-04 | 叶云燕 | 5 步销售方法论 |
| T03-S002 | https://book.douban.com/subject/35186050/ | verified_primary | 2026-05-04 | 江立辉 | 保单体检方法论 |
| T03-S003 | https://feed.xyzfm.space/xxxqdegwqba9 | verified_primary | 2026-05-04 | 谷主吕志远 | 高客方案 + 健康告知案例 |
| T03-S004 | https://www.dt.com.cn/baoxianjia | surrogate_primary | 2026-05-04 | 大童 | vendor docs (大童产品官方页) |
| T03-S005 | https://www.iaria.org.cn/zlfwIndex.do?actType=goPathDownByIaria&fileId=70 | verified_primary | 2026-05-04 | 行业协会 | 重疾定义 — 健康告知 + 理赔基线 |
| T03-S006 | https://www.nfra.gov.cn/cn/view/pages/governmentDetail.html?docId=1186437&itemId=861 | verified_primary | 2026-05-04 | NFRA | 利率切换通知 |
| T03-S007 | https://www.shenlanbao.com/jinbang | surrogate_primary | 2026-05-04 | 深蓝保 | vendor docs (测评平台官方页) |
| T03-S008 | https://www.mdrt.org/about-mdrt/whole-person/ | surrogate_primary | 2026-05-04 | MDRT | association (MDRT Whole Person 框架页) |
| T03-S009 | https://www.nfra.gov.cn/cn/view/pages/governmentDetail.html?docId=1185902&itemId=861 | verified_primary | 2026-05-04 | NFRA | 健康保险新规 |
| T03-S010 | https://www.nfra.gov.cn/branch/baoxianxiaoshou | verified_primary | 2026-05-04 | NFRA | 双录管理系统 |

> 一手 = 10/10.

## 必备 workflow (6 个)

### W1. 客户经营 5 步循环 (叶云燕) — evidence: [T03-S001]
- Trigger: 新线索 / 老客户新阶段
- 入门 SOP: 1) Identify 2) Analyze 3) Design 4) Close (双录) 5) Serve + 转介绍
- 资深: skip 标准开场白; optimize Analyze 压到 30 min; add 决策者识别
- last_updated: 2024-09 (利率切换后话术重写)

### W2. 保单体检 (江立辉) — evidence: [T03-S002, T03-S005]
- Trigger: 客户主动 / 转介绍
- 入门 SOP: 1) 保单清单 2) 覆盖审计 3) 续期能力 4) 受益人审查
- 资深: skip 低保额客户全审计; optimize 受益人面谈带配偶; add 保单变更回溯
- last_updated: 2025-Q1 (健康险新规)

### W3. 健康告知 + 投保 (合规中枢) — evidence: [T03-S005, T03-S010]
- Trigger: 投保健康险 / 重疾
- 入门 SOP: 1) 模板获取 2) 客户本人填 3) 智能 / 人工核保 4) 双录 5) 签约
- 资深: skip 简单家庭刚需的人工核保; optimize 主动指出高频踩雷项; add 复述确认
- last_updated: 2025-Q2 (AI 核保试点)

### W4. 利率切换决策 (新增 workflow) — evidence: [T03-S006, T01-S006]
- Trigger: 老客户咨询 + 主动联系 (2024-09 后预定利率切换全行业重写产品形态, 老客户被销售方话术干扰高发)
- 入门 SOP: 1) 老保单盘点 (已缴期/总缴期/现金价值/预定利率) 2) 新方案模拟 (同等保额在 2.5% 利率下的费率) 3) 4 路径决策 (保留/部分减保/全退保/加保新产品) 4) 执行 + 双录确认
- 资深: skip 预定利率 ≤ 2.0% 老保单不做切换分析; optimize 13 个精算师工具一次性出多年期对比图; add 家庭整体保单地图视角而非孤立看单张保单
- 4 路径决策树详细规则:
  - 保留: 老保单收益锁定明确 + 不需流动性
  - 部分减保: 部分提取现金价值用作流动性 + 保留部分原合同
  - 全退保: 现金价值 ≈ 已交保费 + 急需流动性 (高损失场景)
  - 加保新产品: 老合同保留 + 新合同补充其他风险维度
- 反模式 (合规雷区):
  - 「锁定 3.0% 末班车」销售话术 2024-08-31 截止后再用 → 监管违规, 经纪人执业证悬 (evidence: [T03-S006])
  - 不考虑流动性需求, 只看收益率推荐保留 → 客户后续急用钱时被动退保高损失
  - 演示老保单未来分红 / 万能账户结算时把「中档收益」当「预期收益」给客户看 → 销售误导
- 关键工具: 大童保险家产品库 (T03-S004) / 13 个精算师现金价值演算工具 (T02-S011)
- 关键人物: 谷主吕志远 podcast E45-E50 多集深度讨论利率切换 + 老保单 4 路径决策 (evidence: [T01-S006])
- last_updated: 2024-12

### W5. 理赔陪跑 — evidence: [T03-S001, T03-S003]
- Trigger: 客户出险
- 入门 SOP: 1) 报案 2) 资料 3) 提交核赔 4) 协调拒赔 5) 回访
- 资深: skip 标准指导; optimize 内部协调先于法律; add 理赔后家庭重新规划
- last_updated: 2024 (理赔 app 数字化)

### W6. 续期管理 + 客户经营 — evidence: [T03-S001]
- Trigger: 续期月 + 家庭事件
- 入门 SOP: 1) 续期日历 2) 续期前沟通 3) 加保识别 4) 客户档案更新
- 资深: skip 低件均主动提醒; optimize 集中关怀; add 客户分层关怀
- last_updated: 2024-2025

### W7. 同业合规边界 / 拒绝违规跨保司分单 — evidence: [T03-S010, T01-S005, T01-S006, T05-S001]
- Trigger: 同业 (师兄 / 上线 / 跨机构合作伙伴) 邀你「绕过双录拿快单」「电话签约不走双录」「分佣 30-50% 给你帮忙签约」
- 入门 SOP:
  1) 立即识别合规风险: 双录系统 (T03-S010) 是 NFRA 强制, 报行合一后跨保司分单 + 跳过双录 = 经纪人执业证可被吊销, 不论件均多小
  2) 标准化拒绝话术: 「这单我接不了, 不是钱的事 — 双录跳不过去, 报行合一之后保司风控比以前严, 一旦被抽到, 执业证悬. 30 万重疾对客户也是一辈子事, 没双录档案后期理赔起争议我们俩都背锅」
  3) 给替代方案 (保住关系): 「客户嫌麻烦? 让他来一趟我这边, 我半小时给他做完双录 + 健康告知本人填, 走我经纪通道」
  4) 拒绝后档案备份: 微信对话截图存档, 防止后续同业反咬经纪人「不配合」
- 资深路径:
  - skip 解释合规细节 — 资深人直接说「不行」, 不展开监管条文
  - optimize 给具体替代方案 (我帮你做) 比泛泛拒绝更保关系
  - add 跨机构合规习惯: 长期不接「跳双录」邀请的经纪人, 同业渐渐不再邀请, 反而获得「合规名声」, 拿到更多正规合作
- 关键合规依据:
  - 双录强制场景: 大额保单 (≥ 50 万年保费) / 60 岁以上客户 / 投连险 / 万能险等 (NFRA T03-S010)
  - 报行合一: 杜绝渠道返点 + 二次定价, 跨保司分佣需走正规备案 (evidence: [T03-S010, T01-S005])
- 流派立场:
  - 站在经纪人体系 (明亚 / 大童 / 永达理) 一侧: 客户最佳利益 + 监管合规 + 个人执业声誉 (evidence: [T01-S005])
  - 不站代理人体系 (平安体系) 师徒分单文化 — 但不公开贬低师兄, 只强调自己合规要求
- 常见失败模式:
  - 因为是「师兄」碍于面子接单 → 5-10 年后某次理赔争议时合规问题暴露 → 双方都失去职业声誉
  - 直接公开举报同业 → 行业内被孤立, 反而失去后续合作机会 (除非涉及客户重大利益, 走 NFRA 投诉通道)
  - 接单后试图「补双录」(事后录) → 仍是销售误导认定, 不能补救
- 真实案例: 谷主吕志远 podcast 多集讨论同业合规张力 + 「执业证悬」「我们俩都背锅」是经纪人内部高频私聊语 (evidence: [T01-S006, T05-S001])
- last_updated: 2025-Q1 (报行合一加严)
- Decay risk: medium (报行合一 12-18 月持续落地, 拒绝话术稳定)

## 支线 workflow (4 个)

### S1. 高客 Whole Person — evidence: [T03-S008]
### S2. 测评驱动方案 — evidence: [T03-S007]
### S3. 团险 to-B — evidence: [T03-S002]
### S4. 直播销售 (experimental) — evidence: [T03-S010]

(详见 synthesis.md 第 4 节)
