# Machine EFI Configuration Reference

Last updated: 2026-05-31 | OpenCore 1.0.7

---

## HP ProDesk 600 G5 DM (i5-9500T) — PRIMARY 24×7 Hermes Machine

| Component | Detail |
|-----------|--------|
| CPU | Intel Core i5-9500T (Coffee Lake, 6C/6T, 2.2-3.7GHz) |
| iGPU | Intel UHD 630 |
| RAM | TBD |
| Storage | Samsung PM961 256GB NVMe ✅ (system) + optional 2.5" SATA. ⚠️ 3.5" drives do NOT fit. |
| Ethernet | Intel I219-LM (native macOS support) |
| WiFi (planned) | Intel AX210NGW (M.2 E-key) — see WiFi note below |
| Audio | Realtek ALC235 |
| SMBIOS | **iMac19,1** |
| iGPU platform-id | `0x3E9B0007` |
| boot-args | `-v keepsyms=1 debug=0x100 alcid=11` |

EFI: `HP600G5_DM_EFI.zip` (copied from G5 SFF base, adjusted for Coffee Lake)

**WiFi (Intel AX210NGW)**: Requires `itlwm.kext` v2.3.0 + HeliPort.app on Sequoia (AirportItlwm not compatible). Bluetooth: `IntelBluetoothFirmware.kext` + `BlueToolFixup.kext` + `IntelBTPatcher.kext`. Ethernet works during install — WiFi kexts can be added post-install. See SKILL.md §1.7 for full config.plist entries.

---

## HP 400 G5 SFF (i3-9100T) — TEST MACHINE

| Component | Detail |
|-----------|--------|
| CPU | Intel Core i3-9100T (Coffee Lake, 4C/4T, 3.1-3.7GHz) |
| iGPU | Intel UHD 630 |
| RAM | 8GB DDR4 |
| Storage | 512GB SSD (model TBD) |
| SMBIOS | **iMac19,1** |
| iGPU platform-id | `0x3E9B0007` |
| boot-args | `-v keepsyms=1 debug=0x100 alcid=11` |
| framebuffer | framebuffer-stolenmem, framebuffer-patch-enable |

EFI: `HP400G5_EFI_FIXED.zip`
Fixes from OpCore-Simplify output: SN/MLB template → real values, platform-id corrected from `0x983E0003` to `0x3E9B0007`, XhciPortLimit enabled.

---

## HP 400 G3 Mini (i5-7400T)

| Component | Detail |
|-----------|--------|
| CPU | Intel Core i5-7400T (Kaby Lake, 4C/4T, 2.4-3.0GHz) |
| iGPU | Intel HD 630 |
| RAM | 16GB DDR4 |
| Storage | PCIe-8 SSD 1TB (compatible, non-Samsung) |
| SMBIOS | **iMac18,2** |
| iGPU platform-id | `0x59120000` |
| boot-args | `-v keepsyms=1 debug=0x100 alcid=15` |

EFI: `HP400G3_Mini_EFI.zip` — random SN/MLB, platform-id `0x59120000`.

---

## Lenovo M710q (i5-6600T)

| Component | Detail |
|-----------|--------|
| CPU | Intel Core i5-6600T (Skylake, 4C/4T, 2.7-3.5GHz) |
| iGPU | Intel HD 530 |
| RAM | 16GB Crucial DDR4 |
| Storage | Samsung M2ULW256GHEHP 256GB (Lenovo OEM, SATA M.2, PM871a family, compatible ✅) |
| SMBIOS | **iMac17,1** |
| iGPU platform-id | `0x19120000` |
| boot-args | `-v keepsyms=1 debug=0x100 alcid=11` |

EFI: `M710q_EFI_complete.zip` — SATA M.2 (Samsung OEM, compatible ✅), platform-id `0x19120000`, 12 kexts including AX210 WiFi/BT.
**USB**: GPT partition table required (MBR won't show in F12 on UEFI Only). Use diskpart `convert gpt` + `dd seek=offset` write (not Etcher — see Phase 3.1–3.2 in SKILL.md).
**Drivers**: Must include `OpenCanopy.efi` + `OpenHfsPlus.efi` + `OpenRuntime.efi` in both `S:\EFI\OC\Drivers\` AND `config.plist UEFI → Drivers` array. Without OpenHfsPlus, "Install macOS Sequoia" won't appear in picker.

---

## HP 400 G3 DM 魔改 (i7-6820HQ) — BLOCKED

| Component | Detail |
|-----------|--------|
| CPU | Intel Core i7-6820HQ (Skylake-H, 4C/8T, 2.7-3.6GHz) — **modded BIOS** |
| iGPU | Intel HD 530 — **STATUS UNKNOWN** (must verify in Windows Device Manager) |
| RAM | 8GB planned |
| Storage | Samsung PM961 256GB NVMe ✅ |
| SMBIOS | **iMac17,1** (tentative) |
| iGPU platform-id | `0x19120000` (tentative) |

**BLOCKER**: If Windows Device Manager shows only "Microsoft 基本显示适配器" instead of "Intel HD Graphics 530", the iGPU is dead after the mod. In that case, macOS won't have graphics acceleration. Do NOT generate EFI until confirmed.

EFI: **Not yet generated** — waiting for iGPU confirmation screenshot.
