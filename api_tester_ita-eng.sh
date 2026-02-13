#!/bin/bash
# -*- coding: utf-8 -*-
# VERSION: 0.0.1
# AUTHORS: Ogekuri

now=$(date '+%Y-%m-%d_%H-%M-%S')

# 1. Ottieni il percorso assoluto completo del file (risolvendo i link simbolici)
FULL_PATH=$(readlink -f "$0")

# 2. Estrai la directory (il percorso senza il nome del file)
SCRIPT_PATH=$(dirname "$FULL_PATH")

# 3. Estrai il nome del file
SCRIPT_NAME=$(basename "$FULL_PATH")

# --- Test di output (puoi rimuoverli) ---
#echo "Full Path:   $FULL_PATH"
#echo "Directory:   $SCRIPT_PATH"
#echo "Script Name: $SCRIPT_NAME"

VENVDIR="${SCRIPT_PATH}/.venv"
#echo ${VENVDIR}

# Se non c'è il ${VENVDIR} lo crea
if ! [ -d "${VENVDIR}/" ]; then
  echo -n "Create virtual environment ..."
  mkdir ${VENVDIR}/
  virtualenv --python=python3 ${VENVDIR}/ >/dev/null
  echo "done."

  # Install requirements
  source ${VENVDIR}/bin/activate

  echo -n "Install python requirements ..."
  ${VENVDIR}/bin/pip install -r "${SCRIPT_PATH}/requirements.txt" >/dev/null
  echo "done." 
else
  # echo "Virtual environment found."
  source ${VENVDIR}/bin/activate
fi

# ita/eng
export DEBRIDDO_CONFIG_URL='http://localhost:58443/C_N4IghgJhD2B2AS0DOAXEAuEALFKAO6A9IQDbQDGYJWyK6ArABwAszAzCADQhICmATgDcAluV4YQ-XlQi8ARv2EQuIWQqUBpXgE8JAdgCiALQ3x4AeQDiAIUsaAigAUATNbYARd2yMBVAJoAcgCCzPSWeu4AagEAKgDq9H70AMLRAUYxyQAyAFLJlgCSzo4+9ioAtmAAHgDKwgBe4pj0AAwqvFXkJACuSMJwWtoA7tD8EEgYANoAutwkYLAA5t1gi7wT6JMgvLAqwmiz20vCsOtTIMIk5KNIYPxwAtB7Vzd30HI9IIdIo2iYAI4rEj7XTcKRIbokFBIRwCexAkESACMbW4lSqACV1pDoRI2KiQOUTskwOQsLwsRCoRsQCiVBAwNokCSybxIlQlHiCZdrvxbvcPt0fJzMNA1gBrbqKZ68-nvHqOIbKTDmNYAQiRzjYoQAbO1Oj0+nApocUOUIHIgnhhMi5BAdQAzWQtXhsOSuvR6FhIsB6MAsB06iB6CAtZgsFSUVkYFD8bq8bh4ebaFCjKSwP6x+PcPh3MkxuMJ1TyRTKrNF8q8FCQMDVxz3ESyfgSM0WkAAXyAA/manifest.json'

# Execute application:
exec ${VENVDIR}/bin/python3 src/api_tester/api_tester.py "$@"
