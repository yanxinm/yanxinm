# aria2c 后台下载 BT 种子注意事项

## 问题

使用 `terminal(background=true)` 运行 aria2c 下载 BT 种子时，`process(action='poll')` 可能泄漏：
1. **非 UTF-8 二进制数据**（tracker 响应中的原始字节）
2. **大量进度行刷屏**（即使加了 `--console-log-level=warn`，aria2c 仍会周期性输出进度条）

## 原因

aria2c 的 stderr 会输出 tracker 原始响应（非 UTF-8），同时 stdout 持续输出进度条。`process poll` 把这些原始字节原样返回。

## 修复

```bash
aria2c --enable-dht=true \
  --bt-tracker="udp://tracker.opentrackr.org:1337/announce,..." \
  "magnet:?xt=urn:btih=..." \
  -d /path/to/download \
  --console-log-level=warn \
  2>/dev/null
```

- `--console-log-level=warn` 过滤掉 debug/info 日志
- `2>/dev/null` 丢弃 stderr 中的二进制垃圾
- **但仍会输出 stdout 进度条**，需容忍

## 注意事项

- 如果种子没有活跃 peer（CN:0 SD:0），aria2c 会一直输出进度行但无下载。这种情况通常是**死种**。
- 长时间 poll 间隔建议 60-120 秒，避免输出堆积。
- **aria2c 进度条中的 ANSI 颜色码**（如 `[#81a27a`）会污染输出，用户不可读。poll 时只取最后一行或过滤 ANSI 码。
- 下载完成后 `process poll` 返回 exit code 0，此时检查目录确认文件。

## 实战记录

### 2026-06-19 乱码泄漏事件

- 第一次尝试：未加 `--console-log-level=warn`，poll 返回数千行非 UTF-8 二进制垃圾
- 第二次尝试：加了 `--console-log-level=warn 2>/dev/null`，仍有大量 ANSI 进度条刷屏
- 教训：aria2c 的 stdout 进度条本身就是大量文本，poll 时必须限制行数或过滤 ANSI 码

### 2026-06-20 连续死种批量判断

- 用户连续发送 6 个磁力链，全部死种（CN:0 SD:0 DL:0B）
- 教训：第 2 个死种时就应告知用户"已确认死种，还有更多吗？"，避免逐一等待
- 优化：连续死种超过 2 个时，主动建议用户换 BT 站重新搜

### 死种判断

- 运行 3 分钟以上 CN:0 SD:0 DL:0B → 死种，终止下载
- 有 peer 但速度 < 100 KiB/s 且 ETA > 100 小时 → 种子极度不活跃，告知用户
- **连续死种优化**：第 2 个死种时应主动告知用户，第 3 个起跳过等待直接判断，避免不必要的 2-3 分钟轮询
