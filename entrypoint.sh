#!/bin/sh
# VERSION: 0.0.34
# AUTHORS: Ogekuri


# Usa valori di default se non sono stati definiti
# per default in ascolto sul container docker
CFG_NODE_HOST="0.0.0.0"
CFG_NODE_PORT=${DOCKER_PORT:-8000}
CFG_NODE_URL=${DOCKER_URL:-http://127.0.0.1:8000}
CFG_NODE_ENV=${DOCKER_ENV:-}

# # Controlla se nproc è disponibile
# if command -v nproc >/dev/null 2>&1; then
#     NUM_CORES=$(nproc)
# else
#     echo "nproc non trovato. Imposta manualmente il numero di core."
#     NUM_CORES=1  # Valore predefinito
# fi

# # Calcola il numero di worker
# NUM_WORKERS=$(( NUM_CORES * 2 + 1 ))

# --workers $NUM_WORKERS

echo -e "INFO:     ENTRYPOINT: "NODE_URL=$CFG_NODE_URL NODE_ENV=$CFG_NODE_ENV exec uvicorn "main:app" --log-level warning --reload --host $CFG_NODE_HOST --port $CFG_NODE_PORT
export NODE_URL=$CFG_NODE_URL
export NODE_ENV=$CFG_NODE_ENV
exec uvicorn "main:app" --log-level warning --host $CFG_NODE_HOST --port $CFG_NODE_PORT
