# Chrome 用户空间安装（免 sudo）

适用场景：headless Linux 主机（无显示器/无 sudo），需要给 Hermes browser 工具配置本地 Chrome。

## 安装步骤

```bash
# 1. 下载 Chrome .deb
curl -L -o /tmp/google-chrome.deb \
  "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

# 2. 解压到用户目录（免 sudo）
mkdir -p ~/apps/chrome
dpkg -x /tmp/google-chrome.deb ~/apps/chrome

# 3. 创建便捷链接
ln -sf ~/apps/chrome/opt/google/chrome/google-chrome ~/.local/bin/google-chrome

# 4. 验证版本
google-chrome --version
```

## 验证无头模式

```bash
# 无头渲染测试
google-chrome --headless --disable-gpu --dump-dom https://example.com | head -5
# 预期：返回 HTML DOM
```

## Hermes 集成

Chrome 加入 PATH 后，Hermes 的 `engine: auto` 会自动发现并使用它。确认 browser 工具启用：

```bash
hermes tools list | grep browser  # 应显示 ✓ enabled
```

Chrome 版本信息（2026-06-08 基地实测）：
- 版本：149.0.7827.53
- 安装路径：`~/apps/chrome/opt/google/chrome/google-chrome`
- 宿主机：M710q Ubuntu 22.04, 16GB RAM
