# TDAI Gateway + NVIDIA Embedding API 兼容补丁

## 问题

TDAI 的远程嵌入服务（`src/core/store/embedding.ts` 中的 `_callApi()` 方法）
默认的请求体格式对 NVIDIA NIM 的 `nv-embedqa-e5-v5` 模型不兼容：

| 问题 | 默认行为 | NVIDIA 要求 |
|------|---------|------------|
| `dimensions` 参数 | 发送该参数 | **不支持** — 该模型固定输出 1024 维 |
| `input_type` 参数 | **不发送** | **必须发送** — asymmetric 模型需要区分 query/passage |

## 补丁位置

`~/.memory-tencentdb/node_modules/@tencentdb-agent-memory/memory-tencentdb/src/core/store/embedding.ts`

## 补丁内容

```typescript
// 在 _callApi() 方法中，body 构建之后添加：
const body: Record<string, unknown> = {
  input: texts,
  model: this.model,
  dimensions: this.dims,
  input_type: "query",           // ← 新增：asymmetric 模型必须
};

// NVIDIA nv-embedqa models don't support the 'dimensions' parameter
if (this.model.includes("nv-embedqa") || this.model.includes("nv-embed-v1")) {
  delete body.dimensions;        // ← 新增：NVIDIA 不支持 dimensions 参数
}
```

## 注意事项

- 此补丁位于 node_modules 内，package 升级后需重新打
- 适用于所有 NVIDIA NIM embedding 模型（nv-embedqa-*, nv-embed-v1）
- TDAI Gateway 通过 `tsx/esm` 热加载 TypeScript，修改源码后重启即生效（无需编译）
- 如果改用 OpenAI 或其他 embedding 服务，此补丁不影响（if 条件不命中）

## 配置参考

在 `tdai-gateway.yaml` 中：

```yaml
memory:
  embedding:
    enabled: true
    provider: "openai_compatible"
    baseUrl: "https://integrate.api.nvidia.com/v1"
    apiKey: "${NVIDIA_API_KEY}"
    model: "nvidia/nv-embedqa-e5-v5"
    dimensions: 1024
    maxInputChars: 5000
    timeoutMs: 10000
```
