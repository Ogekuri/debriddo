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

#export DEBRIDDO_CONFIG_URL='http://localhost:58443/C_N4IghgJhD2B2AS0DOAXEAuEALFKAOS6A9EQO7kB0e0ATgMZgoCmFtA5ugKwBsALLwGYQAGhBImNAG4BLOkwwgaTMABsITAEY1pEESHVadAaSYBPBQHYAogC0j8eAHkA4gCFnRgIoAFAEyuBABFAgRsAVQBNADkAQV5OZwtAgDUogBUAdU4IzgBhVKibNNyAGQApXOcASV9vMM89AFswAA8AZWkAL3lMTgAGPSYWuhUAVyRpOBNTUloIJAwAbQBdURUwWDZRsDYmBfRFkGk0VZAmTelYPaWjlTpaJDAaOAloPWk7h6foDTGQU6QtDQmAAjtsVMdzKIlEhRioUEhvBJPODIQoAIwDUTNFoAJT2cIRCgEWJAjUuuTAdCwTHxsPh+xAmL0EDApiQlOpTGSqh0xNJH3uNEez1+ozCfMw0F2AGtRtp3p9hd8xd5SLpMI5dgBCdG+ATxbiDYZjCZwJanFCNCAaGJ4aQYjQQbgAM3UfSYAg0nosFgAHLx0WALGAAy7uBALBA+rwA3oGFyMCgaKMmKI8OtTChaEpYMDk6nROIntSkym0-pNNoNQWK40mChIIwwN5njJ1DQFFabSAAL5AA/manifest.json'
# no ita filter
export DEBRIDDO_CONFIG_URL='http://localhost:58443/C_N4IghgJhD2B2AS0DOAXEAuEALFKAO6A9IQDbQDGYJWyK6ArABwAszAzCADQhICmATgDcAluV4YQ-XlQi8ARv2EQuIWQqUBpXgE8JAdgCiALQ3x4AeQDiAIUsaAigAUATNbYARd2yMBVAJoAcgCCzPSWeu4AagEAKgDq9H70AMLRAUYxyQAyAFLJlgCSzo4+9ioAtmAAHgDKwgBe4gwADNy8VeQkAK5IwnBa2gDu0PwQSBgA2gC63CRgsADmXWALvOPo022LwrBrkyDCJOQjSGD8cALQKofH-Kfnct0gMzwjaJgAjsskwii63FIkF0SCgkI4BPZvr9dOgAIytECVKoAJTWwNBGDYCPKO2SYHIWF4qKBIPW8O4EDA2iQeIJvEiVCUmIRNxOZ2gjy6PiZmGgqwA1l1FNcjmyHt1HINlJhzKsAISw5xsUIANhU7U6PT6sEmLxQ5QgciCeGEElhcggKoAZrJmrw2HJ7Xo9CxYWA9GAWFaVRA9BBmswWCpKHSMCh+F1eNw8HNtCgRlJYO9w5HuHwzgSwxGo6p5IppSmc+VeChIGBS45ziJZPwJPrDSAAL5AA/manifest.json'

# Execute application:
exec ${VENVDIR}/bin/python3 src/api_tester/api_tester.py "$@"
