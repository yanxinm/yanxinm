# 2026-06-08 实战记录

## 环境

- 主机：M710q Ubuntu，用户 miao
- Hermes 版本：通过 venv 安装
- 现有 profile：default (deepseek-v4-pro, Gateway running)
- 目标：创建 wenan, jike, lvyou, zhidu 四个 profiles

## 执行序列

### 1. 清理断链（关键）

```bash
# 发现 gstack 断链导致 --clone 失败
find /home/miao/.hermes/skills -xtype l
# → /home/miao/.hermes/skills/gstack → broken

rm /home/miao/.hermes/skills/gstack
```

**Pitfall**：所有四个 `hermes profile create --clone` 同时失败，错误 `shutil.Error: No such file or directory`，但 profile 目录已部分创建，需一并清理。

### 2. 批量创建

```bash
hermes profile create wenan --clone
hermes profile create jike --clone  
hermes profile create lvyou --clone
hermes profile create zhidu --clone
```

结果：
- /home/miao/.hermes/profiles/wenan/  ← 含 config.yaml, .env, skills/
- /home/miao/.hermes/profiles/jike/
- /home/miao/.hermes/profiles/lvyou/
- /home/miao/.hermes/profiles/zhidu/
- /home/miao/.local/bin/wenan, jike, lvyou, zhidu  ← CLI wrappers

### 3. 写 SOUL.md

四个文件分别写入，内容见 `references/soul-templates.md`。

### 4. 烟雾测试

```bash
wenan chat -q "你是谁？用一句话回答" 2>&1 | tail -5
# ✅ 8s, 加载了 laomiao-writing-style

jike chat -q "你是谁？用一句话回答" 2>&1 | tail -5
# ✅ 9s

lvyou chat -q "你是谁？用一句话回答" 2>&1 | tail -5  
# ✅ 10s

zhidu chat -q "你是谁？用一句话回答" 2>&1 | tail -5
# ✅ 11s
```

### 5. Kanban 初始化

```bash
hermes kanban init
# → /home/miao/.hermes/kanban.db
# → 自动发现 5 个 profiles: default, jike, lvyou, wenan, zhidu
```

### 6. Cron 任务创建

三个 cron job 均用 `profile='wenan'` 参数：

| Job ID | Name | Schedule | Profile |
|--------|------|----------|---------|
| dfdd687d1890 | 工作台账扫描 | 0 9 * * 1 | wenan |
| 847cc99e02d0 | 月度报告提醒 | 0 9 25 * * | wenan |
| b731c281a20f | 意识形态报告提醒 | 0 9 25 3,6,9,12 * | wenan |

### 7. 路由规则写 Memory

遇到 Memory 满 (1897/2200) → 先删除"黑苹果启动盘"条目 → 再写入路由规则。

## 已发现但未修复

- 灾备 cron `hermes_backup.sh` 报错：`cd: /home/miao/yanxinm: 没有那个文件或目录`（路径残留）
- Profile skills 是 clone 副本，更新主 skill 不同步
