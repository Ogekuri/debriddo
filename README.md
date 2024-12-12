# Debriddo

**Version: 0.0.30**

Debriddo è un addon per Stremio per la ricerca dei film e delle serie tv sui motori di ricerca online di torrent.

Le informazioni per gli sviluppatori sono contenute nel file [DEVELOP.md](DEVELOP.md)


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

# Ringraziamenti

Un ringraziamento speciale a **Riki** che ha sostituito egregiamente ChatGPT del tutto gratuitamente!.

Il progetto è basato sul progetto di **aymene69** [Stremio Jackett Addon](https://github.com/aymene69/stremio-jackett) del quale integra parte dei sorgenti.

Tuttavia, dal momento che il supporto al [Jackett API Server](https://github.com/Jackett/Jackett) è stato completamente rimosso a favore delle ricerche dirette, il progetto non è mantenuto come fork del progretto principale, ma come progetto indipendente.
Grazie a **aymene69** e al team di **Jacket** per il loro prezioso contributo!

Un grazie infine anche ai realizzazetori dei plugins di qTorrentio che sono stati integrati in questo progetto: [LightDestory](https://github.com/LightDestory), [Scare!](https://Scare.ca/dl/qBittorrent/), Lima66, Diego de las Heras, sa3dany, Alyetama, BurningMop, scadams, BurningMop, nindogo, mauricci.
