#!/usr/bin/env python3
"""在 HA Docker 容器内生成长期访问令牌（宿主机版本）

⚠️ 关键：必须在 HA 停止时运行，否则 HA 的延迟保存会覆盖修改！
用法：宿主机上执行（HA 的 /config 目录 bind mount 到 /home/miao/docker/ha/config/）

步骤：
  1. sudo docker stop homeassistant
  2. sudo python3 ha-gen-token.py  # ← 本脚本，在宿主机上跑
  3. sudo docker start homeassistant
  4. sleep 15  # 等待 HA 启动
  5. sudo docker cp homeassistant:/tmp/ha_llt_final.txt /home/miao/.ha_token

JWT 写入容器内 /tmp/ha_llt_final.txt，启动后从容器 cp 出来即可。

注意：
  - 本脚本操作的是宿主机上的 bind mount 路径 /home/miao/docker/ha/config/.storage/auth
  - 容器内运行的脚本版本需改用 /config/.storage/auth 路径
  - 启动 HA 后若 JWT 验证失败（iss 不匹配），在容器内重新签发即可
"""
import json, uuid, time, secrets
import jwt

AUTH_FILE = "/home/miao/docker/ha/config/.storage/auth"
USER_ID = "3917a115d3d14f1682a6ff5dc4c088b8"  # yanxinm

with open(AUTH_FILE) as f:
    auth_data = json.load(f)

# 清理旧的 hermes_proxy tokens
auth_data['data']['refresh_tokens'] = [
    rt for rt in auth_data['data']['refresh_tokens']
    if rt.get('client_name') != 'hermes_proxy'
]

token_id = str(uuid.uuid4())
jwt_key = secrets.token_hex(64)
raw_token = secrets.token_hex(64)

ACCESS_TOKEN_EXPIRATION_SECONDS = 315360000  # 10 年

new_rt = {
    "id": token_id,
    "user_id": USER_ID,
    "client_id": None,
    "client_name": "hermes_proxy",
    "client_icon": None,
    "token_type": "long_lived_access_token",
    "created_at": "2026-06-09T11:30:00+00:00",
    "access_token_expiration": ACCESS_TOKEN_EXPIRATION_SECONDS,
    "token": raw_token,
    "jwt_key": jwt_key,
    "expire_at": None,
    "version": "2026.6.1",
}
auth_data['data']['refresh_tokens'].append(new_rt)

with open(AUTH_FILE, 'w') as f:
    json.dump(auth_data, f, indent=2)

iat = int(time.time())
exp = iat + ACCESS_TOKEN_EXPIRATION_SECONDS
jwt_payload = {"iss": token_id, "iat": iat, "exp": exp}
jwt_token = jwt.encode(jwt_payload, jwt_key, algorithm="HS256")

# 写入宿主机 + 容器 bind mount（启动后容器内 /config/ha_llt_final.txt 可读）
with open('/tmp/ha_llt_final.txt', 'w') as f:
    f.write(jwt_token)
with open('/home/miao/docker/ha/config/ha_llt_final.txt', 'w') as f:
    f.write(jwt_token)

print(f"✅ Token created: {token_id}")
print(f"   JWT: {len(jwt_token)} bytes")
print(f"   Host: /tmp/ha_llt_final.txt")
print(f"   Container: /config/ha_llt_final.txt")
print(f"   Next: sudo docker start homeassistant")
print(f"   Then: cp /home/miao/docker/ha/config/ha_llt_final.txt /home/miao/.ha_token")
