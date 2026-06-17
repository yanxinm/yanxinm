# Dreame 追觅 — 凭据刷新与故障排除

> 适用插件：Tasshack/dreame-vacuum（HACS）
> 测试版本：v2.0.0b23 on HA 2026.6.1

## 凭据过期症状

- HA 中所有 dreame_vacuum 域实体（sensor/switch/button/number/select/vacuum 等）变为 `unavailable`
- HA 日志出现：`ConfigEntryAuthFailed` 或 `Login failed: invalid_user`
- 设备本身在 Dreamehome App 中正常

## 凭据类型

对于 `account_type: "dreame"`（Dreamehome 账号），集成存储两个关键字段：

| 字段 | 存储位置 | 作用 |
|------|---------|------|
| `auth_key` | `config_entry.data.auth_key` | Dreame OAuth refresh_token，626 字符 JWT |
| `token` | `config_entry.data.token` | 设备级 token，dreame 账号类型下通常为空 |

`auth_key` 过期 → 所有云 API 调用返回 401 → 设备不可用。

---

## 方法 A：手动刷新 auth_key（需要密码，无需重装集成）

### 前置条件

- HA 配置存储在 `/home/miao/docker/ha/config/.storage/core.config_entries`
- Dreame 账号密码已知（本环境为 `18651867740`）

### 步骤

1. **读取当前 config entry 数据**

```bash
sudo docker exec homeassistant python3 -c "
import json
with open('/config/.storage/core.config_entries') as f:
    config = json.load(f)
for e in config['data']['entries']:
    if e.get('domain') == 'dreame_vacuum':
        print('username:', e['data']['username'])
        print('auth_key len:', len(e['data'].get('auth_key','')))
"
```

2. **调用 Dreamehome OAuth API 刷新 token**

API 端点解码自 `DREAME_STRINGS`（base64 + zlib），关键端点：

| 索引 | 值 | 含义 |
|------|-----|------|
| [0] | `.iot.dreame.tech` | API 域名后缀 |
| [1] | `13267` | API 端口 |
| [2] | `RAylYC%fmSKp7%Tq` | 密码加盐 |
| [3] | `Dreame_Smarthome/2.1.9 (iPhone; iOS 18.4.1; Scale/3.00)` | User-Agent |
| [5] | `Basic ZHJlYW1lX2FwcHYxOkFQXnZkQHpAU1FZVnhOODg=` | Authorization |
| [17] | `/dreame-auth/oauth/token` | 登录路径 |
| [18] | `access_token` | 响应中的 access_token 字段 |
| [19] | `refresh_token` | 响应中的 refresh_token 字段 |
| [46] | `Dreame-Auth` | API 请求认证头 |
| [50] | `Tenant-Id` | 租户 ID 头 |

**中国区 API 地址**：`https://cn.iot.dreame.tech:13267`

**登录请求头**：
```
User-Agent: Dreame_Smarthome/2.1.9 (iPhone; iOS 18.4.1; Scale/3.00)
Authorization: Basic ZHJlYW1lX2FwcHYxOkFQXnZkQHpAU1FZVnhOODg=
Tenant-Id: 000000
Dreame-Rlc: 1c80b3787b2266776bcdc481f37d8fa42ba10a30af81a6df-1
```

**使用旧 refresh_token 刷新**（优先尝试）：
```
POST /dreame-auth/oauth/token
Body: platform=IOS&scope=all&grant_type=refresh_token&refresh_token={auth_key}
```

**若 refresh 失败，使用密码登录**：
```
POST /dreame-auth/oauth/token
Body: platform=IOS&scope=all&grant_type=password&username=18651867740&password={md5(password+RAylYC%fmSKp7%Tq)}&type=account
```

3. **更新 config entry**

拿到新的 `refresh_token` 后，替换 `config_entry.data.auth_key`：

```bash
sudo cp /home/miao/docker/ha/config/.storage/core.config_entries \
        /home/miao/docker/ha/config/.storage/core.config_entries.bak.$(date +%Y%m%d_%H%M)

# 用 Python 更新 auth_key 字段后写回
# 然后重启 HA
sudo docker restart homeassistant
```

⚠️ **注意**：直接修改 `.storage/core.config_entries` 后需要在 HA 停止状态下写入，或至少备份后操作。

---

## 方法 B：通过 HA Config Flow 重新添加

1. 删除旧 entry：`DELETE /api/config/config_entries/entry/{entry_id}`
2. 创建新 flow：`POST /api/config/config_entries/flow {"handler": "dreame_vacuum"}`
3. 步骤：
   - Step `user`：选 `"Dreamehome Account"`
   - Step `dreame`：填 username + password + country (`cn`)
   - Step `options`：默认即可
   - Step `donation`：`{"donated": false}`

---

## 已知问题：v2.0.0b23 + HA 2026.6.1 设置超时（已解决）

**环境**：HA 2026.6.1 + dreame-vacuum v2.0.0b23 beta

**症状**：Config flow 完成后，集成 setup 阶段报 `CancelledError`，entry 进入 `setup_error` 状态不再重试：

```
coordinator.py:509 → self._device.update()
asyncio.exceptions.CancelledError
```

HA Config Flow API 在 donation 步骤提交后也会超时（30s+）。

**根因**：`update()` 方法中 MQTT 连接到 `bindDomain`（`10000.mt.cn.iot.dreame.tech:19973`）阻塞时间超过 HA 设置超时。MQTT 认证本身正常（uid + access_token 可成功连接），但 paho-mqtt `connect()` 是同步阻塞调用，超时设置不够短。

**绕过方案（已验证有效）**：

1. 手动用 API 获取新 auth_key（方法 A 步骤 2）
2. 直接在 HA 宿主机写入 config entry JSON（绕过 config flow）：
```bash
# 停 HA → 写 config → 起 HA
sudo docker stop homeassistant
# 编辑 /home/miao/docker/ha/config/.storage/core.config_entries
# 新增完整 dreame_vacuum entry（含新 auth_key）
sudo docker start homeassistant
```
3. 启动后 HA 正常加载集成，实体全部恢复

**为什么绕过有效**：HA 启动时的 setup 超时比 config flow 宽松。direct JSON injection 跳过了 HA 的前端 config flow 管道，setup 在后台线程池执行时不会被过早 Cancel。

| 方案 | 结果 |
|------|------|
| Config Flow API | ❌ 超时，entry → setup_error |
| 直接改 JSON + restart | ✅ 成功，242 实体 / 145 可用 |

**注意**：手动写 JSON 后 HA 启动时可能覆盖 auth 文件中的手动修改。如 token 验证失败，用 `docker exec` 在容器内生成 JWT，再 `docker cp` 出来。

---

## 设备在线验证

即使集成不可用，也可通过 API 确认设备在线：

```bash
# 1. 获取 access_token（同上登录流程）
# 2. 查询设备信息
POST https://cn.iot.dreame.tech:13267/dreame-user-iot/iotuserbind/device/info
Headers: Dreame-Auth: {access_token}, Tenant-Id: 000000
Body: {"did": "2123431826"}

# 返回中 property 字段含 "lwt":1 表示设备在线
# bindDomain 为设备 MQTT 中继地址
```
