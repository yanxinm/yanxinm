---
name: gbrain
description: "GBrain knowledge base — install, configure with NVIDIA embedding, and import Windows Office documents on WSL"
version: 1.2.0
author: Hermes Agent
platforms: [linux, wsl]
metadata:
  related_skills: [obsidian, llama-cpp, ocr-and-documents]
---

# GBrain Knowledge Base

GBrain is a personal knowledge base / brain system (TypeScript/PGLite) by Garry Tan. It stores markdown notes as typed, linked pages with vector search via OpenAI-compatible embedding APIs.

## Installation on WSL

### 1. Install Bun

On WSL without sudo access, `curl -fsSL https://bun.sh/install | bash` may fail due to missing `unzip`. Use npm instead:

```bash
npm install -g bun
```

After install, add to PATH:

```bash
echo 'export PATH="$HOME/.bun/bin:$PATH"' >> ~/.bashrc
export PATH="$HOME/.bun/bin:$PATH"
```

### 2. Clone and Install GBrain

```bash
git clone https://github.com/garrytan/gbrain.git ~/gbrain
cd ~/gbrain
bun install
bun link
```

Verify: `gbrain --version`

> **Do NOT use `bun install -g github:garrytan/gbrain`** — Bun blocks the postinstall hook on global installs, so schema migrations never run and the CLI aborts with `Aborted()`. Always use `git clone + bun link`.

## Configuration: NVIDIA API as Embedding Backend

GBrain's embedding service uses an OpenAI-compatible embedding API. The SDK reads `OPENAI_API_KEY` and `OPENAI_BASE_URL` environment variables. Point them at your NVIDIA NIM endpoint to reuse an existing NVIDIA API key:

```bash
export OPENAI_API_KEY="nvapi-<your-key>"
export OPENAI_BASE_URL="https://integrate.api.nvidia.com/v1"
```

Persist in `~/.bashrc`:

```bash
# GBrain: NVIDIA embedding endpoint
export OPENAI_API_KEY="nvapi-<your-key>"
export OPENAI_BASE_URL="https://integrate.api.nvidia.com/v1"
```

### Model Selection (Critical)

GBrain uses `src/core/embedding.ts` for vector generation. The choice of embedding model is constrained by **two hard limits**:

1. **PGLite HNSW index**: max **2000 dimensions** (column `vector(n)` where n ≤ 2000)
2. **NVIDIA embedding API**: does NOT support the `dimensions` parameter to truncate output

| Model | Dims | Context | Compatible? |
|-------|------|---------|-------------|
| `nvidia/nv-embedqa-e5-v5` | **1024** ✅ | 512 tokens | ✅ Best choice |
| `nvidia/nv-embed-v1` | 4096 ❌ | 4096 tokens | ❌ Exceeds 2000-dim limit |
| `nvidia/llama-3.2-nemoretriever-300m-embed-v1` | 2048 ❌ | — | ❌ Exceeds 2000-dim limit |

**nv-embed-v1 can NEVER work with PGLite** — its 4096-dim output exceeds PGLite's 2000-dim HNSW index limit, and NVIDIA's API rejects `dimensions` as an unknown parameter.

**nv-embedqa-e5-v5 is the only viable option** but has a 512-token context limit. You MUST reduce `MAX_CHARS` in `embedding.ts` to prevent 400 errors.

#### Fix Steps

1. Edit `~/gbrain/src/core/embedding.ts`:
   ```diff
   - const MODEL = 'nvidia/nv-embed-v1';
   - const MAX_CHARS = 3000;
   + const MODEL = 'nvidia/nv-embedqa-e5-v5';
   + // 512 token limit for e5, ~1 char/token for Chinese, leave headroom
   + const MAX_CHARS = 480;
   ```

2. Edit `~/gbrain/src/core/pglite-schema.ts` to match database vector dimensions:
   ```diff
   - embedding     vector(1536),
   + embedding     vector(1024),
   ...
   - ('embedding_dimensions', '1536'),
   + ('embedding_dimensions', '1024'),
   ```

3. Rebuild the database (schema change requires fresh DB):
   ```bash
   # Backup first!
   cp -r ~/.gbrain ~/.gbrain.bak
   # Python shutil.rmtree is faster than rm -rf on PGLite directories
   python3 -c "import shutil, os; shutil.rmtree(os.path.expanduser('~/.gbrain/brain.pglite'), ignore_errors=True)"
   gbrain init
   ```

> If you skip step 2-3, `gbrain embed` will error: "expected NNN dimensions, not XXX" or "column cannot have more than 2000 dimensions for hnsw index".

## Importing Windows Office Documents

GBrain's `gbrain import <dir>` only processes `.md` and `.mdx` files. Convert `.docx`, `.xlsx`, and `.pdf` files to `.md` first.

### Prerequisites

```bash
which pandoc                           # for .docx → .md
python3 -c "import openpyxl" 2>&1      # for .xlsx → .md
python3 -c "import pymupdf" 2>&1       # for .pdf → .md
```

### Quick One-Off: Simple docx → md with pandoc

```bash
mkdir -p ~/brain_src
cp -r "/mnt/e/你的目录" ~/brain_src/
find ~/brain_src -name "*.docx" | while read f; do
  out="${f%.docx}.md"
  pandoc "$f" -t markdown --wrap=none -o "$out" 2>/dev/null
done
```

### Bulk Conversion with Python Script (recommended)

For directories with thousands of mixed-format files, use the companion conversion script:

```bash
# Locate the script (installed with the skill):
SCRIPT=~/.hermes/skills/note-taking/gbrain/scripts/convert_docs.py
# Or copy it anywhere convenient: cp "$SCRIPT" ~/brain_src/convert_docs.py

# Creates mirror directory structure in ~/brain_src/ with .md files only
python3 "$SCRIPT" \
  --src "/mnt/e/百度云同步盘/工作台账" \
  --dst ~/brain_src/工作台账 \
  --years "2021-2026"
```

The script handles:
- `.docx` → pandoc conversion
- `.xlsx` → markdown tables via openpyxl (skips old `.xls` format — use `xlrd` if those are critical)
- `.pdf` → text extraction via pymupdf
- Skips images, videos, archives, hidden/temp files
- Resume-safe: skips files where `.md` is newer than the source
- Progress reporting every 20 files

**Note on skip rates**: In a typical work-accounting directory (2021-2026), expect roughly:
- ~40% of source files convert (docx/pdf/xlsx)
- ~25% skip (images, archives, temp files)
- ~2% error (corrupted files, old `.xls` format, empty containers)
- The rest is non-document files

### Import to GBrain

```bash
export OPENAI_API_KEY="nvapi-<your-key>"
export OPENAI_BASE_URL="https://integrate.api.nvidia.com/v1"

# Step 1: Import without embedding (fast)
gbrain import ~/brain_src/ --no-embed

# Step 2: Generate vector embeddings (background recommended for large imports)
gbrain embed --stale
```

For large imports (2000+ pages), run embed as a background task so it doesn't block the conversation:

```bash
# Via terminal tool with background=true, notify_on_complete=true
terminal(command="...gbrain embed --stale", background=true, notify_on_complete=true, timeout=7200)

# Check progress mid-run — note: stdout is buffered in background mode,
# so poll/log may show empty output even when the process is running.
# Use gbrain doctor instead to see real progress:
terminal(command="gbrain doctor | grep -i embed", timeout=15)
# Or check brain score progression:
#   No embed → 10/100
#   24% done → 19/100
#   48% done → 27/100
#   71% done → 35/100
#   95% done → 43/100 (embed subscore 33/35)
#   100% + KG → 70+/100

# Kill and restart if needed (e.g. wrong model):
process(action="kill", session_id="proc_<id>")
```

**Performance expectations (NVIDIA API rate limit)**:
- ~207K chunks from 2405 pages (avg ~86 chunks/page)
- Throughput: ~500-600 chunks/minute (NVIDIA API rate-limited; a chunk is a page fragment ≤480 chars)
- Completion time: ~5-6 hours for a full 2400-page import, spread over multiple 2-hour background sessions
- If interrupted, `gbrain embed --stale` resumes from checkpoint automatically
- Running `embed` multiple times is expected for large imports; each segment restarts from where it left off

**Pitfall: stdout buffering in background processes** — When `gbrain embed --stale` runs as a background terminal task, its stdout is fully buffered and `process(action="poll")` shows an empty output. The process IS making progress, but buffered output never reaches the capture pipe. Use `gbrain doctor | grep -i embed` or `gbrain doctor --json` to see real embedding coverage from the database directly.

**Pitfall: duplicate embed processes competing for PGLite lock** — If you spawn multiple `gbrain embed --stale` processes (e.g. via background terminal in consecutive turns), they compete for the single PGLite connection. One process holds the lock; others print "Timed out waiting for PGLite lock" and exit with code 1. **Always kill existing embed processes before starting a new one:**

```bash
pkill -9 -f "gbrain embed"      # kill bash wrapper
pkill -9 -f "bun"               # kill bun child (may be needed if wrapper survives)
# Verify:
ps aux | grep gbrain | grep -v grep
```

**Pitfall: misleading "0 chunks" output on re-run** — Running `gbrain embed --stale` when embeddings are already at 100% coverage reports "Embedded 0 chunks across NNN pages" and exits cleanly. This does NOT mean embeddings were lost — it means nothing was stale. Verify with `gbrain doctor --json` (check `embeddings` status: "100% coverage, 0 missing").

**Performance expectations (NVIDIA API rate limit)**:
- ~207K chunks from 2405 pages (avg ~86 chunks/page)
- Throughput: ~500-600 chunks/minute (NVIDIA API rate-limited)
- Completion time: ~5-6 hours for a full 2400-page import
- If interrupted, `gbrain embed --stale` resumes from checkpoint automatically

### Error Handling During Embed

Common embedding errors and their fixes:

| Error | Cause | Fix |
|-------|-------|-----|
| `Input length NNN exceeds maximum allowed token size 512` | e5-v5's 512 token limit | Lower `MAX_CHARS` in `embedding.ts` (480 recommended) |
| `expected NNN dimensions, not XXX` | DB vector col dim ≠ model output dim | Rebuild DB with matching `vector(n)` |
| `column cannot have more than 2000 dimensions for hnsw index` | Model dims >2000 | Use e5-v5 (1024 dims) instead of nv-embed-v1 (4096) |
| `infinite value not allowed in vector` | Corrupted content in source | Skip the file or re-extract text |
| `400 "input_type parameter is required"` | Model is asymmetric (query ≠ passage) | Add `input_type: "passage"` to request (already in GBrain's code) |
| `File too large (NNNN bytes)` | .md >10MB (GBrain import limit) | Split the file or skip it — common for large xlsx-to-md conversions |

### Verify

```bash
# Semantic search test
gbrain query "your test query"

# Health check — monitor embedding coverage and brain score progression
gbrain doctor | grep -E "embed|score|missing"

# JSON output for programmatic use:
gbrain doctor --json | python3 -c "
import sys,json; d=json.load(sys.stdin)
print(f'Score: {d[\"health_score\"]}/100, Status: {d[\"status\"]}')
for c in d.get('checks', []):
    if c['name'] in ('embeddings','brain_score'):
        print(f\"  {c['name']}: {c['message'][:120]}\")
"

# Expected brain score during a fresh 2400-page import:
#   No embed yet:  10/100
#   Partial embed: 19→27→35 (increases linearly with coverage)
#   Full embed:    43/100 (embed subscore: 33/35)
#   With knowledge graph: 70+/100 (after extract links + timeline)
```

## Knowledge Graph (Post-Import)

After importing, wire up the entity-relationship graph:

```bash
gbrain extract links --source db --dry-run | head -20   # preview
gbrain extract links --source db                          # commit
gbrain extract timeline --source db                       # dated events
gbrain stats                                              # verify links > 0
```

This enables `gbrain graph-query <slug> --depth 2` for relationship traversal.

### Expected Behavior for Document-Based Imports

If your source documents are **flat work records** (accounting ledgers, meeting notes, administrative reports) without wiki-style internal cross-references, the knowledge graph extraction will produce **0 links and 0 timeline entries**. This is **normal** — the extraction finds explicit inter-page relationships (hyperlinks, backlinks, dated cross-references) that don't exist in standalone documents.

The brain score impact:
| Component | Max Score | Doc Import | Wiki Import |
|-----------|-----------|------------|-------------|
| Embeddings | 35/35 | ✅ 35/35 | ✅ 35/35 |
| Entity Links | 25/25 | ❌ 0/25 | ✅ varies |
| Timeline | 15/15 | ❌ 0/15 | ✅ varies |
| Orphans | 15/15 | ✅ 15/15 | ✅ varies |
| Dead Links | 10/10 | ✅ 10/10 | ✅ 10/10 |

**Total:** ~45/100 for document imports vs 70+/100 for wiki-style content. The missing 30+ points are structurally unreachable for flat documents — **no configuration change can fix this**, and it does not affect vector search quality.

Verify with:
```bash
gbrain doctor --json | python3 -c "
import sys,json; d=json.load(sys.stdin)
for c in d['checks']:
    if c['name'] in ('embeddings','brain_score','graph_coverage'):
        print(f\"{c['name']}: {c['message'][:120]}\")
"

## Scheduled Weekly Sync (Cron)

Keep the knowledge base in sync by running a cron job every Friday to scan for new/modified documents, convert, import, and embed.

### Setup

1. Create the helper script `~/.hermes/scripts/weekly_scan.py`:

```python
#!/usr/bin/env python3
"""Weekly scan: check source dir for new/modified files, convert, import to GBrain, and embed."""
import os, subprocess, time, sys
from pathlib import Path

SRC = "/mnt/e/百度云同步盘/工作台账"
DST = os.path.expanduser("~/brain_src/工作台账")
CONVERT_SCRIPT = os.path.expanduser("~/brain_src/convert_docs.py")
GBRAIN_DIR = os.path.expanduser("~/gbrain")

# ... (run convert, import --no-embed, embed --stale, verify with stats)
```

2. Create the cron job (runs every Friday noon):

```bash
hermes cron create "0 12 * * 5" --name "每周台账扫描" --script weekly_scan.py --no-agent --deliver origin
```

- `--no-agent` keeps it token-free — the script runs directly and only reports results
- `--script` points to the file in `~/.hermes/scripts/` (auto-resolved by the cron runner)
- The conversion script (from `scripts/convert_docs.py`) handles docx/xlsx/pdf → md conversion

### Pitfalls

- **PGLite single-connection** — the cron job will fail if another `gbrain embed` is running. Kill stale processes first: `pkill -9 -f "gbrain embed"`
- **NVIDIA API rate limits** — ~500-600 chunks/minute. A full scan of 100+ new files may take 30-60 minutes. Set script timeout to 900s.
- **Import failures on corrupted files** — the conversion script skips old `.xls` format and damaged `.docx` files. Monitor cron delivery for error counts.
- **Cron sessions pass `skip_memory=True` by default** — the weekly scan runs without Hindsight memory injection, which is correct for a mechanical task.

## Report Generation with Style Reference

For agents generating work reports (monthly/quarterly/annual) based on historical documents:

### Pattern: Date-Gated Cron Job

Use a Python gate script + cron date-range to run only on the last working day:

1. Create `~/.hermes/scripts/is_last_working_day.py` that outputs `LAST_WORKING_DAY|month|YYYY-MM-DD` or `NOT_TODAY`
2. Schedule cron on the last 4 days of month (`0 12 28-31 * *`)
3. The agent prompt instructs: "Check Script Output. If NOT_TODAY, skip. If LAST_WORKING_DAY, generate report."

This limits agent invocation to at most 4 days per month instead of running daily.

### Style Reference Workflow

For generating reports that match the user's existing writing style:

1. **Locate reference documents** — search `/mnt/e/百度云同步盘/工作台账/` for historical reports (季度工作总结, 年度工作总结, 月度重点工作)
2. **Analyze style markers** — heading hierarchy, data presentation (tables vs prose), paragraph structure, formality level, section ordering
3. **Query GBrain** for current-period materials: `cd ~/gbrain && gbrain recall "YYYY年Q季度 工作 总结"`
4. **Generate** following the same template structure with current-period data

Example cron prompt structure for a quarterly report job:
```
Schedule: 0 12 28-31 3,6,9,12 *
Script: is_last_working_day.py
Toolsets: terminal, file, session_search
Prompt:
  [Step 1] Check Script Output for "LAST_WORKING_DAY|quarter"
  [Step 2] Find and read 2-3 previous quarterly reports from the work ledger
  [Step 3] Analyze writing style (format, section structure, data presentation)
  [Step 4] Query GBrain: "YYYY年X季度 工作"
  [Step 5] Generate report following the style template
```

## Pitfalls

- **`patch` / `write_file` cannot write to `~/.hermes/.env`** — use `terminal` with `echo ... >> ~/.hermes/.env` instead (user approval will be prompted).
- **Bun global install breaks migrations** — always use `git clone + bun link`, never `bun install -g`.
- **nv-embed-v1 dimension trap** — nv-embed-v1 outputs 4096 dims, not 1024. PGLite HNSW index caps at 2000 dims. **nv-embed-v1 can never work with PGLite.** Always use `nv-embedqa-e5-v5` (1024 dims).
- **Old `.xls` format** — openpyxl cannot read `.xls` (Excel 97-2003). The conversion script skips these. If those files are critical, install `xlrd` (`pip install xlrd`) and add a conversion branch for `.xls` files.
- **Damaged `.docx` files** — pandoc may fail with "couldn't unpack docx container: not enough bytes" on corrupted files. Skip them.
- **PGLite is single-connection** — parallel import workers only work with Postgres backend.
- **Chinese filenames/paths** work fine in WSL via `/mnt/<drive>/`. Use quotes around paths with special characters.
- **WSL performance** — Accessing files on `/mnt/e/` is slower than local Linux paths (~1/10 speed). For batch operations on thousands of files, prefer copying to `~/` first, or work in-place with longer timeouts. `cp -r` on large directories (41GB+) will timeout at 120s; use rsync or copy per-year subdirectories individually.
- **Sync checkpoint** — `gbrain import` saves a checkpoint at `~/.gbrain/import-checkpoint.json`. Delete it to force a fresh import.
- **Database rebuild** — schema dimension changes require DB wipe and `gbrain init`. Backup first: `cp -r ~/.gbrain ~/.gbrain.bak`. Use Python's `shutil.rmtree` to delete PGLite directory (faster than `rm -rf` on Postgres directories with thousands of small files).
- **nv-embedqa-e5-v5 token limit** — e5-v5 only supports 512 input tokens. Always set `MAX_CHARS = 480` in `embedding.ts` to leave headroom for system tokens. Without this, embedding will error on most real-world chunks.
- **`input_type` parameter** — NVIDIA's asymmetric embedding models (nemoretriever, nv-embedqa-*) require `input_type: "passage"` in the request body. GBrain's `embedding.ts` already includes this, but if testing via direct curl you must add it.
