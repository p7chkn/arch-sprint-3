#!/bin/bash

WORKDIR="$(pwd)"
export PYTHONPATH="$WORKDIR:$PYTHONPATH"

# Change to the directory where migrations are stored
cd infrastructure/postgres/migrations || { echo "Directory not found: infrastructure/postgres/migrations"; exit 1; }

# Run the migration script with the --up flag
python3 migrator.py --down

# Check if the migration was successful
if [ $? -eq 0 ]; then
    echo "Migration applied successfully."
else
    echo "Migration failed."
    exit 1
fi