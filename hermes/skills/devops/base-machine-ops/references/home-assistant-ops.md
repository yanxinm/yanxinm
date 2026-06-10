# Home Assistant on the M710q base — integration/debug notes

Use this reference when continuing HA work on the base machine or troubleshooting HA custom integrations.

## Base layout

- HA runs as Docker container `homeassistant` from `/home/miao/docker/ha/docker-compose.yml`.
- Config directory: `/home/miao/docker/ha/config/`.
- Container uses `network_mode: host`; API/UI is on `http://<base-ip>:8123`.
- API proxy lives at `/home/miao/ha_proxy.py` and listens on `0.0.0.0:8080`, injecting `/home/miao/.ha_token` as Bearer token for API calls.
- When using the API proxy, remember it is API-only; use `8123` for HA UI.

## Bluetooth in HA Docker

Symptom in HA integrations: Bluetooth config entry stuck at `setup_retry` with AppArmor/D-Bus access denied, e.g. `org.freedesktop.DBus.Error.AccessDenied ... AddMatch`.

Fix pattern:

```yaml
# /home/miao/docker/ha/docker-compose.yml
services:
  homeassistant:
    network_mode: host
    privileged: true
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
```

Then restart/recreate:

```bash
cd /home/miao/docker/ha
sudo docker compose up -d
# or after edits:
sudo docker compose restart homeassistant
```

Verify:

```bash
curl http://localhost:8080/api/config/config_entries/entry
# bluetooth state should be loaded
```

## Xiaomi Miot flow

- For Xiaomi Miot Auto account integration, choose account mode, server `cn`, connection mode `auto`.
- If login says password/credential failed but credentials are correct, inspect flow output; Xiaomi often returns `need_verify` and a verification URL.
- In `need_verify`, open the Xiaomi verification page, complete the security check, then resubmit in HA. The user may need to use the HA UI because some flows require entering a verification code/ticket.
- Xiaomi Miot caches cloud auth/devices under `/config/.storage/xiaomi_miot/`, e.g. `auth-<uid>-cn.json` and `devices-<uid>-cn.json`. These are useful for auditing what HA actually sees.

## Midea AC LAN on HA 2026

Observed with `midea_ac_lan v0.3.22`: HA 2026 removed old constants from `homeassistant.const`, causing config flow errors such as:

- `cannot import name 'TIME_DAYS'`
- `TIME_HOURS`, `TIME_MINUTES`, `TIME_SECONDS`
- `TEMP_CELSIUS`, `POWER_WATT`, `PERCENTAGE`, `VOLUME_LITERS`, `ENERGY_KILO_WATT_HOUR`, `CONCENTRATION_*`

Patch strategy in `/config/custom_components/midea_ac_lan/midea_devices.py`:

1. Remove those legacy constants from `from homeassistant.const import (...)`.
2. Define local compatibility values before `BinarySensorDeviceClass` import:

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

Server select bug: old form used numeric keys and HA frontend submitted strings, causing `value must be one of [1, 2, 3, 4]`. Patch `/config/custom_components/midea_ac_lan/config_flow.py` login form to use string keys and cast back to `int`:

```python
server = int(user_input[CONF_SERVER])
cloud_name=SERVERS[server]
...
vol.Required(CONF_SERVER, default="2"): vol.In({
    "1": "MSmartHome",
    "2": "美的美居",
    "3": "Midea Air",
    "4": "NetHome Plus",
})
```

LAN discovery notes:

- Midea discovery sends UDP to ports `6445` and `20086`, then connects to device port (often `6444`).
- If automatic discovery says `no_devices`, try directed discovery by IP. A strengthened UDP scan may find devices that the flow misses.
- For a domestic Midea account, server is usually `2` / `美的美居`.
- A device can be discoverable and have `6444` open but still fail local handshake if cloud says `online: false` or model/protocol is unsupported.

## Dreame Vacuum

- `dreame_vacuum` can import-chain into map rendering and require `py_mini_racer`. If `pip install py_mini_racer` hangs or no wheel is available, a temporary stub module can unblock config-flow import only; do not rely on it for map rendering.
- This plugin has two modes:
  - `With map (Automatic)`: Xiaomi Miio cloud path.
  - `Without map (Manual)`: local path requiring `Host` and `Token`.
- If a Dreame robot is not in the Xiaomi/Mijia ecosystem, Xiaomi Miot cloud will not list it even if Mijia shows a third-party platform sync. Use Dreame-specific IP/token extraction instead.
- Miio UDP discovery on `54321` may return nothing for Dreamehome-only devices; then identify IP via router/DHCP or LAN scan, and obtain token from Dreamehome extraction tooling.

## Safety and credential hygiene

For cloud account tests, have the user write temporary files under `/tmp` (e.g. `/tmp/mi_user.txt`, `/tmp/mi_pass.txt`, `/tmp/midea_user.txt`, `/tmp/midea_pass.txt`). Do not print credentials; print masked account and password length only. Delete files from host and container after tests:

```bash
rm -f /tmp/mi_user.txt /tmp/mi_pass.txt /tmp/midea_user.txt /tmp/midea_pass.txt
sudo docker exec homeassistant rm -f /tmp/mi_user.txt /tmp/mi_pass.txt /tmp/midea_user.txt /tmp/midea_pass.txt 2>/dev/null || true
```
