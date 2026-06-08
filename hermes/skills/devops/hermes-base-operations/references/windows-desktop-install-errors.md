# Hermes Desktop Windows 安装——国内环境踩坑实录

## 环境
- Windows 11 (yanxi)
- 安装路径：`C:\Users\yanxi\AppData\Local\hermes\`
- 日志：`C:\Users\yanxi\AppData\Local\hermes\logs\bootstrap-installer.log`

## 安装失败全记录

### 失败1：git fetch 被墙
```
INSTALL DIDN'T FINISH
git fetch failed (exit 128)
```
- 原因：GitHub 直连超时
- 修复：`git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`

### 失败2：npm 依赖安装卡死 30 分钟
步骤"Installing Node.js dependencies" 9/16 不动
- 原因：npm 从境外 registry 下载，防火墙限流
- 修复：`npm config set registry https://registry.npmmirror.com`
- 额外：`setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"`

### 失败3：Electron 编译卡 10 分钟
步骤"Building desktop app" 10/16 不动
- 原因：Electron 二进制从 GitHub Releases 下载被墙
- 修复：`setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"`

### 失败4：EBUSY -4082
```
npm error EBUSY: resource busy or locked
rename 'node_modules\electron' -> 'node_modules\.electron-xxx'
bootstrap FAILED stage=desktop error=desktop workspace npm install failed (exit -4082)
```
- 原因：Windows Defender 实时防护锁定了 node_modules\electron 目录
- 修复顺序：
  1. 任务管理器结束所有 node.exe 和 hermes 进程
  2. `rmdir /s /q node_modules`
  3. 如果 rmdir 也报锁 → 重启电脑
  4. 重启后先配镜像再装

### 失败5：build failed (exit 1)
```
bootstrap FAILED stage=desktop error=apps/desktop build failed (exit 1)
```
- 原因：通常是上面 3 或 4 的连锁反应
- 修复：清 node_modules → 配镜像 → 重装

## 最佳实践

1. **开装前一次性配好三个镜像**（见 SKILL.md 第三节）
2. **关掉 Windows Defender 实时防护**（装完再开）
3. **安装失败 → 直接重启电脑**（比手动清理进程/文件锁快得多）
4. **如果装了 3 次还失败**：放弃 Desktop，用浏览器打开 Web UI（Funnel URL）
