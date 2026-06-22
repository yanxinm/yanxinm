# Chinese LLM Provider Setup for Hermes Profiles

## Quick Reference

| Provider | Model | API Key Env Var | Endpoint |
|----------|-------|-----------------|----------|
| 智谱 GLM | glm-5 / glm-5-flash | GLM_API_KEY | https://open.bigmodel.cn/api/paas/v4 |
| 豆包 Doubao | doubao-seed-2-0-pro | ARK_API_KEY | https://ark.cn-beijing.volces.com/api/v3 |
| DeepSeek | deepseek-v4-flash | DEEPSEEK_API_KEY | https://api.deepseek.com |

## Zhipu GLM Configuration

**TL;DR: Use built-in `zai` provider.** It handles model discovery, auth, and Web UI integration correctly. The `custom:zhipu` route is fragile — model dropdown stays empty and "新建对话" button greys out in Web UI.

### ✅ 方法一：内置 `zai` provider（推荐）

```bash
hermes config set model.provider zai
hermes config set model.default glm-5
```

确保 `~/.hermes/.env` 中 `GLM_API_KEY` 已设置，并在 `config.yaml` 的 `providers.zhipu.api_key` 中硬编码实际 key（`${GLM_API_KEY}` 在此段不解析）：

```yaml
providers:
  zhipu:
    api: https://open.bigmodel.cn/api/paas/v4
    default_model: glm-5
    api_key: 25a3b50ea118454c99ab9ef585b53107.q5jzjt10XIgLw5T3  # 直接写 key
```

重启 Gateway 后 Web UI 模型下拉即显示 glm-5 系列。

### ⚠️ 方法二：custom_providers（备选，易出问题）

仅在 `zai` provider 不可用时使用。症状：Web UI 新建对话按钮灰色、模型列表为空。

**⚠️ CRITICAL: Do NOT use `${GLM_API_KEY}` syntax — it won't be resolved!**

```yaml
# ❌ WRONG
custom_providers:
  - name: zhipu
    api_key: ${GLM_API_KEY}  # 不解析 → 401

# ✅ CORRECT
custom_providers:
  - name: zhipu
    base_url: https://open.bigmodel.cn/api/paas/v4
    api_key: your_actual_key_here.xxxxx
    model: glm-5
```

同时删除 `model.base_url` 行（与 custom 冲突），并确保 `providers.zhipu` 段也有硬编码 key。

### 添加 Key + 测试

```bash
curl -s https://open.bigmodel.cn/api/paas/v4/chat/completions \
  -H "Authorization: Bearer your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"model":"glm-5","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'
```

## Batch Update All Profiles

```bash
# Add provider to default config first
# Then update all profiles
for p in default jike lvyou wenan zhidu sheji; do
  hermes config set model.default glm-5 --profile $p
  hermes config set model.provider zai --profile $p
done

# Verify
hermes profile list
```

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| HTTP 401: 令牌已过期或验证不正确 | `api_key: ${ENV_VAR}` not resolved | Write key directly in config.yaml |
| named custom provider 'zhipu' has no resolvable api_key | Same as above | Same as above |
| Web UI "新建对话"按钮灰色+模型下拉为空 | `custom:*` provider 无法发现模型 | 改用内置 `zai` provider |

## Model Selection

| Use Case | Recommended Model |
|----------|-------------------|
| 日常对话 | glm-5 / glm-5-flash |
| 代码生成 | glm-5 |
| 长文本处理 | glm-5-long (if available) |
| 出图 (sheji) | gpt-image-2 via fun-codex provider |

## sheji Profile Special Setup

sheji needs both the main model (for text) and fun-codex provider (for image generation):

```yaml
model:
  default: glm-5
  provider: zai

custom_providers:
  - name: zhipu
    base_url: https://open.bigmodel.cn/api/paas/v4
    api_key: your_glm_key_here
    model: glm-5
  - name: fun-codex
    base_url: https://slb.apikey.fun/v1
    api_key: your_apikey_fun_key
    model: gpt-5.5
    api_mode: codex_responses

toolsets:
  - hermes-cli
  - image_gen
```

## Pricing Reference

| Provider | Plan | Price | Notes |
|----------|------|-------|-------|
| 智谱 GLM | Free | ¥0 | 试用，有速率限制 |
| 智谱 GLM | Coding | ¥199/月 | 日常开发使用 |
| 智谱 GLM | Pro | ¥399/月 | 高频使用 |
