---
name: hackintosh
description: Hackintosh (黑苹果) installation workflow — OpenCore EFI generation for HP/Lenovo mini PCs, macOS installer USB creation on Windows via gibMacOS + manual extraction, and post-install configuration.
triggers:
  - User asks to set up or install 黑苹果/Hackintosh/macOS on a PC
  - User needs to generate or fix an OpenCore EFI for a specific machine
  - User needs to create a macOS installer USB on Windows
  - User references gibMacOS, OpenCore, SMBIOS, ig-platform-id, or EFI partition issues
  - User asks about macOS compatibility for HP EliteDesk/ProDesk or Lenovo ThinkCentre mini PCs
---

# Hackintosh (黑苹果) Installation Workflow

This skill covers end-to-end Hackintosh installation on Intel mini PCs (HP EliteDesk/ProDesk, Lenovo ThinkCentre) using OpenCore, including EFI generation, macOS installer USB creation on Windows, and common pitfalls.

## Prerequisites

- **OpenCore 1.0.7** (current stable)
- **gibMacOS** — macOS installer download tool for Windows ([GitHub](https://github.com/corpnewt/gibMacOS))
- **7-Zip** — for extracting `.pkg` files on Windows
- **Python 3.10+** — for OpenCore Simplify and helper scripts
- USB drive ≥ 16GB (preferably 64GB, USB 3.0)

## Workflow Overview

```
1. Generate OpenCore EFI → 2. Download macOS → 3. Create Installer USB → 4. Install → 5. Post-Install
```

---

## Phase 1: OpenCore EFI Generation

### 1.1 Identify Hardware

Collect these from Windows Device Manager:
- **CPU model** (e.g., i5-9500T)
- **iGPU model** (e.g., UHD 630, HD 530) — MUST be visible as Intel HD Graphics, NOT "Microsoft 基本显示适配器"
- **Storage type** (NVMe SSD model — Samsung PM981/PM991 are INCOMPATIBLE; PM961 is OK)
- **Ethernet chipset** (Intel I219-LM/V is typical for HP)
- **Audio codec** (Realtek ALC235/ALC256 on HP mini PCs)

### 1.2 SMBIOS Selection

| CPU Generation | SMBIOS | Minimum macOS |
|---------------|--------|---------------|
| Skylake (6th gen) | iMac17,1 | Monterey |
| Kaby Lake (7th gen) | iMac18,2 | Monterey |
| Coffee Lake (8th-9th gen) | iMac19,1 | Sequoia |

### 1.3 iGPU Platform IDs

| iGPU | Platform ID | Connector | Notes |
|------|-------------|-----------|-------|
| UHD 630 (Coffee Lake) | `0x3E9B0007` | DP+HDMI | Use for i3-9100T, i5-9500T |
| HD 630 (Kaby Lake) | `0x59120000` | DP+HDMI | Use for i5-7400T, i7-7700T |
| HD 530 (Skylake) | `0x19120000` | DP+HDMI | Use for i5-6600T, i7-6820HQ |

### 1.4 Boot Args

Base: `-v keepsyms=1 debug=0x100`
- Add `alcid=11` for HP audio (ALC235/ALC256)
- Add `alcid=15` for some HP 400 G3 Mini variants
- Remove `-v` after install is confirmed stable

### 1.5 Generation Method

Use **OpCore-Simplify** to generate initial EFI, then manually fix:
1. Replace template SN/MLB with random values (use GenSMBIOS)
2. Correct iGPU platform-id
3. Add framebuffer patches (framebuffer-stolenmem, framebuffer-patch-enable)
4. Enable XhciPortLimit for installation
5. Set SecureBootModel = Disabled

### 1.5.1 OpCore-Simplify 模板修复（关键！）

OpCore-Simplify 生成的 config.plist 存在模板占位符 bug，必须修复后才能用：

| 问题 | 占位符模式 | 修复 |
|------|------|------|
| 序列号占位 | `''' + _serial() + '''` | 生成随机 iMac 格式序列号 |
| MLB 占位 | `''' + _mlb() + '''` | 17位随机字母数字 |
| ROM 占位 | `''' + ..._rom()...'''` | 6字节随机 MAC → base64 |
| UUID XML 损坏 | 缺少 `<key>SystemUUID</key>` | 正则修复完整 XML |
| SMBIOS 错误 | 默认 iMac19,1（仅 CFL 正确） | 按 CPU 代际替换 |

**生成模板序列号时**：格式为 `C02` + 9位字母数字（iMac 系列通用前缀）。
**ROM 值**：`base64.b64encode(os.urandom(6)).decode()` → 8 字符 base64。

### 1.5.2 SMBIOS 生成代码

```python
import uuid, random
serial = 'C02' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=9))
mlb = 'C0293200' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))
sys_uuid = str(uuid.uuid4()).upper()
rom = bytes([random.randint(0x00, 0xFF) for _ in range(6)])
```

### 1.6 Machine Reference Configs

See `references/machine-configs.md` for per-machine EFI details (HP 400 G5 SFF, HP 400 G3 Mini, HP ProDesk 600 G5 DM, Lenovo M710q, HP 400 G3 DM modded).

---

### 1.7 WiFi & Bluetooth (Intel Cards)

Intel wireless cards (AX200/AX201/AX210/AX211, AC 9560/9462) are supported via OpenIntelWireless kexts.

**Sequoia (macOS 15) — CRITICAL**: `AirportItlwm.kext` is **NOT compatible** with Sequoia. Use `itlwm.kext` v2.3.0+ plus HeliPort app instead.

| macOS Version | WiFi kext | BT kexts | Helper app |
|---------------|-----------|----------|------------|
| Ventura/Sonoma (13-14) | AirportItlwm.kext | IntelBluetoothFirmware.kext + BlueToolFixup.kext | None (native AirPort) |
| **Sequoia (15)** | **itlwm.kext** v2.3.0+ | IntelBluetoothFirmware.kext + BlueToolFixup.kext | **HeliPort.app** (menu bar WiFi) |

**Sources**:
- WiFi: [OpenIntelWireless/itlwm](https://github.com/OpenIntelWireless/itlwm/releases)
- BT: [OpenIntelWireless/IntelBluetoothFirmware](https://github.com/OpenIntelWireless/IntelBluetoothFirmware/releases) — use the `IntelBTPatcher.kext` variant for Monterey+
- HeliPort: [OpenIntelWireless/HeliPort](https://github.com/OpenIntelWireless/HeliPort/releases)

**config.plist entries** (add to Kernel → Add, minkernel=23.0.0 for Sequoia):

| kext | BundlePath | ExecutablePath | PlistPath | MinKernel |
|------|-----------|----------------|-----------|-----------|
| itlwm.kext | itlwm.kext | Contents/MacOS/itlwm | Contents/Info.plist | 23.0.0 |
| IntelBluetoothFirmware.kext | IntelBluetoothFirmware.kext | Contents/MacOS/IntelBluetoothFirmware | Contents/Info.plist | 23.0.0 |
| BlueToolFixup.kext | BlueToolFixup.kext | Contents/MacOS/BlueToolFixup | Contents/Info.plist | 23.0.0 |
| IntelBTPatcher.kext | IntelBTPatcher.kext | Contents/MacOS/IntelBTPatcher | Contents/Info.plist | 23.0.0 |

**Post-install**: Copy HeliPort.app to `/Applications/` and set it as a Login Item. It provides a menu bar icon similar to native WiFi. Without it, `itlwm.kext` presents WiFi as an Ethernet interface — functional but non-interactive.

**Note for AX210**: The AX210 (PCI ID 0x2725) works out of the box with `itlwm.kext` v2.3.0. No extra firmware injection needed. Confirmed working on Sequoia 15.x per [perez987/Intel-AX210-on-Sonoma-Sequoia-Tahoe](https://github.com/perez987/Intel-AX210-on-Sonoma-Sequoia-Tahoe).

**Pitfall — AirportItlwm on Sequoia**: If `AirportItlwm.kext` is loaded on Sequoia, it silently fails — no kernel panic but WiFi doesn't appear. Remove it from the EFI and use `itlwm.kext` + HeliPort instead. Do NOT mix both kexts.

**Pitfall — EFI priority**: On 1L mini PCs with both Ethernet (Intel I219-LM, natively supported) and Intel WiFi, Ethernet will work immediately during install. WiFi kexts can be added post-install — no need to hold up the install for WiFi. The USB installer EFI does NOT need to be updated for WiFi; wired Ethernet is sufficient for the macOS installation process.

**config.plist 加载顺序**（放在 NVMeFix 之后、SMCProcessor 之前）：
```
… → NVMeFix → itlwm → IntelBTPatcher → IntelBluetoothFirmware → BlueToolFixup → SMCProcessor → …
```

**注意**：IntelBluetoothFirmware.kext 是 codeless kext，ExecutablePath 留空 `<string></string>`。IntelBluetoothInjector.kext（同包附带）**不需要**——BlueToolFixup 已替代其功能。

---

## Phase 2: macOS Download (Windows)

### 2.1 Using gibMacOS

1. Extract gibMacOS to a **stable drive** (not the target USB) — e.g., `D:\gibMacOS-master\`
2. Run `gibMacOS.bat`
3. Press `R` to toggle Recovery-Only → **Off** (we want full InstallAssistant.pkg)
4. Find the desired macOS version in the list
5. Enter the number to download

Files are saved to: `<gibMacOS>\macOS Downloads\publicrelease\<build> – <version>\`

### 2.2 Known Issues with MakeInstall.bat

**DO NOT use MakeInstall.bat** — it has two major bugs:

1. **Python multiprocessing crash**: `OSError: [Errno 22] Invalid argument: 'F:\\gibMacOS-master\\MakeInstall.py'` — caused by multiprocessing `spawn` incompatibility on some Windows Python installs
2. **200MB EFI-only partition**: After DiskPart clean + GPT conversion, the script only creates a 200MB EFI partition, leaving the rest of the USB unallocated. The subsequent data partition creation fails with `No volume selected`.

**Workaround**: Use manual extraction + diskpart (Phase 3 below).

---

## Phase 3: USB Installer Creation (Windows)

### 🚀 Recommended: GPT + dd Offset Write (One-Shot, No Recovery Needed)

The Etcher → DiskGenius recovery path is a DEAD END. Etcher writes DMG raw with no partition table → DiskGenius can't recognise the APFS volume → no partitions found → must redo. **Skip Etcher entirely for Hackintosh USBs.** GPT + dd offset write creates EFI + APFS in one pass with no recovery step.

> **Deep-dive pitfalls:** See `references/installer-usb-pitfalls.md` for 20+ verified USB creation pitfalls, DiskGenius GUI fallback, and PowerShell raw-write failure modes.

### 3.1 Create GPT Partitions (diskpart)

```cmd
diskpart
select disk N                        ← verify N first with `list disk`
clean
convert gpt
create partition primary size=210
format fs=fat32 quick label=EFI
assign letter=S
create partition primary              ← do NOT format — dd writes here
assign letter=H
select disk N
select partition 2
detail partition                      ← note "字节偏移:" value
exit
```

**dd seek calculation**: `seek = ceiling(byte_offset / 1048576)` — e.g. offset 221,249,536 → seek=211.

### 3.2 dd Write SharedSupport.dmg (PowerShell, Admin)

```powershell
# Run from ADMIN PowerShell!
C:\Users\...\ddrelease64.exe if=D:\...\SharedSupport.dmg of=\\.\PhysicalDriveN bs=1M seek=XXX --progress
```

**Expected output**: `14913+1 records in / 14913+1 records out`. The trailing `"Error reading file: 87 参数错误"` is a known dd-for-Windows bug — the last partial 1M-block write succeeds but the error fires anyway. Verify with `records in == records out`.

### 3.3 Install OpenCore EFI

```powershell
Copy-Item -Path <extracted_EFI>\EFI -Destination S:\ -Recurse -Force
dir S:\EFI\BOOT\BOOTx64.efi
dir S:\EFI\OC\OpenCore.efi
```

**⚠️ CRITICAL: Verify drivers + config.plist BEFORE unplugging.** OpCore-Simplify-generated EFIs are missing:
- `OpenHfsPlus.efi` (or `HfsPlus.efi`) — without it, OpenCore can't read macOS BaseSystem → no "Install macOS" entry in picker
- `OpenCanopy.efi` registration in `UEFI → Drivers` (driver file is present but NOT listed in config.plist)

After copying EFI, run:
```powershell
dir S:\EFI\OC\Drivers
```
Must include at minimum: `OpenCanopy.efi`, `OpenRuntime.efi`, `OpenHfsPlus.efi`. Then verify `config.plist` has all three in `UEFI → Drivers` array. If missing, add them via PowerShell XML edit:
```powershell
$xml = [xml](Get-Content S:\EFI\OC\config.plist -Raw)
$drivers = $xml.SelectSingleNode("//key[text()='Drivers']/following-sibling::array[1]")
# Add missing drivers…
$xml.Save("S:\EFI\OC\config.plist")
```

> **PowerShell XML caveat**: PowerShell's XML parser renames `plist` → `plist` preserves structure. Use `.InnerText` not `.innerText` (case-sensitive).

### 3.4 Legacy: Etcher Method (NOT recommended — Dead End)

If you must use Etcher: Etcher writes DMG raw, leaving no partition table. DiskGenius cannot find the APFS partition via "搜索已丢失分区" even with advanced sector-level search. The only reliable path after Etcher is **重新分区+重写** — you lose nothing by switching to the GPT+dd method above. See pitfall #19 below.

## Phase 4: BIOS Configuration

Before booting the installer:

| Setting | Value |
|---------|-------|
| Secure Boot | **Disabled** |
| VT-d | Disabled (or enable with dart=0 boot arg) |
| CSM / Legacy Boot | **Disabled** (UEFI only) |
| Boot Mode | UEFI |
| XHCI Hand-off | Enabled |
| Serial/COM Port | Disabled |
| Intel Platform Trust | Disabled |
| CFG Lock | Disable if available in BIOS |

### 4.1 Lenovo-Specific BIOS Quirks

Lenovo ThinkCentre BIOS (Chinese UI "联想 BIOS 配置程序") has two traps under **启动菜单 → 兼容模块** (Boot Menu → Compatibility Module) that differ from HP:

| Setting (Chinese) | Default (WRONG) | Required |
|-------------------|-----------------|----------|
| 启动方式 (Boot Mode) | **[自动]** (Auto) | **[仅UEFI]** (UEFI Only) |
| 启动优先级 (Boot Priority) | **[Legacy优先]** (Legacy First) | **[UEFI优先]** (UEFI First) |

**Key**: "Auto" boot mode is a trap — it can silently fall back to Legacy boot even when CSM appears disabled. Must explicitly set to "仅UEFI". Both settings are under the "兼容模块" expandable section, not at the top level of the Boot menu.

The full Lenovo BIOS menu flow:
1. **安全菜单** (Security) → 安全启动 (Secure Boot) → Disabled
2. **启动菜单** (Boot) → 兼容模块 (Compatibility Module) → 启动方式 = 仅UEFI, 启动优先级 = UEFI优先
3. **高级菜单** (Advanced) → VT-d disabled, Serial Port disabled (if present)
4. **设备菜单** (Devices) → XHCI Hand-off enabled (if present)

---

## Phase 5: Post-Install

After macOS boots:
1. Run USB mapping (USBToolBox or Hackintool)
2. Disable XhciPortLimit (remove from config.plist)
3. Remove `-v` from boot-args
4. Generate proper serial numbers if using placeholder values
5. Enable FileVault (optional)

### Post-Install Troubleshooting

| 问题 | 解决 |
|------|------|
| 安装卡 `[EB|#LOG:EXITBS:START]` | Booter→Quirks→DevirtualiseMmio=True |
| 安装卡 `IOConsoleUsers: gIOScreenLock...` | 更换 framebuffer 或加 `-igfxvesa` boot-args |
| 安装后显卡无加速 (Skylake HD 530) | macOS 15 Sequoia 对 HD 530 原生驱动已部分移除，需用 **OCLP 2.4.1+** 打 root patches |
| 声卡没声 | 尝试不同 layout-id（3→11→13→16→28） |
| 关机不断电 | ACPI→Quirks→FadtEnableReset=True |
| USB 3.0 只有 2.0 速度 | XhciPortLimit=True 或用 USBToolBox 定制端口 |

---

## Pitfalls

1. **Samsung NVMe incompatibility**: PM981, PM991, PM9A1 — kernel panics on macOS. Use PM961, WD SN730/SN770, or Crucial P3. Verify model BEFORE generating EFI.
2. **魔改 CPU (modded BIOS)**: i7-6820HQ on G3 DM requires verification that HD 530 iGPU is functional in Windows Device Manager. If only "Microsoft 基本显示适配器" shows, macOS won't have graphics acceleration.
3. **gibMacOS MakeInstall.bat**: Never rely on it for USB creation. Always use manual extraction + external flashing tool.
4. **DiskPart from WSL**: Must use temp files (not pipes). Must `cd /d C:\` first. See `windows-system-maintenance` skill for full pattern.
5. **7-Zip command not found**: Install 7-Zip from 7-zip.org first. The standalone \`7za.exe\` download is a zip that itself requires 7-Zip to extract.
6. **WSL cannot see removable drives**: `/mnt/f/` may be empty. Use Windows-side tools (cmd/PowerShell) for USB operations. WSL `lsblk` won't show the USB drive.
7. **EFI partition size**: OpenCore EFI folder is ~50MB. The default 200MB EFI partition is plenty of space.

8. **Etcher DMG write = DEAD END for Hackintosh USB** — Etcher writes DMG raw with NO partition table. DiskGenius "搜索已丢失分区" (even advanced sector-level) CANNOT find the APFS partition — returns "没有搜索到任何分区." The only fix is to re-partition and re-write. **Use GPT + dd offset write instead** (Phase 3.1–3.3) — it creates EFI + APFS in one pass with no recovery needed.

9. **USB disk number shifts on re-plug** — After unplug/re-plug, the USB may get a different disk number (e.g., Disk 1 → Disk 3) and drive letters. Always verify with `list disk` or `Get-Disk` before diskpart commands.

10. **Terminal clarity: CMD vs PowerShell** — diskpart runs inside CMD (command prompt, the black-background window). PowerShell's blue-background window cannot run diskpart interactively. When the user is told to run diskpart, they need CMD (Administrator), not PowerShell.

11. **CRITICAL: `format` after failed `create partition` destroys DMG** — After `shrink`, if `create partition primary` fails ("找不到可用范围") but `format fs=fat32` and `assign` are run anyway, diskpart formats the existing APFS partition (with macOS installer data) as FAT32. Prevention: always `rescan` after `shrink`, and if `create partition primary` fails, STOP immediately. Recovery: re-flash with Etcher.

12. **USB thermal throttling** — Sustained writes cause USB drives to heat up and drop from ~47 MB/s to <1 MB/s. Cancel, unplug for 5 min to cool, plug into rear USB 3.0 (blue) port, re-flash. Etcher overwrites the whole disk — no `clean` needed before re-flashing.

13. **diskpart `create partition primary` fails even after `shrink + rescan`** — Verified on Windows 10.0.26220: the freed 210MB at the APFS partition tail is not recognized as available for new partitions. **Fallback:** Use DiskGenius (free) or MiniTool Partition Wizard (GUI) to create the FAT32 EFI partition. These GUI tools correctly handle shrink-then-create on APFS volumes.

15. **Samsung PM961 Trim issue** — PM961 is an early Samsung NVMe. On macOS, SetApfsTrimTimeout to `-1` disables Trim to prevent I/O timeouts. Unlike PM981/PM991, PM961 is compatible but needs this config.plist fix.

16. **Lenovo M710q BIOS + MBR USB 不可用 → 必须 GPT** — MBR U 盘在仅UEFI模式下F12不显示。即使改「自动+Legacy优先」能进 F12 菜单，MBR 没有 Legacy 引导扇区，链到 PXE 网络启动报错（PXE-E61 Intel Boot Agent）。**结论：Lenovo M710q 强制要求 GPT U 盘**。用 diskpart 先 `convert gpt` 建分区，再 `dd seek=offset` 偏移写入 SharedSupport.dmg（Phase 3.1–3.2）。\n\n17. **ghproxy.net 文件大小限制** — ghproxy.net 自动截断 >3-5MB 的文件（如 OpenCore 10MB 常截到 ~3-4MB），表现为下载完成但 `zipfile.is_zipfile()` 返回 False。jsDelivr CDN 也不工作。**已验证有效链**：直连 GitHub + `curl --connect-timeout 30 --max-time 360`。

18. **Samsung Lenovo OEM 盘型号识别** — Lenovo 定制机上的 Samsung SSD 使用非标准型号（如 `M2ULW256GHEHP`，不以 `MZ-` 开头），无法通过常规搜索引擎查到规格。识别技巧：在 BIOS 启动菜单 (F12) 中，NVMe 盘通常显示为 `NVMe: SAMSUNG ...`，SATA M.2 盘只显示 `M.2 Drive 1: SAMSUNG ...`（无 NVMe 前缀）。SATA M.2 盘（如 PM871a 家族）黑苹果兼容性良好，不在问题名单中。不确定时以实际引导测试为准——macOS 安装器能识别磁盘则兼容。

19. **OpenCore 菜单没有 "Install macOS Sequoia" → 缺 HFS+ 驱动** — OpenCore 选择器只显示 EFI/Windows/ResetNVRAM，但无安装器选项。原因：EFI 缺 `OpenHfsPlus.efi`（或 `HfsPlus.efi`），macOS BaseSystem 是 HFS+ 格式，无此驱动则读不到。OpCore-Simplify 生成的 EFI 默认不含此文件（HfsPlus 是闭源 Apple 驱动，OpenHfsPlus 是开源替代）。从 OpenCore 官方包 `X64/EFI/OC/Drivers/OpenHfsPlus.efi` 拷到 `S:\EFI\OC\Drivers\`，并加到 `config.plist` 的 `UEFI → Drivers` 数组。

20. **OpenCanopy.efi 文件在但菜单不显示 → config.plist 未注册** — OpCore-Simplify 生成的 `config.plist` 的 `UEFI → Drivers` 数组通常只含 `OpenRuntime.efi`，不含 `OpenCanopy.efi` 和 `OpenHfsPlus.efi`。三个驱动都必须同时存在于文件系统和 config.plist 中。PowerShell XML 编辑 config.plist 时注意 XPath 区分大小写（`.InnerText` 不是 `.innerText`），用 `//key[text()='Drivers']/following-sibling::array[1]` 定位。

21. **USB disk number 会变** — 拔插 U 盘后 disk number 可能偏移（如 Disk 1 → Disk 3，空读卡器占用低编号）。每次 diskpart 操作前必须 `list disk` 确认。`clean` 失败报"设备中没有介质"通常是选中了空读卡器槽。\n\n19. **DiskGenius 搜索丢失分区对 Etcher DMG 无效** — Etcher 把 SharedSupport.dmg 裸写到扇区 0 后，磁盘没有分区表结构，DiskGenius 的"搜索已丢失分区"功能（无论按柱面还是按扇区）都无法找到任何分区。不要浪费时间反复尝试扫描。正确路线：用 **GPT + dd 偏移写入**（见 Phase 3.3 Method C）。\n\n20. **Etcher 写盘后 diskpart clean 报"无介质"** — Etcher 写入 DMG 后，Windows 可能将 U 盘识别为"无介质"状态（`list disk` 显示 0 B）。解决：拔掉 U 盘等待 5 秒重新插入，Windows 重新识别后 `list disk` 正常显示容量。但重新插入后磁盘号可能变化（如 Disk 1 → Disk 3），执行 diskpart 前务必用 `list disk` 确认当前编号。\n\n21. **GPT + dd 偏移写入：Lenovo 推荐方案** — 避开 Etcher 无分区表 + DiskGenius 扫不到的死循环。

22. **dd for Windows "Error 87 参数错误" is benign** — 当 DMG 文件大小不是 1MB 的整数倍时，ddrelease64.exe 在最后一个分块会报 `Error reading file: 87 参数错误`。关键是检查 records 计数：如果 `records in` = `records out`（如 `14913+1 records in / 14913+1 records out`），写入成功，报错可忽略。如果 `records out` 明显少于 `records in`，写入不完整，检查磁盘空间或物理坏道。流程：diskpart `clean` → `convert gpt` → 建 210MB FAT32 EFI 分区(S:) → 建剩余空间分区(H:) → `detail partition` 记下偏移量 → `ddrelease64.exe if=SharedSupport.dmg of=\\.\PhysicalDriveN bs=1M seek=XXX`（seek = 偏移字节 ÷ 1048576 取整）→ 复制 OpenCore EFI 到 S:。一次性搞定，无需 Etcher 或 DiskGenius。\n\n---

## References

- `references/machine-configs.md` — Per-machine EFI configuration details (SMBIOS, platform-id, boot-args, storage)
- `references/installer-usb-manual.md` — Full manual USB creation transcript (gibMacOS download → 7z extract → write)
- Cross-reference: `windows-system-maintenance` skill for diskpart-from-WSL patterns
