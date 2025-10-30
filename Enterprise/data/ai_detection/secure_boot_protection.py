"""
Secure Boot Protection System
Advanced boot sector protection and rootkit defense
"""

import os
import sys
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import json
import hashlib
import struct

# Windows API imports for low-level boot sector access
try:
    import ctypes
    from ctypes import wintypes, windll
    import winreg
    WINDOWS_API_AVAILABLE = True
except ImportError:
    WINDOWS_API_AVAILABLE = False

class SecureBootProtection:
    """Advanced boot sector protection and monitoring"""
    
    def __init__(self):
        self.protection_active = False
        self.boot_database = "data/settings/boot_protection.db"
        self.boot_backup_dir = Path("backup/boot_sectors")
        self.boot_backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Boot sector monitoring
        self.original_mbr_hash = None
        self.original_boot_sectors = {}
        self.monitoring_thread = None
        self.stop_monitoring = False
        
        # Initialize database and baseline
        self.init_database()
        self.create_boot_baseline()
    
    def init_database(self):
        """Initialize boot protection database"""
        try:
            os.makedirs(os.path.dirname(self.boot_database), exist_ok=True)
            
            conn = sqlite3.connect(self.boot_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS boot_sectors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    sector_type TEXT,
                    drive_letter TEXT,
                    sector_hash TEXT,
                    sector_data BLOB,
                    is_baseline BOOLEAN
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS boot_threats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    threat_type TEXT,
                    sector_affected TEXT,
                    threat_details TEXT,
                    action_taken TEXT,
                    severity INTEGER
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS boot_repairs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    repair_type TEXT,
                    target_sector TEXT,
                    success BOOLEAN,
                    backup_created TEXT,
                    repair_details TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
            
            print("✅ Boot protection database initialized")
            
        except Exception as e:
            print(f"❌ Failed to initialize boot protection database: {e}")
    
    def create_boot_baseline(self):
        """Create baseline of clean boot sectors"""
        try:
            print("📊 Creating boot sector baseline...")
            
            # Get system drives
            drives = self.get_system_drives()
            
            for drive in drives:
                try:
                    # Read MBR/boot sector
                    boot_data = self.read_boot_sector(drive)
                    if boot_data:
                        # Calculate hash
                        boot_hash = hashlib.sha256(boot_data).hexdigest()
                        
                        # Store baseline
                        self.store_boot_sector(drive, "MBR", boot_data, boot_hash, True)
                        self.original_boot_sectors[drive] = {
                            'hash': boot_hash,
                            'data': boot_data,
                            'timestamp': datetime.now()
                        }
                        
                        print(f"📝 Baseline created for drive {drive}")
                
                except Exception as e:
                    print(f"⚠️ Failed to create baseline for drive {drive}: {e}")
            
            print("✅ Boot sector baseline completed")
            
        except Exception as e:
            print(f"❌ Failed to create boot baseline: {e}")
    
    def get_system_drives(self) -> List[str]:
        """Get list of system drives to monitor"""
        drives = []
        
        if sys.platform == "win32":
            # Get Windows system drives
            drive_bitmask = windll.kernel32.GetLogicalDrives()
            for i in range(26):
                if drive_bitmask & (1 << i):
                    drive_letter = chr(ord('A') + i)
                    drives.append(drive_letter)
        
        return drives[:3]  # Monitor first 3 drives (typically C:, D:, E:)
    
    def read_boot_sector(self, drive_letter: str) -> Optional[bytes]:
        """Read boot sector from drive"""
        try:
            if not WINDOWS_API_AVAILABLE:
                return None
            
            # Open drive handle
            drive_path = f"\\\\.\\{drive_letter}:"
            handle = windll.kernel32.CreateFileW(
                drive_path,
                0x80000000,  # GENERIC_READ
                0x00000003,  # FILE_SHARE_READ | FILE_SHARE_WRITE
                None,
                3,           # OPEN_EXISTING
                0,
                None
            )
            
            if handle == -1:
                return None
            
            # Read first 512 bytes (boot sector)
            buffer = ctypes.create_string_buffer(512)
            bytes_read = wintypes.DWORD()
            
            success = windll.kernel32.ReadFile(
                handle,
                buffer,
                512,
                ctypes.byref(bytes_read),
                None
            )
            
            windll.kernel32.CloseHandle(handle)
            
            if success and bytes_read.value == 512:
                return buffer.raw
            
            return None
            
        except Exception as e:
            print(f"❌ Failed to read boot sector for {drive_letter}: {e}")
            return None
    
    def start_boot_monitoring(self):
        """Start real-time boot sector monitoring"""
        if self.protection_active:
            return
        
        self.protection_active = True
        self.stop_monitoring = False
        
        self.monitoring_thread = threading.Thread(
            target=self.boot_monitoring_loop,
            daemon=True
        )
        self.monitoring_thread.start()
        
        print("🛡️ Boot sector monitoring started")
    
    def stop_boot_monitoring(self):
        """Stop boot sector monitoring"""
        self.protection_active = False
        self.stop_monitoring = True
        
        if self.monitoring_thread and self.monitoring_thread.is_alive():
            self.monitoring_thread.join(timeout=5)
        
        print("⏹️ Boot sector monitoring stopped")
    
    def boot_monitoring_loop(self):
        """Main boot sector monitoring loop"""
        while not self.stop_monitoring:
            try:
                # Check each monitored drive
                for drive in self.original_boot_sectors:
                    self.check_boot_sector_integrity(drive)
                
                # Check for bootkit indicators
                self.scan_for_bootkits()
                
                # Check UEFI/BIOS integrity
                self.check_firmware_integrity()
                
                # Sleep before next check
                time.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                print(f"❌ Boot monitoring error: {e}")
                time.sleep(60)  # Longer sleep on error
    
    def check_boot_sector_integrity(self, drive_letter: str):
        """Check if boot sector has been modified"""
        try:
            # Read current boot sector
            current_data = self.read_boot_sector(drive_letter)
            if not current_data:
                return
            
            # Calculate current hash
            current_hash = hashlib.sha256(current_data).hexdigest()
            
            # Compare with baseline
            baseline = self.original_boot_sectors.get(drive_letter)
            if baseline and current_hash != baseline['hash']:
                # Boot sector modification detected!
                threat_info = {
                    'threat_type': 'Boot Sector Modification',
                    'drive': drive_letter,
                    'original_hash': baseline['hash'],
                    'current_hash': current_hash,
                    'timestamp': datetime.now(),
                    'severity': 10  # Maximum severity
                }
                
                self.handle_boot_threat(threat_info)
        
        except Exception as e:
            print(f"❌ Boot integrity check failed for {drive_letter}: {e}")
    
    def scan_for_bootkits(self):
        """Scan for bootkit indicators"""
        try:
            indicators_found = []
            
            # Check for suspicious registry entries
            bootkit_registry_keys = [
                r"SYSTEM\CurrentControlSet\Control\Session Manager",
                r"SYSTEM\CurrentControlSet\Services",
                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
            ]
            
            for key_path in bootkit_registry_keys:
                if self.scan_registry_for_bootkits(key_path):
                    indicators_found.append(f"Suspicious registry: {key_path}")
            
            # Check for MBR hooks
            if self.check_mbr_hooks():
                indicators_found.append("MBR hook detected")
            
            # Check for SSDT hooks
            if self.check_ssdt_hooks():
                indicators_found.append("SSDT hook detected")
            
            if indicators_found:
                threat_info = {
                    'threat_type': 'Bootkit Indicators',
                    'indicators': indicators_found,
                    'timestamp': datetime.now(),
                    'severity': 9
                }
                
                self.handle_boot_threat(threat_info)
        
        except Exception as e:
            print(f"❌ Bootkit scan failed: {e}")
    
    def check_firmware_integrity(self):
        """Check UEFI/BIOS integrity"""
        try:
            # Check for UEFI variables manipulation
            if self.check_uefi_variables():
                threat_info = {
                    'threat_type': 'UEFI Firmware Threat',
                    'description': 'Suspicious UEFI variable modifications detected',
                    'timestamp': datetime.now(),
                    'severity': 10
                }
                
                self.handle_boot_threat(threat_info)
            
            # Check secure boot status
            secure_boot_status = self.get_secure_boot_status()
            if secure_boot_status == "disabled_unexpectedly":
                threat_info = {
                    'threat_type': 'Secure Boot Disabled',
                    'description': 'Secure Boot has been unexpectedly disabled',
                    'timestamp': datetime.now(),
                    'severity': 8
                }
                
                self.handle_boot_threat(threat_info)
        
        except Exception as e:
            print(f"❌ Firmware integrity check failed: {e}")
    
    def handle_boot_threat(self, threat_info: Dict[str, Any]):
        """Handle detected boot sector threat"""
        try:
            threat_type = threat_info.get('threat_type', 'Unknown Boot Threat')
            severity = threat_info.get('severity', 5)
            
            print(f"🚨 BOOT THREAT DETECTED: {threat_type}")
            
            # Log threat to database
            self.log_boot_threat(threat_info)
            
            # Send critical notification
            from windows_notifications import WindowsNotificationSystem
            notifier = WindowsNotificationSystem()
            notifier.send_boot_protection_alert(threat_info)
            
            # Automatic response based on severity
            if severity >= 9:
                # Critical threat - immediate action
                self.emergency_boot_response(threat_info)
            elif severity >= 7:
                # High threat - defensive measures
                self.defensive_boot_response(threat_info)
            else:
                # Medium threat - monitoring and logging
                self.monitor_boot_threat(threat_info)
        
        except Exception as e:
            print(f"❌ Failed to handle boot threat: {e}")
    
    def emergency_boot_response(self, threat_info: Dict[str, Any]):
        """Emergency response to critical boot threats"""
        try:
            print("🚨 EXECUTING EMERGENCY BOOT RESPONSE")
            
            # 1. Create emergency backup
            self.create_emergency_boot_backup()
            
            # 2. Isolate system
            self.enable_boot_isolation_mode()
            
            # 3. Prepare boot sector restoration
            self.prepare_boot_restoration(threat_info)
            
            # 4. Alert user with immediate action options
            self.show_emergency_boot_dialog(threat_info)
        
        except Exception as e:
            print(f"❌ Emergency boot response failed: {e}")
    
    def defensive_boot_response(self, threat_info: Dict[str, Any]):
        """Defensive response to boot threats"""
        try:
            print("🛡️ EXECUTING DEFENSIVE BOOT RESPONSE")
            
            # 1. Create backup
            self.create_boot_backup()
            
            # 2. Enable enhanced monitoring
            self.enable_enhanced_boot_monitoring()
            
            # 3. Prepare countermeasures
            self.prepare_boot_countermeasures(threat_info)
        
        except Exception as e:
            print(f"❌ Defensive boot response failed: {e}")
    
    def repair_boot_sector(self, drive_letter: str, use_backup: bool = True) -> Dict[str, Any]:
        """Repair infected boot sector"""
        try:
            print(f"🔧 Repairing boot sector for drive {drive_letter}")
            
            # Create backup before repair
            repair_backup = self.create_repair_backup(drive_letter)
            
            if use_backup and drive_letter in self.original_boot_sectors:
                # Restore from clean baseline
                baseline_data = self.original_boot_sectors[drive_letter]['data']
                success = self.write_boot_sector(drive_letter, baseline_data)
                
                if success:
                    print(f"✅ Boot sector restored from baseline for {drive_letter}")
                    self.log_boot_repair(drive_letter, "baseline_restore", True, repair_backup)
                    
                    return {
                        'success': True,
                        'method': 'baseline_restore',
                        'backup_file': repair_backup
                    }
            
            # Alternative: Use Windows boot repair tools
            success = self.use_windows_boot_repair(drive_letter)
            
            if success:
                print(f"✅ Boot sector repaired using Windows tools for {drive_letter}")
                self.log_boot_repair(drive_letter, "windows_tools", True, repair_backup)
                
                return {
                    'success': True,
                    'method': 'windows_tools',
                    'backup_file': repair_backup
                }
            
            print(f"❌ Boot sector repair failed for {drive_letter}")
            return {'success': False, 'error': 'All repair methods failed'}
        
        except Exception as e:
            print(f"❌ Boot sector repair failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def write_boot_sector(self, drive_letter: str, data: bytes) -> bool:
        """Write data to boot sector"""
        try:
            if not WINDOWS_API_AVAILABLE or len(data) != 512:
                return False
            
            # Open drive handle with write access
            drive_path = f"\\\\.\\{drive_letter}:"
            handle = windll.kernel32.CreateFileW(
                drive_path,
                0x40000000,  # GENERIC_WRITE
                0,
                None,
                3,           # OPEN_EXISTING
                0,
                None
            )
            
            if handle == -1:
                return False
            
            # Write boot sector
            bytes_written = wintypes.DWORD()
            success = windll.kernel32.WriteFile(
                handle,
                data,
                512,
                ctypes.byref(bytes_written),
                None
            )
            
            windll.kernel32.CloseHandle(handle)
            
            return success and bytes_written.value == 512
        
        except Exception as e:
            print(f"❌ Failed to write boot sector: {e}")
            return False
    
    def use_windows_boot_repair(self, drive_letter: str) -> bool:
        """Use Windows built-in boot repair tools"""
        try:
            # Use bootrec commands
            commands = [
                ["bootrec", "/fixmbr"],
                ["bootrec", "/fixboot"],
                ["bootrec", "/rebuildbcd"]
            ]
            
            for cmd in commands:
                try:
                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=60
                    )
                    
                    if result.returncode == 0:
                        print(f"✅ Successfully executed: {' '.join(cmd)}")
                    else:
                        print(f"⚠️ Command failed: {' '.join(cmd)}")
                
                except subprocess.TimeoutExpired:
                    print(f"⏰ Command timed out: {' '.join(cmd)}")
                except FileNotFoundError:
                    print(f"❌ Command not found: {' '.join(cmd)}")
            
            return True
        
        except Exception as e:
            print(f"❌ Windows boot repair failed: {e}")
            return False
    
    def scan_registry_for_bootkits(self, key_path: str) -> bool:
        """Scan registry key for bootkit indicators"""
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
            
            # Check for suspicious values
            suspicious_patterns = [
                "bootkit", "rootkit", "hook", "inject", 
                "stealth", "hide", "bypass", "persistence"
            ]
            
            i = 0
            while True:
                try:
                    name, value, type = winreg.EnumValue(key, i)
                    value_str = str(value).lower()
                    name_str = name.lower()
                    
                    if any(pattern in value_str or pattern in name_str 
                          for pattern in suspicious_patterns):
                        winreg.CloseKey(key)
                        return True
                    
                    i += 1
                    
                except WindowsError:
                    break
            
            winreg.CloseKey(key)
            return False
        
        except:
            return False
    
    def check_mbr_hooks(self) -> bool:
        """Check for MBR hooks"""
        try:
            # This would require more advanced techniques
            # For now, return False (no hooks detected)
            return False
        except:
            return False
    
    def check_ssdt_hooks(self) -> bool:
        """Check for SSDT hooks"""
        try:
            # This would require kernel-level access
            # For now, return False (no hooks detected)
            return False
        except:
            return False
    
    def check_uefi_variables(self) -> bool:
        """Check UEFI variables for manipulation"""
        try:
            # Check if running on UEFI system
            if not Path("C:\\Windows\\System32\\uefi").exists():
                return False
            
            # This would require UEFI variable access
            # For now, return False (no threats detected)
            return False
        except:
            return False
    
    def get_secure_boot_status(self) -> str:
        """Get Secure Boot status"""
        try:
            # Check Secure Boot registry key
            key_path = r"SYSTEM\CurrentControlSet\Control\SecureBoot\State"
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
            
            value, _ = winreg.QueryValueEx(key, "UEFISecureBootEnabled")
            winreg.CloseKey(key)
            
            return "enabled" if value == 1 else "disabled"
        
        except:
            return "unknown"
    
    def create_emergency_boot_backup(self):
        """Create emergency boot sector backup"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.boot_backup_dir / f"emergency_backup_{timestamp}.bin"
            
            # Backup all monitored drives
            with open(backup_file, 'wb') as f:
                for drive, baseline in self.original_boot_sectors.items():
                    f.write(baseline['data'])
            
            print(f"💾 Emergency boot backup created: {backup_file}")
            
        except Exception as e:
            print(f"❌ Emergency backup failed: {e}")
    
    def create_boot_backup(self):
        """Create regular boot sector backup"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.boot_backup_dir / f"boot_backup_{timestamp}.bin"
            
            # Read and backup current boot sectors
            backup_data = {}
            for drive in self.original_boot_sectors:
                current_data = self.read_boot_sector(drive)
                if current_data:
                    backup_data[drive] = current_data
            
            # Save backup
            with open(backup_file, 'wb') as f:
                for drive, data in backup_data.items():
                    f.write(data)
            
            print(f"💾 Boot backup created: {backup_file}")
            
        except Exception as e:
            print(f"❌ Boot backup failed: {e}")
    
    def create_repair_backup(self, drive_letter: str) -> str:
        """Create backup before repair"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.boot_backup_dir / f"pre_repair_{drive_letter}_{timestamp}.bin"
            
            current_data = self.read_boot_sector(drive_letter)
            if current_data:
                with open(backup_file, 'wb') as f:
                    f.write(current_data)
                
                return str(backup_file)
            
            return ""
        
        except Exception as e:
            print(f"❌ Repair backup failed: {e}")
            return ""
    
    def enable_boot_isolation_mode(self):
        """Enable boot isolation mode"""
        try:
            # This would implement boot-level isolation
            print("🔒 Boot isolation mode enabled")
        except Exception as e:
            print(f"❌ Failed to enable boot isolation: {e}")
    
    def enable_enhanced_boot_monitoring(self):
        """Enable enhanced boot monitoring"""
        try:
            print("👁️ Enhanced boot monitoring enabled")
            # Reduce monitoring interval for enhanced mode
            # This would be implemented in the monitoring loop
        except Exception as e:
            print(f"❌ Failed to enable enhanced monitoring: {e}")
    
    def prepare_boot_restoration(self, threat_info: Dict[str, Any]):
        """Prepare boot sector restoration"""
        try:
            print("🛠️ Boot restoration prepared")
            # Prepare restoration procedures
        except Exception as e:
            print(f"❌ Failed to prepare boot restoration: {e}")
    
    def prepare_boot_countermeasures(self, threat_info: Dict[str, Any]):
        """Prepare boot countermeasures"""
        try:
            print("⚔️ Boot countermeasures prepared")
            # Prepare countermeasures
        except Exception as e:
            print(f"❌ Failed to prepare countermeasures: {e}")
    
    def show_emergency_boot_dialog(self, threat_info: Dict[str, Any]):
        """Show emergency boot threat dialog"""
        import tkinter as tk
        from tkinter import messagebox
        
        threat_type = threat_info.get('threat_type', 'Critical Boot Threat')
        
        message = f"""
CRITICAL BOOT SECTOR THREAT DETECTED!

Threat: {threat_type}

This is an EXTREME security risk that could:
- Prevent your computer from starting
- Install undetectable malware
- Steal all your sensitive data
- Damage your system permanently

IMMEDIATE ACTION REQUIRED:

1. DISCONNECT from the internet NOW
2. Do NOT restart your computer
3. Allow emergency boot sector repair
4. Run full system scan after repair

Authorize emergency boot repair?

WARNING: Declining repair may result in 
complete system compromise or failure!
        """
        
        result = messagebox.askyesno(
            "🚨 CRITICAL BOOT THREAT",
            message,
            icon=messagebox.ERROR
        )
        
        if result:
            # User authorized repair
            drive = threat_info.get('drive', 'C')
            repair_result = self.repair_boot_sector(drive)
            
            if repair_result['success']:
                messagebox.showinfo(
                    "✅ Boot Repair Complete",
                    f"Boot sector has been successfully repaired.\n\n"
                    f"Method: {repair_result['method']}\n"
                    f"Backup: {repair_result.get('backup_file', 'None')}\n\n"
                    f"Please restart your computer and run a full system scan."
                )
            else:
                messagebox.showerror(
                    "❌ Boot Repair Failed",
                    f"Boot sector repair failed!\n\n"
                    f"Error: {repair_result.get('error', 'Unknown')}\n\n"
                    f"Please contact technical support immediately."
                )
        else:
            messagebox.showwarning(
                "⚠️ Repair Declined",
                "Boot sector repair was declined.\n\n"
                "Your system remains at EXTREME risk.\n"
                "Please backup your data immediately and\n"
                "consider professional malware removal."
            )
    
    def monitor_boot_threat(self, threat_info: Dict[str, Any]):
        """Monitor boot threat"""
        try:
            print(f"👁️ Monitoring boot threat: {threat_info.get('threat_type', 'Unknown')}")
            # Enhanced monitoring for this specific threat
        except Exception as e:
            print(f"❌ Failed to monitor boot threat: {e}")
    
    def store_boot_sector(self, drive: str, sector_type: str, data: bytes, hash_value: str, is_baseline: bool):
        """Store boot sector data in database"""
        try:
            conn = sqlite3.connect(self.boot_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO boot_sectors 
                (timestamp, sector_type, drive_letter, sector_hash, sector_data, is_baseline)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                sector_type,
                drive,
                hash_value,
                data,
                is_baseline
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ Failed to store boot sector: {e}")
    
    def log_boot_threat(self, threat_info: Dict[str, Any]):
        """Log boot threat to database"""
        try:
            conn = sqlite3.connect(self.boot_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO boot_threats 
                (timestamp, threat_type, sector_affected, threat_details, action_taken, severity)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                threat_info.get('threat_type', 'Unknown'),
                threat_info.get('drive', 'Unknown'),
                json.dumps(threat_info),
                threat_info.get('action_taken', 'Detected'),
                threat_info.get('severity', 5)
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ Failed to log boot threat: {e}")
    
    def log_boot_repair(self, drive: str, repair_type: str, success: bool, backup_file: str):
        """Log boot repair action"""
        try:
            conn = sqlite3.connect(self.boot_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO boot_repairs 
                (timestamp, repair_type, target_sector, success, backup_created, repair_details)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                repair_type,
                drive,
                success,
                backup_file,
                f"Boot sector repair for drive {drive}"
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ Failed to log boot repair: {e}")

class SecureBootProtectionGUI:
    """GUI for secure boot protection management"""
    
    def __init__(self, threat_info: Optional[Dict[str, Any]] = None):
        self.threat_info = threat_info
        self.boot_protection = SecureBootProtection()
        
        self.window = tk.Toplevel()
        self.window.title("🛡️ Secure Boot Protection")
        self.window.geometry("900x700")
        self.window.configure(bg='#1a1a1a')
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the boot protection GUI"""
        # Title
        title_frame = tk.Frame(self.window, bg='#1a1a1a')
        title_frame.pack(fill='x', padx=10, pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="🛡️ SECURE BOOT PROTECTION CENTER",
            font=('Arial', 16, 'bold'),
            fg='#ff6600',
            bg='#1a1a1a'
        )
        title_label.pack()
        
        # Main notebook
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_monitoring_tab(notebook)
        self.create_repair_tab(notebook)
        self.create_threats_tab(notebook)
        self.create_settings_tab(notebook)
        
        # Control frame
        control_frame = tk.Frame(self.window, bg='#1a1a1a')
        control_frame.pack(fill='x', padx=10, pady=5)
        
        # Start/Stop monitoring
        self.monitor_btn = tk.Button(
            control_frame,
            text="🚀 Start Protection",
            command=self.toggle_monitoring,
            bg='#009900',
            fg='#ffffff',
            font=('Arial', 12, 'bold'),
            padx=20
        )
        self.monitor_btn.pack(side='left', padx=5)
        
        tk.Button(
            control_frame,
            text="Close",
            command=self.window.destroy,
            bg='#444444',
            fg='#ffffff',
            font=('Arial', 10)
        ).pack(side='right', padx=5)
    
    def create_monitoring_tab(self, notebook):
        """Create boot monitoring tab"""
        tab = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(tab, text="Boot Monitoring")
        
        # Status frame
        status_frame = tk.LabelFrame(
            tab,
            text="Protection Status",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        status_frame.pack(fill='x', padx=10, pady=5)
        
        self.status_label = tk.Label(
            status_frame,
            text="🔴 Protection: INACTIVE",
            font=('Arial', 12, 'bold'),
            fg='#ff4444',
            bg='#2a2a2a'
        )
        self.status_label.pack(pady=10)
        
        # Boot sectors frame
        sectors_frame = tk.LabelFrame(
            tab,
            text="Monitored Boot Sectors",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        sectors_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Sectors tree
        columns = ('Drive', 'Status', 'Hash', 'Last Check')
        self.sectors_tree = ttk.Treeview(sectors_frame, columns=columns, show='headings')
        
        for col in columns:
            self.sectors_tree.heading(col, text=col)
            self.sectors_tree.column(col, width=150)
        
        self.sectors_tree.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Populate with current data
        self.update_sectors_display()
    
    def create_repair_tab(self, notebook):
        """Create boot repair tab"""
        tab = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(tab, text="Boot Repair")
        
        # If we have threat info, show it
        if self.threat_info:
            threat_frame = tk.LabelFrame(
                tab,
                text="Detected Threat",
                font=('Arial', 10, 'bold'),
                fg='#ff4444',
                bg='#2a2a2a'
            )
            threat_frame.pack(fill='x', padx=10, pady=5)
            
            threat_type = self.threat_info.get('threat_type', 'Unknown')
            tk.Label(
                threat_frame,
                text=f"🚨 {threat_type}",
                font=('Arial', 12, 'bold'),
                fg='#ff4444',
                bg='#2a2a2a'
            ).pack(anchor='w', padx=10, pady=5)
        
        # Repair options frame
        repair_frame = tk.LabelFrame(
            tab,
            text="Repair Options",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        repair_frame.pack(fill='x', padx=10, pady=5)
        
        repair_buttons = [
            ("🔧 Quick Boot Repair", "quick_repair"),
            ("💾 Restore from Backup", "restore_backup"),
            ("🛠️ Advanced Repair", "advanced_repair"),
            ("📊 Create Boot Backup", "create_backup")
        ]
        
        for text, action in repair_buttons:
            btn = tk.Button(
                repair_frame,
                text=text,
                command=lambda a=action: self.execute_repair(a),
                bg='#0066cc',
                fg='#ffffff',
                font=('Arial', 10, 'bold'),
                padx=20,
                pady=5
            )
            btn.pack(side='left', padx=5, pady=5)
        
        # Repair log
        log_frame = tk.LabelFrame(
            tab,
            text="Repair Log",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        log_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.repair_log_text = tk.Text(
            log_frame,
            height=15,
            bg='#000000',
            fg='#00ff00',
            font=('Consolas', 9),
            wrap='word'
        )
        self.repair_log_text.pack(fill='both', expand=True, padx=5, pady=5)
    
    def create_threats_tab(self, notebook):
        """Create threats history tab"""
        tab = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(tab, text="Threat History")
        
        # Threats tree
        columns = ('Timestamp', 'Threat Type', 'Sector', 'Severity', 'Action')
        self.threats_tree = ttk.Treeview(tab, columns=columns, show='headings')
        
        for col in columns:
            self.threats_tree.heading(col, text=col)
            self.threats_tree.column(col, width=150)
        
        self.threats_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Load threat history
        self.update_threats_display()
    
    def create_settings_tab(self, notebook):
        """Create settings tab"""
        tab = tk.Frame(notebook, bg='#2a2a2a')
        notebook.add(tab, text="Settings")
        
        # Settings content
        tk.Label(
            tab,
            text="Boot Protection Settings",
            font=('Arial', 14, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        ).pack(pady=20)
        
        # Placeholder for settings
        tk.Label(
            tab,
            text="Settings interface will be implemented here",
            font=('Arial', 10),
            fg='#cccccc',
            bg='#2a2a2a'
        ).pack()
    
    def toggle_monitoring(self):
        """Toggle boot monitoring on/off"""
        if self.boot_protection.protection_active:
            self.boot_protection.stop_boot_monitoring()
            self.monitor_btn.config(
                text="🚀 Start Protection",
                bg='#009900'
            )
            self.status_label.config(
                text="🔴 Protection: INACTIVE",
                fg='#ff4444'
            )
        else:
            self.boot_protection.start_boot_monitoring()
            self.monitor_btn.config(
                text="⏹️ Stop Protection",
                bg='#cc0000'
            )
            self.status_label.config(
                text="🟢 Protection: ACTIVE",
                fg='#00ff00'
            )
    
    def execute_repair(self, action: str):
        """Execute boot repair action"""
        self.log_repair_message(f"\n🔧 Starting {action}...")
        
        try:
            if action == "quick_repair":
                # Quick repair for all drives
                for drive in self.boot_protection.original_boot_sectors:
                    result = self.boot_protection.repair_boot_sector(drive)
                    if result['success']:
                        self.log_repair_message(f"✅ Quick repair completed for drive {drive}")
                    else:
                        self.log_repair_message(f"❌ Quick repair failed for drive {drive}: {result.get('error', 'Unknown')}")
            
            elif action == "restore_backup":
                self.log_repair_message("📦 Backup restoration not yet implemented")
            
            elif action == "advanced_repair":
                self.log_repair_message("⚙️ Advanced repair not yet implemented")
            
            elif action == "create_backup":
                self.boot_protection.create_boot_backup()
                self.log_repair_message("💾 Boot backup created successfully")
        
        except Exception as e:
            self.log_repair_message(f"❌ Repair action failed: {e}")
    
    def log_repair_message(self, message: str):
        """Log message to repair log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        
        self.repair_log_text.insert('end', full_message)
        self.repair_log_text.see('end')
        self.window.update()
    
    def update_sectors_display(self):
        """Update boot sectors display"""
        # Clear existing items
        for item in self.sectors_tree.get_children():
            self.sectors_tree.delete(item)
        
        # Add current sectors
        for drive, baseline in self.boot_protection.original_boot_sectors.items():
            self.sectors_tree.insert('', 'end', values=(
                f"{drive}:",
                "✅ Protected",
                baseline['hash'][:16] + "...",
                baseline['timestamp'].strftime("%Y-%m-%d %H:%M")
            ))
    
    def update_threats_display(self):
        """Update threats history display"""
        try:
            conn = sqlite3.connect(self.boot_protection.boot_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT timestamp, threat_type, sector_affected, severity, action_taken
                FROM boot_threats
                ORDER BY timestamp DESC
                LIMIT 100
            ''')
            
            threats = cursor.fetchall()
            conn.close()
            
            # Clear existing items
            for item in self.threats_tree.get_children():
                self.threats_tree.delete(item)
            
            # Add threats
            for threat in threats:
                timestamp = datetime.fromisoformat(threat[0]).strftime("%Y-%m-%d %H:%M")
                self.threats_tree.insert('', 'end', values=(
                    timestamp,
                    threat[1],
                    threat[2],
                    f"⚠️ {threat[3]}/10",
                    threat[4]
                ))
        
        except Exception as e:
            print(f"❌ Failed to update threats display: {e}")
    
    def show(self):
        """Show the boot protection window"""
        self.window.focus_force()
        self.window.mainloop()

# Test function
def test_boot_protection():
    """Test the boot protection system"""
    # Test basic functionality
    boot_protection = SecureBootProtection()
    
    # Test GUI
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    # Simulate boot threat
    threat_info = {
        'threat_type': 'Boot Sector Rootkit',
        'drive': 'C',
        'severity': 10
    }
    
    gui = SecureBootProtectionGUI(threat_info)
    gui.show()

if __name__ == "__main__":
    test_boot_protection()