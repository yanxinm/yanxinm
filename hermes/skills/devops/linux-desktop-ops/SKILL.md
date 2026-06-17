---
name: linux-desktop-ops
description: Linux GNOME 桌面运维—应用菜单管理、Snap Store 修复、PipeWire 音频排障、Electron 应用部署。
---

# Linux 桌面运维

适用范围：Ubuntu GNOME 桌面环境（22.04+）。涵盖应用菜单管理、软件中心修复、PipeWire 音频排障、Electron 应用在 Linux 上的部署。

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

## 3. PipeWire/WirePlumber 音频排障（Ubuntu 22.04+）

Ubuntu 22.04+ 默认用 PipeWire + WirePlumber 替代 PulseAudio。常见"没声音"问题的根因通常是**默认输出设备指向了错误的 sink**（如已断开的蓝牙设备）。

### 诊断流程

```bash
# 1. 确认硬件声卡存在
cat /proc/asound/cards && aplay -l

# 2. 检查 PipeWire 进程
ps aux | grep -E 'pipewire|wireplumber' | grep -v grep

# 3. 列出输出设备和默认值
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
pactl list sinks short        # 全部输出设备
pactl info | grep '默认音频'   # 当前默认输出
pactl list cards | grep -E '活动配置|available|not available'  # 声卡配置和端口状态
```

### 常见根因

| 症状 | 根因 | 验证方法 |
|------|------|----------|
| 无声，HDMI 接电视 | 默认 sink 指向已断开的蓝牙设备 | `pactl info` 看 "默认音频入口" |
| 模拟口无声 | 配置用了 `output:analog-stereo` 但无内置扬声器 | `pactl list cards` 看端口 status |
| 重启后默认输出又变回蓝牙 | WirePlumber 状态文件持久化了旧优先级 | `cat ~/.local/state/wireplumber/default-nodes` |

### 修复步骤

```bash
export XDG_RUNTIME_DIR=/run/user/1000
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# 1. 切换到正确声卡配置（如 HDMI 输出）
pactl set-card-profile alsa_card.pci-0000_00_1f.3 output:hdmi-stereo+input:analog-stereo

# 2. 设默认输出 sink
pactl set-default-sink alsa_output.pci-0000_00_1f.3.hdmi-stereo

# 3. 取消静音 + 调音量
pactl set-sink-mute alsa_output.pci-0000_00_1f.3.hdmi-stereo 0
pactl set-sink-volume alsa_output.pci-0000_00_1f.3.hdmi-stereo 60%
```

### 持久化（防重启丢失）

WirePlumber 在 `~/.local/state/wireplumber/default-nodes` 持久化了默认输出优先级。**pactl 的临时设置会被这个文件覆盖**，必须同步修改：

```bash
cat > ~/.local/state/wireplumber/default-nodes << 'EOF'
[default-nodes]
default.configured.audio.sink=alsa_output.pci-0000_00_1f.3.hdmi-stereo
default.configured.audio.sink.0=alsa_output.pci-0000_00_1f.3.hdmi-stereo
default.configured.audio.sink.1=bluez_output.XX_XX_XX_XX_XX_XX.1
default.configured.audio.sink.2=alsa_output.pci-0000_00_1f.3.analog-stereo
EOF
```

声卡配置（profile）持久化通过 WirePlumber Lua 规则：

```bash
mkdir -p ~/.config/wireplumber/main.lua.d
# 写入 device.profile 匹配规则（见 references/pipewire-audio-persist.lua）
```

### 前置依赖

```bash
sudo apt install pulseaudio-utils -y   # 提供 pactl（PipeWire 系统上 pactl 通过 pipewire-pulse 通信）
```

### 陷阱

- **`pactl` 连接失败**（"拒绝连接"）：未设置 `XDG_RUNTIME_DIR` 和 `DBUS_SESSION_BUS_ADDRESS`。这两个变量在 GNOME 会话中自动存在，但 Hermes terminal 调用的 shell 里不继承，需手动 export。
- **`pw-cli` 报 "主机已关闭"**：同样缺少上述环境变量。
- **M710q 等迷你主机通常无内置扬声器**：`analog-output-speaker` 端口显示 "availability unknown" 为正常。音频应走 HDMI（接电视/显示器）或 3.5mm 耳机口。

## 4. Electron 应用在国内的部署（GFW 环境）

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
