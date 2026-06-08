# TencentDB Agent Memory

腾讯开源的四层本地记忆系统，MIT 协议，支持 Hermes 和 OpenClaw Agent。

**仓库**: https://github.com/Tencent/TencentDB-Agent-Memory  
**npm 包**: `@tencentdb-agent-memory/memory-tencentdb`  
**Stars**: 3332（截至 2026-05-19）  
**最近更新**: 2026-05-18  

## 架构：4层记忆金字塔

```
L3 用户画像 (Persona)         ← 顶层：日常偏好、长期目标
L2 场景块 (Scenario)          ← 中层：工作流模板、场景经验
L1 原子事实 (Atom)            ← 中层：具体事实、日期、项目细节
L0 对话原始记录 (Conversation)  ← 底层：原始对话文本
```

区别于 Hindsight 的扁平向量检索，每层可逐级下钻，上层保留结构、下层保留证据。

### 短记忆（Context Offload）

将冗长的工具日志（搜索结果、代码、错误堆栈）压缩为 **Mermaid 符号图**，上下文只保留轻量节点。通过 `node_id` 可回溯到完整原始日志。节省 Token 30-61%。

### 关键特性

| 特性 | 说明 |
|------|------|
| 存储引擎 | SQLite + sqlite-vec（无独立进程） |
| 检索方式 | BM25 + 向量 + RRF 混合排序（支持中文） |
| 记忆压缩 | Mermaid 符号图 + 文件外卸 |
| 审计性 | 每层为可读 Markdown，白盒可追踪 |
| 外部依赖 | 零（全本地） |
| 分布式模型 | 需 LLM API key 进行记忆蒸馏（可与 Hermes 共用） |

## 与 Hindsight 对比

| 维度 | Hindsight | TencentDB Agent Memory |
|------|-----------|----------------------|
| 内存 | ~1.5GB（嵌入模型+PostgreSQL） | ~<200MB（SQLite嵌入式） |
| 磁盘 | ~281MB (PostgreSQL) | 预计 50-100MB |
| 记忆结构 | 扁平向量片段 | 4层金字塔（可下钻） |
| 短记忆压缩 | 无 | Mermaid符号图（节省 30-61% Token） |
| 中文支持 | 英文嵌入 | jieba 中文分词 |
| Token节省基准 | — | WideSearch -61%, SWE-bench -33% |
| 成功率基准 | — | WideSearch +51.5%, PersonaMem 48%→76% |
| 独立进程 | PostgreSQL + hindsight-api daemon | 无（作为插件运行） |

## 安装（Hermes 集成）

### 方法1：Docker（官方推荐）

```bash
# 需要 Docker daemon 运行中（WSL 下需 root 或 rootless）
# 仓库根目录
docker build -f docker/opensource/Dockerfile.hermes -t hermes-memory .

docker run -d --name hermes-memory --restart unless-stopped \
  -p 8420:8420 \
  -e MODEL_API_KEY="***" \
  -e MODEL_BASE_URL="https://api.lkeap.cloud.tencent.com/v1" \
  -e MODEL_NAME="deepseek-v3.2" \
  -e MODEL_PROVIDER="custom" \
  -v hermes_data:/opt/data \
  hermes-memory
```

### 方法2：NPM 安装（无 Docker）

项目自带安装脚本 `scripts/install_hermes_memory_tencentdb.sh`，流程：

1. 通过 npm 下载 `@tencentdb-agent-memory/memory-tencentdb` 到 `~/.memory-tencentdb/`
2. 安装 Node.js 依赖（`npm install`）
3. 创建 Hermes 插件 symlink：`~/.hermes/hermes-agent/plugins/memory/memory_tencentdb/` 指向插件源目录
4. 配置环境变量到 `~/.hermes/.env` 和 `/etc/profile.d/`
5. 需要将 `memory.provider` 设置为 `memory_tencentdb` 启用

```
手动安装要点：
- Node.js >= 22.16 必须
- Hermes Agent 需预先安装（`~/.hermes/hermes-agent/` 存在）
- 需要 LLM API key（记忆蒸馏用），设 MEMORY_TENCENTDB_LLM_*
- 内存 Gateway 运行在 8420 端口，Hermes 插件通过 HTTP 与之通信
```

### 架构（无 Docker）

```
Hermes Agent (Python)
  └─ memory_tencentdb 插件 (plugin.yaml)
       └─ hooks: on_memory_write, on_session_end
            └─ HTTP ↔ 内存 Gateway (Node.js, :8420)
                  └─ SQLite + sqlite-vec 存储
```

## 注意（WSL 环境）

- Docker daemon 在 WSL 默认需要 root 权限。无免密 sudo 时可用 rootless 模式（需先 `apt-get install uidmap`）
- 若采用 NPM 安装，需要 Hermes Agent 的 `plugins/memory/` 目录可写（本环境已具备）
- 内存 Gateway 端口 8420 不能与已有服务冲突
- 切换记忆提供者需要 `/reset`（CLI）或 Gateway 重启

## 参考

- [仓库 README](https://github.com/Tencent/TencentDB-Agent-Memory)
- [README_CN 中文版](https://github.com/Tencent/TencentDB-Agent-Memory/blob/main/README_CN.md)
- 安装脚本: `scripts/install_hermes_memory_tencentdb.sh`
- Dockerfile: `docker/opensource/Dockerfile.hermes`
- 源码: `src/core/` (L0-L3 pipeline), `src/gateway/` (Node.js Gateway), `src/offload/` (context offload)
