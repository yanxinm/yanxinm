# Ubuntu Software (Snap Store) 空白/加载失败修复

## 症状

Ubuntu Software 打开后分类列表显示空白占位框（`…`），进入应用详情无响应。

## 诊断步骤

```bash
# 1. 检查 snap-store 进程日志
journalctl -n 30 --no-pager /snap/snap-store/*/usr/bin/snap-store

# 2. 检查 dbus-launch（最关键）
which dbus-launch  # 若无输出 = 根因
```

## 根因一：dbus-x11 未安装

Snap Store 运行在 snap 沙箱中，需要 `dbus-launch` 与系统 D-Bus 通信。Ubuntu 22.04 桌面版可能遗漏此包。

**关键日志信号：**
```
dconf failed to commit changes to dconf: 执行子进程"dbus-launch"失败（No such file or directory）
```

**修复：**
```bash
sudo apt install dbus-x11 -y
pkill -f snap-store  # 自动重启后生效
```

## 根因二：apt 源无法访问（GFW）

PackageKit 刷新时卡在无法访问的源上，导致 snap-store 阻塞。

**关键日志信号：**
```
E: 无法下载 http://security.ubuntu.com/ubuntu/dists/jammy-security/InRelease
E: 无法下载 https://pkgs.tailscale.com/stable/ubuntu/dists/jammy/InRelease
E: 无法下载 https://deb.nodesource.com/node_18.x/dists/nodistro/InRelease
```

**修复：**

```bash
# 1. security.ubuntu.com → 清华镜像
sudo sed -i 's|http://security.ubuntu.com/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ubuntu|g' /etc/apt/sources.list

# 2. 禁用无法访问的第三方源
sudo mv /etc/apt/sources.list.d/nodesource.list /etc/apt/sources.list.d/nodesource.list.disabled
sudo mv /etc/apt/sources.list.d/tailscale.list /etc/apt/sources.list.d/tailscale.list.disabled

# 3. 刷新
sudo apt update
```

## 验证

关掉 Ubuntu Software 重新打开，分类内容应正常加载。
