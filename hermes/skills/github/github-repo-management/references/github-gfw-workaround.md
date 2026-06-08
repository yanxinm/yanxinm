# GitHub Cloning Behind GFW

## Problem
`git clone` from `github.com` times out on mainland China networks, but `api.github.com` remains accessible.

## Workaround: Download Tarball via API

### Step 1: Download
```bash
curl -L --connect-timeout 30 -o /tmp/repo.tar.gz \
  "https://api.github.com/repos/<owner>/<repo>/tarball/main"
```
Typical speed: ~100KB/s. For a 7MB repo, expect ~60-70 seconds.

### Step 2: Extract
```bash
mkdir -p /path/to/target && \
tar xzf /tmp/repo.tar.gz -C /path/to/target --strip-components=1
```

### Step 3: Initialize Git (optional, for tracking)
```bash
cd /path/to/target
git init
git remote add origin https://github.com/<owner>/<repo>.git
```

## Limitations
- No `.git` history (shallow snapshot only)
- Cannot `git pull` updates — must re-download
- Max tarball size ~2GB (GitHub API limit)
- For large repos, use `--depth 1` with a proxy instead

## Alternative: Shallow Clone with Proxy
```bash
git clone --depth 1 https://ghproxy.com/https://github.com/<owner>/<repo>.git
```
