#!/bin/bash
# Python finder and executor for MicroHydro activation

echo "🔍 Finding Python installation..."

# Common Python locations on macOS
PYTHON_PATHS=(
    "/usr/bin/python3"
    "/usr/local/bin/python3"
    "/opt/homebrew/bin/python3"
    "/Library/Frameworks/Python.framework/Versions/Current/bin/python3"
    "/Applications/Xcode.app/Contents/Developer/usr/bin/python3"
    "/System/Library/Frameworks/Python.framework/Versions/Current/bin/python3"
)

SCRIPT_PATH="/Users/gripandripphdd/MircoHydro/automated_activation.py"

for python_path in "${PYTHON_PATHS[@]}"; do
    if [ -x "$python_path" ]; then
        echo "✅ Found Python at: $python_path"
        echo "🚀 Executing activation script..."
        exec "$python_path" "$SCRIPT_PATH"
    fi
done

echo "❌ Python not found in common locations"
echo "💡 Try installing Python or check your PATH"
exit 1