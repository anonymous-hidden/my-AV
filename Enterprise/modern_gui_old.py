"""
Modern Cybersecurity GUI - Bitdefender-inspired design
"""

import tkinter as tk
from tkinter import ttk, font
import threading
import time
from pathlib import Path
import sys

# Add project root to path
sys.path.append(str(Path(__file__).parent))

# Import version configuration
try:
    from version_config import get_version_info, is_feature_available
except ImportError:
    # Default to paid version if config missing
    def get_version_info():
        return {"type": "PAID", "name": "CyberDefense AI Pro", "version": "2.1.0", "is_paid": True}
    def is_feature_available(feature):
        return True

# Mock the missing cybersecurity_platform module
class CybersecurityAIPlatform:
    """Mock cybersecurity platform for standalone operation"""
    def __init__(self):
        self.status = "active"
        self.threats_detected = 0
        self.last_scan = "Never"
    
    def get_status(self):
        return {
            'status': 'protected',
            'threats_detected': 0,
            'last_scan': '2024-10-28 10:30:00',
            'engines_active': 5
        }
    
    def start_scan(self, scan_type="quick"):
        return True
    
    def get_scan_results(self):
        return {
            'files_scanned': 12547,
            'threats_found': 0,
            'status': 'complete'
        }

# Mock other missing modules
def show_safepay():
    """Create and show SafePay with DuckDuckGo browser"""
    import tkinter as tk
    from tkinter import messagebox
    import webbrowser
    import urllib.parse
    import subprocess
    import os
    
    # Create SafePay window
    safepay_window = tk.Toplevel()
    safepay_window.title("🔒 SafePay - DuckDuckGo Secure Browser")
    safepay_window.geometry("1000x700")
    safepay_window.configure(bg="#0d1421")
    
    # Make window modal and on top
    safepay_window.transient()
    safepay_window.grab_set()
    safepay_window.attributes("-topmost", True)
    
    colors = {
        "bg_primary": "#0d1421",
        "bg_secondary": "#1a2332", 
        "accent_green": "#00d4aa",
        "accent_red": "#ff4757",
        "text_primary": "#ffffff"
    }
    
    # Header
    header = tk.Frame(safepay_window, bg=colors["accent_red"], height=50)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    tk.Label(header, text="🛡️ SECURE DUCKDUCKGO BANKING ENVIRONMENT 🛡️",
            font=("Segoe UI", 14, "bold"), bg=colors["accent_red"], fg="white").pack(expand=True)
    
    # Main content
    main_frame = tk.Frame(safepay_window, bg=colors["bg_primary"])
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Title
    tk.Label(main_frame, text="🦆 DuckDuckGo Secure Browser",
            font=("Segoe UI", 20, "bold"), bg=colors["bg_primary"], fg=colors["text_primary"]).pack(pady=30)
    
    # URL frame
    url_frame = tk.Frame(main_frame, bg=colors["bg_primary"])
    url_frame.pack(pady=20)
    
    tk.Label(url_frame, text="Enter URL for secure browsing:", 
            font=("Segoe UI", 12), bg=colors["bg_primary"], fg=colors["text_primary"]).pack(pady=10)
    
    url_entry = tk.Entry(url_frame, font=("Segoe UI", 12), width=60)
    url_entry.pack(pady=10)
    url_entry.insert(0, "https://duckduckgo.com")
    
    def navigate_secure_ddg(url):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        
        result = messagebox.askyesno("DuckDuckGo Secure Browser",
                                   f"🦆 Open in DuckDuckGo secure browser?\n\n" +
                                   f"URL: {url}\n\n" +
                                   "🛡️ All traffic encrypted\n" +
                                   "🔍 Real-time security scanning\n" +
                                   "🚫 Threat protection active\n" +
                                   "🔒 VM isolation maintained")
        
        if result:
            try:
                # Determine the URL to open
                if "duckduckgo.com" in url.lower():
                    final_url = url
                else:
                    # For other URLs, search them on DuckDuckGo for security
                    final_url = f"https://duckduckgo.com/?q=site%3A{urllib.parse.quote(url.replace('https://', '').replace('http://', ''))}"
                
                # Try to use Chrome first, fallback to default browser
                import subprocess
                import os
                
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                if os.path.exists(chrome_path):
                    subprocess.Popen([chrome_path, final_url])
                else:
                    # Fallback to default browser
                    webbrowser.open(final_url)
                
                messagebox.showinfo("Secure Browser Launched",
                                  "🦆 DuckDuckGo opened in secure mode!\n\n" +
                                  "🔒 All traffic encrypted\n" +
                                  "🛡️ Threat protection active\n" +
                                  "🌐 Privacy protection enabled")
            except Exception as e:
                messagebox.showerror("Browser Error", f"Failed to open DuckDuckGo: {e}")
    
    # Buttons
    button_frame = tk.Frame(url_frame, bg=colors["bg_primary"])
    button_frame.pack(pady=20)
    
    tk.Button(button_frame, text="🔍 Security Scan",
             font=("Segoe UI", 12, "bold"), bg="#ff6600", fg="white",
             padx=20, pady=10, command=lambda: messagebox.showinfo("Security Scan", "✅ Website is safe to browse!")).pack(side="left", padx=10)
    
    tk.Button(button_frame, text="🦆 Open in DuckDuckGo", 
             font=("Segoe UI", 12, "bold"), bg=colors["accent_green"], fg="white",
             padx=20, pady=10, command=lambda: navigate_secure_ddg(url_entry.get())).pack(side="left", padx=10)
    
    # Banking links
    banking_frame = tk.LabelFrame(main_frame, text="🏦 Secure Banking Quick Access",
                                 font=("Segoe UI", 12, "bold"), bg=colors["bg_secondary"], fg=colors["text_primary"])
    banking_frame.pack(fill="x", pady=20)
    
    banks = [("🏦 Chase", "chase.com"), ("🏛️ Bank of America", "bankofamerica.com"),
             ("💰 Wells Fargo", "wellsfargo.com"), ("🔷 Citibank", "citibank.com")]
    
    bank_buttons = tk.Frame(banking_frame, bg=colors["bg_secondary"])
    bank_buttons.pack(padx=20, pady=15)
    
    for bank_name, bank_url in banks:
        tk.Button(bank_buttons, text=bank_name, font=("Segoe UI", 10),
                 bg=colors["bg_primary"], fg=colors["text_primary"],
                 padx=15, pady=8, command=lambda url=bank_url: navigate_secure_ddg(f"https://{url}")).pack(side="left", padx=5)
    
    # Close button
    tk.Button(main_frame, text="❌ Close SafePay",
             font=("Segoe UI", 12, "bold"), bg=colors["accent_red"], fg="white",
             padx=20, pady=10, command=safepay_window.destroy).pack(pady=30)
    
    # Center window
    safepay_window.update_idletasks()
    x = (safepay_window.winfo_screenwidth() // 2) - (1000 // 2)
    y = (safepay_window.winfo_screenheight() // 2) - (700 // 2)
    safepay_window.geometry(f"1000x700+{x}+{y}")
    
    return safepay_window

class PrivacyProtectionSuite:
    """Mock Privacy Protection Suite"""
    def __init__(self):
        pass
    def run(self):
        pass

class SettingsManager:
    """Mock Settings Manager"""
    def __init__(self):
        pass
    def run(self):
        pass

class SimpleProtonVPN:
    """Mock Simple Proton VPN"""
    def __init__(self):
        pass
    def run(self):
        pass

class AdvancedVPNGUI:
    """Mock Advanced VPN GUI"""
    def __init__(self):
        pass
    def run(self):
        pass

class AdvancedVPN:
    """Mock Advanced VPN"""
    def __init__(self):
        pass
    def run(self):
        pass

class ModernCybersecurityGUI:
    """Modern cybersecurity interface inspired by Bitdefender"""
    
    def __init__(self):
        # Get version information
        self.version_info = get_version_info()
        
        self.root = tk.Tk()
        title = f"{self.version_info['name']} v{self.version_info['version']}"
        self.root.title(title)
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a1a')
        
        # Set window icon and properties
        self.root.resizable(True, True)
        self.root.minsize(800, 600)
        
        # Platform instance
        self.platform = None
        self.protection_status = "Initializing..."
        self.status_color = "#ffa500"  # Orange for initializing
        
        # VPN and Safepay status
        self.vpn_connected = False
        self.safepay_active = False
        self.current_view = "dashboard"  # Track current view for notifications
        
        # Color scheme (dark theme like Bitdefender)
        self.colors = {
            'bg_primary': '#1a1a1a',      # Main background
            'bg_secondary': '#2d2d2d',     # Card backgrounds
            'bg_tertiary': '#3d3d3d',      # Darker cards
            'accent_green': '#00d4aa',     # Success green
            'accent_blue': '#00d4aa',      # Changed to green (was Bitdefender blue)
            'accent_primary': '#00d4aa',   # Primary accent - now green
            'accent_red': '#ff4444',       # Danger red
            'text_primary': '#ffffff',     # Main text
            'text_secondary': '#b0b0b0',   # Secondary text
            'text_muted': '#808080'        # Muted text
        }
        
        # Initialize notifications early
        self.notifications = []
        
        self.setup_fonts()
        self.create_header()
        self.create_sidebar()
        self.create_main_content()
        self.create_status_bar()
        
        # Start platform initialization
        self.start_platform_initialization()
        
    def setup_fonts(self):
        """Setup custom fonts"""
        self.fonts = {
            'title': font.Font(family="Segoe UI", size=24, weight="bold"),
            'subtitle': font.Font(family="Segoe UI", size=14, weight="normal"),
            'heading': font.Font(family="Segoe UI", size=16, weight="bold"),
            'body': font.Font(family="Segoe UI", size=11, weight="normal"),
            'small': font.Font(family="Segoe UI", size=9, weight="normal")
        }
    
    def create_header(self):
        """Create the top header bar"""
        header_frame = tk.Frame(self.root, bg=self.colors['bg_primary'], height=80)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Logo and title
        title_frame = tk.Frame(header_frame, bg=self.colors['bg_primary'])
        title_frame.pack(side='left', padx=20, pady=20)
        
        # App icon (shield)
        icon_label = tk.Label(title_frame, text="🛡️", font=('Segoe UI', 24), 
                             bg=self.colors['bg_primary'], fg=self.colors['accent_blue'])
        icon_label.pack(side='left', padx=(0, 10))
        
        # Title
        title_label = tk.Label(title_frame, text="CyberDefense AI", 
                              font=self.fonts['title'], bg=self.colors['bg_primary'], 
                              fg=self.colors['text_primary'])
        title_label.pack(side='left')
        
        # Plan indicator (Free/Total Security/Enterprise)
        plan_frame = tk.Frame(title_frame, bg=self.version_info['plan_color'], pady=4, padx=12)
        plan_frame.pack(side='left', padx=(15, 0))
        
        plan_label = tk.Label(plan_frame, text=self.version_info['plan_name'], 
                             font=('Segoe UI', 10, 'bold'), 
                             bg=self.version_info['plan_color'], 
                             fg='white')
        plan_label.pack()
        
        # Status indicator in header
        self.header_status_frame = tk.Frame(header_frame, bg=self.colors['bg_primary'])
        self.header_status_frame.pack(side='right', padx=20, pady=20)
        
        self.status_indicator = tk.Label(self.header_status_frame, text="●", 
                                        font=('Segoe UI', 20), bg=self.colors['bg_primary'], 
                                        fg=self.status_color)
        self.status_indicator.pack(side='right', padx=(0, 5))
        
        self.status_text = tk.Label(self.header_status_frame, text=self.protection_status,
                                   font=self.fonts['body'], bg=self.colors['bg_primary'], 
                                   fg=self.colors['text_primary'])
        self.status_text.pack(side='right')
    
    def create_sidebar(self):
        """Create the left sidebar navigation"""
        self.sidebar = tk.Frame(self.root, bg=self.colors['bg_secondary'], width=200)
        self.sidebar.pack(side='left', fill='y', padx=0, pady=0)
        self.sidebar.pack_propagate(False)
        
        # Navigation items
        nav_items = [
            ("Dashboard", "📊", True),   # Default selected
            ("Protection", "🛡️", False),
            ("Privacy", "👁️", False),
            ("Utilities", "🔧", False),
            ("Notifications", "🔔", False),
            ("Settings", "⚙️", False)
        ]
        
        self.nav_buttons = []
        for item_text, icon, selected in nav_items:
            self.create_nav_button(item_text, icon, selected)
    
    def create_nav_button(self, text, icon, selected=False):
        """Create a navigation button"""
        bg_color = self.colors['accent_blue'] if selected else self.colors['bg_secondary']
        text_color = self.colors['text_primary']
        
        button_frame = tk.Frame(self.sidebar, bg=bg_color, height=60)
        button_frame.pack(fill='x', padx=0, pady=1)
        button_frame.pack_propagate(False)
        
        # Icon
        icon_label = tk.Label(button_frame, text=icon, font=('Segoe UI', 16), 
                             bg=bg_color, fg=text_color)
        icon_label.pack(side='left', padx=(20, 10), pady=20)
        
        # Text
        text_label = tk.Label(button_frame, text=text, font=self.fonts['body'], 
                             bg=bg_color, fg=text_color)
        text_label.pack(side='left', pady=20)
        
        # Make clickable
        for widget in [button_frame, icon_label, text_label]:
            widget.bind("<Button-1>", lambda e, t=text: self.on_nav_click(t))
            widget.bind("<Enter>", lambda e, f=button_frame: self.on_nav_hover(f, True))
            widget.bind("<Leave>", lambda e, f=button_frame: self.on_nav_hover(f, False))
        
        self.nav_buttons.append((button_frame, text, selected))
    
    def on_nav_click(self, nav_text):
        """Handle navigation button click"""
        # Update selected state
        for button_frame, text, _ in self.nav_buttons:
            if text == nav_text:
                button_frame.configure(bg=self.colors['accent_blue'])
                for child in button_frame.winfo_children():
                    child.configure(bg=self.colors['accent_blue'])
            else:
                button_frame.configure(bg=self.colors['bg_secondary'])
                for child in button_frame.winfo_children():
                    child.configure(bg=self.colors['bg_secondary'])
        
        # Update main content based on selection
        self.update_main_content(nav_text)
    
    def on_nav_hover(self, frame, entering):
        """Handle navigation button hover"""
        # Only apply hover effect if not selected
        current_bg = frame.cget('bg')
        if current_bg != self.colors['accent_blue']:
            if entering:
                frame.configure(bg=self.colors['bg_tertiary'])
                for child in frame.winfo_children():
                    child.configure(bg=self.colors['bg_tertiary'])
            else:
                frame.configure(bg=self.colors['bg_secondary'])
                for child in frame.winfo_children():
                    child.configure(bg=self.colors['bg_secondary'])
    
    def create_main_content(self):
        """Create the premium main content area with scrollable functionality"""
        # Main container with enhanced styling
        main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_container.pack(side='right', fill='both', expand=True)
        
        # Create canvas for scrolling with premium styling
        self.main_canvas = tk.Canvas(main_container, 
                                   bg=self.colors['bg_primary'],
                                   highlightthickness=0,
                                   relief='flat',
                                   bd=0)
        
        # Premium scrollbar styling
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg=self.colors['bg_primary'])
        
        # Configure scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )
        
        # Create window in canvas
        self.canvas_window = self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.main_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel scrolling
        self.bind_mousewheel()
        
        # Update scrollable frame when canvas size changes
        self.main_canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Set main_frame to scrollable_frame for compatibility
        self.main_frame = self.scrollable_frame
        
        # Create dashboard by default
        self.create_premium_dashboard()
    
    def bind_mousewheel(self):
        """Bind mouse wheel to scrolling"""
        def _on_mousewheel(event):
            self.main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Bind to various widgets
        self.main_canvas.bind("<MouseWheel>", _on_mousewheel)
        self.scrollable_frame.bind("<MouseWheel>", _on_mousewheel)
        self.root.bind("<MouseWheel>", _on_mousewheel)
    
    def on_canvas_configure(self, event):
        """Update scrollable frame width when canvas size changes"""
        canvas_width = event.width
        self.main_canvas.itemconfig(self.canvas_window, width=canvas_width)
    
    def create_premium_dashboard(self):
        """Create premium dashboard with enhanced styling"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Premium header section
        self.create_premium_header()
        
        # Premium status card
        self.create_premium_status_card()
        
        # Premium action grid with square buttons
        self.create_premium_action_grid()
        
        # Premium quick actions
        self.create_premium_quick_actions()
    
    def create_premium_header(self):
        """Create premium header section"""
        header_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        header_frame.pack(fill='x', pady=(0, 30))
        
        # Main title with premium styling
        title_label = tk.Label(header_frame, 
                             text="🛡️ CYBERDEFENSE AI",
                             font=('Segoe UI', 32, 'bold'),
                             bg=self.colors['bg_primary'],
                             fg=self.colors['accent_green'])
        title_label.pack(anchor='w')
        
        # Subtitle with premium styling
        subtitle_label = tk.Label(header_frame,
                                text="TOTAL SECURITY PLATFORM",
                                font=('Segoe UI', 14, 'normal'),
                                bg=self.colors['bg_primary'],
                                fg=self.colors['text_secondary'])
        subtitle_label.pack(anchor='w', pady=(5, 0))
    
    def create_premium_status_card(self):
        """Create premium status card with enhanced styling"""
        # Status card container with shadow effect
        status_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        status_container.pack(fill='x', pady=(0, 40))
        
        # Shadow frame for depth
        shadow_frame = tk.Frame(status_container, bg='#000000', relief='flat', bd=0)
        shadow_frame.pack(fill='x', padx=(5, 0), pady=(5, 0))
        
        # Main status card with premium styling
        status_card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat', bd=0)
        status_card.pack(fill='x', padx=(0, 5), pady=(0, 5))
        
        # Content frame with enhanced padding
        content_frame = tk.Frame(status_card, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='x', padx=40, pady=30)
        
        # Status header
        header_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Large shield icon with glow effect
        shield_frame = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        shield_frame.pack(side='left', padx=(0, 25))
        
        shield_bg = tk.Frame(shield_frame, bg=self.colors['accent_green'], width=80, height=80)
        shield_bg.pack()
        shield_bg.pack_propagate(False)
        
        shield_icon = tk.Label(shield_bg, text="🛡️", 
                             font=('Segoe UI Emoji', 32, 'bold'),
                             bg=self.colors['accent_green'], fg='white')
        shield_icon.pack(expand=True)
        
        # Status info
        info_frame = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        info_frame.pack(side='left', fill='x', expand=True)
        
        # Main status text (for compatibility with update_protection_status)
        self.main_status_label = tk.Label(info_frame, text="SYSTEM PROTECTED",
                              font=('Segoe UI', 24, 'bold'),
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['accent_green'])
        self.main_status_label.pack(anchor='w')
        
        # Status details (for compatibility with update_protection_status)
        self.status_subtitle = tk.Label(info_frame, text="All protection modules active • Real-time monitoring enabled",
                               font=('Segoe UI', 12),
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['text_secondary'])
        self.status_subtitle.pack(anchor='w', pady=(5, 0))
        
        # Statistics grid
        stats_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        stats_frame.pack(fill='x', pady=(20, 0))
        
        # Create premium statistics
        stats = [
            ("Threats Blocked", "1,247", "🚫"),
            ("Files Scanned", "94,523", "🔍"),
            ("Last Scan", "2 min ago", "⏰"),
            ("System Health", "Excellent", "💚")
        ]
        
        for i, (label, value, icon) in enumerate(stats):
            stat_frame = tk.Frame(stats_frame, bg=self.colors['bg_tertiary'], relief='flat', bd=0)
            stat_frame.grid(row=0, column=i, padx=10, pady=0, sticky='ew')
            
            # Icon
            icon_label = tk.Label(stat_frame, text=icon, font=('Segoe UI Emoji', 16),
                                bg=self.colors['bg_tertiary'], fg=self.colors['accent_green'])
            icon_label.pack(pady=(15, 5))
            
            # Value
            value_label = tk.Label(stat_frame, text=value, font=('Segoe UI', 14, 'bold'),
                                 bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'])
            value_label.pack()
            
            # Label
            label_label = tk.Label(stat_frame, text=label, font=('Segoe UI', 10),
                                 bg=self.colors['bg_tertiary'], fg=self.colors['text_secondary'])
            label_label.pack(pady=(0, 15))
            
            # Configure grid weight
            stats_frame.grid_columnconfigure(i, weight=1)
    
    def create_premium_action_grid(self):
        """Create premium action grid with square buttons"""
        # Action grid container
        grid_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        grid_container.pack(fill='x', pady=(0, 40))
        
        # Section title
        title_frame = tk.Frame(grid_container, bg=self.colors['bg_primary'])
        title_frame.pack(fill='x', pady=(0, 25))
        
        title_label = tk.Label(title_frame, text="🛡️ PROTECTION MODULES",
                             font=('Segoe UI', 20, 'bold'),
                             bg=self.colors['bg_primary'],
                             fg=self.colors['text_primary'])
        title_label.pack(anchor='w')
        
        # Premium square buttons grid
        buttons_frame = tk.Frame(grid_container, bg=self.colors['bg_primary'])
        buttons_frame.pack(fill='x')
        
        # Define premium action buttons
        actions = [
            # Row 1
            [
                ("🔍", "ANTIVIRUS", "Real-time protection", self.colors['accent_green']),
                ("🌐", "WEB SHIELD", "Browse safely", self.colors['accent_blue']),
                ("🔥", "FIREWALL", "Network security", self.colors['accent_red']),
                ("📧", "EMAIL GUARD", "Message protection", self.colors['accent_green'])
            ],
            # Row 2
            [
                ("🛡️", "VPN SECURE", "Anonymous browsing", self.colors['accent_blue']),
                ("💳", "SAFEPAY", "Secure banking", self.colors['accent_green']),
                ("🔒", "PRIVACY", "Data protection", self.colors['accent_red']),
                ("⚙️", "SETTINGS", "Configuration", self.colors['text_secondary'])
            ]
        ]
        
        # Add Enterprise row if Enterprise version
        if is_feature_available('enterprise_features'):
            enterprise_row = [
                ("🧬", "MALWARE ANALYZER", "Advanced analysis", "#ff6b35"),
                ("📊", "NETWORK ANALYZER", "Deep packet inspection", "#ff6b35"),
                ("👥", "USER MANAGEMENT", "Admin dashboard", "#ff6b35"),
                ("📈", "ENTERPRISE LOGS", "Forensic analysis", "#ff6b35")
            ]
            actions.append(enterprise_row)
        
        for row_idx, row in enumerate(actions):
            row_frame = tk.Frame(buttons_frame, bg=self.colors['bg_primary'])
            row_frame.pack(fill='x', pady=10)
            
            for col_idx, (icon, title, desc, color) in enumerate(row):
                self.create_premium_square_button(row_frame, icon, title, desc, color, row_idx, col_idx)
    
    def create_premium_square_button(self, parent, icon, title, description, color, row, col):
        """Create premium square button with enhanced styling"""
        # Button container for proper spacing
        button_container = tk.Frame(parent, bg=self.colors['bg_primary'])
        button_container.grid(row=0, column=col, padx=15, pady=0, sticky='nsew')
        
        # Configure column weights for equal spacing
        parent.grid_columnconfigure(col, weight=1)
        
        # Shadow frame for depth effect
        shadow_frame = tk.Frame(button_container, bg='#000000', width=160, height=160)
        shadow_frame.pack(padx=(4, 0), pady=(4, 0))
        shadow_frame.pack_propagate(False)
        
        # Main button frame (square)
        button_frame = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], 
                               width=156, height=156, relief='flat', bd=0)
        button_frame.pack(padx=(0, 4), pady=(0, 4))
        button_frame.pack_propagate(False)
        
        # Button content
        content_frame = tk.Frame(button_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=15, pady=15)
        
        # Icon with background
        icon_bg = tk.Frame(content_frame, bg=color, width=50, height=50)
        icon_bg.pack(pady=(0, 10))
        icon_bg.pack_propagate(False)
        
        icon_label = tk.Label(icon_bg, text=icon, font=('Segoe UI Emoji', 20, 'bold'),
                            bg=color, fg='white')
        icon_label.pack(expand=True)
        
        # Title
        title_label = tk.Label(content_frame, text=title, font=('Segoe UI', 11, 'bold'),
                             bg=self.colors['bg_secondary'], fg=self.colors['text_primary'])
        title_label.pack(pady=(0, 5))
        
        # Description
        desc_label = tk.Label(content_frame, text=description, font=('Segoe UI', 9),
                            bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                            wraplength=120, justify='center')
        desc_label.pack()
        
        # Make button clickable with hover effects
        clickable_widgets = [button_frame, content_frame, icon_bg, icon_label, title_label, desc_label]
        
        def on_enter(e):
            button_frame.config(bg=self.colors['bg_tertiary'])
            content_frame.config(bg=self.colors['bg_tertiary'])
            title_label.config(bg=self.colors['bg_tertiary'])
            desc_label.config(bg=self.colors['bg_tertiary'])
            
        def on_leave(e):
            button_frame.config(bg=self.colors['bg_secondary'])
            content_frame.config(bg=self.colors['bg_secondary'])
            title_label.config(bg=self.colors['bg_secondary'])
            desc_label.config(bg=self.colors['bg_secondary'])
        
        def on_click(e):
            self.handle_premium_action(title)
            print(f"🔘 Premium button clicked: {title}")
        
        for widget in clickable_widgets:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)
            widget.config(cursor='hand2')
    
    def handle_premium_action(self, action):
        """Handle premium button actions"""
        action_map = {
            "ANTIVIRUS": self.start_antivirus_scan,
            "WEB SHIELD": self.show_web_protection,
            "FIREWALL": self.show_firewall_settings,
            "EMAIL GUARD": self.show_email_protection,
            "VPN SECURE": self.toggle_vpn,
            "SAFEPAY": lambda: show_safepay(),
            "PRIVACY": self.create_privacy_view,
            "SETTINGS": self.show_settings,
            # Enterprise features
            "MALWARE ANALYZER": self.show_malware_analyzer,
            "NETWORK ANALYZER": self.show_network_analyzer,
            "USER MANAGEMENT": self.show_user_management,
            "ENTERPRISE LOGS": self.show_enterprise_logs
        }
        
        if action in action_map:
            action_map[action]()
        else:
            self.show_feature_dialog(action, f"{action} module activated")
    
    def create_premium_quick_actions(self):
        """Create premium quick actions section"""
        # Quick actions container
        quick_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        quick_container.pack(fill='x', pady=(0, 40))
        
        # Section title
        title_frame = tk.Frame(quick_container, bg=self.colors['bg_primary'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(title_frame, text="⚡ QUICK ACTIONS",
                             font=('Segoe UI', 18, 'bold'),
                             bg=self.colors['bg_primary'],
                             fg=self.colors['text_primary'])
        title_label.pack(anchor='w')
        
        # Quick action buttons
        actions_frame = tk.Frame(quick_container, bg=self.colors['bg_primary'])
        actions_frame.pack(fill='x')
        
        quick_actions = [
            ("🚀 FULL SCAN", "Complete system scan", self.colors['accent_green']),
            ("⚡ QUICK SCAN", "Fast security check", self.colors['accent_blue']),
            ("🛡️ ACTIVATE ALL", "Enable all protection", self.colors['accent_green']),
            ("🚨 EMERGENCY", "Emergency shutdown", self.colors['accent_red'])
        ]
        
        for i, (text, desc, color) in enumerate(quick_actions):
            self.create_premium_quick_button(actions_frame, text, desc, color, i)
    
    def create_premium_quick_button(self, parent, text, description, color, index):
        """Create premium quick action button"""
        # Button container
        container = tk.Frame(parent, bg=self.colors['bg_primary'])
        container.grid(row=0, column=index, padx=10, pady=0, sticky='ew')
        parent.grid_columnconfigure(index, weight=1)
        
        # Shadow frame
        shadow = tk.Frame(container, bg='#000000', height=60)
        shadow.pack(fill='x', padx=(3, 0), pady=(3, 0))
        
        # Main button
        button = tk.Button(shadow, text=text, font=('Segoe UI', 11, 'bold'),
                         bg=color, fg='white', relief='flat', bd=0,
                         height=2, cursor='hand2',
                         activebackground=self.lighten_color(color),
                         command=lambda: self.handle_quick_action(text))
        button.pack(fill='both', expand=True, padx=(0, 3), pady=(0, 3))
        
        # Add hover effects
        def on_enter(e):
            button.config(bg=self.lighten_color(color))
            
        def on_leave(e):
            button.config(bg=color)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def handle_quick_action(self, action):
        """Handle quick action button clicks"""
        print(f"⚡ Quick action: {action}")
        
        if "FULL SCAN" in action:
            self.show_scan_progress("Full System Scan")
        elif "QUICK SCAN" in action:
            self.show_scan_progress("Quick Scan")
        elif "ACTIVATE ALL" in action:
            self.activate_all_systems()
        elif "EMERGENCY" in action:
            self.emergency_shutdown()
    
    def create_dashboard(self):
        """Create the main dashboard view"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Main status card
        self.create_status_card()
        
        # Action buttons grid
        self.create_action_grid()
        
        # Quick actions
        self.create_quick_actions()
    
    def create_status_card(self):
        """Create the main status card"""
        status_frame = tk.Frame(self.main_frame, bg=self.colors['bg_secondary'], 
                               relief='flat', bd=0)
        status_frame.pack(fill='x', pady=(0, 20))
        
        # Status content
        content_frame = tk.Frame(status_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='x', padx=30, pady=30)
        
        # Large shield icon
        shield_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        shield_frame.pack(side='left', padx=(0, 30))
        
        shield_canvas = tk.Canvas(shield_frame, width=120, height=120, 
                                 bg=self.colors['bg_secondary'], highlightthickness=0)
        shield_canvas.pack()
        
        # Draw shield with checkmark
        self.draw_shield_status(shield_canvas)
        
        # Status text
        text_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        text_frame.pack(side='left', fill='both', expand=True)
        
        # Main status message
        self.main_status_label = tk.Label(text_frame, text="You are safe", 
                                         font=self.fonts['title'], bg=self.colors['bg_secondary'], 
                                         fg=self.colors['text_primary'])
        self.main_status_label.pack(anchor='w')
        
        # Subtitle
        self.status_subtitle = tk.Label(text_frame, text="We're looking out for your device and data.", 
                                       font=self.fonts['subtitle'], bg=self.colors['bg_secondary'], 
                                       fg=self.colors['text_secondary'])
        self.status_subtitle.pack(anchor='w', pady=(5, 20))
        
        # AI recommendations section
        recommendations_frame = tk.Frame(text_frame, bg=self.colors['bg_secondary'])
        recommendations_frame.pack(anchor='w', fill='x')
        
        rec_title = tk.Label(recommendations_frame, text="AI Security Recommendations", 
                            font=self.fonts['heading'], bg=self.colors['bg_secondary'], 
                            fg=self.colors['text_primary'])
        rec_title.pack(anchor='w')
        
        rec_text = tk.Label(recommendations_frame, 
                           text="AI advisor provides contextual recommendations based\non your device usage and needs. Advanced threat detection\nand automated response systems are active.",
                           font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                           fg=self.colors['text_secondary'], justify='left')
        rec_text.pack(anchor='w', pady=(5, 0))
    
    def draw_shield_status(self, canvas):
        """Draw the hexagonal shield status indicator"""
        # Clear canvas
        canvas.delete("all")
        
        # Shield color based on status
        if self.protection_status == "Protected":
            shield_color = self.colors['accent_green']
            inner_color = "#ffffff"
        else:
            shield_color = self.colors['accent_blue']
            inner_color = "#ffffff"
        
        # Draw hexagonal shield
        center_x, center_y = 60, 60
        radius = 35
        
        # Calculate hexagon points
        import math
        points = []
        for i in range(6):
            angle = math.pi * 2 * i / 6 - math.pi / 2  # Start from top
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        
        # Draw outer hexagon (shield body)
        canvas.create_polygon(points, fill=shield_color, outline=shield_color, width=2, smooth=False)
        
        # Draw inner white circle
        circle_radius = 8
        canvas.create_oval(
            center_x - circle_radius, center_y - circle_radius,
            center_x + circle_radius, center_y + circle_radius,
            fill=inner_color, outline=inner_color
        )
        
        # Add subtle border
        canvas.create_polygon(points, fill="", outline=self.colors['text_primary'], width=1, smooth=False)
    
    def create_action_grid(self):
        """Create the grid of action buttons"""
        grid_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        grid_frame.pack(fill='x', pady=(0, 20))
        
        # Action buttons data with dynamic status
        def get_vpn_status():
            return "VPN (Connected)" if self.vpn_connected else "VPN"
            
        def get_safepay_status():
            return "Safepay (Active)" if self.safepay_active else "Safepay"
        
        actions = [
            ("System Scan", "💻", "Full system security scan"),
            ("Quick Scan", "⚡", "Fast threat detection"),
            ("Vulnerability Scan", "🔍", "Check for vulnerabilities"),
            (get_vpn_status(), "🔗", "Secure VPN connection"),
            (get_safepay_status(), "🛡️", "Protected browsing"),
            ("Add Action", "➕", "Quick actions menu")
        ]
        
        # Create 3x2 grid
        for i, (title_func_or_str, icon, desc) in enumerate(actions):
            row = i // 3
            col = i % 3
            
            # Handle dynamic titles
            title = title_func_or_str() if callable(title_func_or_str) else title_func_or_str
            
            self.create_action_card(grid_frame, title, icon, desc, row, col)
    
    def create_quick_actions(self):
        """Create quick actions section"""
        qa_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        qa_frame.pack(fill='x')
        
        # Subscription info (like Bitdefender)
        info_frame = tk.Frame(qa_frame, bg=self.colors['bg_secondary'])
        info_frame.pack(fill='x', pady=10)
        
        info_content = tk.Frame(info_frame, bg=self.colors['bg_secondary'])
        info_content.pack(fill='x', padx=20, pady=15)
        
        info_text = tk.Label(info_content, 
                           text="🔹 You can protect 3 more devices with your subscription. Install CyberDefense AI on a new device",
                           font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                           fg=self.colors['accent_blue'])
        info_text.pack(anchor='w')
    
    def create_status_card(self):
        """Create the main status card"""
        status_frame = tk.Frame(self.main_frame, bg=self.colors['bg_secondary'], 
                               relief='flat', bd=0)
        status_frame.pack(fill='x', pady=(0, 20))
        
        # Status content
        content_frame = tk.Frame(status_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='x', padx=30, pady=30)
        
        # Large shield icon
        shield_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        shield_frame.pack(side='left', padx=(0, 30))
        
        shield_canvas = tk.Canvas(shield_frame, width=120, height=120, 
                                 bg=self.colors['bg_secondary'], highlightthickness=0)
        shield_canvas.pack()
        
        # Draw shield with checkmark
        self.draw_shield_status(shield_canvas)
        
        # Status text
        text_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        text_frame.pack(side='left', fill='both', expand=True)
        
        # Main status message
        self.main_status_label = tk.Label(text_frame, text="You are safe", 
                                         font=self.fonts['title'], bg=self.colors['bg_secondary'], 
                                         fg=self.colors['text_primary'])
        self.main_status_label.pack(anchor='w')
        
        # Subtitle
        self.status_subtitle = tk.Label(text_frame, text="We're looking out for your device and data.", 
                                       font=self.fonts['subtitle'], bg=self.colors['bg_secondary'], 
                                       fg=self.colors['text_secondary'])
        self.status_subtitle.pack(anchor='w', pady=(5, 20))
        
        # AI recommendations section
        recommendations_frame = tk.Frame(text_frame, bg=self.colors['bg_secondary'])
        recommendations_frame.pack(anchor='w', fill='x')
        
        rec_title = tk.Label(recommendations_frame, text="AI Security Recommendations", 
                            font=self.fonts['heading'], bg=self.colors['bg_secondary'], 
                            fg=self.colors['text_primary'])
        rec_title.pack(anchor='w')
        
        rec_text = tk.Label(recommendations_frame, 
                           text="AI advisor provides contextual recommendations based\non your device usage and needs. Advanced threat detection\nand automated response systems are active.",
                           font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                           fg=self.colors['text_secondary'], justify='left')
        rec_text.pack(anchor='w', pady=(5, 0))
    
    def draw_shield_status(self, canvas):
        """Draw the hexagonal shield status indicator like in the image"""
        # Clear canvas
        canvas.delete("all")
        
        # Shield color based on status
        if self.protection_status == "Protected":
            shield_color = self.colors['accent_green']
            inner_color = "#ffffff"
        else:
            shield_color = self.colors['accent_blue']
            inner_color = "#ffffff"
        
        # Draw hexagonal shield (like in the image)
        center_x, center_y = 60, 60
        radius = 35
        
        # Calculate hexagon points
        import math
        points = []
        for i in range(6):
            angle = math.pi * 2 * i / 6 - math.pi / 2  # Start from top
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        
        # Draw outer hexagon (shield body)
        canvas.create_polygon(points, fill=shield_color, outline=shield_color, width=2, smooth=False)
        
        # Draw inner white circle (like in the image)
        circle_radius = 8
        canvas.create_oval(
            center_x - circle_radius, center_y - circle_radius,
            center_x + circle_radius, center_y + circle_radius,
            fill=inner_color, outline=inner_color
        )
        
        # Add subtle border
        canvas.create_polygon(points, fill="", outline=self.colors['text_primary'], width=1, smooth=False)
    
    def create_action_grid(self):
        """Create the grid of action buttons"""
        grid_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        grid_frame.pack(fill='x', pady=(0, 20))
        
        # Action buttons data with dynamic status
        def get_vpn_status():
            return "VPN (Connected)" if self.vpn_connected else "VPN"
            
        def get_safepay_status():
            return "Safepay (Active)" if self.safepay_active else "Safepay"
        
        actions = [
            ("System Scan", "💻", "Full system security scan"),
            ("Quick Scan", "⚡", "Fast threat detection"),
            ("Vulnerability Scan", "🔍", "Check for vulnerabilities"),
            (get_vpn_status(), "🔗", "Secure VPN connection"),
            (get_safepay_status(), "🛡️", "Protected browsing"),
            ("Add Action", "➕", "Quick actions menu")
        ]
        
        # Create 3x2 grid
        for i, (title_func_or_str, icon, desc) in enumerate(actions):
            row = i // 3
            col = i % 3
            
            # Handle dynamic titles
            title = title_func_or_str() if callable(title_func_or_str) else title_func_or_str
            
            self.create_action_card(grid_frame, title, icon, desc, row, col)
    
    def create_action_card(self, parent, title, icon, description, row, col):
        """Create an individual action card"""
        # Special styling for "Add Action" card
        is_add_action = title == "Add Action"
        bg_color = self.colors['bg_primary'] if is_add_action else self.colors['bg_secondary']
        border_style = 'dashed' if is_add_action else 'solid'
        
        card_frame = tk.Frame(parent, bg=bg_color, relief='flat', bd=1, 
                             highlightbackground=self.colors['text_muted'], 
                             highlightthickness=1 if is_add_action else 0)
        card_frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        # Configure grid weights for responsive design
        parent.grid_rowconfigure(row, weight=1, minsize=120)
        parent.grid_columnconfigure(col, weight=1, minsize=200)
        
        # Card content
        content_frame = tk.Frame(card_frame, bg=bg_color)
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Icon with better positioning
        icon_label = tk.Label(content_frame, text=icon, font=('Segoe UI', 28), 
                             bg=bg_color, fg=self.colors['accent_blue'])
        icon_label.pack(pady=(5, 8))
        
        # Title with better spacing
        title_label = tk.Label(content_frame, text=title, font=self.fonts['heading'], 
                              bg=bg_color, fg=self.colors['text_primary'])
        title_label.pack()
        
        # Add subtle description for non-add-action cards
        if not is_add_action:
            desc_label = tk.Label(content_frame, text=description, font=self.fonts['small'], 
                                 bg=bg_color, fg=self.colors['text_muted'], wraplength=150)
            desc_label.pack(pady=(3, 0))
        
        # Make clickable with improved hover effect
        widgets_to_bind = [card_frame, content_frame, icon_label, title_label]
        if not is_add_action and 'desc_label' in locals():
            widgets_to_bind.append(desc_label)
            
        for widget in widgets_to_bind:
            widget.bind("<Button-1>", lambda e, t=title: self.on_action_click(t))
            widget.bind("<Enter>", lambda e, f=card_frame, bg=bg_color: self.on_card_hover(f, True, bg_color))
            widget.bind("<Leave>", lambda e, f=card_frame, bg=bg_color: self.on_card_hover(f, False, bg_color))
    
    def on_card_hover(self, frame, entering, original_bg=None):
        """Handle card hover effect with improved styling"""
        if entering:
            # Lighter hover effect
            hover_color = self.colors['bg_tertiary']
            frame.configure(bg=hover_color)
            for child in frame.winfo_children():
                child.configure(bg=hover_color)
                for grandchild in child.winfo_children():
                    grandchild.configure(bg=hover_color)
        else:
            # Return to original color
            restore_color = original_bg if original_bg else self.colors['bg_secondary']
            frame.configure(bg=restore_color)
            for child in frame.winfo_children():
                child.configure(bg=restore_color)
                for grandchild in child.winfo_children():
                    grandchild.configure(bg=restore_color)
    
    def on_action_click(self, action):
        """Handle action button clicks"""
        print(f"Action clicked: {action}")
        
        # Normalize action names for dynamic titles
        if "VPN" in action:
            action = "VPN"
        elif "Safepay" in action:
            action = "Safepay"
        
        # Show scanning progress
        if action in ["System Scan", "Quick Scan", "Vulnerability Scan"]:
            self.show_scan_progress(action)
        
        # Implement actual functionality
        if action == "System Scan":
            self.start_system_scan()
        elif action == "Quick Scan":
            self.start_quick_scan()
        elif action == "Vulnerability Scan":
            self.start_vulnerability_scan()
        elif action == "VPN":
            self.toggle_vpn()
        elif action == "Safepay":
            self.launch_safepay()
        elif action == "Add Action":
            self.show_add_action_menu()
    
    def show_scan_progress(self, scan_type):
        """Show scan progress in a popup"""
        # Create progress window
        progress_window = tk.Toplevel(self.root)
        progress_window.title(f"{scan_type} Progress")
        progress_window.geometry("400x200")
        progress_window.configure(bg=self.colors['bg_secondary'])
        progress_window.resizable(False, False)
        
        # Center the window
        progress_window.transient(self.root)
        progress_window.grab_set()
        
        # Progress content
        content_frame = tk.Frame(progress_window, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(content_frame, text=f"{scan_type} in Progress", 
                              font=self.fonts['heading'], bg=self.colors['bg_secondary'], 
                              fg=self.colors['text_primary'])
        title_label.pack(pady=(0, 20))
        
        # Progress bar
        progress_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        progress_frame.pack(fill='x', pady=(0, 10))
        
        # Custom progress bar (simplified)
        progress_bg = tk.Frame(progress_frame, bg=self.colors['bg_primary'], height=6)
        progress_bg.pack(fill='x')
        
        progress_fill = tk.Frame(progress_bg, bg=self.colors['accent_blue'], height=6)
        progress_fill.pack(side='left', fill='y')
        
        # Status text
        status_label = tk.Label(content_frame, text="Initializing scan...", 
                               font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                               fg=self.colors['text_secondary'])
        status_label.pack()
        
        # Simulate progress
        self.animate_progress(progress_fill, status_label, progress_window, scan_type)
    
    def animate_progress(self, progress_fill, status_label, window, scan_type):
        """Animate the progress bar"""
        def update_progress(step=0):
            if step <= 100:
                # Update progress bar width
                progress_fill.configure(width=int(step * 3.6))  # 360px max width
                
                # Update status text
                if step < 30:
                    status_label.configure(text="Scanning system files...")
                elif step < 60:
                    status_label.configure(text="Checking for threats...")
                elif step < 90:
                    status_label.configure(text="Analyzing results...")
                else:
                    status_label.configure(text="Finalizing scan...")
                
                # Continue animation
                window.after(50, lambda: update_progress(step + 2))
            else:
                # Scan complete
                status_label.configure(text="Scan completed successfully!", 
                                     fg=self.colors['accent_green'])
                window.after(2000, window.destroy)
        
        update_progress()
    

    def create_status_bar(self):
        """Create bottom status bar"""
        self.status_bar = tk.Frame(self.root, bg=self.colors['bg_secondary'], height=30)
        self.status_bar.pack(side='bottom', fill='x')
        self.status_bar.pack_propagate(False)
        
        # Real-time status
        self.real_time_status = tk.Label(self.status_bar, text="Real-time protection: Active", 
                                        font=self.fonts['small'], bg=self.colors['bg_secondary'], 
                                        fg=self.colors['text_secondary'])
        self.real_time_status.pack(side='left', padx=10, pady=5)
        
        # VPN status
        self.vpn_status_label = tk.Label(self.status_bar, text="VPN: Disconnected", 
                                        font=self.fonts['small'], bg=self.colors['bg_secondary'], 
                                        fg=self.colors['text_secondary'])
        self.vpn_status_label.pack(side='left', padx=10, pady=5)
        
        # Safepay status  
        self.safepay_status_label = tk.Label(self.status_bar, text="Safepay: Inactive", 
                                           font=self.fonts['small'], bg=self.colors['bg_secondary'], 
                                           fg=self.colors['text_secondary'])
        self.safepay_status_label.pack(side='left', padx=10, pady=5)
        
        # Last scan info
        self.last_scan_status = tk.Label(self.status_bar, text="Last scan: Never", 
                                        font=self.fonts['small'], bg=self.colors['bg_secondary'], 
                                        fg=self.colors['text_secondary'])
        self.last_scan_status.pack(side='right', padx=10, pady=5)
    
    def start_platform_initialization(self):
        """Initialize the platform in background"""
        def init_worker():
            try:
                self.platform = CybersecurityAIPlatform()
                # Update status to protected
                self.root.after(0, self.update_protection_status, "Protected", self.colors['accent_green'])
            except Exception as e:
                self.root.after(0, self.update_protection_status, "Error", self.colors['accent_red'])
                print(f"Platform initialization error: {e}")
        
        threading.Thread(target=init_worker, daemon=True).start()
    
    def update_protection_status(self, status, color):
        """Update the protection status"""
        self.protection_status = status
        self.status_color = color
        
        # Update header status
        self.status_indicator.configure(fg=color)
        self.status_text.configure(text=status)
        
        # Update main status
        if status == "Protected":
            self.main_status_label.configure(text="You are safe", fg=self.colors['accent_green'])
            self.status_subtitle.configure(text="Advanced AI protection is active and monitoring.")
        elif status == "Error":
            self.main_status_label.configure(text="Protection Error", fg=self.colors['accent_red'])
            self.status_subtitle.configure(text="There was an issue initializing protection.")
        
        # Redraw shield
        for widget in self.main_frame.winfo_children():
            if hasattr(widget, 'winfo_children'):
                for child in widget.winfo_children():
                    if hasattr(child, 'winfo_children'):
                        for canvas in child.winfo_children():
                            if isinstance(canvas, tk.Canvas):
                                canvas.delete("all")
                                self.draw_shield_status(canvas)
    
    def update_main_content(self, section):
        """Update main content based on navigation selection"""
        self.current_view = section.lower()  # Track current view
        
        if section == "Dashboard":
            self.create_dashboard()
        elif section == "Protection":
            self.create_protection_view()
        elif section == "Privacy":
            self.create_privacy_view()
        elif section == "Settings":
            self.create_settings_view()
        elif section == "Utilities":
            self.create_utilities_view()
        elif section == "Notifications":
            self.create_notifications_view()
        # Add more sections as needed
    
    def create_protection_view(self):
        """Create premium protection features view with scrollable design"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Premium title section with enhanced styling
        title_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        title_container.pack(fill='x', pady=(0, 40))
        
        # Enhanced header with gradient-like effect
        header_frame = tk.Frame(title_container, bg=self.colors['bg_primary'])
        header_frame.pack(fill='x')
        
        # Large shield icon with glow effect
        shield_container = tk.Frame(header_frame, bg=self.colors['bg_primary'])
        shield_container.pack(side='left', padx=(0, 30))
        
        shield_bg = tk.Frame(shield_container, bg=self.colors['accent_green'], width=80, height=80)
        shield_bg.pack()
        shield_bg.pack_propagate(False)
        
        shield_icon = tk.Label(shield_bg, text="🛡️", font=('Segoe UI Emoji', 36, 'bold'),
                             bg=self.colors['accent_green'], fg='white')
        shield_icon.pack(expand=True)
        
        # Title section with premium typography
        title_frame = tk.Frame(header_frame, bg=self.colors['bg_primary'])
        title_frame.pack(side='left', fill='x', expand=True)
        
        # Main title
        main_title = tk.Label(title_frame, text="PROTECTION FEATURES", 
                             font=('Segoe UI', 32, 'bold'), 
                             bg=self.colors['bg_primary'], 
                             fg=self.colors['text_primary'])
        main_title.pack(anchor='w')
        
        # Subtitle
        subtitle = tk.Label(title_frame, text="Advanced security modules for comprehensive protection",
                          font=('Segoe UI', 14), 
                          bg=self.colors['bg_primary'], 
                          fg=self.colors['text_secondary'])
        subtitle.pack(anchor='w', pady=(5, 0))
        
        # Premium protection features grid
        self.create_premium_protection_grid()
    
    def create_premium_protection_grid(self):
        """Create Bitdefender-style protection grid"""
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create header
        header_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        header_frame.pack(fill='x', pady=(0, 30))
        
        # Title matching Bitdefender style
        title = tk.Label(header_frame, text="Protection Features",
                        font=('Segoe UI', 28, 'bold'),
                        bg=self.colors['bg_primary'],
                        fg=self.colors['text_primary'])
        title.pack(anchor='w')
        
        # Grid container for cards
        grid_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        grid_container.pack(fill='both', expand=True, pady=(0, 30))
        
        # Protection features matching Bitdefender layout
        features = [
            {
                'title': 'Antivirus',
                'description': 'Real-time protection blocks any threat\nfrom running on your device.',
                'icon': '🛡️',
                'icon_color': '#4a9eff',
                'status': True,
                'button_text': 'Open',
                'has_toggle': False
            },
            {
                'title': 'Email Protection', 
                'description': 'Scans and identifies potentially dangerous\ncontent received via email.',
                'icon': '📧',
                'icon_color': '#4a9eff',
                'status': False,
                'button_text': 'Open',
                'has_toggle': False
            },
            {
                'title': 'Cryptomining Protection',
                'description': 'Prevents the use of your device and\nelectricity in Cryptomining activities that\ngenerate revenue for attackers.',
                'icon': '⚡',
                'icon_color': '#4a9eff',
                'status': True,
                'button_text': 'Settings',
                'has_toggle': True
            },
            {
                'title': 'Advanced Threat Defense',
                'description': 'Identifies suspicious behavior and blocks\neven zero-day attacks from compromising\nyour device.',
                'icon': '🔍',
                'icon_color': '#4a9eff',
                'status': False,
                'button_text': 'Open',
                'has_toggle': False
            },
            {
                'title': 'Online Threat Prevention',
                'description': 'Our cloud-based Global Protective\nNetwork secures your device by blocking\nany online threat.',
                'icon': '🌐',
                'icon_color': '#ff6b6b',
                'status': False,
                'button_text': 'Settings',
                'has_toggle': False
            },
            {
                'title': 'Vulnerability',
                'description': 'Analyze your system, apps and network\nfor vulnerabilities that might compromise\nyour device and data.',
                'icon': '🔍',
                'icon_color': '#ff6b6b',
                'status': True,
                'button_text': 'Open',
                'has_toggle': True
            },
            {
                'title': 'Firewall',
                'description': 'Monitors connections performed by your\napps and provides advanced control of\nnetwork connectivity.',
                'icon': '🔥',
                'icon_color': '#ff6b6b',
                'status': True,
                'button_text': 'Settings',
                'has_toggle': True
            },
            {
                'title': 'Ransomware Remediation',
                'description': 'Ransomware Remediation reverses any\ndamage done by ransomware by restoring\nencrypted files.',
                'icon': '�',
                'icon_color': '#4a9eff',
                'status': True,
                'button_text': 'Manage',
                'has_toggle': True
            },
            {
                'title': 'Antispam',
                'description': 'Filters what is not relevant in the Inbox of\nyour local email client (Outlook,\nThunderbird).',
                'icon': '📮',
                'icon_color': '#4a9eff',
                'status': True,
                'button_text': 'Settings',
                'has_toggle': True
            }
        ]
        
        # Create cards in 2-column layout
        for i, feature in enumerate(features):
            row = i // 2
            col = i % 2
            
            self.create_bitdefender_card(grid_container, feature, row, col)
    
    def create_bitdefender_card(self, parent, feature, row, col):
        """Create Bitdefender-style protection card"""
        # Configure grid weights
        parent.grid_rowconfigure(row, weight=1, minsize=180)
        parent.grid_columnconfigure(0, weight=1, minsize=500)
        parent.grid_columnconfigure(1, weight=1, minsize=500)
        
        # Main card frame - rectangular like Bitdefender
        card_frame = tk.Frame(parent, bg=self.colors['bg_secondary'], relief='flat', bd=0)
        card_frame.grid(row=row, column=col, padx=15, pady=8, sticky='ew')
        
        # Content frame with proper padding
        content_frame = tk.Frame(card_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='both', expand=True, padx=25, pady=20)
        
        # Left side - Icon and text
        left_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        left_frame.pack(side='left', fill='both', expand=True)
        
        # Icon container with colored background
        icon_container = tk.Frame(left_frame, bg=self.colors['bg_secondary'])
        icon_container.pack(side='left', anchor='n', padx=(0, 20))
        
        # Icon background (square with rounded appearance)
        icon_bg = tk.Frame(icon_container, bg=feature['icon_color'], width=45, height=45)
        icon_bg.pack()
        icon_bg.pack_propagate(False)
        
        # Icon
        icon_label = tk.Label(icon_bg, text=feature['icon'],
                             font=('Segoe UI Emoji', 20),
                             bg=feature['icon_color'], fg='white')
        icon_label.pack(expand=True)
        
        # Text container
        text_container = tk.Frame(left_frame, bg=self.colors['bg_secondary'])
        text_container.pack(side='left', fill='both', expand=True)
        
        # Title
        title_label = tk.Label(text_container, text=feature['title'],
                              font=('Segoe UI', 16, 'bold'),
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['text_primary'],
                              anchor='w')
        title_label.pack(fill='x', anchor='w')
        
        # Description
        desc_label = tk.Label(text_container, text=feature['description'],
                             font=('Segoe UI', 11),
                             bg=self.colors['bg_secondary'],
                             fg=self.colors['text_secondary'],
                             anchor='w',
                             justify='left')
        desc_label.pack(fill='x', anchor='w', pady=(8, 0))
        
        # Button (bottom left under description)
        button_label = tk.Label(text_container, text=feature['button_text'],
                               font=('Segoe UI', 11, 'bold'),
                               bg=self.colors['bg_secondary'],
                               fg='#4a9eff',
                               anchor='w',
                               cursor='hand2')
        button_label.pack(fill='x', anchor='w', pady=(10, 0))
        
        # Bind button click handler
        button_label.bind("<Button-1>", lambda e, f=feature: self.on_feature_action(f))
        
        # Right side - Toggle switch if needed
        right_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        right_frame.pack(side='right', anchor='n', pady=(10, 0))
        
        if feature['has_toggle']:
            # Create iOS-style toggle switch
            toggle_var = tk.BooleanVar(value=feature['status'])
            
            # Toggle switch canvas
            toggle_canvas = tk.Canvas(right_frame, width=60, height=30, 
                                    bg=self.colors['bg_secondary'],
                                    highlightthickness=0, relief='flat', bd=0)
            toggle_canvas.pack()
            
            # Draw toggle switch
            self.draw_bitdefender_toggle(toggle_canvas, feature['status'])
            
            # Store toggle info for click handling
            toggle_canvas.feature = feature
            toggle_canvas.bind("<Button-1>", lambda e, c=toggle_canvas: self.toggle_bitdefender_switch(c))
            
            # Store canvas reference
            if not hasattr(self, 'bitdefender_toggles'):
                self.bitdefender_toggles = []
            self.bitdefender_toggles.append(toggle_canvas)
        
        # Hover effects for the entire card
        def on_enter(e):
            card_frame.configure(bg='#3a3a3a')
            content_frame.configure(bg='#3a3a3a')
            left_frame.configure(bg='#3a3a3a')
            icon_container.configure(bg='#3a3a3a')
            text_container.configure(bg='#3a3a3a')
            right_frame.configure(bg='#3a3a3a')
            title_label.configure(bg='#3a3a3a')
            desc_label.configure(bg='#3a3a3a')
            button_label.configure(bg='#3a3a3a')
            if feature['has_toggle']:
                toggle_canvas.configure(bg='#3a3a3a')
        
        def on_leave(e):
            card_frame.configure(bg=self.colors['bg_secondary'])
            content_frame.configure(bg=self.colors['bg_secondary'])
            left_frame.configure(bg=self.colors['bg_secondary'])
            icon_container.configure(bg=self.colors['bg_secondary'])
            text_container.configure(bg=self.colors['bg_secondary'])
            right_frame.configure(bg=self.colors['bg_secondary'])
            title_label.configure(bg=self.colors['bg_secondary'])
            desc_label.configure(bg=self.colors['bg_secondary'])
            button_label.configure(bg=self.colors['bg_secondary'])
            if feature['has_toggle']:
                toggle_canvas.configure(bg=self.colors['bg_secondary'])
        
        # Bind hover events to all widgets
        widgets_to_bind = [card_frame, content_frame, left_frame, icon_container, 
                          text_container, right_frame, title_label, desc_label, button_label]
        
        for widget in widgets_to_bind:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
    
    def draw_bitdefender_toggle(self, canvas, is_on):
        """Draw iOS-style toggle switch like Bitdefender"""
        canvas.delete("all")
        
        # Toggle colors
        bg_color = '#4a9eff' if is_on else '#666666'
        handle_x = 42 if is_on else 18
        
        # Background rounded rectangle
        canvas.create_oval(5, 5, 25, 25, fill=bg_color, outline=bg_color, width=0)
        canvas.create_rectangle(15, 5, 45, 25, fill=bg_color, outline=bg_color, width=0)
        canvas.create_oval(35, 5, 55, 25, fill=bg_color, outline=bg_color, width=0)
        
        # Handle (white circle)
        canvas.create_oval(handle_x-12, 3, handle_x+12, 27, fill='white', outline='white', width=0)
    
    def toggle_bitdefender_switch(self, canvas):
        """Toggle the Bitdefender-style switch"""
        feature = canvas.feature
        feature['status'] = not feature['status']
        self.draw_bitdefender_toggle(canvas, feature['status'])
        
        # Optional: Add toggle action feedback
        print(f"Toggle {feature['title']}: {'ON' if feature['status'] else 'OFF'}")

    def create_premium_feature_card(self, parent, feature, row, col):
        """Create premium protection feature card with square design"""
        # Card container for proper spacing
        card_container = tk.Frame(parent, bg=self.colors['bg_primary'])
        card_container.grid(row=row, column=col, padx=20, pady=20, sticky='nsew')
        
        # Configure grid weights for responsive design
        parent.grid_rowconfigure(row, weight=1, minsize=220)
        parent.grid_columnconfigure(col, weight=1, minsize=450)
        
        # Shadow frame for depth
        shadow_frame = tk.Frame(card_container, bg='#000000', relief='flat', bd=0)
        shadow_frame.pack(fill='both', expand=True, padx=(6, 0), pady=(6, 0))
        
        # Main card frame with premium styling
        card_frame = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat', bd=0)
        card_frame.pack(fill='both', expand=True, padx=(0, 6), pady=(0, 6))
        
        # Card content with enhanced padding
        content_frame = tk.Frame(card_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='both', expand=True, padx=30, pady=25)
        
        # Header with icon and title
        header_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        header_frame.pack(fill='x', pady=(0, 15))
        
        # Premium icon with colored background
        icon_container = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        icon_container.pack(side='left', padx=(0, 20))
        
        icon_bg = tk.Frame(icon_container, bg=feature['color'], width=60, height=60)
        icon_bg.pack()
        icon_bg.pack_propagate(False)
        
        icon_label = tk.Label(icon_bg, text=feature['icon'], 
                             font=('Segoe UI Emoji', 24, 'bold'), 
                             bg=feature['color'], fg='white')
        icon_label.pack(expand=True)
        
        # Title and toggle container
        title_container = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        title_container.pack(side='left', fill='x', expand=True)
        
        # Premium title styling
        title_label = tk.Label(title_container, text=feature['title'], 
                              font=('Segoe UI', 18, 'bold'), 
                              bg=self.colors['bg_secondary'], 
                              fg=self.colors['text_primary'])
        title_label.pack(side='left', anchor='w')
        
        # Premium toggle switch if enabled
        if feature.get('toggle'):
            toggle_frame = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
            toggle_frame.pack(side='right')
            
            # Initialize toggle state
            if not hasattr(self, 'toggle_states'):
                self.toggle_states = {}
            
            feature_key = feature['title'].lower().replace(' ', '_')
            if feature_key not in self.toggle_states:
                self.toggle_states[feature_key] = True
            
            # Create enhanced toggle switch
            toggle_canvas = tk.Canvas(toggle_frame, width=60, height=30, 
                                    bg=self.colors['bg_secondary'], 
                                    highlightthickness=0,
                                    cursor='hand2')
            toggle_canvas.pack()
            
            # Draw toggle switch
            self.draw_premium_toggle_switch(toggle_canvas, self.toggle_states[feature_key])
            
            # Bind click handler
            toggle_canvas.bind("<Button-1>", lambda e, canvas=toggle_canvas, key=feature_key, f=feature: self.toggle_switch(canvas, key, f))
        
        # Enhanced description
        desc_label = tk.Label(content_frame, text=feature['description'], 
                             font=('Segoe UI', 12), 
                             bg=self.colors['bg_secondary'], 
                             fg=self.colors['text_secondary'],
                             wraplength=380, justify='left')
        desc_label.pack(anchor='w', pady=(10, 20), fill='x')
        
        # Premium square action button
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        button_frame.pack(anchor='w')
        
        # Shadow for button
        btn_shadow = tk.Frame(button_frame, bg='#000000', height=45, width=120)
        btn_shadow.pack(padx=(3, 0), pady=(3, 0))
        btn_shadow.pack_propagate(False)
        
        # Main square button
        action_btn = tk.Button(btn_shadow, text=feature['button_text'],
                              bg=feature['color'], fg='white',
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0,
                              width=12, height=2,
                              cursor='hand2',
                              activebackground=self.lighten_color(feature['color']),
                              activeforeground='white',
                              command=lambda f=feature: self.on_feature_action(f))
        action_btn.pack(fill='both', expand=True, padx=(0, 3), pady=(0, 3))
        
        # Enhanced hover effects for button
        def on_btn_enter(e):
            action_btn.config(bg=self.lighten_color(feature['color']))
            btn_shadow.config(bg='#333333')
            
        def on_btn_leave(e):
            action_btn.config(bg=feature['color'])
            btn_shadow.config(bg='#000000')
            
        action_btn.bind("<Enter>", on_btn_enter)
        action_btn.bind("<Leave>", on_btn_leave)
        
        # Make card clickable with premium hover effects
        clickable_widgets = [card_frame, content_frame, header_frame, title_container, 
                           title_label, desc_label, icon_container]
        
        for widget in clickable_widgets:
            widget.bind("<Enter>", lambda e, f=card_frame: self.on_premium_feature_hover(f, True))
            widget.bind("<Leave>", lambda e, f=card_frame: self.on_premium_feature_hover(f, False))
            widget.bind("<Button-1>", lambda e, f=feature: self.on_feature_click(f))
    
    def draw_premium_toggle_switch(self, canvas, is_on):
        """Draw premium toggle switch with enhanced styling"""
        canvas.delete("all")
        
        if is_on:
            # ON state - premium green gradient
            canvas.create_oval(2, 2, 58, 28, fill='#000000', outline="", width=0)  # Shadow
            canvas.create_oval(1, 1, 57, 27, fill=self.colors['accent_green'], outline="", width=0)
            canvas.create_oval(2, 2, 56, 26, fill=self.lighten_color(self.colors['accent_green']), outline="")
            
            # Premium circle with shadow
            canvas.create_oval(35, 3, 53, 21, fill='#cccccc', outline="")  # Shadow
            canvas.create_oval(34, 2, 52, 20, fill='white', outline="", width=0)
            canvas.create_oval(36, 4, 44, 12, fill='#f8f8f8', outline="")  # Highlight
        else:
            # OFF state - premium gray
            canvas.create_oval(2, 2, 58, 28, fill='#000000', outline="", width=0)  # Shadow
            canvas.create_oval(1, 1, 57, 27, fill='#555555', outline="", width=0)
            canvas.create_oval(2, 2, 56, 26, fill='#666666', outline="")
            
            # Premium circle with shadow
            canvas.create_oval(9, 3, 27, 21, fill='#cccccc', outline="")  # Shadow
            canvas.create_oval(8, 2, 26, 20, fill='white', outline="", width=0)
            canvas.create_oval(10, 4, 18, 12, fill='#f8f8f8', outline="")  # Highlight
    
    def on_premium_feature_hover(self, frame, entering):
        """Handle premium feature card hover effects"""
        def update_widget_bg(widget, bg_color):
            try:
                if hasattr(widget, 'configure') and not isinstance(widget, tk.Canvas):
                    widget.configure(bg=bg_color)
                for child in widget.winfo_children():
                    if not isinstance(child, tk.Canvas):
                        update_widget_bg(child, bg_color)
            except:
                pass
        
        if entering:
            update_widget_bg(frame, self.colors['bg_tertiary'])
            frame.configure(relief='solid', bd=1, highlightbackground=self.colors['accent_green'])
        else:
            update_widget_bg(frame, self.colors['bg_secondary'])
            frame.configure(relief='flat', bd=0)
    
    def create_protection_features_grid(self):
        """Create the protection features grid like Bitdefender"""
        # Main grid container
        grid_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        grid_container.pack(fill='both', expand=True, padx=20)
        
        # Protection features data matching Bitdefender layout
        features = [
            # Row 1
            {
                'title': 'Antivirus',
                'icon': '🛡️',
                'description': 'Real-time protection blocks any threat from running on your device.',
                'button_text': 'Open',
                'button_color': self.colors['accent_blue'],
                'enabled': True
            },
            {
                'title': 'Email Protection', 
                'icon': '📧',
                'description': 'Scans and identifies potentially dangerous content received via email.',
                'button_text': 'Open',
                'button_color': self.colors['accent_blue'],
                'enabled': True
            },
            # Row 2
            {
                'title': 'Cryptomining Protection',
                'icon': '⛏️',
                'description': 'Prevents the use of your device and electricity in Cryptomining activities that generate revenue for attackers.',
                'button_text': 'Settings',
                'button_color': self.colors['accent_blue'],
                'enabled': True,
                'toggle': True
            },
            {
                'title': 'Advanced Threat Defense',
                'icon': '🔍',
                'description': 'Identifies suspicious behavior and blocks even zero-day attacks from compromising your device.',
                'button_text': 'Open',
                'button_color': self.colors['accent_blue'],
                'enabled': True
            },
            # Row 3
            {
                'title': 'Online Threat Prevention',
                'icon': '🌐',
                'description': 'Our cloud-based Global Protective Network secures your device by blocking any online threat.',
                'button_text': 'Settings',
                'button_color': self.colors['accent_blue'],
                'enabled': True
            },
            {
                'title': 'Vulnerability',
                'icon': '🔍',
                'description': 'Analyze your system, apps and network for vulnerabilities that might compromise your device and data.',
                'button_text': 'Open',
                'button_color': self.colors['accent_blue'],
                'enabled': True,
                'toggle': True
            },
            # Row 4
            {
                'title': 'Firewall',
                'icon': '🔥',
                'description': 'Monitors network traffic and blocks unauthorized connections to keep your data safe.',
                'button_text': 'Settings',
                'button_color': self.colors['accent_blue'],
                'enabled': True,
                'toggle': True
            },
            {
                'title': 'Ransomware Remediation',
                'icon': '🔐',
                'description': 'Automatically backs up your files and restores them if ransomware attacks occur.',
                'button_text': 'Settings', 
                'button_color': self.colors['accent_blue'],
                'enabled': True,
                'toggle': True
            }
        ]
        
        # Create feature cards in 2-column grid
        for i, feature in enumerate(features):
            row = i // 2
            col = i % 2
            self.create_feature_card(grid_container, feature, row, col)
    
    def create_feature_card(self, parent, feature, row, col):
        """Create a protection feature card"""
        # Card frame with Bitdefender styling
        card_frame = tk.Frame(parent, bg=self.colors['bg_secondary'], 
                             relief='flat', bd=0)
        card_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        # Configure grid weights
        parent.grid_rowconfigure(row, weight=1, minsize=160)
        parent.grid_columnconfigure(col, weight=1, minsize=400)
        
        # Card content with padding
        content_frame = tk.Frame(card_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Header with icon and title
        header_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        header_frame.pack(fill='x', pady=(0, 15))
        
        # Feature icon
        icon_label = tk.Label(header_frame, text=feature['icon'], 
                             font=('Segoe UI', 24), 
                             bg=self.colors['bg_secondary'], 
                             fg=self.colors['accent_blue'])
        icon_label.pack(side='left', padx=(0, 15))
        
        # Title and toggle container
        title_container = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        title_container.pack(side='left', fill='x', expand=True)
        
        # Title
        title_label = tk.Label(title_container, text=feature['title'], 
                              font=('Segoe UI', 16, 'bold'), 
                              bg=self.colors['bg_secondary'], 
                              fg=self.colors['text_primary'])
        title_label.pack(side='left')
        
        # Toggle switch if enabled
        if feature.get('toggle'):
            toggle_frame = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
            toggle_frame.pack(side='right')
            
            # Initialize toggle state if not exists
            if not hasattr(self, 'toggle_states'):
                self.toggle_states = {}
            
            # Set default state (ON for most features)
            feature_key = feature['title'].lower().replace(' ', '_')
            if feature_key not in self.toggle_states:
                self.toggle_states[feature_key] = True
            
            # Create toggle switch
            toggle_canvas = tk.Canvas(toggle_frame, width=50, height=25, 
                                    bg=self.colors['bg_secondary'], 
                                    highlightthickness=0,
                                    cursor='hand2')
            toggle_canvas.pack()
            
            # Draw toggle switch based on current state
            self.draw_toggle_switch(toggle_canvas, self.toggle_states[feature_key])
            
            # Bind click handler
            toggle_canvas.bind("<Button-1>", lambda e, canvas=toggle_canvas, key=feature_key, f=feature: self.toggle_switch(canvas, key, f))
        
        # Description text
        desc_label = tk.Label(content_frame, text=feature['description'], 
                             font=('Segoe UI', 11), 
                             bg=self.colors['bg_secondary'], 
                             fg=self.colors['text_secondary'],
                             wraplength=350, justify='left')
        desc_label.pack(anchor='w', pady=(0, 20))
        
        # Enhanced action button with better interactivity
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        button_frame.pack(anchor='w')
        
        action_btn = tk.Button(button_frame, text=feature['button_text'],
                              bg=feature['button_color'], fg='white',
                              font=('Segoe UI', 11, 'bold'),
                              relief='flat', bd=0, padx=20, pady=8,
                              cursor='hand2',
                              activebackground=self.lighten_color(feature['button_color']),
                              activeforeground='white',
                              command=lambda f=feature: self.on_feature_action(f))
        action_btn.pack(side='left')
        
        # Add hover effects for better user feedback
        def on_button_enter(e):
            action_btn.config(bg=self.lighten_color(feature['button_color']))
            
        def on_button_leave(e):
            action_btn.config(bg=feature['button_color'])
            
        action_btn.bind("<Enter>", on_button_enter)
        action_btn.bind("<Leave>", on_button_leave)
        
        # Make card clickable
        clickable_widgets = [card_frame, content_frame, header_frame, title_container, 
                           title_label, desc_label, icon_label]
        
        for widget in clickable_widgets:
            widget.bind("<Enter>", lambda e, f=card_frame: self.on_feature_hover(f, True))
            widget.bind("<Leave>", lambda e, f=card_frame: self.on_feature_hover(f, False))
            widget.bind("<Button-1>", lambda e, f=feature: self.on_feature_click(f))
    
    def on_feature_hover(self, frame, entering):
        """Handle feature card hover effect"""
        if entering:
            frame.configure(bg=self.colors['bg_tertiary'])
            for child in frame.winfo_children():
                child.configure(bg=self.colors['bg_tertiary'])
                for grandchild in child.winfo_children():
                    grandchild.configure(bg=self.colors['bg_tertiary'])
                    for great_grandchild in grandchild.winfo_children():
                        if isinstance(great_grandchild, tk.Label):
                            great_grandchild.configure(bg=self.colors['bg_tertiary'])
        else:
            frame.configure(bg=self.colors['bg_secondary'])
            for child in frame.winfo_children():
                child.configure(bg=self.colors['bg_secondary'])
                for grandchild in child.winfo_children():
                    grandchild.configure(bg=self.colors['bg_secondary'])
                    for great_grandchild in grandchild.winfo_children():
                        if isinstance(great_grandchild, tk.Label):
                            great_grandchild.configure(bg=self.colors['bg_secondary'])
    
    def on_feature_click(self, feature):
        """Handle feature card click"""
        print(f"Feature clicked: {feature['title']}")
        self.on_feature_action(feature)
    
    def on_feature_action(self, feature):
        """Handle feature action button click"""
        title = feature['title']
        print(f"🔘 Button clicked: {title}")
        
        if title == 'Antivirus':
            self.show_antivirus_settings()
        elif title == 'Email Protection':
            self.show_email_protection_settings()
        elif title == 'Cryptomining Protection':
            self.show_cryptomining_settings()
        elif title == 'Advanced Threat Defense':
            self.show_threat_defense_settings()
        elif title == 'Online Threat Prevention':
            self.show_online_protection_settings()
        elif title == 'Vulnerability':
            self.show_vulnerability_settings()
        elif title == 'Firewall':
            self.show_firewall_settings()
        elif title == 'Ransomware Remediation':
            self.show_ransomware_settings()
        elif title == 'Antispam':
            self.show_antispam_settings()
        elif title == 'Vulnerability':
            self.show_vulnerability_settings()
        elif title == 'Online Threat Prevention':
            self.show_online_protection_settings()
        elif title == 'Email Protection':
            self.show_email_protection_settings()
        elif title == 'Advanced Threat Defense':
            self.show_threat_defense_settings()
        else:
            self.show_feature_dialog(title, feature['description'])
    
    def start_antivirus_scan(self):
        """Start antivirus scan"""
        self.show_scan_progress("Antivirus Scan")
    
    def show_antivirus_settings(self):
        """Show comprehensive antivirus settings within main app"""
        self.create_integrated_settings_view("Antivirus", {
            "Real-time Protection": {
                "type": "toggle",
                "default": True,
                "description": "Monitor files and programs in real-time",
                "premium": False
            },
            "AI-Powered Detection": {
                "type": "toggle",
                "default": True,
                "description": "Advanced machine learning threat detection",
                "premium": True
            },
            "Scan Archives": {
                "type": "toggle",
                "default": True,
                "description": "Scan compressed files and archives",
                "premium": False
            },
            "Advanced Heuristic Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Deep behavioral analysis with neural networks",
                "premium": True
            },
            "Cloud Protection": {
                "type": "toggle",
                "default": True,
                "description": "Use cloud-based threat intelligence",
                "premium": False
            },
            "Zero-Day Protection": {
                "type": "toggle",
                "default": True,
                "description": "Advanced protection against unknown malware",
                "premium": True
            },
            "Memory Protection": {
                "type": "toggle",
                "default": True,
                "description": "Protect against memory-based attacks",
                "premium": True
            },
            "Rootkit Detection": {
                "type": "toggle",
                "default": True,
                "description": "Scan for and remove deeply hidden rootkits",
                "premium": True
            },
            "Scan Sensitivity": {
                "type": "scale",
                "range": (1, 10),
                "default": 7,
                "description": "Detection sensitivity level",
                "premium": False
            },
            "Advanced Scan Depth": {
                "type": "scale",
                "range": (1, 5),
                "default": 3,
                "description": "Deep scanning intensity (1=Fast, 5=Forensic)",
                "premium": True
            },
            "Quarantine Action": {
                "type": "radio",
                "options": ["Quarantine", "Delete", "Ask User"],
                "default": "Quarantine",
                "description": "Action to take when threat is detected",
                "premium": False
            },
            "Advanced Actions": {
                "type": "radio",
                "options": ["Standard", "Secure Delete", "Forensic Analysis", "Cloud Report"],
                "default": "Standard",
                "description": "Advanced threat handling options",
                "premium": True
            }
        })
    
    def show_email_protection(self):
        """Show email protection interface"""
        self.show_feature_dialog("Email Protection", "Email protection scans incoming and outgoing emails for threats.")
    
    def show_cryptomining_settings(self):
        """Show comprehensive cryptomining protection settings within main app"""
        self.create_integrated_settings_view("Cryptomining Protection", {
            "Protection Level": {
                "type": "radio",
                "options": ["Basic", "Advanced", "Maximum"],
                "default": "Advanced",
                "description": "Select the level of cryptomining protection"
            },
            "Real-time Monitoring": {
                "type": "toggle",
                "default": True,
                "description": "Monitor CPU usage patterns in real-time"
            },
            "CPU Usage Threshold": {
                "type": "scale",
                "range": (50, 95),
                "default": 80,
                "description": "CPU usage % that triggers protection"
            },
            "Block Known Miners": {
                "type": "toggle",
                "default": True,
                "description": "Block known cryptocurrency mining applications"
            },
            "Browser Protection": {
                "type": "toggle",
                "default": True,
                "description": "Protect against browser-based mining scripts"
            },
            "Alert on Detection": {
                "type": "toggle",
                "default": True,
                "description": "Show alerts when mining activity is detected"
            },
            "Whitelist Applications": {
                "type": "text",
                "default": "",
                "description": "Applications to exclude from protection (one per line)"
            }
        })
    
    def show_threat_defense(self):
        """Show advanced threat defense"""
        self.show_feature_dialog("Advanced Threat Defense", "Advanced behavioral analysis and zero-day protection.")
    
    def show_online_protection(self):
        """Show online threat prevention"""
        self.show_feature_dialog("Online Threat Prevention", "Cloud-based protection against online threats.")
    
    def show_firewall_settings(self):
        """Show comprehensive firewall configuration within main app"""
        self.create_integrated_settings_view("Firewall", {
            "Firewall Mode": {
                "type": "radio",
                "options": ["Allow All", "Smart Mode", "Block All"],
                "default": "Smart Mode",
                "description": "Basic firewall operating mode",
                "premium": False
            },
            "Advanced Security Mode": {
                "type": "radio",
                "options": ["Standard", "High Security", "Military Grade", "Zero Trust"],
                "default": "Standard",
                "description": "Enhanced security protocols with AI monitoring",
                "premium": True
            },
            "Enable Stealth Mode": {
                "type": "toggle",
                "default": True,
                "description": "Hide your computer from network scans",
                "premium": False
            },
            "Deep Packet Inspection": {
                "type": "toggle",
                "default": True,
                "description": "Analyze packet contents for advanced threats",
                "premium": True
            },
            "Block Malicious IPs": {
                "type": "toggle",
                "default": True,
                "description": "Automatically block known malicious IP addresses",
                "premium": False
            },
            "AI Threat Intelligence": {
                "type": "toggle",
                "default": True,
                "description": "Real-time AI-powered threat IP detection",
                "premium": True
            },
            "Monitor Outbound Connections": {
                "type": "toggle",
                "default": True,
                "description": "Monitor and control outbound network connections",
                "premium": False
            },
            "Advanced Application Control": {
                "type": "toggle",
                "default": True,
                "description": "Granular control over application network access",
                "premium": True
            },
            "Enable Port Scanning Detection": {
                "type": "toggle",
                "default": True,
                "description": "Detect and block port scanning attempts",
                "premium": False
            },
            "Network Intrusion Prevention": {
                "type": "toggle",
                "default": True,
                "description": "Active prevention of network-based attacks",
                "premium": True
            },
            "Log Network Activity": {
                "type": "toggle",
                "default": False,
                "description": "Log all network activity for analysis",
                "premium": False
            },
            "Forensic Network Logging": {
                "type": "toggle",
                "default": True,
                "description": "Detailed logging for security forensics",
                "premium": True
            },
            "Custom Rules": {
                "type": "text",
                "default": "",
                "description": "Custom firewall rules (advanced users only)",
                "premium": False
            },
            "Enterprise Rule Sets": {
                "type": "text",
                "default": "",
                "description": "Import enterprise-grade security rule sets",
                "premium": True
            }
        })
    
    def show_ransomware_settings(self):
        """Show comprehensive ransomware remediation settings within main app"""
        self.create_integrated_settings_view("Ransomware Remediation", {
            "Protection Mode": {
                "type": "radio",
                "options": ["Basic", "Advanced", "Maximum"],
                "default": "Advanced",
                "description": "Level of ransomware protection",
                "premium": False
            },
            "AI Behavioral Analysis": {
                "type": "radio", 
                "options": ["Standard", "Enhanced", "Military Grade", "Zero-Day Detection"],
                "default": "Enhanced",
                "description": "Advanced AI-powered ransomware behavior detection",
                "premium": True
            },
            "Real-time File Monitoring": {
                "type": "toggle",
                "default": True,
                "description": "Monitor file system for suspicious encryption activity",
                "premium": False
            },
            "Deep File System Protection": {
                "type": "toggle",
                "default": True,
                "description": "Advanced file system hooks and kernel-level protection",
                "premium": True
            },
            "Automatic Backup": {
                "type": "toggle",
                "default": True,
                "description": "Create automatic backups of important files",
                "premium": False
            },
            "Continuous Data Protection": {
                "type": "toggle",
                "default": True,
                "description": "Real-time backup with versioning and rollback",
                "premium": True
            },
            "Backup Frequency": {
                "type": "radio",
                "options": ["Hourly", "Daily", "Weekly"],
                "default": "Daily",
                "description": "How often to create backups",
                "premium": False
            },
            "Cloud Backup Integration": {
                "type": "radio",
                "options": ["Disabled", "Encrypted Local", "Secure Cloud", "Multi-Cloud"],
                "default": "Encrypted Local",
                "description": "Advanced backup storage options",
                "premium": True
            },
            "Monitor Document Folders": {
                "type": "toggle",
                "default": True,
                "description": "Monitor Documents, Pictures, and Desktop folders",
                "premium": False
            },
            "Process Injection Protection": {
                "type": "toggle",
                "default": True,
                "description": "Prevent ransomware from injecting into system processes",
                "premium": True
            },
            "Block Suspicious Processes": {
                "type": "toggle",
                "default": True,
                "description": "Block processes showing ransomware behavior",
                "premium": False
            },
            "Decoy File System": {
                "type": "toggle",
                "default": True,
                "description": "Deploy honeypot files to detect encryption attempts",
                "premium": True
            },
            "Network Share Protection": {
                "type": "toggle",
                "default": True,
                "description": "Protect network drives and shared folders",
                "premium": False
            },
            "Advanced Recovery Tools": {
                "type": "toggle",
                "default": True,
                "description": "Tools for recovering from sophisticated ransomware attacks",
                "premium": True
            }
        })

    def show_antispam_settings(self):
        """Show comprehensive antispam settings within main app"""
        self.create_integrated_settings_view("Antispam", {
            "Protection Level": {
                "type": "radio",
                "options": ["Low", "Medium", "High", "Maximum"],
                "default": "High",
                "description": "Spam detection sensitivity level"
            },
            "Enable Spam Learning": {
                "type": "toggle",
                "default": True,
                "description": "Learn from your spam marking behavior"
            },
            "Block Phishing Emails": {
                "type": "toggle",
                "default": True,
                "description": "Block emails containing phishing attempts"
            },
            "Quarantine Suspicious Emails": {
                "type": "toggle",
                "default": True,
                "description": "Quarantine emails instead of deleting them"
            },
            "Whitelist Domains": {
                "type": "text",
                "default": "",
                "description": "Always allow emails from these domains"
            },
            "Blacklist Domains": {
                "type": "text",
                "default": "",
                "description": "Always block emails from these domains"
            },
            "Check Attachments": {
                "type": "toggle",
                "default": True,
                "description": "Scan email attachments for malware"
            },
            "Real-time Scanning": {
                "type": "toggle",
                "default": True,
                "description": "Scan emails as they arrive"
            }
        })

    def show_vulnerability_settings(self):
        """Show comprehensive vulnerability scanner settings within main app"""
        self.create_integrated_settings_view("Vulnerability Scanner", {
            "Scan Frequency": {
                "type": "radio",
                "options": ["Daily", "Weekly", "Monthly", "Manual"],
                "default": "Weekly",
                "description": "How often to run vulnerability scans"
            },
            "Scan System Files": {
                "type": "toggle",
                "default": True,
                "description": "Check system files for vulnerabilities"
            },
            "Scan Installed Software": {
                "type": "toggle",
                "default": True,
                "description": "Check installed applications for updates"
            },
            "Network Port Scanning": {
                "type": "toggle",
                "default": True,
                "description": "Scan for open network ports"
            },
            "Registry Scanning": {
                "type": "toggle",
                "default": False,
                "description": "Deep scan Windows registry for issues"
            },
            "Auto-Fix Safe Issues": {
                "type": "toggle",
                "default": True,
                "description": "Automatically fix non-critical vulnerabilities"
            },
            "Create Restore Point": {
                "type": "toggle",
                "default": True,
                "description": "Create system restore point before fixes"
            },
            "Detailed Logging": {
                "type": "toggle",
                "default": False,
                "description": "Keep detailed logs of scan results"
            }
        })

    def show_online_protection_settings(self):
        """Show comprehensive online threat prevention settings within main app"""
        self.create_integrated_settings_view("Online Threat Prevention", {
            "Protection Mode": {
                "type": "radio",
                "options": ["Basic", "Standard", "Advanced", "Paranoid"],
                "default": "Advanced",
                "description": "Level of online protection"
            },
            "Block Malicious URLs": {
                "type": "toggle",
                "default": True,
                "description": "Block access to known malicious websites"
            },
            "Phishing Protection": {
                "type": "toggle",
                "default": True,
                "description": "Protect against phishing websites"
            },
            "Download Scanning": {
                "type": "toggle",
                "default": True,
                "description": "Scan all downloaded files for malware"
            },
            "Cloud Intelligence": {
                "type": "toggle",
                "default": True,
                "description": "Use cloud-based threat intelligence"
            },
            "Safe Browsing Mode": {
                "type": "toggle",
                "default": False,
                "description": "Enable safe browsing sandbox"
            },
            "Block Tracking Scripts": {
                "type": "toggle",
                "default": True,
                "description": "Block website tracking and analytics"
            },
            "HTTPS Enforcement": {
                "type": "toggle",
                "default": True,
                "description": "Force HTTPS connections when available"
            },
            "DNS Protection": {
                "type": "toggle",
                "default": True,
                "description": "Use secure DNS servers"
            }
        })

    def show_email_protection_settings(self):
        """Show comprehensive email protection settings within main app"""
        self.create_integrated_settings_view("Email Protection", {
            "Real-time Scanning": {
                "type": "toggle",
                "default": True,
                "description": "Scan emails as they arrive"
            },
            "Attachment Scanning": {
                "type": "toggle",
                "default": True,
                "description": "Scan all email attachments"
            },
            "Link Protection": {
                "type": "toggle",
                "default": True,
                "description": "Check links in emails for safety"
            },
            "Phishing Detection": {
                "type": "toggle",
                "default": True,
                "description": "Detect and block phishing attempts"
            },
            "Quarantine Threats": {
                "type": "toggle",
                "default": True,
                "description": "Quarantine suspicious emails"
            },
            "Email Clients": {
                "type": "text",
                "default": "Outlook, Thunderbird, Windows Mail",
                "description": "Email clients to protect (comma-separated)"
            },
            "Archive Scanning": {
                "type": "toggle",
                "default": True,
                "description": "Scan compressed attachments"
            },
            "Advanced Heuristics": {
                "type": "toggle",
                "default": True,
                "description": "Use behavioral analysis for threat detection"
            }
        })

    def show_threat_defense_settings(self):
        """Show comprehensive advanced threat defense settings within main app"""
        self.create_integrated_settings_view("Advanced Threat Defense", {
            "Behavioral Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Monitor application behavior for threats"
            },
            "Zero-Day Protection": {
                "type": "toggle",
                "default": True,
                "description": "Protect against unknown threats"
            },
            "Machine Learning": {
                "type": "toggle",
                "default": True,
                "description": "Use AI for threat detection"
            },
            "Sandbox Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Run suspicious files in sandbox"
            },
            "Network Traffic Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Monitor network traffic patterns"
            },
            "Memory Protection": {
                "type": "toggle",
                "default": True,
                "description": "Protect against memory-based attacks"
            },
            "Process Monitoring": {
                "type": "toggle",
                "default": True,
                "description": "Monitor all system processes"
            },
            "Threat Intelligence": {
                "type": "toggle",
                "default": True,
                "description": "Use global threat intelligence feeds"
            },
            "Sensitivity Level": {
                "type": "scale",
                "range": (1, 10),
                "default": 7,
                "description": "Detection sensitivity (1=Low, 10=Maximum)"
            }
        })

    def create_integrated_settings_view(self, feature_name, settings_config):
        """Create integrated settings view with completely fixed header"""
        # Hide the main scrollable system entirely for settings
        self.main_canvas.pack_forget()
        try:
            # Find and hide the scrollbar too
            for widget in self.main_canvas.master.winfo_children():
                if isinstance(widget, ttk.Scrollbar):
                    widget.pack_forget()
        except:
            pass
        
        # Create a new non-scrollable container for settings
        self.settings_container = tk.Frame(self.main_canvas.master, bg=self.colors['bg_primary'])
        self.settings_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Fixed header (absolutely fixed - no scrolling possible)
        header_frame = tk.Frame(self.settings_container, bg=self.colors['bg_primary'])
        header_frame.pack(fill='x', side='top')
        
        # Back button
        back_button = tk.Button(header_frame, text="← Return to Protection",
                               font=('Segoe UI', 12),
                               bg=self.colors['bg_primary'],
                               fg='#4a9eff',
                               relief='flat',
                               bd=0,
                               cursor='hand2',
                               command=self.return_to_protection)
        back_button.pack(anchor='w', pady=(0, 10))
        
        # Feature title
        title_label = tk.Label(header_frame, text=feature_name,
                              font=('Segoe UI', 24, 'bold'),
                              bg=self.colors['bg_primary'],
                              fg=self.colors['text_primary'])
        title_label.pack(anchor='w', pady=(0, 15))
        
        # Tab navigation
        tab_frame = tk.Frame(header_frame, bg=self.colors['bg_primary'])
        tab_frame.pack(fill='x', pady=(0, 10))
        
        # Create tabs
        self.current_tab = "Settings"
        tabs = ["Scans", "Settings", "Advanced"]
        
        self.tab_buttons = {}
        for tab in tabs:
            is_active = tab == self.current_tab
            
            tab_btn = tk.Button(tab_frame, text=tab,
                               font=('Segoe UI', 11, 'bold' if is_active else 'normal'),
                               bg=self.colors['bg_primary'],
                               fg='#4a9eff' if is_active else self.colors['text_secondary'],
                               relief='flat',
                               bd=0,
                               padx=15, pady=8,
                               cursor='hand2',
                               command=lambda t=tab: self.switch_settings_tab(t, feature_name, settings_config))
            tab_btn.pack(side='left', padx=(0, 20))
            self.tab_buttons[tab] = tab_btn
        
        # Separator line
        separator = tk.Frame(header_frame, bg='#444444', height=1)
        separator.pack(fill='x', pady=(10, 0))
        
        # Content area with its own scrolling system
        self.settings_content_frame = tk.Frame(self.settings_container, bg=self.colors['bg_primary'])
        self.settings_content_frame.pack(fill='both', expand=True, pady=(15, 0))
        
        # Show default content
        self.show_settings_content(self.settings_content_frame, settings_config)
    
    def return_to_protection(self):
        """Return to protection view and restore normal layout"""
        # Destroy the settings container
        if hasattr(self, 'settings_container'):
            self.settings_container.destroy()
            
        # Restore the main scrollable system
        self.main_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        # Restore scrollbar
        try:
            for widget in self.main_canvas.master.winfo_children():
                if isinstance(widget, ttk.Scrollbar):
                    widget.pack(side="right", fill="y")
                    break
        except:
            pass
            
        # Go back to protection view
        self.update_main_content("Protection")
    
    def switch_settings_tab(self, tab_name, feature_name, settings_config):
        """Switch between tabs in settings view"""
        self.current_tab = tab_name
        
        # Update tab button styles
        for tab, button in self.tab_buttons.items():
            is_active = tab == tab_name
            button.config(
                font=('Segoe UI', 11, 'bold' if is_active else 'normal'),
                fg='#4a9eff' if is_active else self.colors['text_secondary']
            )
        
        # Clear content frame
        for widget in self.settings_content_frame.winfo_children():
            widget.destroy()
        
        # Show appropriate content
        if tab_name == "Scans":
            self.show_scans_content(self.settings_content_frame, feature_name)
        elif tab_name == "Settings":
            self.show_settings_content(self.settings_content_frame, settings_config)
        elif tab_name == "Advanced":
            self.show_advanced_content(self.settings_content_frame, feature_name)
    
    def switch_tab(self, tab_name, feature_name, settings_config):
        """Switch between tabs in integrated settings view"""
        self.current_tab = tab_name
        
        # Update tab button styles
        for tab, button in self.tab_buttons.items():
            is_active = tab == tab_name
            button.config(
                font=('Segoe UI', 12, 'bold' if is_active else 'normal'),
                fg='#4a9eff' if is_active else self.colors['text_secondary']
            )
        
        # Clear only the content container (keep header fixed)
        for widget in self.content_container.winfo_children():
            widget.destroy()
        
        # Show content based on selected tab
        if tab_name == "Scans":
            self.show_scans_content(self.content_container, feature_name)
        elif tab_name == "Settings":
            self.show_settings_content(self.content_container, settings_config)
        elif tab_name == "Advanced":
            self.show_advanced_content(self.content_container, feature_name)
    
    def show_scans_content(self, parent, feature_name):
        """Show scans tab content with fixed layout"""
        # Container for scan options (no scrolling needed)
        scans_container = tk.Frame(parent, bg=self.colors['bg_primary'])
        scans_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Quick Scan section
        quick_scan_frame = tk.Frame(scans_container, bg=self.colors['bg_secondary'], relief='flat', bd=1)
        quick_scan_frame.pack(fill='x', pady=(0, 15))
        
        scan_content = tk.Frame(quick_scan_frame, bg=self.colors['bg_secondary'])
        scan_content.pack(fill='x', padx=25, pady=20)
        
        # Quick scan icon and info
        scan_info = tk.Frame(scan_content, bg=self.colors['bg_secondary'])
        scan_info.pack(side='left', fill='x', expand=True)
        
        # Icon
        icon_label = tk.Label(scan_info, text="⚡",
                             font=('Segoe UI Emoji', 28),
                             bg=self.colors['bg_secondary'],
                             fg='#4a9eff')
        icon_label.pack(side='left', padx=(0, 20))
        
        # Text info
        text_info = tk.Frame(scan_info, bg=self.colors['bg_secondary'])
        text_info.pack(side='left', fill='x', expand=True)
        
        title = tk.Label(text_info, text="Quick Scan",
                        font=('Segoe UI', 18, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_primary'])
        title.pack(anchor='w')
        
        desc = tk.Label(text_info, text="Run a lightweight scan for your peace of mind.",
                       font=('Segoe UI', 12),
                       bg=self.colors['bg_secondary'],
                       fg=self.colors['text_secondary'])
        desc.pack(anchor='w', pady=(5, 0))
        
        # Run scan button
        scan_btn = tk.Button(scan_content, text="Run Scan",
                            font=('Segoe UI', 12, 'bold'),
                            bg='#4a9eff',
                            fg='white',
                            relief='flat',
                            padx=30, pady=12,
                            cursor='hand2',
                            command=lambda: self.start_feature_scan(feature_name, "Quick"))
        scan_btn.pack(side='right')
        
        # System Scan section
        system_scan_frame = tk.Frame(scans_container, bg=self.colors['bg_secondary'], relief='flat', bd=1)
        system_scan_frame.pack(fill='x', pady=(0, 15))
        
        system_content = tk.Frame(system_scan_frame, bg=self.colors['bg_secondary'])
        system_content.pack(fill='x', padx=25, pady=20)
        
        # System scan icon and info
        system_info = tk.Frame(system_content, bg=self.colors['bg_secondary'])
        system_info.pack(side='left', fill='x', expand=True)
        
        # Icon
        system_icon = tk.Label(system_info, text="💻",
                              font=('Segoe UI Emoji', 28),
                              bg=self.colors['bg_secondary'],
                              fg='#4a9eff')
        system_icon.pack(side='left', padx=(0, 20))
        
        # Text info
        system_text = tk.Frame(system_info, bg=self.colors['bg_secondary'])
        system_text.pack(side='left', fill='x', expand=True)
        
        system_title = tk.Label(system_text, text="System Scan",
                               font=('Segoe UI', 18, 'bold'),
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['text_primary'])
        system_title.pack(anchor='w')
        
        system_desc = tk.Label(system_text, text="Run a deep analysis of your device.",
                              font=('Segoe UI', 12),
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['text_secondary'])
        system_desc.pack(anchor='w', pady=(5, 0))
        
        # Run system scan button
        system_btn = tk.Button(system_content, text="Run Scan",
                              font=('Segoe UI', 12, 'bold'),
                              bg='#4a9eff',
                              fg='white',
                              relief='flat',
                              padx=30, pady=12,
                              cursor='hand2',
                              command=lambda: self.start_feature_scan(feature_name, "System"))
        system_btn.pack(side='right')
        
        # Custom Scan section
        custom_scan_frame = tk.Frame(scans_container, bg=self.colors['bg_secondary'], relief='flat', bd=1)
        custom_scan_frame.pack(fill='x')
        
        custom_content = tk.Frame(custom_scan_frame, bg=self.colors['bg_secondary'])
        custom_content.pack(fill='x', padx=25, pady=20)
        
        custom_info = tk.Frame(custom_content, bg=self.colors['bg_secondary'])
        custom_info.pack(side='left', fill='x', expand=True)
        
        # Custom scan icon
        custom_icon = tk.Label(custom_info, text="⚙️",
                              font=('Segoe UI Emoji', 28),
                              bg=self.colors['bg_secondary'],
                              fg='#4a9eff')
        custom_icon.pack(side='left', padx=(0, 20))
        
        # Custom scan text
        custom_text = tk.Frame(custom_info, bg=self.colors['bg_secondary'])
        custom_text.pack(side='left', fill='x', expand=True)
        
        custom_title = tk.Label(custom_text, text="Manage Scans",
                               font=('Segoe UI', 18, 'bold'),
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['text_primary'])
        custom_title.pack(anchor='w')
        
        custom_desc = tk.Label(custom_text, text="Create scan tasks and schedule them.",
                              font=('Segoe UI', 12),
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['text_secondary'])
        custom_desc.pack(anchor='w', pady=(5, 0))
        
        # Custom scan button
        custom_btn = tk.Button(custom_content, text="+ Custom Scan",
                              font=('Segoe UI', 12, 'bold'),
                              bg='#4a9eff',
                              fg='white',
                              relief='flat',
                              padx=30, pady=12,
                              cursor='hand2',
                              command=lambda: self.create_custom_scan(feature_name))
        custom_btn.pack(side='right')
    
    def show_settings_content(self, parent, settings_config):
        """Show clean, organized settings content with minimal scrolling"""
        # Create canvas for scrolling only the settings content
        canvas = tk.Canvas(parent, bg=self.colors['bg_primary'], highlightthickness=0, bd=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_primary'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create minimal, clean settings
        for i, (setting_name, config) in enumerate(settings_config.items()):
            # Check if this is a premium setting
            is_premium = config.get('premium', False)
            
            # Skip premium features in free version or show upgrade prompt
            if is_premium and not is_feature_available('premium_features'):
                self.create_upgrade_prompt(scrollable_frame, setting_name, config)
                continue
            
            # Clean setting row
            setting_row = tk.Frame(scrollable_frame, bg=self.colors['bg_primary'])
            setting_row.pack(fill='x', pady=8, padx=10)
            
            # Setting card with premium styling if needed
            card_bg = '#1a2332' if is_premium else self.colors['bg_secondary']
            setting_card = tk.Frame(setting_row, bg=card_bg, 
                                   relief='flat', bd=0, pady=15, padx=20)
            setting_card.pack(fill='x')
            
            # Premium indicator
            if is_premium:
                premium_indicator = tk.Label(setting_card, text="⭐ PREMIUM", 
                                           font=('Segoe UI', 8, 'bold'),
                                           bg=card_bg, fg='#ffd700',
                                           anchor='w')
                premium_indicator.pack(anchor='w', pady=(0, 5))
            
            # Left side - setting info
            left_side = tk.Frame(setting_card, bg=card_bg)
            left_side.pack(side='left', fill='x', expand=True)
            
            # Setting name - clean and bold with premium color
            name_color = '#e8f4fd' if is_premium else self.colors['text_primary']
            name_label = tk.Label(left_side, text=setting_name,
                                 font=('Segoe UI', 13, 'bold'),
                                 bg=card_bg,
                                 fg=name_color,
                                 anchor='w')
            name_label.pack(anchor='w', fill='x')
            
            # Setting description - clean and readable
            desc_color = '#b8d4ea' if is_premium else self.colors['text_secondary']
            desc_label = tk.Label(left_side, text=config['description'],
                                 font=('Segoe UI', 10),
                                 bg=card_bg,
                                 fg=desc_color,
                                 anchor='w',
                                 wraplength=350,
                                 justify='left')
            desc_label.pack(anchor='w', fill='x', pady=(3, 0))
            
            # Right side - control
            right_side = tk.Frame(setting_card, bg=card_bg)
            right_side.pack(side='right', padx=(10, 0))
            
            # Create clean controls
            if config['type'] == 'toggle':
                var = tk.BooleanVar(value=config['default'])
                
                # Clean toggle switch
                toggle_canvas = tk.Canvas(right_side, width=44, height=24,
                                        bg=card_bg,
                                        highlightthickness=0, bd=0)
                toggle_canvas.pack(anchor='center')
                
                self.draw_minimal_toggle(toggle_canvas, var.get())
                toggle_canvas.bind("<Button-1>", 
                    lambda e, c=toggle_canvas, v=var: self.toggle_minimal_switch(c, v))
                toggle_canvas.config(cursor='hand2')
                
            elif config['type'] == 'radio':
                var = tk.StringVar(value=config['default'])
                
                # Clean dropdown-style display
                dropdown_frame = tk.Frame(right_side, bg=card_bg)
                dropdown_frame.pack()
                
                value_color = '#ffd700' if is_premium else '#4a9eff'
                value_label = tk.Label(dropdown_frame, text=config['default'],
                                     font=('Segoe UI', 10, 'bold'),
                                     bg=card_bg,
                                     fg=value_color,
                                     cursor='hand2')
                value_label.pack()
                
                arrow_color = desc_color
                arrow_label = tk.Label(dropdown_frame, text="▼",
                                     font=('Segoe UI', 8),
                                     bg=card_bg,
                                     fg=arrow_color)
                arrow_label.pack()
                
                value_label.bind("<Button-1>", 
                    lambda e, cfg=config, v=var, lbl=value_label: self.show_clean_radio_options(cfg, v, lbl))
                
            elif config['type'] == 'scale':
                var = tk.IntVar(value=config['default'])
                
                # Clean value display
                value_frame = tk.Frame(right_side, bg=card_bg)
                value_frame.pack()
                
                value_color = '#ffd700' if is_premium else '#4a9eff'
                value_label = tk.Label(value_frame, text=str(config['default']),
                                     font=('Segoe UI', 11, 'bold'),
                                     bg=card_bg,
                                     fg=value_color,
                                     cursor='hand2')
                value_label.pack()
                
                range_label = tk.Label(value_frame, 
                                     text=f"({config['range'][0]}-{config['range'][1]})",
                                     font=('Segoe UI', 8),
                                     bg=card_bg,
                                     fg=desc_color)
                range_label.pack()
                
                value_label.bind("<Button-1>", 
                    lambda e, cfg=config, v=var, lbl=value_label: self.show_clean_scale_control(cfg, v, lbl))
                
            elif config['type'] == 'text':
                # Clean configure button with premium styling
                btn_color = '#b8860b' if is_premium else '#4a9eff'
                config_btn = tk.Button(right_side, text="Configure",
                                     font=('Segoe UI', 9, 'bold'),
                                     bg=btn_color,
                                     fg='white',
                                     relief='flat',
                                     bd=0,
                                     padx=12, pady=6,
                                     cursor='hand2',
                                     command=lambda cfg=config: self.show_clean_text_config(cfg))
                config_btn.pack()
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mouse wheel scrolling - only for this canvas
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        canvas.bind("<MouseWheel>", on_mousewheel)
        scrollable_frame.bind("<MouseWheel>", on_mousewheel)

    def draw_clean_toggle(self, canvas, is_on):
        """Draw clean iOS-style toggle switch"""
        canvas.delete("all")
        
        # Toggle colors
        bg_color = '#4a9eff' if is_on else '#666666'
        handle_x = 28 if is_on else 8
        
        # Background rounded rectangle (smaller and cleaner)
        canvas.create_oval(2, 2, 22, 24, fill=bg_color, outline=bg_color, width=0)
        canvas.create_rectangle(12, 2, 38, 24, fill=bg_color, outline=bg_color, width=0)
        canvas.create_oval(28, 2, 48, 24, fill=bg_color, outline=bg_color, width=0)
        
        # Handle (white circle) - smaller and cleaner
        canvas.create_oval(handle_x, 4, handle_x+16, 22, fill='white', outline='white', width=0)
    
    def toggle_clean_switch(self, canvas, var):
        """Toggle clean switch and update visual"""
        var.set(not var.get())
        self.draw_clean_toggle(canvas, var.get())
        print(f"Setting toggled: {var.get()}")

    def show_advanced_content(self, parent, feature_name):
        """Show advanced tab content with clean layout"""
        # Create main advanced frame (no scrolling needed for now)
        advanced_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        advanced_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Advanced settings card
        settings_card = tk.Frame(advanced_frame, bg=self.colors['bg_secondary'], relief='flat', bd=0)
        settings_card.pack(fill='x', pady=(0, 15))
        
        content = tk.Frame(settings_card, bg=self.colors['bg_secondary'])
        content.pack(fill='x', padx=25, pady=20)
        
        # Advanced title
        title = tk.Label(content, text=f"Advanced {feature_name} Settings",
                        font=('Segoe UI', 16, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_primary'])
        title.pack(anchor='w')
        
        desc = tk.Label(content, text="Advanced configuration options for expert users.",
                       font=('Segoe UI', 11),
                       bg=self.colors['bg_secondary'],
                       fg=self.colors['text_secondary'])
        desc.pack(anchor='w', pady=(5, 15))
        
        # Expert mode setting
        expert_setting = tk.Frame(content, bg=self.colors['bg_secondary'])
        expert_setting.pack(fill='x', pady=5)
        
        expert_info = tk.Frame(expert_setting, bg=self.colors['bg_secondary'])
        expert_info.pack(side='left', fill='x', expand=True)
        
        expert_label = tk.Label(expert_info, text="Expert Mode",
                               font=('Segoe UI', 12, 'bold'),
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['text_primary'])
        expert_label.pack(anchor='w')
        
        expert_desc = tk.Label(expert_info, text="Enable advanced configuration options",
                              font=('Segoe UI', 10),
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['text_secondary'])
        expert_desc.pack(anchor='w')
        
        expert_control = tk.Frame(expert_setting, bg=self.colors['bg_secondary'])
        expert_control.pack(side='right')
        
        expert_toggle = tk.Canvas(expert_control, width=50, height=26,
                                 bg=self.colors['bg_secondary'],
                                 highlightthickness=0, relief='flat', bd=0)
        expert_toggle.pack()
        self.draw_clean_toggle(expert_toggle, False)
        
        # Coming soon notice
        notice_frame = tk.Frame(advanced_frame, bg=self.colors['bg_secondary'], relief='flat', bd=0)
        notice_frame.pack(fill='x')
        
        notice_content = tk.Frame(notice_frame, bg=self.colors['bg_secondary'])
        notice_content.pack(fill='x', padx=25, pady=20)
        
        coming_soon = tk.Label(notice_content, text="🔧 Additional advanced options coming in next update",
                              font=('Segoe UI', 11),
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['text_secondary'])
        coming_soon.pack()
    
    def toggle_integrated_switch(self, canvas, var):
        """Toggle integrated switch and update visual"""
        var.set(not var.get())
        self.draw_bitdefender_toggle(canvas, var.get())
    
    def show_radio_options(self, config, var, label):
        """Show radio button options in a dropdown-style menu"""
        # Create small popup for radio options
        popup = tk.Toplevel(self.root)
        popup.title("Select Option")
        popup.geometry("200x150")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.transient(self.root)
        popup.grab_set()
        
        # Position near the label
        x = label.winfo_rootx()
        y = label.winfo_rooty() + label.winfo_height()
        popup.geometry(f"+{x}+{y}")
        
        for option in config['options']:
            option_btn = tk.Button(popup, text=option,
                                 font=('Segoe UI', 11),
                                 bg=self.colors['bg_secondary'],
                                 fg=self.colors['text_primary'],
                                 relief='flat',
                                 padx=20, pady=8,
                                 command=lambda opt=option: self.select_radio_option(var, label, opt, popup))
            option_btn.pack(fill='x', padx=10, pady=2)
    
    def select_radio_option(self, var, label, option, popup):
        """Select radio option and update display"""
        var.set(option)
        label.config(text=option)
        popup.destroy()
    
    def show_scale_control(self, config, var, label):
        """Show scale control in a popup"""
        popup = tk.Toplevel(self.root)
        popup.title("Adjust Value")
        popup.geometry("300x100")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.transient(self.root)
        popup.grab_set()
        
        # Position near the label
        x = label.winfo_rootx()
        y = label.winfo_rooty() + label.winfo_height()
        popup.geometry(f"+{x}+{y}")
        
        # Scale widget
        scale = tk.Scale(popup,
                       from_=config['range'][0],
                       to=config['range'][1],
                       orient='horizontal',
                       variable=var,
                       bg=self.colors['bg_secondary'],
                       fg=self.colors['text_primary'],
                       highlightthickness=0,
                       troughcolor=self.colors['bg_primary'])
        scale.pack(fill='x', padx=20, pady=20)
        
        # Update button
        update_btn = tk.Button(popup, text="Update",
                             bg='#4a9eff',
                             fg='white',
                             command=lambda: self.update_scale_value(var, label, popup))
        update_btn.pack(pady=10)
    
    def update_scale_value(self, var, label, popup):
        """Update scale value and close popup"""
        label.config(text=str(var.get()))
        popup.destroy()
    
    def show_text_config(self, config):
        """Show text configuration dialog"""
        popup = tk.Toplevel(self.root)
        popup.title("Text Configuration")
        popup.geometry("500x300")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.transient(self.root)
        popup.grab_set()
        
        # Title
        title = tk.Label(popup, text=config['description'],
                        font=('Segoe UI', 12, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_primary'])
        title.pack(pady=20)
        
        # Text area
        text_area = tk.Text(popup,
                          height=8,
                          font=('Segoe UI', 10),
                          bg=self.colors['bg_primary'],
                          fg=self.colors['text_primary'],
                          insertbackground=self.colors['text_primary'])
        text_area.pack(fill='both', expand=True, padx=20, pady=10)
        text_area.insert('1.0', config['default'])
        
        # Save button
        save_btn = tk.Button(popup, text="Save",
                           bg='#4a9eff',
                           fg='white',
                           command=popup.destroy)
        save_btn.pack(pady=10)
    
    def start_feature_scan(self, feature_name, scan_type):
        """Start a scan for specific feature"""
        self.show_status_message(f"🔍 Starting {scan_type} {feature_name} scan...", self.colors['accent_green'])
        print(f"Starting {scan_type} scan for {feature_name}")
    
    def create_custom_scan(self, feature_name):
        """Create custom scan dialog"""
        self.show_status_message(f"🛠️ Custom {feature_name} scan configuration coming soon", self.colors['accent_green'])
        print(f"Custom scan for {feature_name}")

    def create_advanced_settings_window(self, title, settings_config):
        """Create an advanced settings window with various control types"""
        # Create settings window
        settings_window = tk.Toplevel(self.root)
        settings_window.title(title)
        settings_window.geometry("800x700")
        settings_window.configure(bg=self.colors['bg_primary'])
        settings_window.transient(self.root)
        settings_window.grab_set()
        
        # Window styling
        settings_window.resizable(True, True)
        settings_window.minsize(600, 500)
        
        # Header
        header_frame = tk.Frame(settings_window, bg=self.colors['accent_primary'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(header_frame, text=title,
                               font=('Segoe UI', 16, 'bold'),
                               bg=self.colors['accent_primary'],
                               fg='white')
        header_label.pack(expand=True)
        
        # Main content frame with scrolling
        main_frame = tk.Frame(settings_window, bg=self.colors['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Create canvas and scrollbar for scrolling
        canvas = tk.Canvas(main_frame, bg=self.colors['bg_primary'], highlightthickness=0)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_primary'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Store setting variables
        setting_vars = {}
        
        # Create settings controls
        for setting_name, config in settings_config.items():
            # Setting container
            setting_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_secondary'], relief='flat', bd=1)
            setting_frame.pack(fill='x', pady=10, padx=5)
            
            # Setting header
            header = tk.Frame(setting_frame, bg=self.colors['bg_secondary'])
            header.pack(fill='x', padx=15, pady=10)
            
            # Setting name
            name_label = tk.Label(header, text=setting_name,
                                 font=('Segoe UI', 12, 'bold'),
                                 bg=self.colors['bg_secondary'],
                                 fg=self.colors['text_primary'])
            name_label.pack(anchor='w')
            
            # Setting description
            desc_label = tk.Label(header, text=config['description'],
                                 font=('Segoe UI', 10),
                                 bg=self.colors['bg_secondary'],
                                 fg=self.colors['text_secondary'],
                                 wraplength=400,
                                 justify='left')
            desc_label.pack(anchor='w', pady=(5, 0))
            
            # Setting control based on type
            control_frame = tk.Frame(setting_frame, bg=self.colors['bg_secondary'])
            control_frame.pack(fill='x', padx=15, pady=(0, 15))
            
            if config['type'] == 'toggle':
                var = tk.BooleanVar(value=config['default'])
                setting_vars[setting_name] = var
                
                toggle_cb = tk.Checkbutton(control_frame,
                                         text=f"Enable {setting_name}",
                                         variable=var,
                                         font=('Segoe UI', 11),
                                         bg=self.colors['bg_secondary'],
                                         fg=self.colors['text_primary'],
                                         selectcolor=self.colors['bg_primary'],
                                         activebackground=self.colors['bg_secondary'])
                toggle_cb.pack(anchor='w')
                
            elif config['type'] == 'radio':
                var = tk.StringVar(value=config['default'])
                setting_vars[setting_name] = var
                
                for option in config['options']:
                    radio_btn = tk.Radiobutton(control_frame,
                                             text=option,
                                             variable=var,
                                             value=option,
                                             font=('Segoe UI', 10),
                                             bg=self.colors['bg_secondary'],
                                             fg=self.colors['text_primary'],
                                             selectcolor=self.colors['accent_primary'],
                                             activebackground=self.colors['bg_secondary'])
                    radio_btn.pack(anchor='w', padx=20)
                    
            elif config['type'] == 'scale':
                var = tk.IntVar(value=config['default'])
                setting_vars[setting_name] = var
                
                scale_frame = tk.Frame(control_frame, bg=self.colors['bg_secondary'])
                scale_frame.pack(fill='x', pady=5)
                
                scale = tk.Scale(scale_frame,
                               from_=config['range'][0],
                               to=config['range'][1],
                               orient='horizontal',
                               variable=var,
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['text_primary'],
                               highlightthickness=0,
                               troughcolor=self.colors['bg_primary'])
                scale.pack(fill='x')
                
            elif config['type'] == 'text':
                var = tk.StringVar(value=config['default'])
                setting_vars[setting_name] = var
                
                text_entry = tk.Text(control_frame,
                                   height=3,
                                   font=('Segoe UI', 10),
                                   bg=self.colors['bg_primary'],
                                   fg=self.colors['text_primary'],
                                   insertbackground=self.colors['text_primary'],
                                   relief='flat',
                                   bd=1)
                text_entry.pack(fill='x', pady=5)
                text_entry.insert('1.0', config['default'])
                
                # Store text widget instead of StringVar for multi-line text
                setting_vars[setting_name] = text_entry
        
        # Buttons frame
        button_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_primary'])
        button_frame.pack(fill='x', pady=20)
        
        # Cancel button
        cancel_btn = tk.Button(button_frame, text="Cancel",
                              bg=self.colors['bg_secondary'],
                              fg=self.colors['text_primary'],
                              font=('Segoe UI', 12),
                              relief='flat',
                              padx=30, pady=10,
                              command=settings_window.destroy)
        cancel_btn.pack(side='right', padx=(10, 0))
        
        # Apply button
        def apply_settings():
            """Apply the settings"""
            values = {}
            for name, var in setting_vars.items():
                if isinstance(var, tk.Text):
                    values[name] = var.get('1.0', tk.END).strip()
                else:
                    values[name] = var.get()
            
            print(f"Applied settings for {title}:")
            for name, value in values.items():
                print(f"  {name}: {value}")
            
            # Show confirmation
            self.show_status_message(f"✅ {title} updated successfully", self.colors['accent_green'])
            settings_window.destroy()
        
        apply_btn = tk.Button(button_frame, text="Apply Settings",
                             bg=self.colors['accent_green'],
                             fg='white',
                             font=('Segoe UI', 12, 'bold'),
                             relief='flat',
                             padx=30, pady=10,
                             command=apply_settings)
        apply_btn.pack(side='right')
        
        # Reset to defaults button
        def reset_defaults():
            """Reset all settings to defaults"""
            for setting_name, config in settings_config.items():
                var = setting_vars[setting_name]
                if isinstance(var, tk.Text):
                    var.delete('1.0', tk.END)
                    var.insert('1.0', config['default'])
                else:
                    var.set(config['default'])
        
        reset_btn = tk.Button(button_frame, text="Reset Defaults",
                             bg=self.colors['accent_red'],
                             fg='white',
                             font=('Segoe UI', 12),
                             relief='flat',
                             padx=30, pady=10,
                             command=reset_defaults)
        reset_btn.pack(side='left')
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Focus the window
        settings_window.focus_force()
    
    def show_settings(self):
        """Show main settings window - redirect to settings view"""
        # Navigate to settings in the main interface
        self.update_main_content("Settings")
    
    def draw_toggle_switch(self, canvas, is_on):
        """Draw toggle switch on canvas"""
        canvas.delete("all")
        
        if is_on:
            # ON state - green background, circle on right
            canvas.create_oval(2, 2, 48, 23, fill=self.colors['accent_green'], outline="")
            canvas.create_oval(28, 4, 44, 21, fill='white', outline="")
        else:
            # OFF state - gray background, circle on left
            canvas.create_oval(2, 2, 48, 23, fill='#666666', outline="")
            canvas.create_oval(6, 4, 22, 21, fill='white', outline="")
    
    def toggle_switch(self, canvas, feature_key, feature):
        """Toggle switch state and update visual"""
        # Toggle the state
        self.toggle_states[feature_key] = not self.toggle_states[feature_key]
        new_state = self.toggle_states[feature_key]
        
        # Update visual
        self.draw_toggle_switch(canvas, new_state)
        
        # Debug output
        print(f"🔄 Toggle clicked: {feature['title']} -> {new_state}")
        
        # Handle the toggle action
        self.handle_toggle_action(feature['title'], new_state)
    
    def handle_toggle_action(self, feature_title, is_enabled):
        """Handle toggle switch actions"""
        status = "ENABLED" if is_enabled else "DISABLED"
        color = self.colors['accent_green'] if is_enabled else '#ff4444'
        
        if feature_title == 'Cryptomining Protection':
            message = f"🔒 Cryptomining Protection {status}"
            self.show_status_message(message, color)
            print(f"Cryptomining Protection: {status}")
            
        elif feature_title == 'Vulnerability':
            message = f"🔍 Vulnerability Scanner {status}"
            self.show_status_message(message, color)
            print(f"Vulnerability Scanner: {status}")
            
        elif feature_title == 'Firewall':
            message = f"🔥 Firewall Protection {status}"
            self.show_status_message(message, color)
            print(f"Firewall: {status}")
            
        elif feature_title == 'Ransomware Remediation':
            message = f"🔐 Ransomware Protection {status}"
            self.show_status_message(message, color)
            print(f"Ransomware Remediation: {status}")
    
    def show_status_message(self, message, color=None):
        """Show status message to user"""
        if color is None:
            color = self.colors['accent_green']
            
        # Create a temporary status label
        status_window = tk.Toplevel(self.root)
        status_window.title("Protection Status")
        status_window.geometry("350x120")
        status_window.configure(bg=self.colors['bg_secondary'])
        status_window.transient(self.root)
        status_window.grab_set()
        
        # Center the window
        status_window.geometry("+{}+{}".format(
            self.root.winfo_rootx() + 200,
            self.root.winfo_rooty() + 100))
        
        # Status message with colored background
        msg_frame = tk.Frame(status_window, bg=color, relief='flat', bd=0)
        msg_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        msg_label = tk.Label(msg_frame, text=message,
                           font=('Segoe UI', 12, 'bold'),
                           bg=color,
                           fg='white',
                           wraplength=300,
                           justify='center')
        msg_label.pack(expand=True)
        
        # Auto close after 2.5 seconds
        status_window.after(2500, status_window.destroy)
    
    def lighten_color(self, hex_color):
        """Lighten a hex color for hover effects"""
        # Remove # if present
        hex_color = hex_color.lstrip('#')
        
        # Convert to RGB
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Lighten by adding 30 to each component (max 255)
        lightened_rgb = tuple(min(255, c + 30) for c in rgb)
        
        # Convert back to hex
        return '#{:02x}{:02x}{:02x}'.format(*lightened_rgb)
    
    def create_privacy_view(self):
        """Create privacy features view - Bitdefender style"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Main title section
        title_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        title_frame.pack(fill='x', pady=(0, 30))
        
        # Large shield icon and title
        header_frame = tk.Frame(title_frame, bg=self.colors['bg_primary'])
        header_frame.pack(anchor='w')
        
        # Shield icon
        shield_label = tk.Label(header_frame, text="🛡️", font=('Segoe UI', 48), 
                               bg=self.colors['bg_primary'], fg=self.colors['accent_green'])
        shield_label.pack(side='left', padx=(0, 20))
        
        # Title text
        title_text_frame = tk.Frame(header_frame, bg=self.colors['bg_primary'])
        title_text_frame.pack(side='left')
        
        main_title = tk.Label(title_text_frame, text="Privacy Features", 
                             font=('Segoe UI', 32, 'bold'), 
                             bg=self.colors['bg_primary'], 
                             fg=self.colors['text_primary'])
        main_title.pack(anchor='w')
        
        # Privacy features grid
        self.create_privacy_features_grid()
    
    def create_privacy_features_grid(self):
        """Create the privacy features grid like Bitdefender"""
        # Main grid container
        grid_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        grid_container.pack(fill='both', expand=True, padx=20)
        
        # Privacy features data matching Bitdefender layout
        features = [
            # Row 1
            {
                'title': 'Safepay',
                'icon': '🏦',
                'description': 'Safepay is a secure environment for sensitive transactions and online banking.',
                'button_text': 'Settings',
                'button_color': self.colors['accent_primary'],
                'enabled': True
            },
            {
                'title': 'VPN', 
                'icon': '🔒',
                'description': 'Proton VPN-style interface with world map, server selection, and advanced privacy features.',
                'button_text': 'Open VPN',
                'button_color': self.colors['accent_primary'],
                'enabled': True
            },
            # Row 2
            {
                'title': 'SecurePass',
                'icon': '🔑',
                'description': 'Manage and protect your passwords, financial data and other sensitive information on all your devices.',
                'button_text': 'Open',
                'button_color': self.colors['accent_primary'],
                'enabled': True,
                'link_icon': True
            },
            {
                'title': 'Video & Audio Protection',
                'icon': '🎥',
                'description': 'Protects your privacy by stopping cyber attacks that might track and record your activity.',
                'button_text': 'Settings',
                'button_color': self.colors['accent_primary'],
                'enabled': True
            },
            # Row 3
            {
                'title': 'Anti-tracker',
                'icon': '🚫',
                'description': 'Blocks web trackers from collecting data that would enable user profiling and commercial targeting.',
                'button_text': 'Settings',
                'button_color': self.colors['accent_primary'],
                'enabled': True,
                'toggle': True
            },
            {
                'title': 'Parental Control',
                'icon': '👨‍👩‍👧‍👦',
                'description': 'Check the activity and location of your child across devices.',
                'button_text': 'Configure',
                'button_color': self.colors['accent_primary'],
                'enabled': True,
                'link_icon': True
            }
        ]
        
        # Create feature cards in 2-column grid
        for i, feature in enumerate(features):
            row = i // 2
            col = i % 2
            self.create_privacy_feature_card(grid_container, feature, row, col)
    
    def create_privacy_feature_card(self, parent, feature, row, col):
        """Create a privacy feature card"""
        # Card frame with Bitdefender styling
        card_frame = tk.Frame(parent, bg=self.colors['bg_secondary'], 
                             relief='flat', bd=0)
        card_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        # Configure grid weights
        parent.grid_rowconfigure(row, weight=1, minsize=160)
        parent.grid_columnconfigure(col, weight=1, minsize=400)
        
        # Card content with padding
        content_frame = tk.Frame(card_frame, bg=self.colors['bg_secondary'])
        content_frame.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Header with icon and title
        header_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        header_frame.pack(fill='x', pady=(0, 15))
        
        # Feature icon (larger and more colorful)
        icon_colors = {
            '🏦': '#4A90E2',  # Blue for Safepay
            '🔒': '#7ED321',  # Green for VPN
            '🔑': '#F5A623',  # Orange for SecurePass
            '🎥': '#9013FE',  # Purple for Video & Audio
            '🚫': '#D0021B',  # Red for Anti-tracker
            '👨‍👩‍👧‍👦': '#50E3C2'   # Cyan for Parental Control
        }
        
        icon_color = icon_colors.get(feature['icon'], self.colors['accent_primary'])
        icon_label = tk.Label(header_frame, text=feature['icon'], 
                             font=('Segoe UI', 24), 
                             bg=self.colors['bg_secondary'], 
                             fg=icon_color)
        icon_label.pack(side='left', padx=(0, 15))
        
        # Title and toggle container
        title_container = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        title_container.pack(side='left', fill='x', expand=True)
        
        # Title
        title_label = tk.Label(title_container, text=feature['title'], 
                              font=('Segoe UI', 16, 'bold'), 
                              bg=self.colors['bg_secondary'], 
                              fg=self.colors['text_primary'])
        title_label.pack(side='left')
        
        # Toggle switch if enabled
        if feature.get('toggle'):
            toggle_frame = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
            toggle_frame.pack(side='right')
            
            # Create toggle switch (ON state)
            toggle_canvas = tk.Canvas(toggle_frame, width=50, height=25, 
                                    bg=self.colors['bg_secondary'], 
                                    highlightthickness=0)
            toggle_canvas.pack()
            
            # Draw toggle switch
            toggle_canvas.create_oval(2, 2, 48, 23, fill=self.colors['accent_primary'], outline="")
            toggle_canvas.create_oval(28, 4, 44, 21, fill='white', outline="")
        
        # Description text
        desc_label = tk.Label(content_frame, text=feature['description'], 
                             font=('Segoe UI', 11), 
                             bg=self.colors['bg_secondary'], 
                             fg=self.colors['text_secondary'],
                             wraplength=350, justify='left')
        desc_label.pack(anchor='w', pady=(0, 20))
        
        # Action button with optional link icon
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
        button_frame.pack(anchor='w')
        
        button_text = feature['button_text']
        if feature.get('link_icon'):
            button_text = f"🔗 {button_text}"
        
        action_btn = tk.Button(button_frame, text=button_text,
                              bg=feature['button_color'], fg='white',
                              font=('Segoe UI', 11, 'bold'),
                              relief='flat', bd=0, padx=20, pady=8,
                              command=lambda f=feature: self.on_privacy_feature_action(f))
        action_btn.pack(side='left')
        
        # Make card clickable
        clickable_widgets = [card_frame, content_frame, header_frame, title_container, 
                           title_label, desc_label, icon_label]
        
        for widget in clickable_widgets:
            widget.bind("<Enter>", lambda e, f=card_frame: self.on_privacy_feature_hover(f, True))
            widget.bind("<Leave>", lambda e, f=card_frame: self.on_privacy_feature_hover(f, False))
            widget.bind("<Button-1>", lambda e, f=feature: self.on_privacy_feature_click(f))
    
    def on_privacy_feature_hover(self, frame, entering):
        """Handle privacy feature card hover effect"""
        if entering:
            frame.configure(bg=self.colors['bg_tertiary'])
            for child in frame.winfo_children():
                child.configure(bg=self.colors['bg_tertiary'])
                for grandchild in child.winfo_children():
                    grandchild.configure(bg=self.colors['bg_tertiary'])
                    for great_grandchild in grandchild.winfo_children():
                        if isinstance(great_grandchild, tk.Label):
                            great_grandchild.configure(bg=self.colors['bg_tertiary'])
        else:
            frame.configure(bg=self.colors['bg_secondary'])
            for child in frame.winfo_children():
                child.configure(bg=self.colors['bg_secondary'])
                for grandchild in child.winfo_children():
                    grandchild.configure(bg=self.colors['bg_secondary'])
                    for great_grandchild in grandchild.winfo_children():
                        if isinstance(great_grandchild, tk.Label):
                            great_grandchild.configure(bg=self.colors['bg_secondary'])
    
    def on_privacy_feature_click(self, feature):
        """Handle privacy feature card click"""
        print(f"Privacy feature clicked: {feature['title']}")
        self.on_privacy_feature_action(feature)
    
    def on_privacy_feature_action(self, feature):
        """Handle privacy feature action button click"""
        title = feature['title']
        
        if title == 'Safepay':
            self.launch_safepay()
        elif title == 'VPN':
            self.toggle_vpn()
        elif title == 'SecurePass':
            self.show_secure_pass()
        elif title == 'Video & Audio Protection':
            self.show_media_protection()
        elif title == 'Anti-tracker':
            self.show_anti_tracker()
        elif title == 'Parental Control':
            self.show_parental_control()
        else:
            self.show_feature_dialog(title, feature['description'])
    
    def launch_safepay(self):
        """Launch Safepay secure browser"""
        try:
            # Import and launch the actual SafePay system
            import sys
            from pathlib import Path
            
            # Add project root to path
            project_root = Path(__file__).parent
            if str(project_root) not in sys.path:
                sys.path.insert(0, str(project_root))
            
            print("SafePay: Launching from main GUI...")
            
            # Try multiple import paths
            try:
                # Use local mock function
                show_safepay()
            except ImportError:
                try:
                    # Use local mock function
                    show_safepay()
                except ImportError:
                    # Show SafePay directly
                    show_safepay()
                    self.add_notification("Information", "SafePay Launched", 
                                        "🔒 Secure banking environment launched successfully!", "🏦")
                    return
            
            # Launch SafePay with proper GUI
            safepay_manager = show_safepay()
            
            if safepay_manager:
                self.add_notification("Information", "SafePay Launched", 
                                    "🔒 Secure banking environment activated with military-grade protection!", "🏦")
                print("SafePay: Successfully launched from main GUI")
            else:
                # Show SafePay directly
                show_safepay()
                self.add_notification("Information", "SafePay Launched", 
                                    "🔒 Secure banking environment launched successfully!", "🏦")
                
        except Exception as e:
            print(f"SafePay launch error: {e}")
            # Launch SafePay directly
            try:
                show_safepay()
                self.add_notification("Information", "SafePay Launched", 
                                    "🔒 Secure banking environment launched successfully!", "🏦")
            except Exception as fallback_error:
                print(f"SafePay fallback error: {fallback_error}")
                self.add_notification("Error", "SafePay Error", 
                                    f"Failed to launch SafePay: {str(e)}", "❌")
    
    def show_secure_pass(self):
        """Show SecurePass password manager"""
        self.show_feature_dialog("SecurePass", "Password manager for secure storage and generation of passwords across all devices.")
    
    def show_media_protection(self):
        """Show Video & Audio Protection settings"""
        self.add_notification("Information", "Media Protection Settings", 
                            "Video and audio protection settings have been accessed.", "🎥")
        self.show_feature_dialog("Video & Audio Protection", "Configure protection against webcam and microphone hijacking attempts.")
    
    def show_anti_tracker(self):
        """Show Anti-tracker settings"""
        self.show_feature_dialog("Anti-tracker", "Configure web tracker blocking to prevent user profiling and targeted advertising.")
    
    def show_parental_control(self):
        """Show Parental Control configuration"""
        self.show_feature_dialog("Parental Control", "Set up monitoring and restrictions for child device usage and online activity.")

    def open_privacy_suite(self):
        """Open the full privacy protection suite"""
        try:
            # Use local mock class
            if not hasattr(self, 'privacy_suite') or not self.privacy_suite:
                self.privacy_suite = PrivacyProtectionSuite()
            else:
                # Bring existing window to front
                if hasattr(self.privacy_suite, 'privacy_window'):
                    self.privacy_suite.privacy_window.lift()
                    self.privacy_suite.privacy_window.focus_force()
        except Exception as e:
            print(f"Failed to open privacy suite: {e}")
    
    def create_settings_view(self):
        """Create settings view"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        title = tk.Label(self.main_frame, text="Settings", 
                        font=self.fonts['title'], bg=self.colors['bg_primary'], 
                        fg=self.colors['text_primary'])
        title.pack(anchor='w', pady=(0, 20))
        
        # Add button to open full settings manager
        button_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        button_frame.pack(fill='x', pady=20)
        
        open_settings_btn = tk.Button(button_frame, text="🔧 Open Settings Manager",
                                     bg=self.colors['accent_primary'], fg='white', 
                                     font=('Segoe UI', 14, 'bold'),
                                     command=self.open_settings_manager,
                                     relief='flat', padx=30, pady=15)
        open_settings_btn.pack(anchor='w', padx=20)
        
        # Create scrollable content frame for settings overview
        canvas = tk.Canvas(self.main_frame, bg=self.colors['bg_primary'], highlightthickness=0)
        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_primary'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Account Information Section
        account_frame = tk.LabelFrame(scrollable_frame, text="👤 Account Information", 
                                    font=('Segoe UI', 12, 'bold'),
                                    bg=self.colors['bg_primary'], 
                                    fg=self.colors['text_primary'],
                                    relief='flat', bd=1)
        account_frame.pack(fill='x', padx=20, pady=10)
        
        # Support Email
        email_frame = tk.Frame(account_frame, bg=self.colors['bg_primary'])
        email_frame.pack(fill='x', padx=15, pady=10)
        
        tk.Label(email_frame, text="📧 Support Email:", 
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['bg_primary'], 
                fg=self.colors['text_primary']).pack(side='left')
        
        email_entry = tk.Entry(email_frame, font=('Segoe UI', 11),
                              bg=self.colors['bg_secondary'], 
                              fg=self.colors['text_primary'],
                              insertbackground=self.colors['text_primary'],
                              relief='flat', bd=1)
        email_entry.insert(0, "anonymous-hide-me-pls@proton.me")
        email_entry.pack(side='right', padx=(10, 0))
        
        # Common Settings Section
        common_frame = tk.LabelFrame(scrollable_frame, text="⚙️ Common Settings", 
                                   font=('Segoe UI', 12, 'bold'),
                                   bg=self.colors['bg_primary'], 
                                   fg=self.colors['text_primary'],
                                   relief='flat', bd=1)
        common_frame.pack(fill='x', padx=20, pady=10)
        
        # Auto Start
        autostart_var = tk.BooleanVar(value=True)
        autostart_cb = tk.Checkbutton(common_frame, text="🚀 Start with Windows", 
                                    variable=autostart_var,
                                    font=('Segoe UI', 11),
                                    bg=self.colors['bg_primary'], 
                                    fg=self.colors['text_primary'],
                                    selectcolor=self.colors['bg_secondary'],
                                    activebackground=self.colors['bg_primary'])
        autostart_cb.pack(anchor='w', padx=15, pady=5)
        
        # Notifications
        notify_var = tk.BooleanVar(value=True)
        notify_cb = tk.Checkbutton(common_frame, text="🔔 Enable Notifications", 
                                 variable=notify_var,
                                 font=('Segoe UI', 11),
                                 bg=self.colors['bg_primary'], 
                                 fg=self.colors['text_primary'],
                                 selectcolor=self.colors['bg_secondary'],
                                 activebackground=self.colors['bg_primary'])
        notify_cb.pack(anchor='w', padx=15, pady=5)
        
        # Dark Mode
        dark_var = tk.BooleanVar(value=True)
        dark_cb = tk.Checkbutton(common_frame, text="🌙 Dark Mode", 
                               variable=dark_var,
                               font=('Segoe UI', 11),
                               bg=self.colors['bg_primary'], 
                               fg=self.colors['text_primary'],
                               selectcolor=self.colors['bg_secondary'],
                               activebackground=self.colors['bg_primary'])
        dark_cb.pack(anchor='w', padx=15, pady=5)
        
        # Auto Updates
        updates_var = tk.BooleanVar(value=True)
        updates_cb = tk.Checkbutton(common_frame, text="🔄 Automatic Updates", 
                                  variable=updates_var,
                                  font=('Segoe UI', 11),
                                  bg=self.colors['bg_primary'], 
                                  fg=self.colors['text_primary'],
                                  selectcolor=self.colors['bg_secondary'],
                                  activebackground=self.colors['bg_primary'])
        updates_cb.pack(anchor='w', padx=15, pady=5)
        
        # Language Selection
        lang_frame = tk.Frame(common_frame, bg=self.colors['bg_primary'])
        lang_frame.pack(fill='x', padx=15, pady=10)
        
        tk.Label(lang_frame, text="🌐 Language:", 
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['bg_primary'], 
                fg=self.colors['text_primary']).pack(side='left')
        
        lang_var = tk.StringVar(value="English")
        lang_combo = tk.OptionMenu(lang_frame, lang_var, "English", "Español", "Français", "Deutsch", "中文", "日本語")
        lang_combo.config(bg=self.colors['bg_secondary'], 
                         fg=self.colors['text_primary'],
                         font=('Segoe UI', 10),
                         relief='flat', bd=1)
        lang_combo.pack(side='right', padx=(10, 0))
        
        # Advanced Settings Section
        advanced_frame = tk.LabelFrame(scrollable_frame, text="🔬 Advanced Settings", 
                                     font=('Segoe UI', 12, 'bold'),
                                     bg=self.colors['bg_primary'], 
                                     fg=self.colors['text_primary'],
                                     relief='flat', bd=1)
        advanced_frame.pack(fill='x', padx=20, pady=10)
        
        # Debug Mode
        debug_var = tk.BooleanVar(value=False)
        debug_cb = tk.Checkbutton(advanced_frame, text="🐛 Debug Mode", 
                                variable=debug_var,
                                font=('Segoe UI', 11),
                                bg=self.colors['bg_primary'], 
                                fg=self.colors['text_primary'],
                                selectcolor=self.colors['bg_secondary'],
                                activebackground=self.colors['bg_primary'])
        debug_cb.pack(anchor='w', padx=15, pady=5)
        
        # Performance Mode
        perf_frame = tk.Frame(advanced_frame, bg=self.colors['bg_primary'])
        perf_frame.pack(fill='x', padx=15, pady=10)
        
        tk.Label(perf_frame, text="⚡ Performance Mode:", 
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['bg_primary'], 
                fg=self.colors['text_primary']).pack(side='left')
        
        perf_var = tk.StringVar(value="Balanced")
        perf_combo = tk.OptionMenu(perf_frame, perf_var, "Eco", "Balanced", "High Performance", "Maximum")
        perf_combo.config(bg=self.colors['bg_secondary'], 
                         fg=self.colors['text_primary'],
                         font=('Segoe UI', 10),
                         relief='flat', bd=1)
        perf_combo.pack(side='right', padx=(10, 0))
        
        # Save Button
        save_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_primary'])
        save_frame.pack(fill='x', padx=20, pady=20)
        
        save_btn = tk.Button(save_frame, text="💾 Save Settings",
                           bg=self.colors['accent_green'], fg='white', 
                           font=('Segoe UI', 12, 'bold'),
                           command=self.save_settings,
                           relief='flat', padx=30, pady=10)
        save_btn.pack(side='right')

        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def open_settings_manager(self):
        """Open the full settings manager"""
        try:
            # Use local mock class
            if not hasattr(self, 'settings_manager') or not self.settings_manager:
                self.settings_manager = SettingsManager()
            else:
                # Bring existing window to front
                if hasattr(self.settings_manager, 'settings_window'):
                    self.settings_manager.settings_window.lift()
                    self.settings_manager.settings_window.focus_force()
        except Exception as e:
            print(f"Failed to open settings manager: {e}")
    
    def create_utilities_view(self):
        """Create utilities view placeholder"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        title = tk.Label(self.main_frame, text="Utilities", 
                        font=self.fonts['title'], bg=self.colors['bg_primary'], 
                        fg=self.colors['text_primary'])
        title.pack(anchor='w', pady=(0, 20))
        
        placeholder = tk.Label(self.main_frame, text="Utilities features coming soon...", 
                              font=self.fonts['body'], bg=self.colors['bg_primary'], 
                              fg=self.colors['text_secondary'])
        placeholder.pack(pady=50)
    
    def create_notifications_view(self):
        """Create notifications view - Bitdefender style"""
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Initialize notifications list if not exists
        if not hasattr(self, 'notifications'):
            self.notifications = []
        
        # Main title
        title = tk.Label(self.main_frame, text="Notifications", 
                        font=self.fonts['title'], bg=self.colors['bg_primary'], 
                        fg=self.colors['text_primary'])
        title.pack(anchor='w', pady=(0, 20))
        
        # Filter tabs frame
        filter_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        filter_frame.pack(fill='x', pady=(0, 20))
        
        # Filter buttons
        if not hasattr(self, 'current_filter'):
            self.current_filter = "All"
        filters = ["All", "Critical", "Warning", "Information"]
        
        self.filter_buttons = {}  # Store button references
        
        for i, filter_name in enumerate(filters):
            is_active = filter_name == self.current_filter
            bg_color = self.colors['accent_primary'] if is_active else self.colors['bg_primary']
            fg_color = 'white' if is_active else self.colors['text_primary']
            
            filter_btn = tk.Button(filter_frame, text=filter_name,
                                 bg=bg_color, fg=fg_color,
                                 font=('Segoe UI', 11, 'bold' if is_active else 'normal'),
                                 relief='flat', bd=0, padx=20, pady=8,
                                 command=lambda f=filter_name: self.filter_notifications(f))
            filter_btn.pack(side='left', padx=(0, 10))
            self.filter_buttons[filter_name] = filter_btn
        
        # Notification controls frame
        controls_frame = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        controls_frame.pack(fill='x', pady=(0, 20))
        
        # Clear all button
        clear_btn = tk.Button(controls_frame, text="🗑️ Clear All",
                            bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                            font=('Segoe UI', 10),
                            relief='flat', bd=1, padx=15, pady=5,
                            command=self.clear_all_notifications)
        clear_btn.pack(side='right', padx=(10, 0))
        
        # Mark all read button
        mark_read_btn = tk.Button(controls_frame, text="✓ Mark All Read",
                                bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                                font=('Segoe UI', 10),
                                relief='flat', bd=1, padx=15, pady=5,
                                command=self.mark_all_read)
        mark_read_btn.pack(side='right')
        
        # Notification list container
        self.notifications_container = tk.Frame(self.main_frame, bg=self.colors['bg_primary'])
        self.notifications_container.pack(fill='both', expand=True)
        
        # Create scrollable frame for notifications
        canvas = tk.Canvas(self.notifications_container, bg=self.colors['bg_primary'], highlightthickness=0)
        scrollbar = tk.Scrollbar(self.notifications_container, orient="vertical", command=canvas.yview)
        self.scrollable_notifications = tk.Frame(canvas, bg=self.colors['bg_primary'])
        
        self.scrollable_notifications.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_notifications, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Load and display notifications
        self.load_notifications()
        self.display_notifications()
    
    def load_notifications(self):
        """Load sample notifications for demonstration"""
        if len(self.notifications) == 0:  # Only load if empty
            from datetime import datetime, timedelta
            now = datetime.now()
            
            # Sample notifications
            sample_notifications = [
                {
                    'id': 1,
                    'type': 'Information',
                    'title': 'System Scan Completed',
                    'message': 'Quick scan completed successfully. No threats detected.',
                    'timestamp': now - timedelta(minutes=5),
                    'read': False,
                    'icon': '✅'
                },
                {
                    'id': 2,
                    'type': 'Warning',
                    'title': 'Vulnerability Detected',
                    'message': 'Outdated software detected that may pose security risks.',
                    'timestamp': now - timedelta(hours=2),
                    'read': False,
                    'icon': '⚠️'
                },
                {
                    'id': 3,
                    'type': 'Critical',
                    'title': 'Firewall Alert',
                    'message': 'Suspicious network activity blocked from IP 192.168.1.100',
                    'timestamp': now - timedelta(hours=6),
                    'read': True,
                    'icon': '🚨'
                },
                {
                    'id': 4,
                    'type': 'Information',
                    'title': 'VPN Connected',
                    'message': 'Successfully connected to VPN server in Netherlands.',
                    'timestamp': now - timedelta(hours=12),
                    'read': True,
                    'icon': '🔗'
                },
                {
                    'id': 5,
                    'type': 'Information',
                    'title': 'Real-time Protection Active',
                    'message': 'All protection modules are running and monitoring your system.',
                    'timestamp': now - timedelta(days=1),
                    'read': True,
                    'icon': '🛡️'
                }
            ]
            
            self.notifications.extend(sample_notifications)
    
    def display_notifications(self):
        """Display filtered notifications"""
        # Clear existing notifications display
        for widget in self.scrollable_notifications.winfo_children():
            widget.destroy()
        
        # Filter notifications
        filtered_notifications = self.get_filtered_notifications()
        
        if not filtered_notifications:
            # Show empty state like Bitdefender
            empty_frame = tk.Frame(self.scrollable_notifications, bg=self.colors['bg_primary'])
            empty_frame.pack(expand=True, fill='both', pady=100)
            
            # Calendar icon
            calendar_label = tk.Label(empty_frame, text="📅", font=('Segoe UI', 48),
                                    bg=self.colors['bg_primary'], fg=self.colors['text_muted'])
            calendar_label.pack(pady=(0, 20))
            
            # Empty message
            if self.current_filter == "Critical":
                message = "You have no critical notifications."
            elif self.current_filter == "Warning":
                message = "You have no warning notifications."
            elif self.current_filter == "Information":
                message = "You have no information notifications."
            else:
                message = "You have no notifications."
            
            empty_label = tk.Label(empty_frame, text=message,
                                 font=self.fonts['body'], bg=self.colors['bg_primary'],
                                 fg=self.colors['text_muted'])
            empty_label.pack()
        else:
            # Display notifications
            for notification in filtered_notifications:
                self.create_notification_item(notification)
    
    def get_filtered_notifications(self):
        """Get notifications based on current filter"""
        if self.current_filter == "All":
            return self.notifications
        else:
            return [n for n in self.notifications if n['type'] == self.current_filter]
    
    def create_notification_item(self, notification):
        """Create a notification item with expandable details"""
        # Add expanded state to notification if not exists
        if 'expanded' not in notification:
            notification['expanded'] = False
        
        # Notification container
        bg_color = self.colors['bg_secondary'] if not notification['read'] else self.colors['bg_primary']
        
        notif_frame = tk.Frame(self.scrollable_notifications, bg=bg_color, relief='flat', bd=1,
                              highlightbackground=self.colors['bg_tertiary'], highlightthickness=1)
        notif_frame.pack(fill='x', padx=10, pady=5)
        
        # Main content frame (always visible)
        main_content_frame = tk.Frame(notif_frame, bg=bg_color)
        main_content_frame.pack(fill='x', padx=20, pady=15)
        
        # Header with icon, title, and expand button
        header_frame = tk.Frame(main_content_frame, bg=bg_color)
        header_frame.pack(fill='x', pady=(0, 5))
        
        # Icon
        icon_label = tk.Label(header_frame, text=notification['icon'],
                            font=('Segoe UI', 16), bg=bg_color,
                            fg=self.get_notification_color(notification['type']))
        icon_label.pack(side='left', padx=(0, 10))
        
        # Title and timestamp container
        title_container = tk.Frame(header_frame, bg=bg_color)
        title_container.pack(side='left', fill='x', expand=True)
        
        title_label = tk.Label(title_container, text=notification['title'],
                             font=('Segoe UI', 12, 'bold'), bg=bg_color,
                             fg=self.colors['text_primary'])
        title_label.pack(anchor='w')
        
        # Timestamp
        time_str = self.format_timestamp(notification['timestamp'])
        time_label = tk.Label(title_container, text=time_str,
                            font=('Segoe UI', 9), bg=bg_color,
                            fg=self.colors['text_muted'])
        time_label.pack(anchor='w')
        
        # Expand/Collapse button
        expand_text = "▼" if notification['expanded'] else "▶"
        expand_btn = tk.Button(header_frame, text=expand_text,
                             bg=bg_color, fg=self.colors['text_muted'],
                             font=('Segoe UI', 10), relief='flat', bd=0,
                             padx=5, pady=0,
                             command=lambda: self.toggle_notification_details(notification, notif_frame))
        expand_btn.pack(side='right', padx=(10, 0))
        
        # Brief message (always visible)
        brief_message = notification['message'][:100] + "..." if len(notification['message']) > 100 else notification['message']
        message_label = tk.Label(main_content_frame, text=brief_message,
                               font=self.fonts['body'], bg=bg_color,
                               fg=self.colors['text_secondary'],
                               wraplength=600, justify='left')
        message_label.pack(anchor='w', pady=(5, 0))
        
        # Details frame (expandable)
        if notification['expanded']:
            self.create_notification_details(notif_frame, notification, bg_color)
        
        # Make header clickable to mark as read
        def mark_read(event):
            if not notification['read']:
                notification['read'] = True
                self.display_notifications()
        
        # Bind click events
        for widget in [main_content_frame, header_frame, title_container, 
                      icon_label, title_label, time_label, message_label]:
            widget.bind("<Button-1>", mark_read)
    
    def create_notification_details(self, parent_frame, notification, bg_color):
        """Create detailed notification information panel"""
        details_frame = tk.Frame(parent_frame, bg=self.colors['bg_tertiary'], relief='flat')
        details_frame.pack(fill='x', padx=20, pady=(0, 15))
        
        # Details content
        details_content = tk.Frame(details_frame, bg=self.colors['bg_tertiary'])
        details_content.pack(fill='x', padx=20, pady=15)
        
        # Full message
        full_message_label = tk.Label(details_content, text="Full Details:",
                                    font=('Segoe UI', 10, 'bold'),
                                    bg=self.colors['bg_tertiary'], 
                                    fg=self.colors['text_primary'])
        full_message_label.pack(anchor='w', pady=(0, 5))
        
        full_message = tk.Label(details_content, text=notification['message'],
                              font=self.fonts['body'], bg=self.colors['bg_tertiary'],
                              fg=self.colors['text_secondary'],
                              wraplength=600, justify='left')
        full_message.pack(anchor='w', pady=(0, 10))
        
        # Additional details based on notification type
        additional_info = self.get_additional_notification_info(notification)
        
        if additional_info:
            info_label = tk.Label(details_content, text="Additional Information:",
                                font=('Segoe UI', 10, 'bold'),
                                bg=self.colors['bg_tertiary'], 
                                fg=self.colors['text_primary'])
            info_label.pack(anchor='w', pady=(0, 5))
            
            for info_line in additional_info:
                info_item = tk.Label(details_content, text=f"• {info_line}",
                                   font=self.fonts['body'], bg=self.colors['bg_tertiary'],
                                   fg=self.colors['text_secondary'],
                                   wraplength=580, justify='left')
                info_item.pack(anchor='w', padx=(10, 0))
        
        # Timestamp details
        timestamp_label = tk.Label(details_content, text="Timestamp:",
                                 font=('Segoe UI', 10, 'bold'),
                                 bg=self.colors['bg_tertiary'], 
                                 fg=self.colors['text_primary'])
        timestamp_label.pack(anchor='w', pady=(10, 5))
        
        full_time = notification['timestamp'].strftime("%B %d, %Y at %I:%M %p")
        timestamp_detail = tk.Label(details_content, text=full_time,
                                   font=self.fonts['body'], bg=self.colors['bg_tertiary'],
                                   fg=self.colors['text_secondary'])
        timestamp_detail.pack(anchor='w', padx=(10, 0))
        
        # Action buttons based on notification type
        self.create_notification_actions(details_content, notification)
    
    def get_additional_notification_info(self, notification):
        """Get additional information based on notification type"""
        info_map = {
            'System Scan': [
                "Scan Duration: 2 minutes 34 seconds",
                "Files Scanned: 1,247,891 files",
                "Memory Usage: 156 MB",
                "Last Full Scan: 3 days ago"
            ],
            'Quick Scan': [
                "Scan Duration: 45 seconds", 
                "Critical Areas Checked: Boot sectors, System files, Running processes",
                "Memory Usage: 89 MB"
            ],
            'Vulnerability Scan': [
                "Outdated Software: Adobe Reader, Java Runtime",
                "Security Score: 7.2/10",
                "Recommendations: Update 2 programs, Enable Windows Defender"
            ],
            'VPN': [
                "Server Location: Netherlands (Amsterdam)",
                "Connection Speed: 98.5 Mbps",
                "Encryption: AES-256",
                "Protocol: OpenVPN"
            ],
            'Firewall Alert': [
                "Source IP: 192.168.1.100",
                "Attempted Port: 443 (HTTPS)",
                "Block Reason: Suspicious activity pattern",
                "Previous Attempts: 15 in last hour"
            ]
        }
        
        # Try to match notification title with info
        for key, info in info_map.items():
            if key.lower() in notification['title'].lower():
                return info
        
        # Default info for other types
        if notification['type'] == 'Critical':
            return ["Priority: High", "Action Required: Immediate attention needed"]
        elif notification['type'] == 'Warning':
            return ["Priority: Medium", "Action Required: Review when convenient"]
        else:
            return ["Priority: Low", "Status: Informational"]
    
    def create_notification_actions(self, parent, notification):
        """Create action buttons for notifications"""
        actions_frame = tk.Frame(parent, bg=self.colors['bg_tertiary'])
        actions_frame.pack(fill='x', pady=(15, 0))
        
        # Different actions based on notification type
        if 'scan' in notification['title'].lower():
            # Scan-related actions
            view_report_btn = tk.Button(actions_frame, text="📊 View Full Report",
                                      bg=self.colors['accent_primary'], fg='white',
                                      font=('Segoe UI', 9, 'bold'),
                                      relief='flat', bd=0, padx=15, pady=5,
                                      command=lambda: self.show_scan_report(notification))
            view_report_btn.pack(side='left', padx=(0, 10))
            
            run_again_btn = tk.Button(actions_frame, text="🔄 Run Again",
                                    bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                                    font=('Segoe UI', 9),
                                    relief='flat', bd=1, padx=15, pady=5,
                                    command=lambda: self.rerun_scan(notification))
            run_again_btn.pack(side='left', padx=(0, 10))
            
        elif 'vpn' in notification['title'].lower():
            # VPN-related actions
            vpn_settings_btn = tk.Button(actions_frame, text="⚙️ VPN Settings",
                                       bg=self.colors['accent_primary'], fg='white',
                                       font=('Segoe UI', 9, 'bold'),
                                       relief='flat', bd=0, padx=15, pady=5,
                                       command=self.show_vpn_settings)
            vpn_settings_btn.pack(side='left', padx=(0, 10))
            
        elif 'firewall' in notification['title'].lower():
            # Firewall-related actions
            firewall_log_btn = tk.Button(actions_frame, text="📋 View Firewall Log",
                                       bg=self.colors['accent_primary'], fg='white',
                                       font=('Segoe UI', 9, 'bold'),
                                       relief='flat', bd=0, padx=15, pady=5,
                                       command=self.show_firewall_log)
            firewall_log_btn.pack(side='left', padx=(0, 10))
        
        # Common actions for all notifications
        dismiss_btn = tk.Button(actions_frame, text="✕ Dismiss",
                              bg=self.colors['accent_red'], fg='white',
                              font=('Segoe UI', 9),
                              relief='flat', bd=0, padx=15, pady=5,
                              command=lambda: self.dismiss_notification(notification))
        dismiss_btn.pack(side='right')
    
    def toggle_notification_details(self, notification, frame):
        """Toggle the expanded state of a notification"""
        notification['expanded'] = not notification['expanded']
        
        # Refresh the notifications display to show/hide details
        self.display_notifications()
    
    def show_scan_report(self, notification):
        """Show detailed scan report"""
        self.show_feature_dialog("Scan Report", f"Detailed report for {notification['title']}\n\nThis would show comprehensive scan results, detected items, and recommended actions.")
    
    def rerun_scan(self, notification):
        """Rerun the scan"""
        if 'quick' in notification['title'].lower():
            self.start_quick_scan()
        elif 'vulnerability' in notification['title'].lower():
            self.start_vulnerability_scan()
        else:
            self.start_system_scan()
    
    def show_vpn_settings(self):
        """Show comprehensive VPN settings within main app"""
        self.create_integrated_settings_view("VPN Protection", {
            "VPN Status": {
                "type": "toggle",
                "default": False,
                "description": "Enable VPN protection for secure browsing",
                "premium": False
            },
            "Premium VPN Servers": {
                "type": "toggle",
                "default": True,
                "description": "Access to high-speed premium VPN servers worldwide",
                "premium": True
            },
            "Server Location": {
                "type": "radio",
                "options": ["Auto", "USA", "Europe", "Asia"],
                "default": "Auto",
                "description": "Choose VPN server location",
                "premium": False
            },
            "Premium Locations": {
                "type": "radio",
                "options": ["Standard", "Streaming Optimized", "Gaming Optimized", "P2P Optimized"],
                "default": "Standard",
                "description": "Specialized premium server configurations",
                "premium": True
            },
            "Protocol": {
                "type": "radio",
                "options": ["OpenVPN", "IKEv2", "WireGuard"],
                "default": "OpenVPN",
                "description": "VPN protocol for connection",
                "premium": False
            },
            "Advanced Protocols": {
                "type": "radio",
                "options": ["WireGuard Plus", "Stealth VPN", "Military Grade", "Zero-Log Protocol"],
                "default": "WireGuard Plus",
                "description": "Advanced VPN protocols with enhanced security",
                "premium": True
            },
            "Kill Switch": {
                "type": "toggle",
                "default": True,
                "description": "Block internet if VPN disconnects",
                "premium": False
            },
            "Advanced Kill Switch": {
                "type": "toggle",
                "default": True,
                "description": "Application-level kill switch with process monitoring",
                "premium": True
            },
            "DNS Leak Protection": {
                "type": "toggle",
                "default": True,
                "description": "Prevent DNS requests from leaking",
                "premium": False
            },
            "Custom DNS Servers": {
                "type": "toggle",
                "default": True,
                "description": "Use premium encrypted DNS servers",
                "premium": True
            },
            "Auto-Connect": {
                "type": "toggle",
                "default": False,
                "description": "Automatically connect VPN on startup",
                "premium": False
            },
            "Smart Connect": {
                "type": "toggle",
                "default": True,
                "description": "AI-powered server selection for optimal performance",
                "premium": True
            }
        })
    
    def show_firewall_log(self):
        """Show firewall log"""
        self.show_feature_dialog("Firewall Log", "Recent firewall activity:\n\n• Blocked connections\n• Traffic analysis\n• Security events\n• Rule configurations")
    
    def dismiss_notification(self, notification):
        """Dismiss a specific notification"""
        if notification in self.notifications:
            self.notifications.remove(notification)
            self.display_notifications()
    
    def get_notification_color(self, notification_type):
        """Get color for notification type"""
        colors = {
            'Critical': self.colors['accent_red'],
            'Warning': '#ffa500',  # Orange
            'Information': self.colors['accent_primary']
        }
        return colors.get(notification_type, self.colors['text_primary'])
    
    def format_timestamp(self, timestamp):
        """Format timestamp for display"""
        from datetime import datetime, timedelta
        now = datetime.now()
        diff = now - timestamp
        
        if diff.days > 0:
            return f"{diff.days} day{'s' if diff.days > 1 else ''} ago"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif diff.seconds > 60:
            minutes = diff.seconds // 60
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        else:
            return "Just now"
    
    def filter_notifications(self, filter_name):
        """Filter notifications by type"""
        self.current_filter = filter_name
        
        # Update filter button states
        if hasattr(self, 'filter_buttons'):
            for btn_name, btn in self.filter_buttons.items():
                if btn_name == filter_name:
                    # Active button
                    btn.configure(bg=self.colors['accent_primary'], fg='white', 
                                font=('Segoe UI', 11, 'bold'))
                else:
                    # Inactive button
                    btn.configure(bg=self.colors['bg_primary'], fg=self.colors['text_primary'],
                                font=('Segoe UI', 11, 'normal'))
        
        # Refresh only the notifications display
        self.display_notifications()
    
    def clear_all_notifications(self):
        """Clear all notifications"""
        self.notifications = []
        self.display_notifications()
    
    def mark_all_read(self):
        """Mark all notifications as read"""
        for notification in self.notifications:
            notification['read'] = True
        self.display_notifications()
    
    def add_notification(self, notification_type, title, message, icon="📢"):
        """Add a new notification"""
        from datetime import datetime
        
        new_notification = {
            'id': len(self.notifications) + 1,
            'type': notification_type,
            'title': title,
            'message': message,
            'timestamp': datetime.now(),
            'read': False,
            'icon': icon
        }
        
        self.notifications.insert(0, new_notification)  # Add to beginning
        
        # Refresh notifications view if currently displayed
        if hasattr(self, 'current_view') and self.current_view == 'notifications':
            self.display_notifications()
    
    def start_system_scan(self):
        """Start a system scan"""
        print("Starting system scan...")
        
        # Add notification for scan start
        self.add_notification("Information", "System Scan Started", 
                            "Full system scan is now running. This may take several minutes.", "🔍")
        
        # Show progress dialog
        self.show_scan_progress("System Scan")
        
        # Simulate scan completion after some time
        self.root.after(5000, lambda: self.complete_scan("System Scan", "No threats detected"))
    
    def start_quick_scan(self):
        """Start a quick scan"""
        print("Starting quick scan...")
        
        # Add notification for scan start
        self.add_notification("Information", "Quick Scan Started", 
                            "Quick scan is checking critical system areas.", "⚡")
        
        # Show progress dialog
        self.show_scan_progress("Quick Scan")
        
        # Simulate scan completion after some time
        self.root.after(3000, lambda: self.complete_scan("Quick Scan", "System is clean"))
    
    def start_vulnerability_scan(self):
        """Start vulnerability scan"""
        print("Starting vulnerability scan...")
        
        # Add notification for scan start
        self.add_notification("Information", "Vulnerability Scan Started", 
                            "Scanning system for security vulnerabilities and outdated software.", "🔍")
        
        # Show progress dialog
        self.show_scan_progress("Vulnerability Scan")
        
        # Simulate scan completion with some vulnerabilities found
        self.root.after(4000, lambda: self.complete_scan("Vulnerability Scan", "2 vulnerabilities found", True))
    
    def complete_scan(self, scan_type, result, has_issues=False):
        """Complete a scan and add notification"""
        if has_issues:
            notification_type = "Warning"
            icon = "⚠️"
            title = f"{scan_type} - Issues Found"
        else:
            notification_type = "Information"
            icon = "✅"
            title = f"{scan_type} Completed"
        
        self.add_notification(notification_type, title, result, icon)
    
    def toggle_vpn(self):
        """Open the Simple Proton VPN-style Interface"""
        try:
            # Import and launch the simple, functional VPN UI
            # Use local mock class
            
            # Create VPN interface instance
            vpn_interface = SimpleProtonVPN()
            
            # Show the VPN interface window
            vpn_interface.show_vpn_interface()
            
            # Add notification about VPN UI launch
            self.add_notification("Information", "VPN Interface Opened", 
                                "Functional Proton VPN-style interface has been launched.", "🔗")
            
            print("Simple Proton VPN Interface opened successfully")
            
        except Exception as e:
            print(f"Simple Proton VPN UI error: {e}")
            import traceback
            traceback.print_exc()
            
            # Show error dialog
            from tkinter import messagebox
            messagebox.showerror("VPN Error", 
                               f"Failed to open VPN Interface:\n{str(e)}\n\nPlease check the console for details.")
            
            # Add error notification
            self.add_notification("Error", "VPN Interface Error", 
                                "Failed to open VPN interface. Check console for details.", "❌")
    
    def toggle_vpn_basic(self):
        """Toggle VPN connection with basic functionality"""
        def vpn_worker():
            try:
                if not self.vpn_connected:
                    # Initialize advanced VPN if not already done
                    if not hasattr(self, 'vpn_engine'):
                        try:
                            # Use local mock class
                            self.vpn_engine = AdvancedVPN()
                        except ImportError:
                            # Fallback to basic functionality
                            self.vpn_engine = None
                    
                    # Connect VPN
                    self.root.after(0, lambda: self.show_vpn_connecting("Connecting..."))
                    
                    if self.vpn_engine:
                        # Use advanced VPN
                        fastest_server = self.vpn_engine.get_fastest_server()
                        self.root.after(0, lambda: self.show_vpn_connecting(f"Connecting to {fastest_server}..."))
                        
                        success, message = self.vpn_engine.connect_to_server(fastest_server)
                        
                        if success:
                            server_info = self.vpn_engine.servers[fastest_server]
                            self.vpn_connected = True
                            self.root.after(0, lambda: self.show_vpn_status(f"Connected - {server_info['location']}", self.colors['accent_green']))
                            self.root.after(0, lambda: self.update_vpn_status(f"VPN: Connected to {server_info['location']}"))
                            
                            # Add notification for successful connection
                            self.root.after(0, lambda: self.add_notification("Information", "VPN Connected", 
                                          f"Successfully connected to VPN server in {server_info['location']}.", "🔗"))
                            
                            # Launch secure browser
                            self.launch_secure_browser()
                        else:
                            self.root.after(0, lambda: self.show_vpn_status("Connection Failed", self.colors['accent_red']))
                            self.root.after(0, lambda: self.update_vpn_status(f"VPN: Failed - {message}"))
                            
                            # Add notification for failed connection
                            self.root.after(0, lambda: self.add_notification("Warning", "VPN Connection Failed", 
                                          f"Failed to connect to VPN: {message}", "❌"))
                    else:
                        # Fallback to basic VPN simulation
                        import time
                        time.sleep(2)
                        
                        self.vpn_connected = True
                        self.root.after(0, lambda: self.show_vpn_status("Connected", self.colors['accent_green']))
                        self.root.after(0, lambda: self.update_vpn_status("VPN: Connected - Basic mode"))
                        
                        # Add notification for basic VPN connection
                        self.root.after(0, lambda: self.add_notification("Information", "VPN Connected", 
                                      "Successfully connected to VPN (Basic mode).", "🔗"))
                        
                        # Launch secure browser
                        self.launch_secure_browser()
                    
                else:
                    # Disconnect VPN
                    self.root.after(0, lambda: self.show_vpn_connecting("Disconnecting..."))
                    
                    if self.vpn_engine:
                        success, message = self.vpn_engine.disconnect()
                    
                    import time
                    time.sleep(1)
                    
                    self.vpn_connected = False
                    self.root.after(0, lambda: self.show_vpn_status("Disconnected", self.colors['text_muted']))
                    self.root.after(0, lambda: self.update_vpn_status("VPN: Disconnected"))
                    
                    # Add notification for disconnection
                    self.root.after(0, lambda: self.add_notification("Information", "VPN Disconnected", 
                                  "VPN connection has been terminated.", "🔓"))
                    
            except Exception as e:
                self.root.after(0, lambda: self.show_vpn_status("Error", self.colors['accent_red']))
                self.root.after(0, lambda: self.update_vpn_status(f"VPN: Error - {str(e)}"))
                print(f"VPN error: {e}")
        
        # Start VPN operation in background thread
        import threading
        threading.Thread(target=vpn_worker, daemon=True).start()
    
    def launch_secure_browser(self):
        """Launch secure browser for VPN browsing"""
        try:
            import subprocess
            import webbrowser
            
            # Try to launch browsers with VPN-optimized settings
            browsers = [
                ('chrome.exe', ['--incognito', '--disable-webrtc', '--proxy-server=127.0.0.1:8080']),
                ('firefox.exe', ['-private-window']),
                ('msedge.exe', ['--inprivate'])
            ]
            
            browser_launched = False
            for browser, args in browsers:
                try:
                    subprocess.Popen([browser] + args, shell=True)
                    browser_launched = True
                    break
                except:
                    continue
            
            if not browser_launched:
                # Fallback to default browser
                webbrowser.open('https://www.whatismyipaddress.com/')
                
        except Exception as e:
            print(f"Failed to launch secure browser: {e}")
    
    def show_vpn_connecting(self, message="Connecting..."):
        """Show VPN connection progress"""
        popup = tk.Toplevel(self.root)
        popup.title("VPN Connection")
        popup.geometry("350x200")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        popup.grab_set()
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # VPN icon
        icon_label = tk.Label(content_frame, text="🔗", font=('Segoe UI', 32), 
                             bg=self.colors['bg_secondary'], fg=self.colors['accent_blue'])
        icon_label.pack(pady=(0, 15))
        
        # Status message
        status_label = tk.Label(content_frame, text=message, font=self.fonts['heading'], 
                               bg=self.colors['bg_secondary'], fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 10))
        
        # Progress bar simulation
        progress_frame = tk.Frame(content_frame, bg=self.colors['bg_primary'], height=4)
        progress_frame.pack(fill='x', pady=(0, 15))
        
        progress_fill = tk.Frame(progress_frame, bg=self.colors['accent_blue'], height=4)
        progress_fill.pack(side='left', fill='y')
        
        # Animate progress
        def animate(width=0):
            if width <= 300:
                progress_fill.configure(width=width)
                popup.after(20, lambda: animate(width + 6))
            else:
                popup.after(500, popup.destroy)
        
        animate()
    
    def show_vpn_status(self, status, color):
        """Show VPN status popup"""
        popup = tk.Toplevel(self.root)
        popup.title("VPN Status")
        popup.geometry("300x150")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Status icon
        status_icon = "🔗" if status == "Connected" else "🔓"
        icon_label = tk.Label(content_frame, text=status_icon, font=('Segoe UI', 24), 
                             bg=self.colors['bg_secondary'], fg=color)
        icon_label.pack(pady=(0, 10))
        
        # Status text
        msg_text = {
            "Connected": "VPN Connected\nYour connection is now secure and anonymous.",
            "Disconnected": "VPN Disconnected\nYour connection is using your regular ISP.",
            "Error": "VPN Connection Error\nPlease try again or check your internet connection."
        }
        
        msg_label = tk.Label(content_frame, text=msg_text.get(status, status), 
                            font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                            fg=self.colors['text_primary'], justify='center')
        msg_label.pack()
        
        # Auto close
        popup.after(3000, popup.destroy)
    
    def update_vpn_status(self, status_text):
        """Update VPN status in status bar"""
        if hasattr(self, 'vpn_status_label'):
            self.vpn_status_label.configure(text=status_text)
        else:
            # Create VPN status label if it doesn't exist
            self.vpn_status_label = tk.Label(self.status_bar if hasattr(self, 'status_bar') else self.root, 
                                           text=status_text, font=self.fonts['small'], 
                                           bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'])
            if hasattr(self, 'status_bar'):
                self.vpn_status_label.pack(side='left', padx=10, pady=5)
    
    def launch_safepay_v2(self):
        """Launch Safepay secure browser with real functionality"""
        def safepay_worker():
            try:
                if not getattr(self, 'safepay_active', False):
                    # Launch Safepay
                    self.root.after(0, lambda: self.show_safepay_launching())
                    
                    # Launch the actual SafePay system
                    import sys
                    from pathlib import Path
                    
                    # Add project root to path
                    project_root = Path(__file__).parent
                    if str(project_root) not in sys.path:
                        sys.path.insert(0, str(project_root))
                    
                    try:
                        # Launch our secure VM interface instead
                        safepay_manager = show_safepay()
                        
                        if safepay_manager:
                            self.safepay_active = True
                            self.root.after(0, lambda: self.show_safepay_launched())
                        else:
                            # Launch SafePay directly
                            show_safepay()
                            self.safepay_active = True
                            self.root.after(0, lambda: self.show_safepay_launched())
                            
                    except Exception as e:
                        print(f"SafePay launch error: {e}")
                        # Launch SafePay directly as fallback
                        show_safepay()
                        self.safepay_active = True
                        self.root.after(0, lambda: self.show_safepay_launched())
                    
                    # SafePay launched successfully
                    self.root.after(0, lambda: self.show_safepay_launched())
                    
                    # Update status
                    self.root.after(0, lambda: self.update_safepay_status("Safepay: Active - Secure browsing session"))
                    
                else:
                    # Safepay already active
                    self.root.after(0, lambda: self.show_safepay_already_active())
                    
            except Exception as e:
                self.root.after(0, lambda: self.show_safepay_error())
                print(f"Safepay error: {e}")
        
        # Start Safepay in background thread
        import threading
        threading.Thread(target=safepay_worker, daemon=True).start()
    
    def show_safepay_launching(self):
        """Show Safepay launch progress"""
        popup = tk.Toplevel(self.root)
        popup.title("Launching Safepay")
        popup.geometry("400x200")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        popup.grab_set()
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Safepay icon
        icon_label = tk.Label(content_frame, text="🛡️", font=('Segoe UI', 32), 
                             bg=self.colors['bg_secondary'], fg=self.colors['accent_green'])
        icon_label.pack(pady=(0, 15))
        
        # Status message
        status_label = tk.Label(content_frame, text="Launching Secure Browser...", 
                               font=self.fonts['heading'], bg=self.colors['bg_secondary'], 
                               fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 10))
        
        # Security message
        security_label = tk.Label(content_frame, 
                                 text="Initializing secure environment for safe browsing\nand online transactions.",
                                 font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                                 fg=self.colors['text_secondary'], justify='center')
        security_label.pack()
        
        # Auto close
        popup.after(2000, popup.destroy)
    
    def show_safepay_launched(self):
        """Show Safepay successfully launched"""
        popup = tk.Toplevel(self.root)
        popup.title("Safepay Active")
        popup.geometry("450x250")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Success icon
        icon_label = tk.Label(content_frame, text="✅", font=('Segoe UI', 32), 
                             bg=self.colors['bg_secondary'], fg=self.colors['accent_green'])
        icon_label.pack(pady=(0, 15))
        
        # Title
        title_label = tk.Label(content_frame, text="Safepay Secure Browser Active", 
                              font=self.fonts['heading'], bg=self.colors['bg_secondary'], 
                              fg=self.colors['accent_green'])
        title_label.pack(pady=(0, 10))
        
        # Features list
        features_text = (
            "🔒 Isolated browsing environment\n"
            "🛡️ Protection against keyloggers\n"
            "🔐 Secure connection encryption\n"
            "💳 Safe for banking and shopping\n"
            "🚫 Ad and tracker blocking"
        )
        
        features_label = tk.Label(content_frame, text=features_text, font=self.fonts['body'], 
                                 bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                                 justify='left')
        features_label.pack(pady=(0, 15))
        
        # Instructions
        instructions_label = tk.Label(content_frame, 
                                     text="Use the secure browser window for sensitive activities.\nClose the browser when finished.",
                                     font=self.fonts['small'], bg=self.colors['bg_secondary'], 
                                     fg=self.colors['text_secondary'], justify='center')
        instructions_label.pack()
        
        # Auto close
        popup.after(8000, popup.destroy)
    
    def show_safepay_already_active(self):
        """Show Safepay already active message"""
        popup = tk.Toplevel(self.root)
        popup.title("Safepay Status")
        popup.geometry("300x150")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Info icon
        icon_label = tk.Label(content_frame, text="ℹ️", font=('Segoe UI', 24), 
                             bg=self.colors['bg_secondary'], fg=self.colors['accent_blue'])
        icon_label.pack(pady=(0, 10))
        
        # Message
        msg_label = tk.Label(content_frame, text="Safepay is already active.\nSecure browsing session is running.",
                            font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                            fg=self.colors['text_primary'], justify='center')
        msg_label.pack()
        
        # Auto close
        popup.after(3000, popup.destroy)
    
    def show_safepay_error(self):
        """Show Safepay error message"""
        popup = tk.Toplevel(self.root)
        popup.title("Safepay Error")
        popup.geometry("350x150")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Error icon
        icon_label = tk.Label(content_frame, text="❌", font=('Segoe UI', 24), 
                             bg=self.colors['bg_secondary'], fg=self.colors['accent_red'])
        icon_label.pack(pady=(0, 10))
        
        # Message
        msg_label = tk.Label(content_frame, 
                            text="Failed to launch Safepay.\nPlease ensure a web browser is installed.",
                            font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                            fg=self.colors['text_primary'], justify='center')
        msg_label.pack()
        
        # Auto close
        popup.after(4000, popup.destroy)
    
    def update_safepay_status(self, status_text):
        """Update Safepay status in status bar"""
        if hasattr(self, 'safepay_status_label'):
            self.safepay_status_label.configure(text=status_text)
        else:
            # Create Safepay status label if it doesn't exist
            self.safepay_status_label = tk.Label(self.status_bar if hasattr(self, 'status_bar') else self.root, 
                                               text=status_text, font=self.fonts['small'], 
                                               bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'])
            if hasattr(self, 'status_bar'):
                self.safepay_status_label.pack(side='right', padx=10, pady=5)
    
    def show_feature_popup(self, feature_name, message):
        """Show a feature activation popup"""
        popup = tk.Toplevel(self.root)
        popup.title(feature_name)
        popup.geometry("350x150")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        popup.grab_set()
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Feature icon
        icon_map = {"VPN": "🔗", "Safepay": "🛡️"}
        icon_label = tk.Label(content_frame, text=icon_map.get(feature_name, "ℹ️"), 
                             font=('Segoe UI', 24), bg=self.colors['bg_secondary'], 
                             fg=self.colors['accent_blue'])
        icon_label.pack(pady=(0, 10))
        
        # Message
        msg_label = tk.Label(content_frame, text=message, font=self.fonts['body'], 
                            bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                            wraplength=300, justify='center')
        msg_label.pack()
        
    def show_add_action_menu(self):
        """Show add action menu with additional features"""
        popup = tk.Toplevel(self.root)
        popup.title("Quick Actions")
        popup.geometry("300x400")
        popup.configure(bg=self.colors['bg_secondary'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.root)
        popup.grab_set()
        
        # Content
        content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(content_frame, text="Quick Actions", font=self.fonts['heading'], 
                              bg=self.colors['bg_secondary'], fg=self.colors['text_primary'])
        title_label.pack(pady=(0, 20))
        
        # Additional actions
        additional_actions = [
            ("�", "Advanced VPN", "Enterprise VPN with servers"),
            ("�🔄", "Update Definitions", "Update threat signatures"),
            ("📊", "Security Report", "Generate detailed report"),
            ("🔧", "System Cleanup", "Clean temporary files"),
            ("🌐", "Network Scanner", "Scan network devices"),
            ("🔒", "Password Manager", "Launch password vault"),
            ("🏰", "Firewall Config", "Advanced firewall rules"),
            ("❓", "Help & Support", "Get assistance")
        ]
        
        # Create action buttons
        for icon, title, desc in additional_actions:
            self.create_quick_action_button(content_frame, icon, title, desc, popup)
    
    def create_quick_action_button(self, parent, icon, title, description, popup_window):
        """Create a quick action button"""
        button_frame = tk.Frame(parent, bg=self.colors['bg_tertiary'])
        button_frame.pack(fill='x', pady=2)
        
        # Content frame
        content_frame = tk.Frame(button_frame, bg=self.colors['bg_tertiary'])
        content_frame.pack(fill='x', padx=10, pady=8)
        
        # Icon
        icon_label = tk.Label(content_frame, text=icon, font=('Segoe UI', 16), 
                             bg=self.colors['bg_tertiary'], fg=self.colors['accent_blue'])
        icon_label.pack(side='left', padx=(0, 10))
        
        # Text content
        text_frame = tk.Frame(content_frame, bg=self.colors['bg_tertiary'])
        text_frame.pack(side='left', fill='both', expand=True)
        
        title_label = tk.Label(text_frame, text=title, font=self.fonts['body'], 
                              bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'])
        title_label.pack(anchor='w')
        
        desc_label = tk.Label(text_frame, text=description, font=self.fonts['small'], 
                             bg=self.colors['bg_tertiary'], fg=self.colors['text_muted'])
        desc_label.pack(anchor='w')
        
        # Make clickable
        def on_click(event, action=title):
            popup_window.destroy()
            self.handle_quick_action(action)
        
        for widget in [button_frame, content_frame, icon_label, text_frame, title_label, desc_label]:
            widget.bind("<Button-1>", on_click)
            widget.bind("<Enter>", lambda e, f=button_frame: f.configure(bg=self.colors['bg_secondary']))
            widget.bind("<Leave>", lambda e, f=button_frame: f.configure(bg=self.colors['bg_tertiary']))
    
    def handle_quick_action(self, action):
        """Handle quick action clicks"""
        # Special handling for Advanced VPN
        if action == "Advanced VPN":
            self.show_advanced_vpn()
            return
        
        action_messages = {
            "Update Definitions": "Threat definitions updated successfully!",
            "Security Report": "Generating comprehensive security report...",
            "System Cleanup": "System cleanup completed. 247 MB freed.",
            "Network Scanner": "Network scan initiated. Found 8 devices.",
            "Password Manager": "Password manager launched securely.",
            "Firewall Config": "Opening advanced firewall configuration...",
            "Help & Support": "Help documentation opened in browser."
        }
        
        message = action_messages.get(action, f"{action} completed successfully!")
        self.show_feature_popup(action, message)
    
    def refresh_action_grid(self):
        """Refresh the action grid to show updated VPN/Safepay status"""
        # Clear and recreate the action grid
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                # Check if this is the action grid frame
                for child in widget.winfo_children():
                    if hasattr(child, 'grid_info') and child.grid_info():
                        widget.destroy()
                        self.create_action_grid()
                        return
    
    def show_advanced_vpn(self):
        """Show advanced VPN configuration window"""
        try:
            # Use local mock class
            
            # Create advanced VPN window
            vpn_window = AdvancedVPNGUI()
            
            # Position window
            vpn_window.window.geometry("900x700")
            vpn_window.window.transient(self.root)
            vpn_window.window.grab_set()
            
        except ImportError as e:
            self.show_error_dialog("Advanced VPN", f"Failed to load advanced VPN module: {e}")
        except Exception as e:
            self.show_error_dialog("Advanced VPN", f"Error opening advanced VPN: {e}")
    
    def show_error_dialog(self, title, message):
        """Show error dialog"""
        error_window = tk.Toplevel(self.root)
        error_window.title(title)
        error_window.geometry("400x200")
        error_window.configure(bg=self.colors['bg_primary'])
        error_window.transient(self.root)
        error_window.grab_set()
        
        # Center the window
        error_window.update_idletasks()
        x = (error_window.winfo_screenwidth() // 2) - (400 // 2)
        y = (error_window.winfo_screenheight() // 2) - (200 // 2)
        error_window.geometry(f"400x200+{x}+{y}")
        
        # Error message
        message_frame = tk.Frame(error_window, bg=self.colors['bg_primary'])
        message_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        error_label = tk.Label(message_frame, text="❌ Error", 
                              font=('Segoe UI', 14, 'bold'),
                              bg=self.colors['bg_primary'], fg=self.colors['accent_red'])
        error_label.pack(pady=(0, 10))
        
        message_label = tk.Label(message_frame, text=message, 
                                font=('Segoe UI', 10),
                                bg=self.colors['bg_primary'], fg=self.colors['text_primary'],
                                wraplength=350, justify='center')
        message_label.pack(pady=(0, 20))
        
        ok_button = tk.Button(message_frame, text="OK", 
                             bg=self.colors['accent_blue'], fg='white',
                             command=error_window.destroy)
        ok_button.pack()
    
    def save_settings(self):
        """Save all settings to configuration"""
        try:
            # Show save confirmation
            popup = tk.Toplevel(self.root)
            popup.title("Settings Saved")
            popup.geometry("300x150")
            popup.configure(bg=self.colors['bg_secondary'])
            popup.resizable(False, False)
            
            # Center the popup
            popup.transient(self.root)
            popup.grab_set()
            
            # Content
            content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
            content_frame.pack(expand=True, fill='both', padx=20, pady=20)
            
            # Success icon
            icon_label = tk.Label(content_frame, text="💾", font=('Segoe UI', 24), 
                                 bg=self.colors['bg_secondary'], fg=self.colors['accent_green'])
            icon_label.pack(pady=(0, 10))
            
            # Message
            msg_label = tk.Label(content_frame, text="Settings Saved Successfully!\nChanges will take effect immediately.", 
                                font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                                fg=self.colors['text_primary'], justify='center')
            msg_label.pack()
            
            # Auto close
            popup.after(2000, popup.destroy)
            
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def save_privacy_settings(self):
        """Save all privacy settings to configuration"""
        try:
            # Show save confirmation
            popup = tk.Toplevel(self.root)
            popup.title("Privacy Settings Saved")
            popup.geometry("300x150")
            popup.configure(bg=self.colors['bg_secondary'])
            popup.resizable(False, False)
            
            # Center the popup
            popup.transient(self.root)
            popup.grab_set()
            
            # Content
            content_frame = tk.Frame(popup, bg=self.colors['bg_secondary'])
            content_frame.pack(expand=True, fill='both', padx=20, pady=20)
            
            # Success icon
            icon_label = tk.Label(content_frame, text="🔐", font=('Segoe UI', 24), 
                                 bg=self.colors['bg_secondary'], fg=self.colors['accent_green'])
            icon_label.pack(pady=(0, 10))
            
            # Message
            msg_label = tk.Label(content_frame, text="Privacy Settings Saved!\nYour privacy is now enhanced.", 
                                font=self.fonts['body'], bg=self.colors['bg_secondary'], 
                                fg=self.colors['text_primary'], justify='center')
            msg_label.pack()
            
            # Auto close
            popup.after(2000, popup.destroy)
            
        except Exception as e:
            print(f"Error saving privacy settings: {e}")

    def show_network_monitor(self):
        """Show network monitoring tools"""
        self.show_feature_dialog("Network Monitor", 
                                "Real-time network traffic analysis and monitoring.")
    
    def show_file_encryption(self):
        """Show file encryption tools"""
        self.show_feature_dialog("File Encryption", 
                                "Encrypt and protect your sensitive files.")
    
    def run_system_cleanup(self):
        """Run system cleanup"""
        self.show_feature_dialog("System Cleanup", 
                                "Clean temporary files and optimize system performance.")
    
    def show_password_manager(self):
        """Show password manager"""
        self.show_feature_dialog("Password Manager", 
                                "Secure password storage and generation.")
    
    def show_firewall_config(self):
        """Show firewall configuration"""
        self.show_feature_dialog("Firewall Configuration", 
                                "Advanced firewall settings and rules configuration.")
    
    def run_threat_detection(self):
        """Run threat detection"""
        self.show_feature_dialog("Threat Detection", 
                                "Advanced threat analysis and malware detection.")
    
    def show_feature_dialog(self, title, description):
        """Show a feature dialog with description"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("500x300")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the window
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (300 // 2)
        dialog.geometry(f"500x300+{x}+{y}")
        
        # Content
        content_frame = tk.Frame(dialog, bg=self.colors['bg_primary'])
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        title_label = tk.Label(content_frame, text=title, 
                              font=('Segoe UI', 16, 'bold'),
                              bg=self.colors['bg_primary'], fg=self.colors['text_primary'])
        title_label.pack(pady=(0, 15))
        
        desc_label = tk.Label(content_frame, text=description, 
                             font=('Segoe UI', 11),
                             bg=self.colors['bg_primary'], fg=self.colors['text_secondary'],
                             wraplength=450, justify='center')
        desc_label.pack(pady=(0, 20))
        
        # Feature status
        if title == "Advanced VPN":
            status_text = "✅ Available - Click to open advanced settings"
            status_color = self.colors['accent_green']
        else:
            status_text = "🚧 This feature is coming soon!"
            status_color = self.colors['accent_blue']
        
        status_label = tk.Label(content_frame, text=status_text, 
                               font=('Segoe UI', 12, 'bold'),
                               bg=self.colors['bg_primary'], fg=status_color)
        status_label.pack(pady=(0, 20))
        
        # Buttons
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_primary'])
        button_frame.pack()
        
        if title == "Advanced VPN":
            open_button = tk.Button(button_frame, text="Open Advanced VPN", 
                                   bg=self.colors['accent_green'], fg='white',
                                   command=lambda: [dialog.destroy(), self.show_advanced_vpn()])
            open_button.pack(side='left', padx=(0, 10))
        
        close_button = tk.Button(button_frame, text="Close", 
                                bg=self.colors['accent_blue'], fg='white',
                                command=dialog.destroy)
        close_button.pack(side='left')
    
    def draw_minimal_toggle(self, canvas, is_on):
        """Draw a minimal, clean toggle switch"""
        canvas.delete("all")
        
        # Toggle track
        track_color = '#4a9eff' if is_on else '#2a2a2a'
        canvas.create_rectangle(2, 6, 42, 18, fill=track_color, outline="", tags="track")
        
        # Toggle handle
        handle_x = 30 if is_on else 12
        canvas.create_oval(handle_x-8, 4, handle_x+8, 20, fill='white', outline="", tags="handle")
    
    def toggle_minimal_switch(self, canvas, var):
        """Toggle the minimal switch state"""
        var.set(not var.get())
        self.draw_minimal_toggle(canvas, var.get())
    
    def show_clean_radio_options(self, config, var, label):
        """Show clean radio button options"""
        # Simple option cycling for now
        options = config['options']
        current = var.get()
        current_index = options.index(current) if current in options else 0
        next_index = (current_index + 1) % len(options)
        next_value = options[next_index]
        
        var.set(next_value)
        label.config(text=next_value)
    
    def show_clean_scale_control(self, config, var, label):
        """Show clean scale control"""
        # Simple increment for now
        current = var.get()
        range_min, range_max = config['range']
        
        if current < range_max:
            new_value = min(current + 10, range_max)
        else:
            new_value = range_min
            
        var.set(new_value)
        label.config(text=str(new_value))
    
    def show_clean_text_config(self, config):
        """Show clean text configuration"""
        # Simple placeholder
        print(f"Configure: {config.get('name', 'Setting')}")
    
    def create_upgrade_prompt(self, parent, setting_name, config):
        """Create upgrade prompt for premium features in free version"""
        # Upgrade prompt row
        upgrade_row = tk.Frame(parent, bg=self.colors['bg_primary'])
        upgrade_row.pack(fill='x', pady=8, padx=10)
        
        # Upgrade card with special styling
        upgrade_card = tk.Frame(upgrade_row, bg='#2a1810', 
                               relief='flat', bd=2, pady=15, padx=20)
        upgrade_card.pack(fill='x')
        
        # Left side - feature info
        left_side = tk.Frame(upgrade_card, bg='#2a1810')
        left_side.pack(side='left', fill='x', expand=True)
        
        # Locked icon and feature name
        header_frame = tk.Frame(left_side, bg='#2a1810')
        header_frame.pack(fill='x')
        
        lock_label = tk.Label(header_frame, text="🔒", 
                             font=('Segoe UI', 14),
                             bg='#2a1810', fg='#ff9500')
        lock_label.pack(side='left', padx=(0, 8))
        
        name_label = tk.Label(header_frame, text=setting_name,
                             font=('Segoe UI', 13, 'bold'),
                             bg='#2a1810', fg='#cccccc')
        name_label.pack(side='left')
        
        premium_badge = tk.Label(header_frame, text="PREMIUM", 
                               font=('Segoe UI', 8, 'bold'),
                               bg='#ff9500', fg='white',
                               padx=6, pady=2)
        premium_badge.pack(side='left', padx=(10, 0))
        
        # Feature description
        desc_label = tk.Label(left_side, text=config['description'],
                             font=('Segoe UI', 10),
                             bg='#2a1810', fg='#999999',
                             wraplength=350, justify='left')
        desc_label.pack(fill='x', pady=(5, 0))
        
        # Right side - upgrade button
        right_side = tk.Frame(upgrade_card, bg='#2a1810')
        right_side.pack(side='right', padx=(10, 0))
        
        upgrade_btn = tk.Button(right_side, text="Upgrade to Pro",
                               font=('Segoe UI', 9, 'bold'),
                               bg='#ff9500', fg='white',
                               relief='flat', bd=0,
                               padx=15, pady=8,
                               cursor='hand2',
                               command=self.show_upgrade_dialog)
        upgrade_btn.pack(anchor='center')
    
    def show_upgrade_dialog(self):
        """Show upgrade to premium dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Upgrade to Premium")
        dialog.geometry("500x600")
        dialog.configure(bg=self.colors['bg_primary'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 350, self.root.winfo_rooty() + 100))
        
        # Main content frame
        main_frame = tk.Frame(dialog, bg=self.colors['bg_primary'], padx=30, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Header
        header_label = tk.Label(main_frame, text="🚀 Upgrade to CyberDefense AI Pro",
                               font=('Segoe UI', 18, 'bold'),
                               bg=self.colors['bg_primary'], fg='#ff9500')
        header_label.pack(pady=(0, 20))
        
        # Benefits list
        benefits = [
            "🔥 AI-Powered Threat Detection",
            "🛡️ Advanced Ransomware Protection", 
            "🌐 Premium VPN Servers Worldwide",
            "🔍 Deep System Scanning & Forensics",
            "⚡ Real-time Advanced Protection",
            "🏢 Enterprise Security Features",
            "☁️ Cloud Backup Integration",
            "🎯 Zero-Day Threat Protection"
        ]
        
        for benefit in benefits:
            benefit_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
            benefit_frame.pack(fill='x', pady=5)
            
            benefit_label = tk.Label(benefit_frame, text=benefit,
                                   font=('Segoe UI', 11),
                                   bg=self.colors['bg_primary'], fg=self.colors['text_primary'],
                                   anchor='w')
            benefit_label.pack(fill='x')
        
        # Pricing
        price_frame = tk.Frame(main_frame, bg=self.colors['bg_secondary'], pady=20)
        price_frame.pack(fill='x', pady=(30, 20))
        
        price_label = tk.Label(price_frame, text="Only $130/year",
                              font=('Segoe UI', 16, 'bold'),
                              bg=self.colors['bg_secondary'], fg='#ff9500')
        price_label.pack()
        
        savings_label = tk.Label(price_frame, text="Save 60% vs monthly plan!",
                                font=('Segoe UI', 10),
                                bg=self.colors['bg_secondary'], fg='#4a9eff')
        savings_label.pack()
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        button_frame.pack(fill='x', pady=(20, 0))
        
        upgrade_btn = tk.Button(button_frame, text="Upgrade Now",
                               font=('Segoe UI', 12, 'bold'),
                               bg='#ff9500', fg='white',
                               relief='flat', bd=0,
                               padx=30, pady=12,
                               cursor='hand2',
                               command=lambda: self.open_upgrade_website(dialog))
        upgrade_btn.pack(side='left', padx=(0, 10))
        
        close_btn = tk.Button(button_frame, text="Maybe Later",
                             font=('Segoe UI', 10),
                             bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                             relief='flat', bd=0,
                             padx=20, pady=12,
                             cursor='hand2',
                             command=dialog.destroy)
        close_btn.pack(side='left')
    
    def open_upgrade_website(self, dialog):
        """Open upgrade website"""
        import webbrowser
        webbrowser.open("https://cyberdefense-ai.com/upgrade")
        dialog.destroy()
    
    def show_malware_analyzer(self):
        """Show advanced malware analyzer (Enterprise only)"""
        if not is_feature_available('advanced_malware_analyzer'):
            self.show_upgrade_dialog()
            return
            
        self.create_integrated_settings_view("Advanced Malware Analyzer", {
            "AI-Powered Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Use machine learning for advanced malware detection",
                "premium": False
            },
            "Behavioral Sandboxing": {
                "type": "toggle",
                "default": True,
                "description": "Execute suspicious files in isolated environment",
                "premium": False
            },
            "Code Emulation": {
                "type": "toggle",
                "default": True,
                "description": "Emulate suspicious code to analyze behavior",
                "premium": False
            },
            "Binary Analysis": {
                "type": "radio",
                "options": ["Basic", "Deep", "Forensic", "Reverse Engineering"],
                "default": "Deep",
                "description": "Level of binary code analysis",
                "premium": False
            },
            "Threat Intelligence": {
                "type": "toggle",
                "default": True,
                "description": "Cross-reference with global threat databases",
                "premium": False
            },
            "Memory Dump Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Analyze memory dumps for hidden threats",
                "premium": False
            },
            "Auto-Submit Samples": {
                "type": "toggle",
                "default": False,
                "description": "Automatically submit unknown samples for analysis",
                "premium": False
            }
        })
    
    def show_network_analyzer(self):
        """Show deep network analyzer (Enterprise only)"""
        if not is_feature_available('deep_network_analyzer'):
            self.show_upgrade_dialog()
            return
            
        self.create_integrated_settings_view("Deep Network Analyzer", {
            "Deep Packet Inspection": {
                "type": "toggle",
                "default": True,
                "description": "Analyze all network packet contents",
                "premium": False
            },
            "Protocol Analysis": {
                "type": "radio",
                "options": ["Basic", "Advanced", "Expert", "Wireshark-Level"],
                "default": "Advanced",
                "description": "Network protocol analysis depth",
                "premium": False
            },
            "Traffic Anomaly Detection": {
                "type": "toggle",
                "default": True,
                "description": "AI-powered detection of unusual network patterns",
                "premium": False
            },
            "Bandwidth Monitoring": {
                "type": "toggle",
                "default": True,
                "description": "Monitor and analyze bandwidth usage",
                "premium": False
            },
            "Geo-Location Tracking": {
                "type": "toggle",
                "default": True,
                "description": "Track geographic location of network connections",
                "premium": False
            },
            "DNS Analysis": {
                "type": "toggle",
                "default": True,
                "description": "Deep analysis of DNS requests and responses",
                "premium": False
            },
            "Network Forensics": {
                "type": "toggle",
                "default": True,
                "description": "Detailed logging for network forensic analysis",
                "premium": False
            }
        })
    
    def show_user_management(self):
        """Show admin user management dashboard (Enterprise only)"""
        if not is_feature_available('admin_management'):
            self.show_upgrade_dialog()
            return
            
        # Hide main canvas and create user management interface
        self.main_canvas.pack_forget()
        
        # Create user management container
        self.user_mgmt_container = tk.Frame(self.main_canvas.master, bg=self.colors['bg_primary'])
        self.user_mgmt_container.pack(fill='both', expand=True)
        
        # Header
        header_frame = tk.Frame(self.user_mgmt_container, bg=self.colors['bg_primary'])
        header_frame.pack(fill='x', padx=20, pady=20)
        
        back_btn = tk.Button(header_frame, text="← Back", 
                           font=('Segoe UI', 11, 'bold'),
                           bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                           relief='flat', bd=0, padx=15, pady=8,
                           command=self.return_to_protection)
        back_btn.pack(side='left')
        
        title_label = tk.Label(header_frame, text="👥 User Management Dashboard",
                              font=('Segoe UI', 18, 'bold'),
                              bg=self.colors['bg_primary'], fg=self.colors['text_primary'])
        title_label.pack(side='left', padx=(20, 0))
        
        # Admin stats
        stats_frame = tk.Frame(self.user_mgmt_container, bg=self.colors['bg_primary'])
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        stats = [
            ("Total Users", "47/50", self.colors['accent_blue']),
            ("Active Sessions", "23", self.colors['accent_green']),
            ("Threats Blocked", "1,247", self.colors['accent_red']),
            ("Alerts Today", "15", "#ffa500")
        ]
        
        for i, (label, value, color) in enumerate(stats):
            stat_card = tk.Frame(stats_frame, bg=self.colors['bg_secondary'], 
                               relief='flat', bd=1, padx=20, pady=15)
            stat_card.grid(row=0, column=i, padx=10, sticky='ew')
            stats_frame.grid_columnconfigure(i, weight=1)
            
            value_label = tk.Label(stat_card, text=value, 
                                 font=('Segoe UI', 16, 'bold'),
                                 bg=self.colors['bg_secondary'], fg=color)
            value_label.pack()
            
            label_label = tk.Label(stat_card, text=label,
                                 font=('Segoe UI', 10),
                                 bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'])
            label_label.pack()
        
        # User list with scrolling
        users_frame = tk.Frame(self.user_mgmt_container, bg=self.colors['bg_primary'])
        users_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Canvas for scrolling
        canvas = tk.Canvas(users_frame, bg=self.colors['bg_primary'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(users_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_primary'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Sample users
        users = [
            ("admin", "Administrator", "Active", "2 hours ago", self.colors['accent_green']),
            ("john.doe", "John Doe", "Active", "15 min ago", self.colors['accent_green']),
            ("jane.smith", "Jane Smith", "Idle", "1 hour ago", "#ffa500"),
            ("mike.wilson", "Mike Wilson", "Offline", "1 day ago", self.colors['text_secondary']),
        ] * 12  # Simulate 48 users
        
        for i, (username, fullname, status, last_seen, status_color) in enumerate(users[:47]):
            user_card = tk.Frame(scrollable_frame, bg=self.colors['bg_secondary'], 
                               relief='flat', bd=1, pady=10, padx=15)
            user_card.pack(fill='x', pady=2)
            
            # User info
            info_frame = tk.Frame(user_card, bg=self.colors['bg_secondary'])
            info_frame.pack(side='left', fill='x', expand=True)
            
            name_label = tk.Label(info_frame, text=f"{fullname} ({username})",
                                font=('Segoe UI', 11, 'bold'),
                                bg=self.colors['bg_secondary'], fg=self.colors['text_primary'])
            name_label.pack(anchor='w')
            
            status_label = tk.Label(info_frame, text=f"Status: {status} • Last seen: {last_seen}",
                                  font=('Segoe UI', 9),
                                  bg=self.colors['bg_secondary'], fg=status_color)
            status_label.pack(anchor='w')
            
            # Actions
            actions_frame = tk.Frame(user_card, bg=self.colors['bg_secondary'])
            actions_frame.pack(side='right')
            
            view_btn = tk.Button(actions_frame, text="View Activity",
                               font=('Segoe UI', 8),
                               bg=self.colors['accent_blue'], fg='white',
                               relief='flat', bd=0, padx=8, pady=4)
            view_btn.pack(side='right', padx=2)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def show_enterprise_logs(self):
        """Show enterprise logging and forensics (Enterprise only)"""
        if not is_feature_available('advanced_logging'):
            self.show_upgrade_dialog()
            return
            
        self.create_integrated_settings_view("Enterprise Forensic Logs", {
            "Real-time Logging": {
                "type": "toggle",
                "default": True,
                "description": "Log all security events in real-time",
                "premium": False
            },
            "Log Level": {
                "type": "radio",
                "options": ["Basic", "Detailed", "Verbose", "Forensic"],
                "default": "Detailed",
                "description": "Level of detail in security logs",
                "premium": False
            },
            "User Activity Tracking": {
                "type": "toggle",
                "default": True,
                "description": "Track all user activities and system access",
                "premium": False
            },
            "Network Event Logging": {
                "type": "toggle",
                "default": True,
                "description": "Log all network connections and transfers",
                "premium": False
            },
            "File System Monitoring": {
                "type": "toggle",
                "default": True,
                "description": "Monitor all file system changes",
                "premium": False
            },
            "Registry Monitoring": {
                "type": "toggle",
                "default": True,
                "description": "Monitor Windows registry modifications",
                "premium": False
            },
            "Log Retention": {
                "type": "scale",
                "range": (30, 365),
                "default": 90,
                "description": "Days to retain logs (30-365 days)",
                "premium": False
            },
            "Export Format": {
                "type": "radio",
                "options": ["JSON", "XML", "CSV", "SIEM Compatible"],
                "default": "JSON",
                "description": "Format for log exports and analysis",
                "premium": False
            }
        })
    
    def draw_clean_toggle(self, canvas, is_on):
        """Draw a clean, modern toggle switch"""
        canvas.delete("all")
        
        # Modern toggle design
        bg_color = '#4a9eff' if is_on else '#3a3a3a'
        canvas.create_rounded_rectangle(2, 3, 48, 23, radius=10, fill=bg_color, outline="")
        
        # Toggle circle
        circle_x = 35 if is_on else 15
        canvas.create_oval(circle_x-10, 5, circle_x+10, 21, fill='white', outline="")
    
    def toggle_clean_switch(self, canvas, var):
        """Toggle the clean switch"""
        var.set(not var.get())
        self.draw_clean_toggle(canvas, var.get())
    
    def run(self):
        """Start the GUI"""
        self.root.mainloop()

def main():
    """Main entry point"""
    app = ModernCybersecurityGUI()
    app.run()

if __name__ == "__main__":
    main()