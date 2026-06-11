# 老缪的 AI 团队花名册

| Profile | 角色 | 代号 | 路由关键词 | 技能依赖 |
|---|---|---|---|---|
| default | 总负责 | — | — | 全部 |
| wenan | 文案 | 文墨 | 报告/策划/方案/请示/公文/意识形态/台账 | laomiao-writing-style |
| jike | 极客 | 螺丝刀 | 脚本/Python/部署/LoRA/代码/运维/报错 | apikey-image-gen, 各类 devops |
| lvyou | 旅游定制师 | 路书 | 行程/旅游/酒店/记账/美食 | travel-itinerary |
| zhidu | 制度规划师 | 规尺 | 制度/考核/管理办法/安全制度/规章 | laomiao-writing-style |
| sheji | 设计师 | 画板 | 海报/设计/修图/封面/视觉/出图/美工 | apikey-image-gen |

## 调度规则

1. **第一优先**: 关键词匹配路由 → 分派给对应 profile
2. **无匹配**: default profile 自己处理
3. **Kanban**: gateway 的 Kanban dispatch 会按 config.yaml 中的 `kanban.dispatch_in_gateway: true` 自动分派任务

## 创建时间

- 2026-06-08: wenan, jike, lvyou, zhidu (初始搭建)
- 2026-06-10: sheji (增量加入，专供视觉创作)

## Cron 任务

| 任务 | 频率 | 执行 profile |
|---|---|---|
| 台账扫描 | 每周一 9:00 | wenan |
| 月度报告提醒 | 每月25日 9:00 | wenan |
| 意识形态提醒 | 季末25日 9:00 | wenan |
