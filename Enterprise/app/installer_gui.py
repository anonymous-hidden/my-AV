#!/usr/bin/env python3
"""
Professional Cybersecurity Platform Installer
Bitdefender-style installation interface
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
import threading
import time
import subprocess
import sys
from pathlib import Path

class CybersecurityInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cybersecurity Platform Installer")
        self.root.geometry("800x600")  # Back to standard size with scrolling
        self.root.configure(bg="#0a0e0f")
        self.root.resizable(False, False)
        
        # Make sure window stays on top for testing
        self.root.attributes('-topmost', True)
        self.root.after(2000, lambda: self.root.attributes('-topmost', False))
        
        # Modern green theme colors
        self.colors = {
            "bg_primary": "#0a0e0f",
            "bg_secondary": "#1a2f1f",
            "bg_tertiary": "#2d4a34",
            "accent_green": "#00ff88",
            "accent_light_green": "#4fffb0",
            "accent_dark_green": "#00cc6a",
            "accent_red": "#ff4757",
            "text_primary": "#ffffff",
            "text_secondary": "#a8e6b8",
            "border": "#3a5a42"
        }
        
        # Installation settings
        self.install_path = "C:\\Program Files\\Cybersecurity Platform"
        self.create_desktop_shortcut = tk.BooleanVar(value=True)
        self.create_start_menu = tk.BooleanVar(value=True)
        self.add_to_startup = tk.BooleanVar(value=False)
        self.install_vpn_component = tk.BooleanVar(value=True)
        self.install_safepay_component = tk.BooleanVar(value=True)
        self.install_scanner_component = tk.BooleanVar(value=True)
        self.enable_real_time_protection = tk.BooleanVar(value=True)
        self.install_type = tk.StringVar(value="quick")  # quick, custom, minimal
        self.current_step = 0
        self.max_steps = 6
        
        # Create installer frames
        self.create_header()
        self.create_main_content()
        self.create_footer()
        
        # Show installation type selection
        self.show_install_type()
        
        # Center window
        self.center_window()
        
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)  # Updated for standard height
        self.root.geometry(f"800x600+{x}+{y}")
        
    def create_header(self):
        """Create professional header with logo and title"""
        header_frame = tk.Frame(self.root, bg=self.colors["bg_secondary"], height=100)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        # Add a subtle top accent line
        accent_line = tk.Frame(header_frame, bg=self.colors["accent_green"], height=3)
        accent_line.pack(fill="x")
        
        # Logo and title with proper spacing
        title_frame = tk.Frame(header_frame, bg=self.colors["bg_secondary"])
        title_frame.pack(expand=True, fill="both", pady=10)
        
        # Shield icon and title
        icon_title_frame = tk.Frame(title_frame, bg=self.colors["bg_secondary"])
        icon_title_frame.pack(expand=True)
        
        tk.Label(icon_title_frame, text="🛡️", font=("Segoe UI", 32), 
                bg=self.colors["bg_secondary"], fg=self.colors["accent_green"]).pack(side="left", padx=(30, 15))
        
        title_text = tk.Frame(icon_title_frame, bg=self.colors["bg_secondary"])
        title_text.pack(side="left", expand=True, fill="y")
        
        tk.Label(title_text, text="Cybersecurity Platform", 
                font=("Segoe UI", 18, "bold"), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_primary"]).pack(anchor="w", pady=(8, 2))
        
        tk.Label(title_text, text="Professional Security Suite Installer", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w")
        
        # Version info in top right
        version_label = tk.Label(title_frame, text="v2.0", 
                               font=("Segoe UI", 10, "bold"), bg=self.colors["bg_secondary"], 
                               fg=self.colors["accent_green"])
        version_label.pack(side="right", padx=30, pady=10, anchor="ne")
        
    def create_main_content(self):
        """Create main content area with scrolling"""
        # Create scrollable main frame
        self.main_container = tk.Frame(self.root, bg=self.colors["bg_primary"])
        self.main_container.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self.main_container, bg=self.colors["bg_primary"], 
                               highlightthickness=0, bd=0)
        scrollbar = tk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.colors["bg_primary"])
        
        # Configure scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        
        # Set main_frame to the scrollable frame
        self.main_frame = self.scrollable_frame
        
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def create_footer(self):
        """Create footer with progress bar and buttons"""
        # Create footer frame that STAYS at bottom
        footer_frame = tk.Frame(self.root, bg=self.colors["bg_secondary"], height=120)
        footer_frame.pack(fill="x", side="bottom")
        footer_frame.pack_propagate(False)
        
        # Progress section
        progress_frame = tk.Frame(footer_frame, bg=self.colors["bg_secondary"])
        progress_frame.pack(fill="x", padx=20, pady=(10, 5))
        
        self.progress_label = tk.Label(progress_frame, text="Step 1 of 6: Installation Type", 
                                     font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                                     fg=self.colors["text_secondary"])
        self.progress_label.pack(anchor="w", pady=2)
        
        # Progress bar
        progress_bg = tk.Frame(progress_frame, bg=self.colors["bg_tertiary"], height=8)
        progress_bg.pack(fill="x", pady=2)
        
        self.progress_fill = tk.Frame(progress_bg, bg=self.colors["accent_green"], height=8)
        self.progress_fill.pack(side="left")
        
        # Button section - GUARANTEED VISIBLE
        button_container = tk.Frame(footer_frame, bg=self.colors["bg_secondary"], height=60)
        button_container.pack(fill="x", padx=20, pady=(5, 15))
        button_container.pack_propagate(False)
        
        # Buttons with LARGE size
        self.back_button = tk.Button(button_container, text="◀ Back", 
                                   font=("Segoe UI", 11, "bold"),
                                   bg=self.colors["bg_tertiary"], fg=self.colors["text_primary"],
                                   padx=25, pady=12, state="disabled", command=self.go_back,
                                   relief="flat", borderwidth=0, cursor="hand2")
        self.back_button.pack(side="left", pady=10)
        
        self.next_button = tk.Button(button_container, text="Next ▶", 
                                   font=("Segoe UI", 11, "bold"),
                                   bg=self.colors["accent_green"], fg="#000000",
                                   padx=25, pady=12, command=self.go_next,
                                   relief="flat", borderwidth=0, cursor="hand2")
        self.next_button.pack(side="right", pady=10)
        
        self.cancel_button = tk.Button(button_container, text="Cancel", 
                                     font=("Segoe UI", 11),
                                     bg=self.colors["accent_red"], fg="white",
                                     padx=25, pady=12, command=self.cancel_installation,
                                     relief="flat", borderwidth=0, cursor="hand2")
        self.cancel_button.pack(side="right", padx=(0, 10), pady=10)
        self.cancel_button.pack(side="right")
        
    def update_progress(self):
        """Update progress bar"""
        progress_width = int((self.current_step / (self.max_steps - 1)) * 760)
        self.progress_fill.configure(width=progress_width)
        
        step_names = ["Installation Type", "Welcome", "License Agreement", "Installation Path", "Options", "Installing", "Complete"]
        if self.current_step < len(step_names):
            self.progress_label.configure(text=f"Step {self.current_step + 1} of {self.max_steps}: {step_names[self.current_step]}")
        
    def clear_main_frame(self):
        """Clear main content area and reset scroll"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        # Reset scroll to top
        self.canvas.yview_moveto(0)
            
    def show_welcome(self):
        """Show welcome screen"""
        self.clear_main_frame()
        self.current_step = 1
        self.update_progress()
        
        # Welcome content
        welcome_frame = tk.Frame(self.main_frame, bg=self.colors["bg_primary"])
        welcome_frame.pack(expand=True, fill="both")
        
        # Large modern shield icon with glow effect
        shield_frame = tk.Frame(welcome_frame, bg=self.colors["bg_primary"])
        shield_frame.pack(pady=30)
        
        tk.Label(shield_frame, text="🛡️", font=("Segoe UI", 72), 
                bg=self.colors["bg_primary"], fg=self.colors["accent_green"]).pack()
        
        # Subtitle with modern spacing
        tk.Label(welcome_frame, text="Welcome to Cybersecurity Platform", 
                font=("Segoe UI", 26, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=(10, 5))
        
        tk.Label(welcome_frame, text="Next-generation security suite with advanced AI protection", 
                font=("Segoe UI", 13), bg=self.colors["bg_primary"], 
                fg=self.colors["text_secondary"]).pack(pady=(0, 20))
        
        # Modern features grid
        features_frame = tk.Frame(welcome_frame, bg=self.colors["bg_secondary"], relief="flat", bd=2)
        features_frame.pack(pady=25, padx=40, fill="x")
        
        # Add gradient-like top border
        gradient_top = tk.Frame(features_frame, bg=self.colors["accent_green"], height=2)
        gradient_top.pack(fill="x")
        
        features = [
            "🔒 AI-Powered Real-time Protection",
            "🌐 Global VPN with Zero-Log Policy", 
            "💳 SafePay Secure Banking Environment",
            "🔍 Advanced Behavioral Analysis",
            "🛡️ Complete Privacy Protection Suite"
        ]
        
        tk.Label(features_frame, text="✨ Key Features", font=("Segoe UI", 16, "bold"),
                bg=self.colors["bg_secondary"], fg=self.colors["accent_green"]).pack(pady=15)
        
        for i, feature in enumerate(features):
            feature_label = tk.Label(features_frame, text=feature, font=("Segoe UI", 12),
                    bg=self.colors["bg_secondary"], fg=self.colors["text_secondary"])
            feature_label.pack(pady=4, anchor="w", padx=30)
        
        self.back_button.configure(state="normal")
        self.next_button.configure(state="normal")
        
    def show_install_type(self):
        """Show installation type selection"""
        self.clear_main_frame()
        self.current_step = 0
        self.update_progress()
        
        # Title
        tk.Label(self.main_frame, text="Choose Installation Type", 
                font=("Segoe UI", 20, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=(20, 10))
        
        tk.Label(self.main_frame, text="Select the type of installation that best suits your needs", 
                font=("Segoe UI", 11), bg=self.colors["bg_primary"], 
                fg=self.colors["text_secondary"]).pack(pady=(0, 20))
        
        # Installation type options
        options_frame = tk.Frame(self.main_frame, bg=self.colors["bg_primary"])
        options_frame.pack(expand=True, fill="both", padx=30, pady=10)
        
        # Quick Install Option
        quick_frame = tk.Frame(options_frame, bg=self.colors["bg_secondary"], relief="flat", bd=2)
        quick_frame.pack(fill="x", pady=10)
        
        quick_header = tk.Frame(quick_frame, bg=self.colors["accent_green"], height=3)
        quick_header.pack(fill="x")
        
        quick_radio = tk.Radiobutton(quick_frame, text="⚡ Quick Install (Recommended)", 
                                   variable=self.install_type, value="quick",
                                   font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                   fg=self.colors["accent_green"], selectcolor=self.colors["bg_tertiary"],
                                   command=self.update_install_type)
        quick_radio.pack(anchor="w", padx=20, pady=10)
        
        tk.Label(quick_frame, text="• Install all components with default settings", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40)
        tk.Label(quick_frame, text="• Real-time protection, VPN, SafePay, and Scanner", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40)
        tk.Label(quick_frame, text="• Desktop shortcut and Start Menu entry", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40, pady=(0, 15))
        
        # Custom Install Option
        custom_frame = tk.Frame(options_frame, bg=self.colors["bg_secondary"], relief="flat", bd=2)
        custom_frame.pack(fill="x", pady=10)
        
        custom_header = tk.Frame(custom_frame, bg=self.colors["accent_light_green"], height=3)
        custom_header.pack(fill="x")
        
        custom_radio = tk.Radiobutton(custom_frame, text="🔧 Custom Install", 
                                    variable=self.install_type, value="custom",
                                    font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                    fg=self.colors["text_primary"], selectcolor=self.colors["bg_tertiary"],
                                    command=self.update_install_type)
        custom_radio.pack(anchor="w", padx=20, pady=10)
        
        tk.Label(custom_frame, text="• Choose which components to install", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40)
        tk.Label(custom_frame, text="• Select installation directory and options", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40)
        tk.Label(custom_frame, text="• Configure advanced settings", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40, pady=(0, 15))
        
        # Minimal Install Option
        minimal_frame = tk.Frame(options_frame, bg=self.colors["bg_secondary"], relief="flat", bd=2)
        minimal_frame.pack(fill="x", pady=10)
        
        minimal_header = tk.Frame(minimal_frame, bg=self.colors["text_secondary"], height=3)
        minimal_header.pack(fill="x")
        
        minimal_radio = tk.Radiobutton(minimal_frame, text="📦 Minimal Install", 
                                     variable=self.install_type, value="minimal",
                                     font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                     fg=self.colors["text_primary"], selectcolor=self.colors["bg_tertiary"],
                                     command=self.update_install_type)
        minimal_radio.pack(anchor="w", padx=20, pady=10)
        
        tk.Label(minimal_frame, text="• Core antivirus protection only", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40)
        tk.Label(minimal_frame, text="• Smallest disk footprint (~ 25 MB)", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40)
        tk.Label(minimal_frame, text="• No additional components", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=40, pady=(0, 15))
        
        self.back_button.configure(state="disabled")
        self.next_button.configure(state="normal")
        
        # Set default selection
        self.install_type.set("quick")
        self.update_install_type()
        
    def update_install_type(self):
        """Update installation settings based on selected type"""
        if self.install_type.get() == "quick":
            self.install_vpn_component.set(True)
            self.install_safepay_component.set(True)
            self.install_scanner_component.set(True)
            self.enable_real_time_protection.set(True)
            self.create_desktop_shortcut.set(True)
            self.create_start_menu.set(True)
            self.add_to_startup.set(False)
        elif self.install_type.get() == "minimal":
            self.install_vpn_component.set(False)
            self.install_safepay_component.set(False)
            self.install_scanner_component.set(False)
            self.enable_real_time_protection.set(True)
            self.create_desktop_shortcut.set(True)
            self.create_start_menu.set(False)
            self.add_to_startup.set(False)
        
    def show_license(self):
        """Show license agreement"""
        self.clear_main_frame()
        self.current_step = 2
        self.update_progress()
        
        tk.Label(self.main_frame, text="License Agreement", 
                font=("Segoe UI", 20, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=20)
        
        # License text area
        license_frame = tk.Frame(self.main_frame, bg=self.colors["bg_secondary"])
        license_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        license_text = tk.Text(license_frame, bg=self.colors["bg_tertiary"], 
                              fg=self.colors["text_primary"], font=("Consolas", 9),
                              wrap="word", height=15)
        license_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        license_content = """CYBERSECURITY PLATFORM LICENSE AGREEMENT

Copyright (c) 2025 Cybersecurity Platform. All rights reserved.

TERMS OF USE:
1. This software is provided for personal and educational use only.
2. You may install and use this software on your personal devices.
3. Redistribution or commercial use requires written permission.
4. The software is provided "as is" without warranties.
5. Use of this software implies acceptance of these terms.

PRIVACY POLICY:
- No personal data is collected or transmitted
- All scanning is performed locally on your device
- VPN connections are encrypted and anonymous
- SafePay browsing uses secure, isolated environment

By installing this software, you agree to these terms and conditions."""
        
        license_text.insert("1.0", license_content)
        license_text.configure(state="disabled")
        
        # Acceptance checkbox
        accept_frame = tk.Frame(self.main_frame, bg=self.colors["bg_primary"])
        accept_frame.pack(pady=10)
        
        self.accept_license = tk.BooleanVar()
        accept_cb = tk.Checkbutton(accept_frame, text="I accept the license agreement", 
                                  variable=self.accept_license, font=("Segoe UI", 11),
                                  bg=self.colors["bg_primary"], fg=self.colors["text_primary"],
                                  selectcolor=self.colors["bg_tertiary"],
                                  command=self.check_license_acceptance)
        accept_cb.pack()
        
        self.next_button.configure(state="disabled")
        self.back_button.configure(state="normal")
        
    def check_license_acceptance(self):
        """Enable/disable next button based on license acceptance"""
        if self.accept_license.get():
            self.next_button.configure(state="normal")
        else:
            self.next_button.configure(state="disabled")
            
    def show_install_path(self):
        """Show installation path selection"""
        self.clear_main_frame()
        self.current_step = 3
        self.update_progress()
        
        tk.Label(self.main_frame, text="Installation Directory", 
                font=("Segoe UI", 20, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=20)
        
        # Path selection
        path_frame = tk.Frame(self.main_frame, bg=self.colors["bg_secondary"])
        path_frame.pack(fill="x", padx=20, pady=20)
        
        tk.Label(path_frame, text="Select installation directory:", 
                font=("Segoe UI", 12), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_primary"]).pack(anchor="w", padx=20, pady=10)
        
        path_input_frame = tk.Frame(path_frame, bg=self.colors["bg_secondary"])
        path_input_frame.pack(fill="x", padx=20, pady=10)
        
        self.path_entry = tk.Entry(path_input_frame, font=("Segoe UI", 11), 
                                  bg=self.colors["bg_tertiary"], fg=self.colors["text_primary"])
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.path_entry.insert(0, self.install_path)
        
        browse_button = tk.Button(path_input_frame, text="Browse...", 
                                 font=("Segoe UI", 10), bg=self.colors["accent_green"], 
                                 fg="#000000", padx=15, command=self.browse_install_path)
        browse_button.pack(side="right")
        
        # Space requirements
        req_frame = tk.Frame(self.main_frame, bg=self.colors["bg_secondary"])
        req_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(req_frame, text="Space Requirements:", 
                font=("Segoe UI", 12, "bold"), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_primary"]).pack(anchor="w", padx=20, pady=5)
        
        tk.Label(req_frame, text="• Required space: 50 MB", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_secondary"]).pack(anchor="w", padx=30)
        
        tk.Label(req_frame, text="• Available space: 2.5 GB", 
                font=("Segoe UI", 10), bg=self.colors["bg_secondary"], 
                fg=self.colors["accent_light_green"]).pack(anchor="w", padx=30)
        
        self.next_button.configure(state="normal")
        
    def browse_install_path(self):
        """Browse for installation directory"""
        path = filedialog.askdirectory(title="Select Installation Directory",
                                      initialdir=os.path.dirname(self.install_path))
        if path:
            self.install_path = os.path.join(path, "Cybersecurity Platform")
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, self.install_path)
            
    def show_options(self):
        """Show installation options"""
        self.clear_main_frame()
        self.current_step = 4
        self.update_progress()
        
        tk.Label(self.main_frame, text="Installation Options", 
                font=("Segoe UI", 20, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=20)
        
        # Show component selection for custom install
        if self.install_type.get() == "custom":
            # Components section
            components_frame = tk.LabelFrame(self.main_frame, text="🔧 Components", 
                                           font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                           fg=self.colors["accent_green"])
            components_frame.pack(fill="x", padx=20, pady=10)
            
            component_items = [
                (self.install_vpn_component, "🌐 VPN Module", "Secure VPN with global servers (15 MB)"),
                (self.install_safepay_component, "💳 SafePay Browser", "Secure banking environment (8 MB)"),
                (self.install_scanner_component, "🔍 Deep Scanner", "Advanced malware scanning engine (12 MB)"),
                (self.enable_real_time_protection, "🛡️ Real-time Protection", "Always-on security monitoring (Required)")
            ]
            
            for var, title, desc in component_items:
                comp_frame = tk.Frame(components_frame, bg=self.colors["bg_secondary"])
                comp_frame.pack(fill="x", padx=15, pady=5)
                
                cb = tk.Checkbutton(comp_frame, text=title, variable=var,
                                   font=("Segoe UI", 11, "bold"), bg=self.colors["bg_secondary"],
                                   fg=self.colors["text_primary"], selectcolor=self.colors["bg_tertiary"])
                cb.pack(anchor="w")
                
                if title == "🛡️ Real-time Protection":
                    cb.configure(state="disabled")  # Always required
                
                tk.Label(comp_frame, text=f"   {desc}", font=("Segoe UI", 9),
                        bg=self.colors["bg_secondary"], fg=self.colors["text_secondary"]).pack(anchor="w")
        
        # Options frame
        options_frame = tk.LabelFrame(self.main_frame, text="⚙️ Additional Options", 
                                     font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                     fg=self.colors["accent_green"])
        options_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(options_frame, text="Select additional options:", 
                font=("Segoe UI", 12), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_primary"]).pack(anchor="w", padx=15, pady=10)
        
        # Checkboxes
        option_items = [
            (self.create_desktop_shortcut, "Create desktop shortcut", "Quick access from desktop"),
            (self.create_start_menu, "Add to Start Menu", "Add to Windows Start Menu"),
            (self.add_to_startup, "Start with Windows", "Launch automatically on startup")
        ]
        
        for var, title, desc in option_items:
            option_frame = tk.Frame(options_frame, bg=self.colors["bg_secondary"])
            option_frame.pack(fill="x", padx=15, pady=5)
            
            cb = tk.Checkbutton(option_frame, text=title, variable=var,
                               font=("Segoe UI", 11), bg=self.colors["bg_secondary"],
                               fg=self.colors["text_primary"], selectcolor=self.colors["bg_tertiary"])
            cb.pack(anchor="w")
            
            tk.Label(option_frame, text=f"   {desc}", font=("Segoe UI", 9),
                    bg=self.colors["bg_secondary"], fg=self.colors["text_secondary"]).pack(anchor="w")
        
        # Installation summary
        summary_frame = tk.LabelFrame(self.main_frame, text="📋 Installation Summary", 
                                     font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                     fg=self.colors["accent_green"])
        summary_frame.pack(fill="x", padx=20, pady=10)
        
        install_type_text = {
            "quick": "Quick Install - All Components",
            "custom": "Custom Install - Selected Components", 
            "minimal": "Minimal Install - Core Only"
        }
        
        tk.Label(summary_frame, text=f"Type: {install_type_text.get(self.install_type.get(), 'Unknown')}", 
                font=("Segoe UI", 11), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_primary"]).pack(anchor="w", padx=15, pady=5)
        
        # Calculate estimated size
        size = 15  # Base size
        if self.install_vpn_component.get(): size += 15
        if self.install_safepay_component.get(): size += 8  
        if self.install_scanner_component.get(): size += 12
        
        tk.Label(summary_frame, text=f"Estimated Size: ~{size} MB", 
                font=("Segoe UI", 11), bg=self.colors["bg_secondary"], 
                fg=self.colors["text_primary"]).pack(anchor="w", padx=15, pady=5)
        
        self.next_button.configure(text="Install", state="normal")
        
    def show_installing(self):
        """Show installation progress"""
        self.clear_main_frame()
        self.current_step = 5
        self.update_progress()
        
        tk.Label(self.main_frame, text="Installing Cybersecurity Platform", 
                font=("Segoe UI", 20, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=30)
        
        # Progress animation
        self.install_progress_frame = tk.Frame(self.main_frame, bg=self.colors["bg_secondary"])
        self.install_progress_frame.pack(fill="x", padx=40, pady=20)
        
        self.install_status = tk.Label(self.install_progress_frame, text="Preparing installation...", 
                                      font=("Segoe UI", 12), bg=self.colors["bg_secondary"], 
                                      fg=self.colors["text_primary"])
        self.install_status.pack(pady=10)
        
        # Progress bar for installation
        install_progress_bg = tk.Frame(self.install_progress_frame, bg=self.colors["bg_tertiary"], height=20)
        install_progress_bg.pack(fill="x", pady=10)
        
        self.install_progress_fill = tk.Frame(install_progress_bg, bg=self.colors["accent_light_green"], height=20)
        self.install_progress_fill.pack(side="left")
        
        self.install_percent = tk.Label(self.install_progress_frame, text="0%", 
                                       font=("Segoe UI", 14, "bold"), bg=self.colors["bg_secondary"], 
                                       fg=self.colors["accent_light_green"])
        self.install_percent.pack(pady=10)
        
        # Disable buttons during installation
        self.next_button.configure(state="disabled")
        self.back_button.configure(state="disabled")
        self.cancel_button.configure(state="disabled")
        
        # Start installation in separate thread
        threading.Thread(target=self.perform_installation, daemon=True).start()
        
    def perform_installation(self):
        """Perform the actual installation"""
        install_steps = [
            ("Preparing installation...", 10),
            ("Creating directories...", 25),
            ("Copying files...", 50),
            ("Creating shortcuts...", 75),
            ("Registering components...", 90),
            ("Finalizing installation...", 100)
        ]
        
        try:
            for status, percent in install_steps:
                self.root.after(0, lambda s=status, p=percent: self.update_install_progress(s, p))
                time.sleep(1.5)  # Simulate installation time
                
                if percent == 25:
                    # Create installation directory
                    self.install_path = self.path_entry.get()
                    os.makedirs(self.install_path, exist_ok=True)
                    
                elif percent == 50:
                    # Copy executable
                    exe_source = "CybersecurityPlatform.exe"
                    if os.path.exists(exe_source):
                        shutil.copy2(exe_source, os.path.join(self.install_path, "CybersecurityPlatform.exe"))
                    
                elif percent == 75:
                    # Create shortcuts
                    if self.create_desktop_shortcut.get():
                        self.create_shortcut("Desktop")
                    if self.create_start_menu.get():
                        self.create_shortcut("StartMenu")
                    
            self.root.after(0, self.show_complete)
            
        except Exception as e:
            self.root.after(0, lambda: self.show_error(str(e)))
            
    def update_install_progress(self, status, percent):
        """Update installation progress display"""
        self.install_status.configure(text=status)
        self.install_percent.configure(text=f"{percent}%")
        
        progress_width = int((percent / 100) * 680)
        self.install_progress_fill.configure(width=progress_width)
        
    def create_shortcut(self, location):
        """Create desktop or start menu shortcut"""
        try:
            import winshell
            if location == "Desktop":
                desktop = winshell.desktop()
                shortcut_path = os.path.join(desktop, "Cybersecurity Platform.lnk")
            else:
                start_menu = winshell.start_menu()
                shortcut_path = os.path.join(start_menu, "Cybersecurity Platform.lnk")
                
            target = os.path.join(self.install_path, "CybersecurityPlatform.exe")
            winshell.CreateShortcut(Path=shortcut_path, Target=target, 
                                   Icon=(target, 0), Description="Cybersecurity Platform")
        except:
            pass  # Ignore shortcut creation errors
            
    def show_complete(self):
        """Show installation complete screen"""
        self.clear_main_frame()
        self.current_step = 6
        self.update_progress()
        
        # Success content
        tk.Label(self.main_frame, text="✅", font=("Segoe UI", 64), 
                bg=self.colors["bg_primary"], fg=self.colors["accent_light_green"]).pack(pady=40)
        
        tk.Label(self.main_frame, text="Installation Complete!", 
                font=("Segoe UI", 24, "bold"), bg=self.colors["bg_primary"], 
                fg=self.colors["text_primary"]).pack(pady=10)
        
        tk.Label(self.main_frame, text="Cybersecurity Platform has been successfully installed", 
                font=("Segoe UI", 12), bg=self.colors["bg_primary"], 
                fg=self.colors["text_secondary"]).pack(pady=5)
        
        # Launch option
        launch_frame = tk.Frame(self.main_frame, bg=self.colors["bg_secondary"])
        launch_frame.pack(pady=30, padx=50, fill="x")
        
        self.launch_now = tk.BooleanVar(value=True)
        launch_cb = tk.Checkbutton(launch_frame, text="Launch Cybersecurity Platform now", 
                                  variable=self.launch_now, font=("Segoe UI", 12),
                                  bg=self.colors["bg_secondary"], fg=self.colors["text_primary"],
                                  selectcolor=self.colors["bg_tertiary"])
        launch_cb.pack(pady=10)
        
        # Update buttons
        self.next_button.configure(text="Finish", state="normal", command=self.finish_installation)
        self.back_button.configure(state="disabled")
        self.cancel_button.configure(text="Close", state="normal")
        
    def show_error(self, error_msg):
        """Show installation error"""
        messagebox.showerror("Installation Error", f"Installation failed:\n\n{error_msg}")
        self.cancel_installation()
        
    def go_next(self):
        """Go to next installation step"""
        if self.current_step == 0:
            self.show_welcome()
        elif self.current_step == 1:
            self.show_license()
        elif self.current_step == 2:
            if self.accept_license.get():
                if self.install_type.get() == "quick":
                    self.show_installing()
                else:
                    self.show_install_path()
        elif self.current_step == 3:
            self.install_path = self.path_entry.get()
            self.show_options()
        elif self.current_step == 4:
            self.show_installing()
            
    def go_back(self):
        """Go to previous installation step"""
        if self.current_step == 1:
            self.show_install_type()
        elif self.current_step == 2:
            self.show_welcome()
        elif self.current_step == 3:
            self.show_license()
        elif self.current_step == 4:
            self.show_install_path()
            
    def finish_installation(self):
        """Finish installation and optionally launch"""
        if self.launch_now.get():
            try:
                exe_path = os.path.join(self.install_path, "CybersecurityPlatform.exe")
                if os.path.exists(exe_path):
                    subprocess.Popen([exe_path])
            except Exception as e:
                messagebox.showerror("Launch Error", f"Could not launch application:\n{e}")
        
        self.root.quit()
        
    def cancel_installation(self):
        """Cancel installation"""
        if messagebox.askyesno("Cancel Installation", "Are you sure you want to cancel the installation?"):
            self.root.quit()
            
    def run(self):
        """Run the installer"""
        self.root.mainloop()

if __name__ == "__main__":
    installer = CybersecurityInstaller()
    installer.run()