---
name: multi-profile-team
description: "Hermes 多角色团队全生命周期管理：从零搭建 + 新增成员 + 编写 SOUL.md + 配置路由 + 共享技能。覆盖初始创建和增量扩展两种场景。"
category: devops
tags: [profiles, multi-agent, kanban, routing, team, orchestration]
---

 # 多角色 Profile 团队架构

## ⚡ 新增：给已有团队加新成员的工作流


## ⚡ 新增：给已有团队加新成员的工作流

*参考文件: `references/soul-conventions.md`（SOUL 写作规范）, `references/team-roster.md`（全员花名册）, `references/chinese-llm-provider-setup.md`（国产模型配置——智谱/豆包/DeepSeek）*

当用户说"给团队增加一个小伙伴"时，按以下步骤走：

### Step 1: 取名
选短小精悍的中文拼音，2-6个小写字母。参考：wenan, jike, lvyou, zhidu, sheji。

### Step 2: 建目录
```bash
mkdir -p ~/.hermes/profiles/<name>/{skills,logs,sessions,home}
```
三个核心文件：`config.yaml`, `SOUL.md`, `.env`（可空）。

### Step 3: 写 config.yaml
从已有 profile 复制一份，改模型设置。如果是出图类 profile，需加 `fun-codex` provider：
```yaml
custom_providers:
- api_key: sk-877...b8b8
  base_url: https://slb.apikey.fun/v1
  model: gpt-5.5
  name: fun-codex
```

### Step 4: 写 SOUL.md（灵魂）
每个 profile 的 SOUL.md 遵循统一结构：

| 章节 | 用途 | 必填 |
|---|---|---|
| `# <称号> — 老缪的<角色>` | 角色名+代号 | ✅ |
| 开头段 | "你是老缪（缪言信）的<角色>" | ✅ |
| `## 你的定位` | 一句话职责 | ✅ |
| `## 你的能力范围` | 能力列表 | ✅ |
| `## 你的风格/信条/纪律` | 行为规则 | ✅ |

SOUL 中应引用它需要加载的技能名（如 `apikey-image-gen`），这样后续 prompt 自动加载。

### Step 5: 共享技能
Skills 是 **per-profile** 的。新 profile 需要用的技能得手动复制：
```bash
cp -r ~/.hermes/profiles/jike/skills/apikey-image-gen ~/.hermes/profiles/<name>/skills/
```

### Step 6: 更新路由规则
路由规则存 memory 里。用 `memory(action='replace')` 更新。

### 常见坑

| 坑 | 解 |
|---|---|
| 新 profile 用不了 image-gen | 没复制技能。skills 不跨 profile 共享。 |
| `.env` 不存在 | `touch ~/.hermes/profiles/<name>/.env` |
| 出图失败 → 缺 fun-codex provider | config.yaml 没加 custom_providers |
| memory 满了加不进路由 | 先合并精简已有条目 |

## Profile 模型配置

**模型统一切换方式**：`patch` config.yaml 的 `model.default` 和 `model.provider` 字段。

```bash
# 批量切换所有 profile 的模型
for p in default jike lvyou wenan zhidu sheji; do
  hermes config set model.default <model_name> --profile $p
  hermes config set model.provider custom:<provider_name> --profile $p
done
```

**sheji 特殊配置**：文本走主模型，image_gen toolset 需保留 fun-codex provider 调用 gpt-image-2 出图。

## Pitfalls

| 问题 | 解决 |
|------|------|
| `--clone` 失败 `shutil.Error` | skills 目录有断链，`find ~/.hermes/skills -xtype l -delete` |
| Profile skills 不同步 | 默认 skills 更新后，其他 profile 的副本仍是旧版。共享 skills 用 symlink |
| Gateway 只跑在 default | 其他 profile 的 gateway 需单独启动，一般不需要——任务通过总负责调用 |
| Kanban dispatcher 不干活 | 检查 Gateway 是否在跑：`hermes gateway status` |
| 角色没加载预期 skill | 调用时加 `-s <skill>` 参数强制加载 |
| **Studio 显示模型为空** | config.yaml 缺 `model.default` 字段。检查：`grep "^  default:" ~/.hermes/profiles/<name>/config.yaml`，若无则添加 |
| **custom_providers 401 错误** | `api_key: ${ENV_VAR}` 在 config.yaml 中不会被解析。必须直接写入完整 key：`api_key: xxx.yyy` |
| **批量切换后配置文件损坏** | `hermes config set` 多次调用可能导致 config.yaml 被截断。批量操作后用 `cat ~/.hermes/config.yaml` 验证完整性 |

## Profile 切换原则

1. **默认前台是 `default`**——日常对话、总负责路由都走 default。
2. **任务分配时切换**——需要 jike/wenan/lvyou/sheji/zhidu 执行任务时，切换到对应 profile。
3. **专项长任务**——切换到对应 profile 执行，完成后下一次新对话切回 default。

## 已有团队清单

用户想把不同类别的工作分给专门的 AI 助手（如文案、极客、旅游规划师、制度写手），而不是所有任务都交给一个 agent。

## 架构模型

```
用户（微信/飞书）
      │
      ▼
┌─────────────┐
│  总负责      │  default profile + Gateway
│  收消息→分类  │  路由规则判断任务类型
│  →分派→汇总  │  →调用对应 profile
└──┬──┬──┬───┘
   │  │  │
   ▼  ▼  ▼
 专项 profiles（各司其职，独立记忆）
```

## 搭建流程

### Step 1: 创建 Profiles

```bash
# 创建独立 profile（克隆 default 的配置和 skills）
hermes profile create wenan --clone
hermes profile create jike --clone
hermes profile create lvyou --clone
hermes profile create zhidu --clone

# ⚠️ 若 --clone 失败（断链），先清理
find ~/.hermes/skills -xtype l -delete
rm -rf ~/.hermes/profiles/<name>
# 再重试
```

每个 profile 自动生成 CLI wrapper：`/home/miao/.local/bin/<name>`

### Step 2: 注入 SOUL.md（人格定义）

为每个 profile 写 `~/.hermes/profiles/<name>/SOUL.md`：

- 明确角色代号和定位
- 列出能力范围和限制
- 标注该角色必须加载的 skills
- 定义工作纪律和输出风格
- 设置对老缪的称呼方式

示例结构：
```markdown
# 角色名 — 一句话定位

## 你的定位
## 你的能力范围
## 你的资源
## 工作纪律
```

### Step 3: 配置 Skills

Profile 的 skills 在 `~/.hermes/profiles/<name>/skills/` 目录。`--clone` 会复制 default 的全部 skills。

**注意**：clone 后各 profile 的 skills 是独立副本，更新 default skill 不会自动同步。如需共享，可用 symlink 替代副本。

### Step 4: 初始化 Kanban

```bash
hermes kanban init
# 自动发现所有 profile，创建 kanban.db
```

Gateway 内置调度器每 60 秒 tick 一次，自动分配就绪任务。

### Step 5: 设置 Cron 分工

每个 cron job 可指定 `profile` 参数，让定时任务以特定角色执行：

```bash
# 示例：每周一让文案扫描工作台账
cronjob(action='create',
  name='工作台账扫描',
  schedule='0 9 * * 1',
  profile='wenan',
  skills=['laomiao-writing-style'],
  prompt='扫描 /mnt/e/百度云同步盘/工作台账/ ...',
  deliver='origin')
```

### Step 6: 配置路由规则

在总负责（default profile）的 memory 中写入路由表：

```
路由规则：
含"报告/策划/方案/请示/公文/意识形态/台账"→wenan
含"行程/旅游/酒店/记账/美食"→lvyou
含"脚本/Python/部署/LoRA/代码/运维/报错"→jike
含"制度/考核/管理办法/安全制度/规章"→zhidu
不确定的→总负责直接处理
```

总负责通过 `terminal(command="<profile> chat -q '...' -s <skill>")` 调用专项 profile。

### 复杂任务路由：delegate_task 模式

当任务需要多步骤分析（扫描文件夹、读取大量文件、跨文件数据分析、生成结构化文档），单次 `chat -q` 不够用。改用 `delegate_task` 注入 profile 人格 + 全工具集：

```python
# 总负责（default）中调用 zhitu 执行复杂分析
delegate_task(
  goal="你的分析目标",
  context=f'''
你是老缪的{profile_name}（角色人格注入）。
文件清单：...（列出所有文件路径及说明）
分析要求：
1. 读方案文件了解框架
2. 用 Python (openpyxl/xlrd) 读取 xlsx 提取数据
3. 用 antiword/catdoc/markitdown 读取 doc/docx
4. 找规律 → 输出方案
''',
  toolsets=["terminal", "file", "web"]
)
```

**适用场景**：
- 分析类任务（财务数据挖掘、绩效规律提取、制度起草）
- 需要读取 10+ 文件的批量分析
- 需要 Python 做数据处理和回归

**对比 `chat -q`**：

| 维度 | `terminal("<profile> chat -q")` | `delegate_task` + 人格注入 |
|------|------|------|
| 工具 | 仅 terminal | terminal + file + web + vision |
| 文件读取上限 | 依赖单次上下文 | 可循环读取几十个文件 |
| 数据分析 | 手动描述数据 | Python 写脚本读 xlsx |
| 输出格式 | 文字回复 | 可 write_file 输出文档 |

**坑**：
- 子 agent 没有 user memory（个人偏好/历史记录），context 须写完整
- 子 agent 的 summary 是自述，对外部副作用（文件写入）要核实：`read_file` 确认文件存在再汇报
- 结果语言须在 context 中指定（默认英文），老缪团队任务一律 `context` 里写明"输出中文"

## 已落地团队（老缪专用）

| Profile | 别名 | 代号 | 职责 | 核心 Skill |
|---------|------|------|------|-----------|
| default | — | 赫妹(H) | 总负责，收消息、路由、汇总 | — |
| wenan | wenan | 文墨 | 文案：公文/方案/报告 | laomiao-writing-style |
| jike | jike | 螺丝刀 | 极客：编程/运维/AI工具 | hermes-agent |
| lvyou | lvyou | 路书 | 旅游：行程/记账/美食 | travel-itinerary |
| zhidu | zhidu | 规尺 | 制度：管理/考核/安全制度 | laomiao-writing-style |
| sheji | sheji | 画板 | 设计师：海报/修图/封面/视觉 | apikey-image-gen |

## 验证方法

```bash
# 查看所有 profile
hermes profile list

# 烟雾测试每个角色
wenan chat -q "你是谁？简短回答"
jike chat -q "你是谁？简短回答"
lvyou chat -q "你是谁？简短回答"
zhidu chat -q "你是谁？简短回答"

# 查看 cron 任务
hermes cron list

# 查看 kanban 状态
hermes kanban ls
```

## Pitfalls

| 问题 | 解决 |
|------|------|
| `--clone` 失败 `shutil.Error` | skills 目录有断链，`find ~/.hermes/skills -xtype l -delete` |
| Profile skills 不同步 | 默认 skills 更新后，其他 profile 的副本仍是旧版。共享 skills 用 symlink |
| Gateway 只跑在 default | 其他 profile 的 gateway 需单独启动，一般不需要——任务通过总负责调用 |
| Kanban dispatcher 不干活 | 检查 Gateway 是否在跑：`hermes gateway status` |
| 角色没加载预期 skill | 调用时加 `-s <skill>` 参数强制加载 |
