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
#echo "Percorso completo:   $FULL_PATH"
#echo "Directory:           $SCRIPT_PATH"
#echo "Nome script:         $SCRIPT_NAME"

# go to script path
cd "${SCRIPT_PATH}"

### VENV

VENVDIR="${SCRIPT_PATH}/.venv"
echo ${VENVDIR}

# rimuove il vecchio venv
if [ -d "${VENVDIR}/" ]; then
    echo -n "Remove old virtual enviromnet ..."
    rm -rf ${VENVDIR}/
    echo "done."
fi

# Se non c'e il ${VENVDIR} lo crea
if ! [ -d "${VENVDIR}/" ]; then
  echo -n "Create virtual environment ..."
  mkdir ${VENVDIR}/
  virtualenv --python=python3 ${VENVDIR}/ >/dev/null
  echo "done."

  # Installa i requisiti Python
  source ${VENVDIR}/bin/activate

  echo -n "Install python requirements ..."
  ${VENVDIR}/bin/pip install -r "requirements.txt"
  echo "done." 
else
  echo "ERROR: Already exist."
fi
