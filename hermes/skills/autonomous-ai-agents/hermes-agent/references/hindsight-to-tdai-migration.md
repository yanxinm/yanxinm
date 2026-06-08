# Hindsight → TDAI (TencentDB Agent Memory) 记忆迁移

## 背景

将 Hindsight PostgreSQL 中的 2,184 条记忆迁移到 TDAI 的 SQLite 向量库，
绕过 Seed API（因其每轮调用 LLM 提取记忆，太慢且 OOM 易挂）。

## 迁移步骤总览

### Step 1: 导出 Hindsight 记忆为 batch JSON

从 PostgreSQL `memory_units` 表导出，组织成 TDAI seed 格式（session + conversations）。

```sql
COPY memory_units TO '/tmp/hindsight_memories.json';
```

用 Python/Node 转换为 `{sessions: [{sessionKey, sessionId, conversations: [[userMsg, asstMsg], ...]}]}` 格式，
拆分为多个 batch JSON 文件（每文件约 100 轮对话）。

### Step 2: 直接写入向量库（绕过 Seed API）

Seed API 的问题：每轮对话都会调用 LLM 提取记忆慢，且进程易被 OOM Killer 干掉。
因此直接写 SQLite。

```bash
NODE_PATH=/home/yanxin/Hermes-Agent/node_modules node direct_import.js
```

脚本逻辑：
1. 读取所有 batch JSON 文件 → 解析 Hindsight 记忆
2. 去重（按内容前80字符）
3. 转换为 TDAI `l1_records` 表格式
4. 直接 `INSERT INTO l1_records` → 完成文本入库

### Step 3: 计算向量嵌入

文本入库后需要计算 1024 维浮点向量用于语义搜索。

**使用的模型**: `nvidia/nv-embedqa-e5-v5` via NVIDIA NIM API（1024 维）
**关键配置**: `input_type: "query"` 参数（该模型是 asymmetric 模型，必须加此参数）

```bash
cd ~/.memory-tencentdb && source ~/.hermes/.env && export NVIDIA_API_KEY && \
  node --experimental-sqlite embed_l1.cjs
```

脚本逻辑：
1. 用 `node:sqlite`（DatabaseSync）打开 vectors.db
2. 加载 sqlite-vec 扩展（需要 `{allowExtension: true}` 选项创建连接）
3. 查询 l1_records 中 l1_vec 没有对应记录的行
4. 每 20 条一批调用 NVIDIA Embedding API
5. 插入 l1_vec 表

### Step 4: 配置 TDAI 网关的嵌入服务

在网关启动目录创建 `tdai-gateway.yaml`：

```yaml
memory:
  embedding:
    enabled: true
    provider: "openai_compatible"
    baseUrl: "https://integrate.api.nvidia.com/v1"
    apiKey: "${NVIDIA_API_KEY}"
    model: "nvidia/nv-embedqa-e5-v5"
    dimensions: 1024
```

**重要: 环境变量必须 export 到子进程** —— `.env` 文件通常没加 `export` 前缀，
启动时要加 `set -a && source ~/.hermes/.env && set +a`。

### Step 5: 验证

```bash
curl -X POST http://localhost:8420/search/memories \
  -H 'Content-Type: application/json' \
  -d '{"query":"老缪 南京报业 文旅","limit":5}'
```

预期返回 `strategy: "embedding"` 的结果。

## 关键陷阱

1. **sqlite-vec 扩展加载** — `new DatabaseSync(dbPath, { allowExtension: true })` 是必须的，
   否则 `loadExtension()` 报 "not authorized"。
2. **启动脚本 env 变量** — 在 background terminal 中启动 TDAI 网关时，
   环境变量不会自动传递给子进程。需要使用 `set -a; source ~/.hermes/.env; set +a`。
3. **NVIDIA API 的 `input_type` 参数** — `nv-embedqa-e5-v5` 是 asymmetric 模型，
   必须在每个 embedding 请求中包含 `input_type: "query"`，否则返回 HTTP 400。
4. **NVIDIA API 不支持 `dimensions` 参数** — 该模型固定输出 1024 维，
   请求中不可带 `dimensions` 参数，否则返回 HTTP 400。
5. **TDAI 内置 embedding.ts 需要打补丁** — TDAI 的 `_callApi()` 默认发 `dimensions` 参数，
   且不发送 `input_type`。对 NVIDIA NV-Embed 模型需在 embedding.ts 中额外 patch（已做）。
