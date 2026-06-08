# html-video 项目部署记录

> 日期：2026-06-07 | 项目：nexu-io/html-video | 基地：M710q Ubuntu

## 环境要求

| 依赖 | 版本 | 来源 |
|------|------|------|
| Node.js | ≥20 (基地 v22.22.3) | Hermes 自带 |
| pnpm | ≥9 (基地 v11.5.2) | npm install -g，在 `~/.hermes/node/bin/pnpm` |
| ffmpeg | 任意 (基地系统自带) | apt |
| Playwright Chromium | ≥1.49 | 渲染引擎需要 |

## 部署步骤

```bash
# 1. 设置 PATH（pnpm 在 Hermes node 目录下）
export PATH="/home/miao/.hermes/node/bin:$PATH"

# 2. 下载（github.com 被墙，用 api.github.com tarball）
curl -L -o /tmp/html-video.tar.gz \
  "https://api.github.com/repos/nexu-io/html-video/tarball/main"
tar xzf /tmp/html-video.tar.gz -C /home/miao/html-video --strip-components=1

# 3. 安装依赖（跳过 onnxruntime-node postinstall，它下载被墙）
pnpm install --ignore-scripts

# 4. 安装 Playwright Chromium（不能用 npx/pnpm exec，需直接调 CLI）
node_modules/.pnpm/playwright@*/node_modules/playwright/cli.js install chromium

# 5. 构建
pnpm build

# 6. 修改监听地址（默认 127.0.0.1 → 0.0.0.0）
# packages/cli/dist/studio-server.js 中：
#   server.listen(port, '127.0.0.1', ...)  →  server.listen(port, '0.0.0.0', ...)

# 7. 启动 Studio
node packages/cli/dist/bin.js studio --port 3071
```

## 关键坑点

### 1. github.com 被墙
- git clone 超时，但 api.github.com 可通
- 解：用 tarball 方式 `api.github.com/repos/.../tarball/main`
- curl 下载 6.9MB，约需 60s+

### 2. onnxruntime-node 下载失败
- postinstall 从 onnxruntime.ai 下载二进制，国内超时
- 解：`--ignore-scripts` 跳过，AI 音频功能不可用但核心渲染正常

### 3. Playwright CLI 路径
- `npx playwright` 和 `pnpm exec playwright` 都找不到
- 解：直接用 `node_modules/.pnpm/playwright@*/node_modules/playwright/cli.js`

### 4. Studio 监听地址
- 默认 `127.0.0.1`，远程访问不到
- 解：patch `studio-server.js` 改成 `0.0.0.0`

### 5. 远程访问
- 通过 Tailscale IP (100.86.13.11) + 端口 3071
- Tailscale 网络切换会断连，需确认任务栏图标绿

## 验证

```bash
# smoke test
pnpm smoke

# API 测试
curl http://127.0.0.1:3071/api/projects
curl -X POST http://127.0.0.1:3071/api/projects/<proj_id>/export
```
