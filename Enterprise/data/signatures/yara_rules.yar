# YARA Rules for Advanced Malware Detection
# Format: Standard YARA rule syntax

rule WannaCry_Ransomware {
    meta:
        description = "Detects WannaCry ransomware variants"
        author = "CyberDefense AI"
        severity = 10
        family = "Ransomware"
        
    strings:
        $s1 = "tasksche.exe" ascii wide
        $s2 = "Global\\MsWinZonesCacheCounterMutexA" ascii wide
        $s3 = "WNcry@2ol7" ascii wide
        $s4 = ".WNCRY" ascii wide
        $hex1 = { 4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00 }
        
    condition:
        uint16(0) == 0x5A4D and 2 of ($s*) or $hex1
}

rule Emotet_Banking_Trojan {
    meta:
        description = "Detects Emotet banking trojan"
        author = "CyberDefense AI"
        severity = 9
        family = "Banking Trojan"
        
    strings:
        $s1 = "moduleconfig" ascii
        $s2 = "/wp-admin/" ascii
        $s3 = "Content-Type: multipart/form-data" ascii
        $hex1 = { E8 ?? ?? ?? ?? 58 83 E8 05 }
        
    condition:
        uint16(0) == 0x5A4D and 2 of them
}

rule Zeus_Banking_Trojan {
    meta:
        description = "Detects Zeus banking trojan variants"
        author = "CyberDefense AI"
        severity = 9
        family = "Banking Trojan"
        
    strings:
        $s1 = "ntos.exe" ascii
        $s2 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" ascii
        $s3 = "winlogon.exe" ascii
        $hex1 = { 55 8B EC 51 53 8B 5D 08 83 65 FC 00 }
        
    condition:
        uint16(0) == 0x5A4D and 2 of them
}

rule Cobalt_Strike_Beacon {
    meta:
        description = "Detects Cobalt Strike beacon payloads"
        author = "CyberDefense AI"
        severity = 9
        family = "Backdoor"
        
    strings:
        $s1 = "beacon.dll" ascii wide
        $s2 = "rundll32.exe" ascii wide
        $hex1 = { FC 48 83 E4 F0 E8 C8 00 00 00 }
        $hex2 = { 4D 5A 41 52 55 48 89 E5 48 81 EC 20 00 00 00 }
        
    condition:
        uint16(0) == 0x5A4D and any of them
}

rule XMRig_Cryptocurrency_Miner {
    meta:
        description = "Detects XMRig cryptocurrency miners"
        author = "CyberDefense AI"
        severity = 7
        family = "Cryptominer"
        
    strings:
        $s1 = "xmrig.exe" ascii wide
        $s2 = "cryptonight" ascii
        $s3 = "stratum+tcp" ascii
        $s4 = "donate-level" ascii
        $s5 = "RandomX" ascii
        
    condition:
        2 of them
}

rule Generic_Ransomware {
    meta:
        description = "Generic ransomware detection"
        author = "CyberDefense AI"
        severity = 10
        family = "Ransomware"
        
    strings:
        $s1 = "Your files are encrypted" ascii wide nocase
        $s2 = "pay the ransom" ascii wide nocase
        $s3 = "bitcoin" ascii wide nocase
        $s4 = "decrypt" ascii wide nocase
        $s5 = "HOW_TO_RESTORE" ascii wide
        $s6 = "RESTORE_FILES" ascii wide
        $ext1 = ".locked" ascii
        $ext2 = ".encrypted" ascii
        $ext3 = ".crypt" ascii
        
    condition:
        2 of ($s*) or any of ($ext*)
}

rule PowerShell_Malware {
    meta:
        description = "Detects malicious PowerShell scripts"
        author = "CyberDefense AI"
        severity = 8
        family = "Fileless Malware"
        
    strings:
        $s1 = "IEX (New-Object Net.WebClient).DownloadString" ascii wide
        $s2 = "powershell -WindowStyle Hidden" ascii wide
        $s3 = "bypass -enc" ascii wide
        $s4 = "[System.Convert]::FromBase64String" ascii wide
        $s5 = "Invoke-Expression" ascii wide
        
    condition:
        any of them
}

rule Macro_Malware {
    meta:
        description = "Detects malicious Office macros"
        author = "CyberDefense AI"
        severity = 8
        family = "Macro Virus"
        
    strings:
        $s1 = "Auto_Open" ascii wide
        $s2 = "Document_Open" ascii wide
        $s3 = "Workbook_Open" ascii wide
        $s4 = "Shell32.Application" ascii wide
        $s5 = "CreateObject" ascii wide
        $s6 = "WScript.Shell" ascii wide
        
    condition:
        2 of them
}

rule Generic_Keylogger {
    meta:
        description = "Detects keylogger behavior"
        author = "CyberDefense AI"
        severity = 7
        family = "Spyware"
        
    strings:
        $s1 = "GetAsyncKeyState" ascii
        $s2 = "SetWindowsHookEx" ascii
        $s3 = "keylog" ascii wide nocase
        $s4 = "GetKeyState" ascii
        $s5 = "GetForegroundWindow" ascii
        
    condition:
        2 of them
}

rule Rootkit_Detection {
    meta:
        description = "Generic rootkit detection"
        author = "CyberDefense AI"
        severity = 9
        family = "Rootkit"
        
    strings:
        $s1 = "ntoskrnl.exe" ascii
        $s2 = "ZwCreateFile" ascii
        $s3 = "NtQuerySystemInformation" ascii
        $s4 = "SSDT" ascii
        $hex1 = { FA 33 C0 8E D0 BC 00 7C }
        
    condition:
        2 of them
}

rule Browser_Hijacker {
    meta:
        description = "Detects browser hijacking malware"
        author = "CyberDefense AI"
        severity = 6
        family = "Adware"
        
    strings:
        $s1 = "search.yahoo.com" ascii wide
        $s2 = "toolbar.dll" ascii wide
        $s3 = "browser_hijack" ascii wide
        $s4 = "homepage" ascii wide
        $s5 = "default_search" ascii wide
        
    condition:
        2 of them
}

rule Backdoor_Detection {
    meta:
        description = "Generic backdoor detection"
        author = "CyberDefense AI"
        severity = 8
        family = "Backdoor"
        
    strings:
        $s1 = "cmd.exe /c" ascii wide
        $s2 = "nc.exe -l -p" ascii wide
        $s3 = "reverse_shell" ascii wide
        $s4 = "bind_shell" ascii wide
        $s5 = "CreateProcess" ascii
        
    condition:
        2 of them
}

rule APT_Indicators {
    meta:
        description = "Advanced Persistent Threat indicators"
        author = "CyberDefense AI"
        severity = 10
        family = "APT"
        
    strings:
        $s1 = "apt.exe" ascii wide
        $s2 = "persistence" ascii wide
        $s3 = "lateral_movement" ascii wide
        $s4 = "credential_dump" ascii wide
        $hex1 = { 89 4C 24 1C 8B 44 24 20 }
        
    condition:
        2 of them
}

rule DDoS_Tool {
    meta:
        description = "Detects DDoS attack tools"
        author = "CyberDefense AI"
        severity = 7
        family = "DDoS Tool"
        
    strings:
        $s1 = "LOIC" ascii wide
        $s2 = "botnet" ascii wide
        $s3 = "flood" ascii wide
        $s4 = "ddos" ascii wide nocase
        $s5 = "syn_flood" ascii wide
        
    condition:
        any of them
}

rule Network_Scanner {
    meta:
        description = "Detects network scanning tools"
        author = "CyberDefense AI"
        severity = 5
        family = "Reconnaissance"
        
    strings:
        $s1 = "nmap" ascii wide
        $s2 = "masscan" ascii wide
        $s3 = "port_scan" ascii wide
        $s4 = "network_recon" ascii wide
        
    condition:
        any of them
}

rule LockBit_Ransomware {
    meta:
        description = "Detects LockBit ransomware variants"
        author = "CyberDefense AI"
        severity = 10
        family = "Ransomware"
        
    strings:
        $s1 = ".lockbit" ascii wide
        $s2 = "LockBit_Ransomware" ascii wide
        $s3 = "Your data is stolen and encrypted" ascii wide
        $s4 = "lockbitapt" ascii wide
        
    condition:
        any of them
}

rule BlackCat_ALPHV_Ransomware {
    meta:
        description = "Detects BlackCat/ALPHV ransomware"
        author = "CyberDefense AI"
        severity = 10
        family = "Ransomware"
        
    strings:
        $s1 = ".alphv" ascii wide
        $s2 = "HOW_TO_RESTORE" ascii wide
        $s3 = "BlackCat" ascii wide
        $s4 = "alphv" ascii wide nocase
        
    condition:
        any of them
}

rule Qakbot_Banking_Trojan {
    meta:
        description = "Detects Qakbot banking trojan"
        author = "CyberDefense AI"
        severity = 9
        family = "Banking Trojan"
        
    strings:
        $s1 = "/t4" ascii
        $s2 = "qakbot" ascii wide nocase
        $s3 = "explorer.exe" ascii wide
        $hex1 = { 55 8B EC 83 EC ?? 83 65 ?? 00 }
        
    condition:
        2 of them
}

rule IcedID_Banking_Trojan {
    meta:
        description = "Detects IcedID banking trojan"
        author = "CyberDefense AI"
        severity = 8
        family = "Banking Trojan"
        
    strings:
        $s1 = "gzip64" ascii
        $s2 = "icedid" ascii wide nocase
        $s3 = "rundll32.exe" ascii wide
        $hex1 = { 4D 5A ?? ?? ?? ?? BA ?? 00 }
        
    condition:
        2 of them
}

rule BazarLoader {
    meta:
        description = "Detects BazarLoader malware"
        author = "CyberDefense AI"
        severity = 8
        family = "Loader"
        
    strings:
        $s1 = "/api/v" ascii
        $s2 = "bazarloader" ascii wide nocase
        $hex1 = { BA ?? ?? ?? ?? B9 ?? ?? ?? ?? }
        
    condition:
        any of them
}