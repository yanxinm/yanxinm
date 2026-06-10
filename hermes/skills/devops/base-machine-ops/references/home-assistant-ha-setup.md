# Home Assistant on M710q — setup/troubleshooting notes

Use for HA Docker on 老缪的基地 and smart-home integrations.

## Known deployment
- HA Docker config: `/home/miao/docker/ha/config/`
- Compose: `/home/miao/docker/ha/docker-compose.yml`, `network_mode: host`, `restart: unless-stopped`
- Use `privileged: true` when Bluetooth integration fails with AppArmor/D-Bus `AddMatch` denied.
- HA local account: `yanxinm`; current local password may be stored in memory, do not expose in chat.
- API proxy: `/home/miao/ha_proxy.py`, reads `/home/miao/.ha_token`, listens `0.0.0.0:8080`, forwards to `127.0.0.1:8123`, injects `Authorization: Bearer ...`, enables CORS.
- Tailscale API check: `curl http://100.86.13.11:8080/api/` should return `{"message":"API running."}`.

## Creating/validating a HA long-lived token
Preferred: use HA auth API if local login works. For HA 2026 login flow:
1. `POST /auth/login_flow` with `{"client_id":"http://localhost:8123/","handler":["homeassistant", null],"redirect_uri":"http://localhost:8123/"}`.
2. `POST /auth/login_flow/<flow_id>` with `client_id`, `username`, `password`.
3. `POST /auth/token` with `grant_type=authorization_code`, `code`, `client_id`.
4. Long-lived token creation is websocket-only in HA 2026; if REST `/auth/long_lived_access_token` 404s, use UI or internal auth store carefully.

If resetting the HA password manually, `auth_provider.homeassistant` stores **base64(bcrypt_hash)**, not raw bcrypt.

## Bluetooth fix
Symptom: Bluetooth config entry `setup_retry`, reason includes AppArmor/D-Bus `AccessDenied` on `org.freedesktop.DBus AddMatch`.
Fix:
```yaml
services:
  homeassistant:
    network_mode: host
    privileged: true
    volumes:
      - /run/dbus:/run/dbus:ro
```
Then `sudo docker compose down && sudo docker compose up -d`.

## Xiaomi Miot
- Add via `Xiaomi Miot` -> `Add devices using Mi Account`.
- If account/password are correct but login fails, inspect API response/logs; common real error is `need_verify` with `description_placeholders.url` for Xiaomi identity verification.
- After user opens verification URL and completes it, resubmit. In Exclude filter mode, selecting no devices means include all devices.

## Midea AC LAN on HA 2026
Installed plugin observed: `midea_ac_lan v0.3.22`. It is old and needs compatibility patches for HA 2026.

### Config flow import failures
Symptoms: HA UI says `Invalid handler specified`; logs show imports from `homeassistant.const` failing.
Patch `/home/miao/docker/ha/config/custom_components/midea_ac_lan/midea_devices.py`:
- Remove imports of legacy constants: `TIME_DAYS`, `TIME_HOURS`, `TIME_MINUTES`, `TIME_SECONDS`, `TEMP_CELSIUS`, `POWER_WATT`, `PERCENTAGE`, `VOLUME_LITERS`, `ENERGY_KILO_WATT_HOUR`, `CONCENTRATION_MICROGRAMS_PER_CUBIC_METER`, `CONCENTRATION_PARTS_PER_MILLION`.
- Add before first HA component import:
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
Restart HA and test config flow via `/api/config/config_entries/flow`.

### Server select validation bug
Symptom on login form: `value must be one of [1, 2, 3, 4]` even when selecting 美的美居.
Patch `/home/miao/docker/ha/config/custom_components/midea_ac_lan/config_flow.py`:
- Convert selected `server` to int before indexing `SERVERS`.
- Change schema from numeric keys to string keys, default `"2"`:
```python
vol.Required(CONF_SERVER, default="2"): vol.In({
    "1": "MSmartHome",
    "2": "美的美居",
    "3": "Midea Air",
    "4": "NetHome Plus",
})
```

### Discovery notes
- Built-in `auto` discovery can miss devices. Midea discovery sends UDP to port `6445` and `20086`; devices may expose TCP `6444` for control.
- Base network seen: `192.168.1.0/24`; base IP often `192.168.1.42`.
- In this session, strengthened scan found:
  - `192.168.1.10` responding as `Microwave Steam Oven`, device id `210006738498579`, TCP `6444` open.
  - `192.168.1.7` responded but old parser threw `IndexError: bytearray index out of range` in `discover.py`, likely another Midea device (possibly water purifier).
- For `192.168.1.10`, Midea AC LAN requires 美的美居 account login to fetch device key. If UI reports connection failure, check logs for Midea cloud DNS/API errors such as `mp-prod.appsmb.com` DNS no data, then retry when DNS resolves.

## Secret hygiene
When asking user to provide third-party credentials for API testing, prefer temporary files under `/tmp` and delete after use. Never print or repeat passwords; warn user when screenshots expose visible passwords.
