# 外部 npm 插件/扩展安全安装指南

## 问题背景

一些外部的 Hermes 插件（如 MemOS memos-local-plugin）通过 npm 分发安装脚本。这些脚本通常包含 `pkill -f "/bin/hermes"` 命令来重启网关——但这会**直接杀掉当前 Feishu/WeChat 等平台的会话连接**，导致 agent 掉线。

**永远不要直接运行包含 `pkill` / `kill` Hermes 进程的外部安装脚本。** 拆成手动步骤执行。

## 通用手动安装步骤

### 前提条件

- Node.js ≥ 20
- npm
- Python 3 (Hermes 运行环境)

### Step 1: 下载 npm 包

```bash
npm pack @scope/package-name
# => scope-package-version.tgz
```

⚠️ **中国网络**：npm 官方源可能超时，用国内镜像搜索：

```bash
# 包搜索: https://npmmirror.com/
npm pack @scope/package-name --registry=https://registry.npmmirror.com
```

### Step 2: 解压到目标目录

```bash
mkdir -p ~/.hermes/plugin-name
tar xzf scope-package-version.tgz -C ~/.hermes/plugin-name --strip-components=1
```

### Step 3: 安装 npm 依赖

```bash
cd ~/.hermes/plugin-name
npm install --omit=dev --no-fund --no-audit --registry=https://registry.npmmirror.com
```

### Step 4: 编译原生模块

如果包依赖 `better-sqlite3` 等 C++ 原生模块：

```bash
cd ~/.hermes/plugin-name
npm rebuild better-sqlite3
```

**Node v25+ 注意**：没有预编译二进制，会从源码编译，耗时较长。

验证：
```bash
node -e "require('better-sqlite3'); console.log('OK')"
```

### Step 5: 创建 Hermes 提供器链接

找到 Hermes 插件目录并创建符号链接：

```bash
# 通常位置
ls ~/Hermes-Agent/plugins/memory/
# 或
ls ~/.hermes/hermes-agent/plugins/memory/

# 创建链接
ln -s ~/.hermes/plugin-name/adapters/hermes/memos_provider \
  ~/Hermes-Agent/plugins/memory/provider-name
```

### Step 6: 验证提供器可用

```bash
python3 -c "
from plugins.memory import load_memory_provider
p = load_memory_provider('provider-name')
print('OK' if p and p.name == 'provider-name' else 'FAIL')
"
```

### Step 7: 打补丁 config.yaml

编辑 `~/.hermes/config.yaml`：

```yaml
memory:
  provider: provider-name
  memory_enabled: true
  user_profile_enabled: true
plugins:
  enabled:
    - provider-name
```

### Step 8: 启动后台服务（如有）

如果插件包含一个 HTTP 服务/守护进程（如 Memory Viewer），在后台启动：

```bash
cd ~/.hermes/plugin-name
nohup node node_modules/.bin/tsx path/to/entry.cts --agent=hermes --daemon \
  > logs/daemon.log 2>&1 &
```

验证服务响应：
```bash
curl http://127.0.0.1:<PORT>/
```

## 如何判断安装脚本是否危险

安装前先阅读 `install.sh` / `install.ps1`，搜索以下关键词：

| 关键词 | 风险 | 应对 |
|--------|------|------|
| `pkill -f "/bin/hermes"` | 🔴 会杀掉当前会话 | 手动安装 |
| `pkill -f "hermes"` | 🔴 同上 | 手动安装 |
| `kill \`pgrep -f "hermes"\`` | 🔴 同上 | 手动安装 |
| `systemctl --user restart hermes-gateway` | 🟡 掉线但会自动重连 | 提前告知用户 |
| `hermes gateway restart` | 🟡 同上 | 提前告知用户 |
| `npm rebuild` / `node-gyp rebuild` | 🟡 可能超时 | 加长 timeout |
| `playwright install` / `scrapling install` | 🟡 下载大文件 | 单独执行 |

## 回退方法

```bash
# 恢复 config.yaml（改回原 memory provider）
# 删除插件目录
rm -rf ~/.hermes/plugin-name
# 删除符号链接
rm ~/Hermes-Agent/plugins/memory/provider-name
# 杀掉后台进程
pkill -f "plugin-entry-point"
```
