#!/bin/bash
# VERSION: 0.0.34
# AUTHORS: Ogekuri

# check parameters
if [ -z $2 ]; then
    echo "ERROR: missing parameters"
    echo ""
    echo "Usage:      $0 <listen port> <application url> [<environment name>]"
    echo ""
    echo "Examples:"
    echo "            $0 8000 http://127.0.0.1:8000"
    echo "            $0 8000 http://127.0.0.1:8000 test"
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

# cancella le cache di sviluppo
find . -type d -iname "__pycache__" -exec rm -rf "{}" +

# Imposta i valori di default
DEFAULT_NODE_PORT="8000"
DEFAULT_NODE_URL="http://127.0.0.1:8000"
DEFAULT_NODE_ENV=""

# Controlla se i parametri sono stati forniti
CFG_NODE_HOST="127.0.0.1"
CFG_NODE_PORT=${1:-$DEFAULT_NODE_PORT}
CFG_NODE_URL=${2:-http://$CFG_NODE_HOST:$CFG_NODE_PORT}
CFG_NODE_ENV=${3:-$DEFAULT_NODE_ENV}

IMAGE_NAME="debriddo-compose"

# Build and run container (with arguments or not)
#sudo docker compose up --build
sudo DOCKER_PORT=$CFG_NODE_PORT DOCKER_URL=$CFG_NODE_URL DOCKER_ENV=$CFG_NODE_ENV docker compose up --build

# Remove container after Ctr+C
ID=$(sudo docker ps -a | grep "${IMAGE_NAME}" | awk '{print $1}')
if [ -n "$ID" ]; then
    sudo docker rm -f $ID >/dev/null
fi

ID=$(sudo docker images -a | grep "${IMAGE_NAME}" | awk '{print $3}')
if [ -n "$ID" ]; then
    sudo docker rmi $ID >/dev/null
fi

# remove build cache
sudo docker buildx prune -f

# remove network
sudo docker network prune -f

# Print remaining containers and images
echo "Remaining docker containers:"
sudo docker ps -a

echo "Remaining docker images:"
sudo docker images -a

echo "Remaining docker networks:"
sudo docker network ls

echo "Remaining disk usage:"
sudo docker system df
