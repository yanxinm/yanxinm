# Batch Profile Model Switch — Pitfalls & Recovery

## Problem
When using `hermes config set model.default MODEL --profile NAME` in a loop to switch all profiles, the main `~/.hermes/config.yaml` can get truncated to just 3 lines, losing all provider definitions, toolsets, gateway settings, etc.

## Symptoms
- `wc -l ~/.hermes/config.yaml` returns 3
- `hermes profile list` shows new model but gateway fails to start
- Missing providers, custom_providers, toolsets sections

## Recovery Steps
1. **Backup:** `cp ~/.hermes/config.yaml ~/.hermes/config.yaml.bak`
2. **Rebuild config:** Recreate the full config.yaml with all sections:
   - `model:` section with default provider and model
   - `providers:` section with all provider definitions
   - `custom_providers:` section with all custom endpoints
   - `toolsets:` section
   - `gateway:` section
   - `agent:` section
3. **Verify:** `cat ~/.hermes/config.yaml | wc -l` should return 100+ lines
4. **Restart gateway:** `terminal(command='hermes gateway restart', background=true)`

## Prevention
- Always check `wc -l ~/.hermes/config.yaml` before AND after batch updates
- Use `hermes config set` one profile at a time, verify between each
- Consider using `patch` for targeted edits instead of `config set` for bulk ops