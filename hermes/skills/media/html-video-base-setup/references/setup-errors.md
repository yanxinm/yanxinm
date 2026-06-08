# html-video 基地部署故障实录

## 2026-06-07 首次部署

### 1. onnxruntime-node 下载失败

```
Error: Failed to download build list. HTTP status code = 302
```

根因：`https://github.com/microsoft/onnxruntime/releases/download/...` 被墙返回 302。

解决：`pnpm install --ignore-scripts` 跳过 postinstall，不影响核心渲染。

### 2. GitHub git clone 超时

```
git clone https://github.com/nexu-io/html-video.git → 超时 60s/120s
```

`github.com` 不通但 `api.github.com` 可达。解决：用 API tarball 下载（约 6.9MB，速度 ~170KB/s）。

### 3. pnpm 找不到

```
bash: 找不到命令 "pnpm"
```

pnpm 装在 Hermes node 目录：`/home/miao/.hermes/node/bin/pnpm`，v11.5.2。
每次新 shell 需 `export PATH="/home/miao/.hermes/node/bin:$PATH"`。

### 4. Studio 127.0.0.1 绑定

`packages/cli/dist/studio-server.js` 第 1262 行硬编码：
```
server.listen(port, '127.0.0.1', ...)
```
改为 `'0.0.0.0'` 后笔记本才能通过 Tailscale 访问。

### 5. Export MP4 "Failed to fetch"

笔记本端出现此错误时，基地后端 API 正常（curl 127.0.0.1:3071/api/projects 返回 200）。
排查路径：
- `tailscale status` → Ethan 显示 `-` 即离线
- 笔记本 Tailscale 图标可能灰色，需手动 Connect
- 重新连接后走 DERP relay（`active; relay "sea"`），延迟较高但可用

### 6. Playwright 找不到

`npx playwright install chromium` 报 `playwright: not found`。
pnpm workspace 下 playwright 在 `.pnpm` hoisted 目录，非全局可执行。
正确命令：
```bash
/home/miao/html-video/node_modules/.pnpm/playwright@1.60.0/node_modules/playwright/cli.js install chromium
```
