---
name: hermes-skill-deployment
description: 在 Hermes Agent 中安装、集成和自动加载外部 Skill（非 Hermes Hub 来源）。覆盖 npx skills add 安装、符号链接整合、通过 SOUL.md 注入实现按任务类型自动激活、以及验证流程。
---

# Hermes Skill 部署与自动加载

Class-level skill for deploying third-party skills into Hermes Agent and making them auto-activate without manual loading each session.

## 安装外部 Skill（非 Hermes Hub）

使用 Vercel 生态的 `npx skills add` CLI 安装：

```bash
# 安装仓库中所有 Skill
npx skills add https://github.com/Leonxlnx/taste-skill --yes

# 只装单个 Skill
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend" --yes
```

`npx skills add` 会自动检测 Hermes Agent 并在安装时创建符号链接。

## 文件布局

```
~/.agents/skills/           # npx skills add 安装位置（源目录）
  └── <skill-name>/
      └── SKILL.md          # 完整的 Skill 文档
~/.hermes/skills/           # Hermes 技能目录
  └── <skill-name> -> ../../.agents/skills/<skill-name>/  # 符号链接
```

## 验证安装

```bash
# 检查符号链接
ls -la ~/.hermes/skills/ | grep agents

# 用 Hermes 验证加载（通过 Hermes session 中调用 skill_view）
# skill_view('skill-name') 应返回完整 SKILL.md 内容
```

## 实现自动加载（SOUL.md 注入法）

### 问题

Hermes **没有** `default_skills` 配置项或在 Gateway 模式下自动加载指定 Skill 的机制。`--skills` CLI flag 仅对 CLI 交互模式有效，Gateway/WeChat 会话不生效。

### 方案：SOUL.md 指令注入

SOUL.md 是 Hermes 的主 agent 身份提示，每个会话启动时自动注入系统提示首位（slot #1）。通过在 SOUL.md 中添加指令，可以让 agent 在遇到特定任务类型时自动调用 skill_view() 加载 Skill。

### 操作步骤

编辑 `~/.hermes/SOUL.md`（全局生效）或 `~/.hermes/profiles/<profile>/SOUL.md`（仅某 profile 生效）：

```markdown
## 自动加载 <Skill 名称>

当要求做任何**<任务类型描述>**工作时，你必须：
1. 先调用 skill_view("<skill-install-name>") 加载
2. 按该 Skill 的规则执行
3. 输出前过校验清单（如有）
```

示例（taste-skill）：

```
当要求做任何前端设计/页面开发/UI 视觉/设计类代码生成工作时，你必须：
1. 先调用 skill_view("design-taste-frontend") 加载 taste-skill
2. 按 taste-skill 的三个旋钮（VARIANCE / MOTION / DENSITY）和设计读推理规则执行
3. 输出前跑一遍 pre-flight check 清单
```

可选：同时列出其他变体供 agent 按需选择：

```
也可按需选择其他变体：
- high-end-visual-design — 高端奢华视觉
- minimalist-ui — 极简风格
- gpt-taste — 更激进的 anti-slop
- industrial-brutalist-ui — 硬核工业风
```

### 原理

SOUL.md 内容在每个会话的系统提示中作为首要身份指令注入。LLM 会解读其中的指令并自动遵守。这是一个**软性引导**（依赖 LLM 遵循指令），并非硬性配置，但实践证明有效。

### 局限

- 依赖 LLM 遵守指令，不保证 100% 执行
- 大型 Skill（>50KB）无法内联到 SOUL.md，必须通过 skill_view() 按需加载引用外部位
- 已在会话中修改 SOUL.md 需要新会话（/reset 或 Gateway 重启）才生效
- **SOUL.md 注入仅在技能文件已存在于 skills 目录时有效**：SOUL.md 指令指导 agent `skill_view('skill-name')`，但如果该技能不在 `~/.hermes/skills/` 或当前 profile 的 `skills/` 目录中，skill_view 返回 not found。注入不是自动安装——文件必须实际存在。
- **Profile 技能隔离**：profile 的 skills 目录 (`~/.hermes/profiles/<name>/skills/`) 是全局 `~/.hermes/skills/` 的独立副本（非 symlink）。全局有某个 skill ≠ profile 也能用。需要手动 `cp -r ~/.hermes/skills/<skill> ~/.hermes/profiles/<profile>/skills/` 复制过去。

## 与 Hermes 内置 Skill 的关系

| 来源 | 受保护？ | 示例 |
|------|---------|------|
| Bundled（随 Hermes 发布） | 是，不可编辑 | hermes-agent, autonomous-ai-agents |
| Hub（hermes skills install） | 是，不可编辑 | 来自技能市场的安装 |
| Agent 创建（skill_manage create） | 否，可编辑 | laomiao-writing-style |
| 第三方工具安装（npx skills add） | 否，可编辑/引用 | taste-skill 系列 |

## 典型陷阱

- **SOUL.md 修改后需新会话才生效**：在用 Gateway 时需重启 gateway
- **符号链接目标必须存在**：如果 ~/.agents/skills/ 被清空，~/.hermes/skills/ 的链接会断链，skill_view() 返回 not found
- **重复安装问题**：npx skills add 会 overwrite 已有安装，但不会自动清理旧符号链接
