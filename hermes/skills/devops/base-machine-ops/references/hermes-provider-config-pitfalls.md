# Hermes Provider 配置避坑

## `${VAR}` 环境变量引用问题

在 `providers` 段使用 `${GLM_API_KEY}` 引用环境变量时，Hermes 可能不会正确展开（取决于版本和 provider 类型）。

### 症状
- Web UI 新建对话按钮灰色
- 模型下拉框为空
- Gateway `/v1/models` API 返回 `"Invalid API key"`
- 但直接用 curl 测试同一个 API key 可以正常工作

### 根因
`providers.<name>.api_key: ${ENV_VAR}` 中的环境变量引用未被 Hermes 运行时解析。`custom_providers` 段中的硬编码 key 是正常的，但 `providers` 段的 `${...}` 引用被当作字面字符串传给 API。

### 修复
直接用硬编码的 API key 值：

```bash
hermes config set providers.zhipu.api_key "实际key值"
```

不要用 `hermes config set providers.zhipu.api_key '${GLM_API_KEY}'`（单引号会写入字面量 `${GLM_API_KEY}` 而非展开后的值）。

### 验证
```bash
hermes config show | grep -A5 "providers:"
# 确认 api_key 是实际值，不是 ${...} 形式

curl http://localhost:8642/v1/models
# 应返回模型列表，而非 "Invalid API key"
```

### 相关
- 智谱 GLM / Z.AI provider 会自动查找 `GLM_API_KEY`、`ZAI_API_KEY`、`Z_AI_API_KEY` 环境变量
- 但 `custom:zhipu` provider 不走自动查找逻辑，必须显式配置 api_key
- `custom_providers` 段支持硬编码，不受此问题影响

## 跨 Profile 模型统一切换

### 场景

需要将所有 Profile（jike、lvyou、sheji、wenan、zhidu 及 default）的默认模型改为同一个 provider。例如：从 GLM 全部切到 DeepSeek，视觉模型统一用 Doubao。

### 操作步骤

**1. 主配置文件（default profile）**

用 `hermes config set` 修改 `~/.hermes/config.yaml`：

```bash
# 主模型
hermes config set model.default "deepseek-v4-flash"
hermes config set model.provider "deepseek"

# 添加新 provider（需要先定义）
hermes config set providers.ark-doubao.api "https://ark.cn-beijing.volces.com/api/v3"
hermes config set providers.ark-doubao.api_key "<key>"
hermes config set providers.ark-doubao.default_model "doubao-seed-1-6-vision-250815"

# 视觉模型（各 profile 无独立 auxiliary 时继承主配置）
hermes config set auxiliary.vision.provider "ark-doubao"
hermes config set auxiliary.vision.model "doubao-seed-1-6-vision-250815"
```

**2. 各 Profile 配置文件**

`hermes config set` 仅作用于 default profile。修改其他 profile 需直接编辑 `~/.hermes/profiles/<name>/config.yaml`：

```yaml
# 批量改模型
model:
  default: deepseek-v4-flash
  provider: deepseek
```

| 修改项 | 文件 | 方式 |
|--------|------|------|
| 主模型 default | `~/.hermes/config.yaml` | `hermes config set` |
| 主模型 vision | `~/.hermes/config.yaml` | `hermes config set` |
| Profile 模型 | `~/.hermes/profiles/<name>/config.yaml` | 直接 patch 文件（注意保留后续的 `mcp_servers:`、`toolsets:` 等键） |
| Profile vision | 无独立 auxiliary 时继承主配置 | 无需修改 |

**3. 特殊情况处理**

| Profile | 需要保留的配置 |
|---------|---------------|
| **sheji** | `custom_providers.fun-codex`（出图用 gpt-image-2）、`image_gen` toolset、`custom:fun-codex.stale_timeout_seconds: 300` |
| **jike** | 原有的 provider 定义（ark/volces、fun-codex、agnes-ai 等）仍保留供技能调用，只改 `model.default` |

**4. 验证**

```bash
for p in jike lvyou sheji wenan zhidu; do
  echo "$p: $(grep -A1 "default:" ~/.hermes/profiles/$p/config.yaml | head -2 | tr '\n' ' ')"
done
# 正确输出：每个 profile 都显示 deepseek-v4-flash + deepseek
```

### 视觉模型继承规则

- 如果 profile 的 `config.yaml` 中没有 `auxiliary.vision` 段，则继承主配置的 `auxiliary.vision` 设置
- 如果 profile 有独立的 `auxiliary.vision`（如 jike profile），则以 profile 自身配置为准
- 验证：`grep -A6 "auxiliary:" ~/.hermes/profiles/<name>/config.yaml`，无输出 = 继承主配置

### 常见错误

| 错误 | 原因 | 修复 |
|------|------|------|
| lvyou/wenan 等 profile 结构损坏 | 直接替换 `model:` 段时意外覆盖了后续的 `mcp_servers:` 键名 | patch 后检查结构：`grep -E '^(model|providers|mcp_servers|custom_providers):' config.yaml` |
| `hermes config set` 被拒 | Agent 不能直接修改主 config.yaml（安全限制） | 用 `hermes config set` CLI 命令，或告知用户手动编辑 |
| profile 视觉不生效 | profile 自己定义了空的 `auxiliary:` 段但无 `vision:` 子项 | 检查 `auxiliary:` 段是否存在，存在则需单独配置 |

## Gateway 重启阻塞

### 症状
`sudo hermes gateway restart` 超时或长时间不返回。

### 根因
Gateway 有 `drain_timeout`（默认 180s），重启时会等待所有活跃连接（包括当前对话的 WebSocket）优雅关闭。如果从 Gateway 管理的 session 内执行 restart，会形成死锁：restart 等待当前 session 结束，但 session 被 restart 命令阻塞。

### 修复
从**另一个终端窗口**直接用 systemctl 强制重启：

```bash
sudo systemctl restart hermes-gateway
```

systemctl 的 `SIGTERM → SIGKILL` 流程不等待 drain_timeout。
