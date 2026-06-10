# Desktop 模型切换与发送失败排查

## 触发场景
- Desktop 显示已连接远程后端，但发送提示词失败。
- Desktop UI 中切换模型失败，而微信/Gateway 仍可正常对话。
- 刚改过 `~/.hermes/config.yaml` 主模型或自定义 provider。

## 关键判断
1. 先区分网络/路由问题与 Desktop 会话/API 问题：
   - `curl http://127.0.0.1:9119/api/status` 应为 `200`。
   - `curl https://<ts-host>/api/status` 应为 `200`。
   - `tailscale serve status` 中 `/` 必须代理到 `http://127.0.0.1:9119`，不要被 HA/其他服务占用。
2. 如果 `/api/status` 正常，但 Desktop 仍失败，优先怀疑：
   - Dashboard 前端/后端版本或残留进程状态不同步。
   - Desktop 没重新加载 9119 根页面，未拿到新的 session token。
   - Desktop/前端调用旧模型接口（如 `/api/models`、`/api/providers`）或未带 token；新接口以 `/api/model/info`、`/api/model/options` 为准。
3. 不要把旧会话里的 provider 超时直接等同于当前主模型不可用；需独立验证当前 provider。

## 安全验证 provider（不泄露 key）
- 用脚本从 config 读取 key，只输出 HTTP 状态、模型名、错误类别，不打印完整 key。
- 验证顺序：
  1. `<base_url>/models`。
  2. `<base_url>/chat/completions` 的最小请求。
  3. `hermes chat -q '只回答 OK' --provider <provider> -m <model>`。

## 修复顺序
```bash
# 1. 停 Dashboard
/home/miao/.hermes/hermes-agent/venv/bin/hermes dashboard --stop || true

# 2. 清残留进程（如果端口未监听但 pgrep 仍有 dashboard）
pkill -f 'hermes dashboard' 2>/dev/null || true

# 3. 用受控后台方式重新启动 9119 Dashboard
/home/miao/.hermes/hermes-agent/venv/bin/hermes dashboard \
  --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build

# 4. 验证
curl -sS -o /tmp/status.json -w '%{http_code}\n' http://127.0.0.1:9119/api/status
curl -sS -o /tmp/info.json -w '%{http_code}\n' http://127.0.0.1:9119/api/model/info
```

> 通过 Hermes `terminal` 工具启动长驻 Dashboard 时，不要用 `nohup ... &`；改用 `terminal(background=true)`，再用独立命令做 readiness checks。

## Desktop 侧收尾
- 完全退出 Desktop 后重新打开，强制重新拉取 9119 根页面和 session token。
- 远程地址填 Dashboard 根地址：`https://<ts-host>` 或 `http://127.0.0.1:9119`。
- 不要把 Desktop 指到 `8642`；那是 Gateway API，不是 Desktop 的 Dashboard 后端。
- 新建会话测试一句短提示，避免旧会话仍带旧 provider/model 状态。
