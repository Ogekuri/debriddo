#!/bin/sh

# Usa valori di default se non sono stati definiti
# per default in ascolto sul container docker
CFG_NODE_HOST="0.0.0.0"
CFG_NODE_PORT=${DOCKER_PORT:-8000}
CFG_NODE_URL=${DOCKER_URL:-http://127.0.0.1:8000}
CFG_NODE_ENV=${DOCKER_ENV:-}

echo -e "INFO:     ENTRYPOINT: "NODE_URL=$CFG_NODE_URL NODE_ENV=$CFG_NODE_ENV exec uvicorn "main:app" --reload --host $CFG_NODE_HOST --port $CFG_NODE_PORT
export NODE_URL=$CFG_NODE_URL
export NODE_ENV=$CFG_NODE_ENV
exec uvicorn "main:app" --reload --host $CFG_NODE_HOST --port $CFG_NODE_PORT
