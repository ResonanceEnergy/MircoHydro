#!/bin/bash
# UNIVERSAL MASTER LAUNCHER - MicroHydro Complete Operations
# Auto-detects platform and launches appropriate master system
# ZERO DATA LOSS - Comprehensive backup and recovery

WORKSPACE="/Users/gripandripphdd/MircoHydro"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Detect platform
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PLATFORM="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="macos"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    PLATFORM="windows"
else
    PLATFORM="unknown"
fi

echo "🚀 UNIVERSAL MASTER LAUNCHER - MICROHYDRO COMPLETE OPERATIONS"
echo "============================================================="
echo ""
echo "📍 Platform detected: $PLATFORM"
echo "📍 Workspace: $WORKSPACE"
echo "📍 Timestamp: $TIMESTAMP"
echo ""

# Pre-flight validation
if [ ! -d "$WORKSPACE" ]; then
    echo "❌ ERROR: Workspace directory not found: $WORKSPACE"
    exit 1
fi

cd "$WORKSPACE" || exit 1

# Launch appropriate master system
case $PLATFORM in
    "linux"|"macos")
        echo "🐧 Launching Unix/Linux master system..."
        if [ -f "MASTER_LAUNCH_SYSTEM.sh" ]; then
            chmod +x MASTER_LAUNCH_SYSTEM.sh
            ./MASTER_LAUNCH_SYSTEM.sh
        else
            echo "❌ ERROR: MASTER_LAUNCH_SYSTEM.sh not found"
            exit 1
        fi
        ;;
    "windows")
        echo "🪟 Launching Windows master system..."
        if [ -f "MASTER_LAUNCH_SYSTEM.bat" ]; then
            ./MASTER_LAUNCH_SYSTEM.bat
        else
            echo "❌ ERROR: MASTER_LAUNCH_SYSTEM.bat not found"
            exit 1
        fi
        ;;
    *)
        echo "❌ ERROR: Unsupported platform: $PLATFORM"
        echo ""
        echo "Supported platforms:"
        echo "  - Linux (linux-gnu)"
        echo "  - macOS (darwin)"
        echo "  - Windows (msys/win32)"
        exit 1
        ;;
esac