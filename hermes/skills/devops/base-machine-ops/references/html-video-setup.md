# html-video 项目（nexu-io/html-video）

> 安装于 2026-06-07，@ `/home/miao/html-video/`

## 项目概述

HTML→Video 开源 Meta-aggregator。混合 Hyperframes + Remotion 引擎，22 个模板，支持 Hermes Agent 驱动。

## 启动与访问

```bash
export PATH="/home/miao/.hermes/node/bin:$PATH"
cd /home/miao/html-video

# Studio（Web 界面）
node packages/cli/dist/bin.js studio --port 3071
# → http://100.86.13.11:3071

# Smoke test
pnpm smoke

# 构建
pnpm build
```

## 关键修改

- `packages/cli/dist/studio-server.js` L1262：`127.0.0.1` → `0.0.0.0`（为了 Tailscale 远程访问）
- 原因：上游硬编码 `server.listen(port, '127.0.0.1', ...)`，每次 rebuild 后需要重新 patch

## 依赖环境

| 组件 | 路径/版本 |
|------|----------|
| pnpm | `/home/miao/.hermes/node/bin/pnpm` (v11.5.2) |
| Node | v22.22.3 (Hermes 自带) |
| ffmpeg | `/usr/bin/ffmpeg` (系统) |
| Playwright Chromium | `~/.cache/ms-playwright/chromium_headless_shell-1223` |
| Playwright CLI | `node_modules/.pnpm/playwright@1.60.0/.../cli.js` |

## 已知问题

- `onnxruntime-node` postinstall 下载被墙→用 `pnpm install --ignore-scripts` 跳过（不影响核心渲染）
- `github.com` git clone 被墙→用 `api.github.com` tarball 下载
