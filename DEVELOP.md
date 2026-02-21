
# Informazioni per gli sviluppatori

**Version: Version: 0.0.39**

## TODO

Attività ancora da portare a termine prima del primo rilascio.

### Implementazioni

* Risolvere il problema che la engine_results = await search_service.search(media) ritorna None se c'è un errore 500 a livello basso
* Uniformare la gestione delle eccezioni a partire da async_httpx_session a salire
* Implementare l'auto-disibiltazione di un plug-ins per un tempo configurabile in caso di down del servizio (importante)
* Verificare queste funzioni di Read-Debird get_availability_bulk (serve ancora???) e select_files
* Refactory dei Plug-Ins
  * Valutare se mantenere la compatibilità con i plug-ins d qTorrrentio o rifarli
  * Valutare se implementare un plug-ins unico parametrizzabile con i [file yml di Jacket server](https://github.com/Jackett/Jackett/tree/master/src/Jackett.Common/Definitions)
  * Implementare il supporto 'private'/'public' per i motori di ricerca che hanno la password (da decidere)
* Implementare l'esportazione e l'importazione del database della cache per i container docker (file? contenuto?).
* Mettere un progress se il torrent non è al 100% su debrid (se è possibile?)
* Verificare perché non tiene i risultati della cache per primi
* Implementare il supporto per https://debrid-link.com/
* Implementare il supporto per l'uso concorrente di più debrid (ha senso?)
* Rimuovere **[NON TESTATO]** una volta testati

### Test da completare

- Verificare come mai con --workers $NUM_WORKERS l'auto-update dell'applicazione non funziona
- Testare 'alldebrid', 'premiumize', 'torbox' che sono passati tutti a funzioni asincrone (e non testati)

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

La semantica di versionamento aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

La costante **APPLICATION_VERSION** nel constant.py contiene il numero di versione nel formato **X.Y.Z** (ad esempio 1.2.3).

La sessa cosa vale per la **#VERSION** dei files.

Le versioni rilasciate vengono taggate nel brench *master* nel formato **vX.Y.Z** (ad esempio v1.2.3).

Il rilascio del tag sul *master* è utilizzato per le automazioni di GitHub per la generazione della __release__ e del __package__ (immagine docker).

Lo script [scripts/version.sh](scripts/version.sh) consente di aggiornare il numero di versione in tutti i file.

Il file [CHANGELOG.md] deve essere aggiornato a mano, seguendo le linee guida di [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)


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

