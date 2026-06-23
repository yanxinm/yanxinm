# npx skills add — Vercel Agent Skills 生态安装指南

将第三方 Agent Skills（如 taste-skill）通过 Vercel 的 [agent-skills](https://github.com/vercel-labs/agent-skills) 生态安装到 Hermes Agent。

## TL;DR

```bash
# 一键安装全部技能
npx skills add https://github.com/Leonxlnx/taste-skill --yes

# 只安装指定技能
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend" --yes
```

## 原理

`npx skills add` 会：
1. Clone 仓库
2. 扫描 `skills/` 目录下的 SKILL.md 文件
3. 自动检测已安装的 agent 工具（Hermes Agent、Claude Code、Codex、Cursor 等）
4. 将 SKILL.md 解压到 `~/.agents/skills/<name>/`
5. **自动创建符号链接** `~/.hermes/skills/<name>` → `../../.agents/skills/<name>`
6. 运行安全风险评估（Socket/Snyk）

## 验证安装

```bash
# 检查符号链接
ls -la ~/.hermes/skills/ | grep agents

# 确认 SKILL.md 存在
ls -la ~/.agents/skills/<name>/
cat ~/.agents/skills/<name>/SKILL.md | head
```

Hermes 中验证（**在当前 session 看不到，需新 session 生效**）：

```
skill_view('<install-name>')
```

## 已验证案例：taste-skill

| 项目 | 值 |
|------|-----|
| 仓库 | `Leonxlnx/taste-skill` |
| 技能数 | 13 个 |
| 安装位置 | `~/.agents/skills/` |
| Hermes 链接 | `~/.hermes/skills/` → `../../.agents/skills/` |
| 验证工具 | `skill_view('design-taste-frontend')` ✅ |
| 安全评估 | Gen: Safe, Socket: 0 alerts, Snyk: Low Risk |

## 安装全部 vs 单个

```bash
# 全部（13 个）
npx skills add https://github.com/Leonxlnx/taste-skill --yes

# 单个
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

# 多个，可重复执行
npx skills add https://github.com/Leonxlnx/taste-skill --skill "high-end-visual-design"
```

## 覆盖更新

```bash
# 重新安装会覆盖已有文件（install name 不变时自动升级）
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

## 注意事项

- `npx skills` 依赖 npm registry，在国内可能需要代理或镜像
- 技能安装后需要**新 session** 才能被 Hermes `skills_list` 看到
- `skill_view()` 可以直接加载刚安装的技能（不受 session 缓存限制）
- 符号链接在 skills 目录，Hermes `profile create --clone` 时可能因断链报错（见 §九 Profile 管理）
- 每个 skill 的 install name 来自 SKILL.md 的 `name:` 字段，不是文件夹名

## 与手动安装的对比

| 对比项 | `npx skills add` | 手动下载（原 §13 方案） |
|--------|-------------------|------------------------|
| 操作步骤 | 1 条命令 | 4-5 步（下载→解压→移动→配 runtime→验证） |
| Hermes 集成 | 自动创建符号链接 | 需手动放入 `~/.hermes/skills/` |
| 安全审计 | ✅ 内置 Socket/Snyk | ❌ 无 |
| 更新 | `npx skills add` 重跑即可 | 手动覆盖 |
| 适用性 | 仅 Vercel agent-skills 生态的仓库 | 任何 SKILL.md 格式的仓库 |
