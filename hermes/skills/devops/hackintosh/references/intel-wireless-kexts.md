# AX210 / Intel WiFi+BT Kext Download Guide

## For M710q with AX210NGW (Sequoia)

These are the exact kexts needed for Intel wireless on macOS Sequoia hackintosh:

### Download Links

1. **itlwm.kext (WiFi, 15MB)**
   https://github.com/OpenIntelWireless/itlwm/releases/download/v2.3.0/itlwm_v2.3.0_stable.kext.zip
   → Extract: `itlwm.kext/`

2. **IntelBluetoothFirmware.kext + IntelBTPatcher.kext (Bluetooth, 11MB)**
   https://github.com/OpenIntelWireless/IntelBluetoothFirmware/releases/download/v2.4.0/IntelBluetooth-v2.4.0.zip
   → Extract: `IntelBluetoothFirmware.kext/` and `IntelBTPatcher.kext/`

3. **BlueToolFixup.kext (Bluetooth fix, 5MB)**
   https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.7.2/BrcmPatchRAM-2.7.2-RELEASE.zip
   → Extract: `BlueToolFixup.kext/`

### Placement

All four kexts go into `EFI/OC/Kexts/`:
```
EFI/OC/Kexts/
  itlwm.kext/
    Contents/
      Info.plist
      MacOS/itlwm
  IntelBluetoothFirmware.kext/
    Contents/
      Info.plist
      (no MacOS/ — codeless kext, ExecutablePath="" in config.plist)
  IntelBTPatcher.kext/
    Contents/
      Info.plist
      MacOS/IntelBTPatcher
  BlueToolFixup.kext/
    Contents/
      Info.plist
      MacOS/BlueToolFixup
```

### config.plist Kernel > Add (load order)

Insert after NVMeFix.kext and before SMCProcessor.kext:

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

### Notes

- **Sequoia**: AirportItlwm.kext does NOT support Sequoia. Use itlwm.kext + HeliPort app (install HeliPort after macOS setup)
- **IntelBluetoothFirmware**: The kext is "codeless" — ExecutablePath must be `""` (empty string) in config.plist
- **Download failures**: GitHub direct downloads from China frequently time out on large files (>10MB). The agent cannot reliably download these. Ask the user to download from Windows browser and place kexts manually. In a 2026-06-03 session, agent wget downloads of three files (itlwm 15MB, IntelBT 11MB, BrcmPatchRAM 5MB) all produced 0KB after 2+ minutes. The user completed the downloads via Windows browser in ~10 minutes. **Do not attempt agent-side downloads of kext zips >5MB from mainland China** — prepare the config.plist and directory structure, provide links, and let the user handle the actual file transfer.
