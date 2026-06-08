# Provider Connectivity Testing

Systematic debugging approach when a custom provider or new model endpoint doesn't respond.

## The 5-Step Diagnosis

### Step 1: Verify config.yaml entry

Every `custom_providers` entry needs all 4 fields:

```yaml
custom_providers:
  - name: MyProvider          # Unique name used in `hermes config set model.provider custom:MyProvider`
    base_url: https://api.example.com/v1
    api_key: sk-abc123...
    model: some-org/some-model
```

Missing `api_key` or wrong `base_url` is the most common mistake. **Pitfall**: the `model` field is the model identifier sent in the API request body, not a display name. Some providers require the full org-prefixed name (e.g. `minimaxai/minimax-m2.7`).

### Step 2: Test model list endpoint (GET)

This confirms the API key is valid and the endpoint is reachable:

```bash
curl -s "$BASE_URL/models" -H "Authorization: Bearer $API_KEY" | head -40
```

Expected: HTTP 200 + JSON with `data` array containing model IDs.
Known-issue code: 000 (curl timed out) = network unreachable. 401/403 = bad key. 404 = wrong base URL path.

**China network note**: GET requests often work even when POST doesn't. A successful `curl -s` here does NOT guarantee chat works.

### Step 3: Test chat completion (POST) — minimal payload

Use the absolute minimum request to rule out parameter issues:

```bash
curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "$BASE_URL/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"MODEL_NAME","messages":[{"role":"user","content":"hi"}]}'
```

Expected: HTTP 200 + JSON with `choices[0].message.content`.

**Pitfall**: Some providers require `"max_tokens"` or `"stream": false` in the request body, or they silently hang.

### Step 4: Distinguish root cause

| Symptom | Root cause |
|---------|------------|
| GET works (200), POST times out (code 000 or >60s) | **Network/firewall** — GFW blocks POST to overseas endpoints (NVIDIA, some Hugging Face, etc.) |
| GET works, POST returns 400 | **Wrong model name** or missing required request fields |
| GET returns 401/403 | **Invalid API key** or key lacks permission for this model |
| GET returns 404 | **Wrong base URL** — check trailing `/v1` or `/api` path |
| Everything returns 000 | **No internet** or DNS failure — check with `curl -s https://httpbin.org/get` |
| POST returns JSON but Hermes still fails | **Deploy-time catalog mismatch** — the provider may serve the model only at certain endpoints/regions, not globally |

### Step 5: Check Hermes deploy-time model catalog

After confirming curl works, verify Hermes picks it up:

```bash
hermes models list 2>&1 | grep -i "MODEL_NAME"
```

If the model isn't listed, run `hermes config edit` and check `model_catalog.*` — the provider may only accept the model on specific endpoint URLs.

## Specific Case: Model In Catalog But Returns 404 ("Not Found For Account")

Some providers (notably NVIDIA NIM) list models in their `/v1/models` endpoint that your specific API key/account *cannot actually use*. The symptom is:

```text
HTTP 404
{"status":404,"title":"Not Found","detail":"Function '...': Not found for account '...'"}
```

This is different from:
- **400** (bad request — wrong model name or missing params)
- **404 on base URL** (wrong endpoint path entirely)
- **401/403** (invalid key)

It means: the model exists on the provider's platform, but your account tier/API key doesn't have access to it. The model appears in the listing because the listing is global, not per-account.

### How to find working models on a restricted NVIDIA NIM account

1. Get the model list:
   ```bash
   curl -s "$BASE_URL/models" -H "Authorization: Bearer $API_KEY" | python3 -c "import json,sys; [print(m['id']) for m in json.load(sys.stdin).get('data',[])]"
   ```

2. Iterate through models with a minimal test:
   ```bash
   for model in $(curl -s "$BASE_URL/models" -H "Authorization: Bearer $API_KEY" | python3 -c "import json,sys; [print(m['id']) for m in json.load(sys.stdin).get('data',[])]"); do
     result=$(curl -s -w "\nHTTP:%{http_code}" "$BASE_URL/chat/completions" \
       -H "Authorization: Bearer $API_KEY" \
       -H "Content-Type: application/json" \
       -d "{\"model\": \"$model\", \"messages\": [{\"role\": \"user\", \"content\": \"Say: ok\"}], \"max_tokens\": 10}")
     http_code=$(echo "$result" | tail -1)
     if echo "$http_code" | grep -q "200"; then
       echo "✅ WORKING: $model"
     else
       echo "❌ BLOCKED: $model ($http_code)"
     fi
   done
   ```

3. Update config.yaml with a working model from the ✅ list.

### Real-World Case: This NVIDIA Account

The API key `nvapi-...R6Vx` on `integrate.api.nvidia.com` has access to:
- `google/gemma-2-2b-it` ✅
- `meta/llama-3.1-8b-instruct` ✅

Many other listed models (including `01-ai/yi-large`, `google/gemma-3-12b-it`, `mistralai/mistral-7b-instruct-v0.3`) return 404. The **working** model that's a good compromise between capability and availability is `meta/llama-3.1-8b-instruct`.

## Real-World Example: Minimax via NVIDIA NIM

```bash
# Step 2: GET works — models listed successfully
curl -s https://integrate.api.nvidia.com/v1/models -H "Authorization: Bearer nvapi-..." | grep minimax
# → "minimaxai/minimax-m2.7" (found! Key is valid)

# Step 3: POST times out after 120s
curl -s -w "\nHTTP_CODE:%{http_code}" -X POST https://integrate.api.nvidia.com/v1/chat/completions \
  -H "Authorization: Bearer nvapi-..." \
  -H "Content-Type: application/json" \
  -d '{"model":"minimaxai/minimax-m2.7","messages":[{"role":"user","content":"hi"}]}'
# → HTTP_CODE:000 (timed out, not a config error)

# Conclusion: China → NVIDIA network issue. GET can pass but POST cannot.
# Workaround: Use a proxy, or use a different provider with better China connectivity.
```

## One-Line Sanity Check (All-in-One)

```bash
curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "$BASE_URL/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"'"$MODEL"'","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'
```

## Pitfalls

- **Trailing slash**: Some providers require it (`/v1/`), others reject it (`/v1`). Try both.
- **API key header format**: Most use `Bearer TOKEN`, but some use `Token TOKEN`, `key=TOKEN`, or query params like `?api_key=TOKEN`.
- **Model name prefix**: Some providers strip org prefixes (NVIDIA accepts both `minimaxai/minimax-m2.7` and just `minimax-m2.7`). Others require the prefix.
- **stream parameter**: Some providers default to `stream: true`. Add `"stream": false` explicitly for curl testing.
- **Rate limiting**: If you get 429, the provider is working — you just hit a rate limit. Wait and retry.
