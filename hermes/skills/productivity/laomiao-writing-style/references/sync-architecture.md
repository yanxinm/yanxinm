# 文档同步管线架构

## 概览

工作台账从笔记本（Ethan）到基地（M710q）的文档同步管线。

```
笔记本 E:\百度云同步盘\工作台账\
        │  Samba 共享 (Tailscale 100.86.148.56)
        │  每周同步
        ▼
基地 /mnt/ethan_taizhang/  ← 挂载点（仅同步时）
        │  rsync 增量
        ▼
基地 /home/miao/工作台账/   ← 本地副本（扫描任务数据源）
```

## 关键参数

| 参数 | 值 |
|------|-----|
| 源路径 | 笔记本 `E:\百度云同步盘\工作台账\` |
| Samba 共享名 | `\\100.86.148.56\工作台账` |
| Samba 账户 | `taizhang` |
| 挂载点 | 基地 `/mnt/ethan_taizhang/` |
| 本地副本 | 基地 `/home/miao/工作台账/` |
| 文件范围 | docx/doc/xlsx/xls/pdf/txt/md（不含 PPT/媒体） |
| 总量 | ~3726 份文档，2.49 GB |
| 同步频率 | 每周一次（周五扫描前） |

## 涉及脚本

| 脚本 | 路径 | 用途 |
|------|------|------|
| `sync_taizhang.sh` | `~/.hermes/scripts/sync_taizhang.sh` | 挂载→rsync→卸载 |
| `weekly_scan.py` | `~/.hermes/scripts/weekly_scan.py` | 调 sync + 扫描近7天变动（无 Agent 脚本） |

## 相关定时任务

| 任务 | 触发 | 说明 |
|------|------|------|
| `5323ccd7cf51` 每周台账扫描 | 周五 12:00 | no_agent，调 sync_taizhang.sh 后统计 |
| `dfdd687d1890` 工作台账扫描 | 周一 9:00 | wenan profile，LLM 驱动，加载 laomiao-writing-style+markitdown |

## 渐进路线

1. **当前阶段**：笔记本 Samba 共享 → 基地挂载 → rsync 本地副本。扫描跑本地路径。
2. **成熟阶段**：本地副本沉淀足够历史文档，挂载仅用于增量。笔记本离线不影响扫描。
3. **最终阶段**：本地知识库自给自足，彻底去掉对笔记本的依赖。

## 权限注意

- `mount/umount` 需要 miao 用户的免密 sudo（`/etc/sudoers.d/miao-mount`）
- 若笔记本离线导致挂载失败，`weekly_scan.py` 会跳过同步、直接扫描本地副本（容错设计）
