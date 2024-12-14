#!/bin/bash
# VERSION: 0.0.32
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

cd -- "$(dirname "$0")/../"
echo "Run on path: "$(pwd -P)
echo "Terminate app with Ctrl+C"

# Imposta i valori di default
DEFAULT_NODE_PORT="8000"
DEFAULT_NODE_URL="http://127.0.0.1:8000"
DEFAULT_NODE_ENV=""

# Controlla se i parametri sono stati forniti
CFG_NODE_HOST="127.0.0.1"
CFG_NODE_PORT=${1:-$DEFAULT_NODE_PORT}
CFG_NODE_URL=${2:-http://$CFG_NODE_HOST:$CFG_NODE_PORT}
CFG_NODE_ENV=${3:-$DEFAULT_NODE_ENV}

# cancella il virtual environment
VENVDIR=".venv"
if [ -d "${VENVDIR}/" ]; then
    rm -rf ${VENVDIR}/
fi

# cancella il virual environmenr (run-python.sh)
VENVDIR=".venv_run-python"
if [ -d "${VENVDIR}/" ]; then
    rm -rf ${VENVDIR}/
fi

# cancella le cache di sviluppo
find . -type d -iname "__pycache__" -exec rm -rf "{}" +

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
