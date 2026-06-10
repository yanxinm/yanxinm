# Home Assistant on M710q Docker — session notes

Use this reference when operating the Home Assistant (HA) Docker stack on the base machine.

## Current layout

- Compose directory: `/home/miao/docker/ha/`
- Main config: `/home/miao/docker/ha/docker-compose.yml`
- HA config volume: `/home/miao/docker/ha/config:/config`
- HA container: `homeassistant`
- Network: `host`
- HA UI/API: `http://100.86.13.11:8123`
- API proxy: `/home/miao/ha_proxy.py`, listens on `0.0.0.0:8080`, injects token from `/home/miao/.ha_token`
- HA local user during this session: `yanxinm`; password was reset to `ha2026!`

## Verify HA + proxy

```bash
# HA container state
sudo docker ps --filter name=homeassistant --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'

# HA direct should return 401 if no token is supplied — this is normal
curl -s --connect-timeout 5 http://localhost:8123/api/

# Proxy should inject token and return API running
curl -s --connect-timeout 5 http://localhost:8080/api/
curl -s --connect-timeout 5 http://100.86.13.11:8080/api/

# Config entries summary
curl -s http://localhost:8080/api/config/config_entries/entry > /tmp/ha_entries.json
python3 - <<'PY'
import json
for e in json.load(open('/tmp/ha_entries.json')):
    print(e['state'], e['domain'], e.get('title'), (e.get('reason') or '')[:120])
PY
```

## Bluetooth/AppArmor fix for HA Docker

Symptom in config entries/logs:

- `bluetooth` state `setup_retry`
- reason includes `org.freedesktop.DBus.Error.AccessDenied`
- AppArmor prevents `AddMatch` on D-Bus

Fix used here:

1. In `/home/miao/docker/ha/docker-compose.yml`, under `homeassistant`, add:

```yaml
network_mode: host
privileged: true
restart: unless-stopped
volumes:
  - /home/miao/docker/ha/config:/config
  - /etc/localtime:/etc/localtime:ro
  - /run/dbus:/run/dbus:ro
```

2. Recreate container from the base terminal when sudo is available:

```bash
cd /home/miao/docker/ha
sudo docker compose down
sudo docker compose up -d
```

3. Verify:

```bash
sudo docker inspect homeassistant --format '{{.HostConfig.Privileged}}'  # true
curl -s http://localhost:8080/api/config/config_entries/entry > /tmp/ha_entries.json
```

`bluetooth` should become `loaded`.

## HA long-lived token / proxy pattern

When HA REST access is needed but the browser login is separate:

- Store HA long-lived JWT/token at `/home/miao/.ha_token` with `0600` permissions.
- `ha_proxy.py` reads that file and overwrites inbound `Authorization` with `Bearer <token>`.
- Do not expose token in logs or chat. Use the proxy for routine API checks.

Important implementation detail discovered:

- HA password hashes in `.storage/auth_provider.homeassistant` are `base64(bcrypt_hash)`, not raw bcrypt strings.
- If resetting a local HA password by file, generate bcrypt inside/compatible with HA, base64 encode it, write the encoded value, then restart HA.

Minimal password verification flow is in `/home/miao/debug_ha_login.py` from this session; it tests `/auth/login_flow` using handler `["homeassistant", null]`, `redirect_uri`, and `client_id`.

## Xiaomi Miot login troubleshooting

For `xiaomi_miot` / Xiaomi Miot Auto:

- The plugin version seen here: `1.1.4`.
- Config flow supports two paths:
  - `account`: Mi Account cloud login, recommended for batch import.
  - `token`: one LAN device using host/token.
- Account flow fields observed:
  - `username`
  - `password`
  - `server_country` default `cn`
  - `conn_mode` default `auto`
  - `trans_options` false
  - `filter_models` false

If the user says the Mi account/password is correct but HA reports login failure:

1. Confirm this is the Xiaomi/Mi account form, not the HA local login.
2. Try account formats: phone, `+86` phone, email, Xiaomi ID.
3. Keep `server_country=cn` for mainland Mi Home accounts.
4. Check `description_placeholders.tip` in the config-flow response: the integration may provide an Open verification page URL or captcha, while the HA UI only shows a generic login failure.
5. Search logs for `xiaomi_miot`, `MiCloudNeedVerify`, `captcha`, `AccessDenied`, `cannot_login`.

Useful API probing:

```bash
# Start Xiaomi Miot flow
curl -s -X POST http://localhost:8080/api/config/config_entries/flow \
  -H 'Content-Type: application/json' \
  -d '{"handler":"xiaomi_miot"}'

# Submit first step for account mode with returned flow_id
curl -s -X POST "http://localhost:8080/api/config/config_entries/flow/$FLOW_ID" \
  -H 'Content-Type: application/json' \
  -d '{"action":"account"}'
```

Credential handling preference: ask the user to enter Xiaomi credentials in HA UI, or place them in temporary local files on the base machine; do not ask them to paste passwords into chat unless they explicitly choose to.

## Other custom integrations detected

Installed config flow handlers seen in this HA instance:

- `xiaomi_miot`
- `midea_ac_lan`
- `haier`
- `hon`
- `dreame_vacuum`
- `treeow`
- `treeow_home`

If `midea_ac_lan` appears in `/api/config/config_entries/flow_handlers` but starting the flow returns `Invalid handler specified`, inspect/restart HA and check custom component load errors before assuming the plugin is broken.
