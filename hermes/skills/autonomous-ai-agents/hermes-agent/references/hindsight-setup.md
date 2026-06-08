# Hindsight Memory Provider Setup (Quick-Start)

> **This is the quick-start guide.** For the complete setup with full config.json schema, env vars, and provider options, see [hindsight-memory-setup.md](hindsight-memory-setup.md). For debugging and troubleshooting, see [hindsight-debugging.md](hindsight-debugging.md).

## Quick: Local Embedded + OpenAI-Compatible LLM (e.g. DeepSeek)

```bash
# 1. Set the memory provider
hermes config set memory.provider hindsight

# 2. Add environment variables
echo "HINDSIGHT_MODE=local_embedded" >> ~/.hermes/.env
echo "HINDSIGHT_LLM_API_KEY=sk-your-llm-key" >> ~/.hermes/.env
echo "HINDSIGHT_API_LLM_BASE_URL=https://api.deepseek.com" >> ~/.hermes/.env
echo "HINDSIGHT_API_LLM_PROVIDER=openai" >> ~/.hermes/.env
echo "HINDSIGHT_API_LLM_MODEL=deepseek-v4-flash" >> ~/.hermes/.env
echo "HINDSIGHT_API_LLM_API_KEY=sk-your-llm-key" >> ~/.hermes/.env

# 3. Create Hindsight config (v0.6.1 format)
mkdir -p ~/.hermes/hindsight
cat > ~/.hermes/hindsight/config.json << 'EOF'
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
EOF
```

## Domestic Network (China)

The plugin sets `HF_HUB_OFFLINE=1` by default. For domestic networks, override in the generated profile env at `~/.hindsight/profiles/hermes.env`:

```
HF_ENDPOINT=https://hf-mirror.com
HF_HUB_OFFLINE=0
TRANSFORMERS_OFFLINE=0
```

## Verify

```bash
hermes memory status
# Expected:
#   Provider: hindsight
#   Status: available ✓
```

## Logs

- Daemon startup: `~/.hermes/logs/hindsight-embed.log`
- Runtime: `~/.hindsight/profiles/hermes.log`

## Pitfalls

- `.env` is protected from `patch`/`write_file` — use `echo ... >> ~/.hermes/.env`
- Provider changes require `/reset` or gateway restart
- The daemon auto-assigns its port (not fixed at 8888)
- For full config reference, troubleshooting, and provider options, see [hindsight-memory-setup.md](hindsight-memory-setup.md)
