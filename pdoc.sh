#!/bin/bash
# -*- coding: utf-8 -*-
# VERSION: 0.0.52
# AUTHORS: Ogekuri

now=$(date '+%Y-%m-%d_%H-%M-%S')

# 1. Get the full absolute path of the file (resolving symbolic links)
FULL_PATH=$(readlink -f "$0")

# 2. Extract the directory (the path without the filename)
SCRIPT_PATH=$(dirname "$FULL_PATH")

# 3. Extract the filename
SCRIPT_NAME=$(basename "$FULL_PATH")

# --- Output tests (can be removed) ---
#echo "Full path:          $FULL_PATH"
#echo "Directory:          $SCRIPT_PATH"
#echo "Script name:        $SCRIPT_NAME"

VENVDIR="${SCRIPT_PATH}/.venv"
#echo ${VENVDIR}

# If ${VENVDIR} does not exist, create it
if ! [ -d "${VENVDIR}/" ]; then
  echo -n "Create virtual environment ..."
  mkdir ${VENVDIR}/
  virtualenv --python=python3 ${VENVDIR}/ >/dev/null
  echo "done."

  # Install Python requirements
  source ${VENVDIR}/bin/activate

  echo -n "Install python requirements ..."
  ${VENVDIR}/bin/pip install -r "${SCRIPT_PATH}/requirements.txt" >/dev/null
  echo "done." 
else
  # echo "Virtual environment found."
  source ${VENVDIR}/bin/activate
fi

OUTPUT_DIR="${SCRIPT_PATH}/pdoc"

mkdir -p "${OUTPUT_DIR}"

PYTHONPYCACHEPREFIX="${OUTPUT_DIR}/__pycache__" \
  PYTHONPATH="${SCRIPT_PATH}/src:${PYTHONPATH}" \
  ${VENVDIR}/bin/python3 -m compileall -q "${SCRIPT_PATH}/src/debriddo"

PYTHONPATH="${SCRIPT_PATH}/src:${PYTHONPATH}" \
  ${VENVDIR}/bin/python3 -m pdoc --html --output-dir "${OUTPUT_DIR}" debriddo

echo "pdoc documentation generated in ${OUTPUT_DIR}"
