# NVIDIA Embedding API: Error Reference

This file documents every error encountered when configuring GBrain with
NVIDIA's embedding API, so future sessions don't rediscover them.

## Dimension Errors

### "expected 1536 dimensions, not 4096"

**Context:** `gbrain embed --stale`
**Cause:** `nv-embed-v1` outputs 4096 dimensions. The database `chunks.embedding`
column was created as `vector(1536)` by the original schema (OpenAI
text-embedding-3-large default). NVIDIA's API does NOT support the `dimensions`
parameter (returns `extra_forbidden`).
**Fix:** Use `nv-embedqa-e5-v5` (1024 dims) and rebuild DB with `vector(1024)`.

### "column cannot have more than 2000 dimensions for hnsw index"

**Context:** `gbrain init` after changing schema to `vector(4096)`
**Cause:** PGLite's HNSW vector index implementation hard-caps dimension at 2000.
This is a PGLite limitation, not Postgres itself.
**Fix:** Use a model with ≤2000 dims. Only `nv-embedqa-e5-v5` (1024) qualifies.

### "expected 1536 dimensions, not 1024"

**Context:** `gbrain embed` after switching to e5-v5 but NOT rebuilding DB
**Cause:** Schema still has `vector(1536)` but e5-v5 outputs 1024.
**Fix:** Change `pglite-schema.ts` to `vector(1024)` + `embedding_dimensions 1024`,
then delete and recreate DB.

## Token Limit Errors

### "Input length NNN exceeds maximum allowed token size 512"

**Context:** `gbrain embed --stale` with `nv-embedqa-e5-v5`
**Cause:** e5-v5 has a 512-token context limit. GBrain's default `MAX_CHARS=3000`
produces chunks far exceeding this. Each Chinese character ≈1 token.
**Fix:** Set `MAX_CHARS = 480` in `embedding.ts` (480 chars + ~32 system tokens).
Verified clean: no more 400 errors.

## PGLite Concurrency Errors

### "Timed out waiting for PGLite lock"

**Context:** `gbrain embed --stale` (second invocation while first is still running)
**Cause:** PGLite is single-connection. A second `gbrain embed` process cannot
acquire the database lock and times out (default wait: ~60s).
**Fix:** Kill existing embed processes before starting a new one:
```bash
pkill -9 -f "gbrain embed"
pkill -9 -f "bun"        # bun child process may survive parent kill
```

Also clean up stale pid files if the process was killed ungracefully:
```bash
rm -f ~/.gbrain/brain.pglite/postmaster.pid
```

## Content Errors

### "infinite value not allowed in vector"

**Context:** `gbrain embed --stale` on specific documents
**Cause:** Corrupted or malformed source content after pandoc/xlsx conversion
produced text that the embedding API interprets as containing infinity/NaN.
**Fix:** Skip the offending files. Re-extracting text with different tools
may help.

### "400 'input_type parameter is required' for asymmetric models"

**Context:** Direct curl test of models like `llama-3.2-nemoretriever-*`
**Cause:** NVIDIA requires `input_type: "passage"` for asymmetric embedding models.
GBrain's `embedding.ts` already includes this, but direct API calls must add it.
**Fix:** Include `"input_type": "passage"` in the request body.

## API Quirks

- **`dimensions` parameter**: NVIDIA's embedding API rejects this with
  `extra_forbidden`. Only OpenAI's native API supports dimension truncation.
- **`input_type`**: Required for asymmetric models, ignored for symmetric ones.
  GBrain always sends it, which is correct for all models tested.
- **Rate limits**: Maximum retry backoff is 120s (configurable in `embedding.ts`).
