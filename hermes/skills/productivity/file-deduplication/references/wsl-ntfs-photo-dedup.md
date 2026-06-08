# WSL → NTFS Photo Deduplication (Real Session)

## Context

- Target: `/mnt/e/网盘图片/` — 37,731 images across 24 folders
- Windows E: drive, accessed via WSL's 9p protocol
- Folder structure: year-folders (2000-2026) + `重复/` (8,622 files pre-moved) + `未分类/` (13,360 files)
- Total photo size: ~50GB+
- Retention strategy: keep files in year-folders > classified > shorter paths; delete from `重复/` folder

## Script Location

`~/Hermes-Agent/scripts/dedup-photos.py`

## Launch Command

```python
# Background execution with extended timeout (critical!)
terminal(background=True, timeout=600, notify_on_complete=True, command="cd ~ && python3 ~/Hermes-Agent/scripts/dedup-photos.py")
```

## Timing (37K files over /mnt/e/)

- Scanning (MD5 hashing): ~27 minutes
- Deletion (os.remove): ~2 minutes

## Result

- 6,510 duplicate groups found
- 7,699 duplicate files deleted
- 5.57 GB space recovered

## Key Files

| File | Purpose |
|------|---------|
| `/tmp/dedup_cache.json` | Scan cache (path+size → MD5); loadable for resume |
| `/tmp/dedup_report.txt` | Full report of all duplicate groups |
| `~/Hermes-Agent/scripts/dedup-photos.py` | The scanner script |

## What Went Wrong (First Attempt)

1. First run used `process(action='start', ...)` — the process disappeared with no output and no files.
2. Root cause: default timeout killed it before the first 200 files were scanned.
3. Fix: use `terminal(background=True, timeout=600)` instead.

## Retention Rule Used

```python
def pick_keep(files):
    # 1. Prefer files NOT in "重复/" folder
    normal = [f for f in files if "/重复/" not in f["path"]]
    if normal:
        # 2. Among normal, prefer files in year-folders (4-digit)
        year_files = [f for f in normal if any(
            p.isdigit() and len(p)==4 for p in f["path"].split("/"))]
        if year_files:
            return min(year_files, key=lambda x: x["path"])
        # 3. Then prefer classified (not in "未分类/")
        classified = [f for f in normal if "/未分类/" not in f["path"]]
        if classified:
            return min(classified, key=lambda x: x["path"])
        return min(normal, key=lambda x: x["path"])
    # 4. All in "重复/" — keep shortest path
    return min(files, key=lambda x: x["path"])
```
