# AX210NGW Wi-Fi + Bluetooth Kexts for macOS Sequoia

## Kexts Required (4)

| # | Kext | Purpose | Source | Latest** |
|---|------|---------|--------|-----------|
| 1 | **itlwm.kext** | Intel Wi-Fi 6E driver (use with HeliPort) | [OpenIntelWireless/itlwm](https://github.com/OpenIntelWireless/itlwm/releases) | v2.3.0 |
| 2 | **IntelBluetoothFirmware.kext** | AX210 Bluetooth firmware loader | [OpenIntelWireless/IntelBluetoothFirmware](https://github.com/OpenIntelWireless/IntelBluetoothFirmware/releases) | v2.4.0 |
| 3 | **IntelBTPatcher.kext** | Bluetooth patcher | Same as above (included in zip) | v2.4.0 |
| 4 | **BlueToolFixup.kext** | Bluetooth fix for macOS 12+ (Sequoia) | [acidanthera/BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM/releases) | v2.7.2 |

> **Sequoia note:** AirportItlwm.kext does NOT support Sequoia yet (latest is Sonoma 14.4). Use **itlwm.kext** + **HeliPort app** (install HeliPort post-install from [OpenIntelWireless/HeliPort](https://github.com/OpenIntelWireless/HeliPort/releases)).

## config.plist Additions

Add to `Kernel → Add` array (order matters — after NVMeFix, before SMCProcessor):

```xml
<dict>
    <key>BundlePath</key><string>itlwm.kext</string>
    <key>Enabled</key><true/>
    <key>ExecutablePath</key><string>Contents/MacOS/itlwm</string>
    <key>PlistPath</key><string>Contents/Info.plist</string>
</dict>
<dict>
    <key>BundlePath</key><string>IntelBTPatcher.kext</string>
    <key>Enabled</key><true/>
    <key>ExecutablePath</key><string>Contents/MacOS/IntelBTPatcher</string>
    <key>PlistPath</key><string>Contents/Info.plist</string>
</dict>
<dict>
    <key>BundlePath</key><string>IntelBluetoothFirmware.kext</string>
    <key>Enabled</key><true/>
    <key>ExecutablePath</key><string></string>
    <key>PlistPath</key><string>Contents/Info.plist</string>
</dict>
<dict>
    <key>BundlePath</key><string>BlueToolFixup.kext</string>
    <key>Enabled</key><true/>
    <key>ExecutablePath</key><string>Contents/MacOS/BlueToolFixup</string>
    <key>PlistPath</key><string>Contents/Info.plist</string>
</dict>
```

## Full kext load order (M710q EFI example)

```
1.  Lilu.kext
2.  VirtualSMC.kext
3.  WhateverGreen.kext
4.  AppleALC.kext
5.  IntelMausi.kext
6.  NVMeFix.kext
7.  itlwm.kext                    ← WiFi
8.  IntelBTPatcher.kext           ← BT
9.  IntelBluetoothFirmware.kext   ← BT firmware (codeless)
10. BlueToolFixup.kext            ← BT fix
11. SMCProcessor.kext
12. SMCSuperIO.kext
```

## Post-install: HeliPort

After macOS is installed, download [HeliPort.app](https://github.com/OpenIntelWireless/HeliPort/releases) — the GUI client for itlwm.kext. It lives in the menu bar and provides Wi-Fi scanning + connection UI.

Without HeliPort, itlwm.kext loads but has no way to connect to networks (no System Preferences integration).

## Bluetooth Notes

- `IntelBluetoothFirmware.kext` has `ExecutablePath: ""` (empty) — it's a codeless kext that only loads firmware. This is intentional.
- `IntelBTPatcher.kext` MUST load before `IntelBluetoothFirmware.kext`.
- `BlueToolFixup.kext` replaces `IntelBluetoothInjector.kext` (deprecated) on macOS 12+.
- DO NOT include `IntelBluetoothInjector.kext` — it conflicts with BlueToolFixup on Sequoia.

## Download Speed Note (China)

GitHub direct downloads from China are slow (~100 KB/s for 15MB). Files:
- itlwm_v2.3.0_stable.kext.zip: 15MB (~3-5 min on good connection, may timeout)
- IntelBluetooth-v2.4.0.zip: 11MB
- BrcmPatchRAM-2.7.2-RELEASE.zip: 5.4MB

If WSL `wget` times out, download on Windows browser (which has better HTTP connection handling) or use a mirror.
