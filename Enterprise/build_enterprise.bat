@echo off
echo Building CyberDefense AI ENTERPRISE version from Enterprise folder...

cd Enterprise

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Build Enterprise version
pyinstaller --onefile --windowed --name cybersecurityenterprise modern_gui.py

REM Move executable up one level
if exist dist\cybersecurityenterprise.exe move dist\cybersecurityenterprise.exe ..\

REM Clean up
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

cd ..

echo.
echo ✅ ENTERPRISE version built successfully!
echo 📁 Output: cybersecurityenterprise.exe
echo.
pause