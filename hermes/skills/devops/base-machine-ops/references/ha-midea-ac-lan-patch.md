# Midea AC LAN (v0.3.22) HA 2026 Compatibility Patch

## Problem

`midea_ac_lan v0.3.22` fails to load config flow on HA 2026.6+:

```
cannot import name 'TIME_DAYS' from 'homeassistant.const'
```

HA 2026 removed many legacy unit constants from `homeassistant.const`.

## Files to Patch

| File | Path |
|------|------|
| midea_devices.py | /home/miao/docker/ha/config/custom_components/midea_ac_lan/midea_devices.py |
| config_flow.py | /home/miao/docker/ha/config/custom_components/midea_ac_lan/config_flow.py |

## Patch 1: Removed Constants (midea_devices.py)

Remove these from `from homeassistant.const import (...)` block:

TIME_DAYS, TIME_HOURS, TIME_MINUTES, TIME_SECONDS, TEMP_CELSIUS, POWER_WATT, PERCENTAGE, VOLUME_LITERS, ENERGY_KILO_WATT_HOUR, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION

Add local definitions before first file-level usage:

```python
TIME_DAYS = "d"; TIME_HOURS = "h"; TIME_MINUTES = "min"; TIME_SECONDS = "s"
TEMP_CELSIUS = "°C"; POWER_WATT = "W"; PERCENTAGE = "%"
VOLUME_LITERS = "L"; ENERGY_KILO_WATT_HOUR = "kWh"
CONCENTRATION_MICROGRAMS_PER_CUBIC_METER = "µg/m³"
CONCENTRATION_PARTS_PER_MILLION = "ppm"
```

## Patch 2: Server Select Bug (config_flow.py)

Schema `vol.In(SERVERS)` uses int keys but HA 2026 frontend submits strings.

Fix: In async_step_login, cast `server = int(user_input[CONF_SERVER])`. Change schema to string keys with default "2".

## Apply

```bash
cd /home/miao/docker/ha && sudo docker compose restart homeassistant
```
