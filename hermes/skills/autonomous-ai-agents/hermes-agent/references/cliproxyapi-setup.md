# CLIProxyAPI Setup (WSL / China Network)

CLIProxyAPI (router-for-me/CLIProxyAPI) wraps Gemini CLI, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service. This lets you use your CLI subscriptions (Gemini 3.1 Pro, GPT 5.5, etc.) via standard API calls.

## Overview

| Item | Value |
|------|-------|
| GitHub | https://github.com/router-for-me/CLIProxyAPI |
| Stars | ~33k+ (2026-05) |
| Language | Go |
| License | MIT |
| Latest | v7.1.17 (2026-05-19) |
| Default port | 8317 |

## Install on WSL (China network)

GitHub release downloads timeout from WSL in China. Use a mirror:

```bash
# Download via ghproxy mirror
cd /tmp
curl -sL "https://ghproxy.net/https://github.com/router-for-me/CLIProxyAPI/releases/download/v7.1.17/CLIProxyAPI_7.1.17_linux_amd64.tar.gz" -o cliproxyapi.tar.gz
tar xzf cliproxyapi.tar.gz

# Install to ~/.local/bin/
mkdir -p ~/.local/bin
cp cli-proxy-api ~/.local/bin/
chmod +x ~/.local/bin/cli-proxy-api

# Verify
~/.local/bin/cli-proxy-api --version
# Expected: CLIProxyAPI Version: 7.1.17, Commit: ...
```

**Note:** `sudo` is not available in WSL without password interop. Install to user-local bin instead.

## Minimal config

```yaml
# ~/.cli-proxy-api/config.yaml
host: "127.0.0.1"
port: 8317
auth-dir: "~/.cli-proxy-api"

remote-management:
  allow-remote: false
  secret-key: ""

api-keys:
  - "sk-test-key"    # change this

debug: true
usage-statistics-enabled: false
```

## Start the server

```bash
mkdir -p ~/.cli-proxy-api

# Foreground (for testing):
~/.local/bin/cli-proxy-api -config ~/.cli-proxy-api/config.yaml

# Background (for use in Hermes):
# Run via terminal tool with background=true, or use nohup
```

## Verify

```bash
curl -s http://127.0.0.1:8317/v1/models -H "Authorization: Bearer sk-test-key"
# Returns {"data":[],"object":"list"} if no providers configured
# Returns list of models once providers are added
```

## Adding a provider (e.g. Gemini CLI)

```bash
# OAuth login to Google account
~/.local/bin/cli-proxy-api -login

# Or configure OpenAI-compatible upstream:
# Add to config.yaml:
# openai-compatibility:
#   - name: "deepseek"
#     base-url: "https://api.deepseek.com/v1"
#     api-key-entries:
#       - api-key: "sk-..."
#     models:
#       - name: "deepseek-chat"
#         alias: "deepseek-chat"
```

Providers: Gemini CLI (OAuth), OpenAI Codex (OAuth), Claude Code (OAuth), Grok Build (OAuth), AI Studio, API keys, or OpenAI-compatible upstreams.

## Using with Hermes Agent

Add as a custom_provider in `~/.hermes/config.yaml`:

```yaml
custom_providers:
  - name: cliproxy
    base_url: http://127.0.0.1:8317/v1
    api_key: sk-test-key
    model: gemini-2.5-flash     # or whatever model CLIProxyAPI proxies
```

Then set model to use: `hermes config set model.default cliproxy/gemini-2.5-flash`

## Provider Connectivity Testing (通用方法)

当自定义 provider 或新模型端点不响应时，系统诊断步骤：

### Step 1: 验证 config.yaml 的 custom_providers 条目

确保 4 个字段完整：`name`, `base_url`, `api_key`, `model`

### Step 2: 测试模型列表端点

```bash
curl -s "$BASE_URL/models" -H "Authorization: Bearer $API_KEY" | head -20
```

### Step 3: 逐层隔离

模型列表返回 200 但聊天请求超时/404 → 执行最小 curl 测试：

```bash
curl -s -w "\n%{http_code}" -X POST "$BASE_URL/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"MODEL_NAME","messages":[{"role":"user","content":"hi"}],"max_tokens":5}'
```

#### NVIDIA NIM 特殊问题

- 端点：`https://integrate.api.nvidia.com/v1`
- **并非所有模型对某个 API Key 都可用**。`01-ai/yi-large` 报了 404 "Function not found for account"
- 排查：先 `GET /v1/models` 列出该 Key 可用的模型，逐个发最小请求测试
- 可用模型快速扫描：
  ```bash
  for model in $(curl -s "$BASE_URL/models" -H "Authorization: Bearer $API_KEY" | python3 -c "import json,sys; [print(m['id']) for m in json.load(sys.stdin).get('data',[])]" 2>/dev/null); do
    http=$(curl -s -w "\n%{http_code}" -X POST "$BASE_URL/chat/completions" \
      -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json" \
      -d "{\"model\":\"$model\",\"messages\":[{\"role\":\"user\",\"content\":\"ok\"}],\"max_tokens\":5}" | tail -1)
    echo "$http $model"
  done
  ```
- 已知可用的模型：`meta/llama-3.1-8b-instruct`, `google/gemma-2-2b-it`
- 某些模型虽在列表里但请求可能超时（如 `deepseek-ai/deepseek-v4-flash`）

### Step 4: 区分根因

GET (模型列表) 通 + POST (聊天) 超时 = **网络可达性问题**（非配置错误）。中国大陆→海外 API 网关（NVIDIA NIM 等）的 POST 请求可能被防火墙阻断。

## 当前已配置的模型 Provider 速查

| 名称 | 模型 | API Key来源 | 用途 |
|------|------|------------|------|
| DeepSeek | deepseek-v4-flash | `DEEPSEEK_API_KEY` in `.env` | ✅ 主模型 |
| Ark 豆包文本 | doubao-seed-2-0-pro-260215 | 火山引擎 Key (config.yaml) | ✅ 备用 |
| Ark 豆包视觉 | doubao-seed-1-6-vision-250815 | 同上 | ✅ 图片识别 |
| NVIDIA NIM | meta/llama-3.1-8b-instruct | `NVIDIA_API_KEY` in `.env` | ✅ 额外通道 |
| Ark Seedream | doubao-seedream-4-5-251128 | `ARK_IMAGE_API_KEY` in `.env` | ✅ 文生图+图生图 |

## Pitfalls

- **GitHub download timeout**: WSL → GitHub release download fails in China. Always use `ghproxy.net` or another mirror prefix.
- **No sudo**: WSL without password interop can't use `sudo cp`. Use `~/.local/bin/`.
- **No models initially**: The server starts with zero providers. You must configure at least one provider (OAuth login or API key) before it returns any models.
- **OAuth login needs browser**: `-login` opens a browser for OAuth. In headless WSL, use `-no-browser` flag and copy the URL manually.
- **Docker not viable**: Docker daemon typically not running in WSL by default. Binary install is the reliable path.
