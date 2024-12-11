#!/bin/bash
# VERSION: 0.0.26
# AUTHORS: Ogekuri

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

#
# Only local packages on virtual environment
#  pip freeze -l > pip-freeze.txt # or --local instead of -l
#
# Only local packages installed by the user on virtual environment
#  pip freeze --user > pip-freeze.txt
#

${VENVDIR}/bin/pip3 freeze --local > pip-freeze.txt
