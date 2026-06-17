---
name: multi-profile-orchestration
description: 创建和管理多角色 Hermes Profile 团队 —— Profile 创建、SOUL 注入、任务路由、Cron 分工、Kanban 调度。
category: devops
tags: [profiles, multi-agent, orchestration, soul, routing, kanban, cron]
---

# 多角色 Profile 团队编排

## 适用场景

当用户需要将工作拆分为多个专业角色，每个角色由独立的 Hermes Profile 承担时——文案、极客、旅行规划师、制度专家等，按此流程执行。

## 架构模型

```
用户 ─→ 总负责（default profile, Gateway）
              │
              │ 收消息→分类→分派
              ├─→ 角色A profile（terminal 调用）
              ├─→ 角色B profile（terminal 调用）
              └─→ 角色N profile（terminal 调用）
```

总负责保持 Gateway 运行（微信/飞书接入），其他 Profile 不启动独立 Gateway，由总负责通过 `hermes -p <name> chat -q` 单次调用。

## 创建 Profile 的标准流程

### Step 1: 清理断链

`--clone` 会复制所有 skills，断链会中断流程：

```bash
# 检查并删除断链
find /home/miao/.hermes/skills -xtype l -delete
```

### Step 2: 批量创建

```bash
hermes profile create <name> --clone
```

每个 profile 会生成：
- `/home/miao/.hermes/profiles/<name>/` — 配置目录
- `/home/miao/.local/bin/<name>` — CLI wrapper

### Step 3: 注入 SOUL.md

为每个角色写 SOUL.md（路径：`~/.hermes/profiles/<name>/SOUL.md`），内容应包含：
1. **定位**：一句话说明角色身份
2. **职责范围**：具体做什么
3. **风格/信条**：行为准则
4. **资源/环境**：可用工具和路径
5. **纪律**：汇报规范

### Step 4: 烟雾测试

```bash
<name> chat -q "用一句话描述你的角色" 2>&1 | tail -5
```

确认 Profile 能正常启动并加载 SOUL。

## 标准 SOUL 模板

### 文案类
```
- 你是谁，帮谁写什么
- 写作规范和风格要求
- 必须加载的技能
- 排版规范（字体/字号/行距）
- 工作台账路径
```

### 极客类
```
- 技术领域和能力边界
- 工作环境（主机/用户/网络）
- 信条（能不能跑通比好不好看重要）
- 汇报要求（先验证再汇报）
```

### 旅行定制师
```
- 用户出行偏好（逐条列出）
- 工作模板（逐日表格/费用预估/Checklist）
- 记账分类体系
- 酒店搜索限制（三四线城市=用户 App 搜）
```

### 制度规划师
```
- 制度类型清单
- 标准章节结构
- 语言规范（禁用模糊词）
- 审核 checklist
```

## 任务路由规则

在总负责的记忆中写入路由表（memory → target=memory）：

| 关键词 | 路由到 |
|--------|--------|
| 报告/策划/方案/请示/公文/意识形态/台账 | wenan |
| 行程/旅游/酒店/记账/美食/路线 | lvyou |
| 脚本/Python/部署/LoRA/代码/运维/报错/SDXL | jike |
| 制度/考核/管理办法/安全制度/规章/条例 | zhidu |
| 其他/不确定 | 总负责直接处理 |

总负责收到用户任务后：
1. 分析关键词
2. `terminal(command="<profile> chat -q '...'", timeout=120)` 调用
3. 汇总输出回复用户

## Cron 定时任务

| 任务 | 调度 | Profile | 说明 |
|------|------|---------|------|
| 工作台账扫描 | 每周一 9:00 | wenan | 扫描新文档→简报 |
| 月度报告提醒 | 每月25日 9:00 | wenan | 提醒下月工作计划 |
| 意识形态提醒 | 季末25日 9:00 | wenan | 提醒季度自查报告 |

创建命令：
```bash
cronjob(action='create', schedule='0 9 * * 1', profile='wenan', ...)
```

## Kanban 初始化

```bash
hermes kanban init
```

自动发现所有 profiles 作为 assignee。如果 Gateway 在运行，dispatcher 每60秒轮询。

## 常见 Pitfalls

| 问题 | 方案 |
|------|------|
| `--clone` 失败："No such file or directory" | 清理断链：`find ~/.hermes/skills -xtype l -delete` |
| 残骸目录残留 | 重试前 `rm -rf ~/.hermes/profiles/<name>` |
| Memory 已满无法写入路由规则 | 先 `memory(action='remove')` 删非关键条目，再 `add` |
| Profile 不加载 SOUL | 确认 SOUL.md 路径：`~/.hermes/profiles/<name>/SOUL.md` |
| Profile skills 未同步 | `--clone` 复制了 skills，但后续更新不同步。关键技能考虑 symlink |
| Cron 未用正确的 profile | 用 `profile='wenan'` 参数指定，否则走 default |\n| 多个 cron 同日触发冲突 | 错开时间（9:00, 9:30 等），避免同时大量 API 调用 |\n| **`cron_mode: deny` 静默杀死 cron 任务** | profile（`--clone` 创建或默认）的 `approvals.cron_mode: deny` 使 cron worker 在调工具时被审批拦截，任务悄悄挂掉，`hermes cron list` 不显示错误。2026-06-13 实战确认。 | 创建 profile 后立即：`sed -i 's/cron_mode: deny/cron_mode: allow/' ~/.hermes/profiles/<name>/config.yaml`。同时检查 default profile。修改后需重启 Gateway。 |
| **Web UI 群聊里 profile 不说话** | Web UI 的「群聊」功能不是多人在线聊天。只有 default profile 的 Gateway 在运行，其他 profile（jike/lvyou/sheji/wenan/zhidu）Gateway 均为 stopped——它们没有"耳朵"，群里说话不会自动回应。正确用法：对 default（赫妹）说话，赫妹根据关键词分析后通过 `terminal(command="<profile> chat -q '...'")` 调用对应 profile，汇总返回。群聊功能在当前架构下意义不大，推荐直接用路由模式。 |
| **Cron 任务静默失败：`cron_mode: deny`** | `--clone` 创建的 profile 默认带有 `approvals.cron_mode: deny`，定时任务执行到需要审批的命令（terminal/write_file 等）时直接被拒绝，任务悄悄挂掉，`hermes cron list` 不显示任何错误。**创建 profile 后必须改：** `sed -i 's/cron_mode: deny/cron_mode: allow/' ~/.hermes/profiles/<name>/config.yaml`。同时检查 default profile：`grep cron_mode ~/.hermes/config.yaml`。 |
| **API Server 绑定回退到 127.0.0.1** | Gateway 的 API Server 绑定地址由 default profile 的 `platforms.api_server.extra.host` 决定。如果 default config.yaml 中缺少该配置段（`--clone` 不会同步此段，`hermes config set` 可能写到其他 profile），Gateway 回退到 `127.0.0.1`，导致 Tailscale/远程 Web UI 无法连接。**验证：** `grep -A5 '^platforms:' ~/.hermes/config.yaml | grep api_server`，确保存在 `platforms.api_server.extra.host: 0.0.0.0`。修复后需重启 Gateway。 |

## 验证 Checklist

- [ ] `hermes profile list` 显示所有 profile
- [ ] 每个 profile 都能独立执行 `chat -q "你是谁"`
- [ ] SOUL.md 被正确加载（看回复是否体现角色身份）
- [ ] `hermes cron list` 显示正确的定时任务
- [ ] `hermes kanban ls` 可访问
- [ ] 路由规则已写入 memory
- [ ] 总负责能正确分派任务（用实际请求测试）

## 参考文件

- `references/soul-templates.md` — 四个角色的 SOUL.md 完整模板（文案/极客/旅游/制度）
- `references/session-log-2026-06-08.md` — 实战创建五个 profile 的完整执行序列与踩坑记录
