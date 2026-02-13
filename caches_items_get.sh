#!/bin/bash
# -*- coding: utf-8 -*-
# VERSION: 0.0.1
# AUTHORS: Ogekuri

now=$(date '+%Y-%m-%d_%H-%M-%S')

# 1. Ottieni il percorso assoluto completo del file (risolvendo i link simbolici)
FULL_PATH=$(readlink -f "$0")

# 2. Estrai la directory (il percorso senza il nome del file)
SCRIPT_PATH=$(dirname "$FULL_PATH")

# 3. Estrai il nome del file
SCRIPT_NAME=$(basename "$FULL_PATH")

# --- Test di output (puoi rimuoverli) ---
#echo "Percorso completo:   $FULL_PATH"
#echo "Directory:           $SCRIPT_PATH"
#echo "Nome script:         $SCRIPT_NAME"

# go to script path
cd "${SCRIPT_PATH}"

# Nome del database SQLite
DB_PATH="caches_items.db"

# Verifica che il file del database esista
if [ ! -f "$DB_PATH" ]; then
  echo "Errore: Il file del database '$DB_PATH' non esiste."
  exit 1
fi

# Elenca le tabelle nel database
echo "Tabelle trovate nel database '$DB_PATH':"
TABLES=$(sqlite3 "$DB_PATH" ".tables")

if [ -z "$TABLES" ]; then
  echo "Nessuna tabella trovata."
  exit 0
fi

# Stampa i nomi delle tabelle
for TABLE in $TABLES; do
  echo "- $TABLE"
done

# Stampa il contenuto di ciascuna tabella
echo ""
echo "Contenuto delle tabelle:"
for TABLE in $TABLES; do
  echo ""
  echo "Tabella: $TABLE"
  echo "-------------------"

  # Ottieni le colonne della tabella
  COLUMNS=$(sqlite3 "$DB_PATH" "PRAGMA table_info($TABLE);" | awk -F'|' '{print $2}' | paste -sd "," -)

  echo "Colonne: $COLUMNS"

  # Stampa il contenuto della tabella
  DATA=$(sqlite3 "$DB_PATH" "SELECT * FROM $TABLE;")
  if [ -z "$DATA" ]; then
    echo "Nessun dato trovato."
  else
#    sqlite3 "$DB_PATH" "SELECT * FROM $TABLE;"
    sqlite3 "$DB_PATH" "SELECT * FROM $TABLE;" | cut -d "|" -f 1-19,23- # salto i magnet, link e traker
  fi
done
