---
name: file-deduplication
description: "Find and remove duplicate files in large directory trees using content hashing. Supports batch scanning, progress reporting, configurable retention rules, and safe bulk deletion."
version: 1.0.0
author: Hermes Agent
platforms: [linux, macos, wsl]
---

# File Deduplication

Find exact duplicate files in a directory tree by computing content hashes (MD5). Designed for large collections (10K–100K+ files) with cross-filesystem access (WSL → Windows drives).

## When to Use

- User has a messy photo/media collection with copies scattered across folders
- Disk space is filling up and duplicate files are suspected
- Backup or sync operations have created duplicates (e.g. `_1` suffixed copies)
- A `重复/` (duplicate) folder exists with moved copies

## Decision: GUI Tool vs Script

Before diving into the script workflow, offer the user a choice:

- **Option A (Windows GUI tools):** czkawka, dupeGuru, or CCleaner on Windows. Faster (native NTFS), has preview UI, safer for selective deletion. Best when the user is at their desktop and wants visual confirmation.
- **Option B (background script):** Python MD5-hash script in WSL. Batch-only, no UI, requires user approval before delete. Best when photos are plentiful and the user wants to set-and-forget.

Let the user choose. If they pick B, proceed with the workflow below.

## Workflow

### Phase 1: Write and launch the scanner

Create a Python script with these key components and save it to `~/Hermes-Agent/scripts/` or `~/.hermes/scripts/`:

```python
import os, hashlib, json, time
from collections import defaultdict

PHOTOS_DIR = "/path/to/target"
CACHE_FILE = "/tmp/dedup_cache.json"
REPORT_FILE = "/tmp/dedup_report.txt"
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', ...}

def file_md5(filepath):
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(65536)
            if not chunk: break
            h.update(chunk)
    return h.hexdigest()
```

Key design decisions:
- **Streaming hash** — 64KB chunks; no memory pressure for multi-GB files
- **Path+size cache key** — enables resumable scanning; stores `{fpath|fsize: md5}`
- **Batch progress** — report every 200 files so the user isn't waiting blind
- **Background execution** — use `nohup` or `terminal(background=True)` for large collections

### Phase 2: Retention rule (pick_keep)

For each duplicate group (same MD5), decide which file to keep:

```python
def pick_keep(files):
    """
    Priority rules:
    1. Prefer files NOT in a "重复/" (duplicate) folder
    2. If all are in "重复/", keep the shortest path
    3. If all are in normal folders, prefer year-named folders over "未分类"
    4. If still tied, keep the one with the shortest path
    """
    normal = [f for f in files if "/重复/" not in f["path"]]
    if normal:
        # Among normal files, prefer year-folders over "未分类"
        year_folder = [f for f in normal if not "/未分类/" in f["path"]]
        if year_folder:
            return min(year_folder, key=lambda f: len(f["path"]))
        return min(normal, key=lambda f: len(f["path"]))
    # All in duplicate folder → shortest path
    return min(files, key=lambda f: len(f["path"]))
```

### Phase 3: Report

Generate a text report with summary + per-group details:

```
去重报告 - {timestamp}
共 N 组重复, M 个文件, 可释放 X.XX GB

--- 重复组 (MD5: a1b2c3..., 1234.5KB) ---
  [保留] /path/to/keep.jpg
  [删除] /path/to/delete1.jpg
  [删除] /path/to/delete2.jpg
...
```

### Phase 4: Execute deletion

Run the script again with `--delete` flag. Show per-batch progress:

```python
if "--delete" in sys.argv:
    for md5, files in dupes.items():
        keep = pick_keep(files)
        for f in files:
            if f != keep:
                os.remove(f["path"])
                if deleted % 200 == 0:
                    print(f"已删除 {deleted} 个文件, 释放 {saved/(1024**3):.2f} GB")
```

### Phase 5: Cleanup

```bash
rm -f /tmp/dedup_cache.json /tmp/dedup_report.txt
```

## Pitfalls

- **Cross-filesystem performance:** Scanning files on `/mnt/e/` (Windows NTFS via WSL) is slow. Each `os.path.getsize()` or `os.remove()` call has WSL↔Windows overhead. Estimate: ~60-120 seconds per 1000 files for MD5 hashing over /mnt/.
- **Background process timeout:** The default timeout for terminal(background=True) may be 120s for process execution. For 37K+ images, set an explicit `timeout=600` (10 minutes) or more. Otherwise the process may be killed silently before producing any output.
- **First-run failure:** If the background process returns no output and no files, it likely timed out. Restart with a longer timeout.
- **File handles on Windows:** Files opened in Windows apps (Explorer preview pane, photo viewer) may cause permission errors on deletion. Skip `PermissionError` gracefully.
- **Cache size:** A 37K-file scan produces a ~2MB JSON cache. This is fine, but the initial `json.load()` takes a second.
- **Background process notifications:** Use `terminal(background=True, notify_on_complete=True)` so the agent is alerted when done.
- **Always preview before delete:** Generate the report first and confirm with the user. The `pick_keep` logic is automated but the user should approve the strategy.
- **Only exact duplicates:** This is MD5-based — it finds pixel-identical files only. It won't find near-duplicates or resized versions.

## Example (from real session)

- Target: `/mnt/e/网盘图片/` (37,000+ files, cross-WSL)
- Duration: ~27 minutes to scan, ~2 minutes to delete
- Result: 6,510 duplicate groups, 7,699 files deleted, 5.57 GB recovered
- Retention: kept files in normal folders (year-based > uncategorized) over `重复/` folder
- Full log: see `references/wsl-ntfs-photo-dedup.md` in this skill directory

## Related Skills
