# api_tester.py | Python | 1127L | 33 symbols | 9 imports | 35 comments
> Path: `src/api_tester/api_tester.py`
> CLI autonoma per testare le API HTTP esposte da Debriddo. La configurazione può arrivare da: ...

## Imports
```
from __future__ import annotations
import argparse
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote, urlparse
import requests
```

## Definitions

- var `DEFAULT_CONFIG_ENV = "DEBRIDDO_CONFIG_URL"` (L30) — : @brief Exported constant `DEFAULT_CONFIG_ENV` used by runtime workflows.
- var `DEFAULT_TIMEOUT = 180.0` (L32) — : @brief Exported constant `DEFAULT_TIMEOUT` used by runtime workflows.
- var `DEBRIDDO_MODULE_PREFIX = "debriddo"` (L34) — : @brief Exported constant `DEBRIDDO_MODULE_PREFIX` used by runtime workflows.
### class `class CliError(Exception)` : Exception (L37-44)
L38-41> @brief Class `CliError` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.

### fn `def ensure_no_debriddo_modules_loaded() -> None` (L45-62)
L46-51> Verifica che nessun modulo del package 'debriddo' sia stato caricato. Raises: CliError: Se vengono rilevati moduli 'debriddo' caricati.
L58> `raise CliError(`

### class `class TargetUrls` `@dataclass` (L64-73)
L65-68> @brief Class `TargetUrls` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.

### class `class CheckResult` `@dataclass` (L75-84)
L76-79> @brief Class `CheckResult` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.

### fn `def normalize_config_url(raw_value: str) -> TargetUrls` (L85-133)
L86-97> Analizza e normalizza l'URL di configurazione fornito. Args: raw_value (str): L'URL grezzo passato come input. Returns: TargetUrls: Oggetto contenente URL base, segmento config e URL completo. Raises: CliError: Se l'URL non è valido o manca del segmento di configurazione.
L100> `raise CliError("config URL vuota.")`
L104> `raise CliError(f"URL non valido: '{value}'.")`
L108> `raise CliError("Path URL non valido: manca il segmento C_<config>.")`
L119> `raise CliError("Impossibile trovare un segmento 'C_' nell'URL di configurazione.")`
L127> `return TargetUrls(`

### fn `def get_target_from_args(args: argparse.Namespace) -> TargetUrls` (L134-154)
L135-146> Recupera l'URL target dagli argomenti CLI o variabili d'ambiente. Args: args (argparse.Namespace): Gli argomenti parsati della CLI. Returns: TargetUrls: L'oggetto TargetUrls risolto. Raises: CliError: Se la configurazione è mancante.
L149> `raise CliError(`
L152> `return normalize_config_url(config_url)`

### fn `def request_url(` (L155-161)

### fn `def make_url(base_url: str, path: str) -> str` (L187-200)
L188-197> Costruisce un URL completo combinando base URL e path. Args: base_url (str): L'URL base. path (str): Il percorso relativo. Returns: str: L'URL completo senza doppi slash.
L198> `return f"{base_url.rstrip('/')}/{path.lstrip('/')}"`

### fn `def parse_json_body(response: requests.Response) -> Optional[Any]` (L201-216)
L202-210> Tenta di parsare il corpo della risposta come JSON. Args: response (requests.Response): La risposta HTTP. Returns: Optional[Any]: Il JSON parsato o None se il parsing fallisce.
L212> `return response.json()`
L214> `return None`

### fn `def print_response_summary(` (L217-220)

### fn `def call_simple_endpoint(` (L252-258)

### fn `def build_stream_path(` (L288-292)

### fn `def cmd_target(args: argparse.Namespace) -> int` (L312-328)
L313-321> Stampa le informazioni sul target risolto (comando 'target'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Sempre 0.
L326> `return 0`

### fn `def cmd_root(args: argparse.Namespace) -> int` (L329-350)
L330-338> Esegue il test dell'endpoint root '/' (comando 'root'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L341> `return call_simple_endpoint(`

### fn `def cmd_configure(args: argparse.Namespace) -> int` (L351-366)
L352-360> Esegue il test dell'endpoint '/configure' (comando 'configure'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L364> `return call_simple_endpoint(session, args, target, path, method="GET")`

### fn `def cmd_manifest(args: argparse.Namespace) -> int` (L367-382)
L368-376> Esegue il test dell'endpoint '/manifest.json' (comando 'manifest'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L380> `return call_simple_endpoint(session, args, target, path, method="GET")`

### fn `def cmd_site_webmanifest(args: argparse.Namespace) -> int` (L383-397)
L384-392> Esegue il test dell'endpoint '/site.webmanifest' (comando 'site-webmanifest'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L395> `return call_simple_endpoint(session, args, target, "/site.webmanifest", method="GET")`

### fn `def cmd_asset(args: argparse.Namespace) -> int` (L398-430)
L399-407> Esegue il test degli asset statici (comando 'asset'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L422> `raise CliError(f"Tipo asset non supportato: {args.asset_type}")`
L428> `return call_simple_endpoint(session, args, target, asset_path, method="GET")`

### fn `def request_stream(` (L431-437)

### fn `def cmd_stream(args: argparse.Namespace) -> int` (L470-506)
L471-479> Esegue il test dell'endpoint '/stream' (comando 'stream'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L504> `return 0 if response.ok else 1`

### fn `def cmd_search(args: argparse.Namespace) -> int` (L507-546)
L508-516> Esegue una ricerca stream stampando il payload completo (comando 'search'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L544> `return 0 if response.ok else 1`

### fn `def extract_playback_path_from_streams(streams_payload: Dict[str, Any]) -> Optional[str]` (L547-572)
L548-556> Estrae il path di playback dal payload degli stream. Args: streams_payload (Dict[str, Any]): Il payload JSON degli stream. Returns: Optional[str]: Il path di playback se trovato, altrimenti None.
L559> `return None`
L569> `return parsed.path`
L570> `return None`

### fn `def request_playback(` (L573-578)

### fn `def cmd_playback(args: argparse.Namespace) -> int` (L604-653)
L605-613> Esegue il test dell'endpoint '/playback' (comando 'playback'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L623> `raise CliError("Per usare playback senza --query devi passare --stream-type e --stream-id.")`
L635> `raise CliError(`
L651> `return 0 if response.status_code < 400 else 1`

### fn `def validate_manifest_payload(payload: Dict[str, Any]) -> Tuple[bool, str]` (L654-677)
L655-663> Valida il payload del manifest JSON. Args: payload (Dict[str, Any]): Il payload JSON. Returns: Tuple[bool, str]: (Valido, Messaggio di dettaglio).
L666> `return False, "manifest senza array 'resources'"`
L674> `return True, "resource stream con movie+series trovata"`
L675> `return False, "resource stream con movie+series non trovata"`

### fn `def add_check(results: List[CheckResult], name: str, ok: bool, detail: str) -> None` (L678-690)
L679-687> Aggiunge un risultato di controllo alla lista. Args: results (List[CheckResult]): Lista dei risultati. name (str): Nome del controllo. ok (bool): Esito del controllo. detail (str): Dettaglio del controllo.

### fn `def run_smoke(args: argparse.Namespace, target: TargetUrls) -> List[CheckResult]` (L691-890)
L692-701> Esegue una serie di test smoke (controllo salute di base). Args: args (argparse.Namespace): Argomenti CLI. target (TargetUrls): URL target. Returns: List[CheckResult]: Lista dei risultati dei test.

### fn `def cmd_smoke(args: argparse.Namespace) -> int` (L919-942)
L920-928> Esegue il comando 'smoke' che lancia una suite di test. Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 fallimento).
L940> `return 0 if failed == 0 else 1`

### fn `def build_parser() -> argparse.ArgumentParser` (L943-1104)
L944-949> Costruisce il parser degli argomenti della riga di comando. Returns: argparse.ArgumentParser: Il parser configurato.
L1102> `return parser`

### fn `def main() -> int` (L1105-1125)
L1106-1111> Punto di ingresso principale dello script. Returns: int: Codice di uscita da passare a sys.exit().
L1117> `return int(args.func(args))`
L1120> `return 2`
L1123> `return 2`

## Comments
- L2: CLI autonoma per testare le API HTTP esposte da Debriddo. La configurazione può arrivare da: ...
- L38: @brief Class `CliError` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- L46: Verifica che nessun modulo del package 'debriddo' sia stato caricato. Raises: ...
- L65: @brief Class `TargetUrls` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- L76: @brief Class `CheckResult` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- L86: Analizza e normalizza l'URL di configurazione fornito. Args: ...
- L135: Recupera l'URL target dagli argomenti CLI o variabili d'ambiente. Args: ...
- L163: Esegue una richiesta HTTP utilizzando la sessione fornita. Args: ...
- L188: Costruisce un URL completo combinando base URL e path. Args: ...
- L202: Tenta di parsare il corpo della risposta come JSON. Args: ...
- L222: Stampa un riepilogo della risposta HTTP su stdout. Args: ...
- L260: Esegue una chiamata a un endpoint semplice e stampa il risultato. Args: ...
- L294: Costruisce il percorso per l'endpoint di stream. Args: ...
- L313: Stampa le informazioni sul target risolto (comando 'target'). Args: ...
- L330: Esegue il test dell'endpoint root '/' (comando 'root'). Args: ...
- L352: Esegue il test dell'endpoint '/configure' (comando 'configure'). Args: ...
- L368: Esegue il test dell'endpoint '/manifest.json' (comando 'manifest'). Args: ...
- L384: Esegue il test dell'endpoint '/site.webmanifest' (comando 'site-webmanifest'). Args: ...
- L399: Esegue il test degli asset statici (comando 'asset'). Args: ...
- L439: Esegue la richiesta HTTP per ottenere lo stream. Args: ...
- L471: Esegue il test dell'endpoint '/stream' (comando 'stream'). Args: ...
- L508: Esegue una ricerca stream stampando il payload completo (comando 'search'). Args: ...
- L548: Estrae il path di playback dal payload degli stream. Args: ...
- L580: Esegue la richiesta HTTP per il playback. Args: ...
- L605: Esegue il test dell'endpoint '/playback' (comando 'playback'). Args: ...
- L655: Valida il payload del manifest JSON. Args: ...
- L679: Aggiunge un risultato di controllo alla lista. Args: ...
- L692: Esegue una serie di test smoke (controllo salute di base). Args: ...
- L920: Esegue il comando 'smoke' che lancia una suite di test. Args: ...
- L944: Costruisce il parser degli argomenti della riga di comando. Returns: ...
- L1106: Punto di ingresso principale dello script. Returns: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`DEFAULT_CONFIG_ENV`|var|pub|30||
|`DEFAULT_TIMEOUT`|var|pub|32||
|`DEBRIDDO_MODULE_PREFIX`|var|pub|34||
|`CliError`|class|pub|37-44|class CliError(Exception)|
|`ensure_no_debriddo_modules_loaded`|fn|pub|45-62|def ensure_no_debriddo_modules_loaded() -> None|
|`TargetUrls`|class|pub|64-73|class TargetUrls|
|`CheckResult`|class|pub|75-84|class CheckResult|
|`normalize_config_url`|fn|pub|85-133|def normalize_config_url(raw_value: str) -> TargetUrls|
|`get_target_from_args`|fn|pub|134-154|def get_target_from_args(args: argparse.Namespace) -> Tar...|
|`request_url`|fn|pub|155-161|def request_url(|
|`make_url`|fn|pub|187-200|def make_url(base_url: str, path: str) -> str|
|`parse_json_body`|fn|pub|201-216|def parse_json_body(response: requests.Response) -> Optio...|
|`print_response_summary`|fn|pub|217-220|def print_response_summary(|
|`call_simple_endpoint`|fn|pub|252-258|def call_simple_endpoint(|
|`build_stream_path`|fn|pub|288-292|def build_stream_path(|
|`cmd_target`|fn|pub|312-328|def cmd_target(args: argparse.Namespace) -> int|
|`cmd_root`|fn|pub|329-350|def cmd_root(args: argparse.Namespace) -> int|
|`cmd_configure`|fn|pub|351-366|def cmd_configure(args: argparse.Namespace) -> int|
|`cmd_manifest`|fn|pub|367-382|def cmd_manifest(args: argparse.Namespace) -> int|
|`cmd_site_webmanifest`|fn|pub|383-397|def cmd_site_webmanifest(args: argparse.Namespace) -> int|
|`cmd_asset`|fn|pub|398-430|def cmd_asset(args: argparse.Namespace) -> int|
|`request_stream`|fn|pub|431-437|def request_stream(|
|`cmd_stream`|fn|pub|470-506|def cmd_stream(args: argparse.Namespace) -> int|
|`cmd_search`|fn|pub|507-546|def cmd_search(args: argparse.Namespace) -> int|
|`extract_playback_path_from_streams`|fn|pub|547-572|def extract_playback_path_from_streams(streams_payload: D...|
|`request_playback`|fn|pub|573-578|def request_playback(|
|`cmd_playback`|fn|pub|604-653|def cmd_playback(args: argparse.Namespace) -> int|
|`validate_manifest_payload`|fn|pub|654-677|def validate_manifest_payload(payload: Dict[str, Any]) ->...|
|`add_check`|fn|pub|678-690|def add_check(results: List[CheckResult], name: str, ok: ...|
|`run_smoke`|fn|pub|691-890|def run_smoke(args: argparse.Namespace, target: TargetUrl...|
|`cmd_smoke`|fn|pub|919-942|def cmd_smoke(args: argparse.Namespace) -> int|
|`build_parser`|fn|pub|943-1104|def build_parser() -> argparse.ArgumentParser|
|`main`|fn|pub|1105-1125|def main() -> int|


---

# check_unused_requirements.py | Python | 130L | 3 symbols | 3 imports | 15 comments
> Path: `src/debriddo/check_unused_requirements.py`
> @file src/debriddo/check_unused_requirements.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import os
import ast
import importlib.metadata
```

## Definitions

### fn `def get_imported_modules_from_file(filepath)` (L14-41)
L15-23> Estrae i moduli importati da un file Python analizzandone l'AST. Args: filepath (str): Il percorso del file da analizzare. Returns: set: Un set di stringhe contenente i nomi dei moduli top-level importati.
L29> `return imported_modules`
L34> forziamo minuscolo
L38> forziamo minuscolo
L40> `return imported_modules`

### fn `def get_all_imported_modules(root_dir)` (L42-63)
L43-51> Scansiona ricorsivamente una directory per trovare tutti i moduli importati nei file .py. Args: root_dir (str): La directory radice da cui iniziare la scansione. Returns: set: Un set di tutti i moduli importati trovati.
L54> Ignora virtual env
L62> `return all_imports`

### fn `def get_requirements(requirements_file)` (L64-85)
L65-73> Legge un file requirements.txt e restituisce un set di pacchetti richiesti. Args: requirements_file (str): Il percorso del file requirements.txt. Returns: set: Un set di nomi di pacchetti (senza versioni).
L80> estrai il nome del pacchetto senza versione
L81> minuscolo
L84> `return packages`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L15: Estrae i moduli importati da un file Python analizzandone l'AST. Args: ...
- L43: Scansiona ricorsivamente una directory per trovare tutti i moduli importati nei file .py. Args: ...
- L54: Ignora virtual env
- L65: Legge un file requirements.txt e restituisce un set di pacchetti richiesti. Args: ...
- L80: estrai il nome del pacchetto senza versione
- L95: imported_modules ora contiene solo minuscole
- L98: required_packages ora contiene i nomi dei pacchetti in minuscolo
- L101-104: pkg_to_distributions ha una struttura: | { "bs4": ["beautifulsoup4"], "apscheduler": ["APScheduler"], ... } | Invertiamo il mapping in modo da ottenere distribution -> {top_modules}
- L117: Se non troviamo moduli top-level per questo pacchetto, supponiamo che il modulo top-level coincida con il nome del pacchetto
- L121: Controlliamo se almeno uno dei top_modules è stato importato

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_imported_modules_from_file`|fn|pub|14-41|def get_imported_modules_from_file(filepath)|
|`get_all_imported_modules`|fn|pub|42-63|def get_all_imported_modules(root_dir)|
|`get_requirements`|fn|pub|64-85|def get_requirements(requirements_file)|


---

# constants.py | Python | 27L | 6 symbols | 0 imports | 12 comments
> Path: `src/debriddo/constants.py`
> @file src/debriddo/constants.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Definitions

- var `APPLICATION_NAME = "Debriddo"` (L11) — Application name
- var `APPLICATION_VERSION = "0.0.35"` (L13) — : @brief Exported constant `APPLICATION_VERSION` used by runtime workflows.
- var `APPLICATION_DESCRIPTION = "Ricerca online i Film e le tue Serie Tv preferite."` (L15) — : @brief Exported constant `APPLICATION_DESCRIPTION` used by runtime workflows.
- var `CACHE_DATABASE_FILE = "caches_items.db"` (L19) — SQL3llite database
- var `NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/refs/heads/master/videos/nocache.mp4"` (L23) — Link per AllDebrid/Real-Debird/Premiumize che è ritornato in caso di errore
- var `RUN_IN_MULTI_THREAD = True` (L27) — Run in multi-thread
## Comments
- L7: AUTHORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`APPLICATION_NAME`|var|pub|11||
|`APPLICATION_VERSION`|var|pub|13||
|`APPLICATION_DESCRIPTION`|var|pub|15||
|`CACHE_DATABASE_FILE`|var|pub|19||
|`NO_CACHE_VIDEO_URL`|var|pub|23||
|`RUN_IN_MULTI_THREAD`|var|pub|27||


---

# alldebrid.py | Python | 247L | 10 symbols | 7 imports | 21 comments
> Path: `src/debriddo/debrid/alldebrid.py`
> @file src/debriddo/debrid/alldebrid.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
import uuid
from urllib.parse import unquote
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class AllDebrid(BaseDebrid)` : BaseDebrid (L23-222)
L212-221> @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__add_magnet_or_torrent`. @param magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. @param torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. @param ip Runtime input parameter consumed by `__add_magnet_or_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L28-39) L24> @brief Class `AllDebrid` encapsulates cohesive runtime behavior. @details Generated Doxygen block...
  L29-36> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L40-52)
  L41-49> @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_magnet`. @param magnet Runtime input parameter consumed by `add_magnet`. @param ip Runtime input parameter consumed by `add_magnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L51> `return await self.get_json_response(url)`
- fn `async def add_torrent(self, torrent_file, ip)` (L53-66)
  L54-62> @brief Execute `add_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_torrent`. @param torrent_file Runtime input parameter consumed by `add_torrent`. @param ip Runtime input parameter consumed by `add_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L65> `return await self.get_json_response(url, method='post', files=files)`
- fn `async def check_magnet_status(self, id, ip)` (L67-79)
  L68-76> @brief Execute `check_magnet_status` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `check_magnet_status`. @param id Runtime input parameter consumed by `check_magnet_status`. @param ip Runtime input parameter consumed by `check_magnet_status`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L78> `return await self.get_json_response(url)`
- fn `async def unrestrict_link(self, link, ip)` (L80-92)
  L81-89> @brief Execute `unrestrict_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `unrestrict_link`. @param link Runtime input parameter consumed by `unrestrict_link`. @param ip Runtime input parameter consumed by `unrestrict_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L91> `return await self.get_json_response(url)`
- fn `async def get_stream_link(self, query, ip=None)` (L93-180)
  L94-102> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L111-116> @brief Execute `is_ready` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L119> `return False`
  L120> `return status_response.get("data", {}).get("magnets", {}).get("status") == "Ready"`
  L124> `return NO_CACHE_VIDEO_URL`
  L130> `return NO_CACHE_VIDEO_URL`
  L133> `return NO_CACHE_VIDEO_URL`
  L159> `raise ValueError(f"Error: No matching files for {season} {episode} in torrent.")`
  L164> `raise ValueError("Error: Unsupported stream type.")`
  L167> `return link`
  L175> `raise ValueError("Error: Failed to unlock link.")`
  L179> `return unlocked_link_data["data"]["link"]`
- fn `async def is_ready()` (L110-121)
  L111-116> @brief Execute `is_ready` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L119> `return False`
  L120> `return status_response.get("data", {}).get("magnets", {}).get("status") == "Ready"`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L181-210)
  L182-190> @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_availability_bulk`. @param hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. @param ip Runtime input parameter consumed by `get_availability_bulk`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L195> `return ids`
  L200> `return ids`
  L202> if len(hashes_or_magnets) == 0:
  L203> logger.debug("No hashes to be sent to All-Debrid.")
  L204> return dict()
  L206> url = f"{self.base_url}magnet/instant?agent=debriddo&apikey={self.config['debridKey']}&magnets[]={'&magnets[]='.join(hashes_or_magnets)}&ip={ip}
  L207> logger.debug(url)
  L208> return await self.get_json_response(url)

### fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None, ip=None)` `priv` (L211-247)
L208> return await self.get_json_response(url)
L212-221> @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__add_magnet_or_torrent`. @param magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. @param torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. @param ip Runtime input parameter consumed by `__add_magnet_or_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L229> `raise ValueError("Error: Failed to add magnet.")`
L242> `raise ValueError("Error: Failed to add torrent file.")`
L247> `return torrent_id`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L29: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L41: @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L54: @brief Execute `add_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L68: @brief Execute `check_magnet_status` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoni...
- L81: @brief Execute `unrestrict_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L94: @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L111: @brief Execute `is_ready` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return...
- L182: @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...
- L202-207: if len(hashes_or_magnets) == 0: | logger.debug("No hashes to be sent to All-Debrid.") | return dict() | url = f"{self.base_url}magnet/instant?agent=debriddo&apikey={self.config['debridKey']}&magnets[]=... | logger.debug(url)
- L212: @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static rea...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`AllDebrid`|class|pub|23-222|class AllDebrid(BaseDebrid)|
|`AllDebrid.__init__`|fn|priv|28-39|def __init__(self, config)|
|`AllDebrid.add_magnet`|fn|pub|40-52|async def add_magnet(self, magnet, ip=None)|
|`AllDebrid.add_torrent`|fn|pub|53-66|async def add_torrent(self, torrent_file, ip)|
|`AllDebrid.check_magnet_status`|fn|pub|67-79|async def check_magnet_status(self, id, ip)|
|`AllDebrid.unrestrict_link`|fn|pub|80-92|async def unrestrict_link(self, link, ip)|
|`AllDebrid.get_stream_link`|fn|pub|93-180|async def get_stream_link(self, query, ip=None)|
|`AllDebrid.is_ready`|fn|pub|110-121|async def is_ready()|
|`AllDebrid.get_availability_bulk`|fn|pub|181-210|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`__add_magnet_or_torrent`|fn|priv|211-247|async def __add_magnet_or_torrent(self, magnet, torrent_d...|


---

# base_debrid.py | Python | 148L | 9 symbols | 5 imports | 15 comments
> Path: `src/debriddo/debrid/base_debrid.py`
> @file src/debriddo/debrid/base_debrid.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
import asyncio
import httpx
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class BaseDebrid` (L18-148)
- fn `def __init__(self, config)` `priv` (L23-34) L19> @brief Class `BaseDebrid` encapsulates cohesive runtime behavior. @details Generated Doxygen bloc...
  L24-31> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def wait_for_ready_status_async_func(self, check_status_func, timeout=30, interval=5)` (L35-56)
  L36-45> @brief Execute `wait_for_ready_status_async_func` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `wait_for_ready_status_async_func`. @param check_status_func Runtime input parameter consumed by `wait_for_ready_status_async_func`. @param timeout Runtime input parameter consumed by `wait_for_ready_status_async_func`. @param interval Runtime input parameter consumed by `wait_for_ready_status_async_func`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L49> Se check_status_func è asincrona, uso `await check_status_func()`.
  L52> `return True`
  L55> `return False`
- fn `async def wait_for_ready_status_sync_func(self, check_status_func, timeout=30, interval=5)` (L57-79)
  L58-67> @brief Execute `wait_for_ready_status_sync_func` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `wait_for_ready_status_sync_func`. @param check_status_func Runtime input parameter consumed by `wait_for_ready_status_sync_func`. @param timeout Runtime input parameter consumed by `wait_for_ready_status_sync_func`. @param interval Runtime input parameter consumed by `wait_for_ready_status_sync_func`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L71> Se check_status_func è sincrona, la chiamiamo direttamente.
  L74> `return True`
  L77> `return False`
- fn `async def get_json_response(self, url, **kwargs)` (L80-94)
  L81-89> @brief Execute `get_json_response` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_json_response`. @param url Runtime input parameter consumed by `get_json_response`. @param **kwargs Runtime input parameter consumed by `get_json_response`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L90> Usa il client asincrono
  L93> `return ret`
- fn `async def download_torrent_file(self, download_url)` (L95-109)
  L96-103> @brief Execute `download_torrent_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent_file`. @param download_url Runtime input parameter consumed by `download_torrent_file`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L104> Usa il client asincrono
  L107> `return ret`
- fn `async def get_stream_link(self, query, ip=None)` (L110-122)
  L111-119> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L120> `raise NotImplementedError`
- fn `async def add_magnet(self, magnet, ip=None)` (L123-135)
  L124-132> @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_magnet`. @param magnet Runtime input parameter consumed by `add_magnet`. @param ip Runtime input parameter consumed by `add_magnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L133> `raise NotImplementedError`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L136-148)
  L137-145> @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_availability_bulk`. @param hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. @param ip Runtime input parameter consumed by `get_availability_bulk`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L146> `raise NotImplementedError`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L24: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L36: @brief Execute `wait_for_ready_status_async_func` operational logic. @details Generated Doxygen block describing callable contract for LLM-native s...
- L49: Se check_status_func è asincrona, uso `await check_status_func()`.
- L58: @brief Execute `wait_for_ready_status_sync_func` operational logic. @details Generated Doxygen block describing callable contract for LLM-native st...
- L71: Se check_status_func è sincrona, la chiamiamo direttamente.
- L81: @brief Execute `get_json_response` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning...
- L96: @brief Execute `download_torrent_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...
- L111: @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L124: @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L137: @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BaseDebrid`|class|pub|18-148|class BaseDebrid|
|`BaseDebrid.__init__`|fn|priv|23-34|def __init__(self, config)|
|`BaseDebrid.wait_for_ready_status_async_func`|fn|pub|35-56|async def wait_for_ready_status_async_func(self, check_st...|
|`BaseDebrid.wait_for_ready_status_sync_func`|fn|pub|57-79|async def wait_for_ready_status_sync_func(self, check_sta...|
|`BaseDebrid.get_json_response`|fn|pub|80-94|async def get_json_response(self, url, **kwargs)|
|`BaseDebrid.download_torrent_file`|fn|pub|95-109|async def download_torrent_file(self, download_url)|
|`BaseDebrid.get_stream_link`|fn|pub|110-122|async def get_stream_link(self, query, ip=None)|
|`BaseDebrid.add_magnet`|fn|pub|123-135|async def add_magnet(self, magnet, ip=None)|
|`BaseDebrid.get_availability_bulk`|fn|pub|136-148|async def get_availability_bulk(self, hashes_or_magnets, ...|


---

# get_debrid_service.py | Python | 39L | 1 symbols | 5 imports | 5 comments
> Path: `src/debriddo/debrid/get_debrid_service.py`
> @file src/debriddo/debrid/get_debrid_service.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from fastapi.exceptions import HTTPException
from debriddo.debrid.alldebrid import AllDebrid
from debriddo.debrid.premiumize import Premiumize
from debriddo.debrid.realdebrid import RealDebrid
from debriddo.debrid.torbox import TorBox
```

## Definitions

### fn `def get_debrid_service(config)` (L19-39)
L20-26> @brief Execute `get_debrid_service` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param config Runtime input parameter consumed by `get_debrid_service`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L37> `raise HTTPException(status_code=500, detail="Invalid service configuration.")`
L39> `return debrid_service`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L20: @brief Execute `get_debrid_service` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasonin...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_debrid_service`|fn|pub|19-39|def get_debrid_service(config)|


---

# premiumize.py | Python | 221L | 10 symbols | 5 imports | 18 comments
> Path: `src/debriddo/debrid/premiumize.py`
> @file src/debriddo/debrid/premiumize.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import get_info_hash_from_magnet, season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class Premiumize(BaseDebrid)` : BaseDebrid (L22-221)
- fn `def __init__(self, config)` `priv` (L27-38) L23> @brief Class `Premiumize` encapsulates cohesive runtime behavior. @details Generated Doxygen bloc...
  L28-35> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L39-52)
  L40-48> @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_magnet`. @param magnet Runtime input parameter consumed by `add_magnet`. @param ip Runtime input parameter consumed by `add_magnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L51> `return await self.get_json_response(url, method='post', data=form)`
- fn `async def add_torrent(self, torrent_file)` (L54-66) L53> Doesn't work for the time being. Premiumize does not support torrent file torrents
  L55-62> @brief Execute `add_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_torrent`. @param torrent_file Runtime input parameter consumed by `add_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L65> `return await self.get_json_response(url, method='post', data=form)`
- fn `async def list_transfers(self)` (L67-77)
  L68-74> @brief Execute `list_transfers` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `list_transfers`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L76> `return await self.get_json_response(url)`
- fn `async def get_folder_or_file_details(self, item_id, is_folder=True)` (L78-95)
  L79-87> @brief Execute `get_folder_or_file_details` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_folder_or_file_details`. @param item_id Runtime input parameter consumed by `get_folder_or_file_details`. @param is_folder Runtime input parameter consumed by `get_folder_or_file_details`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L94> `return await self.get_json_response(url)`
- fn `async def get_availability(self, hash)` (L96-107)
  L97-104> @brief Execute `get_availability` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_availability`. @param hash Runtime input parameter consumed by `get_availability`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L106> `return await self.get_json_response(url)`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L108-121)
  L109-117> @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_availability_bulk`. @param hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. @param ip Runtime input parameter consumed by `get_availability_bulk`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L120> `return await self.get_json_response(url)`
- fn `async def get_stream_link(self, query, ip=None)` (L122-221)
  L123-131> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L142> `raise ValueError("Error: Failed to create transfer.")`
  L147-152> @brief Execute `is_ready` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L155> `return False`
  L157> `return isinstance(transcoded, list) and len(transcoded) > 0 and bool(transcoded[0])`
  L161> `return NO_CACHE_VIDEO_URL`
  L165> Assuming the transfer is complete, we need to find whether it's a file or a folder
  L179> `raise ValueError("Error: Transfer completed but no item ID found.")`
  L186> For movies, we pick the largest file in the folder or the file itself
  L190> `raise ValueError("Error: Empty Premiumize folder content.")`
  L208> `raise ValueError(f"Error: No matching files for {season} {episode} in torrent.")`
  L215> `raise ValueError("Error: Unsupported stream type.")`
  L218> `raise ValueError("Error: No Premiumize link found.")`
  L221> `return link`
- fn `async def is_ready()` (L146-158)
  L147-152> @brief Execute `is_ready` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L155> `return False`
  L157> `return isinstance(transcoded, list) and len(transcoded) > 0 and bool(transcoded[0])`

## Comments
- L7-11: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri | Assuming the BaseDebrid class and necessary imports are already defined as shown previously
- L28: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L40: @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L55: @brief Execute `add_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L68: @brief Execute `list_transfers` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @...
- L79: @brief Execute `get_folder_or_file_details` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static ...
- L97: @brief Execute `get_availability` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L109: @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...
- L123: @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L147: @brief Execute `is_ready` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return...
- L165: Assuming the transfer is complete, we need to find whether it's a file or a folder
- L186: For movies, we pick the largest file in the folder or the file itself

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Premiumize`|class|pub|22-221|class Premiumize(BaseDebrid)|
|`Premiumize.__init__`|fn|priv|27-38|def __init__(self, config)|
|`Premiumize.add_magnet`|fn|pub|39-52|async def add_magnet(self, magnet, ip=None)|
|`Premiumize.add_torrent`|fn|pub|54-66|async def add_torrent(self, torrent_file)|
|`Premiumize.list_transfers`|fn|pub|67-77|async def list_transfers(self)|
|`Premiumize.get_folder_or_file_details`|fn|pub|78-95|async def get_folder_or_file_details(self, item_id, is_fo...|
|`Premiumize.get_availability`|fn|pub|96-107|async def get_availability(self, hash)|
|`Premiumize.get_availability_bulk`|fn|pub|108-121|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`Premiumize.get_stream_link`|fn|pub|122-221|async def get_stream_link(self, query, ip=None)|
|`Premiumize.is_ready`|fn|pub|146-158|async def is_ready()|


---

# realdebrid.py | Python | 496L | 19 symbols | 10 imports | 40 comments
> Path: `src/debriddo/debrid/realdebrid.py`
> @file src/debriddo/debrid/realdebrid.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
import time
import asyncio
from urllib.parse import unquote
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import get_info_hash_from_magnet
from debriddo.utils.general import is_video_file
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class RealDebrid(BaseDebrid)` : BaseDebrid (L26-225)
L196-204> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L224> `raise ValueError("Error: Unsupported stream type.")`
- fn `def __init__(self, config)` `priv` (L31-43) L27> @brief Class `RealDebrid` encapsulates cohesive runtime behavior. @details Generated Doxygen bloc...
  L32-39> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L44-57)
  L45-53> @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_magnet`. @param magnet Runtime input parameter consumed by `add_magnet`. @param ip Runtime input parameter consumed by `add_magnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L56> `return await self.get_json_response(url, method='post', headers=self.headers, data=data)`
- fn `async def add_torrent(self, torrent_file)` (L58-69)
  L59-66> @brief Execute `add_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_torrent`. @param torrent_file Runtime input parameter consumed by `add_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L68> `return await self.get_json_response(url, method='put', headers=self.headers, data=torrent_file)`
- fn `async def delete_torrent(self, id)` (L70-81)
  L71-78> @brief Execute `delete_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `delete_torrent`. @param id Runtime input parameter consumed by `delete_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L80> `return await self.get_json_response(url, method='delete', headers=self.headers)`
- fn `async def get_torrent_info(self, torrent_id)` (L82-100)
  L83-90> @brief Execute `get_torrent_info` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_torrent_info`. @param torrent_id Runtime input parameter consumed by `get_torrent_info`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L96> `return None`
  L98> `return torrent_info`
  L99> `return None`
- fn `async def select_files(self, torrent_id, file_id)` (L101-117)
  L102-110> @brief Execute `select_files` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `select_files`. @param torrent_id Runtime input parameter consumed by `select_files`. @param file_id Runtime input parameter consumed by `select_files`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L114> TODO verificare perché è stato sostituito dalla get_json_response che tanto non ritorna nulla!
  L115> self.request_post(url, headers=self.headers, data=data)
- fn `async def unrestrict_link(self, link)` (L118-130) L115> self.request_post(url, headers=self.headers, data=data)
  L119-126> @brief Execute `unrestrict_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `unrestrict_link`. @param link Runtime input parameter consumed by `unrestrict_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L129> `return await self.get_json_response(url, method='post', headers=self.headers, data=data)`
- fn `async def is_already_added(self, magnet)` (L131-148)
  L132-139> @brief Execute `is_already_added` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `is_already_added`. @param magnet Runtime input parameter consumed by `is_already_added`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L146> `return torrent['id']`
  L147> `return False`
- fn `async def wait_for_link(self, torrent_id, timeout=30, interval=2)` (L149-168)
  L150-159> @brief Execute `wait_for_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `wait_for_link`. @param torrent_id Runtime input parameter consumed by `wait_for_link`. @param timeout Runtime input parameter consumed by `wait_for_link`. @param interval Runtime input parameter consumed by `wait_for_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L164> `return torrent_info['links']`
  L167> `return None`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L169-194)
  L170-178> @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_availability_bulk`. @param hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. @param ip Runtime input parameter consumed by `get_availability_bulk`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L181> `return dict()`
  L183> TODO: verificare che cazzo fa sta cosa
  L188> `return dict()`
  L193> `return await self.get_json_response(url, headers=self.headers)`

### fn `async def get_stream_link(self, query, ip=None)` (L195-264)
L196-204> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L224> `raise ValueError("Error: Unsupported stream type.")`
L226> The torrent is not yet added
L230> `raise ValueError("Error: Failed to get torrent info.")`
L235> == operator, to avoid adding the season pack twice and setting 5 as season pack treshold
L245> Waiting for the link(s) to be ready
L248> `return NO_CACHE_VIDEO_URL`
L257> Unrestricting the download link
L260> `raise ValueError("Error: Failed to unrestrict link.")`
L263> `return unrestrict_response['download']`

### fn `async def __get_cached_torrent_ids(self, info_hash)` `priv` (L265-285)
L266-273> @brief Execute `__get_cached_torrent_ids` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__get_cached_torrent_ids`. @param info_hash Runtime input parameter consumed by `__get_cached_torrent_ids`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L283> `return torrent_ids`
L284> `return []`

### fn `async def __get_cached_torrent_info(self, cached_ids, file_index, season, episode)` `priv` (L286-313)
L287-297> @brief Execute `__get_cached_torrent_info` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__get_cached_torrent_info`. @param cached_ids Runtime input parameter consumed by `__get_cached_torrent_info`. @param file_index Runtime input parameter consumed by `__get_cached_torrent_info`. @param season Runtime input parameter consumed by `__get_cached_torrent_info`. @param episode Runtime input parameter consumed by `__get_cached_torrent_info`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L304> If the links are ready
L305> `return cached_torrent_info`
L310> `return None`
L312> `return max(cached_torrents, key=lambda x: x['progress'])`

### fn `def __torrent_contains_file(self, torrent_info, file_index, season, episode)` `priv` (L314-339)
L315-325> @brief Execute `__torrent_contains_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__torrent_contains_file`. @param torrent_info Runtime input parameter consumed by `__torrent_contains_file`. @param file_index Runtime input parameter consumed by `__torrent_contains_file`. @param season Runtime input parameter consumed by `__torrent_contains_file`. @param episode Runtime input parameter consumed by `__torrent_contains_file`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L327> `return False`
L332> `return True`
L336> `return file["selected"] == 1`
L338> `return False`

### fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None)` `priv` (L340-378)
L341-349> @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__add_magnet_or_torrent`. @param magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. @param torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L358> `raise ValueError("Error: Failed to add magnet.")`
L372> `raise ValueError("Error: Failed to add torrent file.")`
L377> `return await self.get_torrent_info(torrent_id)`

### fn `async def __prefetch_season_pack(self, magnet, torrent_download, timeout=30, interval=2)` `priv` (L379-407)
L380-390> @brief Execute `__prefetch_season_pack` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__prefetch_season_pack`. @param magnet Runtime input parameter consumed by `__prefetch_season_pack`. @param torrent_download Runtime input parameter consumed by `__prefetch_season_pack`. @param timeout Runtime input parameter consumed by `__prefetch_season_pack`. @param interval Runtime input parameter consumed by `__prefetch_season_pack`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L393> `return None`
L402> TODO: da testare bene
L403> await asyncio.sleep(10)
L406> `return await self.get_torrent_info(torrent_info["id"])`

### fn `async def __select_file(self, torrent_info, stream_type, file_index, season, episode)` `priv` (L408-451)
L409-420> @brief Execute `__select_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__select_file`. @param torrent_info Runtime input parameter consumed by `__select_file`. @param stream_type Runtime input parameter consumed by `__select_file`. @param file_index Runtime input parameter consumed by `__select_file`. @param season Runtime input parameter consumed by `__select_file`. @param episode Runtime input parameter consumed by `__select_file`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L425> `return`
L438> if season_episode_in_filename(file["path"], season, episode, strict=True):
L439> strict_matching_files.append(file)
L440> elif season_episode_in_filename(file["path"], season, episode, strict=False):
L441> matching_files.append(file)
L447> `raise ValueError("Error: No matching file found in torrent.")`

### fn `def __find_appropiate_link(self, torrent_info, links, file_index, season, episode)` `priv` (L452-496)
L453-464> @brief Execute `__find_appropiate_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__find_appropiate_link`. @param torrent_info Runtime input parameter consumed by `__find_appropiate_link`. @param links Runtime input parameter consumed by `__find_appropiate_link`. @param file_index Runtime input parameter consumed by `__find_appropiate_link`. @param season Runtime input parameter consumed by `__find_appropiate_link`. @param episode Runtime input parameter consumed by `__find_appropiate_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L479> if season_episode_in_filename(file["path"], season, episode, strict=True):
L480> strict_matching_indexes.append({"index": index, "file": file})
L481> elif season_episode_in_filename(file["path"], season, episode, strict=False):
L482> matching_indexes.append({"index": index, "file": file})
L489> `return NO_CACHE_VIDEO_URL`
L494> `return NO_CACHE_VIDEO_URL`
L496> `return links[index]`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L32: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L45: @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L59: @brief Execute `add_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L71: @brief Execute `delete_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @...
- L83: @brief Execute `get_torrent_info` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L102: @brief Execute `select_files` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @pa...
- L114: TODO verificare perché è stato sostituito dalla get_json_response che tanto non ritorna nulla!
- L119: @brief Execute `unrestrict_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L132: @brief Execute `is_already_added` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L150: @brief Execute `wait_for_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...
- L170: @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...
- L183: TODO: verificare che cazzo fa sta cosa
- L196: @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L226: The torrent is not yet added
- L235: == operator, to avoid adding the season pack twice and setting 5 as season pack treshold
- L245: Waiting for the link(s) to be ready
- L257: Unrestricting the download link
- L266: @brief Execute `__get_cached_torrent_ids` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static re...
- L287: @brief Execute `__get_cached_torrent_info` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static r...
- L315: @brief Execute `__torrent_contains_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static rea...
- L341: @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static rea...
- L380: @brief Execute `__prefetch_season_pack` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L402-403: TODO: da testare bene | await asyncio.sleep(10)
- L409: @brief Execute `__select_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...
- L438-441: if season_episode_in_filename(file["path"], season, episode, strict=True): | strict_matching_files.append(file) | elif season_episode_in_filename(file["path"], season, episode, strict=False): | matching_files.append(file)
- L453: @brief Execute `__find_appropiate_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L479-482: if season_episode_in_filename(file["path"], season, episode, strict=True): | strict_matching_indexes.append({"index": index, "file": file}) | elif season_episode_in_filename(file["path"], season, episode, strict=False): | matching_indexes.append({"index": index, "file": file})

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`RealDebrid`|class|pub|26-225|class RealDebrid(BaseDebrid)|
|`RealDebrid.__init__`|fn|priv|31-43|def __init__(self, config)|
|`RealDebrid.add_magnet`|fn|pub|44-57|async def add_magnet(self, magnet, ip=None)|
|`RealDebrid.add_torrent`|fn|pub|58-69|async def add_torrent(self, torrent_file)|
|`RealDebrid.delete_torrent`|fn|pub|70-81|async def delete_torrent(self, id)|
|`RealDebrid.get_torrent_info`|fn|pub|82-100|async def get_torrent_info(self, torrent_id)|
|`RealDebrid.select_files`|fn|pub|101-117|async def select_files(self, torrent_id, file_id)|
|`RealDebrid.unrestrict_link`|fn|pub|118-130|async def unrestrict_link(self, link)|
|`RealDebrid.is_already_added`|fn|pub|131-148|async def is_already_added(self, magnet)|
|`RealDebrid.wait_for_link`|fn|pub|149-168|async def wait_for_link(self, torrent_id, timeout=30, int...|
|`RealDebrid.get_availability_bulk`|fn|pub|169-194|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`get_stream_link`|fn|pub|195-264|async def get_stream_link(self, query, ip=None)|
|`__get_cached_torrent_ids`|fn|priv|265-285|async def __get_cached_torrent_ids(self, info_hash)|
|`__get_cached_torrent_info`|fn|priv|286-313|async def __get_cached_torrent_info(self, cached_ids, fil...|
|`__torrent_contains_file`|fn|priv|314-339|def __torrent_contains_file(self, torrent_info, file_inde...|
|`__add_magnet_or_torrent`|fn|priv|340-378|async def __add_magnet_or_torrent(self, magnet, torrent_d...|
|`__prefetch_season_pack`|fn|priv|379-407|async def __prefetch_season_pack(self, magnet, torrent_do...|
|`__select_file`|fn|priv|408-451|async def __select_file(self, torrent_info, stream_type, ...|
|`__find_appropiate_link`|fn|priv|452-496|def __find_appropiate_link(self, torrent_info, links, fil...|


---

# torbox.py | Python | 277L | 9 symbols | 8 imports | 26 comments
> Path: `src/debriddo/debrid/torbox.py`
> @file src/debriddo/debrid/torbox.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
import time
import asyncio
from urllib.parse import unquote
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TorBox(BaseDebrid)` : BaseDebrid (L24-223)
L165-173> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L182> `return NO_CACHE_VIDEO_URL`
L187> `return NO_CACHE_VIDEO_URL`
L196> `return NO_CACHE_VIDEO_URL`
L200> `return NO_CACHE_VIDEO_URL`
L205> `return NO_CACHE_VIDEO_URL`
L211> `return await self.get_file_download_link(torrent_id, largest_file_index)`
L222> `return await self.get_file_download_link(torrent_id, selected_index)`
- fn `def __init__(self, config)` `priv` (L29-43) L25> @brief Class `TorBox` encapsulates cohesive runtime behavior. @details Generated Doxygen block fo...
  L30-37> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def wait_for_files(self, torrent_hash, timeout=30, interval=5)` (L44-69)
  L45-54> @brief Execute `wait_for_files` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `wait_for_files`. @param torrent_hash Runtime input parameter consumed by `wait_for_files`. @param timeout Runtime input parameter consumed by `wait_for_files`. @param interval Runtime input parameter consumed by `wait_for_files`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L64> `return files`
  L68> `return None`
- fn `async def add_magnet(self, magnet, ip=None)` (L70-106)
  L71-79> @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `add_magnet`. @param magnet Runtime input parameter consumed by `add_magnet`. @param ip Runtime input parameter consumed by `add_magnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L95> `return None`
  L97> `return {`
  L105> `return None`
- fn `async def check_magnet_status(self, torrent_hash)` (L107-125)
  L108-115> @brief Execute `check_magnet_status` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `check_magnet_status`. @param torrent_hash Runtime input parameter consumed by `check_magnet_status`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L121> `return response["data"] if response["data"] else []`
  L124> `return None`
- fn `async def get_file_download_link(self, torrent_id, file_name)` (L126-144)
  L127-135> @brief Execute `get_file_download_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_file_download_link`. @param torrent_id Runtime input parameter consumed by `get_file_download_link`. @param file_name Runtime input parameter consumed by `get_file_download_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L140> `return response["data"]`
  L143> `return None`
- fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None)` `priv` (L145-163)
  L146-154> @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__add_magnet_or_torrent`. @param magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. @param torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L162> `return torrent_id`

### fn `async def get_stream_link(self, query, ip=None)` (L164-229)
L165-173> @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_stream_link`. @param query Runtime input parameter consumed by `get_stream_link`. @param ip Runtime input parameter consumed by `get_stream_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L182> `return NO_CACHE_VIDEO_URL`
L187> `return NO_CACHE_VIDEO_URL`
L196> `return NO_CACHE_VIDEO_URL`
L200> `return NO_CACHE_VIDEO_URL`
L205> `return NO_CACHE_VIDEO_URL`
L211> `return await self.get_file_download_link(torrent_id, largest_file_index)`
L222> `return await self.get_file_download_link(torrent_id, selected_index)`
L225> `return NO_CACHE_VIDEO_URL`
L228> `raise ValueError("Error: Unsupported stream type.")`

### fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L245-277)
L242> logger.error(f"HTTP request failed: {e}")
L247-255> @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_availability_bulk`. @param hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. @param ip Runtime input parameter consumed by `get_availability_bulk`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L277> `return available_torrents`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L30: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L45: @brief Execute `wait_for_files` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @...
- L71: @brief Execute `add_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L108: @brief Execute `check_magnet_status` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoni...
- L127: @brief Execute `get_file_download_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L146: @brief Execute `__add_magnet_or_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static rea...
- L165: @brief Execute `get_stream_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L230-241: def get_json_response(self, url, method='get', **kwargs): | try: | if method == 'get': | response = requests.request_get(url, headers=self.headers, **kwargs) | elif method == 'post': | response = requests.request_post(url, headers=self.headers, **kwargs) | else: | raise ValueError(f"Unsupported HTTP method: {method}") | response.raise_for_status() | return response.json() | except requests.exceptions.RequestException as e:
- L247: @brief Execute `get_availability_bulk` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorBox`|class|pub|24-223|class TorBox(BaseDebrid)|
|`TorBox.__init__`|fn|priv|29-43|def __init__(self, config)|
|`TorBox.wait_for_files`|fn|pub|44-69|async def wait_for_files(self, torrent_hash, timeout=30, ...|
|`TorBox.add_magnet`|fn|pub|70-106|async def add_magnet(self, magnet, ip=None)|
|`TorBox.check_magnet_status`|fn|pub|107-125|async def check_magnet_status(self, torrent_hash)|
|`TorBox.get_file_download_link`|fn|pub|126-144|async def get_file_download_link(self, torrent_id, file_n...|
|`TorBox.__add_magnet_or_torrent`|fn|priv|145-163|async def __add_magnet_or_torrent(self, magnet, torrent_d...|
|`get_stream_link`|fn|pub|164-229|async def get_stream_link(self, query, ip=None)|
|`get_availability_bulk`|fn|pub|245-277|async def get_availability_bulk(self, hashes_or_magnets, ...|


---

# main.py | Python | 769L | 23 symbols | 36 imports | 96 comments
> Path: `src/debriddo/main.py`
> @file src/debriddo/main.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import os
import sys
import re
import shutil
import time
import zipfile
import uvicorn
import json
from pathlib import Path
import starlette.status as status
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import asyncio
from concurrent.futures import ThreadPoolExecutor
from starlette.responses import FileResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager
from debriddo.debrid.get_debrid_service import get_debrid_service
from debriddo.search.search_result import SearchResult
from debriddo.search.search_service import SearchService
from debriddo.metdata.cinemeta import Cinemeta
from debriddo.metdata.tmdb import TMDB
from debriddo.torrent.torrent_service import TorrentService
from debriddo.torrent.torrent_smart_container import TorrentSmartContainer
from debriddo.utils.cache import search_cache
from debriddo.utils.filter_results import filter_items, sort_items
from debriddo.utils.logger import setup_logger
from debriddo.utils.parse_config import parse_config, parse_query
from debriddo.utils.stremio_parser import parse_to_stremio_streams
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.web.pages import get_index
from debriddo.constants import APPLICATION_NAME, APPLICATION_VERSION, APPLICATION_DESCRIPTION
```

## Definitions

- var `APP_DIR = Path(__file__).resolve().parent` (L60) — : @brief Exported constant `APP_DIR` used by runtime workflows.
- var `WEB_DIR = APP_DIR / "web"` (L62) — : @brief Exported constant `WEB_DIR` used by runtime workflows.
### fn `def calculate_optimal_thread_count()` (L109-126)
L108> calcola il numero ottimale di thread
L110-116> Calcola il numero ottimale di thread basato sui core della CPU. Formula: (N CPU Cores * 2) + 1. Returns: int: Il numero ottimale di thread.
L117> Ottieni il numero di core della CPU
L120> `raise RuntimeError("os.cpu_count() non ha restituito un valore valido")`
L122> Calcola il numero ottimale di threads
L124> `return optimal_num_threads`

### fn `def resolve_thread_count()` (L127-154)
L128-133> Risolve il numero di thread da utilizzare basandosi sulle variabili d'ambiente. Returns: int: Il numero di thread risolto.
L136> `return resolve_auto_thread_count()`
L140> `return resolve_auto_thread_count()`
L146> `return 1`
L150> `return 1`
L152> `return n_threads`

### fn `def resolve_auto_thread_count()` (L155-168)
L156-161> Risolve automaticamente il numero di thread calcolandolo. Returns: int: Il numero di thread calcolato o 1 in caso di errore.
L163> `return calculate_optimal_thread_count()`
L166> `return 1`

### fn `def get_or_create_event_loop()` (L169-183)
L170-175> Ottiene il loop di eventi corrente o ne crea uno nuovo se non esiste. Returns: asyncio.AbstractEventLoop: Il loop di eventi.
L177> `return asyncio.get_event_loop()`
L181> `return loop`

### fn `async def lifespan(app: FastAPI)` `@asynccontextmanager` (L186-214)
L184> Lifespan: gestisce startup e shutdown
L187-195> Gestisce il ciclo di vita dell'applicazione (avvio e arresto). Args: app (FastAPI): L'istanza dell'applicazione FastAPI. Yields: None: Controllo restituito all'applicazione.
L197> Il check dell'update ogni 60 secondi
L201> Verifica se il server Uvicorn è configurato con reload
L208> `yield` — Qui puoi mettere codice che deve girare durante la vita dell'app
L210> terminazione

### class `class LogFilterMiddleware` (L226-283)
L225> Aggiunge il loggin del middleware fastapi
- fn `def __init__(self, app)` `priv` (L230-238) L227> Middleware per il filtraggio e il logging delle richieste.
  L231-236> Inizializza il middleware. Args: app (ASGIApp): L'applicazione ASGI successiva.
- fn `async def __call__(self, scope, receive, send)` `priv` (L239-283) L231> Inizializza il middleware. Args: ...
  L240-250> Gestisce la richiesta in ingresso. Args: scope (dict): Lo scope della connessione. receive (callable): Funzione per ricevere messaggi. send (callable): Funzione per inviare messaggi. Returns: None: Il risultato dell'invocazione dell'app successiva.
  L251> Gestisci solo richieste HTTP,
  L252> la classe Request di Starlette è progettata solo per gestire richieste HTTP,
  L253> quindi non può essere utilizzata con eventi "lifespan" (es. avvio e arresto).
  L255> `return await self.app(scope, receive, send)`
  L258> Log informazioni sulla richiesta
  L263> GET - /C_<CONFIG>/config
  L266> GET - /playback/C_<CONFIG>/Q_<QUERY>
  L271> Log body della richiesta (se presente)
  L275> Chiamata all'applicazione
  L280> `raise HTTPException(status_code=500, detail="An error occurred while processing the request.")`
  L282> `return response`

### fn `async def root()` `@app.get("/")` (L307-315)
L305> root:
L308-313> Gestisce la root path reindirizzando alla pagina di configurazione. Returns: RedirectResponse: Redirect alla configurazione.
L314> `return RedirectResponse(url="/configure")`

### fn `async def get_favicon()` `@app.get("/favicon.ico")` (L318-327)
L316> favicon.ico
L319-324> Restituisce l'icona favicon. Returns: FileResponse: Il file favicon.ico.
L326> `return response`

### fn `async def get_config_js()` `@app.get("/{config}/config.js")` (L331-340)
L328> config.js
L332-337> Restituisce il file javascript di configurazione. Returns: FileResponse: Il file config.js.
L339> `return response`

### fn `async def get_lz_string_js()` `@app.get("/{config}/lz-string.min.js")` (L344-353)
L341> lz-string.min.js
L345-350> Restituisce la libreria lz-string minimizzata. Returns: FileResponse: Il file lz-string.min.js.
L352> `return response`

### fn `async def get_styles_css()` `@app.get("/{config}/styles.css")` (L357-366)
L354> styles.css
L358-363> Restituisce il foglio di stile CSS. Returns: FileResponse: Il file styles.css.
L365> `return response`

### fn `async def configure()` `@app.get("/{config}/configure", response_class=HTMLResponse)` (L371-379)
L368> ?/configure
L372-377> Restituisce la pagina HTML di configurazione. Returns: HTMLResponse: La pagina HTML generata.
L378> `return get_index(app_name, app_version, app_environment)`

### fn `async def function(file_path: str)` `@app.get("/{config}/images/{file_path:path}")` (L383-395)
L380> imges/?
L384-392> Serve le immagini statiche dalla directory images. Args: file_path (str): Il percorso relativo del file immagine. Returns: FileResponse: Il file immagine richiesto.
L394> `return response`

### fn `async def get_webmanifest()` `@app.get("/site.webmanifest", response_class=HTMLResponse)` (L398-434)
L396> site.webmanifest
L399-404> Genera e restituisce il web manifest per l'applicazione. Returns: JSONResponse: Il contenuto del manifest in formato JSON.
L430> `return JSONResponse(`
L432> Specifica il Content-Type corretto

### fn `async def get_manifest()` `@app.get("/{params}/manifest.json")` (L439-520)
L436> ?/manifest.json
L440-445> Restituisce il manifest di Stremio. Returns: JSONResponse: Il manifest in formato JSON.
L467> TODO: da implementare (volendo)
L468> fornisce come catalogo la lista dei file su Real-Debird
L469> catalogs": [
L470> {
L471> id": app_name_lc + "-realdebrid",
L472> name": "RealDebrid",
L473> type": "other",
L474> extra": [
L475> {
L476> name": "skip
L477> }
L478> ]
L479> }
L480> ],
L516> `return JSONResponse(`
L518> Specifica il Content-Type corretto

### fn `async def get_results(config_url: str, stream_type: str, stream_id: str, request: Request)` `@app.get("/{config_url}/stream/{stream_type}/{stream_id}")` (L523-635)
L521> ?/stream/?/?
L524-535> Gestisce la richiesta di stream per un determinato media. Args: config_url (str): La configurazione codificata. stream_type (str): Il tipo di stream (movie o series). stream_id (str): L'ID del media (es. IMDB ID). request (Request): La richiesta HTTP originale. Returns: JSONResponse: La lista degli stream disponibili.
L548> `return Response(`
L574> se la cache non ritorna abbastanza risultati
L619> TODO: Maybe add an if to only save to cache if caching is enabled?
L633> `return {"streams": stream_list}`

### fn `async def head_playback(config: str, query: str, request: Request)` `@app.head("/playback/{config_url}/{query}")` (L638-655)
L636> playback/?/?
L639-649> Gestisce la richiesta HEAD per il playback (check di validità). Args: config (str): La configurazione codificata. query (str): La query string codificata. request (Request): La richiesta HTTP originale. Returns: Response: Risposta con status code.
L651> `raise HTTPException(status_code=400, detail="Query required.")`
L652> Qui potrei limitarmi a controllare la validità di config e query
L653> e restituire comunque lo stesso set di header (es: un redirect) senza generare effettivamente la destinazione.
L654> `return Response(status_code=status.HTTP_200_OK)`

### fn `async def get_playback(config_url: str, query_string: str, request: Request)` `@app.get("/playback/{config_url}/{query_string}")` (L658-693)
L656> playback/?/?
L659-669> Gestisce il playback e restituisce il link di streaming (redirect). Args: config_url (str): La configurazione codificata. query_string (str): La query string codificata. request (Request): La richiesta HTTP originale. Returns: RedirectResponse: Redirect al link di streaming finale.
L672> `raise HTTPException(status_code=400, detail="Query required.")`
L675> decodifica la query
L678> logger.debug(f"Decoded <QUERY>: {query}")
L686> `raise HTTPException(status_code=500, detail="Unable to get stream link.")`
L687> `return RedirectResponse(url=link, status_code=status.HTTP_301_MOVED_PERMANENTLY)`
L691> `raise HTTPException(status_code=500, detail="An error occurred while processing the request.")`

### fn `async def update_app()` (L698-763)
L695> # self update ###
L699-707> Verifica e applica aggiornamenti automatici dell'applicazione. Se l'applicazione è avviata con --reload e non in modalità sviluppo, controlla GitHub Releases e aggiorna il codice. Returns: None
L709> senza --reload non gestisce l'upgrade, --reload implica --workers 1
L711> `return`
L713> in modalità sviluppo non fa l'upgrade
L715> `return`
L718> Usa il client asincrono
L723> `return`
L731> `return`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L65: load .env
- L69: get environment variables
- L86: define common string
- L96: logger
- L100: application start
- L104: verifica se è in reload
- L110-117: Calcola il numero ottimale di thread basato sui core della CPU. Formula: (N CPU Cores * 2) + 1. ... | Ottieni il numero di core della CPU
- L122: Calcola il numero ottimale di threads
- L128: Risolve il numero di thread da utilizzare basandosi sulle variabili d'ambiente. Returns: ...
- L156: Risolve automaticamente il numero di thread calcolandolo. Returns: ...
- L170: Ottiene il loop di eventi corrente o ne crea uno nuovo se non esiste. Returns: ...
- L187: Gestisce il ciclo di vita dell'applicazione (avvio e arresto). Args: ...
- L201: Verifica se il server Uvicorn è configurato con reload
- L210: terminazione
- L215: Creazione dell'app FastAPI
- L218: Imposta un maggior numero di thread, per esempio 16
- L240-253: Gestisce la richiesta in ingresso. Args: ... | Gestisci solo richieste HTTP, | la classe Request di Starlette è progettata solo per gestire richieste HTTP, | quindi non può essere utilizzata con eventi "lifespan" (es. avvio e arresto).
- L258: Log informazioni sulla richiesta
- L263: GET - /C_<CONFIG>/config
- L266: GET - /playback/C_<CONFIG>/Q_<QUERY>
- L271: Log body della richiesta (se presente)
- L275: Chiamata all'applicazione
- L288: Abilita CORSMiddleware per le chiamate OPTIONS e il redirect
- L300-302: ############## | # Fast API ### | ##############
- L308: Gestisce la root path reindirizzando alla pagina di configurazione. Returns: ...
- L319: Restituisce l'icona favicon. Returns: ...
- L332: Restituisce il file javascript di configurazione. Returns: ...
- L345: Restituisce la libreria lz-string minimizzata. Returns: ...
- L358: Restituisce il foglio di stile CSS. Returns: ...
- L367: configure
- L372: Restituisce la pagina HTML di configurazione. Returns: ...
- L384: Serve le immagini statiche dalla directory images. Args: ...
- L399: Genera e restituisce il web manifest per l'applicazione. Returns: ...
- L435: manifest.json
- L440: Restituisce il manifest di Stremio. Returns: ...
- L467-480: TODO: da implementare (volendo) | fornisce come catalogo la lista dei file su Real-Debird | catalogs": [ | { | id": app_name_lc + "-realdebrid", | name": "RealDebrid", | type": "other", | extra": [ | { | name": "skip | } | ] | } | ],
- L524: Gestisce la richiesta di stream per un determinato media. Args: ...
- L574: se la cache non ritorna abbastanza risultati
- L619: TODO: Maybe add an if to only save to cache if caching is enabled?
- L639: Gestisce la richiesta HEAD per il playback (check di validità). Args: ...
- L652-653: Qui potrei limitarmi a controllare la validità di config e query | e restituire comunque lo stesso set di header (es: un redirect) senza generare effettivamente la ...
- L659: Gestisce il playback e restituisce il link di streaming (redirect). Args: ...
- L675: decodifica la query
- L678: logger.debug(f"Decoded <QUERY>: {query}")
- L694: #################
- L699-709: Verifica e applica aggiornamenti automatici dell'applicazione. Se l'applicazione è avviata con --... | senza --reload non gestisce l'upgrade, --reload implica --workers 1
- L713: in modalità sviluppo non fa l'upgrade
- L764-766: ########## | # MAIN ### | ##########

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`APP_DIR`|var|pub|60||
|`WEB_DIR`|var|pub|62||
|`calculate_optimal_thread_count`|fn|pub|109-126|def calculate_optimal_thread_count()|
|`resolve_thread_count`|fn|pub|127-154|def resolve_thread_count()|
|`resolve_auto_thread_count`|fn|pub|155-168|def resolve_auto_thread_count()|
|`get_or_create_event_loop`|fn|pub|169-183|def get_or_create_event_loop()|
|`lifespan`|fn|pub|186-214|async def lifespan(app: FastAPI)|
|`LogFilterMiddleware`|class|pub|226-283|class LogFilterMiddleware|
|`LogFilterMiddleware.__init__`|fn|priv|230-238|def __init__(self, app)|
|`LogFilterMiddleware.__call__`|fn|priv|239-283|async def __call__(self, scope, receive, send)|
|`root`|fn|pub|307-315|async def root()|
|`get_favicon`|fn|pub|318-327|async def get_favicon()|
|`get_config_js`|fn|pub|331-340|async def get_config_js()|
|`get_lz_string_js`|fn|pub|344-353|async def get_lz_string_js()|
|`get_styles_css`|fn|pub|357-366|async def get_styles_css()|
|`configure`|fn|pub|371-379|async def configure()|
|`function`|fn|pub|383-395|async def function(file_path: str)|
|`get_webmanifest`|fn|pub|398-434|async def get_webmanifest()|
|`get_manifest`|fn|pub|439-520|async def get_manifest()|
|`get_results`|fn|pub|523-635|async def get_results(config_url: str, stream_type: str, ...|
|`head_playback`|fn|pub|638-655|async def head_playback(config: str, query: str, request:...|
|`get_playback`|fn|pub|658-693|async def get_playback(config_url: str, query_string: str...|
|`update_app`|fn|pub|698-763|async def update_app()|


---

# cinemeta.py | Python | 62L | 2 symbols | 4 imports | 6 comments
> Path: `src/debriddo/metdata/cinemeta.py`
> @file src/debriddo/metdata/cinemeta.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class Cinemeta(MetadataProvider)` : MetadataProvider (L17-62)
- fn `async def get_metadata(self, id, type)` (L23-62) L19> @brief Class `Cinemeta` encapsulates cohesive runtime behavior. @details Generated Doxygen block ...
  L24-32> @brief Execute `get_metadata` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_metadata`. @param id Runtime input parameter consumed by `get_metadata`. @param type Runtime input parameter consumed by `get_metadata`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L38> Usa il client asincrono
  L61> `return result`
  L62> `return None`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L24: @brief Execute `get_metadata` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @pa...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Cinemeta`|class|pub|17-62|class Cinemeta(MetadataProvider)|
|`Cinemeta.get_metadata`|fn|pub|23-62|async def get_metadata(self, id, type)|


---

# metadata_provider_base.py | Python | 74L | 4 symbols | 1 imports | 8 comments
> Path: `src/debriddo/metdata/metadata_provider_base.py`
> @file src/debriddo/metdata/metadata_provider_base.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring ag...

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class MetadataProvider` (L13-74)
- fn `def __init__(self, config)` `priv` (L19-31) L15> @brief Class `MetadataProvider` encapsulates cohesive runtime behavior. @details Generated Doxyge...
  L20-27> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def replace_weird_characters(self, string)` (L32-63)
  L33-40> @brief Execute `replace_weird_characters` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `replace_weird_characters`. @param string Runtime input parameter consumed by `replace_weird_characters`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L62> `return string`
- fn `async def get_metadata(self, id, type)` (L64-74)
  L65-73> @brief Execute `get_metadata` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_metadata`. @param id Runtime input parameter consumed by `get_metadata`. @param type Runtime input parameter consumed by `get_metadata`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L74> `raise NotImplementedError`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L20: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L33: @brief Execute `replace_weird_characters` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static re...
- L65: @brief Execute `get_metadata` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @pa...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MetadataProvider`|class|pub|13-74|class MetadataProvider|
|`MetadataProvider.__init__`|fn|priv|19-31|def __init__(self, config)|
|`MetadataProvider.replace_weird_characters`|fn|pub|32-63|def replace_weird_characters(self, string)|
|`MetadataProvider.get_metadata`|fn|pub|64-74|async def get_metadata(self, id, type)|


---

# tmdb.py | Python | 74L | 2 symbols | 6 imports | 6 comments
> Path: `src/debriddo/metdata/tmdb.py`
> @file src/debriddo/metdata/tmdb.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.media import Media
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class TMDB(MetadataProvider)` : MetadataProvider (L18-74)
- fn `async def get_metadata(self, id, type)` (L24-74) L20> @brief Class `TMDB` encapsulates cohesive runtime behavior. @details Generated Doxygen block for ...
  L25-33> @brief Execute `get_metadata` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_metadata`. @param id Runtime input parameter consumed by `get_metadata`. @param type Runtime input parameter consumed by `get_metadata`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L43> Usa il client asincrono
  L74> `return result`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L25: @brief Execute `get_metadata` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @pa...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TMDB`|class|pub|18-74|class TMDB(MetadataProvider)|
|`TMDB.get_metadata`|fn|pub|24-74|async def get_metadata(self, id, type)|


---

# media.py | Python | 28L | 2 symbols | 0 imports | 6 comments
> Path: `src/debriddo/models/media.py`
> @file src/debriddo/models/media.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Definitions

### class `class Media` (L11-28)
L8> AUTHORS: aymene69
- fn `def __init__(self, id, titles, languages, type)` `priv` (L15-28) L12> Rappresenta un media generico (film o serie TV).
  L16-24> Inizializza un oggetto Media. Args: id (str): L'identificatore del media (es. IMDB ID). titles (list): Lista dei titoli associati. languages (list): Lista delle lingue. type (str): Il tipo di media ('movie' o 'series').

## Comments
- L7: VERSION: 0.0.35
- L16: Inizializza un oggetto Media. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Media`|class|pub|11-28|class Media|
|`Media.__init__`|fn|priv|15-28|def __init__(self, id, titles, languages, type)|


---

# movie.py | Python | 28L | 2 symbols | 1 imports | 6 comments
> Path: `src/debriddo/models/movie.py`
> @file src/debriddo/models/movie.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.models.media import Media
```

## Definitions

### class `class Movie(Media)` : Media (L13-28)
- fn `def __init__(self, id, titles, year, languages)` `priv` (L17-28) L14> Rappresenta un film.
  L18-26> Inizializza un oggetto Movie. Args: id (str): L'identificatore del film. titles (list): Lista dei titoli. year (str|int): L'anno di uscita. languages (list): Lista delle lingue.

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L18: Inizializza un oggetto Movie. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Movie`|class|pub|13-28|class Movie(Media)|
|`Movie.__init__`|fn|priv|17-28|def __init__(self, id, titles, year, languages)|


---

# series.py | Python | 31L | 2 symbols | 1 imports | 6 comments
> Path: `src/debriddo/models/series.py`
> @file src/debriddo/models/series.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.models.media import Media
```

## Definitions

### class `class Series(Media)` : Media (L13-31)
- fn `def __init__(self, id, titles, season, episode, languages)` `priv` (L17-31) L14> Rappresenta un episodio di una serie TV.
  L18-27> Inizializza un oggetto Series. Args: id (str): L'identificatore della serie. titles (list): Lista dei titoli. season (str): Identificatore della stagione (es. S01). episode (str): Identificatore dell'episodio (es. E01). languages (list): Lista delle lingue.

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L18: Inizializza un oggetto Series. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Series`|class|pub|13-31|class Series(Media)|
|`Series.__init__`|fn|priv|17-31|def __init__(self, id, titles, season, episode, languages)|


---

# base_plugin.py | Python | 61L | 5 symbols | 1 imports | 8 comments
> Path: `src/debriddo/search/plugins/base_plugin.py`
> @file src/debriddo/search/plugins/base_plugin.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class BasePlugin` (L12-61)
- fn `def __init__(self, config)` `priv` (L17-28) L13> @brief Class `BasePlugin` encapsulates cohesive runtime behavior. @details Generated Doxygen bloc...
  L18-25> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def login(self, session=None) -> bool | None` (L29-39)
  L30-37> @brief Execute `login` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `login`. @param session Runtime input parameter consumed by `login`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L40-51) L30> @brief Execute `login` operational logic. @details Generated Doxygen block describing callable co...
  L41-49> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L50> `raise NotImplementedError`
- fn `async def download_torrent(self, info)` (L52-61) L41> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable c...
  L53-60> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L61> `raise NotImplementedError`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L18: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L53: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BasePlugin`|class|pub|12-61|class BasePlugin|
|`BasePlugin.__init__`|fn|priv|17-28|def __init__(self, config)|
|`BasePlugin.login`|fn|pub|29-39|async def login(self, session=None) -> bool | None|
|`BasePlugin.search`|fn|pub|40-51|async def search(self, what, cat='all')|
|`BasePlugin.download_torrent`|fn|pub|52-61|async def download_torrent(self, info)|


---

# ilcorsaroblu.py | Python | 347L | 7 symbols | 7 imports | 35 comments
> Path: `src/debriddo/search/plugins/ilcorsaroblu.py`
> @file src/debriddo/search/plugins/ilcorsaroblu.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
from urllib.parse import quote
```

## Definitions

### class `class ilcorsaroblu(BasePlugin)` : BasePlugin (L18-217)
L19-22> @brief Class `ilcorsaroblu` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L28> uncomment appropriate lines to include TPB category in qBittorrent search category
L29> currently set to include only HD video for "movies" & "tv
L34> Parodie
L35> DVD-R (DVD5 & DVD9)
L36> 1080p
L37> 720p
L38> 3D
L39> BDRip-mkv-h264
L40> Movies - Films
L41> 4K-UltraHD
L42> Anime
L43> Cartoons
L44> Documentari
L45> Films (TNT Village)
L46> Sport / Gare
L47> Commedia
L48> BDRip-mkv-h264-TNT
L52> Fumetti
L53> Pdf
L54> eBooks
L55> Romanzi
L56> Edicola: Giornali/Quotidiani
L60> Games -> Console
L61> Games -> Xbox360
L62> Retro Games
L63> Games -> Nintendo
L64> Games -> PC
L68> Audio -> Mp3
L69> Radio Trasmissioni
L70> Audio / Music
L74> Archive
L76> but not games
L78> Windows
L79> Linux
L80> Macintosh-Apple
L81> Student's Office
L82> Android
L83> iOS / iPhone
L87> TV Show 1080p
L88> TV Show 720p
L89> TV Show Standard
L90> TV Show (TNT Village)
L94> Disegni e Modelli
L95> Other
L96> Adult
L100> V.I.P.
L101> Premium
L198-205> @brief Execute `login` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `login`. @param session Runtime input parameter consumed by `login`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L207> `return False`
L208> Esegui il login
L214> Verifica se il login è stato effettuato correttamente
- fn `def __init__(self, config)` `priv` (L123-138)
  L124-131> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L133> Dati del form di autenticazione
- fn `async def __extract_info_hash(self, html_content, suffix_to_remove=" - il CorSaRo Blu")` `priv` (L139-168)
  L140-145> Estrae l'info hash da un contenuto HTML. :param html_content: stringa contenente il contenuto HTML :return: lista di info hash trovati (può essere vuota se non ce ne sono)
  L148> Trova name
  L153> Rimuovi il suffisso, se presente
  L157> Trova il primo input con name="info_hash
  L165> `return info_hash, name`
  L167> `return None`
- fn `async def __generate_magnet_link(self, info_hash, name=None, tracker_urls=None)` `priv` (L169-196)
  L170-177> Genera un magnet link dato un info hash, un nome e (opzionalmente) una lista di tracker URLs. :param info_hash: stringa contenente l'info hash (SHA-1) del torrent :param name: stringa contenente il nome descrittivo del torrent (opzionale) :param tracker_urls: lista di URL dei tracker opzionali (default: None) :return: stringa con il magnet link generato
  L178> Base del magnet link con l'info hash
  L181> Aggiungi il nome se fornito
  L183> Codifica il nome per essere compatibile con URL
  L188> Aggiungi i tracker se forniti
  L190> Aggiungi ogni tracker al magnet link
  L194> `return base_magnet`

### fn `async def login(self, session=None)` (L197-225)
L198-205> @brief Execute `login` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `login`. @param session Runtime input parameter consumed by `login`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L207> `return False`
L208> Esegui il login
L214> Verifica se il login è stato effettuato correttamente
L218> `return True`
L223> `return False`

### fn `async def download_torrent(self,info)` (L226-262)
L228-235> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L236> Usa il client asincrono
L238> login
L241> `return None`
L245> Esegui la ricerca
L256> `return magnet_link`
L261> `return None`

### fn `async def search(self,what,cat='all')` (L263-347)
L264-272> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L273> Usa il client asincrono
L275> login
L278> `return None`
L288> TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
L291> URL e parametri per la ricerca
L294> Esegui la ricerca
L299> Parsing della risposta HTML
L302> Identifica righe della tabella con classe "lista
L304> Identifica righe della tabella con classe "lista
L306> Estrai i dati desiderati
L309> scarta l'intestazione
L311> Assicura che ci siano abbastanza colonne
L321> non usati
L322> Data": date,
L323> C": completed,
L336> Stampa i risultati
L339> salta l'intestazione
L347> `return prettyPrinter.get()`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L19: @brief Class `ilcorsaroblu` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundar...
- L28-29: uncomment appropriate lines to include TPB category in qBittorrent search category | currently set to include only HD video for "movies" & "tv
- L124-133: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable... | Dati del form di autenticazione
- L140: Estrae l'info hash da un contenuto HTML. :param html_content: stringa contenente il contenuto HTML ...
- L148: Trova name
- L153: Rimuovi il suffisso, se presente
- L157: Trova il primo input con name="info_hash
- L170-178: Genera un magnet link dato un info hash, un nome e (opzionalmente) una lista di tracker URLs. :pa... | Base del magnet link con l'info hash
- L181-183: Aggiungi il nome se fornito | Codifica il nome per essere compatibile con URL
- L188-190: Aggiungi i tracker se forniti | Aggiungi ogni tracker al magnet link
- L198: @brief Execute `login` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param sel...
- L208: Esegui il login
- L214: Verifica se il login è stato effettuato correttamente
- L228: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L238: login
- L245: Esegui la ricerca
- L264: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L275: login
- L288: TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
- L291: URL e parametri per la ricerca
- L294: Esegui la ricerca
- L299: Parsing della risposta HTML
- L306: Estrai i dati desiderati
- L321-323: non usati | Data": date, | C": completed,
- L336: Stampa i risultati

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ilcorsaroblu`|class|pub|18-217|class ilcorsaroblu(BasePlugin)|
|`ilcorsaroblu.__init__`|fn|priv|123-138|def __init__(self, config)|
|`ilcorsaroblu.__extract_info_hash`|fn|priv|139-168|async def __extract_info_hash(self, html_content, suffix_...|
|`ilcorsaroblu.__generate_magnet_link`|fn|priv|169-196|async def __generate_magnet_link(self, info_hash, name=No...|
|`login`|fn|pub|197-225|async def login(self, session=None)|
|`download_torrent`|fn|pub|226-262|async def download_torrent(self,info)|
|`search`|fn|pub|263-347|async def search(self,what,cat='all')|


---

# ilcorsaronero.py | Python | 165L | 7 symbols | 6 imports | 16 comments
> Path: `src/debriddo/search/plugins/ilcorsaronero.py`
> @file src/debriddo/search/plugins/ilcorsaronero.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
from urllib.parse import quote_plus
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class ilcorsaronero(BasePlugin)` : BasePlugin (L19-165)
L20-23> @brief Class `ilcorsaronero` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L39-42> @brief Class `HTMLParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L44-51> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L56-63> @brief Execute `feed` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `feed`. @param html Runtime input parameter consumed by `feed`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L68> `return`
L83-90> @brief Execute `__findTorrents` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__findTorrents`. @param html Runtime input parameter consumed by `__findTorrents`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L92> Find all TR nodes with class odd or odd2
L94> Skip the first TR node because it's the header
L95> Extract from the A node all the needed information
L110> `return torrents`
- fn `async def download_torrent(self, info)` (L112-135)
  L113-120> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L121> Usa il client asincrono
  L129> `return(str(magnet_str + " " + magnet_str))`
  L132> `raise Exception('Error, please fill a bug report!')`
  L134> `return None`
- fn `async def search(self, what, cat='all')` (L136-165)
  L137-145> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L146> Usa il client asincrono
  L151> filter = '&cat={0}'.format(self.supported_categories[cat])
  L153> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L156> Some replacements to format the html source
  L165> `return prettyPrinter.get()`

### class `class HTMLParser` (L37-111)
- fn `def __init__(self, url)` `priv` (L43-54) L39> @brief Class `HTMLParser` encapsulates cohesive runtime behavior. @details Generated Doxygen bloc...
  L44-51> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def feed(self, html)` (L55-81)
  L56-63> @brief Execute `feed` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `feed`. @param html Runtime input parameter consumed by `feed`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L68> `return`
- fn `def __findTorrents(self, html)` `priv` (L82-111)
  L83-90> @brief Execute `__findTorrents` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__findTorrents`. @param html Runtime input parameter consumed by `__findTorrents`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L92> Find all TR nodes with class odd or odd2
  L94> Skip the first TR node because it's the header
  L95> Extract from the A node all the needed information
  L110> `return torrents`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: LightDestory (https://github.com/LightDestory) | CONTRIBUTORS: Ogekuri
- L20: @brief Class `ilcorsaronero` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension bounda...
- L44: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L56: @brief Execute `feed` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self...
- L83-92: @brief Execute `__findTorrents` operational logic. @details Generated Doxygen block describing ca... | Find all TR nodes with class odd or odd2
- L95: Extract from the A node all the needed information
- L113: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L137: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L151-153: filter = '&cat={0}'.format(self.supported_categories[cat]) | TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
- L156: Some replacements to format the html source

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ilcorsaronero`|class|pub|19-165|class ilcorsaronero(BasePlugin)|
|`HTMLParser`|class|pub|37-111|class HTMLParser|
|`HTMLParser.__init__`|fn|priv|43-54|def __init__(self, url)|
|`HTMLParser.feed`|fn|pub|55-81|def feed(self, html)|
|`HTMLParser.__findTorrents`|fn|priv|82-111|def __findTorrents(self, html)|
|`ilcorsaronero.download_torrent`|fn|pub|112-135|async def download_torrent(self, info)|
|`ilcorsaronero.search`|fn|pub|136-165|async def search(self, what, cat='all')|


---

# limetorrents.py | Python | 225L | 9 symbols | 9 imports | 18 comments
> Path: `src/debriddo/search/plugins/limetorrents.py`
> @file src/debriddo/search/plugins/limetorrents.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
from datetime import datetime, timedelta
from html.parser import HTMLParser
from urllib.parse import quote
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
import ssl
```

## Definitions

### class `class limetorrents(BasePlugin)` : BasePlugin (L26-225)
L27-30> @brief Class `limetorrents` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L44> Sub-class for parsing results
L47-54> @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `error`. @param message Runtime input parameter consumed by `error`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L60-67> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L70> dict for found item
L75> key's name in current_item dict
L90-98> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L104> `return`
L106> noqa
L111> `return`
L131-138> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L154-161> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L173-196)
  L174-181> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L182> Usa il client asincrono
  L183> since limetorrents provides torrent links in itorrent (cloudflare protected),
  L184> we have to fetch the info page and extract the magnet link
  L190> `return(str(magnet_match.groups()[0] + " " + info))`
  L193> `raise Exception('Error, please fill a bug report!')`
  L195> `return None`
- fn `async def search(self, what, cat='all')` (L197-225)
  L198-206> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L207> Usa il client asincrono
  L208> Performs search
  L214> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L225> `return prettyPrinter.get()`

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L43-172)
- fn `def error(self, message)` (L46-56) L44> Sub-class for parsing results
  L47-54> @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `error`. @param message Runtime input parameter consumed by `error`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L59-88)
  L60-67> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L70> dict for found item
  L75> key's name in current_item dict
- fn `def handle_starttag(self, tag, attrs)` (L89-129)
  L90-98> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L104> `return`
  L106> noqa
  L111> `return`
- fn `def handle_data(self, data)` (L130-152)
  L131-138> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L153-172)
  L154-161> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: Lima66 | CONTRIBUTORS: Ogekuri, Diego de las Heras (ngosang@hotmail.es)
- L21: Fix invalid certificate in Windows
- L27: @brief Class `limetorrents` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundar...
- L47: @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param sel...
- L60: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L90: @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L131: @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L154: @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...
- L174-184: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing ... | since limetorrents provides torrent links in itorrent (cloudflare protected), | we have to fetch the info page and extract the magnet link
- L198-208: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable c... | Performs search
- L214: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`limetorrents`|class|pub|26-225|class limetorrents(BasePlugin)|
|`MyHtmlParser`|class|pub|43-172|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|46-56|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|59-88|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|89-129|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|130-152|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|153-172|def handle_endtag(self, tag)|
|`limetorrents.download_torrent`|fn|pub|173-196|async def download_torrent(self, info)|
|`limetorrents.search`|fn|pub|197-225|async def search(self, what, cat='all')|


---

# one337x.py | Python | 231L | 9 symbols | 7 imports | 42 comments
> Path: `src/debriddo/search/plugins/one337x.py`
> @file src/debriddo/search/plugins/one337x.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
from urllib.parse import quote_plus
from html.parser import HTMLParser
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class one337x(BasePlugin)` : BasePlugin (L39-231)
L40-43> @brief Class `one337x` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L60-63> @brief Class `MyHtmlParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L65-72> @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `error`. @param message Runtime input parameter consumed by `error`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L78-85> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L101-109> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L113> `return`
L116> `return`
L119> `return`
L126> `return`
L130> `return`
L134> fix non scarico subito il file
L135> torrent_page = retrieve_url(link)
L136> magnet_regex = r'href="magnet:.
L137> matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE)
L138> magnet_urls = [x.group() for x in matches]
L139> self.row['link'] = magnet_urls[0].split('"')[1]
L140> self.row['engine_url'] = self.url
L141> self.row['desc_link'] = link
L147-154> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L162-169> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L176> `return`
- fn `async def download_torrent(self, info)` (L180-202)
  L181-188> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L189> Usa il client asincrono
  L190> fix le info dopo
  L199> `return(str(magnet))`
  L201> `return None`
- fn `async def search(self, what, cat='all')` (L203-231)
  L204-212> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L213> Usa il client asincrono
  L219> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L226> exists on every page but the last
  L231> `return prettyPrinter.get()`

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L58-179)
- fn `def error(self, message)` (L64-74) L60> @brief Class `MyHtmlParser` encapsulates cohesive runtime behavior. @details Generated Doxygen bl...
  L65-72> @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `error`. @param message Runtime input parameter consumed by `error`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L77-99)
  L78-85> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L100-145)
  L101-109> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L113> `return`
  L116> `return`
  L119> `return`
  L126> `return`
  L130> `return`
  L134> fix non scarico subito il file
  L135> torrent_page = retrieve_url(link)
  L136> magnet_regex = r'href="magnet:.
  L137> matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE)
  L138> magnet_urls = [x.group() for x in matches]
  L139> self.row['link'] = magnet_urls[0].split('"')[1]
  L140> self.row['engine_url'] = self.url
  L141> self.row['desc_link'] = link
- fn `def handle_data(self, data)` (L146-160)
  L147-154> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L161-179)
  L162-169> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L176> `return`

## Comments
- L7-28: VERSION: 0.0.35 | AUTHORS: sa3dany, Alyetama, BurningMop, scadams | CONTRIBUTORS: Ogekuri | LICENSING INFORMATION | Permission is hereby granted, free of charge, to any person obtaining a copy | of this software and associated documentation files (the "Software"), to deal | in the Software without restriction, including without limitation the rights | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell | copies of the Software, and to permit persons to whom the Software is | furnished to do so, subject to the following conditions: | The above copyright notice and this permission notice shall be included in | all copies or substantial portions of the Software. | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE | SOFTWARE.
- L40: @brief Class `one337x` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- L65: @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param sel...
- L78: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L101: @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L134-141: fix non scarico subito il file | torrent_page = retrieve_url(link) | magnet_regex = r'href="magnet:. | matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE) | magnet_urls = [x.group() for x in matches] | self.row['link'] = magnet_urls[0].split('"')[1] | self.row['engine_url'] = self.url | self.row['desc_link'] = link
- L147: @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L162: @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...
- L181-190: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing ... | fix le info dopo
- L204: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L219: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
- L226: exists on every page but the last

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`one337x`|class|pub|39-231|class one337x(BasePlugin)|
|`MyHtmlParser`|class|pub|58-179|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|64-74|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|77-99|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|100-145|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|146-160|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|161-179|def handle_endtag(self, tag)|
|`one337x.download_torrent`|fn|pub|180-202|async def download_torrent(self, info)|
|`one337x.search`|fn|pub|203-231|async def search(self, what, cat='all')|


---

# thepiratebay_categories.py | Python | 188L | 4 symbols | 7 imports | 18 comments
> Path: `src/debriddo/search/plugins/thepiratebay_categories.py`
> @file src/debriddo/search/plugins/thepiratebay_categories.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refact...

## Imports
```
import urllib.parse
import json
from urllib.parse import quote
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class thepiratebay(BasePlugin)` : BasePlugin (L21-53)
L22-25> @brief Class `thepiratebay` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L32> uncomment appropriate lines to include TPB category in qBittorrent search category
L33> currently set to include only HD video for "movies" & "tv
L38> Video > HD - Movies
L39> Video > HD - TV shows
L40> Video > Movies
L41> Video > Movies DVDR
L42> Video > TV shows
L43> Video > Handheld
L44> Video > 3D
L45> Video > Other
L46> Porn > Movies
L47> Porn > Movies DVDR
L48> Porn > HD - Movies
L49> Porn > Other			!!! comma after each number...
L50> Other > Other			!!! ...except the last!

### fn `async def download_torrent(self,info)` (L111-139)
L112-119> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L120> Usa il client asincrono
L130> `return(str(self.magnet.format(hash		=data['info_hash'],`
L136> `raise Exception('Error in "'+self.name+'" search plugin, download_torrent()')`
L138> `return None`

### fn `async def search(self,what,cat='all')` (L140-167)
L141-149> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L150> Usa il client asincrono
L154> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
L157> fix risulati nulli
L166> `return prettyPrinter.get()`

### fn `def parseJSON(self,collection)` (L168-188)
L169-176> @brief Execute `parseJSON` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `parseJSON`. @param collection Runtime input parameter consumed by `parseJSON`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: Scare! (https://Scare.ca/dl/qBittorrent/) | CONTRIBUTORS: Ogekuri, LightDestory https://github.com/LightDestory
- L22: @brief Class `thepiratebay` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundar...
- L32-33: uncomment appropriate lines to include TPB category in qBittorrent search category | currently set to include only HD video for "movies" & "tv
- L54: 102,	# Audio > Audio books
- L65-67: 201,	# Video > Movies | 202,	# Video > Movies DVDR | 209,	# Video > 3D
- L72: 203,	# Video > Music videos
- L88: 205,	# Video > TV shows
- L112: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L141: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L154: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
- L157: fix risulati nulli
- L169: @brief Execute `parseJSON` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`thepiratebay`|class|pub|21-53|class thepiratebay(BasePlugin)|
|`download_torrent`|fn|pub|111-139|async def download_torrent(self,info)|
|`search`|fn|pub|140-167|async def search(self,what,cat='all')|
|`parseJSON`|fn|pub|168-188|def parseJSON(self,collection)|


---

# therarbg.py | Python | 301L | 11 symbols | 7 imports | 38 comments
> Path: `src/debriddo/search/plugins/therarbg.py`
> @file src/debriddo/search/plugins/therarbg.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
from urllib.parse import quote
from html.parser import HTMLParser
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class therarbg(BasePlugin)` : BasePlugin (L40-239)
L41-44> @brief Class `therarbg` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L66-69> @brief Class `MyHtmlParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L71-78> @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `error`. @param message Runtime input parameter consumed by `error`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L84-91> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L113-121> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L146> torrent_page = await session.retrieve_url(link)
L147> matches = re.finditer(self.magnet_regex, torrent_page, re.MULTILINE)
L148> magnet_urls = [x.group() for x in matches]
L149> self.row['link'] = magnet_urls[0].split('"')[1]
L165-172> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L195-202> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L215-236)
  L216-223> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L224> Usa il client asincrono
  L231> `return str(magnet_urls[0].split('"')[1])`
  L235> `return None`

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L64-214)
- fn `def error(self, message)` (L70-80) L66> @brief Class `MyHtmlParser` encapsulates cohesive runtime behavior. @details Generated Doxygen bl...
  L71-78> @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `error`. @param message Runtime input parameter consumed by `error`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L83-111)
  L84-91> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L112-163)
  L113-121> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L146> torrent_page = await session.retrieve_url(link)
  L147> matches = re.finditer(self.magnet_regex, torrent_page, re.MULTILINE)
  L148> magnet_urls = [x.group() for x in matches]
  L149> self.row['link'] = magnet_urls[0].split('"')[1]
- fn `def handle_data(self, data)` (L164-193)
  L165-172> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L194-214)
  L195-202> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def getPageUrl(self, what, cat, page)` (L237-252)
L238-247> @brief Execute `getPageUrl` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `getPageUrl`. @param what Runtime input parameter consumed by `getPageUrl`. @param cat Runtime input parameter consumed by `getPageUrl`. @param page Runtime input parameter consumed by `getPageUrl`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L249> `return f'{self.url}/get-posts/order:-se:category:{cat}:keywords:{what}/?page={page}'`
L251> `return f'{self.url}/get-posts/order:-se:keywords:{what}/?page={page}'`

### fn `async def page_search(self, session, page, what, cat)` (L253-278)
L254-264> @brief Execute `page_search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `page_search`. @param session Runtime input parameter consumed by `page_search`. @param page Runtime input parameter consumed by `page_search`. @param what Runtime input parameter consumed by `page_search`. @param cat Runtime input parameter consumed by `page_search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def search(self, what, cat = 'all')` (L279-301)
L280-288> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L289> Usa il client asincrono
L295> TODO: leggere prima il numero di pagine e poi mandare le richieste in modo asincrono
L301> `return prettyPrinter.get()`

## Comments
- L7-28: VERSION: 0.0.35 | AUTHORS: BurningMop (burning.mop@yandex.com) | CONTRIBUTORS: Ogekuri | LICENSING INFORMATION | Permission is hereby granted, free of charge, to any person obtaining a copy | of this software and associated documentation files (the "Software"), to deal | in the Software without restriction, including without limitation the rights | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell | copies of the Software, and to permit persons to whom the Software is | furnished to do so, subject to the following conditions: | The above copyright notice and this permission notice shall be included in | all copies or substantial portions of the Software. | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE | SOFTWARE.
- L41: @brief Class `therarbg` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- L71: @brief Execute `error` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param sel...
- L84: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L113: @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L146-149: torrent_page = await session.retrieve_url(link) | matches = re.finditer(self.magnet_regex, torrent_page, re.MULTILINE) | magnet_urls = [x.group() for x in matches] | self.row['link'] = magnet_urls[0].split('"')[1]
- L165: @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L195: @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...
- L216: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L238: @brief Execute `getPageUrl` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L254: @brief Execute `page_search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L280: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L295: TODO: leggere prima il numero di pagine e poi mandare le richieste in modo asincrono

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`therarbg`|class|pub|40-239|class therarbg(BasePlugin)|
|`MyHtmlParser`|class|pub|64-214|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|70-80|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|83-111|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|112-163|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|164-193|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|194-214|def handle_endtag(self, tag)|
|`therarbg.download_torrent`|fn|pub|215-236|async def download_torrent(self, info)|
|`getPageUrl`|fn|pub|237-252|def getPageUrl(self, what, cat, page)|
|`page_search`|fn|pub|253-278|async def page_search(self, session, page, what, cat)|
|`search`|fn|pub|279-301|async def search(self, what, cat = 'all')|


---

# torrentgalaxyone.py | Python | 144L | 3 symbols | 6 imports | 18 comments
> Path: `src/debriddo/search/plugins/torrentgalaxyone.py`
> @file src/debriddo/search/plugins/torrentgalaxyone.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring a...

## Imports
```
from bs4 import BeautifulSoup
from urllib.parse import quote
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class torrentgalaxy(BasePlugin)` : BasePlugin (L19-144)
L20-23> @brief Class `torrentgalaxy` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L28> debug=True
L30> uncomment appropriate lines to include TPB category in qBittorrent search category
L31> currently set to include only HD video for "movies" & "tv
- fn `async def download_torrent(self,info)` (L48-77)
  L49-56> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L57> Usa il client asincrono
  L59> Esegui la ricerca
  L64> Parsing della risposta HTML
  L67> Trova la prima tabella
  L71> `return magnet_link`
  L76> `return None`
- fn `async def search(self,what,cat='all')` (L78-144)
  L79-87> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L88> Usa il client asincrono
  L94> TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
  L97> URL e parametri per la ricerca
  L100> Esegui la ricerca
  L105> Parsing della risposta HTML
  L108> Trova la prima tabella
  L110> Trova la prima tabella
  L113> 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF
  L114> - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf
  L115> - /get-posts/keywords:tt14257582
  L119> Divide per "/" e converte in interi
  L133> Stampa i risultati
  L136> salta l'intestazione
  L144> `return prettyPrinter.get()`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L20: @brief Class `torrentgalaxy` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension bounda...
- L30-31: uncomment appropriate lines to include TPB category in qBittorrent search category | currently set to include only HD video for "movies" & "tv
- L49: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....
- L59: Esegui la ricerca
- L64: Parsing della risposta HTML
- L79: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L94: TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
- L97: URL e parametri per la ricerca
- L100: Esegui la ricerca
- L105: Parsing della risposta HTML
- L113-115: 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF | - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf | - /get-posts/keywords:tt14257582
- L133: Stampa i risultati

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentgalaxy`|class|pub|19-144|class torrentgalaxy(BasePlugin)|
|`torrentgalaxy.download_torrent`|fn|pub|48-77|async def download_torrent(self,info)|
|`torrentgalaxy.search`|fn|pub|78-144|async def search(self,what,cat='all')|


---

# torrentgalaxyto.py | Python | 206L | 7 symbols | 10 imports | 31 comments
> Path: `src/debriddo/search/plugins/torrentgalaxyto.py`
> @file src/debriddo/search/plugins/torrentgalaxyto.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring ag...

## Imports
```
import re
import math
import time
from urllib.parse import quote_plus
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
from html.parser import HTMLParser
import asyncio
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

- var `SITE_URL = "https://torrentgalaxy.to/"` (L44) — : @brief Exported constant `SITE_URL` used by runtime workflows.
### class `class torrentgalaxy(BasePlugin)` : BasePlugin (L46-203)
L47-50> @brief Class `torrentgalaxy` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L68-71> @brief Class `TorrentGalaxyParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L79-87> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L90> if (my_attrs.get('class') == 'tgxtablerow txlight'):
L130-137> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def do_search(self, session, url)` (L151-165)
  L152-160> @brief Execute `do_search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `do_search`. @param session Runtime input parameter consumed by `do_search`. @param url Runtime input parameter consumed by `do_search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L166-203)
  L167-175> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L176> Usa il client asincrono
  L197> TODO: run in multi-thread?
  L202> `return prettyPrinter.get()`

### class `class TorrentGalaxyParser(HTMLParser)` : HTMLParser (L67-150)
L68-71> @brief Class `TorrentGalaxyParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- fn `def handle_starttag(self, tag, attrs)` (L78-128)
  L79-87> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L90> if (my_attrs.get('class') == 'tgxtablerow txlight'):
- fn `def handle_data(self, data)` (L129-150)
  L130-137> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Comments
- L7-28: VERSION: 0.0.35 | AUTHORS: nindogo (nindogo@gmail.com) | CONTRIBUTORS: Ogekuri | LICENSING INFORMATION | Permission is hereby granted, free of charge, to any person obtaining a copy | of this software and associated documentation files (the "Software"), to deal | in the Software without restriction, including without limitation the rights | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell | copies of the Software, and to permit persons to whom the Software is | furnished to do so, subject to the following conditions: | The above copyright notice and this permission notice shall be included in | all copies or substantial portions of the Software. | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE | SOFTWARE.
- L47: @brief Class `torrentgalaxy` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension bounda...
- L68: @brief Class `TorrentGalaxyParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension ...
- L79: @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L90: if (my_attrs.get('class') == 'tgxtablerow txlight'):
- L130: @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L152: @brief Execute `do_search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param...
- L167: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L197: TODO: run in multi-thread?

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SITE_URL`|var|pub|44||
|`torrentgalaxy`|class|pub|46-203|class torrentgalaxy(BasePlugin)|
|`TorrentGalaxyParser`|class|pub|67-150|class TorrentGalaxyParser(HTMLParser)|
|`TorrentGalaxyParser.handle_starttag`|fn|pub|78-128|def handle_starttag(self, tag, attrs)|
|`TorrentGalaxyParser.handle_data`|fn|pub|129-150|def handle_data(self, data)|
|`torrentgalaxy.do_search`|fn|pub|151-165|async def do_search(self, session, url)|
|`torrentgalaxy.search`|fn|pub|166-203|async def search(self, what, cat='all')|


---

# torrentproject.py | Python | 214L | 9 symbols | 7 imports | 28 comments
> Path: `src/debriddo/search/plugins/torrentproject.py`
> @file src/debriddo/search/plugins/torrentproject.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring age...

## Imports
```
from debriddo.utils.novaprinter import PrettyPrint
import re
from html.parser import HTMLParser
from urllib.parse import unquote, quote_plus
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class torrentproject(BasePlugin)` : BasePlugin (L21-182)
L22-25> @brief Class `torrentproject` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L34-37> @brief Class `MyHTMLParser` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L39-46> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L66-72> @brief Execute `get_single_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_single_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L73> `return {`
L85-93> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L110-117> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L123> ignore trash stuff
L127> ignore those with link and desc_link equals to -1
L130> fix
L131> data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago
L133> try:
L134> date_string = self.singleResData['pub_date']
L135> date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
L136> self.singleResData['pub_date'] = int(date.timestamp())
L137> except Exception:
L138> logger.error("self.singleResData['pub_date']", self.singleResData)
L145-152> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L163-182)
  L164-172> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L173> Usa il client asincrono
  L175> curr_cat = self.supported_categories[cat]
  L179> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L181> analyze first 5 pages of results

### class `class MyHTMLParser(HTMLParser)` : HTMLParser (L32-162)
- fn `def __init__(self, url)` `priv` (L38-64) L34> @brief Class `MyHTMLParser` encapsulates cohesive runtime behavior. @details Generated Doxygen bl...
  L39-46> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param url Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_single_data(self)` (L65-83)
  L66-72> @brief Execute `get_single_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_single_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L73> `return {`
- fn `def handle_starttag(self, tag, attrs)` (L84-108)
  L85-93> @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_starttag`. @param tag Runtime input parameter consumed by `handle_starttag`. @param attrs Runtime input parameter consumed by `handle_starttag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L109-143)
  L110-117> @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_endtag`. @param tag Runtime input parameter consumed by `handle_endtag`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L123> ignore trash stuff
  L127> ignore those with link and desc_link equals to -1
  L130> fix
  L131> data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago
  L133> try:
  L134> date_string = self.singleResData['pub_date']
  L135> date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
  L136> self.singleResData['pub_date'] = int(date.timestamp())
  L137> except Exception:
  L138> logger.error("self.singleResData['pub_date']", self.singleResData)
- fn `def handle_data(self, data)` (L144-162)
  L145-152> @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `handle_data`. @param data Runtime input parameter consumed by `handle_data`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def download_torrent(self, info)` (L195-214)
L196-203> @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `download_torrent`. @param info Runtime input parameter consumed by `download_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L204> Usa il client asincrono
L205> Downloader
L212> `return(str(magnet + ' ' + info))`
L214> `return None`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: mauricci | CONTRIBUTORS: Ogekuri
- L22: @brief Class `torrentproject` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension bound...
- L39: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L66: @brief Execute `get_single_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L85: @brief Execute `handle_starttag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L110: @brief Execute `handle_endtag` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...
- L123: ignore trash stuff
- L127: ignore those with link and desc_link equals to -1
- L130-138: fix | data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago | try: | date_string = self.singleResData['pub_date'] | date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S') | self.singleResData['pub_date'] = int(date.timestamp()) | except Exception: | logger.error("self.singleResData['pub_date']", self.singleResData)
- L145: @brief Execute `handle_data` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L164: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L175: curr_cat = self.supported_categories[cat]
- L179-183: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina | analyze first 5 pages of results | url = self.url + '/browse?t={0}&p={1}'.format(what, currPage)
- L196-205: @brief Execute `download_torrent` operational logic. @details Generated Doxygen block describing ... | Downloader

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentproject`|class|pub|21-182|class torrentproject(BasePlugin)|
|`MyHTMLParser`|class|pub|32-162|class MyHTMLParser(HTMLParser)|
|`MyHTMLParser.__init__`|fn|priv|38-64|def __init__(self, url)|
|`MyHTMLParser.get_single_data`|fn|pub|65-83|def get_single_data(self)|
|`MyHTMLParser.handle_starttag`|fn|pub|84-108|def handle_starttag(self, tag, attrs)|
|`MyHTMLParser.handle_endtag`|fn|pub|109-143|def handle_endtag(self, tag)|
|`MyHTMLParser.handle_data`|fn|pub|144-162|def handle_data(self, data)|
|`torrentproject.search`|fn|pub|163-182|async def search(self, what, cat='all')|
|`download_torrent`|fn|pub|195-214|async def download_torrent(self, info)|


---

# torrentz.py | Python | 118L | 3 symbols | 7 imports | 15 comments
> Path: `src/debriddo/search/plugins/torrentz.py`
> @file src/debriddo/search/plugins/torrentz.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import urllib.parse
from debriddo.utils.novaprinter import PrettyPrint
from bs4 import BeautifulSoup
from urllib.parse import quote
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin
```

## Definitions

### class `class torrentz(BasePlugin)` : BasePlugin (L20-118)
L21-24> @brief Class `torrentz` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
L29-32> TLDR; It is safer to force an 'all' research Torrentz2 categories not supported
- fn `def __parseHTML(self, html)` `priv` (L36-96)
  L37-44> @brief Execute `__parseHTML` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__parseHTML`. @param html Runtime input parameter consumed by `__parseHTML`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L48> Trova tutti i blocchi <dl> nella pagina
  L50> Estrai il titolo e il link
  L60> Estrai il magnet link
  L69> Estrai gli altri campi
  L77> rmuove i caratteri che non sono numeri
  L82> Crea il dizionario per il risultato
  L95> `return results`
- fn `async def search(self, what, cat='all')` (L97-118)
  L98-106> @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `search`. @param what Runtime input parameter consumed by `search`. @param cat Runtime input parameter consumed by `search`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L107> Usa il client asincrono
  L110> url = '{0}search?q={1}&cat=0'.format(self.api_url, what)
  L111> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L117> `return prettyPrinter.get()`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L21: @brief Class `torrentz` encapsulates cohesive runtime behavior. @details Generated Doxygen block for class-level contract and extension boundaries.
- L29: TLDR; It is safer to force an 'all' research Torrentz2 categories not supported
- L37: @brief Execute `__parseHTML` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L48-50: Trova tutti i blocchi <dl> nella pagina | Estrai il titolo e il link
- L60: Estrai il magnet link
- L69: Estrai gli altri campi
- L77: rmuove i caratteri che non sono numeri
- L82: Crea il dizionario per il risultato
- L98: @brief Execute `search` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L110-111: url = '{0}search?q={1}&cat=0'.format(self.api_url, what) | TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentz`|class|pub|20-118|class torrentz(BasePlugin)|
|`torrentz.__parseHTML`|fn|priv|36-96|def __parseHTML(self, html)|
|`torrentz.search`|fn|pub|97-118|async def search(self, what, cat='all')|


---

# search_indexer.py | Python | 32L | 2 symbols | 1 imports | 5 comments
> Path: `src/debriddo/search/search_indexer.py`
> @file src/debriddo/search/search_indexer.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from typing import Any
```

## Definitions

### class `class SearchIndexer` (L13-32)
- fn `def __init__(self)` `priv` (L18-32) L14> @brief Class `SearchIndexer` encapsulates cohesive runtime behavior. @details Generated Doxygen b...
  L19-25> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L26> general name
  L27> id
  L28> supported language
  L31> engine object
  L32> engine name

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L19: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SearchIndexer`|class|pub|13-32|class SearchIndexer|
|`SearchIndexer.__init__`|fn|priv|18-32|def __init__(self)|


---

# search_result.py | Python | 117L | 4 symbols | 4 imports | 25 comments
> Path: `src/debriddo/search/search_result.py`
> @file src/debriddo/search/search_result.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from RTN import parse
from debriddo.models.series import Series
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class SearchResult` (L18-117)
- fn `def __init__(self)` `priv` (L22-48) L19> Rappresenta un risultato di ricerca grezzo dai motori torrent.
  L23-25> Inizializza un oggetto SearchResult vuoto.
  L26> Raw title of the torrent
  L27> Title of the torrent
  L28> Size of the torrent
  L29> Download link for the torrent file or magnet url
  L30> Indexer
  L31> Seeders count
  L33> Indexer Name
  L35> Magnet url
  L36> infoHash by Search
  L37> public or private (determina se sarà o meno salvato in cache)
  L39> Extra processed details for further filtering
  L40> Language of the torrent
  L41> series or movie
  L43> from cache?
  L46> parsed data
  L47> Ranked result
- fn `def convert_to_torrent_item(self)` (L49-88) L46> parsed data
  L50-55> Converte questo risultato in un oggetto TorrentItem. Returns: TorrentItem: L'oggetto TorrentItem convertito.
  L56> def TorrentItem::__init__(self,
  L57> raw_title,
  L58> title,
  L59> size,
  L60> magnet,
  L61> info_hash,
  L62> link,
  L63> seeders,
  L64> languages,
  L65> indexer,
  L66> engine_name,
  L67> privacy,
  L68> type=None,
  L69> parsed_data=None,
  L70> from_cache=False):
  L72> `return TorrentItem(`
  L81> ilCorSaRoNeRo
  L82> ilcorsaronero (tutto minuscolo)
- fn `def from_cached_item(self, cached_item)` (L89-117)
  L90-98> Popola il SearchResult da un dizionario di item in cache. Args: cached_item (dict): Il dizionario contenente i dati della cache. Returns: SearchResult: L'istanza stessa popolata.
  L117> `return self`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L23: Inizializza un oggetto SearchResult vuoto.
- L39: Extra processed details for further filtering
- L43: from cache?
- L50-70: Converte questo risultato in un oggetto TorrentItem. Returns: ... | def TorrentItem::__init__(self, | raw_title, | title, | size, | magnet, | info_hash, | link, | seeders, | languages, | indexer, | engine_name, | privacy, | type=None, | parsed_data=None, | from_cache=False):
- L90: Popola il SearchResult da un dizionario di item in cache. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SearchResult`|class|pub|18-117|class SearchResult|
|`SearchResult.__init__`|fn|priv|22-48|def __init__(self)|
|`SearchResult.convert_to_torrent_item`|fn|pub|49-88|def convert_to_torrent_item(self)|
|`SearchResult.from_cached_item`|fn|pub|89-117|def from_cached_item(self, cached_item)|


---

# search_service.py | Python | 696L | 20 symbols | 29 imports | 57 comments
> Path: `src/debriddo/search/search_service.py`
> @file src/debriddo/search/search_service.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
import time
import xml.etree.ElementTree as ET
from typing import Any
import asyncio
from unidecode import unidecode
from debriddo.search.search_indexer import SearchIndexer
from debriddo.search.search_result import SearchResult
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.detection import detect_languages
from debriddo.utils.logger import setup_logger
from debriddo.utils.string_encoding import normalize
import time
import xml.etree.ElementTree as ET
from RTN import parse
from debriddo.search.plugins.thepiratebay_categories import thepiratebay
from debriddo.search.plugins.one337x import one337x
from debriddo.search.plugins.limetorrents import limetorrents
from debriddo.search.plugins.torrentproject import torrentproject
from debriddo.search.plugins.ilcorsaronero import ilcorsaronero
from debriddo.search.plugins.torrentz import torrentz
from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy
from debriddo.search.plugins.therarbg import therarbg
from debriddo.search.plugins.ilcorsaroblu import ilcorsaroblu
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from debriddo.utils.multi_thread import MULTI_THREAD, run_coroutine_in_thread
```

## Definitions

- var `SEARCHE_FALL_BACK = True` (L50) — Se non trova risultati prova una ricerca più estesa
### class `class SearchService` (L52-251)
- fn `def __init__(self, config)` `priv` (L56-87) L53> Servizio principale per la ricerca di torrent su diversi indexer.
  L57-62> Inizializza il servizio di ricerca. Args: config (dict): La configurazione dell'applicazione.
- fn `async def search(self, media)` (L88-155)
  L89-97> Esegue la ricerca di torrent per il media specificato. Args: media (Media): L'oggetto media (Movie o Series) da cercare. Returns: list: Una lista di oggetti SearchResult o None se nessun risultato trovato.
  L107> Invece di eseguire le coroutine direttamente sul loop principale,
  L108> le "incapsuliamo" in run_in_executor, cosi ciascuna gira in un proprio thread/loop
  L111> Ora attendiamo i risultati. Il loop principale non si bloccherà,
  L112> perché quel codice gira in un thread separato.
  L126> `return []`
  L128> concatena i risultati
  L134> spost process result ############################################
  L153> `return results`
- fn `def __get_engine(self, engine_name)` `priv` (L156-187)
  L157-165> Recupera l'istanza del plugin motore specificato. Args: engine_name (str): Il nome del motore di ricerca. Returns: object: L'istanza del plugin del motore o solleva ValueError.
  L167> `return thepiratebay(self.__config)`
  L169> `return one337x(self.__config)`
  L171> `return limetorrents(self.__config)`
  L173> `return torrentproject(self.__config)`
  L175> `return torrentz(self.__config)`
  L177> `return torrentgalaxy(self.__config)`
  L179> `return therarbg(self.__config)`
  L181> `return ilcorsaronero(self.__config)`
  L183> `return ilcorsaroblu(self.__config)`
  L185> `raise ValueError(f"Torrent Search '{engine_name}' not supported")`
- fn `def __get_requested_languages(self)` `priv` (L188-200)
  L189-194> Recupera la lista delle lingue richieste dalla configurazione. Returns: list: Lista di codici lingua o [None].
  L197> `return config_languages`
  L198> `return [None]`
- fn `def __get_title_for_language(self, media, lang)` `priv` (L201-227)
  L202-211> Ottiene il titolo del media per la lingua specificata. Args: media (Media): L'oggetto media. lang (str): Il codice lingua. Returns: str: Il titolo localizzato o il primo titolo disponibile.
  L214> `return ""`
  L217> `return titles[0]`
  L223> `return titles[lang_index]`
  L225> `return titles[0]`
- fn `def __get_lang_tag(self, indexer_language, lang)` `priv` (L228-247)
  L229-238> Restituisce il tag lingua appropriato per la ricerca. Args: indexer_language (str): La lingua dell'indexer. lang (str): La lingua richiesta. Returns: str: Il tag lingua mappato o stringa vuota.
  L240> `return ""`
  L243> `return ""`
  L245> `return self.__language_tags.get(lang, self.__default_lang_tag)`

### fn `def __build_query(self, *parts)` `priv` (L248-261)
L249-257> Costruisce una stringa di query normalizzata concatenando le parti. Args: parts: Componenti della query. Returns: str: La query normalizzata.
L259> `return normalize(query)`

### fn `def __build_query_keep_dash(self, *parts)` `priv` (L262-279)
L263-271> Costruisce una query mantenendo i trattini, utile per ricerche specifiche. Args: parts: Componenti della query. Returns: str: La query processata e pulita.
L277> `return query.lower().strip()`

### fn `async def __search_torrents(self, media, indexer, search_string, category)` `priv` (L280-303)
L281-292> Esegue la ricerca torrent su un indexer specifico. Args: media (Media): L'oggetto media. indexer (SearchIndexer): L'indexer su cui cercare. search_string (str): La stringa di ricerca. category (str): La categoria di ricerca. Returns: list: Lista di oggetti SearchResult.
L295> `return []`
L299> `return []`
L301> `return torrents`

### fn `def __log_query_result(` `priv` (L304-310)

### fn `async def __search_movie_indexer(self, movie, indexer)` `priv` (L335-410)
L336-347> Esegue la ricerca per un film su un indexer specifico. Itera sulle lingue richieste e costruisce query appropriate. Args: movie (Movie): L'oggetto film. indexer (SearchIndexer): L'indexer su cui cercare. Returns: list: Lista di risultati trovati.
L408> `return results`

### fn `async def __search_series_indexer(self, series, indexer)` `priv` (L411-511)
L412-423> Esegue la ricerca per una serie TV su un indexer specifico. Gestisce diverse strategie di ricerca (episodio singolo, pack, stagione). Args: series (Series): L'oggetto serie TV. indexer (SearchIndexer): L'indexer su cui cercare. Returns: list: Lista di risultati trovati.
L434> Esempio balordo:
L435> Arcane.S02E01-03.WEBDL 1080p Ita Eng x264-NAHOM
L436> Arcane.S02E04-06.WEBDL 1080p Ita Eng x264-NAHOM
L437> Arcane.S02E07-09.WEBDL 1080p Ita Eng x264-NAHOM
L438> Arcane.S02.720p.ITA-ENG.MULTI.WEBRip.x265.AAC-V3SP4EV3R
L440> Se cerco S02 E02 non lo trovo da nessuna parte, ma è presente in 2 file
L441> Se cerco S02 E04 lo trova in un file, ma è presente in 2 file
L442> Se cerco S02 trova 4 file ma è presente in 2 file
L444> Decido di prendere sempe tutti i risultati e vedere se poi dopo è sufficiente filtrarli
L446> se non ci sono risultati riprova omettendo l'episodio
L447> perché ci sono i torrent con l'intera serie inclusa
L448> bisogna poi cercare il file corretto
L509> `return results`

### fn `def __get_indexers(self)` `priv` (L512-528)
L513-518> Recupera e inizializza tutti gli indexer configurati. Returns: dict: Dizionario degli indexer attivi con nome motore come chiave.
L521> creiamo un dizionario con title come chiave
L523> `return indexers`
L526> `return {}`

### fn `def __get_indexer_from_engines(self, engines)` `priv` (L529-577)
L530-538> Istanzia gli oggetti SearchIndexer a partire dalla lista di motori. Args: engines (list): Lista dei nomi dei motori da attivare. Returns: list: Lista di oggetti SearchIndexer configurati.
L575> `return indexer_list`

### fn `def __get_torrents_from_list_of_dicts(self, media, indexer, list_of_dicts)` `priv` (L578-616)
L579-589> Converte una lista di dizionari grezzi in oggetti SearchResult. Args: media (Media): L'oggetto media. indexer (SearchIndexer): L'indexer di provenienza. list_of_dicts (list): Lista di risultati grezzi dal motore. Returns: list: Lista di oggetti SearchResult.
L602> engine name 'Il Corsaro Nero
L603> engine type 'ilcorsaronero' (minuscolo)
L604> series or movie
L605> public or private (determina se sarà o meno salvato in cache)
L607> processed on __post_process_results after getting pages
L608> shoud be content the link of magnet or .torrent file
L609> but NOW contain the web page or magnet, will be __post_process_results
L610> processed on __post_process_results after getting pages
L614> `return result_list`

### fn `def __is_magnet_link(self, link)` `priv` (L617-630)
L618-626> Verifica se una stringa è un magnet link. Args: link (str): Il link da verificare. Returns: bool: True se è un magnet link, False altrimenti.
L627> Check if link inizia con "magnet:?
L628> `return link.startswith("magnet:?")`

### fn `def __extract_info_hash(self, magnet_link)` `priv` (L631-658)
L632-643> Estrae l'info hash da un magnet link. Args: magnet_link (str): Il magnet link. Returns: str: L'info hash estratto. Raises: ValueError: Se il magnet link non è valido.
L644> parse
L647> extract 'xt
L652> remove prefix "urn:btih:
L654> `return info_hash`
L656> `raise ValueError("Magnet link invalid")`

### fn `async def __post_process_result(self, indexers, result, media)` `priv` (L659-696)
L660-670> Post-processa un risultato di ricerca, risolvendo i magnet link se necessario. Args: indexers (dict): Dizionario degli indexer disponibili. result (SearchResult): Il risultato da processare. media (Media): L'oggetto media. Returns: SearchResult: Il risultato processato o None in caso di fallimento.
L681> raise Exception('Error, please fill a bug report!')
L682> se non riesce a scarica il file ritorna None
L683> `return None`
L686> parse RAW title to detect languages
L688> result.languages = [languages.get(name=language).alpha2 for language in parsed_result.language]
L690> TODO: replace with parsed_result.lang_codes when RTN is updated
L696> `return result`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L37: from search.plugins.torrentgalaxyto import torrentgalaxy
- L57: Inizializza il servizio di ricerca. Args: ...
- L89: Esegue la ricerca di torrent per il media specificato. Args: ...
- L107-108: Invece di eseguire le coroutine direttamente sul loop principale, | le "incapsuliamo" in run_in_executor, cosi ciascuna gira in un proprio thread/loop
- L111-112: Ora attendiamo i risultati. Il loop principale non si bloccherà, | perché quel codice gira in un thread separato.
- L128: concatena i risultati
- L134: spost process result ############################################
- L157: Recupera l'istanza del plugin motore specificato. Args: ...
- L189: Recupera la lista delle lingue richieste dalla configurazione. Returns: ...
- L202: Ottiene il titolo del media per la lingua specificata. Args: ...
- L229: Restituisce il tag lingua appropriato per la ricerca. Args: ...
- L249: Costruisce una stringa di query normalizzata concatenando le parti. Args: ...
- L263: Costruisce una query mantenendo i trattini, utile per ricerche specifiche. Args: ...
- L281: Esegue la ricerca torrent su un indexer specifico. Args: ...
- L312: Registra nei log i risultati di una query. Args: ...
- L336: Esegue la ricerca per un film su un indexer specifico. Itera sulle lingue richieste e costruisce query appropriate. ...
- L412: Esegue la ricerca per una serie TV su un indexer specifico. Gestisce diverse strategie di ricerca (episodio singolo, pack, stagione). ...
- L434-448: Esempio balordo: | Arcane.S02E01-03.WEBDL 1080p Ita Eng x264-NAHOM | Arcane.S02E04-06.WEBDL 1080p Ita Eng x264-NAHOM | Arcane.S02E07-09.WEBDL 1080p Ita Eng x264-NAHOM | Arcane.S02.720p.ITA-ENG.MULTI.WEBRip.x265.AAC-V3SP4EV3R | Se cerco S02 E02 non lo trovo da nessuna parte, ma è presente in 2 file | Se cerco S02 E04 lo trova in un file, ma è presente in 2 file | Se cerco S02 trova 4 file ma è presente in 2 file | Decido di prendere sempe tutti i risultati e vedere se poi dopo è sufficiente filtrarli | se non ci sono risultati riprova omettendo l'episodio | perché ci sono i torrent con l'intera serie inclusa | bisogna poi cercare il file corretto
- L513: Recupera e inizializza tutti gli indexer configurati. Returns: ...
- L521: creiamo un dizionario con title come chiave
- L530: Istanzia gli oggetti SearchIndexer a partire dalla lista di motori. Args: ...
- L579: Converte una lista di dizionari grezzi in oggetti SearchResult. Args: ...
- L609: but NOW contain the web page or magnet, will be __post_process_results
- L618-627: Verifica se una stringa è un magnet link. Args: ... | Check if link inizia con "magnet:?
- L632-644: Estrae l'info hash da un magnet link. Args: ... | parse
- L647: extract 'xt
- L652: remove prefix "urn:btih:
- L660: Post-processa un risultato di ricerca, risolvendo i magnet link se necessario. Args: ...
- L681-682: raise Exception('Error, please fill a bug report!') | se non riesce a scarica il file ritorna None
- L686-690: parse RAW title to detect languages | result.languages = [languages.get(name=language).alpha2 for language in parsed_result.language] | TODO: replace with parsed_result.lang_codes when RTN is updated

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SEARCHE_FALL_BACK`|var|pub|50||
|`SearchService`|class|pub|52-251|class SearchService|
|`SearchService.__init__`|fn|priv|56-87|def __init__(self, config)|
|`SearchService.search`|fn|pub|88-155|async def search(self, media)|
|`SearchService.__get_engine`|fn|priv|156-187|def __get_engine(self, engine_name)|
|`SearchService.__get_requested_languages`|fn|priv|188-200|def __get_requested_languages(self)|
|`SearchService.__get_title_for_language`|fn|priv|201-227|def __get_title_for_language(self, media, lang)|
|`SearchService.__get_lang_tag`|fn|priv|228-247|def __get_lang_tag(self, indexer_language, lang)|
|`__build_query`|fn|priv|248-261|def __build_query(self, *parts)|
|`__build_query_keep_dash`|fn|priv|262-279|def __build_query_keep_dash(self, *parts)|
|`__search_torrents`|fn|priv|280-303|async def __search_torrents(self, media, indexer, search_...|
|`__log_query_result`|fn|priv|304-310|def __log_query_result(|
|`__search_movie_indexer`|fn|priv|335-410|async def __search_movie_indexer(self, movie, indexer)|
|`__search_series_indexer`|fn|priv|411-511|async def __search_series_indexer(self, series, indexer)|
|`__get_indexers`|fn|priv|512-528|def __get_indexers(self)|
|`__get_indexer_from_engines`|fn|priv|529-577|def __get_indexer_from_engines(self, engines)|
|`__get_torrents_from_list_of_dicts`|fn|priv|578-616|def __get_torrents_from_list_of_dicts(self, media, indexe...|
|`__is_magnet_link`|fn|priv|617-630|def __is_magnet_link(self, link)|
|`__extract_info_hash`|fn|priv|631-658|def __extract_info_hash(self, magnet_link)|
|`__post_process_result`|fn|priv|659-696|async def __post_process_result(self, indexers, result, m...|


---

# test_plugins.py | Python | 122L | 7 symbols | 13 imports | 16 comments
> Path: `src/debriddo/test_plugins.py`
> @file src/debriddo/test_plugins.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import sys
import asyncio
from pathlib import Path
from debriddo.search.plugins.thepiratebay_categories import thepiratebay
from debriddo.search.plugins.one337x import one337x
from debriddo.search.plugins.limetorrents import limetorrents
from debriddo.search.plugins.torrentproject import torrentproject
from debriddo.search.plugins.ilcorsaronero import ilcorsaronero
from debriddo.search.plugins.torrentz import torrentz
from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy
from debriddo.search.plugins.therarbg import therarbg
from debriddo.search.plugins.ilcorsaroblu import ilcorsaroblu
from urllib.parse import quote_plus
```

## Definitions

- var `SRC_DIR = Path(__file__).resolve().parents[1]` (L16) — Allow execution as a standalone script from any working directory.
### fn `def build_engines()` (L40-51)
L41-46> @brief Execute `build_engines` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L47> `return [`

- var `SEARCH_STRING = "The Fall Guy 2024 ITA"` (L53) — : @brief Exported constant `SEARCH_STRING` used by runtime workflows.
- var `SEARCH_TYPE = "movies"` (L55) — : @brief Exported constant `SEARCH_TYPE` used by runtime workflows.
### fn `def __is_torrent(link: str) -> bool` `priv` (L57-67)
L58> Controlla se il link termina con ".torrent
L59-65> @brief Execute `__is_torrent` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param link Runtime input parameter consumed by `__is_torrent`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L66> `return link.endswith(".torrent")`

### fn `def __is_magnet_link(link: str) -> bool` `priv` (L68-78)
L59> @brief Execute `__is_torrent` operational logic.
L60> @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
L61> @param link Runtime input parameter consumed by `__is_torrent`.
L62> ...
L69> Check if link inizia con "magnet:?
L70-76> @brief Execute `__is_magnet_link` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param link Runtime input parameter consumed by `__is_magnet_link`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L77> `return link.startswith("magnet:?")`

### fn `async def main()` (L79-120)
L70> @brief Execute `__is_magnet_link` operational logic.
L71> @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
L72> @param link Runtime input parameter consumed by `__is_magnet_link`.
L73> ...
L80-85> @brief Execute `main` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L97> final results
L119> Plugin instances don't need explicit close

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L26: from debriddo.search.plugins.torrentgalaxyto import torrentgalaxy
- L33: Dati del form di autenticazione
- L41: @brief Execute `build_engines` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @r...
- L58: Controlla se il link termina con ".torrent
- L69: Check if link inizia con "magnet:?
- L80: @brief Execute `main` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Com...
- L97: final results

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SRC_DIR`|var|pub|16||
|`build_engines`|fn|pub|40-51|def build_engines()|
|`SEARCH_STRING`|var|pub|53||
|`SEARCH_TYPE`|var|pub|55||
|`__is_torrent`|fn|priv|57-67|def __is_torrent(link: str) -> bool|
|`__is_magnet_link`|fn|priv|68-78|def __is_magnet_link(link: str) -> bool|
|`main`|fn|pub|79-120|async def main()|


---

# test_sviluppo_plugins.py | Python | 110L | 2 symbols | 6 imports | 31 comments
> Path: `src/debriddo/test_sviluppo_plugins.py`
> @file src/debriddo/test_sviluppo_plugins.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from bs4 import BeautifulSoup
from urllib.parse import quote, quote_plus
from pathlib import Path
import sys
import asyncio
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

- var `SRC_DIR = Path(__file__).resolve().parents[1]` (L17) — : @brief Exported constant `SRC_DIR` used by runtime workflows.
### fn `async def main()` (L23-109)
L24-29> @brief Execute `main` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L33> Variabili per l'autenticazione
L37> URL del form di login e dati richiesti
L41> Dati del form di autenticazione
L49> # Esegui il login
L50> try:
L51> response = session.post(login_url, data=data, headers=headers)
L52> print(response.url)  # URL generato da requests
L53> response.raise_for_status()  # Controlla errori HTTP
L54> # Verifica se il login è stato effettuato correttamente
L55> if "Benvenuto" in response.text or "Logout" in response.text:
L56> print("Login effettuato con successo!")
L57> login = True
L58> else:
L59> print("Errore nel login. Controlla username e password.")
L60> except requests.RequestException as e:
L61> print(f"Errore durante il tentativo di login: {e}")
L64> Variabili per la ricerca
L66> https://torrentgalaxy.one/get-posts/category:Movies:keywords:Wolfs%202024%20ITA
L67> https://torrentgalaxy.one/get-posts/category:TV:keywords:Arcane%20S01%20ITA
L68> https://torrentgalaxy.one/get-posts/category:Anime:keywords:Arcane%20S01%20ITA
L74> URL e parametri per la ricerca
L78> Esegui la ricerca
L81> Controlla errori HTTP
L86> Parsing della risposta HTML
L88> Trova la prima tabella
L91> Trova la prima tabella
L94> 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF
L95> - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf
L96> - /get-posts/keywords:tt14257582
L100> Divide per "/" e converte in interi

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L24: @brief Execute `main` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @return Com...
- L33: Variabili per l'autenticazione
- L37: URL del form di login e dati richiesti
- L41: Dati del form di autenticazione
- L49-61: # Esegui il login | try: | response = session.post(login_url, data=data, headers=headers) | print(response.url)  # URL generato da requests | response.raise_for_status()  # Controlla errori HTTP | # Verifica se il login è stato effettuato correttamente | if "Benvenuto" in response.text or "Logout" in response.text: | print("Login effettuato con successo!") | login = True | else: | print("Errore nel login. Controlla username e password.") | except requests.RequestException as e: | print(f"Errore durante il tentativo di login: {e}")
- L64-68: Variabili per la ricerca | https://torrentgalaxy.one/get-posts/category:Movies:keywords:Wolfs%202024%20ITA | https://torrentgalaxy.one/get-posts/category:TV:keywords:Arcane%20S01%20ITA | https://torrentgalaxy.one/get-posts/category:Anime:keywords:Arcane%20S01%20ITA
- L74: URL e parametri per la ricerca
- L78: Esegui la ricerca
- L86: Parsing della risposta HTML
- L94-96: 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF | - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf | - /get-posts/keywords:tt14257582

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SRC_DIR`|var|pub|17||
|`main`|fn|pub|23-109|async def main()|


---

# torrent_item.py | Python | 89L | 3 symbols | 5 imports | 7 comments
> Path: `src/debriddo/torrent/torrent_item.py`
> @file src/debriddo/torrent/torrent_item.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from urllib.parse import quote
from typing import Any
from debriddo.models.media import Media
from debriddo.models.series import Series
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TorrentItem` (L19-89)
- fn `def __init__(self, raw_title, title, size, magnet, info_hash, link, seeders, languages, indexer,` `priv` (L24-72) L20> @brief Class `TorrentItem` encapsulates cohesive runtime behavior. @details Generated Doxygen blo...
  L26-46> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param raw_title Runtime input parameter consumed by `__init__`. @param title Runtime input parameter consumed by `__init__`. @param size Runtime input parameter consumed by `__init__`. @param magnet Runtime input parameter consumed by `__init__`. @param info_hash Runtime input parameter consumed by `__init__`. @param link Runtime input parameter consumed by `__init__`. @param seeders Runtime input parameter consumed by `__init__`. @param languages Runtime input parameter consumed by `__init__`. @param indexer Runtime input parameter consumed by `__init__`. @param engine_name Runtime input parameter consumed by `__init__`. @param privacy Runtime input parameter consumed by `__init__`. @param type Runtime input parameter consumed by `__init__`. @param parsed_data Runtime input parameter consumed by `__init__`. @param from_cache Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L49> Raw title of the torrent
  L50> Title of the torrent
  L51> Size of the video file inside the torrent - it may be updated during __process_torrent()
  L52> Magnet to torrent
  L53> Hash of the torrent
  L54> Link to download torrent file or magnet link
  L55> The number of seeders
  L56> Language of the torrent
  L57> Indexer of the torrent (ilCorSaRoNeRo)
  L58> Engine name of the torrent (ilcorsaronero)
  L59> public or private (determina se sarà o meno salvato in cache)
  L60> series" or "movie
  L61> by default is not from cache
  L63> it may be updated during __process_torrent()
  L64> The files inside of the torrent. If it's None, it means that there is only one file inside of the torrent
  L65> The torrent download url if its None, it means that there is only a magnet link provided by Jackett. It also means, that we cant do series file filtering before debrid.
  L66> Trackers of the torrent
  L67> Index of the file inside of the torrent - it may be updated durring __process_torrent() and update_availability(). If the index is None and torrent is not None, it means that the series episode is not inside of the torrent.
  L68> If it's instantly available on the debrid service
  L71> Ranked result
- fn `def to_debrid_stream_query(self, media: Media) -> dict` (L73-89)
  L74-81> @brief Execute `to_debrid_stream_query` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `to_debrid_stream_query`. @param media Runtime input parameter consumed by `to_debrid_stream_query`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L82> `return {`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L26: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L74: @brief Execute `to_debrid_stream_query` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentItem`|class|pub|19-89|class TorrentItem|
|`TorrentItem.__init__`|fn|priv|24-72|def __init__(self, raw_title, title, size, magnet, info_h...|
|`TorrentItem.to_debrid_stream_query`|fn|pub|73-89|def to_debrid_stream_query(self, media: Media) -> dict|


---

# torrent_service.py | Python | 347L | 13 symbols | 14 imports | 43 comments
> Path: `src/debriddo/torrent/torrent_service.py`
> @file src/debriddo/torrent/torrent_service.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import hashlib
import queue
import threading
import urllib.parse
from typing import List
import bencode
import asyncio
from RTN import parse
from debriddo.search.search_result import SearchResult
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.general import get_info_hash_from_magnet
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.utils.multi_thread import MULTI_THREAD, run_coroutine_in_thread
```

## Definitions

### class `class TorrentService` (L29-228)
L39> # versione originale multi-thread
L40> async def convert_and_process(self, results: List[SearchResult]):
L42> threads = []
L43> torrent_items_queue = queue.Queue()
L44> def thread_target(result: SearchResult):
L45> torrent_item = result.convert_to_torrent_item()
L46> if torrent_item.link.startswith("magnet:"):
L47> processed_torrent_item = self.__process_magnet(torrent_item)
L48> else:
L49> processed_torrent_item = self.__process_web_url(torrent_item)
L50> torrent_items_queue.put(processed_torrent_item)
L51> for result in results:
L52> threads.append(threading.Thread(target=thread_target, args=(result,)))
L53> for thread in threads:
L54> thread.start()
L55> for thread in threads:
L56> thread.join()
L57> torrent_items_result = []
L58> while not torrent_items_queue.empty():
L59> torrent_items_result.append(torrent_items_queue.get())
L218-228> Costruisce una stringa magnet link. Args: hash (str): Info hash. display_name (str): Nome visualizzato. trackers (list): Lista dei tracker. Returns: str: Il magnet link.
- fn `def __init__(self)` `priv` (L33-38) L30> Servizio per la gestione e il processing dei file torrent.
  L34-36> Inizializza il servizio TorrentService.
- fn `async def __process_web_url_or_process_magnet(self, result: SearchResult)` `priv` (L63-84) L60> return torrent_items_result
  L64-72> Processa un risultato determinando se è un link web o magnet. Args: result (SearchResult): Il risultato della ricerca. Returns: TorrentItem: L'item processato o None.
  L77> `return None`
  L80> `return self.__process_magnet(torrent_item)`
  L82> `return await self.__process_web_url(torrent_item)`
- fn `async def convert_and_process(self, results: List[SearchResult])` (L85-106)
  L86-94> Converte e processa una lista di risultati di ricerca. Args: results (List[SearchResult]): Lista dei risultati. Returns: list: Lista di TorrentItem processati.
  L104> `return torrent_items_result`
- fn `async def __process_web_url(self, result: TorrentItem)` `priv` (L107-141)
  L108-116> Scarica e processa un file torrent da un URL web. Args: result (TorrentItem): L'item del torrent. Returns: TorrentItem: L'item aggiornato o None.
  L119> `return None`
  L120> TODO: is the timeout enough?
  L121> Usa il client asincrono
  L122> response = await session.request_get(result.link, allow_redirects=False, timeout=2)
  L127> `return self.__process_torrent(result, response.content)`
  L130> `return self.__process_magnet(result)`
  L134> `return result`
  L139> `return None`
- fn `def __process_torrent(self, result: TorrentItem, torrent_file)` `priv` (L142-182)
  L143-152> Estrae i metadati dal contenuto binario di un file torrent. Args: result (TorrentItem): L'item del torrent. torrent_file (bytes): Il contenuto del file. Returns: TorrentItem: L'item aggiornato con i metadati.
  L162> `return result`
  L181> `return result`
- fn `def __process_magnet(self, result: TorrentItem)` `priv` (L183-202)
  L184-192> Processa un magnet link estraendo info hash e tracker. Args: result (TorrentItem): L'item del torrent. Returns: TorrentItem: L'item aggiornato.
  L201> `return result`
- fn `def __convert_torrent_to_hash(self, torrent_contents)` `priv` (L203-216)
  L204-212> Calcola l'info hash SHA1 del contenuto del torrent. Args: torrent_contents (dict): Contenuto del dizionario 'info'. Returns: str: L'hash esadecimale.
  L215> `return hexHash.lower()`

### fn `def __build_magnet(self, hash, display_name, trackers)` `priv` (L217-236)
L218-228> Costruisce una stringa magnet link. Args: hash (str): Info hash. display_name (str): Nome visualizzato. trackers (list): Lista dei tracker. Returns: str: Il magnet link.
L235> `return magnet`

### fn `def __get_trackers_from_torrent(self, torrent_metadata)` `priv` (L237-267)
L238-246> Estrae la lista dei tracker dai metadati del torrent. Args: torrent_metadata (dict): I metadati del torrent. Returns: list: Lista dei tracker.
L247> Sometimes list, sometimes string
L249> Sometimes 2D array, sometimes 1D array
L266> `return list(trackers)`

### fn `def __get_trackers_from_magnet(self, magnet: str)` `priv` (L268-286)
L269-277> Estrae la lista dei tracker da un magnet link. Args: magnet (str): Il magnet link. Returns: list: Lista dei tracker.
L285> `return trackers`

### fn `def __find_episode_file(self, file_structure, season, episode)` `priv` (L287-327)
L288-298> Trova il file corrispondente a un episodio specifico nella struttura dei file. Args: file_structure (list): Lista dei file nel torrent. season (list): Stagione cercata. episode (list): Episodio cercato. Returns: dict: Dettagli del file trovato o None.
L303> `return None`
L320> Doesn't that need to be indented?
L324> `return None`
L326> `return max(episode_files, key=lambda file: file["size"])`

### fn `def __find_movie_file(self, file_structure)` `priv` (L328-347)
L329-337> Trova il file principale (film) basandosi sulla dimensione. Args: file_structure (list): Lista dei file nel torrent. Returns: int: Indice del file più grande.
L347> `return max_file_index`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L34: Inizializza il servizio TorrentService.
- L39-59: # versione originale multi-thread | async def convert_and_process(self, results: List[SearchResult]): | threads = [] | torrent_items_queue = queue.Queue() | def thread_target(result: SearchResult): | torrent_item = result.convert_to_torrent_item() | if torrent_item.link.startswith("magnet:"): | processed_torrent_item = self.__process_magnet(torrent_item) | else: | processed_torrent_item = self.__process_web_url(torrent_item) | torrent_items_queue.put(processed_torrent_item) | for result in results: | threads.append(threading.Thread(target=thread_target, args=(result,))) | for thread in threads: | thread.start() | for thread in threads: | thread.join() | torrent_items_result = [] | while not torrent_items_queue.empty(): | torrent_items_result.append(torrent_items_queue.get())
- L64: Processa un risultato determinando se è un link web o magnet. Args: ...
- L86: Converte e processa una lista di risultati di ricerca. Args: ...
- L108: Scarica e processa un file torrent da un URL web. Args: ...
- L120-122: TODO: is the timeout enough? | response = await session.request_get(result.link, allow_redirects=False, timeout=2)
- L143: Estrae i metadati dal contenuto binario di un file torrent. Args: ...
- L184: Processa un magnet link estraendo info hash e tracker. Args: ...
- L204: Calcola l'info hash SHA1 del contenuto del torrent. Args: ...
- L218: Costruisce una stringa magnet link. Args: ...
- L238-249: Estrae la lista dei tracker dai metadati del torrent. Args: ... | Sometimes list, sometimes string | Sometimes 2D array, sometimes 1D array
- L269: Estrae la lista dei tracker da un magnet link. Args: ...
- L288: Trova il file corrispondente a un episodio specifico nella struttura dei file. Args: ...
- L320: Doesn't that need to be indented?
- L329: Trova il file principale (film) basandosi sulla dimensione. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentService`|class|pub|29-228|class TorrentService|
|`TorrentService.__init__`|fn|priv|33-38|def __init__(self)|
|`TorrentService.__process_web_url_or_process_magnet`|fn|priv|63-84|async def __process_web_url_or_process_magnet(self, resul...|
|`TorrentService.convert_and_process`|fn|pub|85-106|async def convert_and_process(self, results: List[SearchR...|
|`TorrentService.__process_web_url`|fn|priv|107-141|async def __process_web_url(self, result: TorrentItem)|
|`TorrentService.__process_torrent`|fn|priv|142-182|def __process_torrent(self, result: TorrentItem, torrent_...|
|`TorrentService.__process_magnet`|fn|priv|183-202|def __process_magnet(self, result: TorrentItem)|
|`TorrentService.__convert_torrent_to_hash`|fn|priv|203-216|def __convert_torrent_to_hash(self, torrent_contents)|
|`__build_magnet`|fn|priv|217-236|def __build_magnet(self, hash, display_name, trackers)|
|`__get_trackers_from_torrent`|fn|priv|237-267|def __get_trackers_from_torrent(self, torrent_metadata)|
|`__get_trackers_from_magnet`|fn|priv|268-286|def __get_trackers_from_magnet(self, magnet: str)|
|`__find_episode_file`|fn|priv|287-327|def __find_episode_file(self, file_structure, season, epi...|
|`__find_movie_file`|fn|priv|328-347|def __find_movie_file(self, file_structure)|


---

# torrent_smart_container.py | Python | 368L | 16 symbols | 9 imports | 26 comments
> Path: `src/debriddo/torrent/torrent_smart_container.py`
> @file src/debriddo/torrent/torrent_smart_container.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring a...

## Imports
```
from typing import List, Dict
from debriddo.debrid.alldebrid import AllDebrid
from debriddo.debrid.premiumize import Premiumize
from debriddo.debrid.realdebrid import RealDebrid
from debriddo.debrid.torbox import TorBox
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.cache import cache_results
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TorrentSmartContainer` (L26-225)
- fn `def __init__(self, torrent_items: List[TorrentItem], media)` `priv` (L31-44) L27> @brief Class `TorrentSmartContainer` encapsulates cohesive runtime behavior. @details Generated D...
  L32-40> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param torrent_items Runtime input parameter consumed by `__init__`. @param media Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_hashes(self)` (L45-54)
  L46-52> @brief Execute `get_hashes` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_hashes`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L53> `return list(self.__itemsDict.keys())`
- fn `def get_items(self)` (L55-64) L46> @brief Execute `get_hashes` operational logic. @details Generated Doxygen block describing callab...
  L56-62> @brief Execute `get_items` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_items`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L63> `return list(self.__itemsDict.values())`
- fn `def get_direct_torrentable(self)` (L65-78) L56> @brief Execute `get_items` operational logic. @details Generated Doxygen block describing callabl...
  L66-72> @brief Execute `get_direct_torrentable` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_direct_torrentable`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L77> `return direct_torrentable_items`
- fn `def get_best_matching(self)` (L79-103)
  L80-86> @brief Execute `get_best_matching` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get_best_matching`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L93> Torrent download
  L96> If the season/episode is present inside the torrent filestructure (movies always have a
  L97> file_index)
  L99> Magnet
  L100> If it's a movie with a magnet link
  L102> `return best_matching`
- fn `def cache_container_items(self)` (L104-117)
  L105> threading.Thread(target=self.__save_to_cache).start()
  L106> la versione originale esegue l'upload dei risultati quindi
  L107> gira in un tread separato, ma per sqllite non serve
  L108-114> @brief Execute `cache_container_items` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `cache_container_items`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __save_to_cache(self)` `priv` (L118-128)
  L119-125> @brief Execute `__save_to_cache` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__save_to_cache`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def update_availability(self, debrid_response, debrid_type, media)` (L129-150)
  L130-139> @brief Execute `update_availability` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `update_availability`. @param debrid_response Runtime input parameter consumed by `update_availability`. @param debrid_type Runtime input parameter consumed by `update_availability`. @param media Runtime input parameter consumed by `update_availability`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L149> `raise NotImplemented`
- fn `def __update_availability_realdebrid(self, response, media)` `priv` (L151-197)
  L152-160> @brief Execute `__update_availability_realdebrid` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__update_availability_realdebrid`. @param response Runtime input parameter consumed by `__update_availability_realdebrid`. @param media Runtime input parameter consumed by `__update_availability_realdebrid`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __update_availability_alldebrid(self, response, media)` `priv` (L198-223)
  L199-207> @brief Execute `__update_availability_alldebrid` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__update_availability_alldebrid`. @param response Runtime input parameter consumed by `__update_availability_alldebrid`. @param media Runtime input parameter consumed by `__update_availability_alldebrid`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L210> `return`

### fn `def __update_availability_torbox(self, response, media)` `priv` (L224-251)
L225-233> @brief Execute `__update_availability_torbox` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__update_availability_torbox`. @param response Runtime input parameter consumed by `__update_availability_torbox`. @param media Runtime input parameter consumed by `__update_availability_torbox`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __update_availability_premiumize(self, response)` `priv` (L252-270)
L253-260> @brief Execute `__update_availability_premiumize` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__update_availability_premiumize`. @param response Runtime input parameter consumed by `__update_availability_premiumize`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L263> `return`

### fn `def __update_file_details(self, torrent_item, files)` `priv` (L271-289)
L272-280> @brief Execute `__update_file_details` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__update_file_details`. @param torrent_item Runtime input parameter consumed by `__update_file_details`. @param files Runtime input parameter consumed by `__update_file_details`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L282> `return`

### fn `def __build_items_dict_by_infohash(self, items: List[TorrentItem])` `priv` (L290-308)
L291-298> @brief Execute `__build_items_dict_by_infohash` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__build_items_dict_by_infohash`. @param items Runtime input parameter consumed by `__build_items_dict_by_infohash`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L307> `return items_dict`

### fn `def __explore_folders(self, folder, files, file_index, type, season=None, episode=None)` `priv` (L310-368)
L309> Simple recursion to traverse the file structure returned by AllDebrid
L311-323> @brief Execute `__explore_folders` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__explore_folders`. @param folder Runtime input parameter consumed by `__explore_folders`. @param files Runtime input parameter consumed by `__explore_folders`. @param file_index Runtime input parameter consumed by `__explore_folders`. @param type Runtime input parameter consumed by `__explore_folders`. @param season Runtime input parameter consumed by `__explore_folders`. @param episode Runtime input parameter consumed by `__explore_folders`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L368> `return file_index`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L32: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L66: @brief Execute `get_direct_torrentable` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L80: @brief Execute `get_best_matching` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning...
- L96-97: If the season/episode is present inside the torrent filestructure (movies always have a | file_index)
- L105-114: threading.Thread(target=self.__save_to_cache).start() | la versione originale esegue l'upload dei risultati quindi | gira in un tread separato, ma per sqllite non serve | @brief Execute `cache_container_items` operational logic. @details Generated Doxygen block descri...
- L119: @brief Execute `__save_to_cache` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L130: @brief Execute `update_availability` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoni...
- L152: @brief Execute `__update_availability_realdebrid` operational logic. @details Generated Doxygen block describing callable contract for LLM-native s...
- L199: @brief Execute `__update_availability_alldebrid` operational logic. @details Generated Doxygen block describing callable contract for LLM-native st...
- L225: @brief Execute `__update_availability_torbox` operational logic. @details Generated Doxygen block describing callable contract for LLM-native stati...
- L253: @brief Execute `__update_availability_premiumize` operational logic. @details Generated Doxygen block describing callable contract for LLM-native s...
- L272: @brief Execute `__update_file_details` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reaso...
- L291: @brief Execute `__build_items_dict_by_infohash` operational logic. @details Generated Doxygen block describing callable contract for LLM-native sta...
- L311: @brief Execute `__explore_folders` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentSmartContainer`|class|pub|26-225|class TorrentSmartContainer|
|`TorrentSmartContainer.__init__`|fn|priv|31-44|def __init__(self, torrent_items: List[TorrentItem], media)|
|`TorrentSmartContainer.get_hashes`|fn|pub|45-54|def get_hashes(self)|
|`TorrentSmartContainer.get_items`|fn|pub|55-64|def get_items(self)|
|`TorrentSmartContainer.get_direct_torrentable`|fn|pub|65-78|def get_direct_torrentable(self)|
|`TorrentSmartContainer.get_best_matching`|fn|pub|79-103|def get_best_matching(self)|
|`TorrentSmartContainer.cache_container_items`|fn|pub|104-117|def cache_container_items(self)|
|`TorrentSmartContainer.__save_to_cache`|fn|priv|118-128|def __save_to_cache(self)|
|`TorrentSmartContainer.update_availability`|fn|pub|129-150|def update_availability(self, debrid_response, debrid_typ...|
|`TorrentSmartContainer.__update_availability_realdebrid`|fn|priv|151-197|def __update_availability_realdebrid(self, response, media)|
|`TorrentSmartContainer.__update_availability_alldebrid`|fn|priv|198-223|def __update_availability_alldebrid(self, response, media)|
|`__update_availability_torbox`|fn|priv|224-251|def __update_availability_torbox(self, response, media)|
|`__update_availability_premiumize`|fn|priv|252-270|def __update_availability_premiumize(self, response)|
|`__update_file_details`|fn|priv|271-289|def __update_file_details(self, torrent_item, files)|
|`__build_items_dict_by_infohash`|fn|priv|290-308|def __build_items_dict_by_infohash(self, items: List[Torr...|
|`__explore_folders`|fn|priv|310-368|def __explore_folders(self, folder, files, file_index, ty...|


---

# async_httpx_session.py | Python | 405L | 17 symbols | 11 imports | 99 comments
> Path: `src/debriddo/utils/async_httpx_session.py`
> @file src/debriddo/utils/async_httpx_session.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import gzip
import re
import socket
import tempfile
from urllib.parse import urlparse
import html.entities
import asyncio
import httpx
import socks
import json
from debriddo.utils.logger import setup_logger
```

## Definitions

- var `DEFAULT_TIMEOUT = 20.0  # 20 secondi` (L23) — : @brief Exported constant `DEFAULT_TIMEOUT` used by runtime workflows.
### class `class AsyncThreadSafeSession` (L25-224)
L26-28> Gestisce sessioni HTTP asincrone thread-safe con supporto per HTTP/2, proxy e cookie.
L222> versione originale sincrona
L224> def retrieve_url(url):
- fn `def __init__(self, proxy=None)` `priv` (L37-56)
  L38-43> Inizializza la sessione HTTP. Args: proxy (str, optional): Proxy in formato user:pass@host:port. Defaults to None.
  L44> Gestione esplicita dei cookie
  L45> Associa i cookie al client, abilita i reindirizzamenti
  L46> self._lock = asyncio.Lock()  # Usa un lock asincrono
  L47> Timeout predefinito di 20 secondi
  L49> SOCKS5 Proxy setup (if provided)
  L53> per il check dei close
- fn `async def close(self)` (L57-66)
  L58-63> Chiude il client HTTPX e rilascia le risorse. Returns: None
- fn `async def __aenter__(self)` `priv` (L67-75)
  L68-73> Inizia il contesto asincrono. Returns: AsyncThreadSafeSession: L'istanza della sessione.
  L74> `return self`
- fn `async def __aexit__(self, exc_type, exc_val, exc_tb)` `priv` (L76-86) L68> Inizia il contesto asincrono. Returns: ...
  L77-84> Chiude la sessione quando il contesto termina. Args: exc_type: Tipo dell'eccezione. exc_val: Valore dell'eccezione. exc_tb: Traceback dell'eccezione.
- fn `def __del__(self)` `priv` (L87-94) L77> Chiude la sessione quando il contesto termina. Args: ...
  L88-90> Verifica se la sessione è stata chiusa correttamente.
  L92> Logga un avviso, senza tentare di chiudere la sessione
- fn `def _html_entity_decode(s)` `priv` (L98-130) L95> per Debrid
  L99-107> Decodifica le entità HTML in una stringa. Args: s (str): La stringa da decodificare. Returns: str: La stringa decodificata.
  L108> First convert alpha entities (such as &eacute;)
  L109> (Inspired from http://mail.python.org/pipermail/python-list/2007-June/443813.html)
  L111-117> @brief Execute `entity2char` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param m Runtime input parameter consumed by `entity2char`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L120> `return chr(html.entities.name2codepoint[entity])`
  L121> `return " "` — Unknown entity: We replace with a space.
  L124> Then convert numerical entities (such as &#233;)
  L127> Then convert hexa entities (such as &#x00E9;)
  L128> `return re.sub(r'&#x(\w+);', lambda x: chr(int(x.group(1), 16)), t)`
- fn `def entity2char(m)` (L110-121) L99> Decodifica le entità HTML in una stringa. Args: ...
  L111-117> @brief Execute `entity2char` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param m Runtime input parameter consumed by `entity2char`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L120> `return chr(html.entities.name2codepoint[entity])`
  L121> `return " "` — Unknown entity: We replace with a space.
- fn `def _setup_proxy(self, proxy)` `priv` (L131-155)
  L132-140> Configura il proxy SOCKS5. Args: proxy (str): Stringa proxy formattata. Raises: ValueError: Se il formato del proxy non è valido.
  L153> `raise ValueError("Invalid proxy format. Expected format: user:pass@host:port or host:port")`
- fn `async def request(self, method, url, **kwargs)` (L158-193) L156> per i Plug-Ins
  L159-169> Esegue una richiesta HTTP. Args: method (str): Metodo HTTP (GET, POST, etc.). url (str): URL di destinazione. kwargs: Argomenti aggiuntivi per httpx.request. Returns: httpx.Response: La risposta HTTP o None in caso di errore.
  L170> async with self._lock:
  L172> Combina gli header specificati con quelli di default
  L174> Unisce gli header di default e quelli personalizzati
  L176> Usa un timeout personalizzato o quello predefinito
  L182> Solleva un'eccezione per errori HTTP 4xx o 5xx
  L183> `return response` — Restituisce la risposta finale dopo i reindirizzamenti
  L185> Logga l'errore e restituisce una risposta informativa
  L187> `return None`
  L189> Logga l'errore e genera un'eccezione per errori di connessione o altro
  L191> `return None`
- fn `async def request_get(self, url, **kwargs)` (L194-207)
  L195-204> Esegue una richiesta GET. Args: url (str): URL di destinazione. kwargs: Argomenti aggiuntivi. Returns: httpx.Response: La risposta HTTP o None.
  L205> `return await self.request("GET", url, headers=self.headers, **kwargs)`
- fn `async def request_post(self, url, **kwargs)` (L208-220)
  L209-218> Esegue una richiesta POST. Args: url (str): URL di destinazione. kwargs: Argomenti aggiuntivi. Returns: httpx.Response: La risposta HTTP o None.
  L219> `return await self.request("POST", url, headers=self.headers, **kwargs)`

### fn `async def retrieve_url(self, url)` (L251-278)
L248> # return dat.encode('utf-8', 'replace')
L252-260> Recupera il contenuto dell'URL come stringa decodificata. Args: url (str): L'URL da recuperare. Returns: str: Il contenuto decodificato o None.
L266> Handle gzip encoding
L270> Decode the content
L273> `return self._html_entity_decode(decoded_data)`
L277> `return None`

### fn `async def download_file(self, url, referer=None)` (L306-341)
L303> # return file path
L307-316> Scarica un file da un URL e lo salva in un file temporaneo. Args: url (str): URL del file. referer (str, optional): Header referer. Defaults to None. Returns: str: Il percorso del file temporaneo salvato o None.
L327> Handle gzip encoding
L331> Write to a temporary file
L336> `return file_path`
L340> `return None`

### fn `async def get_json_response(self, url, **kwargs)` (L344-392)
L342> per la classe base di Debrid
L345-354> Esegue una richiesta e restituisce il corpo JSON. Args: url (str): URL della richiesta. kwargs: Argomenti aggiuntivi (headers, timeout, method). Returns: dict: Il JSON decodificato o None.
L356> Prende method
L357> per default usa GET
L359> Combina gli header specificati con quelli di default
L361> Unisce gli header di default e quelli personalizzati
L363> Usa un timeout personalizzato o quello predefinito
L371> Solleva un'eccezione per errori HTTP 4xx o 5xx
L374> `return response.json()` — Restituisce la risposta finale dopo i reindirizzamenti
L377> `return None`
L381> `return None`
L383> Logga l'errore e restituisce una risposta informativa
L385> `return None`
L387> Logga l'errore e genera un'eccezione per errori di connessione o altro
L389> `return None`
L391> `return None`

### fn `async def download_torrent_file(self, download_url)` (L393-405)
L394-402> Scarica un file torrent in streaming. Args: download_url (str): L'URL del file torrent. Returns: bytes: Il contenuto binario del file torrent.
L405> `return await response.aread()`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L26: Gestisce sessioni HTTP asincrone thread-safe con supporto per HTTP/2, proxy e cookie.
- L38: Inizializza la sessione HTTP. Args: ...
- L46: self._lock = asyncio.Lock()  # Usa un lock asincrono
- L49: SOCKS5 Proxy setup (if provided)
- L53: per il check dei close
- L58: Chiude il client HTTPX e rilascia le risorse. Returns: ...
- L88-92: Verifica se la sessione è stata chiusa correttamente. | Logga un avviso, senza tentare di chiudere la sessione
- L111: @brief Execute `entity2char` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @par...
- L124: Then convert numerical entities (such as &#233;)
- L127: Then convert hexa entities (such as &#x00E9;)
- L132: Configura il proxy SOCKS5. Args: ...
- L159-172: Esegue una richiesta HTTP. Args: ... | async with self._lock: | Combina gli header specificati con quelli di default
- L176: Usa un timeout personalizzato o quello predefinito
- L185: Logga l'errore e restituisce una risposta informativa
- L189: Logga l'errore e genera un'eccezione per errori di connessione o altro
- L195: Esegue una richiesta GET. Args: ...
- L209: Esegue una richiesta POST. Args: ...
- L221-247: versione originale sincrona | def retrieve_url(url): | Return the content of the url page as a string | try: | req = urllib.request.Request(url, headers=headers) | response = urllib.request.urlopen(req) | except urllib.error.URLError as errno: | logger.error(" ".join(("Connection error:", str(errno.reason)))) | return | dat = response.read() | # Check if it is gzipped | if dat[:2] == b'\x1f\x8b': | # Data is gzip encoded, decode it | compressedstream = io.BytesIO(dat) | gzipper = gzip.GzipFile(fileobj=compressedstream) | extracted_data = gzipper.read() | dat = extracted_data | info = response.info() | charset = 'utf-8 | try: | ignore, charset = info['Content-Type'].split('charset=') | except Exception: | pass | dat = dat.decode(charset, 'replace') | dat = htmlentitydecode(dat)
- L252: Recupera il contenuto dell'URL come stringa decodificata. Args: ...
- L266: Handle gzip encoding
- L270: Decode the content
- L279-302: versione originale sincrona | def download_file(url, referer=None): | Download file at url and write it to a file, return the path to the file and the url | file, path = tempfile.mkstemp() | file = os.fdopen(file, "wb") | # Download url | req = urllib.request.Request(url, headers=headers) | if referer is not None: | req.add_header('referer', referer) | response = urllib.request.urlopen(req) | dat = response.read() | # Check if it is gzipped | if dat[:2] == b'\x1f\x8b': | # Data is gzip encoded, decode it | compressedstream = io.BytesIO(dat) | gzipper = gzip.GzipFile(fileobj=compressedstream) | extracted_data = gzipper.read() | dat = extracted_data | # Write it to a file | file.write(dat) | file.close()
- L307: Scarica un file da un URL e lo salva in un file temporaneo. Args: ...
- L327: Handle gzip encoding
- L331: Write to a temporary file
- L345-356: Esegue una richiesta e restituisce il corpo JSON. Args: ... | Prende method
- L359: Combina gli header specificati con quelli di default
- L363: Usa un timeout personalizzato o quello predefinito
- L383: Logga l'errore e restituisce una risposta informativa
- L387: Logga l'errore e genera un'eccezione per errori di connessione o altro
- L394: Scarica un file torrent in streaming. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`DEFAULT_TIMEOUT`|var|pub|23||
|`AsyncThreadSafeSession`|class|pub|25-224|class AsyncThreadSafeSession|
|`AsyncThreadSafeSession.__init__`|fn|priv|37-56|def __init__(self, proxy=None)|
|`AsyncThreadSafeSession.close`|fn|pub|57-66|async def close(self)|
|`AsyncThreadSafeSession.__aenter__`|fn|priv|67-75|async def __aenter__(self)|
|`AsyncThreadSafeSession.__aexit__`|fn|priv|76-86|async def __aexit__(self, exc_type, exc_val, exc_tb)|
|`AsyncThreadSafeSession.__del__`|fn|priv|87-94|def __del__(self)|
|`AsyncThreadSafeSession._html_entity_decode`|fn|priv|98-130|def _html_entity_decode(s)|
|`AsyncThreadSafeSession.entity2char`|fn|pub|110-121|def entity2char(m)|
|`AsyncThreadSafeSession._setup_proxy`|fn|priv|131-155|def _setup_proxy(self, proxy)|
|`AsyncThreadSafeSession.request`|fn|pub|158-193|async def request(self, method, url, **kwargs)|
|`AsyncThreadSafeSession.request_get`|fn|pub|194-207|async def request_get(self, url, **kwargs)|
|`AsyncThreadSafeSession.request_post`|fn|pub|208-220|async def request_post(self, url, **kwargs)|
|`retrieve_url`|fn|pub|251-278|async def retrieve_url(self, url)|
|`download_file`|fn|pub|306-341|async def download_file(self, url, referer=None)|
|`get_json_response`|fn|pub|344-392|async def get_json_response(self, url, **kwargs)|
|`download_torrent_file`|fn|pub|393-405|async def download_torrent_file(self, download_url)|


---

# cache.py | Python | 338L | 3 symbols | 8 imports | 32 comments
> Path: `src/debriddo/utils/cache.py`
> @file src/debriddo/utils/cache.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from typing import List
import sqlite3
import os
from debriddo.constants import CACHE_DATABASE_FILE
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
from datetime import datetime
from debriddo.utils.string_encoding import normalize
```

## Definitions

- var `TABLE_NAME = "cached_items"` (L20) — : @brief Exported constant `TABLE_NAME` used by runtime workflows.
### fn `def search_cache(config, media)` (L61-167)
L62-71> Cerca risultati nella cache SQLite per il media specificato. Args: config (dict): La configurazione dell'applicazione. media (Media): L'oggetto media da cercare. Returns: list: Lista di risultati trovati in cache o None.
L76> Verifica se la tabella esiste
L77> cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
L80> `return None`
L85> cursor.execute(f"""DELETE FROM '{TABLE_NAME}' WHERE created_at < datetime('now', '-{days} days');""")
L94> cicla sulle lingue
L127> Costruisci la query di filtro in base a `cache_search`
L133> Genera la query dinamica
L136> Esegui la query con i parametri
L140> Recupera i nomi delle colonne
L144> Trasforma ogni riga in un dizionario
L147> strighe di lista in lista
L162> `return cache_items`
L164> `return None`
L165> `return None`

### fn `def cache_results(torrents: List[TorrentItem], media)` (L168-338)
L169-178> Salva i risultati torrent nella cache SQLite. Args: torrents (List[TorrentItem]): Lista di item da cachare. media (Media): L'oggetto media associato. Returns: None
L182> Verifica se il file esiste (opzionale, SQLite lo crea comunque)
L185> Connetti al database (crea il file se non esiste)
L192> Verifica se la tabella esiste, altrimenti la crea
L193> cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
L203> crea dizionario dei titoli
L206> elenco delle entry da aggiungere
L212> Esegui una query per verificare l'esistenza dell'hash
L216> Restituisci True se il risultato non è None
L224> cicla sulle lingue
L249> clean_episode = int(media.episode.replace("E", ""))
L254> parsed_result = parse(result.raw_title) - già popolato
L266> True = contiene la stagione intera
L270> True = contiene la stagione intera
L274> False = contiene un episodio
L278> False = contiene un episodio
L282> prepara i dati per l'inserimento
L289> lista
L298> lista
L306> lista
L309> lista
L312> bool
L323> Estrai dinamicamente le colonne dalla lista di dizionari
L326> Placeholder per ogni colonna
L330> cursor.execute(f"""INSERT INTO {TABLE_NAME} ({", ".join(columns)}) VALUES ({placeholders}) """, data)

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L22-57: : @brief Exported constant `TABLE_SCHEMA` used by runtime workflows. | TABLE_SCHEMA = CREATE TABLE IF NOT EXISTS cached_items ( id INTEGER PRIMARY KEY AUTOINCREMENT, cr...
- L62: Cerca risultati nella cache SQLite per il media specificato. Args: ...
- L76-77: Verifica se la tabella esiste | cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
- L85: cursor.execute(f"""DELETE FROM '{TABLE_NAME}' WHERE created_at < datetime('now', '-{days} days');""")
- L94: cicla sulle lingue
- L127: Costruisci la query di filtro in base a `cache_search`
- L133: Genera la query dinamica
- L136: Esegui la query con i parametri
- L140: Recupera i nomi delle colonne
- L144: Trasforma ogni riga in un dizionario
- L147: strighe di lista in lista
- L169: Salva i risultati torrent nella cache SQLite. Args: ...
- L182: Verifica se il file esiste (opzionale, SQLite lo crea comunque)
- L185: Connetti al database (crea il file se non esiste)
- L192-193: Verifica se la tabella esiste, altrimenti la crea | cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
- L203: crea dizionario dei titoli
- L206: elenco delle entry da aggiungere
- L212: Esegui una query per verificare l'esistenza dell'hash
- L216: Restituisci True se il risultato non è None
- L224: cicla sulle lingue
- L249: clean_episode = int(media.episode.replace("E", ""))
- L254: parsed_result = parse(result.raw_title) - già popolato
- L282: prepara i dati per l'inserimento
- L323: Estrai dinamicamente le colonne dalla lista di dizionari
- L330: cursor.execute(f"""INSERT INTO {TABLE_NAME} ({", ".join(columns)}) VALUES ({placeholders}) """, data)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TABLE_NAME`|var|pub|20||
|`search_cache`|fn|pub|61-167|def search_cache(config, media)|
|`cache_results`|fn|pub|168-338|def cache_results(torrents: List[TorrentItem], media)|


---

# detection.py | Python | 44L | 1 symbols | 1 imports | 5 comments
> Path: `src/debriddo/utils/detection.py`
> @file src/debriddo/utils/detection.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
```

## Definitions

### fn `def detect_languages(torrent_name)` (L13-44)
L14-20> @brief Execute `detect_languages` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param torrent_name Runtime input parameter consumed by `detect_languages`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L42> `return ["en"]`
L44> `return languages`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L14: @brief Execute `detect_languages` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning....

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`detect_languages`|fn|pub|13-44|def detect_languages(torrent_name)|


---

# base_filter.py | Python | 61L | 5 symbols | 0 imports | 9 comments
> Path: `src/debriddo/utils/filter/base_filter.py`
> @file src/debriddo/utils/filter/base_filter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Definitions

### class `class BaseFilter` (L11-61)
L8> AUTHORS: aymene69
- fn `def __init__(self, config, additional_config=None)` `priv` (L16-28) L12> @brief Class `BaseFilter` encapsulates cohesive runtime behavior. @details Generated Doxygen bloc...
  L17-25> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @param additional_config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L29-39)
  L30-37> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `filter`. @param data Runtime input parameter consumed by `filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L38> `raise NotImplementedError`
- fn `def can_filter(self)` (L40-49) L30> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable c...
  L41-47> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `can_filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L48> `raise NotImplementedError`
- fn `def __call__(self, data)` `priv` (L50-61) L41> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callab...
  L51-58> @brief Execute `__call__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__call__`. @param data Runtime input parameter consumed by `__call__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L60> `return self.filter(data)`
  L61> `return data`

## Comments
- L7: VERSION: 0.0.35
- L17: @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...
- L51: @brief Execute `__call__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BaseFilter`|class|pub|11-61|class BaseFilter|
|`BaseFilter.__init__`|fn|priv|16-28|def __init__(self, config, additional_config=None)|
|`BaseFilter.filter`|fn|pub|29-39|def filter(self, data)|
|`BaseFilter.can_filter`|fn|pub|40-49|def can_filter(self)|
|`BaseFilter.__call__`|fn|priv|50-61|def __call__(self, data)|


---

# language_filter.py | Python | 64L | 4 symbols | 2 imports | 8 comments
> Path: `src/debriddo/utils/filter/language_filter.py`
> @file src/debriddo/utils/filter/language_filter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class LanguageFilter(BaseFilter)` : BaseFilter (L17-64)
- fn `def __init__(self, config)` `priv` (L22-32) L18> @brief Class `LanguageFilter` encapsulates cohesive runtime behavior. @details Generated Doxygen ...
  L23-30> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L33-55) L23> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable...
  L34-41> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `filter`. @param data Runtime input parameter consumed by `filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L54> `return filtered_data`
- fn `def can_filter(self)` (L56-64)
  L57-63> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `can_filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L64> `return bool(self.config.get('languages'))`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L34: @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L57: @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`LanguageFilter`|class|pub|17-64|class LanguageFilter(BaseFilter)|
|`LanguageFilter.__init__`|fn|priv|22-32|def __init__(self, config)|
|`LanguageFilter.filter`|fn|pub|33-55|def filter(self, data)|
|`LanguageFilter.can_filter`|fn|pub|56-64|def can_filter(self)|


---

# max_size_filter.py | Python | 57L | 4 symbols | 2 imports | 8 comments
> Path: `src/debriddo/utils/filter/max_size_filter.py`
> @file src/debriddo/utils/filter/max_size_filter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class MaxSizeFilter(BaseFilter)` : BaseFilter (L17-57)
- fn `def __init__(self, config, additional_config=None)` `priv` (L22-33) L18> @brief Class `MaxSizeFilter` encapsulates cohesive runtime behavior. @details Generated Doxygen b...
  L23-31> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @param additional_config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L34-48) L23> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable...
  L35-42> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `filter`. @param data Runtime input parameter consumed by `filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L47> `return filtered_data`
- fn `def can_filter(self)` (L49-57)
  L50-56> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `can_filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L57> `return int(self.config['maxSize']) > 0 and self.item_type == 'movie'`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L35: @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L50: @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MaxSizeFilter`|class|pub|17-57|class MaxSizeFilter(BaseFilter)|
|`MaxSizeFilter.__init__`|fn|priv|22-33|def __init__(self, config, additional_config=None)|
|`MaxSizeFilter.filter`|fn|pub|34-48|def filter(self, data)|
|`MaxSizeFilter.can_filter`|fn|pub|49-57|def can_filter(self)|


---

# quality_exclusion_filter.py | Python | 72L | 6 symbols | 2 imports | 8 comments
> Path: `src/debriddo/utils/filter/quality_exclusion_filter.py`
> @file src/debriddo/utils/filter/quality_exclusion_filter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refacto...

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class QualityExclusionFilter(BaseFilter)` : BaseFilter (L17-72)
- fn `def __init__(self, config)` `priv` (L22-32) L18> @brief Class `QualityExclusionFilter` encapsulates cohesive runtime behavior. @details Generated ...
  L23-30> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- var `RIPS = ["HDRIP", "BRRIP", "BDRIP", "WEBRIP", "TVRIP", "VODRIP", "HDRIP"]` (L33) L23> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable...
- var `CAMS = ["CAM", "TS", "TC", "R5", "DVDSCR", "HDTV", "PDTV", "DSR", "WORKPRINT", "VHSRIP", "HDCAM"]` (L34)
- fn `def filter(self, data)` (L36-63)
  L37-44> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `filter`. @param data Runtime input parameter consumed by `filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L62> `return filtered_items`
- fn `def can_filter(self)` (L64-72)
  L65-71> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `can_filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L72> `return self.config['exclusion'] is not None and len(self.config['exclusion']) > 0`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L37: @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L65: @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`QualityExclusionFilter`|class|pub|17-72|class QualityExclusionFilter(BaseFilter)|
|`QualityExclusionFilter.__init__`|fn|priv|22-32|def __init__(self, config)|
|`QualityExclusionFilter.RIPS`|var|pub|33||
|`QualityExclusionFilter.CAMS`|var|pub|34||
|`QualityExclusionFilter.filter`|fn|pub|36-63|def filter(self, data)|
|`QualityExclusionFilter.can_filter`|fn|pub|64-72|def can_filter(self)|


---

# results_per_quality_filter.py | Python | 65L | 4 symbols | 2 imports | 8 comments
> Path: `src/debriddo/utils/filter/results_per_quality_filter.py`
> @file src/debriddo/utils/filter/results_per_quality_filter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refac...

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class ResultsPerQualityFilter(BaseFilter)` : BaseFilter (L17-65)
- fn `def __init__(self, config)` `priv` (L22-32) L18> @brief Class `ResultsPerQualityFilter` encapsulates cohesive runtime behavior. @details Generated...
  L23-30> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L33-56) L23> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable...
  L34-41> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `filter`. @param data Runtime input parameter consumed by `filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L55> `return filtered_items`
- fn `def can_filter(self)` (L57-65)
  L58-64> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `can_filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L65> `return self.config['resultsPerQuality'] is not None and int(self.config['resultsPerQuality']) > 0`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L34: @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L58: @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ResultsPerQualityFilter`|class|pub|17-65|class ResultsPerQualityFilter(BaseFilter)|
|`ResultsPerQualityFilter.__init__`|fn|priv|22-32|def __init__(self, config)|
|`ResultsPerQualityFilter.filter`|fn|pub|33-56|def filter(self, data)|
|`ResultsPerQualityFilter.can_filter`|fn|pub|57-65|def can_filter(self)|


---

# filter_results.py | Python | 470L | 10 symbols | 9 imports | 71 comments
> Path: `src/debriddo/utils/filter_results.py`
> @file src/debriddo/utils/filter_results.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import re
from RTN import title_match, RTN, DefaultRanking, SettingsModel, sort_torrents
from RTN.exceptions import GarbageTorrent
from debriddo.utils.filter.language_filter import LanguageFilter
from debriddo.utils.filter.max_size_filter import MaxSizeFilter
from debriddo.utils.filter.quality_exclusion_filter import QualityExclusionFilter
from debriddo.utils.filter.results_per_quality_filter import ResultsPerQualityFilter
from debriddo.utils.filter.title_exclusion_filter import TitleExclusionFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### fn `def _match_complete_season(raw_title, numeric_season)` `priv` (L56-106)
L57-64> @brief Execute `_match_complete_season` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param raw_title Runtime input parameter consumed by `_match_complete_season`. @param numeric_season Runtime input parameter consumed by `_match_complete_season`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L67> Localized complete season must use season/complete labels from the same language.
L68> Support both "Season Snn ... COMPLETE" and "Season d ... COMPLETE" (numeric) formats
L74> Pattern 1: Season Snn ... COMPLETE (e.g., "Season S03 ... COMPLETE")
L87> `return True`
L89> Pattern 2: Season d ... COMPLETE (e.g., "Stagione 3 ... COMPLETA")
L102> `return True`
L104> `return False`

### fn `def _match_episode_range_pack(raw_title, numeric_season, numeric_episode)` `priv` (L107-132)
L108-116> @brief Execute `_match_episode_range_pack` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param raw_title Runtime input parameter consumed by `_match_episode_range_pack`. @param numeric_season Runtime input parameter consumed by `_match_episode_range_pack`. @param numeric_episode Runtime input parameter consumed by `_match_episode_range_pack`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L129> `return True`
L130> `return False`

### fn `def _match_season_episode_pair(raw_title, numeric_season, numeric_episode)` `priv` (L133-154)
L134-142> @brief Execute `_match_season_episode_pair` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param raw_title Runtime input parameter consumed by `_match_season_episode_pair`. @param numeric_season Runtime input parameter consumed by `_match_season_episode_pair`. @param numeric_episode Runtime input parameter consumed by `_match_season_episode_pair`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L152> `return season_episode_match.search(title) is not None`

### fn `def _match_title_with_season(raw_title, media_title, numeric_season)` `priv` (L155-207)
L156-161> Match title followed by season in three forms for series: 1. <title>.+Snn (basic season format) 2. <title>.+Season Snn (localized season label with Snn) 3. <title>.+Season d (localized season label with numeric season)
L163> Normalize title to handle dots, spaces, underscores as separators
L164> Replace each word separator in media_title with flexible separator pattern
L167> Pattern 1: <title>.+Snn (e.g., "Person of Interest ... S03" or "Person.Of.Interest.S03")
L173> `return True`
L175> Pattern 2 and 3: <title>.+Season Snn or <title>.+Season d (localized)
L177> Pattern 2: <title>.+Season Snn (e.g., "Person of Interest ... Season S03")
L189> `return True`
L191> Pattern 3: <title>.+Season d (e.g., "Person of Interest ... Stagione 3")
L203> `return True`
L205> `return False`

### fn `def sort_quality(item)` (L208-236)
L209> if item.parsed_data.data.resolution is None or item.parsed_data.data.resolution == "unknown" or item.parsed_data.data.resolution == "":
L210> return float('inf'), True
L212> # TODO: first resolution?
L213> return quality_order.get(item.parsed_data.data.resolution[0],
L214> float('inf')), item.parsed_data.data.resolution is None
L216> Controlla la presenza di parsed_data e data
L217-223> @brief Execute `sort_quality` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param item Runtime input parameter consumed by `sort_quality`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L225> `return float('inf'), True` — True = non trovato
L229> Gestione dei casi con risoluzione mancante o sconosciuta
L231> `return float('inf'), True` — True = non trovato
L233> Ritorna il valore di quality_order con fallback a infinito
L234> `return quality_order.get(resolution, float('inf')), False` — False = trovato

### fn `def items_sort(items, config)` (L237-297)
L240-247> @brief Execute `items_sort` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param items Runtime input parameter consumed by `items_sort`. @param config Runtime input parameter consumed by `items_sort`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L252> custom_ranks={
L253> uhd": CustomRank(enable=True, fetch=True, rank=200),
L254> hdr": CustomRank(enable=True, fetch=True, rank=100),
L255> }
L258> Se genera l'eccezione poi l'ordinamento dei TorrentItems basato sui Torrent non funziona
L259> if rank < self.settings.options["remove_ranks_under"]:
L260> raise GarbageTorrent(f"'{raw_title}' does not meet the minimum rank requirement, got rank of {rank}")
L262> maximun negative value => non ne leva nessuno
L264> default: remove_ranks_under = -10000,
L265> 32 bit?
L269> torrents = [rtn.rank(item.raw_title, item.info_hash) for item in items]
L288> `return sorted(items, key=sort_quality)`
L290> `return sorted(items, key=lambda x: int(x.size))`
L292> `return sorted(items, key=lambda x: int(x.size), reverse=True)`
L294> `return sorted(items, key=lambda x: (sort_quality(x), -int(x.size)))`
L295> `return items`

### fn `def filter_out_non_matching(items, season, episode)` (L314-350)
L311> return filtered_items
L315-323> @brief Execute `filter_out_non_matching` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param items Runtime input parameter consumed by `filter_out_non_matching`. @param season Runtime input parameter consumed by `filter_out_non_matching`. @param episode Runtime input parameter consumed by `filter_out_non_matching`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L326> logger.debug(item.parsed_data)
L348> `return filtered_items`

### fn `def remove_non_matching_title(items, titles, media)` (L351-404)
L352-360> @brief Execute `remove_non_matching_title` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param items Runtime input parameter consumed by `remove_non_matching_title`. @param titles Runtime input parameter consumed by `remove_non_matching_title`. @param media Runtime input parameter consumed by `remove_non_matching_title`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L362> default: threshold: float = 0.85
L369> For series, use season-aware matching
L374> Check if title has season-aware match (validates season is correct)
L379> Generic title match only if no season info in raw_title
L380> (fallback for items without explicit season in title)
L382> Check if raw_title contains any season pattern
L389> Only accept generic match if no season pattern found in title
L394> For movies, use generic title match
L402> `return filtered_items`

### fn `def filter_items(items, media, config)` (L405-457)
L406> vengono processati nell'ordine in cui sono dichiarati
L407-415> @brief Execute `filter_items` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param items Runtime input parameter consumed by `filter_items`. @param media Runtime input parameter consumed by `filter_items`. @param config Runtime input parameter consumed by `filter_items`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L418> Max size filtering only happens for movies, so it
L424> Filtering out 100% non-matching for series
L432> TODO: is titles[0] always the correct title? Maybe loop through all titles and get the highest match?
L438> finché ci sono risultati
L447> per esempio se ci sono solo versioni in inglese, le tiene e ritorna quelle
L455> `return items`

### fn `def sort_items(items, config)` (L458-470)
L459-466> @brief Execute `sort_items` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param items Runtime input parameter consumed by `sort_items`. @param config Runtime input parameter consumed by `sort_items`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L468> `return items_sort(items, config)`
L470> `return items`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L57: @brief Execute `_match_complete_season` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L67-68: Localized complete season must use season/complete labels from the same language. | Support both "Season Snn ... COMPLETE" and "Season d ... COMPLETE" (numeric) formats
- L74: Pattern 1: Season Snn ... COMPLETE (e.g., "Season S03 ... COMPLETE")
- L89: Pattern 2: Season d ... COMPLETE (e.g., "Stagione 3 ... COMPLETA")
- L108: @brief Execute `_match_episode_range_pack` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static r...
- L134: @brief Execute `_match_season_episode_pair` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static ...
- L156-164: Match title followed by season in three forms for series: 1. <title>.+Snn (basic season format) 2... | Normalize title to handle dots, spaces, underscores as separators | Replace each word separator in media_title with flexible separator pattern
- L167: Pattern 1: <title>.+Snn (e.g., "Person of Interest ... S03" or "Person.Of.Interest.S03")
- L175-177: Pattern 2 and 3: <title>.+Season Snn or <title>.+Season d (localized) | Pattern 2: <title>.+Season Snn (e.g., "Person of Interest ... Season S03")
- L191: Pattern 3: <title>.+Season d (e.g., "Person of Interest ... Stagione 3")
- L209-223: if item.parsed_data.data.resolution is None or item.parsed_data.data.resolution == "unknown" or i... | return float('inf'), True | # TODO: first resolution? | return quality_order.get(item.parsed_data.data.resolution[0], | float('inf')), item.parsed_data.data.resolution is None | Controlla la presenza di parsed_data e data | @brief Execute `sort_quality` operational logic. @details Generated Doxygen block describing call...
- L229: Gestione dei casi con risoluzione mancante o sconosciuta
- L233: Ritorna il valore di quality_order con fallback a infinito
- L240: @brief Execute `items_sort` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...
- L252-255: custom_ranks={ | uhd": CustomRank(enable=True, fetch=True, rank=200), | hdr": CustomRank(enable=True, fetch=True, rank=100), | }
- L258-264: Se genera l'eccezione poi l'ordinamento dei TorrentItems basato sui Torrent non funziona | if rank < self.settings.options["remove_ranks_under"]: | raise GarbageTorrent(f"'{raw_title}' does not meet the minimum rank requirement, got rank of {ran... | maximun negative value => non ne leva nessuno | default: remove_ranks_under = -10000,
- L269: torrents = [rtn.rank(item.raw_title, item.info_hash) for item in items]
- L298-310: def filter_season_episode(items, season, episode, config): | filtered_items = [] | for item in items: | if config['language'] == "ru": | if "S" + str(int(season.replace("S", ""))) + "E" + str( | int(episode.replace("E", ""))) not in item['title']: | if re.search(rf'\bS{re.escape(str(int(season.replace("S", ""))))}\b', item['title']) is None: | continue | if re.search(rf'\b{season}\s?{episode}\b', item['title']) is None: | if re.search(rf'\b{season}\b', item['title']) is None: | continue | filtered_items.append(item)
- L315: @brief Execute `filter_out_non_matching` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static rea...
- L326: logger.debug(item.parsed_data)
- L352-362: @brief Execute `remove_non_matching_title` operational logic. @details Generated Doxygen block de... | default: threshold: float = 0.85
- L369: For series, use season-aware matching
- L374: Check if title has season-aware match (validates season is correct)
- L379-382: Generic title match only if no season info in raw_title | (fallback for items without explicit season in title) | Check if raw_title contains any season pattern
- L389: Only accept generic match if no season pattern found in title
- L394: For movies, use generic title match
- L406-415: vengono processati nell'ordine in cui sono dichiarati | @brief Execute `filter_items` operational logic. @details Generated Doxygen block describing call...
- L424: Filtering out 100% non-matching for series
- L432: TODO: is titles[0] always the correct title? Maybe loop through all titles and get the highest match?
- L447: per esempio se ci sono solo versioni in inglese, le tiene e ritorna quelle
- L459: @brief Execute `sort_items` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`_match_complete_season`|fn|priv|56-106|def _match_complete_season(raw_title, numeric_season)|
|`_match_episode_range_pack`|fn|priv|107-132|def _match_episode_range_pack(raw_title, numeric_season, ...|
|`_match_season_episode_pair`|fn|priv|133-154|def _match_season_episode_pair(raw_title, numeric_season,...|
|`_match_title_with_season`|fn|priv|155-207|def _match_title_with_season(raw_title, media_title, nume...|
|`sort_quality`|fn|pub|208-236|def sort_quality(item)|
|`items_sort`|fn|pub|237-297|def items_sort(items, config)|
|`filter_out_non_matching`|fn|pub|314-350|def filter_out_non_matching(items, season, episode)|
|`remove_non_matching_title`|fn|pub|351-404|def remove_non_matching_title(items, titles, media)|
|`filter_items`|fn|pub|405-457|def filter_items(items, media, config)|
|`sort_items`|fn|pub|458-470|def sort_items(items, config)|


---

# title_exclusion_filter.py | Python | 60L | 4 symbols | 2 imports | 8 comments
> Path: `src/debriddo/utils/filter/title_exclusion_filter.py`
> @file src/debriddo/utils/filter/title_exclusion_filter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactori...

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TitleExclusionFilter(BaseFilter)` : BaseFilter (L17-60)
- fn `def __init__(self, config)` `priv` (L22-32) L18> @brief Class `TitleExclusionFilter` encapsulates cohesive runtime behavior. @details Generated Do...
  L23-30> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @param config Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L33-51) L23> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable...
  L34-41> @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `filter`. @param data Runtime input parameter consumed by `filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L50> `return filtered_items`
- fn `def can_filter(self)` (L52-60)
  L53-59> @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `can_filter`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L60> `return self.config['exclusionKeywords'] is not None and len(self.config['exclusionKeywords']) > 0`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L34: @brief Execute `filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param se...
- L53: @brief Execute `can_filter` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @para...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TitleExclusionFilter`|class|pub|17-60|class TitleExclusionFilter(BaseFilter)|
|`TitleExclusionFilter.__init__`|fn|priv|22-32|def __init__(self, config)|
|`TitleExclusionFilter.filter`|fn|pub|33-51|def filter(self, data)|
|`TitleExclusionFilter.can_filter`|fn|pub|52-60|def can_filter(self)|


---

# general.py | Python | 75L | 3 symbols | 2 imports | 7 comments
> Path: `src/debriddo/utils/general.py`
> @file src/debriddo/utils/general.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from RTN import parse
from debriddo.utils.logger import setup_logger
```

## Definitions

### fn `def season_episode_in_filename(filename, season, episode)` (L24-39)
L25-33> @brief Execute `season_episode_in_filename` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param filename Runtime input parameter consumed by `season_episode_in_filename`. @param season Runtime input parameter consumed by `season_episode_in_filename`. @param episode Runtime input parameter consumed by `season_episode_in_filename`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L35> `return False`
L37> `return int(season.replace("S", "")) in parsed_name.seasons and int(episode.replace("E", "")) in parsed_name.episodes`

### fn `def get_info_hash_from_magnet(magnet: str)` (L40-62)
L41-47> @brief Execute `get_info_hash_from_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param magnet Runtime input parameter consumed by `get_info_hash_from_magnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L51> `return None`
L60> `return info_hash.lower()`

### fn `def is_video_file(filename)` (L63-75)
L64-70> @brief Execute `is_video_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param filename Runtime input parameter consumed by `is_video_file`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L73> `return False`
L75> `return filename[extension_idx:] in video_formats`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L25: @brief Execute `season_episode_in_filename` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static ...
- L41: @brief Execute `get_info_hash_from_magnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static r...
- L64: @brief Execute `is_video_file` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @p...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`season_episode_in_filename`|fn|pub|24-39|def season_episode_in_filename(filename, season, episode)|
|`get_info_hash_from_magnet`|fn|pub|40-62|def get_info_hash_from_magnet(magnet: str)|
|`is_video_file`|fn|pub|63-75|def is_video_file(filename)|


---

# logger.py | Python | 118L | 16 symbols | 2 imports | 24 comments
> Path: `src/debriddo/utils/logger.py`
> @file src/debriddo/utils/logger.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import os
import logging
```

## Definitions

### class `class CustomFormatter(logging.Formatter)` : logging.Formatter (L14-74)
L32> Spaziatura
L33> INFO:
L34> DEBUG:
L35> WARNING:
L36> ERROR:
L37> CRITICAL:
- var `WHITE = "\033[97m"` (L17) L15> Logging Formatter to add colors and count warning / errors
- var `WHITE_BOLD = "\033[1;97m"` (L18)
- var `GREY = "\033[90m"` (L19)
- var `LIGHT_GREY = "\033[37m"` (L20)
- var `CYAN = "\033[36m"` (L21)
- var `MAGENTA = "\033[35m"` (L22)
- var `BLUE = "\033[34m"` (L23)
- var `RED = "\033[31m"` (L24)
- var `GREEN = "\033[32m"` (L25)
- var `YELLOW = "\033[33m"` (L26)
- var `RED_BOLD = "\033[1;31m"` (L27)
- var `RESET = "\033[0m"` (L30) L29> Reset color
- var `FORMATS =` (L52)
- fn `def format(self, record)` (L60-74)
  L61-69> Formatta il record di log applicando colori e stili. Args: record (logging.LogRecord): Il record di log da formattare. Returns: str: Il messaggio di log formattato.
  L72> `return formatter.format(record)`

### fn `def setup_logger(name, debug=None)` (L75-111)
L76-85> Configura e restituisce un logger con formatter personalizzato. Args: name (str): Il nome del logger. debug (bool, optional): Se True, imposta il livello a DEBUG. Defaults to None. Returns: logging.Logger: L'istanza del logger configurata.
L88> get environment
L95> define logging level
L102> `return logger`
L104> Create console handler with a higher log level
L106> Adjust as needed: DEBUG, INFO
L110> `return logger`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L32-37: Spaziatura | INFO: | DEBUG: | WARNING: | ERROR: | CRITICAL:
- L61: Formatta il record di log applicando colori e stili. Args: ...
- L76: Configura e restituisce un logger con formatter personalizzato. Args: ...
- L88: get environment
- L95: define logging level
- L104: Create console handler with a higher log level
- L112-118: Example usage | logger = setup_logger(__name__) | logger.debug('This is a debug message') | logger.info('This is an info message') | logger.warning('This is a warning message') | logger.error('This is an error message') | logger.critical('This is a critical message')

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CustomFormatter`|class|pub|14-74|class CustomFormatter(logging.Formatter)|
|`CustomFormatter.WHITE`|var|pub|17||
|`CustomFormatter.WHITE_BOLD`|var|pub|18||
|`CustomFormatter.GREY`|var|pub|19||
|`CustomFormatter.LIGHT_GREY`|var|pub|20||
|`CustomFormatter.CYAN`|var|pub|21||
|`CustomFormatter.MAGENTA`|var|pub|22||
|`CustomFormatter.BLUE`|var|pub|23||
|`CustomFormatter.RED`|var|pub|24||
|`CustomFormatter.GREEN`|var|pub|25||
|`CustomFormatter.YELLOW`|var|pub|26||
|`CustomFormatter.RED_BOLD`|var|pub|27||
|`CustomFormatter.RESET`|var|pub|30||
|`CustomFormatter.FORMATS`|var|pub|52||
|`CustomFormatter.format`|fn|pub|60-74|def format(self, record)|
|`setup_logger`|fn|pub|75-111|def setup_logger(name, debug=None)|


---

# multi_thread.py | Python | 30L | 2 symbols | 2 imports | 6 comments
> Path: `src/debriddo/utils/multi_thread.py`
> @file src/debriddo/utils/multi_thread.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import asyncio
from debriddo.constants import RUN_IN_MULTI_THREAD
```

## Definitions

- var `MULTI_THREAD = RUN_IN_MULTI_THREAD` (L14) — : @brief Exported constant `MULTI_THREAD` used by runtime workflows.
### fn `def run_coroutine_in_thread(coro)` (L17-30)
L16> Funzione per eseguire una coroutine in un nuovo event loop sul thread del pool
L18-24> @brief Execute `run_coroutine_in_thread` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param coro Runtime input parameter consumed by `run_coroutine_in_thread`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L28> `return new_loop.run_until_complete(coro)`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L18: @brief Execute `run_coroutine_in_thread` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static rea...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MULTI_THREAD`|var|pub|14||
|`run_coroutine_in_thread`|fn|pub|17-30|def run_coroutine_in_thread(coro)|


---

# novaprinter.py | Python | 108L | 6 symbols | 1 imports | 26 comments
> Path: `src/debriddo/utils/novaprinter.py`
> @file src/debriddo/utils/novaprinter.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class PrettyPrint` (L24-108)
- fn `def __init__(self)` `priv` (L29-40) L25> @brief Class `PrettyPrint` encapsulates cohesive runtime behavior. @details Generated Doxygen blo...
  L30> Inizializza una lista per salvare tutte le stringhe stampate
  L31-37> @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__init__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __call__(self, dictionary): # *args, **kwargs)` `priv` (L41-56)
  L42> Se serve comunque stampare l'dictionary_list, puoi usare:
  L43-50> @brief Execute `__call__` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `__call__`. @param dictionary Runtime input parameter consumed by `__call__`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L52> convert size to bytes
- fn `def __anySizeToBytes(self, size_string)` `priv` (L57-84)
  L58-60> Convert a string like '1 KB' to '1024' (bytes)
  L61> separate integer from unit
  L71> `return -1`
  L73> `return -1`
  L76> `return int(size)`
  L79> convert
  L83> `return int(size)`
- fn `def get(self)` (L85-98)
  L86> Restituisci l'elenco di tutte le stringhe accumulate
  L87-93> @brief Execute `get` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `get`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
  L95> `return self.dictionary_list`
  L97> `return None`
- fn `def clear(self)` (L99-108)
  L100> Resetta l'elenco delle stringhe salvate
  L101-107> @brief Execute `clear` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param self Runtime input parameter consumed by `clear`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Comments
- L7-20: VERSION: 0.0.35 | AUTHORS: Ogekuri | def prettyPrinter(dictionary): | dictionary['size'] = anySizeToBytes(dictionary['size']) | outtext = "|".join((dictionary["link"], dictionary["name"].replace("|", " "), | str(dictionary["size"]), str(dictionary["seeds"]), | str(dictionary["leech"]), dictionary["engine_url"])) | if 'desc_link' in dictionary: | outtext = "|".join((outtext, dictionary["desc_link"])) | # fd 1 is stdout | with open(1, 'w', encoding='utf-8', closefd=False) as utf8stdout: | print(outtext, file=utf8stdout)
- L30-37: Inizializza una lista per salvare tutte le stringhe stampate | @brief Execute `__init__` operational logic. @details Generated Doxygen block describing callable...
- L42-52: Se serve comunque stampare l'dictionary_list, puoi usare: | @brief Execute `__call__` operational logic. @details Generated Doxygen block describing callable... | convert size to bytes
- L58-61: Convert a string like '1 KB' to '1024' (bytes) | separate integer from unit
- L79: convert
- L86-93: Restituisci l'elenco di tutte le stringhe accumulate | @brief Execute `get` operational logic. @details Generated Doxygen block describing callable cont...
- L100-107: Resetta l'elenco delle stringhe salvate | @brief Execute `clear` operational logic. @details Generated Doxygen block describing callable co...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`PrettyPrint`|class|pub|24-108|class PrettyPrint|
|`PrettyPrint.__init__`|fn|priv|29-40|def __init__(self)|
|`PrettyPrint.__call__`|fn|priv|41-56|def __call__(self, dictionary): # *args, **kwargs)|
|`PrettyPrint.__anySizeToBytes`|fn|priv|57-84|def __anySizeToBytes(self, size_string)|
|`PrettyPrint.get`|fn|pub|85-98|def get(self)|
|`PrettyPrint.clear`|fn|pub|99-108|def clear(self)|


---

# parse_config.py | Python | 57L | 3 symbols | 1 imports | 13 comments
> Path: `src/debriddo/utils/parse_config.py`
> @file src/debriddo/utils/parse_config.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from debriddo.utils.string_encoding import decode_lzstring, encode_lzstring
```

## Definitions

### fn `def parse_config(encoded_config)` (L14-28)
L13> wrapping alla decode_lzstring per gestire eventuali retro-compatibità
L16> decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
L17-23> @brief Execute `parse_config` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param encoded_config Runtime input parameter consumed by `parse_config`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L26> `return config`

### fn `def parse_query(encoded_query)` (L30-43)
L29> wrapping alla decode_lzstring per gestire eventuali retro-compatibità
L32> decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
L33-39> @brief Execute `parse_query` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param encoded_query Runtime input parameter consumed by `parse_query`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L42> `return query`

### fn `def encode_query(query)` (L45-57)
L44> wrapping alla encode_lzstring per gestire eventuali retro-compatibità
L47> decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
L48-54> @brief Execute `encode_query` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param query Runtime input parameter consumed by `encode_query`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L57> `return encoded_query`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L16-23: decodifica utilizzando l'algoritmo di LZString con encodeURIComponent | @brief Execute `parse_config` operational logic. @details Generated Doxygen block describing call...
- L32-39: decodifica utilizzando l'algoritmo di LZString con encodeURIComponent | @brief Execute `parse_query` operational logic. @details Generated Doxygen block describing calla...
- L47-54: decodifica utilizzando l'algoritmo di LZString con encodeURIComponent | @brief Execute `encode_query` operational logic. @details Generated Doxygen block describing call...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`parse_config`|fn|pub|14-28|def parse_config(encoded_config)|
|`parse_query`|fn|pub|30-43|def parse_query(encoded_query)|
|`encode_query`|fn|pub|45-57|def encode_query(query)|


---

# stremio_parser.py | Python | 238L | 8 symbols | 8 imports | 30 comments
> Path: `src/debriddo/utils/stremio_parser.py`
> @file src/debriddo/utils/stremio_parser.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
import queue
import threading
from typing import List
from debriddo.models.media import Media
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
from debriddo.utils.parse_config import encode_query
```

## Definitions

### fn `def get_emoji(language)` (L23-47)
L22> TODO: Languages
L24-30> @brief Execute `get_emoji` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param language Runtime input parameter consumed by `get_emoji`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L45> `return emoji_dict.get(language, "🇬🇧")`

- var `INSTANTLY_AVAILABLE = "[⚡"` (L49) — : @brief Exported constant `INSTANTLY_AVAILABLE` used by runtime workflows.
- var `DOWNLOAD_REQUIRED = "[⬇️"` (L51) — : @brief Exported constant `DOWNLOAD_REQUIRED` used by runtime workflows.
- var `DIRECT_TORRENT = "[🏴‍☠️"` (L53) — : @brief Exported constant `DIRECT_TORRENT` used by runtime workflows.
### fn `def filter_by_availability(item)` (L56-69)
L57-63> @brief Execute `filter_by_availability` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param item Runtime input parameter consumed by `filter_by_availability`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L65> `return 0`
L67> `return 1`

### fn `def filter_by_direct_torrnet(item)` (L70-83)
L71-77> @brief Execute `filter_by_direct_torrnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param item Runtime input parameter consumed by `filter_by_direct_torrnet`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L79> `return 1`
L81> `return 0`

### fn `def parse_to_debrid_stream(torrent_item: TorrentItem, config_url, node_url, playtorrent, results: queue.Queue, media: Media)` (L84-201)
L85-96> @brief Execute `parse_to_debrid_stream` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param torrent_item Runtime input parameter consumed by `parse_to_debrid_stream`. @param config_url Runtime input parameter consumed by `parse_to_debrid_stream`. @param node_url Runtime input parameter consumed by `parse_to_debrid_stream`. @param playtorrent Runtime input parameter consumed by `parse_to_debrid_stream`. @param results Runtime input parameter consumed by `parse_to_debrid_stream`. @param media Runtime input parameter consumed by `parse_to_debrid_stream`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L113> TODO: Always take the first resolution, is that the best one?
L114> resolution = parsed_data.resolution[0] if len(parsed_data.resolution) > 0 else "Unknown
L115> name += f"{resolution}" + (f"\n({'|'.join(parsed_data.quality)})" if len(parsed_data.quality) > 0 else "")
L117> from cache
L123> seson package
L134> formattazione pannello sinistro gui
L157> query_encoded = encode64(json.dumps(torrent_item.to_debrid_stream_query(media))).replace('=', '%3D')
L158> TODO: come mai sostituiva l'=?
L167> TODO: Use parsed title?
L172> warning per url troppo lunghi
L173> TODO: da decidere il valore
L177> Se è abilitato il play diretto del torrent lo aggiunge in coda
L178> Rimmosso 'and torrent_item.privacy == "public":', non devo condividere il torrent, non il file sulla rete torrent
L181> formattazione pannello sinistro gui
L185> if len(parsed_data.quality) > 0 and parsed_data.quality[0] != "Unknown" and \
L186> parsed_data.quality[0] != "":
L187> name += f"({'|'.join(parsed_data.quality)})
L195> TODO: Use parsed title?
L197> sources": ["tracker:" + tracker for tracker in torrent_item.trackers]

### fn `def parse_to_stremio_streams(torrent_items: List[TorrentItem], config, config_url, node_url, media)` (L202-238)
L203-213> @brief Execute `parse_to_stremio_streams` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param torrent_items Runtime input parameter consumed by `parse_to_stremio_streams`. @param config Runtime input parameter consumed by `parse_to_stremio_streams`. @param config_url Runtime input parameter consumed by `parse_to_stremio_streams`. @param node_url Runtime input parameter consumed by `parse_to_stremio_streams`. @param media Runtime input parameter consumed by `parse_to_stremio_streams`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L232> `return []`
L235> ordinamento predefinito
L238> `return stream_list`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L24: @brief Execute `get_emoji` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param...
- L57: @brief Execute `filter_by_availability` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L71: @brief Execute `filter_by_direct_torrnet` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static re...
- L85: @brief Execute `parse_to_debrid_stream` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reas...
- L113-117: TODO: Always take the first resolution, is that the best one? | resolution = parsed_data.resolution[0] if len(parsed_data.resolution) > 0 else "Unknown | name += f"{resolution}" + (f"\n({'|'.join(parsed_data.quality)})" if len(parsed_data.quality) > 0... | from cache
- L123: seson package
- L134: formattazione pannello sinistro gui
- L157-158: query_encoded = encode64(json.dumps(torrent_item.to_debrid_stream_query(media))).replace('=', '%3D') | TODO: come mai sostituiva l'=?
- L172-173: warning per url troppo lunghi | TODO: da decidere il valore
- L177: Se è abilitato il play diretto del torrent lo aggiunge in coda
- L181: formattazione pannello sinistro gui
- L185-187: if len(parsed_data.quality) > 0 and parsed_data.quality[0] != "Unknown" and \ | parsed_data.quality[0] != "": | name += f"({'|'.join(parsed_data.quality)})
- L197: sources": ["tracker:" + tracker for tracker in torrent_item.trackers]
- L203: @brief Execute `parse_to_stremio_streams` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static re...
- L235: ordinamento predefinito

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_emoji`|fn|pub|23-47|def get_emoji(language)|
|`INSTANTLY_AVAILABLE`|var|pub|49||
|`DOWNLOAD_REQUIRED`|var|pub|51||
|`DIRECT_TORRENT`|var|pub|53||
|`filter_by_availability`|fn|pub|56-69|def filter_by_availability(item)|
|`filter_by_direct_torrnet`|fn|pub|70-83|def filter_by_direct_torrnet(item)|
|`parse_to_debrid_stream`|fn|pub|84-201|def parse_to_debrid_stream(torrent_item: TorrentItem, con...|
|`parse_to_stremio_streams`|fn|pub|202-238|def parse_to_stremio_streams(torrent_items: List[TorrentI...|


---

# string_encoding.py | Python | 82L | 3 symbols | 4 imports | 11 comments
> Path: `src/debriddo/utils/string_encoding.py`
> @file src/debriddo/utils/string_encoding.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
import json
import re
from unidecode import unidecode
import lzstring
```

## Definitions

### fn `def encode_lzstring(json_value, tag)` (L17-37)
L18-25> @brief Execute `encode_lzstring` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param json_value Runtime input parameter consumed by `encode_lzstring`. @param tag Runtime input parameter consumed by `encode_lzstring`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L28> `raise ValueError("Incompatible tag encoding lz-string")`
L33> `raise ValueError(f"An error occurred decoding lz-string: {e}")`
L35> `return data`

### fn `def decode_lzstring(data, tag)` (L38-63)
L39-46> @brief Execute `decode_lzstring` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param data Runtime input parameter consumed by `decode_lzstring`. @param tag Runtime input parameter consumed by `decode_lzstring`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L49> Se il prefisso "C_" è presente, rimuovilo
L53> `raise ValueError("Incompatible tag decoding lz-string")`
L57> `raise ValueError("Failed to decompress lz-string payload")`
L60> `raise ValueError(f"An error occurred decoding lz-string: {e}")`
L62> `return json_value`

### fn `def normalize(string)` (L64-82)
L65> kožušček -> kozuscek
L66> 北亰 -> Bei Jing
L67> François -> Francois
L68-74> @brief Execute `normalize` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. @param string Runtime input parameter consumed by `normalize`. @return Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
L76> ’s ->
L80> `return string`

## Comments
- L7-9: VERSION: 0.0.35 | AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L18: @brief Execute `encode_lzstring` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L39: @brief Execute `decode_lzstring` operational logic. @details Generated Doxygen block describing callable contract for LLM-native static reasoning. ...
- L49: Se il prefisso "C_" è presente, rimuovilo
- L65-74: kožušček -> kozuscek | 北亰 -> Bei Jing | François -> Francois | @brief Execute `normalize` operational logic. @details Generated Doxygen block describing callabl...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`encode_lzstring`|fn|pub|17-37|def encode_lzstring(json_value, tag)|
|`decode_lzstring`|fn|pub|38-63|def decode_lzstring(data, tag)|
|`normalize`|fn|pub|64-82|def normalize(string)|


---

# config.js | JavaScript | 236L | 3 symbols | 0 imports | 11 comments
> Path: `src/debriddo/web/config.js`
> variabili generali

## Definitions

### fn `function setElementDisplay(elementId, displayStatus)` (L9-15)
L6> const engines = ['thepiratebay', 'one337x', 'limetorrents', 'torrentproject', 'torrentz', 'torrentgalaxy', 'therarbg', 'ilcorsaronero', 'ilcorsarob...
L12> `return;`

### fn `function loadData()` (L18-236)
L17> caricamento dei parametri
L21> vecchia codifica con atob/btoa
L22> if (data && data[1].startsWith("ey")) {
L23> data = atob(data[1]);
L24> data = JSON.parse(data);
L26> Nuovo formato compresso (con LZString ad esempio)
L193> `return false;`
L196> let stremio_link = `${window.location.host}/${btoa(JSON.stringify(data))}/manifest.json`;
L197> let config_link = `${window.location.host}/${btoa(JSON.stringify(data))}/configure`;
L199> codifica compressa al posto del btoa
L213> `return;`
L226> `return;`

### fn `function getLink(method)` (L97-236)
L193> `return false;`
L196> let stremio_link = `${window.location.host}/${btoa(JSON.stringify(data))}/manifest.json`;
L197> let config_link = `${window.location.host}/${btoa(JSON.stringify(data))}/configure`;
L199> codifica compressa al posto del btoa
L213> `return;`
L226> `return;`

## Comments
- L21-26: vecchia codifica con atob/btoa | if (data && data[1].startsWith("ey")) { | data = atob(data[1]); | data = JSON.parse(data); | Nuovo formato compresso (con LZString ad esempio)
- L196-199: let stremio_link = `${window.location.host}/${btoa(JSON.stringify(data))}/manifest.json`; | let config_link = `${window.location.host}/${btoa(JSON.stringify(data))}/configure`; | codifica compressa al posto del btoa

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`setElementDisplay`|fn||9-15|function setElementDisplay(elementId, displayStatus)|
|`loadData`|fn||18-236|function loadData()|
|`getLink`|fn||97-236|function getLink(method)|


---

# lz-string.min.js | JavaScript | 1L | 1 symbols | 0 imports | 0 comments
> Path: `src/debriddo/web/lz-string.min.js`

## Definitions

- fn `var LZString=function(){var r=String.fromCharCode,o="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",n="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$",e={};function t(r,o){if(!e[r]){e[r]={};for(var n=0;n<r.length;n++)e[r][r.charAt(n)]=n}return e[r][o]}var i={compressToBase64:function(r){if(null==r)return"";var n=i._compress(r,6,function(r){return o.charAt(r)});switch(n.length%4){default:case 0:return n;case 1:return n+"===";case 2:return n+"==";case 3:return n+"="}},decompressFromBase64:function(r){return null==r?"":""==r?null:i._decompress(r.length,32,function(n){return t(o,r.charAt(n))})},compressToUTF16:function(o){return null==o?"":i._compress(o,15,function(o){return r(o+32)})+" "},decompressFromUTF16:function(r){return null==r?"":""==r?null:i._decompress(r.length,16384,function(o){return r.charCodeAt(o)-32})},compressToUint8Array:function(r){for(var o=i.compress(r),n=new Uint8Array(2*o.length),e=0,t=o.length;e<t;e++){var s=o.charCodeAt(e);n[2*e]=s>>>8,n[2*e+1]=s%256}return n},decompressFromUint8Array:function(o){if(null==o)return i.decompress(o);for(var n=new Array(o.length/2),e=0,t=n.length;e<t;e++)n[e]=256*o[2*e]+o[2*e+1];var s=[];return n.forEach(function(o){s.push(r(o))}),i.decompress(s.join(""))},compressToEncodedURIComponent:function(r){return null==r?"":i._compress(r,6,function(r){return n.charAt(r)})},decompressFromEncodedURIComponent:function(r){return null==r?"":""==r?null:(r=r.replace(/ /g,"+"),i._decompress(r.length,32,function(o){return t(n,r.charAt(o))}))},compress:function(o){return i._compress(o,16,function(o){return r(o)})},_compress:function(r,o,n){if(null==r)return"";var e,t,i,s={},u={},a="",p="",c="",l=2,f=3,h=2,d=[],m=0,v=0;for(i=0;i<r.length;i+=1)if(a=r.charAt(i),Object.prototype.hasOwnProperty.call(s,a)||(s[a]=f++,u[a]=!0),p=c+a,Object.prototype.hasOwnProperty.call(s,p))c=p;else{if(Object.prototype.hasOwnProperty.call(u,c)){if(c.charCodeAt(0)<256){for(e=0;e<h;e++)m<<=1,v==o-1?(v=0,d.push(n(m)),m=0):v++;for(t=c.charCodeAt(0),e=0;e<8;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1}else{for(t=1,e=0;e<h;e++)m=m<<1|t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t=0;for(t=c.charCodeAt(0),e=0;e<16;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1}0==--l&&(l=Math.pow(2,h),h++),delete u[c]}else for(t=s[c],e=0;e<h;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1;0==--l&&(l=Math.pow(2,h),h++),s[p]=f++,c=String(a)}if(""!==c){if(Object.prototype.hasOwnProperty.call(u,c)){if(c.charCodeAt(0)<256){for(e=0;e<h;e++)m<<=1,v==o-1?(v=0,d.push(n(m)),m=0):v++;for(t=c.charCodeAt(0),e=0;e<8;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1}else{for(t=1,e=0;e<h;e++)m=m<<1|t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t=0;for(t=c.charCodeAt(0),e=0;e<16;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1}0==--l&&(l=Math.pow(2,h),h++),delete u[c]}else for(t=s[c],e=0;e<h;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1;0==--l&&(l=Math.pow(2,h),h++)}for(t=2,e=0;e<h;e++)m=m<<1|1&t,v==o-1?(v=0,d.push(n(m)),m=0):v++,t>>=1;for(;;){if(m<<=1,v==o-1){d.push(n(m));break}v++}return d.join("")},decompress:function(r){return null==r?"":""==r?null:i._decompress(r.length,32768,function(o){return r.charCodeAt(o)})},_decompress:function(o,n,e){var t,i,s,u,a,p,c,l=[],f=4,h=4,d=3,m="",v=[],g={val:e(0),position:n,index:1};for(t=0;t<3;t+=1)l[t]=t;for(s=0,a=Math.pow(2,2),p=1;p!=a;)u=g.val&g.position,g.position>>=1,0==g.position&&(g.position=n,g.val=e(g.index++)),s|=(u>0?1:0)*p,p<<=1;switch(s){case 0:for(s=0,a=Math.pow(2,8),p=1;p!=a;)u=g.val&g.position,g.position>>=1,0==g.position&&(g.position=n,g.val=e(g.index++)),s|=(u>0?1:0)*p,p<<=1;c=r(s);break;case 1:for(s=0,a=Math.pow(2,16),p=1;p!=a;)u=g.val&g.position,g.position>>=1,0==g.position&&(g.position=n,g.val=e(g.index++)),s|=(u>0?1:0)*p,p<<=1;c=r(s);break;case 2:return""}for(l[3]=c,i=c,v.push(c);;){if(g.index>o)return"";for(s=0,a=Math.pow(2,d),p=1;p!=a;)u=g.val&g.position,g.position>>=1,0==g.position&&(g.position=n,g.val=e(g.index++)),s|=(u>0?1:0)*p,p<<=1;switch(c=s){case 0:for(s=0,a=Math.pow(2,8),p=1;p!=a;)u=g.val&g.position,g.position>>=1,0==g.position&&(g.position=n,g.val=e(g.index++)),s|=(u>0?1:0)*p,p<<=1;l[h++]=r(s),c=h-1,f--;break;case 1:for(s=0,a=Math.pow(2,16),p=1;p!=a;)u=g.val&g.position,g.position>>=1,0==g.position&&(g.position=n,g.val=e(g.index++)),s|=(u>0?1:0)*p,p<<=1;l[h++]=r(s),c=h-1,f--;break;case 2:return v.join("")}if(0==f&&(f=Math.pow(2,d),d++),l[c])m=l[c];else{if(c!==h)return null;m=i+i.charAt(0)}v.push(m),l[h++]=i+m.charAt(0),i=m,0==--f&&(f=Math.pow(2,d),d++)}}};return i}();"function"==typeof define&&define.amd?define(function(){return LZString}):"undefined"!=typeof module&&null!=module?module.exports=LZString:"undefined"!=typeof angular&&null!=angular&&angular.module("LZString",[]).factory("LZString",function(){return LZString});` (L1)
## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`LZString`|fn||1|var LZString=function(){var r=String.fromCharCode,o="ABCD...|


---

# pages.py | Python | 85L | 2 symbols | 1 imports | 6 comments
> Path: `src/debriddo/web/pages.py`
> @file src/debriddo/web/pages.py @brief Module-level runtime logic and reusable symbols. @details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.

## Imports
```
from pathlib import Path
```

## Definitions

- var `WEB_DIR = Path(__file__).resolve().parent` (L13) — : @brief Exported constant `WEB_DIR` used by runtime workflows.
### fn `def get_index(app_name, app_version, app_environment)` (L16-85)
L17-27> Legge e restituisce il contenuto della pagina index.html con i placeholder sostituiti. Args: app_name (str): Il nome dell'applicazione. app_version (str): La versione dell'applicazione. app_environment (str): L'ambiente di esecuzione (es. development). Returns: str: Il contenuto HTML della pagina index processata.
L33> `return index`
L34-84> error = <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Error - Page Not Found</title> <style> body { font-family: Arial, sans-serif; text-align: center; background-color: #f8f9fa; color: #333; margin: 0; padding: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; } h1 { font-size: 4rem; margin: 0; } p { font-size: 1.5rem; margin: 10px 0; } a { display: inline-block; margin-top: 20px; padding: 10px 20px; font-size: 1rem; color: #fff; background-color: #007bff; text-decoration: none; border-radius: 5px; } a:hover { background-color: #0056b3; } </style> </head> <body> <h1>404</h1> <p>Oops! The page you're looking for doesn't exist.</p> <a href="/">Go Back Home</a> </body> </html>
L85> `return error`

## Comments
- L7-8: VERSION: 0.0.35 | AUTHORS: Ogekuri
- L17: Legge e restituisce il contenuto della pagina index.html con i placeholder sostituiti. Args: ...
- L34: error = <!DOCTYPE html> <html lang="en"> <head> ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`WEB_DIR`|var|pub|13||
|`get_index`|fn|pub|16-85|def get_index(app_name, app_version, app_environment)|

