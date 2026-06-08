# GStack 技能安装指南

GStack 是 Garry Tan（YC 创始人）开源的 Claude Code 技能合集，提供 47+ 个结构化开发工作流（review、QA、design、ship 等）。ThomasLiu/hermes-harness 是对接 Hermes 的执行框架。

## 安装步骤

### 1. 安装 GStack 核心技能

```bash
git clone --single-branch --depth 1 \
  https://github.com/garrytan/gstack.git \
  ~/.claude/skills/gstack

cd ~/.claude/skills/gstack
./setup
```

`./setup` 会：
- `bun install` 安装依赖（232 packages）
- 编译浏览器二进制 `browse/dist/browse`（~30s）
- 为 10+ 个 AI Agent 平台生成 SKILL.md 文件（包括 Hermes）
- 下载 Playwright Chromium（~167MB，可选，不影响核心技能）

### 2. 注册到 Hermes

GStack 内置了 Hermes 适配，`./setup` 会在 `.hermes/skills/gstack/` 生成 SKILL.md。
将它链接到 Hermes 主技能目录：

```bash
ln -sf ~/.claude/skills/gstack/.hermes/skills/gstack \
  ~/.hermes/skills/gstack
```

验证：`skill_view(name='gstack')` 应返回技能说明书。

### 3. 安装 Hermes Harness（可选）

```bash
mkdir -p ~/Projects
git clone --depth 1 \
  https://github.com/ThomasLiu/hermes-harness.git \
  ~/Projects/hermes-harness

cd ~/Projects/hermes-harness
./bin/hg init
```

依赖：`jq`（`sudo apt install jq`）、Python `pyyaml`（通常已安装）。

## 已安装的 GStack 子技能（47个）

| 分类 | 技能 |
|------|------|
| 规划 | `/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/plan-tune`, `/autoplan` |
| 执行与审查 | `/review`, `/codex`, `/investigate`, `/design-consultation`, `/design-review`, `/design-shotgun`, `/design-html` |
| 测试 | `/qa`, `/qa-only`, `/browse`, `/setup-browser-cookies` |
| 发布 | `/ship`, `/land-and-deploy`, `/canary`, `/document-release` |
| 安全 | `/cso`, `/careful`, `/freeze`, `/guard`, `/unfreeze` |
| 元能力 | `/learn`, `/retro`, `/context-save`, `/context-restore`, `/sync-gbrain` |

## WSL 注意事项

- **Bun**：需手动安装，通过 `bun.sh/install` 或 `npm install -g bun`
- **jq**：`sudo apt install jq`（需用户提供 sudo 密码）
- **Playwright Chromium 下载超时**：`./setup` 最后一步下载 167MB 浏览器，国内网络可能超时。不影响核心技能，仅影响 `$browse` / `/qa` 中打开真实浏览器的功能。可后续单独安装：`cd ~/.claude/skills/gstack && bunx playwright install chromium`
- **Hermes 技能注册**：`./setup` 已自动生成 `.hermes/skills/gstack/`，但需手动 `ln -sf` 到 `~/.hermes/skills/`

## 升级

```bash
cd ~/.claude/skills/gstack && git pull && ./setup
# 如 Hermes 技能路径有变，重新软链接
```
