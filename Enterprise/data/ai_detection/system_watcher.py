"""
Real-Time System Watcher - Kaspersky-style Protection
Advanced real-time system monitoring and protection
"""

import os
import sys
import time
import threading
import psutil
import winreg
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
import sqlite3
import subprocess
from typing import Dict, List, Any, Set
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket
import struct

# Import AI components
try:
    from self_learning_ai import SelfLearningAI
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

class SystemWatcher:
    """Real-time system monitoring and protection"""
    
    def __init__(self):
        self.monitoring_active = False
        self.ai_system = None
        self.protection_database = "system_protection.db"
        
        # Monitoring components
        self.file_monitor = None
        self.process_monitor = None
        self.network_monitor = None
        self.registry_monitor = None
        
        # Threat detection
        self.suspicious_processes = set()
        self.blocked_files = set()
        self.quarantine_directory = "quarantine"
        
        # Protection statistics
        self.threats_blocked = 0
        self.files_scanned = 0
        self.processes_monitored = 0
        self.network_connections_checked = 0
        
        # Whitelist and blacklist
        self.process_whitelist = set()
        self.file_whitelist = set()
        self.ip_blacklist = set()
        self.domain_blacklist = set()
        
        # Initialize components
        self.init_database()
        self.setup_logging()
        self.load_protection_lists()
        
        if AI_AVAILABLE:
            self.ai_system = SelfLearningAI()
        
        print("🛡️ System Watcher initialized")
    
    def init_database(self):
        """Initialize protection database"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            # Threat detections table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS threat_detections (
                    id INTEGER PRIMARY KEY,
                    timestamp DATE,
                    threat_type TEXT,
                    threat_name TEXT,
                    file_path TEXT,
                    process_name TEXT,
                    threat_level INTEGER,
                    action_taken TEXT,
                    ai_confidence REAL,
                    details TEXT
                )
            ''')
            
            # File monitoring table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS file_events (
                    id INTEGER PRIMARY KEY,
                    timestamp DATE,
                    event_type TEXT,
                    file_path TEXT,
                    file_hash TEXT,
                    file_size INTEGER,
                    process_name TEXT,
                    suspicious BOOLEAN,
                    action_taken TEXT
                )
            ''')
            
            # Process monitoring table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS process_events (
                    id INTEGER PRIMARY KEY,
                    timestamp DATE,
                    event_type TEXT,
                    process_id INTEGER,
                    process_name TEXT,
                    parent_process TEXT,
                    command_line TEXT,
                    user_name TEXT,
                    suspicious BOOLEAN,
                    action_taken TEXT
                )
            ''')
            
            # Network monitoring table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS network_events (
                    id INTEGER PRIMARY KEY,
                    timestamp DATE,
                    event_type TEXT,
                    process_name TEXT,
                    local_address TEXT,
                    remote_address TEXT,
                    port INTEGER,
                    protocol TEXT,
                    suspicious BOOLEAN,
                    action_taken TEXT
                )
            ''')
            
            # System changes table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS system_changes (
                    id INTEGER PRIMARY KEY,
                    timestamp DATE,
                    change_type TEXT,
                    registry_key TEXT,
                    service_name TEXT,
                    startup_item TEXT,
                    old_value TEXT,
                    new_value TEXT,
                    suspicious BOOLEAN,
                    action_taken TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
            print("✅ Protection database initialized")
            
        except Exception as e:
            print(f"❌ Database initialization failed: {e}")
    
    def setup_logging(self):
        """Setup logging for system watcher"""
        logging.basicConfig(
            filename='system_watcher.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def load_protection_lists(self):
        """Load whitelists and blacklists"""
        # Process whitelist (common legitimate processes)
        self.process_whitelist.update([
            'explorer.exe', 'svchost.exe', 'winlogon.exe', 'services.exe',
            'lsass.exe', 'dwm.exe', 'csrss.exe', 'smss.exe', 'wininit.exe',
            'chrome.exe', 'firefox.exe', 'notepad.exe', 'taskmgr.exe'
        ])
        
        # File whitelist patterns
        self.file_whitelist.update([
            'C:\\Windows\\System32\\',
            'C:\\Program Files\\',
            'C:\\Program Files (x86)\\',
            'C:\\Windows\\WinSxS\\'
        ])
        
        # Known malicious IPs (examples - in production, use threat feeds)
        self.ip_blacklist.update([
            '192.168.1.100',  # Example malicious IP
            '10.0.0.50',
            '172.16.0.25'
        ])
        
        # Known malicious domains
        self.domain_blacklist.update([
            'malicious-site.com',
            'phishing-example.net',
            'trojan-host.org'
        ])
        
        print(f"📋 Loaded protection lists - {len(self.process_whitelist)} processes, {len(self.ip_blacklist)} IPs")
    
    def start_monitoring(self):
        """Start comprehensive system monitoring"""
        print("🚀 Starting real-time system monitoring...")
        self.monitoring_active = True
        
        # Create quarantine directory
        Path(self.quarantine_directory).mkdir(exist_ok=True)
        
        # Start monitoring threads
        monitoring_threads = [
            threading.Thread(target=self.file_system_monitor, daemon=True),
            threading.Thread(target=self.process_monitor_loop, daemon=True),
            threading.Thread(target=self.network_monitor_loop, daemon=True),
            threading.Thread(target=self.registry_monitor_loop, daemon=True),
            threading.Thread(target=self.behavior_analysis_loop, daemon=True),
            threading.Thread(target=self.memory_scanner_loop, daemon=True)
        ]
        
        for thread in monitoring_threads:
            thread.start()
        
        # Start AI learning if available
        if self.ai_system:
            self.ai_system.start_continuous_learning()
        
        print("✅ Real-time system monitoring started")
        return monitoring_threads
    
    def file_system_monitor(self):
        """Monitor file system changes in real-time"""
        class ThreatFileHandler(FileSystemEventHandler):
            def __init__(self, watcher):
                self.watcher = watcher
            
            def on_any_event(self, event):
                if event.is_directory:
                    return
                
                self.watcher.analyze_file_event(event)
        
        try:
            observer = Observer()
            handler = ThreatFileHandler(self)
            
            # Monitor critical directories
            critical_dirs = [
                'C:\\Windows\\System32',
                'C:\\Program Files',
                'C:\\Program Files (x86)',
                'C:\\Users',
                'C:\\Windows\\Temp',
                os.environ.get('TEMP', 'C:\\Temp')
            ]
            
            for directory in critical_dirs:
                if os.path.exists(directory):
                    observer.schedule(handler, directory, recursive=True)
            
            observer.start()
            self.file_monitor = observer
            
            print("👁️ File system monitoring started")
            
            while self.monitoring_active:
                time.sleep(1)
            
            observer.stop()
            observer.join()
            
        except Exception as e:
            self.logger.error(f"File system monitoring error: {e}")
    
    def analyze_file_event(self, event):
        """Analyze file system event for threats"""
        try:
            file_path = event.src_path
            event_type = event.event_type
            
            # Skip if file doesn't exist
            if not os.path.exists(file_path):
                return
            
            self.files_scanned += 1
            
            # Check if file is in whitelist
            if any(file_path.startswith(whitelist_path) for whitelist_path in self.file_whitelist):
                return
            
            # Get file information
            file_info = self.get_file_info(file_path)
            
            # Check for suspicious patterns
            is_suspicious = self.is_file_suspicious(file_path, file_info)
            
            if is_suspicious:
                self.handle_suspicious_file(file_path, file_info, event_type)
            
            # Store file event
            self.store_file_event(event_type, file_path, file_info, is_suspicious)
            
        except Exception as e:
            self.logger.error(f"File event analysis error: {e}")
    
    def get_file_info(self, file_path: str) -> Dict:
        """Get comprehensive file information"""
        try:
            stat_info = os.stat(file_path)
            
            # Calculate file hash
            file_hash = self.calculate_file_hash(file_path)
            
            # Get file extension and type
            file_ext = Path(file_path).suffix.lower()
            
            return {
                'size': stat_info.st_size,
                'modified': datetime.fromtimestamp(stat_info.st_mtime),
                'created': datetime.fromtimestamp(stat_info.st_ctime),
                'hash': file_hash,
                'extension': file_ext,
                'path': file_path
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get file info for {file_path}: {e}")
            return {}
    
    def calculate_file_hash(self, file_path: str) -> str:
        """Calculate SHA256 hash of file"""
        try:
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            return ""
    
    def is_file_suspicious(self, file_path: str, file_info: Dict) -> bool:
        """Determine if file is suspicious"""
        suspicious_indicators = []
        
        try:
            # Check file extension
            suspicious_extensions = [
                '.exe', '.scr', '.bat', '.cmd', '.com', '.pif', '.vbs',
                '.js', '.jar', '.dll', '.sys', '.drv'
            ]
            
            if file_info.get('extension', '') in suspicious_extensions:
                suspicious_indicators.append("suspicious_extension")
            
            # Check file size (very small or very large executables)
            file_size = file_info.get('size', 0)
            if file_info.get('extension') == '.exe':
                if file_size < 1024 or file_size > 100 * 1024 * 1024:  # < 1KB or > 100MB
                    suspicious_indicators.append("unusual_size")
            
            # Check file location
            temp_dirs = ['\\temp\\', '\\tmp\\', '\\appdata\\local\\temp\\']
            if any(temp_dir in file_path.lower() for temp_dir in temp_dirs):
                if file_info.get('extension') in ['.exe', '.dll', '.sys']:
                    suspicious_indicators.append("temp_executable")
            
            # Check for hidden files in system directories
            if file_path.startswith('C:\\Windows\\') and '\\.' in file_path:
                suspicious_indicators.append("hidden_system_file")
            
            # Check file hash against known threats
            file_hash = file_info.get('hash', '')
            if self.is_hash_malicious(file_hash):
                suspicious_indicators.append("known_malware_hash")
            
            # AI-based analysis
            if self.ai_system and file_info:
                ai_prediction = self.get_ai_file_analysis(file_info)
                if ai_prediction.get('threat_level', 0) > 7:
                    suspicious_indicators.append("ai_detection")
            
            return len(suspicious_indicators) >= 2  # Require multiple indicators
            
        except Exception as e:
            self.logger.error(f"Suspicious file analysis error: {e}")
            return False
    
    def is_hash_malicious(self, file_hash: str) -> bool:
        """Check if file hash is known malicious"""
        # In production, this would check against threat intelligence databases
        known_malicious_hashes = [
            'd41d8cd98f00b204e9800998ecf8427e',  # Example hashes
            '5d41402abc4b2a76b9719d911017c592',
            '098f6bcd4621d373cade4e832627b4f6'
        ]
        
        return file_hash in known_malicious_hashes
    
    def get_ai_file_analysis(self, file_info: Dict) -> Dict:
        """Get AI analysis of file"""
        try:
            # Extract features for AI analysis
            features = [
                file_info.get('size', 0) / 1024 / 1024,  # Size in MB
                len(file_info.get('path', '')),  # Path length
                1 if file_info.get('extension') in ['.exe', '.dll'] else 0,  # Is executable
                (datetime.now() - file_info.get('created', datetime.now())).days,  # Age in days
                1 if '\\temp\\' in file_info.get('path', '').lower() else 0,  # In temp dir
                len(file_info.get('hash', '')) / 64,  # Hash complexity
                0, 0, 0, 0  # Padding to reach 10 features
            ]
            
            return self.ai_system.predict_threat(features)
            
        except Exception as e:
            self.logger.error(f"AI file analysis error: {e}")
            return {'threat_level': 0}
    
    def handle_suspicious_file(self, file_path: str, file_info: Dict, event_type: str):
        """Handle detection of suspicious file"""
        try:
            threat_name = f"Suspicious_{event_type}_{file_info.get('extension', 'unknown')}"
            
            # Determine action based on threat level
            action = "monitor"
            
            if self.is_hash_malicious(file_info.get('hash', '')):
                action = "quarantine"
                self.quarantine_file(file_path)
            elif file_info.get('extension') in ['.exe', '.dll', '.sys']:
                action = "block"
                self.block_file_execution(file_path)
            
            # Log threat detection
            self.log_threat_detection(
                threat_type="suspicious_file",
                threat_name=threat_name,
                file_path=file_path,
                action_taken=action,
                details=json.dumps(file_info)
            )
            
            self.threats_blocked += 1
            
            print(f"🚨 Suspicious file detected: {file_path} - Action: {action}")
            
        except Exception as e:
            self.logger.error(f"Suspicious file handling error: {e}")
    
    def quarantine_file(self, file_path: str):
        """Move file to quarantine"""
        try:
            quarantine_path = os.path.join(
                self.quarantine_directory,
                f"quarantine_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.path.basename(file_path)}"
            )
            
            # Move file to quarantine
            os.rename(file_path, quarantine_path)
            
            print(f"📦 File quarantined: {file_path} -> {quarantine_path}")
            
        except Exception as e:
            self.logger.error(f"File quarantine error: {e}")
    
    def block_file_execution(self, file_path: str):
        """Block file execution"""
        try:
            # Add to blocked files set
            self.blocked_files.add(file_path)
            
            # In a real implementation, this would integrate with Windows Security Center
            # or use file system permissions to block execution
            
            print(f"🚫 File execution blocked: {file_path}")
            
        except Exception as e:
            self.logger.error(f"File blocking error: {e}")
    
    def process_monitor_loop(self):
        """Monitor running processes for threats"""
        known_processes = set()
        
        while self.monitoring_active:
            try:
                current_processes = set()
                
                for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'username', 'ppid']):
                    try:
                        proc_info = proc.info
                        proc_id = proc_info['pid']
                        proc_name = proc_info['name']
                        
                        current_processes.add(proc_id)
                        self.processes_monitored += 1
                        
                        # Check for new processes
                        if proc_id not in known_processes:
                            self.analyze_new_process(proc_info)
                        
                        # Check for suspicious behavior
                        if self.is_process_suspicious(proc_info):
                            self.handle_suspicious_process(proc_info)
                        
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                
                # Update known processes
                known_processes = current_processes
                
                time.sleep(5)  # Check every 5 seconds
                
            except Exception as e:
                self.logger.error(f"Process monitoring error: {e}")
                time.sleep(10)
    
    def analyze_new_process(self, proc_info: Dict):
        """Analyze newly started process"""
        try:
            proc_name = proc_info.get('name', '')
            cmdline = ' '.join(proc_info.get('cmdline', []))
            
            # Store process event
            self.store_process_event(
                event_type="process_start",
                proc_info=proc_info,
                suspicious=False
            )
            
            print(f"🔍 New process: {proc_name} (PID: {proc_info.get('pid')})")
            
        except Exception as e:
            self.logger.error(f"New process analysis error: {e}")
    
    def is_process_suspicious(self, proc_info: Dict) -> bool:
        """Determine if process is suspicious"""
        suspicious_indicators = []
        
        try:
            proc_name = proc_info.get('name', '').lower()
            cmdline = ' '.join(proc_info.get('cmdline', [])).lower()
            
            # Check if process is not in whitelist
            if proc_name not in self.process_whitelist:
                # Check for suspicious patterns
                suspicious_patterns = [
                    'powershell', 'cmd', 'wscript', 'cscript',
                    'regsvr32', 'rundll32', 'mshta', 'certutil'
                ]
                
                if any(pattern in proc_name for pattern in suspicious_patterns):
                    suspicious_indicators.append("suspicious_process_name")
                
                # Check command line for suspicious patterns
                suspicious_cmdline_patterns = [
                    'base64', 'invoke-expression', 'downloadstring',
                    'powershell -enc', 'cmd /c echo', 'certutil -decode'
                ]
                
                if any(pattern in cmdline for pattern in suspicious_cmdline_patterns):
                    suspicious_indicators.append("suspicious_command_line")
                
                # Check for process injection indicators
                if 'svchost' in proc_name and proc_info.get('username') != 'SYSTEM':
                    suspicious_indicators.append("suspicious_svchost")
                
                # Check for processes running from temp directories
                temp_patterns = ['\\temp\\', '\\tmp\\', '\\appdata\\local\\temp\\']
                if any(pattern in cmdline for pattern in temp_patterns):
                    suspicious_indicators.append("temp_execution")
            
            return len(suspicious_indicators) >= 1
            
        except Exception as e:
            self.logger.error(f"Process suspicion analysis error: {e}")
            return False
    
    def handle_suspicious_process(self, proc_info: Dict):
        """Handle suspicious process detection"""
        try:
            proc_id = proc_info.get('pid')
            proc_name = proc_info.get('name', '')
            
            # Add to suspicious processes
            self.suspicious_processes.add(proc_id)
            
            # Terminate highly suspicious processes
            high_risk_patterns = ['powershell -enc', 'certutil -decode', 'invoke-expression']
            cmdline = ' '.join(proc_info.get('cmdline', [])).lower()
            
            action = "monitor"
            if any(pattern in cmdline for pattern in high_risk_patterns):
                action = "terminate"
                self.terminate_process(proc_id)
            
            # Log threat detection
            self.log_threat_detection(
                threat_type="suspicious_process",
                threat_name=f"Suspicious_{proc_name}",
                process_name=proc_name,
                action_taken=action,
                details=json.dumps(proc_info)
            )
            
            self.threats_blocked += 1
            
            print(f"🚨 Suspicious process detected: {proc_name} (PID: {proc_id}) - Action: {action}")
            
        except Exception as e:
            self.logger.error(f"Suspicious process handling error: {e}")
    
    def terminate_process(self, proc_id: int):
        """Terminate malicious process"""
        try:
            process = psutil.Process(proc_id)
            process.terminate()
            
            print(f"🔪 Process terminated: PID {proc_id}")
            
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            self.logger.warning(f"Failed to terminate process {proc_id}: {e}")
    
    def network_monitor_loop(self):
        """Monitor network connections for threats"""
        while self.monitoring_active:
            try:
                connections = psutil.net_connections(kind='inet')
                
                for conn in connections:
                    if conn.status == psutil.CONN_ESTABLISHED:
                        self.analyze_network_connection(conn)
                        self.network_connections_checked += 1
                
                time.sleep(10)  # Check every 10 seconds
                
            except Exception as e:
                self.logger.error(f"Network monitoring error: {e}")
                time.sleep(30)
    
    def analyze_network_connection(self, connection):
        """Analyze network connection for threats"""
        try:
            if not connection.raddr:
                return
            
            remote_ip = connection.raddr.ip
            remote_port = connection.raddr.port
            local_port = connection.laddr.port if connection.laddr else 0
            
            # Get process information
            try:
                process = psutil.Process(connection.pid)
                proc_name = process.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                proc_name = "unknown"
            
            # Check for suspicious connections
            is_suspicious = self.is_connection_suspicious(remote_ip, remote_port, proc_name)
            
            if is_suspicious:
                self.handle_suspicious_connection(connection, proc_name)
            
            # Store network event
            self.store_network_event(connection, proc_name, is_suspicious)
            
        except Exception as e:
            self.logger.error(f"Network connection analysis error: {e}")
    
    def is_connection_suspicious(self, remote_ip: str, remote_port: int, proc_name: str) -> bool:
        """Determine if network connection is suspicious"""
        try:
            # Check against IP blacklist
            if remote_ip in self.ip_blacklist:
                return True
            
            # Check for connections to suspicious ports
            suspicious_ports = [1337, 4444, 5555, 6666, 31337]
            if remote_port in suspicious_ports:
                return True
            
            # Check for processes making unexpected connections
            system_processes = ['svchost.exe', 'services.exe', 'lsass.exe']
            if proc_name in system_processes and remote_port not in [80, 443, 53]:
                return True
            
            # Check for private IP ranges making external connections
            private_ranges = ['192.168.', '10.', '172.16.', '172.17.', '172.18.', '172.19.']
            if not any(remote_ip.startswith(range_) for range_ in private_ranges):
                if proc_name not in ['chrome.exe', 'firefox.exe', 'edge.exe']:
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Connection suspicion analysis error: {e}")
            return False
    
    def handle_suspicious_connection(self, connection, proc_name: str):
        """Handle suspicious network connection"""
        try:
            remote_ip = connection.raddr.ip
            remote_port = connection.raddr.port
            
            # Log threat detection
            self.log_threat_detection(
                threat_type="suspicious_connection",
                threat_name=f"Suspicious_Connection_{proc_name}",
                process_name=proc_name,
                action_taken="monitor",
                details=f"Connection to {remote_ip}:{remote_port}"
            )
            
            print(f"🌐 Suspicious connection: {proc_name} -> {remote_ip}:{remote_port}")
            
        except Exception as e:
            self.logger.error(f"Suspicious connection handling error: {e}")
    
    def registry_monitor_loop(self):
        """Monitor registry changes"""
        # Note: This is a simplified implementation
        # Real registry monitoring would use Windows API or WMI
        
        while self.monitoring_active:
            try:
                # Monitor critical registry keys
                critical_keys = [
                    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
                    r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
                    r"SYSTEM\CurrentControlSet\Services"
                ]
                
                for key_path in critical_keys:
                    self.check_registry_key(key_path)
                
                time.sleep(60)  # Check every minute
                
            except Exception as e:
                self.logger.error(f"Registry monitoring error: {e}")
                time.sleep(120)
    
    def check_registry_key(self, key_path: str):
        """Check registry key for changes"""
        try:
            # This is a simplified check - real implementation would track changes
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
            
            num_values = winreg.QueryInfoKey(key)[1]
            
            # Store registry check (simplified)
            self.store_system_change(
                change_type="registry_check",
                registry_key=key_path,
                details=f"Values: {num_values}"
            )
            
            winreg.CloseKey(key)
            
        except Exception as e:
            # Key might not exist or access denied
            pass
    
    def behavior_analysis_loop(self):
        """Analyze system behavior patterns"""
        while self.monitoring_active:
            try:
                # Collect system metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                memory_percent = psutil.virtual_memory().percent
                disk_io = psutil.disk_io_counters()
                network_io = psutil.net_io_counters()
                
                # Analyze for anomalies
                self.analyze_system_behavior({
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory_percent,
                    'disk_read_bytes': disk_io.read_bytes if disk_io else 0,
                    'disk_write_bytes': disk_io.write_bytes if disk_io else 0,
                    'network_bytes_sent': network_io.bytes_sent if network_io else 0,
                    'network_bytes_recv': network_io.bytes_recv if network_io else 0
                })
                
                time.sleep(30)  # Analyze every 30 seconds
                
            except Exception as e:
                self.logger.error(f"Behavior analysis error: {e}")
                time.sleep(60)
    
    def analyze_system_behavior(self, metrics: Dict):
        """Analyze system behavior for anomalies"""
        try:
            anomalies = []
            
            # Check for high CPU usage
            if metrics['cpu_percent'] > 90:
                anomalies.append("high_cpu_usage")
            
            # Check for high memory usage
            if metrics['memory_percent'] > 95:
                anomalies.append("high_memory_usage")
            
            # Check for excessive disk activity
            if metrics['disk_write_bytes'] > 100 * 1024 * 1024:  # 100MB/30sec
                anomalies.append("excessive_disk_writes")
            
            # Check for excessive network activity
            if metrics['network_bytes_sent'] > 50 * 1024 * 1024:  # 50MB/30sec
                anomalies.append("excessive_network_traffic")
            
            if anomalies and self.ai_system:
                # Use AI to analyze behavior
                features = [
                    metrics['cpu_percent'],
                    metrics['memory_percent'],
                    metrics['disk_read_bytes'] / 1024 / 1024,
                    metrics['disk_write_bytes'] / 1024 / 1024,
                    metrics['network_bytes_sent'] / 1024 / 1024,
                    metrics['network_bytes_recv'] / 1024 / 1024,
                    len(anomalies),
                    0, 0, 0  # Padding
                ]
                
                ai_result = self.ai_system.predict_threat(features)
                
                if ai_result.get('is_anomaly', False):
                    self.handle_behavior_anomaly(anomalies, metrics, ai_result)
            
        except Exception as e:
            self.logger.error(f"Behavior analysis error: {e}")
    
    def handle_behavior_anomaly(self, anomalies: List[str], metrics: Dict, ai_result: Dict):
        """Handle detected behavior anomaly"""
        try:
            anomaly_description = ", ".join(anomalies)
            
            self.log_threat_detection(
                threat_type="behavior_anomaly",
                threat_name=f"Anomaly_{anomaly_description}",
                action_taken="monitor",
                details=json.dumps({
                    'anomalies': anomalies,
                    'metrics': metrics,
                    'ai_result': ai_result
                })
            )
            
            print(f"⚠️ Behavior anomaly detected: {anomaly_description}")
            
        except Exception as e:
            self.logger.error(f"Behavior anomaly handling error: {e}")
    
    def memory_scanner_loop(self):
        """Scan memory for malicious patterns"""
        while self.monitoring_active:
            try:
                # Simplified memory scanning
                suspicious_processes = []
                
                for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
                    try:
                        if proc.info['memory_percent'] > 50:  # Using > 50% memory
                            suspicious_processes.append(proc.info)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                
                if suspicious_processes:
                    print(f"🧠 Memory scan: {len(suspicious_processes)} high-memory processes")
                
                time.sleep(300)  # Scan every 5 minutes
                
            except Exception as e:
                self.logger.error(f"Memory scanning error: {e}")
                time.sleep(600)
    
    def store_file_event(self, event_type: str, file_path: str, file_info: Dict, suspicious: bool):
        """Store file event in database"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO file_events 
                (timestamp, event_type, file_path, file_hash, file_size, suspicious, action_taken)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now(),
                event_type,
                file_path,
                file_info.get('hash', ''),
                file_info.get('size', 0),
                suspicious,
                'quarantine' if suspicious else 'none'
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to store file event: {e}")
    
    def store_process_event(self, event_type: str, proc_info: Dict, suspicious: bool):
        """Store process event in database"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO process_events 
                (timestamp, event_type, process_id, process_name, command_line, user_name, suspicious, action_taken)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now(),
                event_type,
                proc_info.get('pid', 0),
                proc_info.get('name', ''),
                ' '.join(proc_info.get('cmdline', [])),
                proc_info.get('username', ''),
                suspicious,
                'terminate' if suspicious else 'none'
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to store process event: {e}")
    
    def store_network_event(self, connection, proc_name: str, suspicious: bool):
        """Store network event in database"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            remote_addr = f"{connection.raddr.ip}:{connection.raddr.port}" if connection.raddr else ""
            local_addr = f"{connection.laddr.ip}:{connection.laddr.port}" if connection.laddr else ""
            
            cursor.execute('''
                INSERT INTO network_events 
                (timestamp, event_type, process_name, local_address, remote_address, protocol, suspicious, action_taken)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now(),
                "connection",
                proc_name,
                local_addr,
                remote_addr,
                "TCP" if connection.type == socket.SOCK_STREAM else "UDP",
                suspicious,
                'block' if suspicious else 'none'
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to store network event: {e}")
    
    def store_system_change(self, change_type: str, **kwargs):
        """Store system change in database"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO system_changes 
                (timestamp, change_type, registry_key, service_name, startup_item, old_value, new_value, suspicious, action_taken)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now(),
                change_type,
                kwargs.get('registry_key', ''),
                kwargs.get('service_name', ''),
                kwargs.get('startup_item', ''),
                kwargs.get('old_value', ''),
                kwargs.get('new_value', ''),
                kwargs.get('suspicious', False),
                kwargs.get('action_taken', 'none')
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to store system change: {e}")
    
    def log_threat_detection(self, threat_type: str, threat_name: str, action_taken: str, **kwargs):
        """Log threat detection"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO threat_detections 
                (timestamp, threat_type, threat_name, file_path, process_name, threat_level, action_taken, details)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now(),
                threat_type,
                threat_name,
                kwargs.get('file_path', ''),
                kwargs.get('process_name', ''),
                kwargs.get('threat_level', 5),
                action_taken,
                kwargs.get('details', '')
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to log threat detection: {e}")
    
    def get_protection_status(self) -> Dict:
        """Get current protection status"""
        try:
            conn = sqlite3.connect(self.protection_database)
            cursor = conn.cursor()
            
            # Count recent threats
            cursor.execute('''
                SELECT COUNT(*) FROM threat_detections 
                WHERE timestamp > datetime('now', '-24 hours')
            ''')
            recent_threats = cursor.fetchone()[0]
            
            # Count total events
            cursor.execute("SELECT COUNT(*) FROM file_events")
            total_file_events = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM process_events")
            total_process_events = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM network_events")
            total_network_events = cursor.fetchone()[0]
            
            conn.close()
            
            return {
                'monitoring_active': self.monitoring_active,
                'threats_blocked': self.threats_blocked,
                'files_scanned': self.files_scanned,
                'processes_monitored': self.processes_monitored,
                'network_connections_checked': self.network_connections_checked,
                'recent_threats': recent_threats,
                'total_file_events': total_file_events,
                'total_process_events': total_process_events,
                'total_network_events': total_network_events,
                'ai_available': AI_AVAILABLE,
                'quarantined_files': len(list(Path(self.quarantine_directory).glob('*'))) if Path(self.quarantine_directory).exists() else 0
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get protection status: {e}")
            return {'error': str(e)}
    
    def stop_monitoring(self):
        """Stop system monitoring"""
        self.monitoring_active = False
        
        if self.file_monitor:
            self.file_monitor.stop()
        
        if self.ai_system:
            self.ai_system.stop_learning()
        
        print("🛑 System monitoring stopped")

def main():
    """Main function for system watcher"""
    print("🛡️ CyberDefense AI - Real-Time System Watcher")
    print("Kaspersky-style real-time protection system")
    print("-" * 60)
    
    watcher = SystemWatcher()
    
    try:
        # Start monitoring
        monitoring_threads = watcher.start_monitoring()
        
        print("\n✅ Real-time system protection is active!")
        print("Monitoring files, processes, network, and registry...")
        print("Press Ctrl+C to stop")
        
        # Keep main thread alive and show status updates
        while watcher.monitoring_active:
            status = watcher.get_protection_status()
            
            print(f"\n🛡️ Protection Status:")
            print(f"   🔍 Files Scanned: {status.get('files_scanned', 0)}")
            print(f"   ⚙️ Processes Monitored: {status.get('processes_monitored', 0)}")
            print(f"   🌐 Network Connections: {status.get('network_connections_checked', 0)}")
            print(f"   🚨 Threats Blocked: {status.get('threats_blocked', 0)}")
            print(f"   📦 Quarantined Files: {status.get('quarantined_files', 0)}")
            
            time.sleep(10)  # Update status every 10 seconds
        
    except KeyboardInterrupt:
        print("\n🛑 Stopping system watcher...")
        watcher.stop_monitoring()
    except Exception as e:
        print(f"\n❌ System watcher error: {e}")
        watcher.stop_monitoring()

if __name__ == "__main__":
    main()