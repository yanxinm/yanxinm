# API Relay Provider (中转站) Setup

How to configure a New API-style relay service (e.g. apikey.fun) as a Hermes custom_provider.

## Quick Reference

Relay services provide OpenAI-compatible endpoints through a single API key, routing to multiple upstream models (text, vision, image gen, audio).

## Step 1: Discover Available Models

```bash
curl -s "https://<relay-base>/v1/models" \
  -H "Authorization: Bearer <your-api-key>" \
  | python3 -c "import json,sys; [print(m['id']) for m in json.load(sys.stdin).get('data',[])]"
```

Models may include:
| Type | Example IDs |
|------|------------|
| Text chat | `gpt-5.5`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.2` |
| Codex (coding) | `gpt-5-codex`, `gpt-5.3-codex`, `apikeyfun-codex/gpt-5.5` |
| Vision | `gpt-4o`, `gpt-4o-mini` |
| Image generation | `gpt-image-1`, `gpt-image-1.5`, `gpt-image-2` |
| Audio | `gpt-4o-audio-preview`, `gpt-4o-realtime-preview` |

## Step 2: Test Each Capability

### Text chat
```bash
curl -s -X POST "https://<relay-base>/v1/chat/completions" \
  -H "Authorization: Bearer <key>" -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'
```

### Vision (image recognition)
Write payload to a temp file (base64 can be very large):
```python
import base64, json
with open('photo.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
payload = {
    'model': 'gpt-4o',
    'messages': [{'role': 'user', 'content': [
        {'type': 'text', 'text': 'Describe this image'},
        {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{b64}'}}
    ]}],
    'max_tokens': 100
}
with open('/tmp/vision_test.json', 'w') as f:
    json.dump(payload, f)
```

Then:
```bash
curl -s -X POST "https://<relay-base>/v1/chat/completions" \
  -H "Authorization: Bearer <key>" -H "Content-Type: application/json" \
  -d @/tmp/vision_test.json
```

### Image generation
```bash
curl -s -X POST "https://<relay-base>/v1/images/generations" \
  -H "Authorization: Bearer <key>" -H "Content-Type: application/json" \
  -d '{"model":"gpt-image-2","prompt":"a cat","size":"1024x1024","n":1,"response_format":"b64_json"}' \
  | python3 -c "
import json,sys,base64
d=json.load(sys.stdin)
b64=d['data'][0]['b64_json']
with open('/tmp/result.png','wb') as f: f.write(base64.b64decode(b64))
print(f'Saved {len(base64.b64decode(b64))//1024}KB')
"
```

## Step 3: Configure in Hermes

### As custom_provider (for text)
```yaml
custom_providers:
  - name: my-relay
    base_url: https://<relay-base>/v1
    api_key: <your-key>
    model: gpt-5.5   # default model
```

### As auxiliary vision provider
```yaml
auxiliary:
  vision:
    provider: custom:my-relay
    model: gpt-4o
    base_url: https://<relay-base>/v1
    api_key: <your-key>
```

## Step 4: Client-Side API Key Protection

The relay API key will be visible in `config.yaml`. For security:
1. Use `hermes config set` rather than direct file edits when possible
2. Restrict config file permissions: `chmod 600 ~/.hermes/config.yaml`

## Step 5: Routing Rules (per-user convention)

When a user explicitly defines model routing rules, save them to memory:
- Primary model for text work (conversation, writing, coding)
- Backup relay for fallback
- Image tasks route to specialized providers (Seedream for generation, doubao/relay-gpt-4o for vision)
- Some relay keys also support image generation via gpt-image-2 — available but used only when the user requests it

## Known Providers

| Provider | Base URL | Notes |
|----------|----------|-------|
| apikey.fun | `https://api.apikey.fun/v1` | Supports text, vision, image gen, audio. Has dedicated SLB endpoint: `https://slb.apikey.fun` |
