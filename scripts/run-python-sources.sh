#!/bin/bash

# check parameters
if [ -z $3 ]; then
    echo "ERROR: missing parameters"
    echo ""
    echo "Usage:      $0 <listen ip> <listen port> <application url> [<environment name>]"
    echo ""
    echo "Examples:"
    echo "            $0 127.0.0.1 8000 http://127.0.0.1:8000"
    echo "            $0 127.0.0.1 8000 http://127.0.0.1:8000 test"
    echo ""
    exit 1
fi

cd -- "$(dirname "$0")/../"
echo "Run on path: "$(pwd -P)
echo "Terminate app with Ctrl+C"

# Imposta i valori di default
DEFAULT_NODE_HOST="127.0.0.1"
DEFAULT_NODE_PORT="8000"
DEFAULT_NODE_URL="http://127.0.0.1:8000"
DEFAULT_NODE_ENV=""

# Controlla se i parametri sono stati forniti
CFG_NODE_HOST=${1:-$DEFAULT_NODE_HOST}
CFG_NODE_PORT=${2:-$DEFAULT_NODE_PORT}
CFG_NODE_URL=${3:-http://$CFG_NODE_HOST:$CFG_NODE_PORT}
CFG_NODE_ENV=${4:-$DEFAULT_NODE_ENV}

VENVDIR="venv"

# Se non c'è il ${VENVDIR} lo crea
if ! [ -d "${VENVDIR}/" ]; then
    echo -n "Create virtual environment ..."
    mkdir ${VENVDIR}/
    virtualenv --python=python3 ${VENVDIR}/ >/dev/null
    echo "done."
fi

source ${VENVDIR}/bin/activate

echo "Run main:app @"$CFG_NODE_HOST":"$CFG_NODE_PORT" from "$(pwd -P)

echo -n "Install python requirements ..."
${VENVDIR}/bin/pip install -r requirements.txt >/dev/null
echo "done."

NODE_URL=$CFG_NODE_URL NODE_ENV=$CFG_NODE_ENV ${VENVDIR}/bin/python3 -m uvicorn main:app --reload --host $CFG_NODE_HOST --port $CFG_NODE_PORT

# termina il venv
deactivate

# cancella il virual environmenr (run-python.sh)
if [ -d "${VENVDIR}/" ]; then
    rm -rf ${VENVDIR}/
fi

# cancella le cache di sviluppo
find . -type d -iname "__pycache__" -exec rm -rf "{}" +
