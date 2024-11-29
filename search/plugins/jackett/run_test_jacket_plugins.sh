#!/bin/bash

#cd -- "$(dirname "$0")/../"
echo "Run on path: "$(pwd -P)
echo "Terminate app with Ctrl+C"

VENVDIR="venv"

# Se non c'è il ${VENVDIR} lo crea
if ! [ -d "${VENVDIR}/" ]; then
    echo "Error: virtual environmet not preset"
    exit 1
fi

source ${VENVDIR}/bin/activate


${VENVDIR}/bin/python3 test_jacket_plugins.py

# termina il venv
deactivate

