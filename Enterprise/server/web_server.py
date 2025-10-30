#!/usr/bin/env python3
"""
CyberDefense AI Website Server
A simple HTTP server to host the cybersecurity platform website
"""

import http.server
import socketserver
import os
import sys
import webbrowser
import threading
import time
from pathlib import Path

class CyberDefenseWebServer:
    def __init__(self, port=8000, directory=None):
        self.port = port
        self.directory = directory or os.path.dirname(os.path.abspath(__file__))
        self.httpd = None
        
    def find_available_port(self, start_port=8000):
        """Find an available port starting from start_port"""
        import socket
        for port in range(start_port, start_port + 100):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', port))
                    return port
            except OSError:
                continue
        return None
        
    def start_server(self):
        """Start the web server"""
        try:
            # Find available port
            available_port = self.find_available_port(self.port)
            if not available_port:
                print("❌ No available ports found!")
                return False
                
            self.port = available_port
            
            # Change to website directory
            website_dir = os.path.join(self.directory, '../website')
            if os.path.exists(website_dir):
                os.chdir(website_dir)
            else:
                print(f"❌ Website directory not found: {website_dir}")
                return False
                
            # Create server
            handler = http.server.SimpleHTTPRequestHandler
            self.httpd = socketserver.TCPServer(("", self.port), handler)
            
            print("🛡️" + "="*60)
            print("    CyberDefense AI Website Server Started")
            print("="*62)
            print(f"🌐 Local server: http://localhost:{self.port}")
            print(f"🌍 Production URL: https://cyberdefense-ai.com")
            print(f"📁 Serving files from: {os.getcwd()}")
            print("🔧 Press Ctrl+C to stop the server")
            print("="*62)
            
            # Auto-open browser after a short delay
            threading.Timer(1.0, self.open_browser).start()
            
            # Start serving
            self.httpd.serve_forever()
            return True
            
        except Exception as e:
            print(f"❌ Error starting server: {e}")
            return False
            
        except OSError as e:
            if e.errno == 48:  # Address already in use
                print(f"❌ Port {self.port} is already in use.")
                print(f"🔄 Trying port {self.port + 1}...")
                self.port += 1
                return self.start_server()
            else:
                print(f"❌ Error starting server: {e}")
                return False
        except KeyboardInterrupt:
            self.stop_server()
            return True
            
    def stop_server(self):
        """Stop the web server"""
        if self.httpd:
            print("\n🛑 Shutting down CyberDefense AI Website Server...")
            self.httpd.shutdown()
            self.httpd.server_close()
            print("✅ Server stopped successfully.")
            
    def open_browser(self):
        """Open the website in the default browser"""
        try:
            url = f"http://localhost:{self.port}"
            webbrowser.open(url)
            print(f"🌐 Opened website in browser: {url}")
        except Exception as e:
            print(f"⚠️  Could not open browser automatically: {e}")
            print(f"🌐 Please manually visit: http://localhost:{self.port}")

def main():
    """Main function"""
    print("🛡️ CyberDefense AI Website Server")
    print("="*40)
    
    # Get port from command line or use default
    port = 8000  # Changed default to 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 8000.")
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create and start server
    server = CyberDefenseWebServer(port=port, directory=current_dir)
    
    try:
        if server.start_server():
            print("✅ Server started successfully!")
        else:
            print("❌ Failed to start server!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user.")
        server.stop_server()
    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()