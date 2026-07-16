#!/bin/bash
DIR="$(dirname "$0")"
chmod +x "$DIR"/*.command
xattr -dr com.apple.quarantine "$DIR"
