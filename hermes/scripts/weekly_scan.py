#!/usr/bin/env python3
"""
每周台账扫描（基地版）：
1. 从笔记本 Samba 共享同步文档到本地副本 ~/工作台账/
2. 列出最近7天新增/修改的文档
3. 输出摘要供后续 LLM 任务使用
"""
import os
import subprocess
import sys
import time
from pathlib import Path

LOCAL = os.path.expanduser("~/工作台账")
SYNC_SCRIPT = os.path.expanduser("~/.hermes/scripts/sync_taizhang.sh")
DAYS = 7


def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M')}] {msg}", flush=True)


def main():
    log("=" * 50)
    log("每周台账扫描开始")

    # ===== Step 1: 同步 =====
    if os.path.exists(SYNC_SCRIPT):
        log("执行同步脚本...")
        result = subprocess.run(
            ["bash", SYNC_SCRIPT],
            capture_output=True, text=True, timeout=600
        )
        print(result.stdout, flush=True)
        if result.returncode != 0:
            log(f"同步出错 (exit={result.returncode}):\n{result.stderr[-300:]}")
            # 不退出 — 本地副本可能已有历史数据，继续扫描
    else:
        log(f"同步脚本不存在: {SYNC_SCRIPT}，跳过同步，直接扫描本地副本")

    # ===== Step 2: 扫描最近 N 天的新增/修改文件 =====
    log(f"扫描 {LOCAL} 最近 {DAYS} 天内变动的文档...")
    now = time.time()
    cutoff = now - DAYS * 86400

    recent_files = []
    if os.path.isdir(LOCAL):
        for root, dirs, files in os.walk(LOCAL):
            for f in files:
                fpath = os.path.join(root, f)
                try:
                    mtime = os.path.getmtime(fpath)
                    if mtime >= cutoff:
                        rel = os.path.relpath(fpath, LOCAL)
                        size_kb = os.path.getsize(fpath) / 1024
                        recent_files.append((rel, size_kb, mtime))
                except OSError:
                    continue

    # 按修改时间排序（最新在前）
    recent_files.sort(key=lambda x: x[2], reverse=True)

    # ===== Step 3: 输出摘要 =====
    total_local = sum(1 for _ in Path(LOCAL).rglob("*") if _.is_file()) if os.path.isdir(LOCAL) else 0
    log(f"本地副本总计: {total_local} 个文件")
    log(f"近 {DAYS} 天变动: {len(recent_files)} 个文件")
    print()

    if recent_files:
        for rel, size, mtime in recent_files[:50]:  # 最多展示50个
            ts = time.strftime("%m-%d %H:%M", time.localtime(mtime))
            print(f"  {ts}  {size:7.1f}KB  {rel}")
        if len(recent_files) > 50:
            print(f"  ... 以及其他 {len(recent_files) - 50} 个文件")
    else:
        print("  （无最近变动的文件）")

    print()
    log("每周台账扫描完成")
    log("=" * 50)


if __name__ == "__main__":
    main()
