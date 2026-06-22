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
