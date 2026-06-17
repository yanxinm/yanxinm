# HA 长期访问令牌 — 手动创建（Web UI 不可用时的兜底方案）

## 背景

当无法访问 HA Web UI（无 Funnel、无桌面浏览器）时，需要手动在命令行创建长期访问令牌供 API 使用。

## HA Auth 存储结构

文件：`/config/.storage/auth`（JSON）

```json
{
  "version": 1,
  "key": "<store-level-secret>",
  "data": {
    "users": [...],
    "groups": [...],
    "credentials": [...],
    "refresh_tokens": [...]
  }
}
```

## Refresh Token 必需字段

每个 refresh token 必须包含以下字段才能被 HA 正确加载：

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | UUID string | 令牌 ID，也用作 JWT 的 `iss` claim |
| `user_id` | string | 对应用户 ID（如 yanxinm = `3917a115d3d14f1682a...`） |
| `client_id` | string/null | 客户端 ID，长期令牌通常为 null |
| `client_name` | string/null | 客户端名称（如 "hermes_proxy"） |
| `client_icon` | string/null | 图标，可为 null |
| `token_type` | string | `"long_lived_access_token"` |
| `created_at` | ISO datetime | 如 `"2026-06-09T11:15:00+00:00"` |
| `access_token_expiration` | **number** | ⚠️ 必须为数字（秒），不能为 None！设为 `315360000`（10年） |
| `token` | string | ⚠️ 必须！64 字符 hex（`secrets.token_hex(64)`） |
| `jwt_key` | string | ⚠️ 必须！64 字符 hex（`secrets.token_hex(64)`），用于签发 JWT |
| `expire_at` | number/null | 可为 null |
| `version` | string | HA 版本号，如 `"2026.6.1"` |

## JWT 签发

长期访问令牌是 HS256 签名的 JWT，Payload 必须包含：

```json
{
  "iss": "<refresh_token.id>",
  "iat": <unix_timestamp>,
  "exp": <iat + access_token_expiration_seconds>
}
```

签名密钥 = `refresh_token.jwt_key`（128 字符 hex）。

⚠️ **签名密钥 ≠ auth store 的顶层 `key` 字段**。每个 refresh token 有自己独立的 `jwt_key`，由 `secrets.token_hex(64)` 生成。

## 关键坑：HA 会覆盖手动修改

**HA 启动后会用内存数据覆盖 auth 文件**。正确的操作顺序：

1. `docker stop homeassistant`
2. 修改 `/config/.storage/auth`
3. `docker start homeassistant`

如果 HA 已经在运行中修改了 auth 文件，重启后修改会丢失。

### ⚠️ 更隐蔽的坑：Token 字段格式不匹配导致被静默丢弃

即使按正确顺序操作，如果 new refresh_token 缺少 HA 期望的字段或字段类型不匹配，HA 启动后会**静默删除该 token**（不出现在 refresh_tokens 列表中，JWT 验证返回 401）。

已知导致 token 被丢弃的格式差异：

| 问题 | 错误值 | 正确值 |
|------|--------|--------|
| `access_token_expiration` 类型 | `315360000` (int) | `315360000.0` (float) |
| 缺少 `last_used_at` | 字段不存在 | `null` |
| 缺少 `last_used_ip` | 字段不存在 | `null` |
| 缺少 `credential_id` | 字段不存在 | `null` |

**验证方法**：HA 启动后，检查容器内 auth 文件是否仍含该 token：
```bash
sudo docker exec homeassistant python3 -c "
import json
with open('/config/.storage/auth') as f:
    auth = json.load(f)
names = [rt.get('client_name') for rt in auth['data']['refresh_tokens']]
print('hermes_proxy' in names)
"
```

### ✅ 最可靠的 JWT 生成方式：容器内签发

宿主机的 JWT（ha-gen-token.py 生成）可能因 HA 的 jwt_key 加载时序问题被拒绝。**推荐在容器内签发 JWT**：

```bash
# 容器内生成 JWT 并复制出来
cat > /tmp/gen_jwt.py << 'PYEOF'
import json, jwt, time
with open('/config/.storage/auth') as f:
    auth = json.load(f)
for rt in auth['data']['refresh_tokens']:
    if rt.get('client_name') == 'ha_app':   # 或其他已知有效的 token
        iat = int(time.time())
        exp = iat + int(rt['access_token_expiration'])
        token = jwt.encode({'iss': rt['id'], 'iat': iat, 'exp': exp},
                          rt['jwt_key'], algorithm='HS256')
        with open('/tmp/jwt_out.txt', 'w') as f:
            f.write(token)
        break
PYEOF

sudo docker cp /tmp/gen_jwt.py homeassistant:/tmp/gen_jwt.py
sudo docker exec homeassistant python3 /tmp/gen_jwt.py
sudo docker cp homeassistant:/tmp/jwt_out.txt /home/miao/.ha_token
chmod 600 /home/miao/.ha_token
```

**为什么容器内签发更可靠**：容器内 Python 直接读取 HA 内存中已加载的 auth 数据，jwt_key 保证一致。

## 生成脚本

见同目录 `references/ha-gen-token.py`，在**宿主机**上执行（操作 bind mount 路径 `/home/miao/docker/ha/config/.storage/auth`）：

```bash
# 1. 停止 HA
sudo docker stop homeassistant
# 2. 生成令牌（修改 auth 文件 + 签发 JWT）
sudo python3 ~/.hermes/skills/devops/base-machine-ops/references/ha-gen-token.py
# 3. 启动 HA
sudo docker start homeassistant
sleep 15
# 4. 取出 JWT（脚本同时写到宿主机 bind mount，HA 启动后容器内可读）
cp /home/miao/docker/ha/config/ha_llt_final.txt /home/miao/.ha_token
chmod 600 /home/miao/.ha_token

# 5. 验证令牌（容器内测试）
cat /home/miao/.ha_token  # 确认文件存在
sudo docker exec homeassistant python3 -c "
import urllib.request, json
with open('/config/ha_llt_final.txt') as f:
    token = f.read().strip()
req = urllib.request.Request('http://localhost:8123/api/')
req.add_header('Authorization', 'Bearer ' + token)
resp = urllib.request.urlopen(req)
print(json.loads(resp.read()))  # 应该输出 {'message': 'API running.'}
"
```

## 已知的未解决问题

✅ **2026-06-09 已解决**。手动注入方式在正确的操作顺序下完全可行。要点：
1. **必须先 `docker stop`** 再修改 auth 文件
2. JWT 的 `iss` 必须与 auth 文件中的 refresh_token.id 匹配
3. 若 `iss` 不匹配（跨脚本执行导致 UUID 不同），在容器内重新签发 JWT 即可

## 完整操作流程（已验证通过）

### 方法一：手动注入 auth store（推荐，无需密码）

1. `docker stop homeassistant`
2. 在宿主机上用脚本修改 `/config/.storage/auth`，添加 refresh token + 签发 JWT
3. `docker start homeassistant`
4. 等待 HA 启动（~15s），令牌立即可用

### 方法二：密码重置 + API 创建（需要 API 交互）

1. 在 HA 容器内用 bcrypt 生成密码 hash：`base64.b64encode(bcrypt.hashpw(b'newpass', bcrypt.gensalt(rounds=12)))`
2. 替换 `/config/.storage/auth_provider.homeassistant` 中的密码（⚠️ HA 存储密码是 base64 编码的 bcrypt hash，不是原始 bcrypt 字符串）
3. 重启 HA
4. 通过 `/auth/login_flow` API 登录获取 access token
5. ⚠️ HA 2026.6 没有 REST 接口创建长期令牌——只能通过 WebSocket 命令 `auth/long_lived_access_token`

## HA 2026.6.1 登录 API 变化

`/auth/login_flow` 端点现在要求：
- `handler` 数组至少 2 个元素：`["homeassistant", null]`
- 必须提供 `redirect_uri` 字段
- Step 2 提交凭证时也必须包含 `client_id`

```bash
# Step 1
curl -X POST http://localhost:8123/auth/login_flow \
  -H "Content-Type: application/json" \
  -d '{"client_id":"http://localhost:8123/","handler":["homeassistant",null],"redirect_uri":"http://localhost:8123/"}'

# Step 2（用返回的 flow_id）
curl -X POST "http://localhost:8123/auth/login_flow/{flow_id}" \
  -H "Content-Type: application/json" \
  -d '{"client_id":"http://localhost:8123/","username":"yanxinm","password":"..."}'
```

## 密码重置

HA 的密码存储在 `/config/.storage/auth_provider.homeassistant`，格式为 **base64 编码的 bcrypt hash**（不是原始 bcrypt 字符串！）。

### 正确生成密码 hash

```bash
# 必须在 HA 容器内生成（宿主机的 bcrypt 实现可能与容器不同）
sudo docker exec homeassistant python3 -c "
import bcrypt, base64
raw = bcrypt.hashpw(b'new_password', bcrypt.gensalt(rounds=12))
encoded = base64.b64encode(raw).decode()
print(encoded)  # 形如 JDJiJDEyJE...
"
```

### 错误格式

| 格式 | 是否有效 | 说明 |
|------|----------|------|
| `$2b$12$...` | ❌ | 原始 bcrypt 字符串，HA 解码时 base64 报 Invalid salt |
| `JDJiJDEyJE...` | ✅ | base64 编码的 bcrypt，HA 正确解析 |
