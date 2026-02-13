@echo off
REM MicroHydro Complete Automation System Launcher (Windows)
REM Automatically finds Python and runs the complete automation system

echo 🚀 MicroHydro Complete Automation System Launcher
echo =================================================

set WORKSPACE=C:\MircoHydro
set SCRIPT=%WORKSPACE%\complete_automation_system.py

echo 🔍 Searching for Python interpreter...

REM Try different Python executables in order of preference
set PYTHON_CMDS=python3 python python.exe

set PYTHON_FOUND=
for %%cmd in (%PYTHON_CMDS%) do (
    %%cmd --version >nul 2>&1
    if !errorlevel! equ 0 (
        set PYTHON_FOUND=%%cmd
        echo ✅ Found Python: %%cmd
        goto :found_python
    )
)

:found_python
if "%PYTHON_FOUND%"=="" (
    echo ❌ No Python interpreter found
    echo.
    echo 📋 MANUAL EXECUTION REQUIRED:
    echo Please run the automation system manually:
    echo.
    echo 1. Ensure Python 3.6+ is installed
    echo 2. Run: python3 %SCRIPT%
    echo.
    echo Or try these common Python locations:
    for %%cmd in (%PYTHON_CMDS%) do (
        echo    %%cmd %SCRIPT%
    )
    echo.
    echo 💡 RECOMMENDED: Install Python 3 from https://python.org
    pause
    exit /b 1
)

REM Check if script exists
if not exist "%SCRIPT%" (
    echo ❌ Automation script not found: %SCRIPT%
    pause
    exit /b 1
)

echo 🔧 Starting complete automation suite...
echo.

REM Run the automation system
"%PYTHON_FOUND%" "%SCRIPT%" "%WORKSPACE%"

set EXIT_CODE=%errorlevel%

echo.
if %EXIT_CODE% equ 0 (
    echo 🎉 AUTOMATION COMPLETED SUCCESSFULLY!
    echo 📊 Check the generated log and report files
) else (
    echo ❌ AUTOMATION COMPLETED WITH ISSUES
    echo 📋 Check the log file for details
)

echo.
echo 📁 Generated files:
echo    - automation_log_*.txt (execution log)
echo    - automation_report_*.json (detailed results)
echo    - ai_agent_manifest_*.json (AI deployment plan)

pause
exit /b %EXIT_CODE%