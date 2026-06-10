# Home Assistant on M710q — session notes and repeatable fixes

## Current deployment shape

- HA runs as Docker container `homeassistant` from `ghcr.io/home-assistant/home-assistant:stable`.
- Compose/config path: `/home/miao/docker/ha/` and `/home/miao/docker/ha/config/`.
- `network_mode: host`.
- Web UI/API port: `8123`.
- Tailscale base IP: `100.86.13.11`.
- API proxy: `/home/miao/ha_proxy.py` listens on `0.0.0.0:8080` and injects a HA long-lived token from `/home/miao/.ha_token` before forwarding to `127.0.0.1:8123`.

## HA API proxy pattern

Use this when scripts need HA API access without manually carrying tokens:

```bash
curl http://localhost:8080/api/
curl http://100.86.13.11:8080/api/
```

Expected response:

```json
{"message":"API running."}
```

Important distinction:

- `8123` = HA web UI and normal login/configuration pages.
- `8080` = API proxy only; not the HA frontend.

## Bluetooth in Docker

Symptom in config entry:

```text
bluetooth state=setup_retry
AppArmor policy prevents D-Bus AddMatch ... Failed to start Bluetooth
```

Hardware may still be fine (`hciconfig` shows hci0 UP). Root cause was container confinement. Fix in compose:

```yaml
services:
  homeassistant:
    network_mode: host
    privileged: true
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
```

Then rebuild container from the base terminal when sudo is available:

```bash
cd /home/miao/docker/ha
sudo docker compose down
sudo docker compose up -d
```

Verify:

```bash
curl -s http://localhost:8080/api/config/config_entries/entry
```

Bluetooth should be `loaded`.

## Xiaomi Miot login debugging

For `xiaomi_miot`, HA form may say login failed even when username/password are correct. Use the config-flow API through the proxy to get the real error. Common durable case:

```json
"errors": {"base": "need_verify"}
```

The response includes `description_placeholders.url`, a Xiaomi identity verification URL. User must open that URL, complete Xiaomi verification, then resubmit the same account/password in the HA Xiaomi Miot form.

Flow start pattern:

```bash
curl -s -X POST http://localhost:8080/api/config/config_entries/flow \
  -H 'Content-Type: application/json' \
  -d '{"handler":"xiaomi_miot"}'
```

Then submit `{"action":"account"}` and finally cloud credentials with:

```json
{
  "username": "...",
  "password": "...",
  "server_country": "cn",
  "conn_mode": "auto",
  "trans_options": false,
  "filter_models": false
}
```

Privacy: do not print credentials. If needed, ask the user to create `/tmp/mi_user.txt` and `/tmp/mi_pass.txt`, verify only byte counts with `wc -c`, and delete after use.

## HA local password note

During this session HA local user `yanxinm` was reset for access/token setup. If relevant, check current auth before assuming a password. Prefer API validation over guessing.
