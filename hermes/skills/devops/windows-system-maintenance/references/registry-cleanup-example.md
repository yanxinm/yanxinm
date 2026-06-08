# Worked Example: AiPy Pro Registry Cleanup

Program: AiPy Pro (ad71d55b-76ce-5f3f-aa1c-b9579100adca)
Publisher: AIPY Team
Install path: D:\AiPyPro
Uninstaller: D:\AiPyPro\Uninstall AiPyPro.exe
Installer file: D:\迅雷下载\aipy-pro-1.1.1-3-x64.exe

## Discovery Phase

Comprehensive search:
```
reg.exe query "HKCU\Software" /s /f "AiPy" 2>&1
reg.exe query "HKLM\Software" /s /f "AiPy" 2>&1
reg.exe query "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall" /s /f "AiPy" 2>&1
reg.exe query "HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall" /s /f "AiPy" 2>&1
```

Result: 22 matches across HKCU and HKLM.

## Found Remnants (by location)

### HKCU — 6 key groups, 3 value-only entries

1. `HKCU\...\AppListBackup\ListOfEventDrivenBackedUpApps_*` (3 subkeys)
2. `HKCU\...\AppListBackup\ListOfEventDrivenBackedUpTiles_*` (1 subkey)
3. `HKCU\...\CloudStore\...\$w~app.aipy.pro` (subkey with $ in name)
4. `HKCU\...\FeatureUsage\AppSwitched` (values: app.aipy, D:\AiPyPro\AiPyPro.exe, D:\迅雷下载\aipy-pro-*.exe)
5. `HKCU\...\Search\JumplistData` (value: app.aipy.pro)
6. `HKCU\...\Start\TileProperties\W~app.aipy.pro` (1 subkey)
7. `HKCU\...\AppCompatFlags\Compatibility Assistant\Store` (values: 3 AiPy-related)
8. `HKCU\Software\Classes\aipy` (URL protocol handler)
9. `HKCU\Software\Classes\aipy-pro` (URL protocol handler)
10. `HKCU\...\MuiCache` (values: FriendlyAppName + ApplicationCompany for 2 paths)

### HKLM — 3 key groups

1. `HKLM\Software\ad71d55b-76ce-5f3f-aa1c-b9579100adca` (GUID key)
2. `HKLM\...\Installer\UserData\S-1-5-18\Products\D06BC6C413B5DFB409B6783B11711188\Features`
3. `HKLM\...\Uninstall\ad71d55b-76ce-5f3f-aa1c-b9579100adca` (uninstall entry)

## Cleanup Steps Executed

### Step 1: HKCU key deletions

```
# AppListBackup — delete each subkey individually (not /va)
reg.exe delete "HKCU\...\AppListBackup\ListOfEventDrivenBackedUpApps_993131920" /f
reg.exe delete "HKCU\...\AppListBackup\ListOfEventDrivenBackedUpApps_993188007" /f
reg.exe delete "HKCU\...\AppListBackup\ListOfEventDrivenBackedUpApps_993488106" /f
reg.exe delete "HKCU\...\AppListBackup\ListOfEventDrivenBackedUpTiles_994997918" /f

# FeatureUsage values
reg.exe delete "HKCU\...\FeatureUsage\AppSwitched" /v "D:\AiPyPro\AiPyPro.exe" /f
reg.exe delete "HKCU\...\FeatureUsage\AppSwitched" /v "app.aipy" /f

# Search JumplistData
reg.exe delete "HKCU\...\Search\JumplistData" /v "app.aipy.pro" /f

# Start TileProperties
reg.exe delete "HKCU\...\Start\TileProperties\W~app.aipy.pro" /f

# AppCompatFlags values
reg.exe delete "HKCU\...\AppCompatFlags\Compatibility Assistant\Store" /v "D:\AiPyPro\AiPyPro.exe" /f
reg.exe delete "HKCU\...\AppCompatFlags\Compatibility Assistant\Store" /v "D:\AiPyPro\Uninstall AiPyPro.exe" /f
reg.exe delete "HKCU\...\AppCompatFlags\Compatibility Assistant\Store" /v "D:\迅雷下载\aipy-pro-1.1.1-3-x64.exe" /f

# URL protocol handlers
reg.exe delete "HKCU\Software\Classes\aipy" /f
reg.exe delete "HKCU\Software\Classes\aipy-pro" /f

# MuiCache values
reg.exe delete "HKCU\...\MuiCache" /v "D:\AiPyPro\AiPyPro.exe.FriendlyAppName" /f
reg.exe delete "HKCU\...\MuiCache" /v "D:\AiPyPro\AiPyPro.exe.ApplicationCompany" /f
reg.exe delete "HKCU\...\MuiCache" /v "D:\迅雷下载\aipy-pro-1.1.1-3-x64.exe.FriendlyAppName" /f
reg.exe delete "HKCU\...\MuiCache" /v "D:\迅雷下载\aipy-pro-1.1.1-3-x64.exe.ApplicationCompany" /f
```

### Step 2: Handle $ in CloudStore key name

`reg.exe` could not delete this key inline because of `$` characters. Used a PowerShell script:

```powershell
# del-cloudstore.ps1
$path = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current\{850e600e-9850-4bf6-bd00-4607d31b9688}$windows.data.apps.appleveltileinfo$appleveltilelist\windows.data.apps.appleveltileinfo$w~app.aipy.pro'
if (Test-Path $path) {
    Remove-Item -Path $path -Recurse -Force
}
```

Run from WSL:
```
powershell.exe -ExecutionPolicy Bypass -File "C:\Users\<user>\Desktop\del-cloudstore.ps1"
```

### Step 3: HKLM key deletions (needed admin)

```
reg.exe delete "HKLM\Software\ad71d55b-76ce-5f3f-aa1c-b9579100adca" /f
reg.exe delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\ad71d55b-76ce-5f3f-aa1c-b9579100adca" /f
```

The Installer\UserData key was not found (already cleaned or never present).

### Step 4: Delete residual folder

```
rmdir /s /q D:\AiPyPro
```

## Verification

```
reg.exe query "HKCU\Software" /s /f "AiPy" 2>&1     # expect 0 matches
reg.exe query "HKCU\Software\Classes" /s /f "aipy" /s 2>&1  # expect 0 matches
```

Exit code 1 with "0 匹配" = clean.
