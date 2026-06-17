# Chrome 免 sudo 用户空间安装

## 下载解压

```bash
# 下载 .deb
curl -L -o /tmp/google-chrome.deb \
  "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

# 解压到用户目录（免 sudo）
mkdir -p ~/apps/chrome
dpkg -x /tmp/google-chrome.deb ~/apps/chrome

# 创建 symlink
ln -sf ~/apps/chrome/opt/google/chrome/google-chrome ~/.local/bin/google-chrome
```

## 验证

```bash
google-chrome --version
# Google Chrome 149.0.7827.53
```

## 无头模式测试

```bash
google-chrome --headless --disable-gpu --dump-dom https://example.com | head -5
# 输出 HTML → 正常
```

## Hermes 集成

Chrome 在 PATH 中后，Hermes browser 工具 (`engine: auto`) 自动发现并使用。无需额外配置。
