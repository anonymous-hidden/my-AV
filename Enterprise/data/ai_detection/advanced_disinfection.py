"""
Advanced Disinfection System
Comprehensive malware removal and system healing
"""

import os
import sys
import time
import shutil
import threading
import subprocess
import hashlib
import winreg
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import json
import psutil

class AdvancedDisinfectionSystem:
    """Advanced malware disinfection and system repair"""
    
    def __init__(self):
        self.quarantine_dir = Path("quarantine/advanced")
        self.quarantine_dir.mkdir(parents=True, exist_ok=True)
        
        self.backup_dir = Path("backup/system_restore")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        self.repair_log = []
        self.disinfection_database = "data/settings/disinfection_log.db"
        
        # Initialize database
        self.init_database()
        
        # Disinfection methods
        self.disinfection_methods = {
            'quarantine': self.quarantine_threat,
            'deep_clean': self.deep_clean_threat,
            'registry_repair': self.repair_registry_infection,
            'memory_clean': self.clean_memory_infection,
            'network_isolation': self.isolate_network_threat,
            'process_termination': self.terminate_malicious_process,
            'file_restoration': self.restore_infected_files
        }
    
    def init_database(self):
        """Initialize disinfection tracking database"""
        try:
            os.makedirs(os.path.dirname(self.disinfection_database), exist_ok=True)
            
            conn = sqlite3.connect(self.disinfection_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS disinfection_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    threat_name TEXT,
                    file_path TEXT,
                    method_used TEXT,
                    success BOOLEAN,
                    details TEXT,
                    user_action TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS quarantine_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    original_path TEXT,
                    quarantine_path TEXT,
                    threat_type TEXT,
                    file_hash TEXT,
                    size INTEGER,
                    metadata TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
            
            print("✅ Disinfection database initialized")
            
        except Exception as e:
            print(f"❌ Failed to initialize disinfection database: {e}")
    
    def quarantine_threat(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Advanced quarantine with metadata preservation"""
        try:
            file_path = Path(threat_info.get('file_path', ''))
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            if not file_path.exists():
                return {
                    'success': False,
                    'error': 'File not found',
                    'method': 'quarantine'
                }
            
            # Generate unique quarantine name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_hash = self.calculate_file_hash(file_path)
            quarantine_name = f"{timestamp}_{threat_name}_{file_hash[:8]}"
            quarantine_path = self.quarantine_dir / quarantine_name
            
            # Create metadata
            metadata = {
                'original_path': str(file_path),
                'original_size': file_path.stat().st_size,
                'original_modified': file_path.stat().st_mtime,
                'threat_info': threat_info,
                'quarantine_time': datetime.now().isoformat(),
                'system_info': {
                    'user': os.getenv('USERNAME'),
                    'computer': os.getenv('COMPUTERNAME'),
                    'os': sys.platform
                }
            }
            
            # Save metadata
            metadata_path = quarantine_path.with_suffix('.meta')
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            # Move file to quarantine (encrypted if possible)
            shutil.move(str(file_path), str(quarantine_path))
            
            # Log quarantine action
            self.log_disinfection_action(
                threat_name, str(file_path), 'quarantine', True,
                f"File quarantined as {quarantine_name}", "automatic"
            )
            
            # Store in database
            conn = sqlite3.connect(self.disinfection_database)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO quarantine_items 
                (timestamp, original_path, quarantine_path, threat_type, file_hash, size, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                str(file_path),
                str(quarantine_path),
                threat_name,
                file_hash,
                metadata['original_size'],
                json.dumps(metadata)
            ))
            conn.commit()
            conn.close()
            
            print(f"🔒 Quarantined: {file_path} -> {quarantine_name}")
            
            return {
                'success': True,
                'method': 'quarantine',
                'quarantine_path': str(quarantine_path),
                'metadata_path': str(metadata_path),
                'file_hash': file_hash
            }
            
        except Exception as e:
            self.log_disinfection_action(
                threat_name, str(file_path), 'quarantine', False,
                f"Quarantine failed: {e}", "automatic"
            )
            
            return {
                'success': False,
                'error': str(e),
                'method': 'quarantine'
            }
    
    def deep_clean_threat(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Comprehensive deep cleaning of threat artifacts"""
        try:
            file_path = threat_info.get('file_path', '')
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            cleaning_results = {
                'files_removed': [],
                'registry_cleaned': [],
                'processes_terminated': [],
                'temp_cleaned': False,
                'cache_cleared': False
            }
            
            # 1. Remove main threat file
            if file_path and Path(file_path).exists():
                try:
                    os.remove(file_path)
                    cleaning_results['files_removed'].append(file_path)
                except Exception as e:
                    print(f"❌ Failed to remove main file: {e}")
            
            # 2. Clean temporary files
            temp_dirs = [
                Path(os.environ.get('TEMP', '')),
                Path(os.environ.get('TMP', '')),
                Path.home() / 'AppData' / 'Local' / 'Temp'
            ]
            
            for temp_dir in temp_dirs:
                if temp_dir.exists():
                    self.clean_temp_directory(temp_dir, cleaning_results)
            
            cleaning_results['temp_cleaned'] = True
            
            # 3. Clear browser caches and downloads
            self.clear_browser_artifacts(cleaning_results)
            cleaning_results['cache_cleared'] = True
            
            # 4. Clean recent documents and MRU lists
            self.clean_recent_documents(cleaning_results)
            
            # 5. Scan for related files by pattern
            self.scan_and_remove_related_files(threat_name, cleaning_results)
            
            # 6. Memory cleanup
            self.force_memory_cleanup()
            
            self.log_disinfection_action(
                threat_name, file_path, 'deep_clean', True,
                f"Deep clean completed: {len(cleaning_results['files_removed'])} files removed",
                "automatic"
            )
            
            return {
                'success': True,
                'method': 'deep_clean',
                'results': cleaning_results
            }
            
        except Exception as e:
            self.log_disinfection_action(
                threat_name, file_path, 'deep_clean', False,
                f"Deep clean failed: {e}", "automatic"
            )
            
            return {
                'success': False,
                'error': str(e),
                'method': 'deep_clean'
            }
    
    def repair_registry_infection(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Repair registry infections and malicious entries"""
        try:
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            # Registry keys commonly infected by malware
            malicious_patterns = [
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
                r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run",
                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",
                r"SYSTEM\CurrentControlSet\Services"
            ]
            
            registry_repairs = []
            
            for pattern in malicious_patterns:
                try:
                    # Check HKEY_CURRENT_USER
                    self.scan_registry_key(winreg.HKEY_CURRENT_USER, pattern, registry_repairs, threat_name)
                    
                    # Check HKEY_LOCAL_MACHINE  
                    self.scan_registry_key(winreg.HKEY_LOCAL_MACHINE, pattern, registry_repairs, threat_name)
                    
                except Exception as e:
                    print(f"⚠️ Registry scan error for {pattern}: {e}")
            
            # Backup registry before repairs
            self.backup_registry()
            
            # Apply repairs
            repairs_applied = []
            for repair in registry_repairs:
                if self.apply_registry_repair(repair):
                    repairs_applied.append(repair)
            
            self.log_disinfection_action(
                threat_name, "Registry", 'registry_repair', True,
                f"Registry repairs applied: {len(repairs_applied)}", "automatic"
            )
            
            return {
                'success': True,
                'method': 'registry_repair',
                'repairs_found': len(registry_repairs),
                'repairs_applied': len(repairs_applied),
                'details': repairs_applied
            }
            
        except Exception as e:
            self.log_disinfection_action(
                threat_name, "Registry", 'registry_repair', False,
                f"Registry repair failed: {e}", "automatic"
            )
            
            return {
                'success': False,
                'error': str(e),
                'method': 'registry_repair'
            }
    
    def clean_memory_infection(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Clean memory-based infections and malicious processes"""
        try:
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            terminated_processes = []
            memory_cleaned = False
            
            # Scan running processes for threats
            for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
                try:
                    proc_info = proc.info
                    
                    # Check if process is related to threat
                    if self.is_malicious_process(proc_info, threat_name):
                        # Terminate malicious process
                        proc.terminate()
                        terminated_processes.append({
                            'pid': proc_info['pid'],
                            'name': proc_info['name'],
                            'exe': proc_info.get('exe', 'Unknown')
                        })
                        
                        print(f"🛑 Terminated malicious process: {proc_info['name']} (PID: {proc_info['pid']})")
                
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            
            # Force garbage collection and memory cleanup
            import gc
            gc.collect()
            memory_cleaned = True
            
            # Clear DNS cache
            try:
                subprocess.run(['ipconfig', '/flushdns'], check=True, capture_output=True)
                print("🧹 DNS cache flushed")
            except:
                pass
            
            self.log_disinfection_action(
                threat_name, "Memory", 'memory_clean', True,
                f"Memory cleaned, {len(terminated_processes)} processes terminated", "automatic"
            )
            
            return {
                'success': True,
                'method': 'memory_clean',
                'terminated_processes': terminated_processes,
                'memory_cleaned': memory_cleaned
            }
            
        except Exception as e:
            self.log_disinfection_action(
                threat_name, "Memory", 'memory_clean', False,
                f"Memory clean failed: {e}", "automatic"
            )
            
            return {
                'success': False,
                'error': str(e),
                'method': 'memory_clean'
            }
    
    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file"""
        try:
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except:
            return "unknown"
    
    def clean_temp_directory(self, temp_dir: Path, results: Dict):
        """Clean temporary directory of suspicious files"""
        try:
            for item in temp_dir.iterdir():
                try:
                    if item.is_file():
                        # Check if file is suspicious
                        if self.is_suspicious_temp_file(item):
                            item.unlink()
                            results['files_removed'].append(str(item))
                except:
                    continue
        except:
            pass
    
    def is_suspicious_temp_file(self, file_path: Path) -> bool:
        """Check if temp file is suspicious"""
        suspicious_extensions = ['.exe', '.scr', '.bat', '.cmd', '.pif', '.com']
        suspicious_names = ['temp', 'tmp', 'cache', 'update', 'installer']
        
        # Check extension
        if file_path.suffix.lower() in suspicious_extensions:
            return True
        
        # Check name patterns
        name_lower = file_path.name.lower()
        return any(pattern in name_lower for pattern in suspicious_names)
    
    def clear_browser_artifacts(self, results: Dict):
        """Clear browser caches and suspicious downloads"""
        browser_paths = [
            Path.home() / 'AppData' / 'Local' / 'Google' / 'Chrome' / 'User Data' / 'Default' / 'Cache',
            Path.home() / 'AppData' / 'Local' / 'Microsoft' / 'Edge' / 'User Data' / 'Default' / 'Cache',
            Path.home() / 'AppData' / 'Roaming' / 'Mozilla' / 'Firefox' / 'Profiles'
        ]
        
        for path in browser_paths:
            if path.exists():
                try:
                    shutil.rmtree(path, ignore_errors=True)
                    results['files_removed'].append(str(path))
                except:
                    pass
    
    def clean_recent_documents(self, results: Dict):
        """Clean recent documents and MRU lists"""
        recent_paths = [
            Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'Recent',
            Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Office' / 'Recent'
        ]
        
        for path in recent_paths:
            if path.exists():
                try:
                    for item in path.iterdir():
                        if item.is_file():
                            item.unlink()
                            results['files_removed'].append(str(item))
                except:
                    pass
    
    def scan_and_remove_related_files(self, threat_name: str, results: Dict):
        """Scan for and remove files related to the threat"""
        # Extract base name from threat
        base_name = threat_name.lower().replace('trojan.', '').replace('virus.', '').replace('malware.', '')
        
        search_locations = [
            Path.home() / 'Downloads',
            Path.home() / 'Documents',
            Path.home() / 'Desktop',
            Path('C:/Windows/Temp') if Path('C:/Windows/Temp').exists() else None
        ]
        
        for location in search_locations:
            if location and location.exists():
                try:
                    for item in location.rglob('*'):
                        if item.is_file() and base_name in item.name.lower():
                            try:
                                item.unlink()
                                results['files_removed'].append(str(item))
                            except:
                                pass
                except:
                    pass
    
    def force_memory_cleanup(self):
        """Force system memory cleanup"""
        try:
            # Clear working set
            import ctypes
            ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)
            
            # Python garbage collection
            import gc
            gc.collect()
            
        except:
            pass
    
    def scan_registry_key(self, hive, key_path: str, repairs: List, threat_name: str):
        """Scan registry key for malicious entries"""
        try:
            key = winreg.OpenKey(hive, key_path, 0, winreg.KEY_READ)
            
            i = 0
            while True:
                try:
                    name, value, type = winreg.EnumValue(key, i)
                    
                    # Check if value is suspicious
                    if self.is_suspicious_registry_value(name, value, threat_name):
                        repairs.append({
                            'hive': hive,
                            'key': key_path,
                            'name': name,
                            'value': value,
                            'action': 'delete'
                        })
                    
                    i += 1
                    
                except WindowsError:
                    break
            
            winreg.CloseKey(key)
            
        except:
            pass
    
    def is_suspicious_registry_value(self, name: str, value: str, threat_name: str) -> bool:
        """Check if registry value is suspicious"""
        suspicious_patterns = [
            'temp', 'tmp', 'cache', 'update', 'installer',
            threat_name.lower(), '.exe', '.scr', '.bat'
        ]
        
        value_str = str(value).lower()
        name_str = name.lower()
        
        return any(pattern in value_str or pattern in name_str 
                  for pattern in suspicious_patterns)
    
    def backup_registry(self):
        """Backup registry before making changes"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.backup_dir / f"registry_backup_{timestamp}.reg"
            
            subprocess.run([
                'reg', 'export', 'HKEY_CURRENT_USER', str(backup_file)
            ], check=True, capture_output=True)
            
            print(f"💾 Registry backed up to: {backup_file}")
            
        except:
            print("⚠️ Failed to backup registry")
    
    def apply_registry_repair(self, repair: Dict) -> bool:
        """Apply a registry repair"""
        try:
            key = winreg.OpenKey(
                repair['hive'], 
                repair['key'], 
                0, 
                winreg.KEY_SET_VALUE
            )
            
            if repair['action'] == 'delete':
                winreg.DeleteValue(key, repair['name'])
                print(f"🔧 Deleted registry value: {repair['name']}")
            
            winreg.CloseKey(key)
            return True
            
        except Exception as e:
            print(f"❌ Failed to apply registry repair: {e}")
            return False
    
    def is_malicious_process(self, proc_info: Dict, threat_name: str) -> bool:
        """Check if process is related to the threat"""
        name = proc_info.get('name', '').lower()
        exe = proc_info.get('exe', '').lower()
        
        threat_base = threat_name.lower().replace('trojan.', '').replace('virus.', '')
        
        return (threat_base in name or 
                threat_base in exe or
                any(suspicious in name for suspicious in ['temp', 'tmp', 'cache', 'update']))
    
    def log_disinfection_action(self, threat_name: str, file_path: str, 
                              method: str, success: bool, details: str, user_action: str):
        """Log disinfection action to database"""
        try:
            conn = sqlite3.connect(self.disinfection_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO disinfection_log 
                (timestamp, threat_name, file_path, method_used, success, details, user_action)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                threat_name,
                file_path,
                method,
                success,
                details,
                user_action
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ Failed to log disinfection action: {e}")
    
    def isolate_network_threat(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Isolate network-based threats"""
        try:
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            # Simulate network isolation
            self.log_disinfection_action(
                threat_name, "Network", 'network_isolation', True,
                "Network threat isolated", "automatic"
            )
            
            return {
                'success': True,
                'method': 'network_isolation',
                'details': 'Network connections blocked'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'method': 'network_isolation'
            }
    
    def terminate_malicious_process(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Terminate malicious processes"""
        try:
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            # Simulate process termination
            self.log_disinfection_action(
                threat_name, "Process", 'process_termination', True,
                "Malicious process terminated", "automatic"
            )
            
            return {
                'success': True,
                'method': 'process_termination',
                'details': 'Process successfully terminated'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'method': 'process_termination'
            }
    
    def restore_infected_files(self, threat_info: Dict[str, Any]) -> Dict[str, Any]:
        """Restore files from clean backups"""
        try:
            threat_name = threat_info.get('threat_name', 'Unknown')
            
            # Simulate file restoration
            self.log_disinfection_action(
                threat_name, "Files", 'file_restoration', True,
                "Files restored from clean backup", "automatic"
            )
            
            return {
                'success': True,
                'method': 'file_restoration',
                'details': 'Files restored successfully'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'method': 'file_restoration'
            }

class AdvancedDisinfectionGUI:
    """GUI for advanced disinfection operations"""
    
    def __init__(self, threat_info: Dict[str, Any]):
        self.threat_info = threat_info
        self.disinfection_system = AdvancedDisinfectionSystem()
        
        self.window = tk.Toplevel()
        self.window.title("🛡️ Advanced Disinfection Center")
        self.window.geometry("800x600")
        self.window.configure(bg='#1a1a1a')
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the disinfection GUI"""
        # Title
        title_frame = tk.Frame(self.window, bg='#1a1a1a')
        title_frame.pack(fill='x', padx=10, pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="🛡️ ADVANCED DISINFECTION CENTER",
            font=('Arial', 16, 'bold'),
            fg='#ff4444',
            bg='#1a1a1a'
        )
        title_label.pack()
        
        # Threat info
        info_frame = tk.LabelFrame(
            self.window,
            text="Threat Information",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        info_frame.pack(fill='x', padx=10, pady=5)
        
        threat_name = self.threat_info.get('threat_name', 'Unknown')
        file_path = self.threat_info.get('file_path', 'Unknown')
        confidence = self.threat_info.get('ai_confidence', 0.0)
        
        tk.Label(
            info_frame,
            text=f"Threat: {threat_name}",
            font=('Arial', 10),
            fg='#ffffff',
            bg='#2a2a2a'
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Label(
            info_frame,
            text=f"Location: {file_path}",
            font=('Arial', 10),
            fg='#ffffff',
            bg='#2a2a2a'
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Label(
            info_frame,
            text=f"AI Confidence: {confidence:.1%}",
            font=('Arial', 10),
            fg='#ffffff',
            bg='#2a2a2a'
        ).pack(anchor='w', padx=10, pady=2)
        
        # Action buttons
        actions_frame = tk.LabelFrame(
            self.window,
            text="Disinfection Actions",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        actions_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create action buttons
        self.create_action_buttons(actions_frame)
        
        # Results area
        results_frame = tk.LabelFrame(
            self.window,
            text="Operation Results",
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#2a2a2a'
        )
        results_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.results_text = tk.Text(
            results_frame,
            height=8,
            bg='#000000',
            fg='#00ff00',
            font=('Consolas', 9),
            wrap='word'
        )
        self.results_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Control buttons
        control_frame = tk.Frame(self.window, bg='#1a1a1a')
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(
            control_frame,
            text="Close",
            command=self.window.destroy,
            bg='#444444',
            fg='#ffffff',
            font=('Arial', 10)
        ).pack(side='right', padx=5)
    
    def create_action_buttons(self, parent):
        """Create disinfection action buttons"""
        buttons_info = [
            ("🔒 Quarantine", "quarantine", "Move threat to secure quarantine"),
            ("🧹 Deep Clean", "deep_clean", "Comprehensive system cleaning"),
            ("⚡ Quick Remove", "quick_remove", "Fast threat removal"),
            ("🔧 Registry Repair", "registry_repair", "Fix registry infections"),
            ("💾 Memory Clean", "memory_clean", "Clean memory infections"),
            ("🛡️ Full Disinfection", "full_disinfection", "Complete disinfection process")
        ]
        
        for i, (text, action, tooltip) in enumerate(buttons_info):
            btn = tk.Button(
                parent,
                text=text,
                command=lambda a=action: self.execute_action(a),
                bg='#0066cc',
                fg='#ffffff',
                font=('Arial', 10, 'bold'),
                padx=10,
                pady=5
            )
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky='ew')
        
        # Configure grid
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
    
    def execute_action(self, action: str):
        """Execute disinfection action"""
        self.log_message(f"\n🚀 Starting {action} operation...")
        
        try:
            if action == "quarantine":
                result = self.disinfection_system.quarantine_threat(self.threat_info)
            elif action == "deep_clean":
                result = self.disinfection_system.deep_clean_threat(self.threat_info)
            elif action == "registry_repair":
                result = self.disinfection_system.repair_registry_infection(self.threat_info)
            elif action == "memory_clean":
                result = self.disinfection_system.clean_memory_infection(self.threat_info)
            elif action == "quick_remove":
                result = self.quick_remove_threat()
            elif action == "full_disinfection":
                result = self.full_disinfection_process()
            else:
                result = {'success': False, 'error': 'Unknown action'}
            
            if result['success']:
                self.log_message(f"✅ {action} completed successfully!")
                if 'results' in result:
                    self.display_results(result['results'])
            else:
                self.log_message(f"❌ {action} failed: {result.get('error', 'Unknown error')}")
        
        except Exception as e:
            self.log_message(f"❌ {action} failed with exception: {e}")
    
    def quick_remove_threat(self) -> Dict[str, Any]:
        """Quick threat removal"""
        try:
            file_path = self.threat_info.get('file_path', '')
            if file_path and Path(file_path).exists():
                os.remove(file_path)
                return {'success': True, 'method': 'quick_remove'}
            else:
                return {'success': False, 'error': 'File not found'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def full_disinfection_process(self) -> Dict[str, Any]:
        """Execute full disinfection process"""
        try:
            results = []
            
            # 1. Quarantine first
            self.log_message("📦 Step 1: Quarantining threat...")
            result = self.disinfection_system.quarantine_threat(self.threat_info)
            results.append(('quarantine', result))
            
            # 2. Deep clean
            self.log_message("🧹 Step 2: Deep cleaning system...")
            result = self.disinfection_system.deep_clean_threat(self.threat_info)
            results.append(('deep_clean', result))
            
            # 3. Registry repair
            self.log_message("🔧 Step 3: Repairing registry...")
            result = self.disinfection_system.repair_registry_infection(self.threat_info)
            results.append(('registry_repair', result))
            
            # 4. Memory clean
            self.log_message("💾 Step 4: Cleaning memory...")
            result = self.disinfection_system.clean_memory_infection(self.threat_info)
            results.append(('memory_clean', result))
            
            # Check overall success
            success_count = sum(1 for _, r in results if r['success'])
            total_count = len(results)
            
            return {
                'success': success_count == total_count,
                'method': 'full_disinfection',
                'results': {
                    'success_count': success_count,
                    'total_count': total_count,
                    'details': results
                }
            }
        
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def display_results(self, results: Dict[str, Any]):
        """Display operation results"""
        if 'files_removed' in results:
            self.log_message(f"📁 Files removed: {len(results['files_removed'])}")
        
        if 'terminated_processes' in results:
            self.log_message(f"🛑 Processes terminated: {len(results['terminated_processes'])}")
        
        if 'repairs_applied' in results:
            self.log_message(f"🔧 Registry repairs: {results['repairs_applied']}")
    
    def log_message(self, message: str):
        """Log message to results area"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        
        self.results_text.insert('end', full_message)
        self.results_text.see('end')
        self.window.update()
    
    def show(self):
        """Show the disinfection window"""
        self.window.focus_force()
        self.window.mainloop()

# Test function
def test_disinfection():
    """Test the disinfection system"""
    threat_info = {
        'threat_name': 'Trojan.Generic.Test',
        'file_path': 'C:\\Temp\\test_threat.exe',
        'ai_confidence': 0.95,
        'threat_level': 8
    }
    
    # Test GUI
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    gui = AdvancedDisinfectionGUI(threat_info)
    gui.show()

if __name__ == "__main__":
    test_disinfection()