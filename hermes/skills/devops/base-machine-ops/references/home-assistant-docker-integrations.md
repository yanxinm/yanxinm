# Home Assistant on Base Machine — Docker + Integrations Notes

Session-derived notes for HA running on the M710q base machine.

## Current deployment shape

- HA Docker config root: `/home/miao/docker/ha/`
- HA config mount: `/home/miao/docker/ha/config:/config`
- Network mode: `host`
- Web UI/API: `http://100.86.13.11:8123`
- API proxy: `/home/miao/ha_proxy.py`, listens on `0.0.0.0:8080`, injects HA long-lived token from `/home/miao/.ha_token` and forwards to `127.0.0.1:8123`.
- Proxy health check: `curl http://localhost:8080/api/` should return `{"message":"API running."}`.

## Bluetooth in HA Docker

Symptom in HA integration state/logs:

```text
bluetooth setup_retry
Failed to start Bluetooth: [org.freedesktop.DBus.Error.AccessDenied]
An AppArmor policy prevents this sender ... member="AddMatch"
```

Fix used here: run HA container privileged and mount D-Bus.

`docker-compose.yml` service stanza should include:

```yaml
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    network_mode: host
    privileged: true
    restart: unless-stopped
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    environment:
      - TZ=Asia/Shanghai
```

Then recreate/restart from the base terminal (sudo password required):

```bash
cd /home/miao/docker/ha
sudo docker compose down
sudo docker compose up -d
```

Verify:

```bash
curl http://localhost:8080/api/config/config_entries/entry
# bluetooth should be state=loaded
```

## Xiaomi Miot Auto account integration

Flow:

1. HA UI → Settings → Devices & services → Add integration → `Xiaomi Miot Auto`.
2. Select `Add devices using Mi Account (账号集成)`.
3. Use `server_country=cn`, `conn_mode=auto`.
4. If login says password is wrong but credentials are known-good, inspect flow response/logs. Common real error is `need_verify`, not wrong password.

`need_verify` means Xiaomi requires identity verification. The flow returns a verification URL in `description_placeholders.url` / `tip`:

```text
errors.base = need_verify
打开验证网页 | Open the verification page
```

Open that Xiaomi account URL in a browser, complete SMS/security verification, then submit the same account form again. After success, the flow may show `筛选设备`:

- Leave default `Exclude (排除)`.
- Do not select any device if the goal is to include all devices.
- Submit. In exclude mode with nothing checked, all devices are included.

## Midea AC LAN on HA 2026 compatibility

Observed with `midea_ac_lan v0.3.22` on HA 2026.6:

UI error:

```text
无法加载配置向导: {"message":"Invalid handler specified"}
```

HA log reveals old constants removed from `homeassistant.const`, one by one:

```text
cannot import name 'TIME_DAYS' from 'homeassistant.const'
cannot import name 'TIME_HOURS' from 'homeassistant.const'
cannot import name 'TEMP_CELSIUS' from 'homeassistant.const'
cannot import name 'POWER_WATT' from 'homeassistant.const'
```

Patch target:

```text
/home/miao/docker/ha/config/custom_components/midea_ac_lan/midea_devices.py
```

Patch pattern: remove legacy unit constants from the `from homeassistant.const import (...)` block and define compatibility constants before the first Home Assistant component import:

```python
# Compatibility for HA 2026 unit constants removed from homeassistant.const
TIME_DAYS = "d"
TIME_HOURS = "h"
TIME_MINUTES = "min"
TIME_SECONDS = "s"
TEMP_CELSIUS = "°C"
POWER_WATT = "W"
PERCENTAGE = "%"
VOLUME_LITERS = "L"
ENERGY_KILO_WATT_HOUR = "kWh"
CONCENTRATION_MICROGRAMS_PER_CUBIC_METER = "µg/m³"
CONCENTRATION_PARTS_PER_MILLION = "ppm"
```

Then restart HA:

```bash
cd /home/miao/docker/ha
sudo docker compose restart homeassistant
```

After each patch/restart, test the flow and read the next import error from the log until the wizard opens:

```bash
curl -s -X POST http://localhost:8080/api/config/config_entries/flow \
  -H 'Content-Type: application/json' \
  -d '{"handler":"midea_ac_lan"}'

grep -iE 'midea_ac_lan|cannot import|Error occurred loading flow' \
  /home/miao/docker/ha/config/home-assistant.log | tail -40
```

## Operational caveats

- Do not run long-lived services with shell `&` in foreground terminal calls; use Hermes `terminal(background=true)` or a supervised service/cron.
- Some Docker compose lifecycle commands require interactive sudo. If sudo ticket expires, ask the user to run the exact command on the base machine instead of retrying blindly.
- Direct HA `/api/` on `8123` returns `401` without a token; this is normal. Use the proxy on `8080` for token-injected checks.
