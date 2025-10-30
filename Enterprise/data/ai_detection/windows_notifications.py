"""
Windows Notification System for AI Protection
Advanced notification system with action buttons
"""

import os
import sys
import time
import threading
from datetime import datetime
import subprocess
import json
from pathlib import Path
from typing import Dict, Any, Optional

# Windows notification imports
try:
    import win10toast
    from plyer import notification
    NOTIFICATIONS_AVAILABLE = True
except ImportError:
    print("⚠️ Notification libraries not available. Install win10toast and plyer for full functionality.")
    NOTIFICATIONS_AVAILABLE = False

# Windows API imports for system integration
try:
    import winreg
    import ctypes
    from ctypes import wintypes, windll
    WINDOWS_API_AVAILABLE = True
except ImportError:
    WINDOWS_API_AVAILABLE = False

class WindowsNotificationSystem:
    """Advanced Windows notification system with action buttons"""
    
    def __init__(self):
        self.notification_history = []
        self.toaster = None
        self.notification_id = 0
        
        # Initialize notification system
        if NOTIFICATIONS_AVAILABLE:
            try:
                self.toaster = win10toast.ToastNotifier()
                print("✅ Windows notification system initialized")
            except Exception as e:
                print(f"❌ Failed to initialize notifications: {e}")
        
        # Notification settings
        self.enable_sound = True
        self.enable_popup = True
        self.notification_duration = 10
        self.critical_duration = 30
    
    def send_threat_notification(self, threat_info: Dict[str, Any], severity: str = "high") -> bool:
        """Send threat detection notification with action buttons"""
        try:
            self.notification_id += 1
            
            # Prepare notification content
            title = f"🚨 CyberDefense AI - {severity.upper()} THREAT DETECTED"
            
            threat_name = threat_info.get('threat_name', 'Unknown Threat')
            file_path = threat_info.get('file_path', 'Unknown Location')
            action_taken = threat_info.get('action_taken', 'Monitoring')
            ai_confidence = threat_info.get('ai_confidence', 0.0)
            
            message = f"""
Threat: {threat_name}
Location: {file_path}
Action: {action_taken}
AI Confidence: {ai_confidence:.1%}

Click for advanced options.
            """.strip()
            
            # Determine icon and duration based on severity
            if severity.lower() == "critical":
                icon_path = self.get_icon_path("critical")
                duration = self.critical_duration
            elif severity.lower() == "high":
                icon_path = self.get_icon_path("warning")
                duration = self.notification_duration
            else:
                icon_path = self.get_icon_path("info")
                duration = self.notification_duration
            
            # Send notification with callback
            if self.toaster:
                try:
                    # Try with callback first (newer versions)
                    success = self.toaster.show_toast(
                        title=title,
                        msg=message,
                        icon_path=icon_path,
                        duration=duration,
                        threaded=True,
                        callback_on_click=lambda: self.handle_notification_click(threat_info)
                    )
                except TypeError:
                    # Fallback without callback (older versions)
                    success = self.toaster.show_toast(
                        title=title,
                        msg=message,
                        icon_path=icon_path,
                        duration=duration,
                        threaded=True
                    )
                
                if success:
                    # Store notification in history
                    self.notification_history.append({
                        'id': self.notification_id,
                        'timestamp': datetime.now(),
                        'severity': severity,
                        'threat_info': threat_info,
                        'title': title,
                        'message': message
                    })
                    
                    print(f"📧 Notification sent: {threat_name}")
                    return True
            
            # Fallback to plyer notification
            elif NOTIFICATIONS_AVAILABLE:
                notification.notify(
                    title=title,
                    message=message,
                    timeout=duration,
                    app_icon=icon_path
                )
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Failed to send notification: {e}")
            return False
    
    def send_system_notification(self, title: str, message: str, 
                               notification_type: str = "info") -> bool:
        """Send general system notification"""
        try:
            self.notification_id += 1
            
            full_title = f"🤖 CyberDefense AI - {title}"
            icon_path = self.get_icon_path(notification_type)
            
            if self.toaster:
                success = self.toaster.show_toast(
                    title=full_title,
                    msg=message,
                    icon_path=icon_path,
                    duration=self.notification_duration,
                    threaded=True
                )
                
                if success:
                    print(f"📧 System notification: {title}")
                    return True
            
            # Fallback
            elif NOTIFICATIONS_AVAILABLE:
                notification.notify(
                    title=full_title,
                    message=message,
                    timeout=self.notification_duration
                )
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Failed to send system notification: {e}")
            return False
    
    def get_icon_path(self, icon_type: str) -> Optional[str]:
        """Get appropriate icon path for notification type"""
        icons = {
            "critical": "assets/icons/critical.ico",
            "warning": "assets/icons/warning.ico", 
            "info": "assets/icons/info.ico",
            "success": "assets/icons/success.ico"
        }
        
        # Create icons directory if it doesn't exist
        icons_dir = Path("assets/icons")
        icons_dir.mkdir(parents=True, exist_ok=True)
        
        icon_path = icons.get(icon_type, icons["info"])
        
        # If icon doesn't exist, use system default
        if not Path(icon_path).exists():
            return None
        
        return str(Path(icon_path).absolute())
    
    def handle_notification_click(self, threat_info: Dict[str, Any]):
        """Handle notification click - launch advanced disinfection"""
        print(f"🖱️ Notification clicked for threat: {threat_info.get('threat_name', 'Unknown')}")
        
        # Launch advanced disinfection interface
        try:
            # Import here to avoid circular imports
            from advanced_disinfection import AdvancedDisinfectionGUI
            
            # Launch disinfection GUI in separate thread
            def launch_disinfection():
                disinfection_gui = AdvancedDisinfectionGUI(threat_info)
                disinfection_gui.show()
            
            thread = threading.Thread(target=launch_disinfection, daemon=True)
            thread.start()
            
        except ImportError:
            print("⚠️ Advanced disinfection module not available")
            self.show_basic_threat_dialog(threat_info)
    
    def show_basic_threat_dialog(self, threat_info: Dict[str, Any]):
        """Show basic threat information dialog"""
        import tkinter as tk
        from tkinter import messagebox
        
        threat_name = threat_info.get('threat_name', 'Unknown Threat')
        file_path = threat_info.get('file_path', 'Unknown Location')
        
        message = f"""
Threat Detected: {threat_name}
Location: {file_path}

Would you like to:
- Quarantine the file
- Delete the file
- Ignore this detection
        """
        
        # This would open a dialog box
        result = messagebox.askyesnocancel(
            "Threat Detection",
            message,
            icon=messagebox.WARNING
        )
        
        if result is True:
            print(f"🔒 User chose to quarantine: {file_path}")
        elif result is False:
            print(f"🗑️ User chose to delete: {file_path}")
        else:
            print(f"⏭️ User chose to ignore: {file_path}")
    
    def send_boot_protection_alert(self, boot_threat_info: Dict[str, Any]) -> bool:
        """Send critical boot sector threat notification"""
        try:
            title = "🔴 CRITICAL - BOOT SECTOR THREAT DETECTED"
            
            threat_type = boot_threat_info.get('threat_type', 'Boot Sector Malware')
            sector_location = boot_threat_info.get('sector', 'Unknown')
            
            message = f"""
CRITICAL BOOT THREAT DETECTED!

Type: {threat_type}
Sector: {sector_location}
Risk Level: EXTREME

Immediate action required!
System restart recommended.
            """.strip()
            
            # Send critical notification
            if self.toaster:
                try:
                    # Try with callback first (newer versions)
                    success = self.toaster.show_toast(
                        title=title,
                        msg=message,
                        icon_path=self.get_icon_path("critical"),
                        duration=60,  # Extended duration for critical alerts
                        threaded=True,
                        callback_on_click=lambda: self.handle_boot_threat_click(boot_threat_info)
                    )
                except TypeError:
                    # Fallback without callback (older versions)
                    success = self.toaster.show_toast(
                        title=title,
                        msg=message,
                        icon_path=self.get_icon_path("critical"),
                        duration=60,  # Extended duration for critical alerts
                        threaded=True
                    )
                
                if success:
                    print(f"🚨 CRITICAL boot sector alert sent")
                    return True
            
            return False
            
        except Exception as e:
            print(f"❌ Failed to send boot protection alert: {e}")
            return False
    
    def handle_boot_threat_click(self, boot_threat_info: Dict[str, Any]):
        """Handle boot sector threat notification click"""
        print(f"🚨 Boot threat notification clicked")
        
        try:
            # Launch boot protection interface
            from secure_boot_protection import SecureBootProtectionGUI
            
            def launch_boot_protection():
                boot_gui = SecureBootProtectionGUI(boot_threat_info)
                boot_gui.show()
            
            thread = threading.Thread(target=launch_boot_protection, daemon=True)
            thread.start()
            
        except ImportError:
            print("⚠️ Boot protection module not available")
            self.show_boot_threat_dialog(boot_threat_info)
    
    def show_boot_threat_dialog(self, boot_threat_info: Dict[str, Any]):
        """Show boot sector threat dialog"""
        import tkinter as tk
        from tkinter import messagebox
        
        threat_type = boot_threat_info.get('threat_type', 'Boot Sector Malware')
        
        message = f"""
CRITICAL BOOT SECTOR THREAT!

Threat: {threat_type}

This is extremely dangerous and could:
- Prevent system startup
- Steal sensitive data
- Install persistent malware

Recommended actions:
1. Disconnect from internet
2. Run boot sector repair
3. Perform full system scan
4. Consider system restore

Continue with automated repair?
        """
        
        result = messagebox.askyesno(
            "CRITICAL BOOT THREAT",
            message,
            icon=messagebox.ERROR
        )
        
        if result:
            print("🛠️ User authorized boot sector repair")
            # Trigger automated boot repair
        else:
            print("⚠️ User declined automated repair")
    
    def get_notification_history(self) -> list:
        """Get notification history"""
        return self.notification_history
    
    def clear_notification_history(self):
        """Clear notification history"""
        self.notification_history.clear()
        print("🧹 Notification history cleared")
    
    def set_notification_settings(self, enable_sound: bool = True, 
                                enable_popup: bool = True,
                                duration: int = 10):
        """Configure notification settings"""
        self.enable_sound = enable_sound
        self.enable_popup = enable_popup
        self.notification_duration = duration
        
        print(f"⚙️ Notification settings updated")

# Test function
def test_notifications():
    """Test the notification system"""
    notifier = WindowsNotificationSystem()
    
    # Test system notification
    notifier.send_system_notification(
        "System Startup",
        "AI Protection system is now active and monitoring your system.",
        "success"
    )
    
    time.sleep(3)
    
    # Test threat notification
    threat_info = {
        'threat_name': 'Trojan.Generic.Malware',
        'file_path': 'C:\\Temp\\suspicious_file.exe',
        'action_taken': 'Quarantined',
        'ai_confidence': 0.96,
        'threat_level': 9
    }
    
    notifier.send_threat_notification(threat_info, "high")
    
    time.sleep(3)
    
    # Test boot sector threat
    boot_threat = {
        'threat_type': 'Boot Sector Rootkit',
        'sector': 'Master Boot Record',
        'risk_level': 'EXTREME'
    }
    
    notifier.send_boot_protection_alert(boot_threat)

if __name__ == "__main__":
    test_notifications()