---
name: linux-desktop-ops
description: Linux GNOME 桌面运维—应用菜单管理、Snap Store 修复、Electron 应用部署。
---

# Linux 桌面运维

适用范围：Ubuntu GNOME 桌面环境（22.04+）。涵盖应用菜单管理、软件中心修复、Electron 应用在 Linux 上的部署。

## 1. 应用菜单（Desktop Entry）管理

### 创建菜单入口
Desktop 文件放在 `~/.local/share/applications/` 下，格式：

```ini
[Desktop Entry]
Type=Application
Name=应用名
Name[zh_CN]=中文名
Exec=/path/to/binary %U
Icon=/path/to/icon.png
Terminal=false
Categories=Network;Utility;
```

### 刷新菜单
```bash
update-desktop-database ~/.local/share/applications/
```
用户侧：`Alt+F2` → `r` → 回车重启 GNOME Shell。

### 提取图标
- **ICO 转 PNG**：`sudo apt install icoutils -y && icotool -x -o /tmp/ input.ico`
- **从网页提取 favicon**：查看页面源码搜索 `favicon` 或 `icon shortcut`，找到 CDN 链接后 curl 下载
- **SVG 占位图标**：找不到官方图标时，生成带文字的自定义 SVG 应急

## 2. Snap Store (Ubuntu Software) 故障修复

### 症状
应用列表能打开，进入具体分类/详情页时一直加载（占位框），内容不显示。

### 根因（按优先级）
1. **`dbus-x11` 未安装** — snap-store 运行在沙箱中，依赖 `dbus-launch` 与系统 D-Bus 通信
2. **apt 源不可达** — 墙外源（security.ubuntu.com, tailscale/pkgs 等）无法访问，PackageKit 后端卡在刷新

### 诊断
```bash
# 检查 dbus-launch
which dbus-launch || echo "需要安装 dbus-x11"

# 查看 snap-store 日志
journalctl -n 30 --no-pager /snap/snap-store/current/usr/bin/snap-store

# 关键日志特征
# "执行子进程 dbus-launch 失败" → dbus-x11 缺失
# "无法下载 http://security.ubuntu.com/..." → apt 源不通
```

### 修复
```bash
# 1. 安装 dbus-x11
sudo apt install dbus-x11 -y

# 2. 修复 apt 源（security.ubuntu.com → 清华镜像）
sudo sed -i 's|http://security.ubuntu.com/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ubuntu|g' /etc/apt/sources.list

# 3. 禁用不可达的第三方源
sudo mv /etc/apt/sources.list.d/nodesource.list /etc/apt/sources.list.d/nodesource.list.disabled
sudo mv /etc/apt/sources.list.d/tailscale.list /etc/apt/sources.list.d/tailscale.list.disabled

# 4. 刷新并重启 snap-store
sudo apt update
pkill -f snap-store
# 从应用菜单重新打开
```

## 3. Electron 应用在国内的部署（GFW 环境）

> 详见 `references/electron-deploy-gfw.md`

关键点：
- 使用 `ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/` 下载二进制
- npm 使用 `https://registry.npmmirror.com` 镜像
- pnpm 新版本可能需要 `pnpm approve-builds` 批准 build scripts
- 手动修复 electron 安装：创建 `path.txt` + 放置二进制到 `dist/` 下

### pitfall: `path.txt` 换行符
`echo "electron" > path.txt` 会在末尾添加换行符，导致路径变成 `electron\n`，引发 `ENOENT`。
正确做法：`printf 'electron' > path.txt`

### pitfall: D-Bus 会话变量
从非 GNOME 会话启动 GUI 应用时，需要设置：
```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
DISPLAY=:0 <command>
```

### pitfall: `--no-sandbox`
无桌面会话或 root 运行时，Electron 可能需要 `--no-sandbox`（vite-plugin-electron 通常自动添加）。
