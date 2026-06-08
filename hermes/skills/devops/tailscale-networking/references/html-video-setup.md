# html-video 在基地上的安装记录

> 项目：nexu-io/html-video — HTML→MP4 视频生成，支持 Hermes Agent
> 安装日期：2026-06-07
> 位置：/home/miao/html-video/
> 端口：3071 (Studio)

## 安装步骤与坑

### 1. 克隆
- `git clone` 直连 github.com 超时（被墙）
- **解决**：用 API tarball
  ```bash
  curl -L -o /tmp/html-video.tar.gz "https://api.github.com/repos/nexu-io/html-video/tarball/main"
  mkdir html-video && tar xzf /tmp/html-video.tar.gz -C html-video --strip-components=1
  ```

### 2. 依赖安装
- pnpm 不在系统 PATH，在 `~/.hermes/node/bin/pnpm`
  ```bash
  export PATH="/home/miao/.hermes/node/bin:$PATH"
  ```
- `pnpm install` 失败：onnxruntime-node postinstall 下载超时（AI 音频依赖，不影响核心渲染）
  ```bash
  pnpm install --ignore-scripts   # 跳过全部 postinstall
  pnpm install                     # 再跑一次装其余
  ```
- Playwright Chromium 需要手动指定 CLI 路径：
  ```bash
  ./node_modules/.pnpm/playwright@1.60.0/node_modules/playwright/cli.js install chromium
  ```

### 3. 构建
```bash
pnpm build   # 20 个包全部通过
```

### 4. Smoke test
```bash
pnpm smoke   # ✅ 通过，生成 198KB h264 1080p 4.6s MP4
```

### 5. Studio 启动
```bash
node packages/cli/dist/bin.js studio --port 3071
```
- 默认绑定 127.0.0.1，需要远程访问时修改 `packages/cli/dist/studio-server.js`：
  ```
  server.listen(port, '0.0.0.0', () => {  // 原是 '127.0.0.1'
  ```

## 支持的 Agent
- Hermes CLI（本地）✅
- Claude Code、Cursor、Copilot、Aider 等 14 种

## 模板（22 个）
frame-bold-poster, frame-glitch-title, frame-kinetic-type, frame-data-chart-nyt,
frame-electric-studio, frame-product-promo, frame-light-leak-cinema, 等

## 引擎
- Hyperframes（主力，基于 Playwright + ffmpeg）
- Remotion（实验性，需 feat/remotion-adapter 分支）
