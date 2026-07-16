#!/bin/bash
DIR="$(dirname "$0")"
python3 "$DIR/backup_engine.py" --mode monthly --hash
