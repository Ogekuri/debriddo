#!/bin/bash

cd -- "$(dirname "$0")/../"
echo "Run on path: "$(pwd -P)

VENVDIR=".venv"

# Se non c'è il ${VENVDIR} lo crea
if ! [ -d "${VENVDIR}/" ]; then
    echo "ERROR! Virtual environment not present!"
    exit
fi

source ${VENVDIR}/bin/activate

now=$(date '+%Y-%m-%d_%H-%M-%S')

mv requirements.txt requirements_${now}.txt

#
# Only local packages on virtual environment
#  pip freeze -l > requirements.txt # or --local instead of -l
#
# Only local packages installed by the user on virtual environment
#  pip freeze --user > requirements.txt
#

${VENVDIR}/bin/pip3 freeze --local > requirements.txt
