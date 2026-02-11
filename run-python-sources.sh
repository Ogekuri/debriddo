# -*- coding: utf-8 -*-
# VERSION: 0.0.1
# AUTHORS: Ogekuri

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

### VENV

VENVDIR="${SCRIPT_PATH}/.venv"
#echo ${VENVDIR}

# Se non c'è il ${VENVDIR} lo crea
if ! [ -d "${VENVDIR}/" ]; then
    echo "ERROR! Virtual environment not present!"
    exit
fi

# activete venv
source ${VENVDIR}/bin/activate

# cancella le cache di sviluppo
find . -type d -iname "__pycache__" -exec rm -rf "{}" +

### RUN 
echo "Execute script on path: "$(pwd -P)
echo "Terminate app with Ctrl+C"

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

echo "Run debriddo.main:app @"$CFG_NODE_HOST":"$CFG_NODE_PORT" from "$(pwd -P)

PYTHONPATH="$(pwd -P)/src${PYTHONPATH:+:$PYTHONPATH}" \
NODE_URL=$CFG_NODE_URL NODE_ENV=$CFG_NODE_ENV \

# pass number of thread, if exist
if [ -n "$N_THREADS" ]; then
    export N_THREADS=$N_THREADS
fi

if [ -n "$WORKERS" ]; then
    PYTHONPATH="${SCRIPT_PATH}/src:${PYTHONPATH}" \
	${VENVDIR}/bin/python3 -m uvicorn debriddo.main:app --workers $WORKERS --log-level warning --host $CFG_NODE_HOST --port $CFG_NODE_PORT
else
    PYTHONPATH="${SCRIPT_PATH}/src:${PYTHONPATH}" \
	${VENVDIR}/bin/python3 -m uvicorn debriddo.main:app --log-level warning --host $CFG_NODE_HOST --port $CFG_NODE_PORT
fi

# termina il venv
deactivate
