---
name: html-video-base-setup
description: 在 Hermes 基地（M710q Ubuntu）上部署 html-video Studio 并通过 Tailscale 远程访问——从 GitHub API 拉取到构建、渲染、端口暴露的全链路。
triggers:
  - "html-video"
  - "HTML 转视频"
  - "在基地上部署 html-video"
  - "设置 html-video"
---

# html-video 基地部署与远程访问

将 [nexu-io/html-video](https://github.com/nexu-io/html-video)（HTML→MP4 的 Agent 驱动视频工具）部署在基地上，通过 Tailscale 从笔记本远程访问 Studio。

## 1. 前置条件

| 依赖 | 基地状态 | 备注 |
|------|---------|------|
| Node.js | v22+ ✅ | Hermes 自带 |
| pnpm | 需确认 | 路径在 `/home/miao/.hermes/node/bin/pnpm`，`export PATH` 后可用 |
| ffmpeg | 系统自带 ✅ | `/usr/bin/ffmpeg` |
| Tailscale | 已配 ✅ | 基地: 100.86.13.11 |

## 2. 获取源码（GitHub 被封方案）

github.com 直连超时但 `api.github.com` 可达时，用 tarball 替代 git clone：

```bash
# 下载 main 分支 tarball
curl -L -o /tmp/html-video.tar.gz \
  "https://api.github.com/repos/nexu-io/html-video/tarball/main"

# 解压（strip 顶层目录）
mkdir -p /home/miao/html-video
tar xzf /tmp/html-video.tar.gz -C /home/miao/html-video --strip-components=1
```

## 3. 安装依赖

```bash
export PATH="/home/miao/.hermes/node/bin:$PATH"
cd /home/miao/html-video

# 先跳过 postinstall 脚本（onnxruntime-node 下载被墙）
pnpm install --ignore-scripts

# 再跑一次补上其他脚本
pnpm install
```

### 已知坑

- **onnxruntime-node postinstall 失败**：下载 build list 返回 302（被墙），用 `--ignore-scripts` 跳过即可。不影响核心渲染，只影响 AI 配乐功能。
- **Playwright Chromium 下载**：`cd /home/miao/html-video && <playwright-bin> install chromium`，约 113MB。playwright 在 `.pnpm` hoisted 目录下，需直接用绝对路径：
  ```bash
  /home/miao/html-video/node_modules/.pnpm/playwright@1.60.0/node_modules/playwright/cli.js install chromium
  ```

## 4. 构建

```bash
export PATH="/home/miao/.hermes/node/bin:$PATH"
cd /home/miao/html-video && pnpm build
```

## 5. 远程访问：绑定 0.0.0.0

**关键**：studio-server 硬编码监听 `127.0.0.1`，必须修改后才能从笔记本通过 Tailscale 访问。

```bash
# 修改编译后的文件
# 将 server.listen(port, '127.0.0.1', ...) 改为 '0.0.0.0'
```

文件路径：`packages/cli/dist/studio-server.js`，第 1262 行附近。

## 6. 启动 Studio

```bash
export PATH="/home/miao/.hermes/node/bin:$PATH"
cd /home/miao/html-video
node packages/cli/dist/bin.js studio --port 3071 2>&1
```

验证：
```bash
ss -tlnp | grep 3071   # 应显示 0.0.0.0:3071
curl http://127.0.0.1:3071/  # 应返回 200
```

笔记本访问：`http://100.86.13.11:3071`（基地 Tailscale IP + 3071 端口）

## 7. 验证 MP4 导出

```bash
# smoke test
pnpm smoke

# 检查生成的 MP4
ffprobe -v quiet -show_entries stream=codec_name,width,height,duration \
  -of csv=p=0 <output.mp4>
```

## 8. Tailscale 连通性排查

笔记本打不开时常见原因：

| 现象 | 排查 |
|------|------|
| Ping 不通 | `tailscale status` → Ethan 显示 `-`（离线），笔记本任务栏图标点 Connect |
| 跨网络 | 走 DERP relay（显示 `active; relay "xxx"`），延迟较高但可用 |
| 换网络后掉线 | 笔记本从家→单位切 WiFi 后需手动重连 Tailscale |

## 9. Agent 选择

html-video 支持 Hermes Agent（本地 CLI），Studio 中 AGENT 下拉会自动检测到 Hermes 图标。直接用聊天框输入提示词即可驱动生成。

## 参考

- 项目 README：`/home/miao/html-video/README.md`
- 项目 CLAUDE.md：`/home/miao/html-video/CLAUDE.md`（内部开发笔记）
- Smoke test 产物在 `/tmp/html-video-smoke-*/`
- Studio 项目数据在 `/home/miao/html-video/.html-video/`
