#!/usr/bin/env python3
"""
Weekly scan: check E:/百度云同步盘/工作台账 for new/modified files,
convert to markdown, import to GBrain, and embed.
"""
import os
import subprocess
import sys
import time
from pathlib import Path

SRC = "/mnt/e/百度云同步盘/工作台账"
DST = os.path.expanduser("~/brain_src/工作台账")
CONVERT_SCRIPT = os.path.expanduser("~/brain_src/convert_docs.py")
GBRAIN_DIR = os.path.expanduser("~/gbrain")

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M')}] {msg}", flush=True)

def main():
    log("Starting weekly file scan...")

    # Step 1: Run the conversion script for any new/changed files
    if os.path.exists(CONVERT_SCRIPT):
        log(f"Running conversion script: {CONVERT_SCRIPT}")
        result = subprocess.run(
            [sys.executable, CONVERT_SCRIPT],
            capture_output=True, text=True, timeout=600
        )
        if result.returncode != 0:
            log(f"Conversion errors:\n{result.stderr[-500:]}")
        else:
            log(f"Conversion output:\n{result.stdout[-300:]}")
    else:
        log(f"WARNING: Conversion script not found at {CONVERT_SCRIPT}")

    # Step 2: Count new md files
    md_count = 0
    for year_dir in sorted(os.listdir(DST)):
        year_path = os.path.join(DST, year_dir)
        if os.path.isdir(year_path):
            for root, _, files in os.walk(year_path):
                md_count += len([f for f in files if f.endswith('.md')])
    log(f"Total markdown files available: {md_count}")

    # Step 3: Import to GBrain
    log("Importing to GBrain...")
    result = subprocess.run(
        ["gbrain", "import", DST, "--no-embed"],
        capture_output=True, text=True, timeout=600,
        cwd=GBRAIN_DIR
    )
    if result.returncode != 0:
        log(f"GBrain import errors:\n{result.stderr[-500:]}")
    else:
        log(f"GBrain import:\n{result.stdout[-300:]}")

    # Step 4: Embed stale pages
    log("Running gbrain embed --stale...")
    result = subprocess.run(
        ["gbrain", "embed", "--stale"],
        capture_output=True, text=True, timeout=900,
        cwd=GBRAIN_DIR
    )
    if result.returncode != 0:
        log(f"GBrain embed errors:\n{result.stderr[-500:]}")
    else:
        log(f"GBrain embed:\n{result.stdout[-300:]}")

    # Step 5: Quick stats
    result = subprocess.run(
        ["gbrain", "stats"],
        capture_output=True, text=True, timeout=30,
        cwd=GBRAIN_DIR
    )
    log(f"GBrain stats:\n{result.stdout}")

    log("Weekly scan completed.")

if __name__ == "__main__":
    main()
