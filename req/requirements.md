---
title: "Requisiti Debriddo (BOZZA)"
description: "Specifiche dei requisiti software (bozza derivata dal codice)"
version: "1.1"
date: "2026-02-13"
author: "Auto-generato da analisi del codice sorgente"
scope:
  paths:
    - "src/**/*.py"
    - "src/**/*.html"
    - "src/**/*.js"
    - "src/**/*.css"
  excludes:
    - ".*/**"
visibility: "draft"
tags: ["markdown", "requirements", "srs", "code-derived"]
---

# Requisiti Debriddo (BOZZA)
**Versione**: 1.1  
**Autore**: Auto-generato da analisi del codice sorgente  
**Data**: 2026-02-13

## Indice
<!-- TOC -->
- [Requisiti Debriddo (BOZZA)](#requisiti-debriddo-bozza)
  - [Indice](#indice)
  - [1. Introduzione](#1-introduzione)
    - [1.1 Regole del documento](#11-regole-del-documento)
    - [1.2 Ambito del progetto](#12-ambito-del-progetto)
  - [2. Requisiti di progetto](#2-requisiti-di-progetto)
    - [2.1 Funzioni di progetto](#21-funzioni-di-progetto)
    - [2.2 Vincoli di progetto](#22-vincoli-di-progetto)
  - [3. Requisiti](#3-requisiti)
    - [3.1 Progettazione e implementazione](#31-progettazione-e-implementazione)
    - [3.2 UI di configurazione e asset statici](#32-ui-di-configurazione-e-asset-statici)
    - [3.3 Manifest (Stremio Add-on)](#33-manifest-stremio-add-on)
    - [3.4 Codifica e decodifica configurazione/query](#34-codifica-e-decodifica-configurazionequery)
    - [3.5 Endpoint stream (pipeline principale)](#35-endpoint-stream-pipeline-principale)
    - [3.6 Ricerca torrent (engine plugins)](#36-ricerca-torrent-engine-plugins)
    - [3.7 Filtraggio e ordinamento](#37-filtraggio-e-ordinamento)
    - [3.8 Conversione, disponibilita e selezione file](#38-conversione-disponibilita-e-selezione-file)
    - [3.9 Cache SQLite](#39-cache-sqlite)
    - [3.10 Formattazione stream Stremio](#310-formattazione-stream-stremio)
    - [3.11 Playback (redirect Debrid)](#311-playback-redirect-debrid)
    - [3.12 Servizi Debrid (implementazioni)](#312-servizi-debrid-implementazioni)
    - [3.13 Script API tester](#313-script-api-tester)
  - [4. Requisiti di test](#4-requisiti-di-test)
  - [5. Storico revisioni](#5-storico-revisioni)
<!-- TOC -->

## 1. Introduzione
<!-- Panoramica della SRS: scopo, ambito, pubblico e organizzazione del documento. Evitare requisiti dettagliati qui. -->

- **DES-501**: Questa sezione deve contenere solo il contesto necessario a interpretare i requisiti e non deve introdurre comportamenti esterni osservabili dettagliati che appartengono alle Sezioni 2 e 3.  
  ID originale: `DES-001`.
  Comportamento atteso: i lettori comprendono struttura, scopo e confini del documento senza dettagli implementativi.  
  Criteri di accettazione: l'Introduzione contiene solo regole del documento e ambito del progetto.  
  Evidenza: `.req/templates/requirements.md` / sezione `## 1. Introduction`. Estratto: `<!-- Overview of the SRS: purpose, scope, audience, and document organization. Avoid detailed requirements here. -->`.

### 1.1 Regole del documento
Queste regole devono essere sempre rispettate:

- **DES-502**: Questo documento deve essere scritto in Italiano.  
  ID originale: `DES-002`.
  Comportamento atteso: titoli di sezione, requisiti, criteri di accettazione e testo esplicativo sono in Italiano.  
  Criteri di accettazione: non sono presenti requisiti formulati in una lingua diversa dall'Italiano (esclusi estratti di codice e stringhe tecniche).  
  Evidenza: `.req/templates/requirements.md` / sezione `### 1.1 Document Rules` richiede una lingua vincolata (in template: Inglese). Estratto: `- This document must be written in English.`.

- **DES-503**: Ogni requisito nelle Sezioni 2, 3 e 4 deve essere formulato come obbligo utilizzando l'equivalente Italiano di “shall/must” (ad esempio “deve”, “non deve”).  
  ID originale: `DES-003`.
  Comportamento atteso: ogni requisito e' espresso come vincolo verificabile, non come intenzione.  
  Criteri di accettazione: ogni enunciato di requisito contiene “deve” o “non deve”.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 1.1 Document Rules`. Estratto: `Format the requirements as a bulleted list, utilizing the keywords 'shall' or 'must'`.

- **DES-504**: Ogni identificativo requisito deve essere univoco all'interno di questo documento.  
  ID originale: `DES-004`.
  Comportamento atteso: non esistono ID duplicati.  
  Criteri di accettazione: nessuna stringa ID (es. `REQ-501`) appare su piu' di un requisito.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 1.1 Document Rules`. Estratto: `Each requirement ID ... must be unique`.

- **DES-505**: Ogni identificativo requisito deve usare uno dei seguenti prefissi di gruppo: `PRJ-`, `CTN-`, `DES-`, `REQ-`, `TST-`.  
  ID originale: `DES-005`.
  Comportamento atteso: gli ID sono raggruppabili automaticamente per prefisso.  
  Criteri di accettazione: ogni ID requisito inizia con uno dei prefissi elencati.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 1.1 Document Rules`. Estratto: `All project function requirements start with **PRJ-** ...`.

- **DES-506**: Ogni requisito in questa bozza deve includere evidenza esplicita composta da: percorso file, simbolo (funzione/classe/variabile) o identificatore di rotta, e un breve estratto.  
  ID originale: `DES-006`.
  Comportamento atteso: ogni requisito e' tracciabile a una posizione di codice o template.  
  Criteri di accettazione: ogni requisito include un campo `Evidenza:` con i componenti richiesti.  
  Evidenza: regola introdotta per vincolo di tracciabilita'. Esempio di evidenza nel codice: `src/debriddo/main.py` contiene decoratori di rotta. Estratto: `@app.get(\"/manifest.json\")`.

- **DES-507**: A ogni modifica di questo documento, i campi `date` e `version` devono essere aggiornati sia nell'header YAML sia nel corpo, e deve essere aggiunta una nuova riga nello Storico revisioni.  
  ID originale: `DES-007`.
  Comportamento atteso: la SRS resta auditabile nel tempo.  
  Criteri di accettazione: ogni edit incrementa `version`, aggiorna `date` in entrambi i punti e aggiunge una riga in Sezione 5.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 1.1 Document Rules`. Estratto: `On every change to this document: - Update the date ... - Increment the version number ... - Append a new row ...`.

### 1.2 Ambito del progetto
<!-- Nome/versione, scopo primario, capacita principali e confini. Breve: cosa e perche, non come. -->

- **DES-508**: Questa sezione deve descrivere lo scopo e i confini del progetto ad alto livello e non deve includere il dettaglio rotta-per-rotta (che deve stare in Sezione 3).  
  ID originale: `DES-008`.
  Comportamento atteso: l'ambito resta sintetico e non procedurale.  
  Criteri di accettazione: nessun dettaglio di endpoint HTTP e' presente in questa sezione.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 1.2 Project Scope`. Estratto: `Keep brief and focus on the \"what\" and \"why\", not the \"how\".`.

## 2. Requisiti di progetto
<!-- Contesto e requisiti di alto livello. Evitare requisiti dettagliati qui. -->

- **DES-509**: Questa sezione deve contenere solo funzioni e vincoli di alto livello che guidano i requisiti dettagliati e non deve duplicare i requisiti funzionali dettagliati della Sezione 3.  
  ID originale: `DES-009`.
  Comportamento atteso: la Sezione 2 resta un livello di sintesi.  
  Criteri di accettazione: i requisiti della Sezione 2 sono espressi a livello di funzionalita/vincolo, non come criteri di accettazione rotta-per-rotta.  
  Evidenza: `.req/templates/requirements.md` / sezione `## 2. Project Requirements`. Estratto: `Background and context that shape the project's requirements. Avoid detailed requirements here.`.

### 2.1 Funzioni di progetto
<!-- Aree funzionali maggiori o funzionalita principali del progetto -->

- **DES-510**: Questa sottosezione deve elencare le principali aree funzionali implementate dal progetto e ogni voce deve essere tracciabile ad almeno un percorso di codice implementato.  
  ID originale: `DES-010`.
  Comportamento atteso: ogni funzione di progetto mappa a moduli e/o rotte.  
  Criteri di accettazione: ogni elemento `PRJ-*` include evidenza in `src/`.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 2.1 Project Functions`. Estratto: `<!-- Major functional areas or features of the project -->`.

- **PRJ-501**: Il sistema deve fornire un add-on compatibile con Stremio che restituisce risultati stream per film e serie combinando ricerca torrent online, cache locale e (opzionalmente) redirect di playback tramite un servizio Debrid.  
  ID originale: `PRJ-001`.
  Comportamento atteso: richieste Stremio alla risorsa `stream` producono un JSON con lista `streams` derivata da ricerca/cache e formattata per Stremio.  
  Criteri di accettazione: una richiesta a `/{config_url}/stream/{stream_type}/{stream_id}` restituisce un oggetto JSON contenente un array `streams` quando l'elaborazione Debrid e' abilitata dalla configurazione.  
  Evidenza: `src/debriddo/main.py` / rotta `@app.get(\"/{config_url}/stream/{stream_type}/{stream_id}\")`. Estratto: `return {\"streams\": stream_list}`.

- **PRJ-502**: Il sistema deve esporre una UI web di configurazione per generare un URL di installazione Stremio e un URL di configurazione che incorporano un payload di configurazione compresso.  
  ID originale: `PRJ-002`.
  Comportamento atteso: un utente puo' aprire `/configure` e generare link `.../C_<payload>/manifest.json` e `.../C_<payload>/configure`.  
  Criteri di accettazione: la UI contiene controlli e una funzione JavaScript che costruisce tali link usando il prefisso `C_`.  
  Evidenza: `src/debriddo/web/config.js` / funzione `getLink()`. Estratto: `let stremio_link = `${window.location.host}/C_${compressed}/manifest.json`;`.

- **PRJ-503**: Il sistema deve servire un manifest di add-on Stremio a `/manifest.json` descrivendo supporto per risorse `stream` per film e serie.  
  ID originale: `PRJ-003`.
  Comportamento atteso: Stremio puo' installare l'add-on usando l'endpoint manifest.  
  Criteri di accettazione: la risposta `/manifest.json` contiene `resources` con una voce `stream` che include `types` con `movie` e `series`.  
  Evidenza: `src/debriddo/main.py` / funzione `get_manifest()`. Estratto: `\"resources\": [{\"name\": \"stream\", \"types\": [\"movie\", \"series\"], ...}]`.

- **PRJ-504**: Il sistema deve cercare candidati torrent usando un set configurabile di plugin di motore di ricerca e restituire risultati elaborabili in magnet.  
  ID originale: `PRJ-004`.
  Comportamento atteso: per i motori configurati, una ricerca produce risultati con titolo, seeds, dimensione e link.  
  Criteri di accettazione: `SearchService.search()` invoca implementazioni plugin selezionate da `config['engines']`.  
  Evidenza: `src/debriddo/search/search_service.py` / `SearchService.__get_indexers()` e `SearchService.__get_engine()`. Estratto: `search_indexers = self.__get_indexer_from_engines(self.__config['engines'])`.

- **PRJ-505**: Il sistema deve poter memorizzare e recuperare risultati di ricerca precedenti usando un file di cache SQLite locale.  
  ID originale: `PRJ-005`.
  Comportamento atteso: gli item in cache sono interrogabili per media id o per titolo/lingua normalizzati e stagione/episodio/anno.  
  Criteri di accettazione: le operazioni di cache leggono/scrivono un file SQLite chiamato `caches_items.db`.  
  Evidenza: `src/debriddo/constants.py` / `CACHE_DATABASE_FILE`. Estratto: `CACHE_DATABASE_FILE = \"caches_items.db\"`.

- **PRJ-506**: Il sistema deve poter filtrare e ordinare i candidati torrent in base a selezione lingua quando configurata, parole chiave escluse, qualita escluse, dimensione massima e limiti per qualita.  
  ID originale: `PRJ-006`.
  Comportamento atteso: un set di candidati e' ridotto e ordinato secondo configurazione.  
  Criteri di accettazione: `filter_items()` applica filtri e `sort_items()` applica l'ordinamento configurato.  
  Evidenza: `src/debriddo/utils/filter_results.py` / funzioni `filter_items()` e `sort_items()`. Estratto: `filters = {\"languages\": LanguageFilter(config), ...}`.

- **PRJ-507**: Il sistema deve poter redirigere richieste di playback a un link del servizio Debrid derivato da un magnet e dai dati di selezione media.  
  ID originale: `PRJ-007`.
  Comportamento atteso: un client puo' invocare `/playback/...` e ricevere un redirect a un link risolto.  
  Criteri di accettazione: l'endpoint playback invoca `get_debrid_service(config)`, poi `debrid_service.get_stream_link(...)` e restituisce `RedirectResponse`.  
  Evidenza: `src/debriddo/main.py` / funzione `get_playback()`. Estratto: `return RedirectResponse(url=link, status_code=status.HTTP_301_MOVED_PERMANENTLY)`.

### 2.2 Vincoli di progetto
<!-- Vincoli di progettazione/implementazione che influenzano la soluzione -->

- **DES-511**: Questa sottosezione deve elencare vincoli dimostrabilmente imposti dall'implementazione corrente (runtime, dipendenze esterne, assunzioni operative).  
  ID originale: `DES-011`.
  Comportamento atteso: i vincoli sono supportati da import, letture di configurazione o endpoint hard-coded.  
  Criteri di accettazione: ogni elemento `CTN-*` include evidenza nel codice.  
  Evidenza: `.req/templates/requirements.md` / sezione `### 2.2 Project Constraints`. Estratto: `<!-- Design and implementation constraints that affect the solution of the project -->`.

- **CTN-501**: Il servizio deve richiedere accesso di rete in uscita verso endpoint HTTP di terze parti per recupero metadati e scraping dei plugin di ricerca torrent.  
  ID originale: `CTN-001`.
  Comportamento atteso: il servizio esegue richieste HTTP a domini esterni durante il normale funzionamento.  
  Criteri di accettazione: il codice contiene URL esterni hard-coded usati da provider metadati e plugin.  
  Evidenza: `src/debriddo/metdata/tmdb.py` / `TMDB.get_metadata()`. Estratto: `https://api.themoviedb.org/3/find/`.

- **CTN-502**: Il servizio deve richiedere accesso di rete in uscita verso API di provider Debrid quando il playback Debrid e' abilitato.  
  ID originale: `CTN-002`.
  Comportamento atteso: la risoluzione playback chiama endpoint API Debrid.  
  Criteri di accettazione: il codice contiene base URL hard-coded e header di autorizzazione.  
  Evidenza: `src/debriddo/debrid/realdebrid.py` / `RealDebrid.__init__()`. Estratto: `self.base_url = \"https://api.real-debrid.com\"`.

- **CTN-503**: Il servizio deve accettare la configurazione principalmente tramite un payload JSON compresso incorporato nel segmento di path URL prefissato con `C_`.  
  ID originale: `CTN-003`.
  Comportamento atteso: le richieste includono un segmento `config_url` decodificabile in un oggetto config JSON.  
  Criteri di accettazione: il backend usa decodifica LZString con tag `C_` e rifiuta tag incompatibili.  
  Evidenza: `src/debriddo/utils/parse_config.py` / funzione `parse_config()`. Estratto: `config = decode_lzstring(encoded_config, \"C_\")`.

- **CTN-504**: Il servizio deve usare un file locale `caches_items.db` nella directory di lavoro corrente per memorizzare elementi in cache quando il caching e' invocato.  
  ID originale: `CTN-004`.
  Comportamento atteso: letture/scritture cache puntano a un file database con path relativo.  
  Criteri di accettazione: il codice cache apre SQLite con `sqlite3.connect(CACHE_DATABASE_FILE)` e `CACHE_DATABASE_FILE` non e' un path assoluto.  
  Evidenza: `src/debriddo/utils/cache.py` / funzione `search_cache()`. Estratto: `connection = sqlite3.connect(CACHE_DATABASE_FILE)`.

- **CTN-505**: La UI di configurazione deve essere eseguita in un browser con JavaScript abilitato per generare link di configurazione.  
  ID originale: `CTN-005`.
  Comportamento atteso: generazione link e codifica configurazione avvengono lato client.  
  Criteri di accettazione: la UI usa `LZString.compressToEncodedURIComponent` e accesso al DOM per costruire URL.  
  Evidenza: `src/debriddo/web/config.js` / `getLink()`. Estratto: `const compressed = LZString.compressToEncodedURIComponent(JSON.stringify(data));`.

## 3. Requisiti
<!-- Requisiti identificabili, verificabili e testabili. Evitare dettagli implementativi non necessari. -->

- **DES-512**: Questa sezione deve contenere requisiti dettagliati, verificabili e testabili derivati dal comportamento implementato, includendo limiti noti dove il codice e' parziale o difettoso.  
  ID originale: `DES-012`.
  Comportamento atteso: i requisiti descrivono lo “stato reale” del codebase.  
  Criteri di accettazione: ogni requisito `DES-*` e `REQ-*` include evidenza concreta; difetti noti sono esplicitati come limiti nei requisiti pertinenti.  
  Evidenza: `src/debriddo/main.py` e moduli dipendenti implementano i comportamenti osservabili (rotte e pipeline).

### 3.1 Progettazione e implementazione
<!-- Vincoli e mandate su design, deployment e manutenzione -->

- **DES-513**: Questa sottosezione deve descrivere vincoli architetturali e di implementazione evidenziati dalla struttura del codebase e dagli import, inclusi confini di modulo e responsabilita componenti.  
  ID originale: `DES-101`.
  Comportamento atteso: l'architettura e' tracciabile a moduli concreti.  
  Criteri di accettazione: ogni elemento `DES-1xx` cita file e simboli in `src/`.  
  Evidenza: `src/debriddo/main.py` / import top-level. Estratto: `from debriddo.search.search_service import SearchService`.

- **DES-514**: Il servizio deve essere implementato come applicazione FastAPI con oggetto `app` e definizioni di rotta co-localizzate in `src/debriddo/main.py`.  
  ID originale: `DES-102`.
  Comportamento atteso: l'esecuzione del modulo espone un'app ASGI con rotte configurate.  
  Criteri di accettazione: `src/debriddo/main.py` definisce `app = FastAPI(...)` e usa decoratori `@app.get(...)`.  
  Evidenza: `src/debriddo/main.py` / simbolo `app`. Estratto: `app = FastAPI(lifespan=lifespan)`.

- **DES-515**: Il servizio deve abilitare impostazioni CORS permissive consentendo tutte le origini, metodi e header.  
  ID originale: `DES-103`.
  Comportamento atteso: richieste browser cross-origin sono consentite.  
  Criteri di accettazione: `CORSMiddleware` e' installato con `allow_origins=[\"*\"]`, `allow_methods=[\"*\"]`, `allow_headers=[\"*\"]`.  
  Evidenza: `src/debriddo/main.py` / `app.add_middleware(CORSMiddleware, ...)`. Estratto: `allow_origins=[\"*\"], ... allow_methods=[\"*\"]`.

- **DES-516**: Quando la variabile d'ambiente `NODE_ENV` e' impostata (non vuota), il servizio deve installare un middleware di logging richieste che logga un path sanitizzato e il body della richiesta HTTP.  
  ID originale: `DES-104`.
  Comportamento atteso: il logging debug maschera segmenti config e query.  
  Criteri di accettazione: il middleware e' aggiunto solo sotto `if development is not None:` e usa sostituzioni regex per `/C_.../` e `/Q_...`.  
  Evidenza: `src/debriddo/main.py` / `LogFilterMiddleware` e `app.add_middleware(LogFilterMiddleware)`. Estratto: `sensible_path = re.sub(r'/C_.*?/', '/<CONFIG>/', path)`.

- **DES-517**: Il servizio deve configurare un `ThreadPoolExecutor` di default dimensionato in base a `N_THREADS` quando valido, altrimenti calcolato da `calculate_optimal_thread_count()` e impostarlo come executor di default dell'event loop asyncio.  
  ID originale: `DES-105`.
  Comportamento atteso: se `N_THREADS` non e' definita o contiene `auto`, il numero di thread e' calcolato con `calculate_optimal_thread_count(os.cpu_count())`; se `N_THREADS` contiene un intero, usa quel valore; se `N_THREADS` e' invalida o il calcolo fallisce, `n_threads` e' impostato a `1` e l'errore e' segnalato in output. `loop.run_in_executor` usa questo executor di default.  
  Criteri di accettazione: il codice legge `N_THREADS`, determina `n_threads` seguendo la logica di fallback, gestisce gli errori di parsing o calcolo con una segnalazione in output, crea `ThreadPoolExecutor(max_workers=n_threads)` e invoca `loop.set_default_executor(executor)`.  
  Evidenza: `src/debriddo/main.py` / simboli `calculate_optimal_thread_count`, `executor`, `loop`, `N_THREADS`. Estratto: `n_threads = ...`, `executor = ThreadPoolExecutor(max_workers=n_threads)`.

- **DES-518**: Il servizio deve pianificare un task periodico `update_app` con intervallo 60 secondi per tutta la durata del lifespan FastAPI.  
  ID originale: `DES-106`.
  Comportamento atteso: allo startup avvia `AsyncIOScheduler` e pianifica `update_app`; allo shutdown lo ferma.  
  Criteri di accettazione: `lifespan` invoca `scheduler.add_job(update_app, 'interval', seconds=60)` e in `finally` esegue `scheduler.shutdown()`.  
  Evidenza: `src/debriddo/main.py` / funzione `lifespan()`. Estratto: `scheduler.add_job(update_app, 'interval', seconds=60)`.

- **DES-519 (Limite noto)**: L'implementazione deve includere un meccanismo di auto-aggiornamento inteso a recuperare i metadati della “latest release” via GitHub Releases API quando `--reload` e' abilitato e `NODE_ENV` non e' impostato.  
  ID originale: `DES-107 (Limite noto)`.
  Comportamento atteso: in tali condizioni il task scheduler tenta di verificare una versione remota e, in caso di mismatch, contiene codice per download zip, estrazione, copia file nella working directory e rimozione artefatti temporanei.  
  Criteri di accettazione: `update_app()` termina immediatamente se `is_reload_enabled` e' falso o se `development` non e' `None`; quando procede, assegna `response = session.request_get(url)` senza `await` e poi tenta `response.json()`.  
  Evidenza: `src/debriddo/main.py` / funzione `update_app()`. Estratto: `response = session.request_get(url)` e `data = response.json()`.

- **DES-520**: L'implementazione del client HTTP deve usare un client HTTPX asincrono con HTTP/2 abilitato e redirect abilitati per interazioni HTTP di plugin e provider.  
  ID originale: `DES-108`.
  Comportamento atteso: richieste plugin/provider possono negoziare HTTP/2 e seguire redirect.  
  Criteri di accettazione: `AsyncThreadSafeSession` costruisce `httpx.AsyncClient(http2=True, ..., follow_redirects=True)`.  
  Evidenza: `src/debriddo/utils/async_httpx_session.py` / `AsyncThreadSafeSession.__init__()`. Estratto: `httpx.AsyncClient(http2=True, cookies=self.cookies, follow_redirects=True)`.

- **DES-521**: L'implementazione deve fornire una classe base di plugin che standardizza le interfacce asincrone `search()` e `download_torrent()` usate dalla pipeline di ricerca.  
  ID originale: `DES-109`.
  Comportamento atteso: ogni plugin motore e' invocabile con un'interfaccia uniforme.  
  Criteri di accettazione: `BasePlugin` definisce `async def search(...)` e `async def download_torrent(...)` (NotImplemented nella base).  
  Evidenza: `src/debriddo/search/plugins/base_plugin.py` / classe `BasePlugin`. Estratto: `async def search(self, what, cat='all')`.

- **DES-522**: L'implementazione deve rappresentare il media come oggetti `Movie` o `Series` derivati da `Media` e deve usare la proprieta `type` per guidare decisioni downstream di ricerca ed elaborazione.  
  ID originale: `DES-110`.
  Comportamento atteso: la pipeline differenzia film vs serie in ricerca e selezione file torrent.  
  Criteri di accettazione: `Movie` invoca `super(..., \"movie\")` e `Series` invoca `super(..., \"series\")`; il codice branch-a su `isinstance(media, Movie)` e `isinstance(media, Series)`.  
  Evidenza: `src/debriddo/models/movie.py` / classe `Movie`. Estratto: `super().__init__(id, titles, languages, \"movie\")`.

- **DES-523**: L'implementazione deve rappresentare candidati torrent come oggetti `SearchResult` convertibili in `TorrentItem` per elaborazione successiva e formattazione stream.  
  ID originale: `DES-111`.
  Comportamento atteso: i risultati ricerca sono un modello transitorio; i torrent item sono il modello di processing.  
  Criteri di accettazione: `SearchResult.convert_to_torrent_item()` restituisce un `TorrentItem` costruito dai campi `SearchResult`.  
  Evidenza: `src/debriddo/search/search_result.py` / metodo `convert_to_torrent_item()`. Estratto: `return TorrentItem(self.raw_title, self.title, self.size, ...)`.

- **DES-524**: Il progetto deve usare le seguenti directory e file principali (vista limitata in profondita) come superficie di codice implementato e runtime.  
  ID originale: `DES-112`.
  Comportamento atteso: la struttura documentata e' presente nel repository.  
  Criteri di accettazione: i path elencati esistono.  
  Evidenza: path implementati esistono sotto `src/debriddo/` e `req/`. Estratto (path modulo): `src/debriddo/main.py`.  
  Struttura file/cartelle (profondita max 3; `src/` profondita max 4; esclusi `.git/`, `.venv/`, `node_modules/`, `dist/`, `build/`, `target/`):
  ```text
  .
  ├─ req/
  │  ├─ requirements.md
  │  └─ requirements_DRAFT.md
  ├─ src/
  │  └─ debriddo/
  │     ├─ constants.py
  │     ├─ main.py
  │     ├─ models/
  │     │  ├─ media.py
  │     │  ├─ movie.py
  │     │  └─ series.py
  │     ├─ metdata/
  │     │  ├─ cinemeta.py
  │     │  ├─ metadata_provider_base.py
  │     │  └─ tmdb.py
  │     ├─ debrid/
  │     │  ├─ base_debrid.py
  │     │  ├─ get_debrid_service.py
  │     │  ├─ realdebrid.py
  │     │  ├─ alldebrid.py
  │     │  ├─ premiumize.py
  │     │  └─ torbox.py
  │     ├─ search/
  │     │  ├─ search_indexer.py
  │     │  ├─ search_result.py
  │     │  ├─ search_service.py
  │     │  └─ plugins/
  │     ├─ torrent/
  │     │  ├─ torrent_item.py
  │     │  ├─ torrent_service.py
  │     │  └─ torrent_smart_container.py
  │     ├─ utils/
  │     │  ├─ async_httpx_session.py
  │     │  ├─ cache.py
  │     │  ├─ filter_results.py
  │     │  ├─ parse_config.py
  │     │  ├─ string_encoding.py
  │     │  └─ filter/
  │     └─ web/
  │        ├─ index.html
  │        ├─ config.js
  │        ├─ styles.css
  │        └─ images/
  └─ requirements.txt
  ```

- **DES-525**: In questo codebase sono identificate ottimizzazioni di prestazioni esplicite, e questo documento non deve dichiarare “Nessuna ottimizzazione di prestazioni esplicita identificata”.  
  ID originale: `DES-113`.
  Comportamento atteso: la SRS riflette concorrenza e configurazione client HTTP implementate per throughput/latenza.  
  Criteri di accettazione: la SRS cita evidenza di dimensionamento thread pool, esecuzione multi-thread nel search service e uso HTTP/2.  
  Evidenza: `src/debriddo/main.py` / `calculate_optimal_thread_count()`. Estratto: `optimal_num_threads = (cpu_cores * 2) + 1`; `src/debriddo/constants.py` / `RUN_IN_MULTI_THREAD`. Estratto: `RUN_IN_MULTI_THREAD = True`; `src/debriddo/utils/async_httpx_session.py` / HTTP/2. Estratto: `httpx.AsyncClient(http2=True, ...)`.

- **DES-526**: La SRS deve elencare componenti e librerie di terze parti solo quando evidenziati da un manifest dipendenze o import diretti e non deve dedurre dipendenze non dichiarate.  
  ID originale: `DES-116`.
  Comportamento atteso: la lista dipendenze e' tracciabile.  
  Criteri di accettazione: ogni dipendenza elencata ha evidenza in `requirements.txt` e/o `import` espliciti.  
  Evidenza: `requirements.txt` elenca dipendenze e `src/debriddo/main.py` importa moduli principali. Estratto (manifest): `fastapi`; estratto (import): `from fastapi import FastAPI, Request, HTTPException`.  
  Componenti e librerie con evidenza:
  ```text
  fastapi, starlette, uvicorn, APScheduler, python-dotenv, httpx[http2], PySocks, Unidecode, beautifulsoup4/bs4,
  bencode.py (importata come bencode), rank-torrent-name (importata come RTN), lzstring
  ```

- **DES-527**: L'applicazione deve caricare variabili d'ambiente da un file `.env` all'avvio tramite `load_dotenv()`.  
  ID originale: `DES-901`.
  Comportamento atteso: variabili come `NODE_URL` e `NODE_ENV` possono essere fornite via `.env`.  
  Criteri di accettazione: `main.py` invoca `load_dotenv()` prima di leggere variabili d'ambiente.  
  Evidenza: `src/debriddo/main.py` / `load_dotenv()`. Estratto: `load_dotenv()`.

- **DES-528**: Se la variabile d'ambiente `NODE_URL` e' una stringa non vuota, il servizio deve usarla come base URL (`app_website`) per i campi dei manifest (`/site.webmanifest` e `/manifest.json`); altrimenti deve usare il default `http://127.0.0.1:8000`.  
  ID originale: `DES-902`.
  Comportamento atteso: `start_url`, `icons.src`, `background` e `logo` nei manifest sono derivati da `app_website`.  
  Criteri di accettazione: `main.py` imposta `node_url = os.getenv(\"NODE_URL\", \"http://127.0.0.1:8000\")` e poi assegna `app_website` in base alla non-vuotezza; i handler manifest usano `app_website` in `start_url` e negli URL di `icons`.  
  Evidenza: `src/debriddo/main.py` / simboli `node_url`, `app_website`, handler `/site.webmanifest` e `get_manifest()`. Estratto: `node_url = os.getenv(\"NODE_URL\", \"http://127.0.0.1:8000\")` e `\"start_url\": app_website`.

- **DES-529**: Quando eseguito come script principale, il modulo deve avviare Uvicorn su `127.0.0.1:8000` con `reload=True` e app target `debriddo.main:app`.  
  ID originale: `DES-903`.
  Comportamento atteso: l'esecuzione `python src/debriddo/main.py` avvia un server di sviluppo locale.  
  Criteri di accettazione: esiste il branch `if __name__ == \"__main__\":` che invoca `uvicorn.run(\"debriddo.main:app\", host=\"127.0.0.1\", port=8000, reload=True)`.  
  Evidenza: `src/debriddo/main.py` / blocco `__main__`. Estratto: `uvicorn.run(\"debriddo.main:app\", host=\"127.0.0.1\", port=8000, reload=True)`.

- **DES-530 (Limite noto)**: Il componente `AsyncThreadSafeSession` deve accettare un parametro opzionale `proxy` nel formato `user:pass@host:port` o `host:port`, ma tale capacita non deve essere considerata configurabile tramite l'interfaccia HTTP dell'applicazione poiche' non viene passata da alcun percorso runtime implementato.  
  ID originale: `DES-904 (Limite noto)`.
  Comportamento atteso: se `proxy` e' passato al costruttore, viene configurato un proxy SOCKS5 tramite monkey-patch di `socket.socket`; altrimenti nessun proxy e' configurato.  
  Criteri di accettazione: `AsyncThreadSafeSession.__init__(proxy=None)` invoca `_setup_proxy(proxy)` solo se `proxy` e' truthy e `_setup_proxy` valida il formato; nessuna chiamata in `src/debriddo/` passa un argomento `proxy` al costruttore.  
  Evidenza: `src/debriddo/utils/async_httpx_session.py` / `__init__`, `_setup_proxy`. Estratto: `def __init__(self, proxy=None):` e `if proxy: self._setup_proxy(proxy)`.

### 3.2 UI di configurazione e asset statici
<!-- Comportamenti osservabili via UI web (HTML/JS/CSS) e risorse statiche -->

- **DES-531**: Questa sottosezione deve definire comportamenti osservabili esternamente come endpoint HTTP e relativo comportamento request/response, includendo pipeline funzionali che impattano output osservabili.  
  ID originale: `DES-114`.
  Comportamento atteso: ogni requisito `REQ-*` e' legato a un'interfaccia visibile all'utente (risposte HTTP, link generati, item `streams`).  
  Criteri di accettazione: ogni `REQ-*` include un path/rotta o riferimento schema output.  
  Evidenza: `src/debriddo/main.py` definisce rotte HTTP e restituisce JSON/HTML/redirect.

- **REQ-501**: Il servizio deve redirigere il path root `/` verso `/configure`.  
  ID originale: `REQ-001`.
  Comportamento atteso: una richiesta a `/` riceve un redirect a `/configure`.  
  Criteri di accettazione: l'handler root restituisce `RedirectResponse` con `url=\"/configure\"`.  
  Evidenza: `src/debriddo/main.py` / funzione `root()`. Estratto: `return RedirectResponse(url=\"/configure\")`.

- **REQ-502**: Il servizio deve servire l'HTML della UI di configurazione su `GET /configure` e `GET /{config}/configure`.  
  ID originale: `REQ-002`.
  Comportamento atteso: la response body deriva da `web/index.html` con sostituzione placeholder.  
  Criteri di accettazione: l'handler invoca `get_index(app_name, app_version, app_environment)`.  
  Evidenza: `src/debriddo/main.py` / funzione `configure()` (rotta `/configure`). Estratto: `return get_index(app_name, app_version, app_environment)`.

- **REQ-503**: Il renderer UI di configurazione deve sostituire i placeholder `$APP_NAME`, `$APP_VERSION` e `$APP_ENVIRONMENT` presenti in `index.html`.  
  ID originale: `REQ-003`.
  Comportamento atteso: l'HTML restituito contiene nome/versione/ambiente configurati anziche' placeholder.  
  Criteri di accettazione: `get_index()` esegue `replace` sui tre placeholder.  
  Evidenza: `src/debriddo/web/pages.py` / funzione `get_index()`. Estratto: `index = index.replace( \"$APP_NAME\", app_name )`.

- **REQ-504**: Il servizio deve servire risorse statiche della UI di configurazione sui path `/config.js`, `/lz-string.min.js`, `/styles.css`, `/images/{file_path}` e deve servire le stesse risorse anche sotto `/{config}/...`.  
  ID originale: `REQ-004`.
  Comportamento atteso: asset JS/CSS/immagini sono recuperabili con o senza prefisso config.  
  Criteri di accettazione: ogni risorsa ha sia rotta root sia rotta `/{config}/` che restituisce `FileResponse` da `WEB_DIR`.  
  Evidenza: `src/debriddo/main.py` / decoratori rotta file statici. Estratto: `@app.get(\"/{config}/styles.css\")`.

- **REQ-505**: Il servizio deve servire un manifest web app JSON su `GET /site.webmanifest` con Content-Type `application/manifest+json`.  
  ID originale: `REQ-005`.
  Comportamento atteso: i browser possono recuperare metadati manifest (PWA-style).  
  Criteri di accettazione: l'handler restituisce `JSONResponse(..., media_type=\"application/manifest+json\")`.  
  Evidenza: `src/debriddo/main.py` / rotta `/site.webmanifest`. Estratto: `media_type=\"application/manifest+json\"`.

- **REQ-506**: Il servizio deve servire un file favicon su `GET /favicon.ico` come `FileResponse` da `WEB_DIR/images/favicon.ico`.  
  ID originale: `REQ-901`.
  Comportamento atteso: i client possono recuperare la favicon del sito.  
  Criteri di accettazione: `main.py` definisce una rotta `/favicon.ico` che restituisce `FileResponse(str(WEB_DIR / \"images\" / \"favicon.ico\"))`.  
  Evidenza: `src/debriddo/main.py` / funzione `get_favicon()` (rotta `/favicon.ico`). Estratto: `response = FileResponse(str(WEB_DIR / \"images\" / \"favicon.ico\"))`.

- **REQ-507**: La UI di configurazione deve includere campi di input per chiave API Debrid, chiave API TMDB, impostazioni cache, selezione engine, selezione lingue, ordinamento e selezioni di filtro, e deve mappare tali input in chiavi JSON usate dalla pipeline backend.  
  ID originale: `REQ-036`.
  Comportamento atteso: la configurazione generata contiene le chiavi attese dal backend.  
  Criteri di accettazione: `config.js` costruisce un oggetto `data` includendo `debridKey`, `tmdbApi`, `cache`, `search`, `engines`, `languages`, `sort`, `maxResults`, `minCacheResults`, `daysCacheValid`.  
  Evidenza: `src/debriddo/web/config.js` / costruzione `data` in `getLink()`. Estratto: `let data = { addonHost, service, 'debridKey': debridApi, ... tmdbApi, cache, playtorrent, search, debrid, metadataProvider };`.

- **REQ-508**: La UI di configurazione deve definire un array `engines` senza elementi `undefined` e deve includere solo gli engine abilitati (escludendo `one337x` e `limetorrents` quando disabilitati).  
  ID originale: `REQ-037`.
  Comportamento atteso: l'iterazione sugli engine non genera elementi `undefined` e riflette le scelte di abilitazione UI.  
  Criteri di accettazione: il literal `engines` non contiene virgole consecutive e `selectedEngines` contiene solo engine presenti nel DOM.  
  Evidenza: `src/debriddo/web/config.js` / dichiarazione `engines` e `getLink()`. Estratto: `const engines = ['thepiratebay', 'torrentproject', 'torrentz', 'torrentgalaxy', 'therarbg', 'ilcorsaronero', 'ilcorsaroblu'];`.

- **REQ-509**: La UI di configurazione deve validare la selezione di almeno una lingua verificando la lista effettiva `selectedLanguages` e bloccare la generazione dei link quando la lista e' vuota.  
  ID originale: `REQ-038`.
  Comportamento atteso: la UI impedisce la generazione quando nessuna lingua e' selezionata.  
  Criteri di accettazione: la condizione usa `selectedLanguages.length === 0` all'interno di `getLink()` e mostra l'alert di campi obbligatori.  
  Evidenza: `src/debriddo/web/config.js` / check required-field in `getLink()`. Estratto: `... || selectedLanguages.length === 0) { alert('Please fill all required fields'); ... }`.

- **REQ-510 (Limite noto)**: La UI di configurazione deve consentire la selezione del valore `service=debridlink`, ma il backend deve rifiutare tale valore come configurazione servizio non valida.  
  ID originale: `REQ-039 (Limite noto)`.
  Comportamento atteso: una config generata con `service=\"debridlink\"` fallisce lato server.  
  Criteri di accettazione: `index.html` include un input radio `service` con `value=\"debridlink\"`, mentre `get_debrid_service()` non gestisce `debridlink` e solleva HTTP 500 per valori non supportati.  
  Evidenza: `src/debriddo/web/index.html` / input `value=\"debridlink\"`. Estratto: `<input id=\"debridlink\" name=\"service\" value=\"debridlink\" type=\"radio\">`; `src/debriddo/debrid/get_debrid_service.py` / `get_debrid_service()`. Estratto: `raise HTTPException(status_code=500, detail=\"Invalid service configuration.\")`.

### 3.3 Manifest (Stremio Add-on)

- **REQ-511**: Il servizio deve servire un add-on manifest JSON su `GET /manifest.json` e `GET /{params}/manifest.json` con Content-Type `application/manifest+json`.  
  ID originale: `REQ-006`.
  Comportamento atteso: Stremio puo' installare l'add-on da entrambi i path.  
  Criteri di accettazione: l'handler restituisce `JSONResponse` con `media_type=\"application/manifest+json\"` e include una voce `resources` per `stream` con supporto `movie` e `series`.  
  Evidenza: `src/debriddo/main.py` / funzione `get_manifest()`. Estratto: `\"name\": \"stream\", \"types\": [\"movie\", \"series\"]`.

- **REQ-512 (Limite noto)**: Il manifest JSON deve dichiarare una risorsa `meta` per tipo `other` con `idPrefixes` includendo `realdebrid`, ma il backend non deve implementare una rotta HTTP per servire tale risorsa `meta`.  
  ID originale: `REQ-043 (Limite noto)`.
  Comportamento atteso: client che richiedono `meta` possono ricevere 404.  
  Criteri di accettazione: il manifest include un elemento `resources` con `\"name\": \"meta\"` e `src/debriddo/main.py` non definisce rotte che iniziano con `/meta`.  
  Evidenza: `src/debriddo/main.py` / `resources` nel manifest. Estratto: `{\"name\": \"meta\", \"types\": [\"other\"], \"idPrefixes\": [\"realdebrid\"]}`; `src/debriddo/main.py` / rotte definite includono stream e playback ma non meta. Estratto: `@app.get(\"/{config_url}/stream/{stream_type}/{stream_id}\")`.

### 3.4 Codifica e decodifica configurazione/query

- **REQ-513**: La UI di configurazione deve generare un payload di configurazione serializzando un oggetto JSON e comprimendolo con LZString `compressToEncodedURIComponent`, e deve prefissare il payload con `C_` quando costruisce URL.  
  ID originale: `REQ-007`.
  Comportamento atteso: la configurazione e' URL-safe e decodificabile dal backend.  
  Criteri di accettazione: `config.js` genera `C_<compressed>` e lo usa negli URL di manifest e configure.  
  Evidenza: `src/debriddo/web/config.js` / `getLink()`. Estratto: `let config_link = `${window.location.host}/C_${compressed}/configure`;`.

- **REQ-514**: Il backend deve decodificare un segmento path `config_url` applicando semantica LZString `decompressFromEncodedURIComponent` alla sottostringa dopo il prefisso `C_` e fare parsing JSON.  
  ID originale: `REQ-008`.
  Comportamento atteso: la configurazione decodificata e' un dizionario Python.  
  Criteri di accettazione: `parse_config()` invoca `decode_lzstring(encoded_config, \"C_\")` e restituisce il valore JSON.  
  Evidenza: `src/debriddo/utils/parse_config.py` / `parse_config()`. Estratto: `config = decode_lzstring(encoded_config, \"C_\")`.

- **REQ-515**: Quando genera URL di playback per stream Debrid, il backend deve codificare la query playback come valore JSON compresso con LZString e prefissato con `Q_`.  
  ID originale: `REQ-009`.
  Comportamento atteso: URL di playback contengono `Q_<payload>` decodificabile lato server.  
  Criteri di accettazione: `encode_query()` restituisce `encode_lzstring(query, \"Q_\")` e la formattazione stream lo usa.  
  Evidenza: `src/debriddo/utils/parse_config.py` / `encode_query()` e `src/debriddo/utils/stremio_parser.py` / `parse_to_debrid_stream()`. Estratto: `query_encoded = encode_query(torrent_item.to_debrid_stream_query(media))`.

- **REQ-516**: Il backend deve decodificare il segmento path `query_string` per playback usando lo stesso meccanismo LZString e il prefisso `Q_`.  
  ID originale: `REQ-010`.
  Comportamento atteso: la query decodificata e' un dizionario Python contenente campi playback.  
  Criteri di accettazione: `parse_query()` invoca `decode_lzstring(encoded_query, \"Q_\")`.  
  Evidenza: `src/debriddo/utils/parse_config.py` / `parse_query()`. Estratto: `query = decode_lzstring(encoded_query, \"Q_\")`.

- **REQ-517**: L'handler endpoint stream `GET /{config_url}/stream/{stream_type}/{stream_id}` deve normalizzare `stream_id` rimuovendo un suffisso `.json` finale se presente.  
  ID originale: `REQ-011`.
  Comportamento atteso: ID in stile Stremio con `.json` sono accettati.  
  Criteri di accettazione: l'handler esegue `stream_id = stream_id.replace(\".json\", \"\")` prima del recupero metadati.  
  Evidenza: `src/debriddo/main.py` / funzione `get_results()`. Estratto: `stream_id = stream_id.replace(\".json\", \"\")`.

### 3.5 Endpoint stream (pipeline principale)

- **REQ-518**: L'handler endpoint stream deve selezionare il provider metadati come segue: usare TMDB quando `config['metadataProvider'] == \"tmdb\"` e `config['tmdbApi']` e' truthy; altrimenti usare Cinemeta.  
  ID originale: `REQ-012`.
  Comportamento atteso: lookup metadati dipende dal provider.  
  Criteri di accettazione: l'handler sceglie `TMDB(config)` solo in quelle condizioni; altrimenti `Cinemeta(config)`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `if config['metadataProvider'] == \"tmdb\" and config['tmdbApi']: metadata_provider = TMDB(config)`.

- **REQ-519**: Il provider metadati Cinemeta deve recuperare metadati da `https://v3-cinemeta.strem.io/meta/{type}/{id}.json` e deve assegnare sempre `languages=[\"en\"]` al media risultante.  
  ID originale: `REQ-013`.
  Comportamento atteso: Cinemeta produce una lista lingue solo Inglese indipendentemente dalla configurazione.  
  Criteri di accettazione: `Cinemeta.get_metadata()` imposta `languages=[\"en\"]` sia per film sia per serie.  
  Evidenza: `src/debriddo/metdata/cinemeta.py` / `Cinemeta.get_metadata()`. Estratto: `languages=[\"en\"]`.

- **REQ-520**: Il provider metadati TMDB deve eseguire una richiesta esterna per ogni lingua configurata e deve assemblare un media i cui `titles` includono un titolo per lingua richiesta, mentre `languages` e' impostato alla lista lingue configurata (default `["en"]` quando la lista e' vuota o mancante).  
  ID originale: `REQ-014`.
  Comportamento atteso: i titoli sono varianti per lingua.  
  Criteri di accettazione: `TMDB.get_metadata()` usa una lista lingue effettiva con fallback a `["en"]` quando `config['languages']` e' vuota o mancante, imposta `result.languages` alla lista effettiva e aggiunge titoli per le lingue successive.  
  Evidenza: `src/debriddo/metdata/tmdb.py` / `TMDB.get_metadata()`. Estratto: `languages = self.config.get("languages") or ["en"]`; `result.languages = languages`.

- **REQ-521**: L'handler endpoint stream deve istanziare un servizio Debrid in base a `config['service']` e deve rifiutare valori non supportati restituendo un errore HTTP 500.  
  ID originale: `REQ-015`.
  Comportamento atteso: solo servizi supportati sono accettati.  
  Criteri di accettazione: `get_debrid_service()` supporta `realdebrid`, `alldebrid`, `premiumize`, `torbox`; altrimenti solleva `HTTPException(status_code=500, ...)`.  
  Evidenza: `src/debriddo/debrid/get_debrid_service.py` / `get_debrid_service()`. Estratto: `else: raise HTTPException(status_code=500, detail=\"Invalid service configuration.\")`.

- **REQ-522**: Se `config['cache']` e' true, l'handler endpoint stream deve tentare di caricare risultati cached per il media richiesto e poi filtrarli usando la stessa pipeline di filtraggio usata per risultati engine.  
  ID originale: `REQ-016`.
  Comportamento atteso: risultati cache possono soddisfare richieste stream senza scraping engine.  
  Criteri di accettazione: l'handler invoca `search_cache(config, media)` e, se esistono risultati, li converte con `SearchResult().from_cached_item(...)` e invoca `filter_items(...)`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `cached_results = [SearchResult().from_cached_item(torrent) for torrent in cached_results]`.

- **REQ-523**: Se `config['search']` e' true e il numero di risultati derivati da cache e' inferiore a `int(config['minCacheResults'])`, l'handler endpoint stream deve eseguire ricerca online usando i plugin engine configurati e deve filtrare tali risultati prima di combinarli con quelli cached.  
  ID originale: `REQ-017`.
  Comportamento atteso: la ricerca engine integra risultati cache insufficienti.  
  Criteri di accettazione: l'handler verifica `config['search'] and len(search_results) < int(config['minCacheResults'])`, invoca `SearchService(config).search(media)` e `filter_items(engine_results, ...)`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `if config['search'] and len(search_results) < int(config['minCacheResults']):`.

- **REQ-524**: L'endpoint stream deve restituire un oggetto JSON della forma `{\"streams\": <lista>}` solo quando `config['debrid']` e' truthy; altrimenti l'handler non deve restituire un body esplicito (comportamento FastAPI per `None`).  
  ID originale: `REQ-031`.
  Comportamento atteso: quando Debrid e' disabilitato, l'endpoint stream non produce `streams`.  
  Criteri di accettazione: l'unico `return` in `get_results()` e' dentro `if config['debrid']:`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `if config['debrid']:` seguito da `return {\"streams\": stream_list}`.

- **REQ-525**: Quando `config['service'] == \"torbox\"` e `config['debrid']` e' true, l'endpoint stream deve tentare di aggiornare la disponibilita dei torrent chiamando `debrid_service.get_availability_bulk(hashes, ip)` e aggiornando il container con l'oggetto risultante.  
  ID originale: `REQ-032`.
  Comportamento atteso: l'handler esegue un passo availability-update prima di selezionare best match e formattare stream.  
  Criteri di accettazione: il codice verifica `if config['service'] == \"torbox\":`, assegna `result = debrid_service.get_availability_bulk(hashes, ip)`, e invoca `torrent_smart_container.update_availability(result, type(debrid_service), media)`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `torrent_smart_container.update_availability(result, type(debrid_service), media)`.

### 3.6 Ricerca torrent (engine plugins)

- **REQ-526**: La pipeline di ricerca torrent deve supportare i seguenti identificatori engine, ciascuno mappato a una classe plugin concreta: `thepiratebay`, `one337x`, `limetorrents`, `torrentproject`, `torrentz`, `torrentgalaxy`, `therarbg`, `ilcorsaronero`, `ilcorsaroblu`.  
  ID originale: `REQ-018`.
  Comportamento atteso: stringhe engine selezionano implementazioni plugin.  
  Criteri di accettazione: `SearchService.__get_engine()` contiene branch espliciti per ogni stringa elencata.  
  Evidenza: `src/debriddo/search/search_service.py` / `__get_engine()`. Estratto: `elif engine_name == 'torrentgalaxy': return torrentgalaxy(self.__config)`.

- **REQ-527**: La pipeline di ricerca deve scartare risultati engine il cui campo `seeds` convertito in intero e' minore o uguale a zero.  
  ID originale: `REQ-019`.
  Comportamento atteso: torrent senza seeders sono esclusi.  
  Criteri di accettazione: `__get_torrents_from_list_of_dicts()` esegue `if int(result.seeders) <= 0: continue`.  
  Evidenza: `src/debriddo/search/search_service.py` / `__get_torrents_from_list_of_dicts()`. Estratto: `if int(result.seeders) <= 0: continue`.

- **REQ-528**: Per ogni risultato di ricerca, la pipeline deve garantire che un URL magnet sia disponibile usando un link `magnet:?` esistente oppure invocando `download_torrent()` del plugin e richiedendo che restituisca un magnet link.  
  ID originale: `REQ-020`.
  Comportamento atteso: l'elaborazione downstream riceve sempre un magnet link.  
  Criteri di accettazione: `__post_process_result()` imposta `result.magnet = result.link` per link magnet; altrimenti invoca `indexer.engine.download_torrent(result.link)` e imposta `result.magnet` solo se il risultato inizia con `magnet:?`.  
  Evidenza: `src/debriddo/search/search_service.py` / `__post_process_result()`. Estratto: `res_link = await indexer.engine.download_torrent(result.link)`.

- **REQ-529**: La pipeline di ricerca deve fare parsing del titolo torrent raw per popolare `parsed_data` e deve rilevare lingue torrent dal titolo raw usando detection basata su regex.  
  ID originale: `REQ-021`.
  Comportamento atteso: ogni risultato ha `parsed_data` e una lista `languages` non vuota.  
  Criteri di accettazione: `__post_process_result()` invoca `parse(result.raw_title)` e `detect_languages(result.raw_title)`; quando nessun pattern match-a, `detect_languages` restituisce `[\"en\"]`.  
  Evidenza: `src/debriddo/search/search_service.py` / `__post_process_result()`. Estratto: `result.languages = detect_languages(result.raw_title)`.

- **REQ-530**: La ricerca torrent deve eseguire le chiamate ai motori (engine) in modalita multi-thread quando `RUN_IN_MULTI_THREAD` e' true, eseguendo ciascuna coroutine in un event loop dedicato su thread di executor.  
  ID originale: `REQ-902`.
  Comportamento atteso: `SearchService.search()` usa `loop.run_in_executor(None, run_coroutine_in_thread, <coroutine>)` per ogni indexer quando `MULTI_THREAD` e' attivo.  
  Criteri di accettazione: `MULTI_THREAD` e' impostato da `RUN_IN_MULTI_THREAD`; `SearchService.search()` costruisce una lista `tasks = [loop.run_in_executor(None, run_coroutine_in_thread, ...)]` e attende con `asyncio.gather`.  
  Evidenza: `src/debriddo/constants.py` / `RUN_IN_MULTI_THREAD = True`; `src/debriddo/utils/multi_thread.py` / `run_coroutine_in_thread`; `src/debriddo/search/search_service.py` / `search()` ramo `if MULTI_THREAD:`. Estratto: `tasks = [loop.run_in_executor(None, run_coroutine_in_thread, self.__search_movie_indexer(...)) ...]`.

- **REQ-571**: La pipeline di ricerca deve costruire le stringhe di ricerca per film usando titolo, anno e tag lingua iterando le lingue richieste da `self.__config['languages']` (non da `movie.languages`), con fallback controllato da `SEARCHE_FALL_BACK`.  
  ID originale: `N/A`.
  Comportamento atteso: la ricerca primaria deve essere sempre eseguita anche quando `SEARCHE_FALL_BACK` e' false. Se `self.__config['languages']` e' vuoto o mancante, deve essere eseguita una sola ricerca primaria senza `lang_tag` (`<title> <year>`). Se `self.__config['languages']` contiene lingue, per ogni lingua richiesta la query primaria e' `<title> <year> <lang_tag>` salvo il caso in cui la lingua dell'indexer sia diversa da `en` e uguale alla lingua richiesta, dove la query deve essere `<title> <year>` (senza tag). In tutti gli altri casi il tag deve essere ottenuto da `self.__language_tags[lang]` (se presente). Se `SEARCHE_FALL_BACK` e' true e nessuna ricerca primaria produce risultati, deve essere eseguita una ricerca fallback con `<title> <lang_tag>` oppure `<title>` con le stesse regole di composizione del tag.  
  Criteri di accettazione: `__search_movie_indexer()` legge le lingue da `self.__config['languages']`, non usa `movie.languages` per il ciclo lingue, costruisce `lang_tag` vuoto quando non ci sono lingue richieste o quando `indexer.language != 'en' and indexer.language == lang`, esegue sempre le query primarie `<title> <year>[ <lang_tag>]`, esegue le query fallback `<title>[ <lang_tag>]` solo se `SEARCHE_FALL_BACK` e' true e l'insieme risultati primari e' vuoto, e concatena i risultati in ordine di esecuzione.  
  Evidenza: `src/debriddo/search/search_service.py` / `__search_movie_indexer()`.

- **REQ-572**: La pipeline di ricerca deve eseguire una ricerca primaria multipla per serie TV concatenando i risultati di episodio specifico, pack multi-episodi e stagione specifica, iterando le lingue richieste da `self.__config['languages']` (non da `series.languages`), con fallback controllato da `SEARCHE_FALL_BACK`.  
  ID originale: `N/A`.
  Comportamento atteso: la ricerca primaria deve essere sempre eseguita anche quando `SEARCHE_FALL_BACK` e' false. Se `self.__config['languages']` e' vuoto o mancante, deve essere eseguito un solo ciclo primario senza `lang_tag` con tre query concatenate: a) `<title> <season><episode>`, b) `<title> <season>E01-E`, c) `<title> "<SeasonLocalized>" <season_number>` dove `<SeasonLocalized>` usa la localizzazione della lingua corrente quando presente (es. `Stagione` per `it`) altrimenti `Season`. Se `self.__config['languages']` contiene lingue, per ogni lingua richiesta le stesse tre query usano `<lang_tag>` salvo il caso in cui la lingua dell'indexer sia diversa da `en` e uguale alla lingua richiesta, dove il tag deve essere omesso. In tutti gli altri casi il tag deve essere ottenuto da `self.__language_tags[lang]` (se presente). Se `SEARCHE_FALL_BACK` e' true e nessuna query primaria produce risultati, deve essere eseguita una ricerca fallback con `<title> <lang_tag>` oppure `<title>` con le stesse regole di composizione del tag.  
  Criteri di accettazione: `__search_series_indexer()` legge le lingue da `self.__config['languages']`, non usa `series.languages` per il ciclo lingue, genera per ogni lingua (o una sola volta se lista vuota) le tre query primarie episodio/pack/stagione (`<season>E01-E` incluso), localizza la stringa `Season` in base alla lingua del ciclo, costruisce `lang_tag` vuoto quando non ci sono lingue richieste o quando `indexer.language != 'en' and indexer.language == lang`, concatena i risultati delle tre query primarie, ed esegue fallback `<title>[ <lang_tag>]` solo se `SEARCHE_FALL_BACK` e' true e il totale risultati primari e' zero.  
  Evidenza: `src/debriddo/search/search_service.py` / `__search_series_indexer()`.

### 3.7 Filtraggio e ordinamento

- **REQ-531**: La pipeline di filtraggio deve applicare i seguenti filtri nell'ordine dichiarato quando abilitati da configurazione: filtro lingua (solo se `config['languages']` e' valorizzato), filtro dimensione massima (solo film), esclusione parole chiave titolo, esclusione qualita, risultati-per-qualita.  
  ID originale: `REQ-022`.
  Comportamento atteso: i filtri si compongono deterministicamente.  
  Criteri di accettazione: `filter_items()` costruisce il dict `filters` in tale ordine e applica ogni filtro in ordine di iterazione; quando `config['languages']` e' vuoto o mancante, il filtro `LanguageFilter` non viene applicato.  
  Evidenza: `src/debriddo/utils/filter_results.py` / `filter_items()`. Estratto: `filters = {\"languages\": LanguageFilter(config), \"maxSize\": MaxSizeFilter(config, media.type), ...}`.

- **REQ-532**: Per media di tipo serie, la pipeline di filtraggio deve mantenere un item quando almeno una delle seguenti logiche e' vera (OR logico): a) match episodio con accoppiata stagione/episodio nelle forme `SnnEmm`, `Snn Emm`, `Snn-Emm`; b) match pack range `SnnExx-Eyy`, `Snn Exx-Eyy`, `Snn-Exx-Eyy` con `nn` uguale alla stagione richiesta e `xx <= episodio_richiesto <= yy`; c) match pack range `SnnExx-yy`, `Snn Exx-yy`, `Snn-Exx-yy` con `nn` uguale alla stagione richiesta e `xx <= episodio_richiesto <= yy`; d) match stagione completa testuale localizzato con formato `Season Snn ... COMPLETE` dove "Season" e "COMPLETE" sono localizzati nella stessa lingua (es. `Season S03 ... COMPLETE`, `Stagione 3 ... COMPLETA`) e stagione uguale a quella richiesta; e) match stagione completa testuale localizzato con formato numerico `Season d ... COMPLETE` dove "Season" e "COMPLETE" sono localizzati nella stessa lingua, con `d` il numero di stagione come intero (es. `Season 3 ... COMPLETE`, `Stagione 3 ... COMPLETA`). Tutti gli item che non soddisfano alcuna logica devono essere rimossi.
  ID originale: `REQ-023`.
  Comportamento atteso: un episodio singolo (`S03E01`) mantiene sia match episodio singolo sia season-pack compatibili con il range episodio (`S03E01-23`, `S03E01-13`, `S03E01-23`) e match testuali stagione completa localizzati coerenti nella stessa lingua; deve escludere stagioni diverse, range che non includono l'episodio richiesto e stringhe stagione senza indicazione di completezza.
  Criteri di accettazione: `filter_out_non_matching()` esegue il parsing RTN per il match episodio classico, verifica pattern regex per i due formati di range episodi e verifica pattern localizzati "Season ... COMPLETE" con controllo coerenza lingua e stagione, supportando sia formato `Season Snn` che formato numerico `Season d`; l'item viene mantenuto se almeno un controllo ritorna vero.
  Evidenza: `src/debriddo/utils/filter_results.py` / `filter_out_non_matching()`, `_match_complete_season()`, helper regex stagione/range episodio.

- **REQ-552**: Dopo la fase di filtraggio "non matching series torrents", la pipeline deve loggare il nuovo conteggio item rimasti con il messaggio `Item count changed to <n>`.  
  ID originale: `N/A`.
  Comportamento atteso: subito dopo il log `Filtering out non matching series torrents` e la chiamata `filter_out_non_matching(...)`, il log DEBUG riporta il numero di item rimasti prima del log `Filter results for season: ...`.  
  Criteri di accettazione: nel ramo `media.type == "series"` di `filter_items()`, il codice chiama `filter_out_non_matching(...)`, poi `logger.debug(f"Item count changed to {len(items)}")` e successivamente `logger.debug("Filter results for season: " + media.season + ", spisode: " + media.episode)`.  
  Evidenza: `src/debriddo/utils/filter_results.py` / `filter_items()`. Estratto: `items = filter_out_non_matching(...); logger.debug(f"Item count changed to {len(items)}")`.

- **REQ-573**: In modalita DEBUG, dopo il log `Filtering Torrent Search (Engines) results` e prima del log `Item count before filtering: <n>`, la pipeline deve stampare l'elenco dei risultati engine con indice ordinale, testo usato per il filtering e infohash.  
  ID originale: `N/A`.  
  Comportamento atteso: per ogni risultato engine in ordine di lista, il log emette `NN. "<filter_text>" [infohash <info_hash>]` con `NN` a due cifre, `filter_text` uguale a `SearchResult.raw_title` (fallback `SearchResult.title` se mancante) e `info_hash` uguale a `SearchResult.info_hash`.  
  Criteri di accettazione: in `get_results()` subito dopo `logger.debug("Filtering Torrent Search (Engines) results")`, il codice itera `engine_results` con `enumerate(..., start=1)` e chiama `logger.debug(f"{index:02d}. \"{filter_text}\" [infohash {result.info_hash}]")` prima della chiamata a `filter_items(...)`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`.  

- **REQ-533**: La pipeline di filtraggio deve rimuovere torrent il cui titolo parsato non matcha alcun titolo media sopra una soglia di similarita 0.5 per i film, mentre per le serie deve verificare almeno una delle seguenti condizioni (OR logico): a) match generico titolo sopra soglia 0.5; b) titolo seguito da stagione con pattern `<titolo>.+Snn` dove `nn` e' la stagione richiesta; c) titolo seguito da stagione localizzata con pattern `<titolo>.+Season Snn` dove "Season" e' localizzato in tutte le lingue supportate e `nn` e' la stagione richiesta; d) titolo seguito da stagione localizzata numerica con pattern `<titolo>.+Season d` dove "Season" e' localizzato in tutte le lingue supportate e `d` e' il numero di stagione come intero.
  ID originale: `REQ-024`.
  Comportamento atteso: candidati con mismatch titolo sono scartati; per le serie, il match considera anche la presenza della stagione richiesta nel titolo torrent.
  Criteri di accettazione: `remove_non_matching_title()` usa `threshold = float(0.5)` e `title_match(title, item.parsed_data.parsed_title, threshold)` per i film; per le serie, implementa logica OR tra match generico e pattern regex specifici per stagione nelle tre forme descritte, usando i dizionari `season_labels` per la localizzazione.
  Evidenza: `src/debriddo/utils/filter_results.py` / `remove_non_matching_title()`, `_match_title_with_season()`. Estratto: `threshold = float(0.5)`.

- **REQ-534**: Quando `config['sort']` e' impostato, la pipeline di sorting deve rank-are i torrent usando la libreria RTN e poi applicare uno dei seguenti ordinamenti: `quality`, `sizeasc`, `sizedesc`, `qualitythensize`.  
  ID originale: `REQ-025`.
  Comportamento atteso: i torrent sono ordinati secondo il criterio selezionato.  
  Criteri di accettazione: `items_sort()` imposta `items[index].parsed_data` dal ranking RTN e restituisce un ordinamento in base a `config['sort']`.  
  Evidenza: `src/debriddo/utils/filter_results.py` / `items_sort()`. Estratto: `if config['sort'] == \"quality\": return sorted(items, key=sort_quality)`.

- **REQ-535 (Limite noto)**: Il filtro `QualityExclusionFilter` deve interrompere l'elaborazione degli item quando incontra il primo stream di qualita esclusa a causa dell'uso di `break` invece di continuare l'iterazione, potenzialmente producendo un set filtrato incompleto.  
  ID originale: `REQ-040 (Limite noto)`.
  Comportamento atteso: se una qualita esclusa appare presto, item successivi non esclusi possono essere omessi.  
  Criteri di accettazione: in `QualityExclusionFilter.filter()`, un match di qualita esclusa esegue `break` nel loop esterno degli item.  
  Evidenza: `src/debriddo/utils/filter/quality_exclusion_filter.py` / `filter()`. Estratto: `if quality.upper() in excluded_qualities: break`.

- **REQ-536 (Limite noto)**: Il filtro `LanguageFilter` deve potenzialmente emettere duplicati perche' appende lo stesso torrent piu' volte se piu' lingue matchano e non interrompe il loop interno sul primo match.  
  ID originale: `REQ-041 (Limite noto)`.
  Comportamento atteso: la lista filtrata puo' contenere duplicati.  
  Criteri di accettazione: `LanguageFilter.filter()` appende `torrent` dentro un loop su `torrent.languages` senza de-duplicazione.  
  Evidenza: `src/debriddo/utils/filter/language_filter.py` / `filter()`. Estratto: `for language in torrent.languages: if language in self.config['languages']: filtered_data.append(torrent)`.

### 3.8 Conversione, disponibilita e selezione file

- **REQ-537**: La pipeline di conversione torrent deve processare ogni `SearchResult` in un `TorrentItem` e, per link magnet, deve popolare info hash e lista tracker usando parsing del magnet.  
  ID originale: `REQ-026`.
  Comportamento atteso: ogni `TorrentItem` ha `info_hash` e `trackers` quando possibile.  
  Criteri di accettazione: `TorrentService.__process_magnet()` imposta `result.info_hash = get_info_hash_from_magnet(...)` quando mancante e `result.trackers = self.__get_trackers_from_magnet(...)`.  
  Evidenza: `src/debriddo/torrent/torrent_service.py` / `__process_magnet()`. Estratto: `result.info_hash = get_info_hash_from_magnet(result.magnet)`.

- **REQ-538**: La selezione dei “best matching” torrent deve includere tutti gli item con magnet link e deve includere gli item con `torrent_download` solo quando `file_index` e' disponibile.  
  ID originale: `REQ-903`.
  Comportamento atteso: per risultati basati su torrent file (`torrent_download != None`), item senza `file_index` non vengono considerati “best matching”.  
  Criteri di accettazione: `TorrentSmartContainer.get_best_matching()` appende item se `torrent_download is None` oppure se `torrent_download is not None` e `file_index is not None`.  
  Evidenza: `src/debriddo/torrent/torrent_smart_container.py` / `get_best_matching()`. Estratto: `if torrent_item.torrent_download is not None: ... if torrent_item.file_index is not None: best_matching.append(torrent_item) ... else: best_matching.append(torrent_item)`.

### 3.9 Cache SQLite

- **REQ-539**: Il path di scrittura cache deve persistere solo torrent la cui `privacy` e' `\"public\"`.  
  ID originale: `REQ-033`.
  Comportamento atteso: torrent privati sono esclusi dal database cache.  
  Criteri di accettazione: `TorrentSmartContainer.__save_to_cache()` filtra item con `lambda x: x.privacy == \"public\"`.  
  Evidenza: `src/debriddo/torrent/torrent_smart_container.py` / `__save_to_cache()`. Estratto: `public_torrents = list(filter(lambda x: x.privacy == \"public\", self.get_items()))`.

- **REQ-540**: Il path di lookup cache deve cancellare record scaduti piu' vecchi di `config['daysCacheValid']` giorni prima di cercare match.  
  ID originale: `REQ-034`.
  Comportamento atteso: il database cache viene potato in fase di lookup.  
  Criteri di accettazione: `search_cache()` esegue una DELETE con `datetime('now', '-{days} days')`.  
  Evidenza: `src/debriddo/utils/cache.py` / `search_cache()`. Estratto: `DELETE FROM '{TABLE_NAME}' WHERE created_at < datetime('now', '-{days} days');`.

- **REQ-541**: Il path di lookup cache deve considerare match di serie per stagione/episodio richiesti usando range memorizzati e un boolean `seasonfile`, come implementato dalla logica filtro SQL.  
  ID originale: `REQ-035`.
  Comportamento atteso: season pack e file episodio in cache possono matchare richieste future entro limiti memorizzati.  
  Criteri di accettazione: per serie, il filtro SQL include check su `season_first/season_last`, `episode_first/episode_last` e `seasonfile`.  
  Evidenza: `src/debriddo/utils/cache.py` / clausola filtro serie in `search_cache()`. Estratto: `((season_first <= :season ... episode_first <= :episode ... seasonfile = False) OR (... seasonfile = True))`.

- **REQ-542 (Limite noto)**: Il recupero cache deve eseguire Python `eval()` su valori stringa persistiti per campi lista (`media_titles`, `media_languages`, `torrent_languages`, `torrent_trackers`), che puo' eseguire codice arbitrario se il contenuto del database e' controllato da un attaccante.  
  ID originale: `REQ-049 (Limite noto)`.
  Comportamento atteso: righe cache sono convertite da rappresentazioni stringa a oggetti Python usando `eval()`.  
  Criteri di accettazione: `search_cache()` usa `eval(...)` sui campi elencati.  
  Evidenza: `src/debriddo/utils/cache.py` / `search_cache()`. Estratto: `cache_item['torrent_trackers'] = eval(cache_item['torrent_trackers'])`.

- **REQ-543 (Limite noto)**: La pipeline stream deve scrivere risultati in cache anche quando `config['cache']` e' false, poiche' `cache_container_items()` e' invocato incondizionatamente nel ramo `if config['debrid']:`.  
  ID originale: `REQ-904 (Limite noto)`.
  Comportamento atteso: richieste stream con Debrid abilitato possono produrre scritture su `caches_items.db` anche se caching e' disabilitato in config.  
  Criteri di accettazione: `main.py` invoca `torrent_smart_container.cache_container_items()` senza condizione `if config['cache']`; `cache_container_items()` invoca `__save_to_cache()` che chiama `cache_results(...)`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `torrent_smart_container.cache_container_items()`; `src/debriddo/torrent/torrent_smart_container.py` / `cache_container_items()`. Estratto: `self.__save_to_cache()`.

### 3.10 Formattazione stream Stremio

- **REQ-544**: La pipeline di formattazione stream deve generare fino a `int(config['maxResults'])` stream entry Stremio, ciascuna contenente `name`, `description` e (a seconda della configurazione) un `url` di playback (Debrid) oppure `infoHash`/`fileIdx` (play diretto torrent).  
  ID originale: `REQ-027`.
  Comportamento atteso: gli elementi `streams` matchano le chiavi attese da Stremio.  
  Criteri di accettazione: `parse_to_stremio_streams()` itera `torrent_items[:int(config['maxResults'])]` e produce item con `url` per Debrid e `infoHash` per entry dirette.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / `parse_to_stremio_streams()`. Estratto: `for torrent_item in torrent_items[:int(config['maxResults'])]:`.

- **REQ-545**: Quando `config['playtorrent']` e' true, la pipeline di formattazione stream deve aggiungere una seconda entry stream che rappresenta playback torrent diretto con `name` prefissato `[🏴‍☠️` e chiavi `infoHash` e `fileIdx`.  
  ID originale: `REQ-028`.
  Comportamento atteso: un'entry torrent diretto e' disponibile insieme alle entry Debrid.  
  Criteri di accettazione: `parse_to_debrid_stream()` verifica `if playtorrent:` e pusha un item contenente `infoHash` e `fileIdx`.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / `parse_to_debrid_stream()`. Estratto: `item = {\"name\": name, ... \"infoHash\": torrent_item.info_hash, \"fileIdx\": int(torrent_item.file_index) ...}`.

- **REQ-546**: Ogni stream entry generata per Debrid deve includere `behaviorHints` contenente `bingeGroup` basato su `info_hash` e `filename` basato su `torrent_item.file_name` quando presente (altrimenti `torrent_item.raw_title`).  
  ID originale: `REQ-905`.
  Comportamento atteso: Stremio puo' usare hint di binge-grouping e filename.  
  Criteri di accettazione: `parse_to_debrid_stream()` imposta `behaviorHints.bingeGroup` a `debriddo-<info_hash>` e `behaviorHints.filename` a `file_name` se non `None`.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / `parse_to_debrid_stream()`. Estratto: `\"behaviorHints\":{ \"bingeGroup\": f\"debriddo-{torrent_item.info_hash}\", \"filename\": ... }`.

- **REQ-547**: Ogni stream entry generata per play diretto torrent deve includere `behaviorHints` con gli stessi campi `bingeGroup` e `filename` usati per l'entry Debrid corrispondente.  
  ID originale: `REQ-906`.
  Comportamento atteso: anche l'entry torrent diretto include hint consistenti.  
  Criteri di accettazione: nel ramo `if playtorrent:`, l'item include `behaviorHints` con `bingeGroup` e `filename`.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / ramo `if playtorrent:` in `parse_to_debrid_stream()`. Estratto: `\"behaviorHints\":{ \"bingeGroup\": f\"debriddo-{torrent_item.info_hash}\", \"filename\": ... }`.

- **REQ-548**: Il campo `name` delle entry stream deve iniziare con `[⚡` quando `torrent_item.availability == True` e con `[⬇️` altrimenti; per play diretto torrent deve iniziare con `[🏴‍☠️`.  
  ID originale: `REQ-907`.
  Comportamento atteso: la UI Stremio mostra indicatori di disponibilita e tipo.  
  Criteri di accettazione: `parse_to_debrid_stream()` assegna `INSTANTLY_AVAILABLE=\"[⚡\"`, `DOWNLOAD_REQUIRED=\"[⬇️\"`, `DIRECT_TORRENT=\"[🏴‍☠️\"` e costruisce `name` di conseguenza.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / costanti e logica `name`. Estratto: `if torrent_item.availability == True: name = f\"{INSTANTLY_AVAILABLE}\" ... else: name = f\"{DOWNLOAD_REQUIRED}\"` e `name = f\"{DIRECT_TORRENT}\"`.

- **REQ-549**: Il campo `description` delle entry stream deve includere il titolo raw, opzionalmente `file_name`, seeders e dimensione in GB, indexer e, quando presenti, codec/audio; deve inoltre includere una sequenza di emoji lingua per ciascuna lingua in `torrent_item.languages`.  
  ID originale: `REQ-908`.
  Comportamento atteso: la descrizione fornisce dettagli leggibili dall'utente.  
  Criteri di accettazione: `parse_to_debrid_stream()` costruisce `title` includendo `torrent_item.raw_title`, `torrent_item.file_name` se presente, una riga con `seeders`, `size_in_gb` e `indexer`, e poi appende emoji da `get_emoji(language)` per ogni lingua.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / `parse_to_debrid_stream()`. Estratto: `title = f\"{torrent_item.raw_title}\\n\"` e `title += f\"👥 {torrent_item.seeders}   💾 {size_in_gb}GB   🔍 {torrent_item.indexer}\\n\"` e `title += f\"{get_emoji(language)}/\"`.

- **REQ-550**: La lista `streams` deve essere ordinata (quando `config['debrid']` e' true) in modo da porre prima gli item istantaneamente disponibili e poi gli item di torrent diretto, secondo le funzioni di sorting implementate.  
  ID originale: `REQ-909`.
  Comportamento atteso: l'ordine degli stream favorisce disponibilita e tipo.  
  Criteri di accettazione: `parse_to_stremio_streams()` applica `sorted(stream_list, key=filter_by_availability)` e poi `sorted(stream_list, key=filter_by_direct_torrnet)` sotto `if config['debrid']:`.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / `parse_to_stremio_streams()`. Estratto: `stream_list = sorted(stream_list, key=filter_by_availability)` e `stream_list = sorted(stream_list, key=filter_by_direct_torrnet)`.

- **REQ-551**: Quando l'URL di playback generato per un item supera lunghezza 2000, il sistema deve loggare un warning “Generated url is too long” includendo il titolo torrent raw.  
  ID originale: `REQ-910`.
  Comportamento atteso: viene emesso un warning per URL lunghi potenzialmente problematici.  
  Criteri di accettazione: `parse_to_debrid_stream()` verifica `if len(item['url']) > 2000:` e invoca `logger.warning(...)`.  
  Evidenza: `src/debriddo/utils/stremio_parser.py` / `parse_to_debrid_stream()`. Estratto: `if len(item['url']) > 2000: logger.warning(f\"Generated url is too long in item: {torrent_item.raw_title}\")`.

### 3.11 Playback (redirect Debrid)

- **REQ-552**: L'endpoint playback `GET /playback/{config_url}/{query_string}` deve decodificare config e query, risolvere un link stream Debrid usando il servizio configurato e rispondere con un redirect HTTP 301 verso tale link.  
  ID originale: `REQ-029`.
  Comportamento atteso: i client vengono reindirizzati a un URL streaming risolto.  
  Criteri di accettazione: l'handler invoca `parse_config`, `parse_query`, `get_debrid_service`, attende `get_stream_link` e restituisce `RedirectResponse(..., status_code=301)`.  
  Evidenza: `src/debriddo/main.py` / `get_playback()`. Estratto: `link = await debrid_service.get_stream_link(query, ip)`.

- **REQ-553**: L'endpoint playback deve restituire HTTP 400 quando `query_string` e' vuota o mancante.  
  ID originale: `REQ-030`.
  Comportamento atteso: richieste playback invalide sono rifiutate.  
  Criteri di accettazione: l'handler verifica `if not query_string: raise HTTPException(status_code=400, ...)`.  
  Evidenza: `src/debriddo/main.py` / `get_playback()`. Estratto: `raise HTTPException(status_code=400, detail=\"Query required.\")`.

- **REQ-554 (Limite noto)**: L'endpoint `HEAD /playback/{config_url}/{query}` deve essere considerato non funzionante perche' il nome parametro path `config_url` non corrisponde al nome argomento handler `config`, causando errori di validazione.  
  ID originale: `REQ-042 (Limite noto)`.
  Comportamento atteso: FastAPI restituisce errore di validazione (HTTP 422) per binding parametro mancante.  
  Criteri di accettazione: il decoratore rotta usa `{config_url}` ma la signature handler usa `config: str`.  
  Evidenza: `src/debriddo/main.py` / rotta `@app.head(\"/playback/{config_url}/{query}\")` e signature handler. Estratto: `async def head_playback(config: str, query: str, request: Request):`.

### 3.12 Servizi Debrid (implementazioni)

- **REQ-555 (Limite noto)**: Quando `config['service'] == \"torbox\"`, il check disponibilita nell'endpoint stream deve essere considerato difettoso perche' il codice chiama `debrid_service.get_availability_bulk(...)` senza `await` e poi tratta la coroutine risultante come mapping.  
  ID originale: `REQ-044 (Limite noto)`.
  Comportamento atteso: l'handler stream puo' sollevare eccezione durante l'update disponibilita e fallire la richiesta.  
  Criteri di accettazione: il codice assegna `result = debrid_service.get_availability_bulk(hashes, ip)` senza `await` e poi invoca `result.items()` e passa `result` a `update_availability`.  
  Evidenza: `src/debriddo/main.py` / `get_results()`. Estratto: `result = debrid_service.get_availability_bulk(hashes, ip)`.

- **REQ-556 (Limite noto)**: L'implementazione Debrid AllDebrid deve essere considerata difettosa nel polling di readiness perche' passa una lambda a `wait_for_ready_status_async_func` che tenta di subscriptare una chiamata async senza `await`.  
  ID originale: `REQ-045 (Limite noto)`.
  Comportamento atteso: il polling puo' sollevare eccezione runtime invece di attendere correttamente.  
  Criteri di accettazione: `get_stream_link()` chiama `wait_for_ready_status_async_func(lambda: self.check_magnet_status(...)[...])` dove `check_magnet_status` e' `async def`.  
  Evidenza: `src/debriddo/debrid/alldebrid.py` / `get_stream_link()`. Estratto: `lambda: self.check_magnet_status(torrent_id, ip)[\"data\"][\"magnets\"][\"status\"] == \"Ready\"`.

- **REQ-557 (Limite noto)**: L'implementazione Debrid Premiumize deve essere considerata difettosa nel polling di readiness perche' non fa `await` della chiamata async `wait_for_ready_status_async_func(...)`.  
  ID originale: `REQ-046 (Limite noto)`.
  Comportamento atteso: il codice non attende realmente readiness e procede immediatamente.  
  Criteri di accettazione: `get_stream_link()` usa `if not self.wait_for_ready_status_async_func(...):` senza `await`.  
  Evidenza: `src/debriddo/debrid/premiumize.py` / `get_stream_link()`. Estratto: `if not self.wait_for_ready_status_async_func(lambda: self.get_availability(info_hash)[\"transcoded\"][0] is True):`.

- **REQ-558 (Limite noto)**: L'implementazione Debrid TorBox deve essere considerata difettosa nel percorso cached-file perche' tenta di subscriptare il valore di ritorno di `check_magnet_status(...)` senza attendere correttamente il risultato.  
  ID originale: `REQ-047 (Limite noto)`.
  Comportamento atteso: il path cached puo' sollevare eccezione runtime invece di recuperare metadati file.  
  Criteri di accettazione: nel ramo cached, `get_stream_link()` esegue `await self.check_magnet_status(...)[...]` (subscript prima di usare il risultato atteso della coroutine).  
  Evidenza: `src/debriddo/debrid/torbox.py` / `get_stream_link()`. Estratto: `files = await self.check_magnet_status(magnet_data[\"hash\"])[magnet_data[\"hash\"]]`.

- **REQ-559 (Limite noto)**: Le implementazioni RealDebrid e AllDebrid devono essere considerate difettose nel path “torrent file upload” perche' referenziano un nome metodo errato `donwload_torrent_file` e omettono `await` richiesti in quel ramo.  
  ID originale: `REQ-048 (Limite noto)`.
  Comportamento atteso: se viene fornito un URL `torrent_download`, il path puo' sollevare `AttributeError` o comportarsi in modo errato.  
  Criteri di accettazione: le implementazioni chiamano `self.donwload_torrent_file(...)` (typo) e/o chiamano metodi async senza `await`.  
  Evidenza: `src/debriddo/debrid/realdebrid.py` / `__add_magnet_or_torrent()`. Estratto: `torrent_file = self.donwload_torrent_file(torrent_download)`; `src/debriddo/debrid/alldebrid.py` / `__add_magnet_or_torrent()`. Estratto: `torrent_file = self.donwload_torrent_file(torrent_download)`.

- **REQ-560**: Quando un servizio Debrid non riesce a produrre un link stream pronto (es. caching in corso o assenza file matching), l'implementazione deve restituire l'URL fallback `NO_CACHE_VIDEO_URL`.  
  ID originale: `REQ-911`.
  Comportamento atteso: il playback viene reindirizzato verso un video di fallback in caso di non disponibilita immediata.  
  Criteri di accettazione: almeno una implementazione Debrid ritorna `NO_CACHE_VIDEO_URL` in condizioni di non-readiness; `NO_CACHE_VIDEO_URL` e' definito in `constants.py`.  
  Evidenza: `src/debriddo/constants.py` / `NO_CACHE_VIDEO_URL`. Estratto: `NO_CACHE_VIDEO_URL = \"https://github.com/Ogekuri/debriddo/raw/refs/heads/master/videos/nocache.mp4\"`; `src/debriddo/debrid/realdebrid.py` / `get_stream_link()`. Estratto: `if links is None: return NO_CACHE_VIDEO_URL`.

### 3.13 Script API tester

- **REQ-561**: Tutte le implementazioni API Tester in `src/api_tester/` devono restare autonome e non devono importare o utilizzare moduli/librerie dell'applicazione Debriddo presenti in `src/debriddo/`.  
  ID originale: `REQ-912`.
  Comportamento atteso: i tester API usano solo librerie standard e dipendenze esterne generiche senza accedere al namespace `debriddo`.  
  Criteri di accettazione: ogni entrypoint API tester include un controllo runtime che rifiuta l'esecuzione se rileva moduli `debriddo` caricati e il codice non contiene import diretti di `debriddo`.  
  Evidenza: `src/api_tester/api_tester.py` / `ensure_no_debriddo_modules_loaded()` e `main()`. Estratto: `if name == DEBRIDDO_MODULE_PREFIX or name.startswith(f\"{DEBRIDDO_MODULE_PREFIX}.\")`; `ensure_no_debriddo_modules_loaded()`.

- **REQ-562**: Il tester API deve risolvere il target da `--config-url` oppure da variabile ambiente configurabile con priorita' al parametro CLI, e deve validare che l'URL contenga un segmento `C_`.  
  ID originale: `REQ-913`.
  Comportamento atteso: in assenza di `--config-url`, il tester legge `--config-url-env` (default `DEBRIDDO_CONFIG_URL`) e fallisce con errore descrittivo se il valore e' assente o invalido.  
  Criteri di accettazione: `get_target_from_args()` usa `args.config_url` prima di `os.getenv(args.config_url_env, \"\")`; `normalize_config_url()` richiede schema+host e un segmento path che inizia con `C_`.  
  Evidenza: `src/api_tester/api_tester.py` / `get_target_from_args()`, `normalize_config_url()`, `DEFAULT_CONFIG_ENV`. Estratto: `config_url = args.config_url or os.getenv(args.config_url_env, \"\")`; `if segment.startswith(\"C_\")`.

- **REQ-563**: Il comando `target` deve stampare i tre identificatori normalizzati `base_url`, `config_url`, `config_token` derivati dal target risolto.  
  ID originale: `REQ-914`.
  Comportamento atteso: l'utente ottiene una vista deterministica dei valori usati dai comandi HTTP.  
  Criteri di accettazione: `cmd_target()` stampa le righe con prefissi letterali `base_url`, `config_url`, `config_token`.  
  Evidenza: `src/api_tester/api_tester.py` / `cmd_target()`. Estratto: `print(f\"base_url     : {target.base_url}\")`.

- **REQ-564**: I comandi `root`, `configure`, `manifest`, `site-webmanifest` devono invocare gli endpoint HTTP corrispondenti con timeout/TLS configurabili e restituire codice uscita `0` su risposta `2xx/3xx` e `1` su errore HTTP.  
  ID originale: `REQ-915`.
  Comportamento atteso: il tester fornisce check endpoint basilari riutilizzando un flusso di richiesta/summary comune.  
  Criteri di accettazione: i comandi usano `call_simple_endpoint()`; `configure` e `manifest` supportano `--with-config` per prefisso `/{config}/`; `call_simple_endpoint()` ritorna `0 if response.ok else 1`.  
  Evidenza: `src/api_tester/api_tester.py` / `cmd_root()`, `cmd_configure()`, `cmd_manifest()`, `cmd_site_webmanifest()`, `call_simple_endpoint()`. Estratto: `path = f\"/{target.config_segment}/configure\" if args.with_config else \"/configure\"`; `return 0 if response.ok else 1`.

- **REQ-565**: Il comando `asset` deve supportare i tipi `favicon`, `configjs`, `lzstring`, `styles`, `image` e deve mappare ciascun tipo al path statico previsto, con prefisso `/{config}/` opzionale per i tipi applicabili.  
  ID originale: `REQ-916`.
  Comportamento atteso: il tester copre asset statici principali e fallisce su tipo asset non riconosciuto.  
  Criteri di accettazione: `cmd_asset()` implementa mapping deterministico per `--asset-type`; `--with-config` non viene applicato a `favicon`; i tipi non supportati generano `CliError`.  
  Evidenza: `src/api_tester/api_tester.py` / `cmd_asset()`. Estratto: `choices=[\"favicon\", \"configjs\", \"lzstring\", \"styles\", \"image\"]`; `if args.with_config and args.asset_type != \"favicon\":`.

- **REQ-566**: Il comando `stream` deve costruire il path `/{config}/stream/{type}/{id}` codificando `stream_id`, supportare suffisso opzionale `.json`, e riassumere il numero stream con anteprima chiavi per un massimo configurabile di elementi.  
  ID originale: `REQ-917`.
  Comportamento atteso: l'utente puo' verificare endpoint stream movie/series e ottenere un sommario del payload.  
  Criteri di accettazione: `build_stream_path()` usa `quote(stream_id, safe=\":.\")` e aggiunge `.json` quando richiesto; `cmd_stream()` stampa `streams: <n>` e fino a `args.preview_streams` righe `keys=...` quando il payload e' valido.  
  Evidenza: `src/api_tester/api_tester.py` / `build_stream_path()`, `cmd_stream()`. Estratto: `encoded_stream_id = quote(stream_id, safe=\":.\")`; `print(f\"streams: {len(streams)}\")`.

- **REQ-567**: Il comando `playback` deve chiamare `/playback/{config}/{query}` usando query esplicita o ricavata automaticamente dal primo stream che contiene URL playback, con supporto metodo `GET` o `HEAD`.  
  ID originale: `REQ-918`.
  Comportamento atteso: il tester verifica playback sia con query fornita sia con discovery da endpoint stream.  
  Criteri di accettazione: `cmd_playback()` usa `--query` se presente; in assenza esegue `request_stream()` e `extract_playback_path_from_streams()`; `--head` imposta metodo `HEAD`, altrimenti `GET`; in assenza playback URL viene sollevato `CliError`.  
  Evidenza: `src/api_tester/api_tester.py` / `cmd_playback()`, `extract_playback_path_from_streams()`. Estratto: `if args.query: playback_path = f\"/playback/{target.config_segment}/{args.query}\"`; `if \"/playback/\" in parsed.path: return parsed.path`.

- **REQ-568**: Il comando `smoke` deve eseguire una suite integrata multi-endpoint (root, configure, asset, manifest, stream, playback), registrare esito per check con formato `[PASS|FAIL]`, e restituire `0` solo quando non sono presenti fallimenti.  
  ID originale: `REQ-919`.
  Comportamento atteso: una singola esecuzione produce verifica end-to-end ripetibile delle API principali.  
  Criteri di accettazione: `run_smoke()` aggiunge `CheckResult` per ciascun endpoint previsto incluse le varianti prefissate `/{config}/...`; `cmd_smoke()` stampa il riepilogo `Totale: <n> test, <f> falliti.` e ritorna `0 if failed == 0 else 1`.  
  Evidenza: `src/api_tester/api_tester.py` / `run_smoke()`, `cmd_smoke()`. Estratto: `add_check(results, \"GET /{config}/stream/movie/{id}.json\", ...)`; `print(f\"\\nTotale: {len(results)} test, {failed} falliti.\")`.

- **REQ-569**: Il tester API deve usare codici di uscita dedicati per errori non-funzionali: `2` per errori di dipendenza/modulo HTTP, eccezioni `requests` o validazione CLI.  
  ID originale: `REQ-920`.
  Comportamento atteso: gli errori infrastrutturali/di input sono distinguibili dai fallimenti di check endpoint.  
  Criteri di accettazione: import failure di `requests` termina con `sys.exit(2)`; `main()` intercetta `requests.RequestException` e `CliError` restituendo `2`.  
  Evidenza: `src/api_tester/api_tester.py` / blocco import `requests`, `main()`. Estratto: `sys.exit(2)`; `except requests.RequestException ... return 2`; `except CliError ... return 2`.

- **REQ-570**: Il comando `search` deve eseguire la chiamata stream come `stream` e stampare l'elenco completo degli stream trovati con tutti i campi utili per una successiva richiesta di playback (es. `url`, `infoHash`, `fileIdx`, `behaviorHints`, magnet/torrent se presenti).  
  ID originale: `REQ-921`.
  Comportamento atteso: l'utente ottiene l'intero payload di ciascun item stream, non solo un riepilogo.  
  Criteri di accettazione: `cmd_search()` usa `request_stream()` e `build_stream_path()` come `cmd_stream()`; il comando richiede `--stream-type` e `--stream-id`, supporta `--append-json`, e stampa ogni item `streams` serializzato per intero con indice.  
  Evidenza: `src/api_tester/api_tester.py` / `cmd_search()`, `build_parser()`. Estratto: `parser_search = subparsers.add_parser("search", ...)`; `for index, item in enumerate(streams): print(json.dumps(item, ...))`.

## 4. Requisiti di test
<!-- Requisiti di test legati a requisiti funzionali/non-funzionali o contesti di verifica -->

- **DES-532**: Questa sezione deve definire procedure di verifica riproducibili (manuali o automatizzate) per i comportamenti implementati descritti in Sezione 3 e deve dichiarare limitazioni di copertura quando non esiste una suite di unit test.  
  ID originale: `DES-115`.
  Comportamento atteso: i lettori possono validare comportamenti `REQ-*` senza affidarsi a test non documentati.  
  Criteri di accettazione: ogni requisito di test include un criterio pass/fail chiaro e referenzia almeno un requisito `REQ-*`.  
  Evidenza: la repository contiene una directory `tests/` che contiene una suite convenzionale di unit test.

- **TST-501**: Il sistema deve essere verificabile per `REQ-511` inviando `GET /manifest.json` e asserendo che la risposta e' JSON contenente un array `resources` con una risorsa `stream` che supporta `movie` e `series`.  
  ID originale: `TST-001`.
  Comportamento atteso: l'endpoint manifest restituisce una struttura compatibile Stremio.  
  Criteri di accettazione: PASS se il JSON contiene `resources` e un elemento con `"name": "stream"` e `"types"` includendo `"movie"` e `"series"`; FAIL altrimenti.  
  Evidenza: `src/debriddo/main.py` / `get_manifest()`. Estratto: `\"types\": [\"movie\", \"series\", \"anime\", \"other\"]`.

- **TST-502**: Il sistema deve essere verificabile per `REQ-502` inviando `GET /configure` e asserendo che la risposta e' HTML contenente la sostituzione di `$APP_NAME` (cioe' la substring letterale `$APP_NAME` non deve comparire).  
  ID originale: `TST-002`.
  Comportamento atteso: avviene la sostituzione placeholder.  
  Criteri di accettazione: PASS se il body contiene `Debriddo` e non contiene `$APP_NAME`; FAIL altrimenti.  
  Evidenza: `src/debriddo/web/pages.py` / `get_index()`. Estratto: `index = index.replace( \"$APP_NAME\", app_name )`.

- **TST-503**: Il sistema deve essere verificabile per `REQ-552` costruendo `config_url` e `query_string` validi, chiamando `GET /playback/{config_url}/{query_string}` e asserendo una risposta HTTP 301 con header `Location`.  
  ID originale: `TST-003`.
  Comportamento atteso: richieste playback reindirizzano.  
  Criteri di accettazione: PASS se status e' 301 e `Location` e' presente; FAIL altrimenti.  
  Evidenza: `src/debriddo/main.py` / `get_playback()` imposta `status_code=status.HTTP_301_MOVED_PERMANENTLY`. Estratto: `status_code=status.HTTP_301_MOVED_PERMANENTLY`.

- **TST-504**: Il sistema deve essere verificabile per `REQ-561` eseguendo un'analisi statica delle implementazioni sotto `src/api_tester/` per assicurarsi che non contengano import di `debriddo` e che gli entrypoint includano un controllo runtime di blocco moduli `debriddo`.  
  ID originale: `TST-004`.
  Comportamento atteso: il tester API non dipende dal codice applicativo Debriddo in tutte le varianti implementate.  
  Criteri di accettazione: PASS se non compaiono statement `import debriddo` e se in ciascun entrypoint e' presente una chiamata a `ensure_no_debriddo_modules_loaded()` prima dell'esecuzione operativa; FAIL altrimenti.  
  Evidenza: `src/api_tester/api_tester.py` / `ensure_no_debriddo_modules_loaded()` e `main()`. Estratto: `ensure_no_debriddo_modules_loaded()`; `loaded = sorted(...)`.

- **TST-505**: Il sistema deve essere verificabile per `REQ-562` e `REQ-563` eseguendo `target` con `--config-url` e con fallback env var, e asserendo l'output normalizzato dei campi `base_url`, `config_url`, `config_token`.  
  ID originale: `TST-005`.
  Comportamento atteso: la risoluzione target e' deterministica e valida per URL con o senza suffisso `/manifest.json` o `/configure`.  
  Criteri di accettazione: PASS se il comando `target` stampa i tre campi previsti con valori coerenti al segmento `C_`; FAIL se manca un campo o la normalizzazione non produce token `C_...`.  
  Evidenza: `src/api_tester/api_tester.py` / `normalize_config_url()`, `get_target_from_args()`, `cmd_target()`. Estratto: `if path_segments[-1] in {\"manifest.json\", \"configure\"}:`; `print(f\"config_token : {target.config_segment}\")`.

- **TST-506**: Il sistema deve essere verificabile per `REQ-564`, `REQ-565`, `REQ-566`, `REQ-567`, `REQ-568` eseguendo il comando `smoke` su un'istanza Debriddo raggiungibile e validando l'output dei check endpoint.  
  ID originale: `TST-006`.
  Comportamento atteso: la suite smoke verifica endpoint principali, asset statici, stream movie/series e playback con report unificato PASS/FAIL.  
  Criteri di accettazione: PASS se `cmd_smoke()` riporta solo check `[PASS]` e termina con codice `0`; FAIL se almeno un check e' `[FAIL]` o il codice uscita e' non-zero.  
  Evidenza: `src/api_tester/api_tester.py` / `run_smoke()`, `cmd_smoke()`. Estratto: `results = run_smoke(args, target)`; `status_text = \"PASS\" if result.ok else \"FAIL\"`.

- **TST-507**: Il sistema deve essere verificabile per `REQ-569` inducendo errori controllati e asserendo il codice di uscita `2` per errori di validazione CLI o eccezioni HTTP `requests`.  
  ID originale: `TST-007`.
  Comportamento atteso: gli errori non-funzionali sono distinguibili dai fallimenti endpoint.  
  Criteri di accettazione: PASS se input invalido (es. config URL assente/non valida) produce output errore su `stderr` e codice `2`, e se eccezioni `requests.RequestException` sono intercettate con ritorno `2`; FAIL altrimenti.  
  Evidenza: `src/api_tester/api_tester.py` / `get_target_from_args()`, `main()`. Estratto: `raise CliError(...)`; `except requests.RequestException ... return 2`; `except CliError ... return 2`.

- **TST-508**: Il sistema deve essere verificabile per `REQ-570` eseguendo `search` con un media valido e verificando che l'output includa la lista completa degli stream con i campi payload completi per item.
  ID originale: `TST-008`.
  Comportamento atteso: il comando `search` espone ogni campo stream necessario al playback senza truncare il payload.
  Criteri di accettazione: PASS se l'output include il conteggio `streams: <n>` e almeno un item stampato come JSON completo con chiavi `url` o `infoHash` quando presenti; FAIL altrimenti.
  Evidenza: `src/api_tester/api_tester.py` / `cmd_search()`. Estratto: `print(f\"streams: {len(streams)}\")`; `print(json.dumps(item, ...))`.

- **TST-533**: Il sistema deve essere verificabile per `REQ-532` e `REQ-533` con unit test che verifica il filtraggio episodi serie usando dataset di test con titoli validi e non validi per un episodio specifico (es. `S03E01`).
  ID originale: `N/A`.
  Comportamento atteso: i test verificano che la funzione `filter_out_non_matching()` mantenga solo i torrent che matchano le logiche specificate in `REQ-532` e scartino quelli non conformi; i test verificano che `remove_non_matching_title()` applichi correttamente la logica di match titolo/stagione per le serie.
  Criteri di accettazione: suite di test parametrizzati con almeno 15 casi di test coprendo: episodi singoli nelle tre forme (`SnnEmm`, `Snn Emm`, `Snn-Emm`), pack range nelle varianti (`SnnExx-Eyy`, `SnnExx-yy`) con stagione corretta/errata e episodio dentro/fuori range, stagioni complete localizzate con/senza indicatore COMPLETE, stagioni diverse da quella richiesta; tutti i test devono passare.
  Evidenza: `tests/unit/atomic/test_filter_results.py` / `test_filter_out_non_matching_matches_requested_series_logic()`, `test_remove_non_matching_title_for_series()`.

## 5. Storico revisioni
<!-- A ogni modifica, aggiornare versione e aggiungere una riga -->

- **DES-533**: Questa sezione deve registrare una traccia cronologica delle modifiche a questa bozza SRS, con ogni riga includente data, versione e una descrizione concisa della modifica.  
  ID originale: `DES-117`.
  Comportamento atteso: i consumatori possono tracciare cosa e' cambiato e quando.  
  Criteri di accettazione: ogni modifica al documento aggiunge una riga e incrementa `version`.  
  Evidenza: `.req/templates/requirements.md` / sezione `## 5. Revision History`. Estratto: `On every change to this document, update the version number and add a new row to the revision history`.

| Data       | Versione | Motivazione e descrizione modifica |
|------------|----------|------------------------------------|
| 2026-02-12 | 0.2      | Riorganizzazione, traduzione in Italiano, integrazione di requisiti mancanti dal codice, e rinumerazione (vedi mapping nella risposta dell'agente). |
| 2026-02-12 | 0.3      | Aggiunto requisito di autonomia per lo script API tester e relativo requisito di test. |
| 2026-02-13 | 0.4      | Estesi i requisiti dello script API tester (target/endpoint/asset/stream/playback/smoke/errori) e rafforzato il vincolo di non dipendenza da librerie `src/debriddo/` per tutte le implementazioni API Tester. |
| 2026-02-13 | 0.5      | Aggiunto comando `search` al tester API per stampare i payload stream completi. |
| 2026-02-13 | 0.6      | Correzione validazione lingue UI, fallback lingue TMDB su lista vuota, e pulizia lista engine abilitati. |
| 2026-02-13 | 0.7      | Aggiornata la fase di filtering serie per preservare season-pack completi (`SnnE01-E` e `Season <n>` localizzato) della stagione richiesta. |
| 2026-02-13 | 0.8      | Refactory filtro serie TV: matching OR tra episodio (`SnnEmm`/varianti), range pack (`SnnExx-Eyy` e `SnnExx-yy`/varianti) e stagione completa localizzata (`Season ... COMPLETE` nella stessa lingua). |
| 2026-02-13 | 0.9      | Aggiunto requisito di log conteggio item dopo il filtro serie non matching. |
| 2026-02-13 | 1.0      | Migliorato REQ-532 per supportare match stagione completa con formato numerico (`Season d ... COMPLETE`); esteso REQ-533 per filtraggio titoli serie con pattern stagione (`<titolo>.+Snn`, `<titolo>.+Season Snn`, `<titolo>.+Season d`); aggiunto TST-533 per unit test filtro serie. |
| 2026-02-13 | 1.1      | Aggiornati REQ-571 e REQ-572: ciclo lingue da `config['languages']`, regole `lang_tag` condizionali su lingua indexer, ricerca primaria sempre attiva e fallback solo su assenza risultati primari. |
