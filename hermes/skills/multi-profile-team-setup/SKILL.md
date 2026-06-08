---
name: multi-profile-team-setup
description: 使用 Hermes Profiles 搭建多角色 AI 团队——创建、配置、调度、维护的完整工作流。
category: devops
tags: [multi-agent, profiles, team, orchestration, kanban, cron]
---

# 多角色 AI 团队搭建

## 适用场景

需要将不同类任务分派给不同"角色"（每角色一个 Hermes Profile），实现分工协作、独立记忆、并行执行。

## 角色设计原则

| 原则 | 说明 |
|------|------|
| 职责单一 | 每 profile 只管一类事（文案/极客/旅游/制度），不越界 |
| SOUL.md 定义人格 | 写清角色名、职责范围、工作风格、资源路径 |
| 技能按需加载 | 每 profile 只加载用得到的 skill，别全克隆 |
| 路由由总负责执行 | 总负责（default profile）收消息→分类→调用对应 profile |

## 搭建流程

### Step 1: 清理断链（关键前置）
```bash
# clone 时 copytree 遇到断链会整体失败
find ~/.hermes/skills -xtype l -delete
```

### Step 2: 创建 Profiles
```bash
hermes profile create <name> --clone   # 克隆 config/.env/skills 从 default
```
创建后自动生成 wrapper：`/home/<user>/.local/bin/<name>`

### Step 3: 写 SOUL.md
```bash
# 路径：~/.hermes/profiles/<name>/SOUL.md
```
SOUL.md 包含：
- 角色代号和定位
- 职责范围（具体到文档类型/技术领域）
- 工作风格和纪律
- 可用资源和路径
- 关键约束（如"不确定标注待核实""不编造"）

### Step 4: 验证 Profile 可用
```bash
<name> chat -q "你是谁？用一句话回答"
```
检查是否加载了 SOUL.md 人格、是否正确加载了技能。

### Step 5: 初始化 Kanban（可选）
```bash
hermes kanban init      # 自动发现所有 profiles
```
Kanban dispatcher 嵌入在 Gateway 中，每 60 秒 tick 一次。

### Step 6: 配置 Cron 定时任务
```bash
# 指定 profile 执行的 cron
hermes cron create "0 9 * * 1" \
  --profile wenan \
  --skills laomiao-writing-style \
  --prompt "每周一台账扫描..."
```

### Step 7: 路由规则写入记忆
总负责（default profile）的 memory 中写入路由表，格式：
```
路由规则：含"报告/策划/方案"→wenan；"行程/旅游"→lvyou；"脚本/代码"→jike；"制度/规章"→zhidu
```

## 日常运作模式

```
用户发消息 → Gateway(default/总负责) → 分析关键词
  ├─ 文案类 → terminal: wenan chat -q "..."
  ├─ 旅游类 → terminal: lvyou chat -q "..."
  ├─ 极客类 → terminal: jike chat -q "..."
  └─ 制度类 → terminal: zhidu chat -q "..."
→ 汇总结果 → 回复用户
```

## Pitfalls

| 问题 | 原因 | 解决 |
|------|------|------|
| `profile create --clone` 全部失败 | `~/.hermes/skills/` 有断链 | `find -xtype l -delete` |
| Profile 响应不像角色 | SOUL.md 未写或路径不对 | 确认 `~/.hermes/profiles/<name>/SOUL.md` 存在 |
| 克隆的 skills 不同步 | 默认是文件拷贝不是 symlink | 后续可用 `ln -sf` 替换关键 skill 为 symlink |
| Gateway 只能在一个 profile | Gateway 绑定 default | 其他 profile 通过 `terminal(command="<name> chat -q ...")` 调用 |
| Kanban 空转不分配 | dispatcher 只在 Gateway 内运行 | 确保 Gateway 在跑：`hermes gateway status` |

## 参考案例

`references/team-roster-example.md` — 老缪五人团队（总负责+文案+极客+旅游定制师+制度规划师）完整配置，含 SOUL.md 要点、路由规则、Cron 配置、批量创建命令。
