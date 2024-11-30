# Debriddo

Debriddo è un addon per Stremio per la ricerca dei film e delle serie tv sui motori di ricerca online di torrent.

# Installazione ed esecuzione

## Docker

- Ottenere l'immagine docker da GitHub Container Registry
    ```sh
    sudo docker pull "ghcr.io/ogekuri/debriddo:latest"
    ```
- Eseguire il conteiner docker
    ```sh
    sudo docker run -p "0.0.0.0:8000:8000" --env DOCKER_PORT="8000" --env DOCKER_URL="https://foo.bar:443" "ghcr.io/ogekuri/debriddo:latest"
    ````
- Eventualmente puoi specificare il nome dell'ambinete
    ```sh
    sudo docker run -p "0.0.0.0:8000:8000" --env DOCKER_PORT="8000" --env DOCKER_URL="https://foo.bar:443" --env DOCKER_ENV="test" "ghcr.io/ogekuri/debriddo:latest"
    ````
  Ora è accessibile attraverso `https://foo.bar:443`

- Terminare l'applicazione
    ```sh
    Ctrl+C
    ````

# Esecuzione dei sorgenti

## Python

- Per eseguire direnttamente i sorgenti si può usare lo script:
    ```sh
    scripts/run-python-sources.sh "0.0.0.0" "8000" "https://foo.bar:443" "dev"
    ```
## Docker

- Per eseguire i sorgenti in un conteiner docker usare lo script:
    ```sh
    scripts/run-docker-sources.sh "0.0.0.0" "8000" "https://foo.bar:443" "dev"
    ```

# Note per gli sviluppatori

## Visual Studio Code

- Dopo aver aperto il progetto è possibile creare il virtual environment con lo script:
    ```sh
    scripts/create_vscode_venv.sh
    ```

- Clean del progetto
    ```sh
    scripts/clean.sh
    ```
Altri scrpts sono presenti nella cartella scripts.

