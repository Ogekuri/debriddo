#!/bin/sh
# VERSION: 0.0.35
# AUTHORS: Ogekuri


# Usa valori di default se non sono stati definiti
# per default in ascolto sul container docker
CFG_NODE_HOST="0.0.0.0"
CFG_NODE_PORT=${DOCKER_PORT:-8000}
CFG_NODE_URL=${DOCKER_URL:-http://127.0.0.1:8000}
CFG_NODE_ENV=${DOCKER_ENV:-}

if [ -n "$NUM_WORKERS" ]; then
    if [ "$NUM_WORKERS" = "auto" ]; then
	echo "Try to set number of workers by cpu count."
	# Controlla se nproc è disponibile
	if command -v nproc >/dev/null 2>&1; then
	    NUM_CORES=$(nproc)
	else
	    echo "nproc non trovato. Imposta manualmente il numero di core."
	    NUM_CORES=1  # Valore predefinito
	fi
	# Calcola il numero di worker
	NUM_WORKERS=$(( NUM_CORES * 2 + 1 ))
    fi

    # If NUM_WORKERS is empty use 1 worker.
    WORKERS=${NUM_WORKERS:-1}
    echo "Use $WORKERS workers."
else
    echo "Not use workers."
fi

echo -e "INFO:     ENTRYPOINT: "NODE_URL=$CFG_NODE_URL NODE_ENV=$CFG_NODE_ENV PYTHONPATH=/app/src exec uvicorn "debriddo.main:app" --log-level warning --host $CFG_NODE_HOST --port $CFG_NODE_PORT
export NODE_URL=$CFG_NODE_URL
export NODE_ENV=$CFG_NODE_ENV
export PYTHONPATH="/app/src${PYTHONPATH:+:$PYTHONPATH}"

# pass number of thread, if exist
if [ -n "$N_THREADS" ]; then
    export N_THREADS=$N_THREADS
fi

if [ -n "$WORKERS" ]; then
    exec uvicorn "debriddo.main:app" --workers ${WORKERS} --log-level warning --host $CFG_NODE_HOST --port $CFG_NODE_PORT
else
    exec uvicorn "debriddo.main:app" --log-level warning --host $CFG_NODE_HOST --port $CFG_NODE_PORT
fi
