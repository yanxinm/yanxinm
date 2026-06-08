# Track 03 — Workflows (SEO)

> 深度调研 2026-05-02. 5 个标准工作流. cli_writer-friendly 格式. 一手 ≥ 70%.

## 元数据

- 一手 / 二手 / 推断比例: 4 / 1 / 0
- 工作流数量: 5
- 调研深度: 深度 (≥ 350 行)
- 截止: 2026-05-02

---

### 1. 新站 SEO 上线 (90 天打基线)

- **One-liner**: 新站从 0 到拿到第一波 organic 流量的标准动作 — 90 天内站稳 + 索引 + 关键词上榜.
- **Trigger**: 新建站点 / 重构上线 / 新独立站
- **Output**: 站点正常索引 + 50+ 关键词进入 Google top 100 + GSC 性能数据基线建立
- **入门 SOP**:
  1. **技术基线** (Day 1-7):
     - HTTPS + 站点速度 (Core Web Vitals: LCP ≤ 2.5s / INP ≤ 200ms / CLS ≤ 0.1)
     - Mobile-friendly + responsive
     - robots.txt + sitemap.xml 配置
     - Schema markup (Article / Product / Organization 等)
     - 404 / 重定向 处理
  2. **GSC + GA4 接入** (Day 7-10):
     - Google Search Console 验证 + 提交 sitemap
     - Google Analytics 4 接入 + 转化跟踪
     - Bing Webmaster Tools 接入
  3. **关键词研究 + 站点架构** (Day 10-30):
     - Ahrefs / SEMrush / Moz 研究 50-100 个核心关键词
     - Pillar + Cluster 内容架构 (主题枢纽 + 长尾分支)
     - URL 结构 / 内链规划
  4. **首批内容生产** (Day 30-60):
     - 10-20 篇高质量内容 (1500+ 词, E-E-A-T 完整)
     - 作者 bio + 引用源 + 真实经验
     - 图片 alt + 内部链接
  5. **链接建设** (Day 60-90):
     - 内链 audit + 优化
     - 外链 outreach (Skyscraper Technique)
     - PR / Guest post / Resource pages
  6. **数据复盘** (Day 90):
     - GSC 性能数据 (展示 / 点击 / 平均位置)
     - 关键词上榜数 + 排名分布
     - Core Web Vitals 通过率
- **资深路径**:
  - **skip 技术 baseline**: 资深团队第一周技术全过, 不卡每个细节
  - **optimize 用 Pillar + Cluster 架构**: 不押单点关键词
  - **add 国际化 SEO** (Aleyda Solis 流派): hreflang + 多语言版本前置规划
  - **add E-E-A-T 体系化** (Marie Haynes 流派): 作者权威 / 真实经验前置
  - **add AI Search 优化 (GEO)**: 内容结构化 + Schema + 引用密度高
- **常见失败模式**:
  - 不接入 GSC → 没法看 Google 真实数据
  - Core Web Vitals 没过 → 排名跟不上
  - 内容拍脑袋写, 不做关键词研究
  - 链接 spam (买链接 / 链接农场) → Helpful Content Update 团灭
  - AI 直发不加人工 → 限流
- **Last_updated**: 2026-04-15
- **Decay risk**: medium (技术 SEO 框架稳定, AI Search 部分快速变)

---

### 2. 内容 SEO 生产 (Pillar + Cluster)

- **One-liner**: Pillar (主题枢纽) + Cluster (长尾分支) 内容架构, 内容驱动 SEO 标准方法论.
- **Trigger**: 中型品牌内容站 / 持续 SEO 投入 / 内容营销
- **Output**: 50+ 篇内容矩阵, Pillar 拿头部排名 + Cluster 拿长尾流量, 整站 DA 持续上升
- **入门 SOP**:
  1. **关键词聚类** (Week 1):
     - Ahrefs / SEMrush 找 5-10 个 Pillar 主题词 (高搜索量 + 高难度)
     - 每个 Pillar 找 20-30 个 Cluster 长尾词 (中等搜索量 + 中等难度)
  2. **Pillar 内容写作** (Week 2-4):
     - 每个 Pillar 一篇 3000-5000 词长内容
     - 全面覆盖主题 + 内部跳转到 Cluster
     - E-E-A-T 完整 (作者 / 引用 / 真实经验)
     - Schema markup (Article + FAQ)
  3. **Cluster 内容批量** (Week 4-12):
     - 每个 Cluster 一篇 1500-2500 词
     - 内链回 Pillar (用主题相关锚文本)
     - 子主题深度 + 实战案例
  4. **内链优化** (Week 12-13):
     - Pillar 跟 Cluster 内链双向
     - 锚文本 (anchor text) 自然多样化
     - 站点架构扁平 (≤ 3 click 可达任何页)
  5. **持续优化** (持续):
     - 每月看 GSC 性能数据
     - 头部排名 Cluster 复刻 + 拓展
     - 衰减内容 (12+ 月旧) 更新 + 重新发布
- **资深路径**:
  - **skip 单纯长内容堆字数**: 资深做内容深度 + 真实见解, 不为长而长
  - **optimize 用 AI 辅助内容大纲**: Surfer SEO / Clearscope 内容评分 + AI 大纲 + 真人填写
  - **add 视频 / 播客内容**: YouTube / Spotify SEO 协同, 跨内容形式
  - **add 国际化复刻**: 头部 Pillar 翻译 + 文化适配 + hreflang
- **常见失败模式**:
  - Pillar 太多, Cluster 不够 → 主题深度不够
  - Cluster 没内链回 Pillar → SEO 价值散失
  - AI 全自动生成不加人工 → Helpful Content 限流
  - 内容更新周期 > 12 月不动 → 内容衰减
  - 锚文本 100% exact match → 算法识别 spam
- **Last_updated**: 2026-04-20
- **Decay risk**: low (Pillar + Cluster 框架稳定, 具体策略调整)

---

### 3. 技术 SEO 审计 (Site Audit + Crawlability)

- **One-liner**: 技术 SEO 审计的标准动作 — Crawlability + Indexability + Site Speed + Schema 4 件套.
- **Trigger**: 大站重构 / 流量异常 / 季度审计
- **Output**: 技术 SEO 报告 + 问题清单 + 修复优先级 + ROI 评估
- **入门 SOP**:
  1. **Crawlability 审计** (Day 1-2):
     - Screaming Frog 全站爬取
     - robots.txt + sitemap.xml + canonical 检查
     - 死链 (404) + 重定向 (301/302) 链
     - 内链 audit (内链结构 / 锚文本)
  2. **Indexability 审计** (Day 2-3):
     - GSC 索引状态报告
     - noindex / nofollow 误用
     - 重复内容 / canonical 错误
     - JS 渲染 (Google 是否能爬到 JS 生成内容)
  3. **Core Web Vitals 审计** (Day 3-5):
     - PageSpeed Insights / Lighthouse 跑核心页
     - LCP (≤ 2.5s) / INP (≤ 200ms) / CLS (≤ 0.1) 三件套
     - 性能优化 (图片 lazy load / CDN / minify)
  4. **Schema markup 审计** (Day 5-7):
     - 关键页面 Schema (Article / Product / FAQ / Organization)
     - Rich Results Test 验证
     - Schema vocabulary 选用合理 (不过度堆砌)
  5. **修复优先级 + ROI 评估** (Day 7-10):
     - 高优先级: 影响排名 / 索引
     - 中优先级: 影响 CTR / 用户体验
     - 低优先级: 长期优化
- **资深路径**:
  - **skip 一刀切做全站审计**: 资深先看 GSC 数据找异常页, 不浪费精力
  - **optimize 用 Sitebulb 可视化**: 站点架构图比 Excel 表格直观
  - **add 国际化技术 SEO**: hreflang / locale-specific URL / CDN
  - **add JS-heavy SPA 优化**: SSR / SSG / hydration / Schema 注入
- **常见失败模式**:
  - 只看技术不看流量 → 技术全过排名也不一定起来
  - Core Web Vitals 一刀切优化 → 跨设备不同
  - Schema 堆砌 → 算法识别 spam
  - JS 渲染不验证 → Google 没爬到内容
- **Last_updated**: 2026-04-25
- **Decay risk**: medium (技术 SEO 框架稳定, Core Web Vitals 阈值 12-24 月调整)

---

### 4. 链接建设 (Link Building) — 白帽路径

- **One-liner**: 高质量外链是 SEO 长期权重 — 白帽路径, 不要走链接农场 / 买链接.
- **Trigger**: 中大型项目 / 6-12 月长期 SEO 投入
- **Output**: 50-200 个高质量链接 (DA 30+), 整站 DA 上升 + 头部关键词排名上升
- **入门 SOP**:
  1. **当前链接 audit** (Week 1):
     - Ahrefs / SEMrush 看现有链接
     - 砍掉 toxic links (Disavow)
     - 找出最强链接 (anchor / DA / 主题相关性)
  2. **Skyscraper Technique** (Week 2-4):
     - 找最强对手内容 (Ahrefs Top Pages)
     - 写一份更好版本 (更长 + 更深 + 更新)
     - 给链向对手内容的人 outreach (要求改链接到你)
  3. **Resource Pages** (持续):
     - 找类目相关的 resource pages
     - Outreach + 加入 list
  4. **PR / Guest Post** (持续):
     - 跟行业媒体 / 头部博客 outreach
     - Guest post (高质量内容投稿)
     - HARO / Help A Reporter (记者约稿)
  5. **内容驱动链接** (持续):
     - 写「值得被链接」内容 (data study / 工具 / 长篇 guide)
     - 等待自然链接 + 主动 outreach
- **资深路径**:
  - **skip 链接数量焦虑**: 10 个 DA 50+ 链接 > 100 个 DA 10 链接
  - **optimize Outreach 模板个性化**: 不要批量发 spam 邮件
  - **add 跨主题内容**: 头部品牌做主题相关性高的内容矩阵
  - **add Digital PR**: 媒体关系 + 数据 study + 行业报告
- **常见失败模式**:
  - 买链接 / 链接农场 → 一更新就团灭
  - Anchor text 100% exact match → 算法识别 spam
  - Outreach 批量 spam → 邮箱黑名单
  - Disavow 不做 → toxic links 拖累整站
- **Last_updated**: 2026-04-15
- **Decay risk**: medium (白帽链接建设框架稳定, 但 spam 工具一直在变)

---

### 5. AI Search 优化 (GEO / LLMO) — 2024-2026 新流派

- **One-liner**: 在 AI Overviews / ChatGPT / Perplexity / Claude 中被引用比传统排名重要 — Generative Engine Optimization.
- **Trigger**: 2024-2026 内容站 / 头部品牌 / 信息类内容
- **Output**: AI search 可见度提升 30-40%, 品牌 mention 在 LLM 输出中提升, GEO ROI 6-12 月 300-500%
- **入门 SOP**:
  1. **AI Search 监控接入** (Week 1):
     - Otterly.ai / Profound / Peec AI 接入
     - 监控品牌在 ChatGPT / Perplexity / AI Overviews 中的 mention
     - Baseline 数据建立
  2. **内容 GEO 优化** (Week 2-4):
     - 文章开头 1-2 段直接答案 (LLM 喜欢直接信号)
     - 结构化标题 (H2/H3 清晰, 类似 FAQ)
     - 数据 / 引用密度高 (LLM 引用 source 时偏好高密度数据内容)
     - Schema markup (Article + FAQ + HowTo)
  3. **E-E-A-T 强化** (Week 2-4):
     - 作者权威 (bio / credentials / publication record)
     - Expert quotes + 引用源
     - 真实经验 (case study / data study)
  4. **被 LLM 引用** (持续):
     - 找 ChatGPT / Perplexity 触发的关键词 (用 Otterly.ai)
     - 优化对应内容
     - 监控 AI Overview 引用 (76% 引用 URL 也排 Google top 10)
  5. **跨平台 AI 可见度** (持续):
     - YouTube SEO (LLM 也引用视频 transcript)
     - Reddit / Quora / Wikipedia 提及
     - 跨平台一致性 (品牌信号一致)
- **资深路径**:
  - **skip 单纯堆字数**: AI 喜欢精炼 + 数据密集 + 直接答案
  - **optimize 内容结构化**: 类似 Wikipedia 结构, LLM 引用率高
  - **add 数据 study / 行业报告**: 原创数据是 LLM 引用首选
  - **add 跨语言 GEO**: 多语言 + 多文化适配
- **常见失败模式**:
  - 内容结构散漫 → LLM 没法精准引用
  - 数据密度低 → LLM 引用首选高密度内容
  - Schema markup 缺失 → AI 解析困难
  - 不监控 → 不知道哪些内容被引用
- **Last_updated**: 2026-04-30
- **Decay risk**: high (AI Search / GEO 是 2024-2026 新学科, 方法论 6-12 月迭代)

---

## 工作流之间的关系

```
新站 SEO 上线 (workflow 1)
   │
   │  90 天打基线后
   ↓
内容 SEO 生产 (workflow 2)  ←→  技术 SEO 审计 (workflow 3)
   │                              │
   │  内容矩阵                    │  季度审计
   ↓                              ↓
链接建设 (workflow 4)
   │
   │  6-12 月长期
   ↓
AI Search 优化 (workflow 5, 2024-2026 新流派)
   │
   ↓
头部品牌闭环
```

**典型路径**:
- 新独立站: workflow 1 → workflow 2 → workflow 3 (季度)
- 中型品牌: workflow 1-3 + workflow 4 (链接长期)
- 头部品牌 / 2026+: workflow 1-5 全闭环 + AI Search 优化

---

## Phase 2 提炼提示

每个工作流抽: **一句话抽象 + 决策规则 + 失败模式**.

- workflow 1 → 决策规则: 「新站 90 天打技术基线 + GSC 接入 + 关键词研究 + 首批内容 + 首批链接」
- workflow 2 → 决策规则: 「Pillar + Cluster 架构, 不押单点关键词」
- workflow 3 → 决策规则: 「Crawlability + Indexability + Core Web Vitals + Schema 4 件套」
- workflow 4 → 决策规则: 「链接质量 > 数量, 白帽路径不走 spam」
- workflow 5 → 决策规则: 「AI Search 优化是 2024-2026 新学科, 内容结构化 + 数据密度 + E-E-A-T 强化」

详见 `synthesis.md` Section 2 + Section 9 (Agentic Protocol 维度).
