# Dreame Vacuum 凭据刷新流程

> **适用**: 追觅扫地机使用 Dreamehome 云账号时，`auth_key`（refresh_token）过期导致 HA 实体全部不可用。

## 症状

- HA 中 dreame_vacuum 集成的全部实体（100+）状态变为 `unavailable`
- HA 日志：`Login failed: {"error":"invalid_user","error_description":"username or password error"}` 或 `ConfigEntryAuthFailed`
- API 直接测试返回 401

## 修复步骤

### 1. 获取新的 auth_key

通过 Dreamehome OAuth API 刷新（需用户名和密码）：

```python
import json, hashlib, base64, zlib, requests

# 解码集成内置的 API 配置（从 protocol.py 的 DREAME_STRINGS 常量）
DREAME_STRINGS = 'H4sICAAAAAAEAGNsb3VkX3N0cmluZ3MuanNvbgCNU9tuGjEQ/...'  # 完整 base64
strings = json.loads(zlib.decompress(base64.b64decode(DREAME_STRINGS), zlib.MAX_WBITS | 32))
salt = strings[2]  # "RAylYC%fmSKp7%Tq"

# 登录
api_base = f"https://cn{strings[0]}:{strings[1]}"  # cn.iot.dreame.tech:13267
headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    strings[47]: strings[3],  # User-Agent
    strings[49]: strings[5],  # Authorization: Basic
    strings[50]: strings[6],  # Tenant-Id
    strings[48]: strings[4],  # Dreame-Rlc (if cn)
}

pw_hash = hashlib.md5((password + salt).encode('utf-8')).hexdigest()
data = f"{strings[12]}{strings[14]}{username}{strings[15]}{pw_hash}{strings[16]}"
resp = requests.post(f"{api_base}{strings[17]}", headers=headers, data=data, timeout=15)
result = resp.json()

new_auth_key = result[strings[19]]  # refresh_token 即是新的 auth_key
```

也可用已有的 `auth_key` 尝试刷新（更快）：
```python
data = f"{strings[12]}{strings[13]}{old_auth_key}"
resp = requests.post(f"{api_base}{strings[17]}", headers=headers, data=data, timeout=15)
new_auth_key = resp.json()[strings[19]]
```

### 2. 更新 HA 配置

```python
# 读 config
with open('/home/miao/docker/ha/config/.storage/core.config_entries') as f:
    config = json.load(f)

# 更新 dreame_vacuum entry 的 auth_key
for e in config['data']['entries']:
    if e.get('domain') == 'dreame_vacuum':
        e['data']['auth_key'] = new_auth_key

# 写回（需 sudo）
# sudo cp /tmp/new_config.json /home/miao/docker/ha/config/.storage/core.config_entries
```

### 3. 重启 HA

```bash
sudo docker restart homeassistant
```

## 已知问题

- **v2.0.0b23 + HA 2026.6.1**：集成 setup 阶段 MQTT 连接超时导致 `asyncio.exceptions.CancelledError`。绕过方法：直接写 config JSON + restart，不走 HA config flow。
- HA config flow 中的 donation 步骤会触发 setup，此时也可能超时。删除旧 entry 后手动注入配置更可靠。

## 验证

```python
# 查询 dreame 实体
resp = requests.get('http://localhost:8123/api/states', 
    headers={'Authorization': f'Bearer {ha_token}'})
dreame = [e for e in resp.json() if 'chang_gong' in e['entity_id']]
available = [e for e in dreame if e['state'] not in ('unavailable','unknown')]
print(f"可用/总数: {len(available)}/{len(dreame)}")
```

正常情况下 ~145/242 实体可用。房间级别的 select/number 等实体在机器人休眠时保持 `unavailable` 是正常行为。

## HA Token 续期

若 HA long-lived token 过期：

```bash
# 1. 停 HA
sudo docker stop homeassistant
# 2. 生成新 token（需正确的 user_id）
sudo python3 /home/miao/.hermes/skills/devops/base-machine-ops/references/ha-gen-token.py
# 3. 起 HA 并复制 token
sudo docker start homeassistant
sleep 40
sudo docker cp homeassistant:/tmp/ha_llt_final.txt /home/miao/.ha_token
```

⚠️ `ha-gen-token.py` 中的 `USER_ID` 必须匹配 HA 实际用户 ID。可从 auth.bak 或容器内 `/config/.storage/auth` 确认。
