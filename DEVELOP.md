
# Informazioni per gli sviluppatori

## TODO

Attività ancora da portare a termine prima del primo rilascio.

### Implementazioni

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

