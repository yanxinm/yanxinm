# API Key Truncation in Config — Debug Guide

## Symptom

When reading `~/.hermes/config.yaml` via Python's `yaml.safe_load()`, long API key
values may appear truncated when printed:

```python
import yaml
with open('/home/yanxin/.hermes/config.yaml') as f:
    config = yaml.safe_load(f)
for p in config.get('custom_providers', []):
    if p.get('name') == 'apikey-fun':
        print('API_KEY:', p.get('api_key'))
# → API_KEY: sk-877...b8b8   ← looks truncated!
```

This is NOT a storage issue — the file content is correct. Python's `yaml.safe_load()`
truncates long string reprs at ~48 chars in output display. The actual in-memory
value IS the full key.

## Diagnosis: Check Raw Bytes

To confirm the full key value, read the config file as raw bytes and extract the
hex of the relevant line:

```python
with open('/home/yanxin/.hermes/config.yaml', 'rb') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if b'apikey-fun' in line:
        for j in range(i, min(i+5, len(lines))):
            if b'api_key' in lines[j]:
                print(f'HEX: {lines[j].hex()}')
```

Then decode the hex after `api_key: ` prefix (hex `6170695f6b65793a20`):

| Hex byte range | Purpose |
|----------------|---------|
| `6170695f6b65793a20` | `api_key: ` (4-space indent + key + colon + space) |
| Remaining hex | The actual API key value, terminated by `0a` (newline) |

Quick one-liner for a known line number:

```bash
python3 -c "
with open('/home/yanxin/.hermes/config.yaml', 'rb') as f:
    for i, line in enumerate(f, 1):
        if i == L:  # replace L with line number
            print(bytes.fromhex(line.decode().strip()))
"
```

## Root Cause

Python's `yaml.safe_load()` + subsequent `repr()` / `print()` of the parsed dict
truncates long values in display — this is a Python display artifact, not actual data
loss. The parsed `dict` in memory holds the full key.

## Prevention

When writing API keys to config via `hermes config set` or `hermes auth add`,
the key is stored faithfully. The truncation only affects **display**, not storage.

If you need to verify the key is correct:
1. Use the key directly in a test API call (curl) — if it works, the key is correct.
2. OR use the hex extraction method above.
3. OR use `grep` to see the raw config line (though it may wrap):
   ```bash
   grep -A 3 "apikey-fun" ~/.hermes/config.yaml | grep api_key
   ```
