# Hindsight Memory Provider Debugging

## Config Resolution Chain (v0.6.1+)

The Hindsight memory provider has **two independent config consumers** that are NOT the same:

| Consumer | Config Source | Reads config.json? | 
|----------|---------------|--------------------|
| **Hermes plugin** (`plugins/memory/hindsight/__init__.py`) | `~/.hermes/hindsight/config.json` | **YES** — this is its primary config |
| **Embedded daemon** (`hindsight-api` / `hindsight-embed`) | `~/.hindsight/profiles/<profile>.env` + `HINDSIGHT_API_LLM_*` env vars | **No** — uses env vars only |

### Hermes Plugin Config Resolution

The plugin's `_load_config()` reads in this order (first found wins):

1. `~/.hermes/hindsight/config.json` — profile-scoped (preferred)
2. `~/.hindsight/config.json` — legacy shared path
3. Environment variables (fallback, constructs a synthetic dict)

The plugin then generates a profile env file for the embedded daemon via `_materialize_embedded_profile_env()`, writing to `~/.hindsight/profiles/hermes.env` with key conversion (e.g. `openai_compatible` → `openai`).

### Full config.json Schema (Hermes Plugin)

```json
{
  "mode": "local_embedded",
  "llm_provider": "openai_compatible",
  "llm_model": "deepseek-v4-flash",
  "llm_base_url": "https://api.deepseek.com",
  "timeout": 120,
  "idle_timeout": 300,
  "api_url": "http://localhost:8888",
  "bank_id": "hermes",
  "recall_budget": "mid",
  "memory_mode": "hybrid",
  "recall_prefetch_method": "recall",
  "auto_recall": true,
  "auto_retain": true,
  "retain_every_n_turns": 1,
  "retain_async": true,
  "retain_context": "conversation between Hermes Agent and the User",
  "recall_max_tokens": 4096,
  "recall_max_input_chars": 800,
  "recall_tags_match": "any",
  "banks": {
    "hermes": {
      "bankId": "hermes",
      "budget": "mid",
      "enabled": true
    }
  }
}
```

Key fields:
- `mode` — `cloud`, `local_embedded`, or `local_external`
- `llm_provider` — accepts `openai_compatible` (plugin-internal value); daemon converts to `openai`
- `timeout` / `idle_timeout` — API request timeout and daemon idle timeout in seconds
- `api_url` — endpoint URL (auto-set for local mode)
- `banks` — structured bank configuration with bankId, budget, enabled

### Embedded Daemon Config (for `hindsight-api` CLI)

The daemon reads only from env vars:

```
HINDSIGHT_API_LLM_PROVIDER=openai       # NOT openai_compatible!
HINDSIGHT_API_LLM_API_KEY=<key>
HINDSIGHT_API_LLM_MODEL=deepseek-v4-flash
HINDSIGHT_API_LLM_BASE_URL=https://api.deepseek.com
HINDSIGHT_API_DATABASE_URL=pg0          # embedded PostgreSQL
```

### Valid Provider Values (v0.6.1 daemon)

`openai`, `groq`, `ollama`, `gemini`, `anthropic`, `lmstudio`, `llamacpp`, `vertexai`, `openai-codex`, `claude-code`, `mock`, `none`, `minimax`, `deepseek`, `litellm`, `litellmrouter`, `bedrock`, `volcano`, `openrouter`, `zai`

**`openai_compatible` is NOT a valid daemon value.** Use `openai` with a custom `base_url` instead. The Hermes plugin handles this conversion automatically.

### Key Env Vars

| Env Var | Purpose | Example |
|---------|---------|---------|
| `HINDSIGHT_API_LLM_PROVIDER` | LLM backend (daemon) | `openai` |
| `HINDSIGHT_API_LLM_API_KEY` | API key (daemon) | DeepSeek key |
| `HINDSIGHT_API_LLM_MODEL` | Model name (daemon) | `deepseek-v4-flash` |
| `HINDSIGHT_API_LLM_BASE_URL` | Custom endpoint (daemon) | `https://api.deepseek.com` |
| `HINDSIGHT_LLM_API_KEY` | API key (Hermes plugin fallback) | DeepSeek key |
| `HINDSIGHT_MODE` | Operation mode (plugin fallback) | `local_embedded` |
| `HINDSIGHT_API_DATABASE_URL` | Database URL (daemon) | `pg0` (embedded) |

## Daemon Troubleshooting

### Daemon fails to start

Full error log locations:
```
~/.hindsight/profiles/hermes.log          # daemon runtime log
~/.hermes/logs/hindsight-embed.log        # Hermes plugin daemon startup log
```

Common errors:

**"LLM API key is required"**
→ Missing HINDSIGHT_API_LLM_API_KEY env var. Note: old .env may have HINDSIGHT_LLM_API_KEY but the daemon looks for HINDSIGHT_API_LLM_API_KEY.

**"Invalid LLM provider: openai_compatible"**
→ Using a value not in the valid providers list. Change to openai with a custom base_url.

**"Cannot send a request, as the client has been closed"**
→ huggingface_hub/httpx client closed prematurely. This often happens when HF_HUB_OFFLINE=1 is set and huggingface_hub tries to validate cached model files against the hub while the network is unreachable. Fix:
  1. Set HF_ENDPOINT=https://hf-mirror.com and HF_HUB_OFFLINE=0 in the profile env
  2. pip install --force-reinstall --no-deps huggingface-hub httpx
  3. Kill the daemon and restart

**Authentication error (HTTP 401) on startup**
→ Old/stale API key in the generated profile env at ~/.hindsight/profiles/hermes.env. The profile env may have been generated with an old key. Fix: regenerate by restarting Hermes, or manually update HINDSIGHT_API_LLM_API_KEY in that file.

**Startup hangs after "Starting Hindsight API..."**
→ Daemon may be waiting on DeepSeek API response during initialization or running database migrations. Wait 60-120s before declaring failure.

### Domestic Network / HuggingFace Mirror

When running in a domestic network (China), the embedded daemon may fail to download embedding models from huggingface.co (Errno 101: Network is unreachable). The daemon needs two models:
- BAAI/bge-small-en-v1.5 (embedding, ~40MB)
- cross-encoder/ms-marco-MiniLM-L-6-v2 (reranker, ~80MB)

**Fix: override the plugin-generated profile env**  

The Hermes plugin sets HF_HUB_OFFLINE=1 by default in `_build_embedded_profile_env()`. In domestic networks, this prevents model loading even from cache. Edit `~/.hindsight/profiles/hermes.env`:

```ini
HF_ENDPOINT=https://hf-mirror.com
HF_HUB_OFFLINE=0
TRANSFORMERS_OFFLINE=0
```

⚠️ **Regeneration warning:** Every time Hermes starts a new session with `memory.provider: hindsight`, the plugin's `initialize()` method calls `_materialize_embedded_profile_env()`, which **overwrites** `~/.hindsight/profiles/hermes.env` with default HF settings. If you hand-edited HF vars, they will be lost on next session start.

**Permanent fix:** Set the HF vars in `~/.bashrc` or the system environment so they survive plugin regeneration:
```bash
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
echo 'export HF_HUB_OFFLINE=0' >> ~/.bashrc
echo 'export TRANSFORMERS_OFFLINE=0' >> ~/.bashrc
```

The plugin's `_build_embedded_profile_env()` checks `os.environ.get(key, default)` for HF vars, so shell-level exports take precedence over the hardcoded defaults.

**Verify model cache:**

Check ~/.cache/huggingface/hub/ for the two model directories with snapshot files. If missing, force-download:
```
HF_ENDPOINT=https://hf-mirror.com python3 -c "
from sentence_transformers import SentenceTransformer
SentenceTransformer(BAAI/bge-small-en-v1.5)
SentenceTransformer(cross-encoder/ms-marco-MiniLM-L-6-v2)
"
```

### Process management

```bash
# Check if running
ps aux | grep hindsight-api | grep -v grep

# List all PostgreSQL instances (multiple pg0 instances possible)
ps aux | grep postgres | grep -v grep | grep -E "(hindsight|pg0)"

# Kill all instances
pkill -f hindsight-api

# Start in foreground for debugging
source ~/.hermes/.env && hindsight-api --port 9178

# Start as daemon
hindsight-api --daemon --idle-timeout 300 --port 9177
```

### Switching providers

```bash
# From command line
hermes config set memory.provider hindsight   # enable Hindsight
hermes config set memory.provider memtensor   # enable MemOS
```

Changes require `/reset` or gateway restart to take effect.

### Multiple PostgreSQL instances

Hindsight and other tools may each start their own embedded PostgreSQL (pg0). Look for different ports:

```
5432  hindsight-embed-hermes (Hermes plugin)
5433  hindsight (standalone daemon)
```

Kill old/duplicate instances if they conflict.
