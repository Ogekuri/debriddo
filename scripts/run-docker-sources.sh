#!/bin/bash
# VERSION: 0.0.28
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

IMAGE_NAME="debriddo:docker"

# Build container (with arguments or not)
#
# sudo docker build -f Dockerfile -t ${IMAGE_NAME} .
#
sudo docker build -f Dockerfile -t ${IMAGE_NAME} --build-arg PORT=$CFG_NODE_PORT --build-arg URL=$CFG_NODE_URL --build-arg ENV=$CFG_NODE_ENV .

# Run container (with environment or not)
#
# sudo docker run -p 127.0.0.1:8000:8000 ${IMAGE_NAME}
#
sudo docker run -p $CFG_NODE_HOST:$CFG_NODE_PORT:$CFG_NODE_PORT --env DOCKER_PORT=$CFG_NODE_PORT --env DOCKER_URL=$CFG_NODE_URL --env DOCKER_ENV=$CFG_NODE_ENV ${IMAGE_NAME}

# Remove container after Ctr+C
IMAGE_ID=$(sudo docker images -a ${IMAGE_NAME} | grep -v IMAGE | awk '{print $3}')
CONTAINER_IDS=$(sudo docker ps -a | grep ${IMAGE_NAME} | awk '{print $1}')

# stop and remove containers
if [ -n "${CONTAINER_IDS}" ]; then
    sudo docker stop ${CONTAINER_IDS}
    sudo docker rm ${CONTAINER_IDS}
fi

# remove image
if [ -n "${IMAGE_ID}" ]; then
    sudo docker rmi ${IMAGE_ID}
fi

# remove build cache
sudo docker buildx prune -f

# Print remaining containers and images
echo "Remaining docker containers:"
sudo docker ps -a

echo "Remaining docker images:"
sudo docker images -a

echo "Remaining docker networks:"
sudo docker network ls

echo "Remaining disk usage:"
sudo docker system df
