# Debriddo

Debriddo it's a Stremio'addon to search torrent directly on online search andgines and play media with drbird services.

# Download ed esecusione

## via Python

- Clonare il repository
    ```sh
    git clone https://github.com/Ogekuri/debriddo
    ```
- Eseguire l'applicativo (la porta e l'ip sono facoltativi)
    ```sh
    cd debriddo
    ./run-python.sh <PORT> <IP>
    ````
  Ora è accessibile attraverso `<IP>:<PORT> o 127.0.0.1:8000`

- Terminare l'applicazione
    ```sh
    Ctrl+C
    ````

## via Docker

- Installare l'immagine docker
    ```sh
    sudo docker pull ghcr.io/ogekuri/debriddo:latest
    ./run-docker.sh
    ```

- Eseguire l'immagine ghcr.io/ogekuri/debriddo:latest
    ```sh
    sudo docker run ${IMAGE_NAME}
    ```
  Ora è accessibile attraverso `<IP>:<PORT> o 127.0.0.1:8000`
  
- Terminare l'applicazione
    ```sh
    Ctrl+C
    ````
# Opzionale
## Utilizzo dei certificati

Questa funzionalità è ancora da implementare.
