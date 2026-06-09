# Electron 应用国内部署参考（GFW 环境）

## 典型部署流程（以 Videdown 为例）

### 1. 基础依赖
```bash
npm i -g pnpm
pip3 install yt-dlp -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2. pnpm install（镜像 + approve-builds）
```bash
npm config set registry https://registry.npmmirror.com
ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ pnpm install

# 新版本 pnpm（v8+）可能拦截 build scripts
pnpm approve-builds electron esbuild bufferutil utf-8-validate
```

### 3. 手动修复 electron 二进制
当 `pnpm approve-builds` 后 electron 仍报 `Electron failed to install correctly`：

```bash
# 确认电子二进制不存在
ls node_modules/.pnpm/electron@*/node_modules/electron/dist/electron

# 手动下载解压
ELECTRON_VER="30.0.1"
ELECTRON_DIR="node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/dist"
mkdir -p "$ELECTRON_DIR"
curl -L -o /tmp/electron.zip \
  "https://npmmirror.com/mirrors/electron/v${ELECTRON_VER}/electron-v${ELECTRON_VER}-linux-x64.zip"
unzip -o /tmp/electron.zip -d "$ELECTRON_DIR"

# 创建 path.txt（无换行！）
printf 'electron' > node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/path.txt
chmod +x "$ELECTRON_DIR/electron"
```

**关键 pitfall**：`echo "electron" > path.txt` 会在末尾加 `\n`，导致路径变成 `electron\n`，spawn 时报 `ENOENT`。必须用 `printf 'electron'`。

### 4. D-Bus 会话环境
从非登录 shell（如 SSH、cron、systemd service）启动 Electron GUI：

```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
DISPLAY=:0 pnpm dev
```

否则会报 `Failed to connect to the bus: Unknown address type` 或 `dbus-launch` 缺失。

### 5. 跨平台源码适配
很多 Electron 应用硬编码了 Windows 路径（如 `yt-dlp.exe`），Linux 部署时需修改源码：

```typescript
// 修改前
return 'yt-dlp.exe'

// 修改后（参考 ffmpeg 的跨平台处理）
const isWin = process.platform === 'win32'
const ytDlpName = isWin ? 'yt-dlp.exe' : 'yt-dlp'
```

修改后 `vite-plugin-electron` 会自动重新编译到 `dist-electron/`。

## 常见错误速查

| 错误 | 原因 | 修复 |
|------|------|------|
| `Electron failed to install correctly` | electron 二进制未下载 | 手动下载 + 创建 path.txt |
| `spawn electron ENOENT` | path.txt 有换行符 | `printf` 替代 `echo` |
| `Failed to connect to the bus` | 缺少 D-Bus 会话变量 | 设置上述两个环境变量 |
| `spawn yt-dlp.exe ENOENT` | 硬编码 Windows 路径 | 源码改为跨平台检测 |
| `pnpm: build scripts ignored` | pnpm 安全策略 | `pnpm approve-builds` |
| npm install 下载极慢 | 直连 npm registry | 切 npmmirror |
