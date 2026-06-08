# TencentDB Agent Memory (TDAI) 安装与配置指南

## 概述

TencentDB Agent Memory 是一个腾讯开源的4层记忆系统（L0-L3），支持 Hermes Agent 集成。
源码: https://github.com/Tencent/TencentDB-Agent-Memory

## 无 Docker 安装方式（推荐，适用于 WSL）

### 前提
- Node.js >= 22.16
- 已安装 Hermes Agent
- npm 可用（中国网络建议加 registry 镜像）

### 安装步骤

```bash
# 1. 创建目录并安装包
mkdir -p ~/.memory-tencentdb
cd ~/.memory-tencentdb
npm init -y --silent
npm install @tencentdb-agent-memory/memory-tencentdb@latest tsx \
  --registry=https://registry.npmmirror.com

# 2. 创建数据目录
mkdir -p ~/.memory-tencentdb/tdai-memory

# 3. 创建配置文件 ~/.memory-tencentdb/tdai-gateway.yaml
cat > ~/.memory-tencentdb/tdai-gateway.yaml << 'YAMLEOF'
server:
  port: 8420
  host: "127.0.0.1"
llm:
  baseUrl: "https://api.deepseek.com"
  apiKey: "your-api-key-here"
  model: "deepseek-chat"
recall:
  strategy: "keyword"
embedding:
  enabled: false
  provider: "none"
YAMLEOF

# 4. 链接 Hermes 插件
ln -sf ~/.memory-tencentdb/node_modules/@tencentdb-agent-memory/memory-tencentdb/hermes-plugin/memory/memory_tencentdb \
  /home/yanxin/Hermes-Agent/plugins/memory/memory_tencentdb

# 5. 启动 Gateway
cd ~/.memory-tencentdb
node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts

# 6. 验证
curl http://127.0.0.1:8420/health
# 期望: {"status":"ok","version":"0.1.0",...}

# 7. 配置 Hermes 使用该记忆提供者
# 在 ~/.hermes/config.yaml 中设置:
#   memory:
#     provider: memory_tencentdb
# 并在 ~/.hermes/.env 中添加:
#   MEMORY_TENCENTDB_GATEWAY_HOST="127.0.0.1"
#   MEMORY_TENCENTDB_GATEWAY_PORT="8420"

# 8. 重启 Hermes Gateway 生效
```

## 架构说明

```
Hermes Agent (Python) → memory_tencentdb plugin 
  → HTTP → TDAI Gateway (Node.js, :8420)
    → SQLite (本地存储)
    → LLM (DeepSeek, 用于记忆提取)
```

## 记忆层级

| 层级 | 内容 | 触发条件 |
|------|------|----------|
| L0 | 对话原始记录 | 每次对话 |
| L1 | 原子事实提取 | 每N轮对话 |
| L2 | 场景块（Scene） | 定时蒸馏 |
| L3 | 用户画像（Persona） | 每50条新记忆 |

## 向量搜索（Embedding）配置

TDAI 默认关闭嵌入向量搜索（`embedding.provider: none`）。配置远程 embedding API 后，`search/memories` 和 `recall` 端点才能返回结果。

### 配置示例（NVIDIA NIM embedding）

```yaml
# ~/.memory-tencentdb/tdai-gateway.yaml
memory:
  embedding:
    enabled: true
    provider: "openai_compatible"  # 任何 OpenAI 兼容的 embedding 服务
    baseUrl: "https://integrate.api.nvidia.com/v1"
    apiKey: "${NVIDIA_API_KEY}"    # YAML 变量替换，见下文注意事项
    model: "nvidia/nv-embedqa-e5-v5"
    dimensions: 1024               # 必须与模型匹配
    maxInputChars: 5000
    timeoutMs: 10000
  recall:
    strategy: "hybrid"             # embedding + keyword 混合
    maxResults: 10
    scoreThreshold: 0.3
    timeoutMs: 5000
```

### ⚠️ YAML `${VAR}` 环境变量替换陷阱

`tdai-gateway.yaml` 中的 `${VAR}` 语法依赖 `loadGatewayConfig()` 的 `expandEnvVars` 函数。**仅当变量已 export 到进程环境**时才生效。通过 `source ~/.hermes/.env` 加载 `.env` 文件不会 export 变量，因此子进程（node gateway）看不到它们。

**正确方式：**
```bash
cd ~/.memory-tencentdb && \
  set -a && source ~/.hermes/.env && set +a && \
  node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts
```

`set -a` 使后续所有 source 的变量自动 export。不这样做则 `${VAR}` 留空，embedding 降级为 `provider: none`。

**验证 embedding 已启用：**
```bash
curl -s http://localhost:8420/health
# → stores.embeddingService: true  ✅
```

### 验证搜索

配置好 embedding 并导入数据后：
```bash
curl -s -X POST http://localhost:8420/search/memories \
  -H 'Content-Type: application/json' \
  -d '{"query":"测试查询","limit":5}'
# → strategy: "embedding" 而非 "none"
# → results 包含匹配内容或 "No matching memories found"
```

## 批量导入已有记忆（绕过 /seed API）

TDAI 的 `/seed` 端点逐个用 LLM 提取记忆，**2000+ 条会 OOM/超时**（实测每批 50 轮需 3-4 分钟，14 次尝试均被 OOM 杀掉）。改用**直接写入 SQLite + 单独计算向量**：

### 方法：直接插入 l1_records

```javascript
// 关键步骤
const Database = require('better-sqlite3');
const db = new Database(TDAI_DIR + '/vectors.db');

// 1. 直接写入记忆文本
db.prepare(`INSERT OR REPLACE INTO l1_records 
  (record_id, content, type, priority, scene_name, session_key, session_id,
   timestamp_str, timestamp_start, timestamp_end, created_time, updated_time, metadata_json)
  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`).run(...);

// 2. 后续单独计算向量嵌入（见下面"补充计算向量"）
```

这种方式避开了 LLM 提取，直接保留原文内容。2000+ 条在几秒内完成插入。

### ⚠️ NVIDIA nv-embedqa 模型的 TDAI源码补丁

NVIDIA NIM 的 `nv-embedqa-e5-v5` 模型有两个参数约束：

1. **需要 `input_type: "query"`** 参数（非对称模型要求）
2. **不支持 `dimensions` 参数**（输出固定 1024 维，传参返回 HTTP 400）

TDAI 的 `embedding.ts` 默认不传 `input_type` 且总传 `dimensions`。需要做两处补丁：

```typescript
// ~/.memory-tencentdb/node_modules/@tencentdb-agent-memory/memory-tencentdb/src/core/store/embedding.ts

// 第 497-501 行：加入 input_type
const body = {
  input: texts,
  model: this.model,
  dimensions: this.dims,
  input_type: "query",       // ← 新增
};

// 第 502-505 行：跳过不支持的 model
if (this.model.includes("nv-embedqa") || this.model.includes("nv-embed-v1")) {
  delete body.dimensions;    // ← 新增
}
```

TDAI 通过 `tsx/esm` 实时编译 TypeScript，因此修改 `.ts` 源码后重启网关即刻生效。

### 补充计算向量（嵌入）

插入 l1_records 后，嵌入向量需要写入 `l1_vec` 表。使用 `node:sqlite` 加载 `sqlite-vec` 扩展：

```javascript
const { DatabaseSync } = require('node:sqlite');
const path = require('path');
const db = new DatabaseSync(VECTORS_DB, { allowExtension: true });
db.enableLoadExtension(true);

const VEC_SO = path.join(os.homedir(), '.memory-tencentdb', 
  'node_modules', 'sqlite-vec-linux-x64', 'vec0.so');
db.exec(`SELECT load_extension('${VEC_SO}')`);

// 查询无嵌入的记录
const missing = db.prepare(`
  SELECT r.record_id, r.content
  FROM l1_records r LEFT JOIN l1_vec v ON r.record_id = v.record_id
  WHERE v.record_id IS NULL
`).all();

// 分批调用 NVIDIA embedding API（无 transactionSync — node:sqlite 不支持）
const insertVec = db.prepare(
  'INSERT INTO l1_vec (record_id, embedding, updated_time) VALUES (?, ?, ?)');
for (let i = 0; i < missing.length; i += BATCH_SIZE) {
  const batch = missing.slice(i, i + BATCH_SIZE);
  const response = await fetch(EMBED_URL, { ... });
  const data = await response.json();
  data.data.forEach((e, j) => {
    const vec = new Float32Array(e.embedding);
    insertVec.run(batch[j].record_id, vec, new Date().toISOString());
  });
}
```

**完整脚本**见 hermes-agent skill 的 `scripts/tdai-bulk-embed.mjs`（已修复 `{allowExtension: true}` + 无 transactionSync）。

### /seed 方法仍可用于增量导入

小批量（< 50 轮）可直接用 `/seed`。此时 seed 会触发 LLM 提取，产生质量更高的 L1 记忆（带 LLM 总结的场景块）。对于历史数据批量导入，优先用直接 SQLite 方法。

## 注意

- Gateway 端口 8420，与 Hermes 同机运行
- 底层使用 `node:sqlite`（Node 22+ 内置）+ `sqlite-vec` 扩展，非 better-sqlite3
- 验证搜索：`curl -X POST http://localhost:8420/search/memories`
- 向量维度必须与模型匹配（NVIDIA nv-embedqa-e5-v5 = 1024）
