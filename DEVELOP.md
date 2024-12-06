
# Informazioni per gli sviluppatori

## TODO

Attività ancora da portare a termine prima del primo rilascio.

### Implementazioni

* Implemetare l'aggiornamento via crontab
* Implementare l'aggiornamento automatico
* Mettere un aprogres se il torrent non è al 100% su debrid?
* implementare l'esportazione e l'importazione del database della cache per i container docker.
* verificare perché non tiene i risultati della cache per primi
* Implementare il supporto per https://debrid-link.com/
* Implementare il supporto alle autenticazioni nei plugins di ricerca
* Implementare il supporto 'private'/'public' per i motori di ricerca che hanno la password (da decidere)
* Implementare il supporto per Il Corsaro Blu
* Modificare CORSMiddleware, cambiare "origins"
* Rimuovere **[NON FUNZIONANTE]** una volta implementati
* Rimuovere **[NON TESTATO]** una volta testati

### Test da completare

- Testare 'alldebrid', 'premiumize', 'torbox', 'debridlink']
- Testare NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/main/videos/nocache.mp4"

## Esecuzione dei sorgenti

### Python

- Per eseguire direnttamente i sorgenti si può usare lo script:
    ```sh
    scripts/run-python-sources.sh "0.0.0.0" "8000" "https://foo.bar:443" "dev"
    ```
### Docker

- Per eseguire i sorgenti in un conteiner docker usare lo script:
    ```sh
    scripts/run-docker-sources.sh "0.0.0.0" "8000" "https://foo.bar:443" "dev"
    ```

## Versionamento, repository e deployment

La costante **APPLICATION_VERSION** nel constant.py contiene il numero di versione nel formato **X.Y.Z** (ad esempio 1.2.3).

Le versioni rilasciate vengono taggate nel brench *master* nel formato **vX.Y.Z** (ad esempio v1.2.3).

Ad ogni rilascio, quando il *master* viene taggato, una nuova immagine docker viene buildata e resa disponibile.

## Visual Studio Code

- Dopo aver aperto il progetto è possibile creare il virtual environment con lo script:
    ```sh
    scripts/create_vscode_venv.sh
    ```

- Clean del progetto
    ```sh
    scripts/clean.sh
    ```
Altri utili script sono presenti nella cartella scripts/.

## Informazioni sui plugins di ricerca

- Le informazioni in merito ai plugins di ricerca sono disponibili nei file [PLUGINS](search/PLUGINS.md) e [QBITTORRENT](search/plugins/QBITTORRENT.md)

