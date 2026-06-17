#!/bin/bash
# ============================================================
# Hermes Agent 全量备份脚本
# 备份目录: /mnt/e/Hermes备份/
# 自动保留最近30天备份，更早的自动清理
# ============================================================

set -e

BACKUP_ROOT="/mnt/e/Hermes备份"
HERMES_HOME="$HOME/.hermes"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$BACKUP_ROOT/hermes-backup-$TIMESTAMP"
RETENTION_DAYS=30

echo "[$(date)] === Hermes 备份开始 ==="

# 1. 创建备份目录
mkdir -p "$BACKUP_DIR"
mkdir -p "$BACKUP_DIR/config"
mkdir -p "$BACKUP_DIR/skills"
mkdir -p "$BACKUP_DIR/databases"
mkdir -p "$BACKUP_DIR/memories"
mkdir -p "$BACKUP_DIR/cron"
mkdir -p "$BACKUP_DIR/logs"
mkdir -p "$BACKUP_DIR/plugins"

# 2. 备份核心配置文件
echo "[$(date)] 备份配置文件和密钥..."
cp "$HERMES_HOME/config.yaml" "$BACKUP_DIR/config/config.yaml" 2>/dev/null || echo "  WARN: config.yaml 不存在"
cp "$HERMES_HOME/config.yaml.bak" "$BACKUP_DIR/config/" 2>/dev/null || true
cp "$HERMES_HOME/.env" "$BACKUP_DIR/config/.env" 2>/dev/null || echo "  WARN: .env 不存在"
cp "$HERMES_HOME/SOUL.md" "$BACKUP_DIR/config/SOUL.md" 2>/dev/null || echo "  WARN: SOUL.md 不存在"
cp "$HERMES_HOME/auth.json" "$BACKUP_DIR/config/auth.json" 2>/dev/null || true
cp "$HERMES_HOME/channel_directory.json" "$BACKUP_DIR/config/" 2>/dev/null || true
cp "$HERMES_HOME/gateway_state.json" "$BACKUP_DIR/config/" 2>/dev/null || true
cp "$HERMES_HOME/processes.json" "$BACKUP_DIR/config/" 2>/dev/null || true
cp "$HERMES_HOME/feishu_seen_message_ids.json" "$BACKUP_DIR/config/" 2>/dev/null || true

# 3. 备份记忆文件（核心灵魂数据）
echo "[$(date)] 备份记忆和用户档案..."
cp "$HERMES_HOME/memories/MEMORY.md" "$BACKUP_DIR/memories/MEMORY.md" 2>/dev/null || echo "  WARN: MEMORY.md 不存在"
cp "$HERMES_HOME/memories/USER.md" "$BACKUP_DIR/memories/USER.md" 2>/dev/null || echo "  WARN: USER.md 不存在"
cp "$HERMES_HOME/hindsight/config.json" "$BACKUP_DIR/config/hindsight_config.json" 2>/dev/null || true

# 4. 备份数据库文件
echo "[$(date)] 备份数据库..."
cp "$HERMES_HOME/state.db" "$BACKUP_DIR/databases/state.db" 2>/dev/null || echo "  WARN: state.db 不存在"
cp "$HERMES_HOME/kanban.db" "$BACKUP_DIR/databases/kanban.db" 2>/dev/null || true
cp "$HERMES_HOME/response_store.db" "$BACKUP_DIR/databases/response_store.db" 2>/dev/null || true
cp "$HERMES_HOME/response_store.db-shm" "$BACKUP_DIR/databases/" 2>/dev/null || true
cp "$HERMES_HOME/response_store.db-wal" "$BACKUP_DIR/databases/" 2>/dev/null || true

# 5. 备份定时任务配置
echo "[$(date)] 备份定时任务配置..."
cp "$HERMES_HOME/cron/jobs.json" "$BACKUP_DIR/cron/jobs.json" 2>/dev/null || echo "  WARN: cron/jobs.json 不存在"
# 记录定时任务摘要
if [ -f "$HERMES_HOME/cron/jobs.json" ]; then
    python3 -c "
import json
with open('$HERMES_HOME/cron/jobs.json') as f:
    data = json.load(f)
print('=== 定时任务摘要 ===')
if isinstance(data, dict):
    jobs = data.get('jobs', []) if 'jobs' in data else [data]
elif isinstance(data, list):
    jobs = data
else:
    jobs = []
print(f'共 {len(jobs)} 个定时任务')
print(json.dumps(jobs, indent=2, ensure_ascii=False))
" > "$BACKUP_DIR/cron/cron_summary.txt" 2>/dev/null || echo "  无法导出任务摘要"
fi

# 6. 备份技能库
echo "[$(date)] 备份技能库..."
tar -czf "$BACKUP_DIR/skills/skills.tar.gz" -C "$HERMES_HOME" skills/ 2>/dev/null || echo "  WARN: skills 目录备份失败"
ls -la "$HERMES_HOME/skills/" > "$BACKUP_DIR/skills/skills_list.txt" 2>/dev/null || true

# 7. 备份渠道和平台配置
echo "[$(date)] 备份平台配置..."
if [ -d "$HERMES_HOME/platforms" ]; then
    tar -czf "$BACKUP_DIR/platforms.tar.gz" -C "$HERMES_HOME" platforms/ 2>/dev/null || true
fi

# 8. 备份脚本和插件
echo "[$(date)] 备份脚本和插件..."
if [ -d "$HERMES_HOME/scripts" ]; then
    tar -czf "$BACKUP_DIR/scripts.tar.gz" -C "$HERMES_HOME" scripts/ 2>/dev/null || true
fi
if [ -d "$HERMES_HOME/plugins" ]; then
    tar -czf "$BACKUP_DIR/plugins/plugins.tar.gz" -C "$HERMES_HOME" plugins/ 2>/dev/null || true
fi

# 9. 备份近期日志（保留最后500KB）
echo "[$(date)] 备份近期日志..."
if [ -d "$HERMES_HOME/logs" ]; then
    LOGS_BACKUP="$BACKUP_DIR/logs"
    mkdir -p "$LOGS_BACKUP"
    for logfile in "$HERMES_HOME"/logs/*.log; do
        if [ -f "$logfile" ]; then
            basename=$(basename "$logfile")
            tail -c 512000 "$logfile" > "$LOGS_BACKUP/$basename" 2>/dev/null || true
        fi
    done
fi

# 10. 备份 .hermes 根目录下其他关键文件
echo "[$(date)] 备份其他关键文件..."
for f in "$HERMES_HOME"/*.json; do
    if [ -f "$f" ]; then
        base=$(basename "$f")
        # 跳过已在其他分类中备份的和缓存文件
        case "$base" in
            config.yaml|auth.json|channel_directory.json|gateway_state.json|processes.json|feishu_seen_message_ids.json)
                # 已在 config 目录备份
                ;;
            models_dev_cache.json|.skills_prompt_snapshot.json)
                # 缓存文件，不备份
                ;;
            *)
                cp "$f" "$BACKUP_DIR/config/$base" 2>/dev/null || true
                ;;
        esac
    fi
done

# 11. 备份 session 索引（不含内容）
echo "[$(date)] 备份会话索引..."
if [ -d "$HERMES_HOME/sessions" ]; then
    ls -la "$HERMES_HOME/sessions/" > "$BACKUP_DIR/session_index.txt" 2>/dev/null || true
fi

# 12. 保存恢复指南
echo "[$(date)] 生成恢复指南..."
cat > "$BACKUP_DIR/RESTORE_GUIDE.md" << 'EOF'
# Hermes Agent 完整恢复指南

## 备份时间
BACKUP_TIME_PLACEHOLDER

## 恢复步骤（在新服务器/重装后执行）

### 前提条件
- 已安装 Hermes Agent（git clone + pip install -e .）
- WSL/服务器环境已就绪

### 恢复命令

```bash
# 1. 停止当前 Hermes 服务
hermes gateway stop

# 2. 恢复配置
cp backup_dir/config/config.yaml ~/.hermes/config.yaml
cp backup_dir/config/.env ~/.hermes/.env
cp backup_dir/config/SOUL.md ~/.hermes/SOUL.md
cp backup_dir/config/auth.json ~/.hermes/auth.json
cp backup_dir/config/channel_directory.json ~/.hermes/channel_directory.json
cp backup_dir/config/gateway_state.json ~/.hermes/gateway_state.json
cp backup_dir/config/hindsight_config.json ~/.hermes/hindsight/config.json

# 3. 恢复记忆
cp backup_dir/memories/MEMORY.md ~/.hermes/memories/MEMORY.md
cp backup_dir/memories/USER.md ~/.hermes/memories/USER.md

# 4. 恢复数据库
cp backup_dir/databases/*.db ~/.hermes/
cp backup_dir/databases/*.db-shm ~/.hermes/ 2>/dev/null
cp backup_dir/databases/*.db-wal ~/.hermes/ 2>/dev/null

# 5. 恢复技能库
tar -xzf backup_dir/skills/skills.tar.gz -C ~/.hermes/

# 6. 恢复定时任务（需手动导入）
# cat backup_dir/cron/jobs.json 中的内容记录后，
# 用 hermes cron 命令逐一重建

# 7. 恢复平台配置
tar -xzf backup_dir/platforms.tar.gz -C ~/.hermes/ 2>/dev/null

# 8. 恢复脚本
tar -xzf backup_dir/scripts.tar.gz -C ~/.hermes/ 2>/dev/null

# 9. 重启 Gateway
hermes gateway restart

echo "恢复完成！"
```

注意事项：
- .env 中包含 API 密钥、token 等敏感信息，注意保护
- 恢复后需重新设置 .env 文件权限：chmod 600 ~/.hermes/.env
- 定时任务需要手动重建（因为 job_id 在新环境可能变化）
- 如果 hindsight 记忆系统使用外部 API，恢复 config.json 后会自动连接
EOF

sed -i "s/BACKUP_TIME_PLACEHOLDER/$(date '+%Y-%m-%d %H:%M:%S')/" "$BACKUP_DIR/RESTORE_GUIDE.md"

# 13. 创建备份清单
echo "[$(date)] 生成备份清单..."
cat > "$BACKUP_DIR/MANIFEST.txt" << EOF
Hermes Agent 全量备份
备份时间: $(date '+%Y-%m-%d %H:%M:%S')
备份大小: $(du -sh "$BACKUP_DIR" | cut -f1)
备份目录: $BACKUP_DIR

备份内容清单:
- 配置文件 (config.yaml, .env, SOUL.md, auth.json 等)
- 记忆文件 (MEMORY.md, USER.md)
- 数据库 (state.db, kanban.db, response_store.db)
- 定时任务配置 (cron/jobs.json)
- 技能库 (skills/ 完整目录)
- 平台配置 (platforms/)
- 自定义脚本 (scripts/)
- 插件配置 (plugins/)
- 近期日志 (logs/)
- 会话索引
- 恢复指南 (RESTORE_GUIDE.md)
EOF

# 14. 清理旧备份（保留30天）
echo "[$(date)] 清理 $RETENTION_DAYS 天前的旧备份..."
find "$BACKUP_ROOT" -maxdepth 1 -type d -name "hermes-backup-*" -mtime +$RETENTION_DAYS -exec rm -rf {} \; 2>/dev/null || true

BACKUP_SIZE=$(du -sh "$BACKUP_DIR" | cut -f1)
echo "[$(date)] === Hermes 备份完成 ==="
echo "[$(date)] 备份路径: $BACKUP_DIR"
echo "[$(date)] 备份大小: $BACKUP_SIZE"
echo "[$(date)] 保留策略: 最近 $RETENTION_DAYS 天"
