# apikey.fun 中转站实测记录

> 2026-05-20 实测。中转站地址: https://apikey.fun
> 微信：Laoye1999eth

## 可用模型（2026-05-20）

| 类别 | 模型 |
|------|------|
| 文本 | gpt-5.5, gpt-5.4, gpt-5.4-mini, gpt-5.2, gpt-5.2-pro, gpt-5.2-chat-latest |
| Codex | gpt-5-codex, gpt-5.3-codex, gpt-5.3-codex-spark, apikeyfun-codex/gpt-5.4, apikeyfun-codex/gpt-5.5, codex-auto-review |
| 视觉 | gpt-4o, gpt-4o-mini |
| 图生 | gpt-image-2, gpt-image-1.5, gpt-image-1 |
| 语音 | gpt-4o-audio-preview, gpt-4o-realtime-preview |

共 22 个模型。

## 延迟测试

### 文本对话 (gpt-5.5, "hi"→"ok")

| 请求 | api.apikey.fun | slb.apikey.fun |
|------|---------------|---------------|
| 1（冷启动） | 4.5s | 3.3s |
| 2（热） | 2.2s | 2.4s |
| 3（热） | 1.9s | 2.3s |
| 连续5次平均 | ~3.8s | ~2.7s |

### TCP 延迟
- DNS: 75ms
- TCP: 200-300ms（Cloudflare CDN）
- TTFB: 1-2s

## 功能验证

### 视觉识别 (gpt-4o)
- 图片输入：data URI (base64)
- 准确识别了室内聚餐合影（"一群人在室内聚餐合影，背景有百叶窗和绿植"）
- ✅ 通过

### 图片生成 (gpt-image-2)
- 提示："A cute orange cat sitting on a bookshelf, digital art style"
- 尺寸：1024x1024
- 输出：1.6MB PNG (b64_json)
- 耗时：~90s（比文本慢很多）
- 生成质量：高（细节丰富，风格准确）
- ✅ 通过

## 配置方式

```yaml
# 在 Hermes config.yaml 中
custom_providers:
  - name: apikey-fun
    base_url: https://slb.apikey.fun/v1   # 专线端点
    api_key: sk-xxx
    model: gpt-5.5
```

## 端点对比（v2 2026-05-25 slb 专线 + gpt-image-2）

| 指标 | api.apikey.fun | slb.apikey.fun（专线） |
|------|---------------|----------------------|
| 冷启动（文本） | ~4.5s | **~3.3s** |
| 热请求（文本） | ~2.0s | ~2.4s |
| 平均延迟 | ~2.9s | ~2.7s |
| 波动 | 较大（1.9~6.7s） | **更稳定** |
| gpt-image-2 图生 | ~120s+ | **~69-75s** |

**结论**：slb.apikey.fun 专线冷启动快 1s，图生快 30-50%，波动更小，推荐使用。

## Hermes config 注意事项

```yaml
custom_providers:
  - name: apikey-fun
    base_url: https://slb.apikey.fun/v1   # 推荐用专线
    api_key: <your-key>
    model: gpt-5.5
```

**⚠️ `timeout` 字段不支持**：`custom_providers` 配置项不接受 `timeout` 字段。Hermes 使用 OpenAI Python 客户端的默认超时（600s），远大于 relay 的 ~7s 延迟。如果遇到响应慢，是 relay 本身特性，不是配置问题。
