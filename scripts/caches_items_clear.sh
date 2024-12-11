#!/bin/bash
# VERSION: 0.0.26
# AUTHORS: Ogekuri

cd -- "$(dirname "$0")/../"
echo "Run on path: "$(pwd -P)

# Nome del database SQLite
DB_PATH="caches_items.db"

rm -f "$DB_PATH"
