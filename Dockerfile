# Usa un'immagine base leggera
FROM python:3.12-slim

# Imposta i parametri con i valori passati con --build-arg (o con i valori di default)
ARG PORT=8000
ARG URL=https://127.0.0.1
ARG ENV=
RUN echo PORT=$PORT URL=$URL ENV=$ENV

# Imposta i parametri con i valori passati con le variabili d'ambiente (o con --build-arg di default)
ENV DOCKER_PORT=${DOCKER_PORT:-$PORT}
ENV DOCKER_URL=${DOCKER_URL:-$URL}
ENV DOCKER_ENV=${DOCKER_ENV:-$ENV}
RUN echo DOCKER_PORT=$DOCKER_PORT DOCKER_URL=$DOCKER_URL ENV=$DOCKER_ENV

# Working dir
WORKDIR /app

# This is to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Copia i requirements
COPY requirements.txt .

# Installa i requirements
RUN pip install -r requirements.txt

# Copia il contenuto
COPY . .

# Copia lo script di entrypoint nella directory di lavoro
COPY entrypoint.sh /entrypoint.sh

# Assicurati che lo script sia eseguibile
RUN chmod +x /entrypoint.sh

# Espone la porta specificata
EXPOSE $DOCKER_PORT

# Imposta lo script di entrypoint
ENTRYPOINT ["/entrypoint.sh"]
