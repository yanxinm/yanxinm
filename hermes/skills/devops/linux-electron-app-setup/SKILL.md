---
name: linux-electron-app-setup
description: 在 M710q Ubuntu 基地上安装和运行 Electron 桌面应用的完整流程，包括 npm 镜像、Electron 二进制手动下载、D-Bus 环境修复和 dev 启动。
---

# Linux Electron 应用安装运行

在基地（Ubuntu 22.04 + GNOME + Wayland，有显示器但通过 SSH/远程操作）上安装和运行 Electron 应用的流程。

## 前置条件

- Node.js + pnpm 已装（`npm i -g pnpm`）
- GNOME 桌面已安装且已登录（`loginctl` 确认有 seat0 会话）
- `DISPLAY=:0` 可用（`ls /tmp/.X11-unix/` 确认 X0 存在）

## 安装流程

### 1. 克隆仓库

```bash
# GitHub 被墙走代理
git clone https://ghproxy.net/https://github.com/<owner>/<repo>.git
```

### 2. 安装依赖

```bash
cd <project>
pnpm config set registry https://registry.npmmirror.com
ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ pnpm install
```

### 3. 批准 build scripts（pnpm v9+）

```bash
pnpm approve-builds electron esbuild bufferutil utf-8-validate
```

### 4. 修复 Electron 二进制（如果 postinstall 失败）

如果 `pnpm approve-builds` 后 electron 仍报 "failed to install correctly"：

```bash
# 手动下载
ELECTRON_VER=$(node -e "console.log(require('./node_modules/electron/package.json').version)")
ELECTRON_DIR="./node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/dist"
mkdir -p "$ELECTRON_DIR"
curl -L -o /tmp/electron.zip \
  "https://npmmirror.com/mirrors/electron/v${ELECTRON_VER}/electron-v${ELECTRON_VER}-linux-x64.zip"
cd "$ELECTRON_DIR" && unzip -o /tmp/electron.zip

# 创建 path.txt（注意：不能有换行符！）
printf 'electron' > ./node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/path.txt
chmod +x "$ELECTRON_DIR/electron"
```

**关键坑**：`path.txt` 必须用 `printf` 写，不能用 `echo`，否则末尾换行符会导致 ENOENT 错误。

### 5. 启动（修复 D-Bus）

默认 `DISPLAY=:0 pnpm dev` 会报 D-Bus bus 连接错误，需要显式设置环境变量：

```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
cd <project> && DISPLAY=:0 pnpm dev
```

### 6. 设置便捷别名（可选）

```bash
echo '
alias <appname>="export XDG_RUNTIME_DIR=/run/user/1000 DBUS_SESSION_BUS_ADDRESS=\"unix:path=/run/user/1000/bus\" && cd ~/<project> && DISPLAY=:0 pnpm dev"
' >> ~/.bashrc
```

## 跨平台源码修复

有些 Electron 应用源码硬编码了 Windows 二进制文件名（如 `yt-dlp.exe`、`ffmpeg.exe`），在 Linux 上会 `ENOENT`。需要修改**编译前的 TypeScript 源码**（不是 `dist-electron/` 中的编译产物），加入平台检测：

```typescript
// 修改前（Windows-only）
function getToolPath(): string {
  return 'tool.exe'  // Linux 上直接 ENOENT
}

// 修改后（跨平台）
function getToolPath(): string {
  const isWin = process.platform === 'win32'
  return isWin ? 'tool.exe' : 'tool'
}
```

**实操示例**（videdown 的 `yt-dlp.exe` → `yt-dlp`）：

1. 用 `grep -r "\.exe" electron/ src/` 找到硬编码位置
2. 修改源码文件（如 `electron/main.ts`），参考同项目中已有的跨平台函数（如 `getFfmpegPath`）
3. `pnpm dev` 会自动重新编译 TypeScript → `dist-electron/`

**验证**：修改后 `grep -r "yt-dlp\.exe" dist-electron/` 应无硬编码残留，改为动态检测。

## 常见问题

| 症状 | 原因 | 解决 |
|------|------|------|
| `Failed to connect to the bus` | 缺少 D-Bus 会话地址 | 设置 `DBUS_SESSION_BUS_ADDRESS` |
| `ENOENT: spawn electron\n` | path.txt 有换行符 | 用 `printf` 重写 |
| `Electron failed to install correctly` | 二进制未下载 | 手动下载解压 + 写 path.txt |
| npm 包下载极慢 | registry.npmjs.org 被墙 | 切 npmmirror.com |
| electron 下载极慢 | GitHub releases 被墙 | 设 `ELECTRON_MIRROR` |
| `electron --no-sandbox` 参数 | Linux 下 sandbox 需要额外配置 | 正常，vite-plugin-electron 自动加 |

## 验证

```bash
ps aux | grep '[e]lectron' | wc -l  # 应有 5+ 个进程
```
