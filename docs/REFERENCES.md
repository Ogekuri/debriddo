# api_tester.py | Python | 1112L | 33 symbols | 9 imports | 29 comments
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

- var `DEFAULT_CONFIG_ENV = "DEBRIDDO_CONFIG_URL"` (L29)
- var `DEFAULT_TIMEOUT = 180.0` (L30)
- var `DEBRIDDO_MODULE_PREFIX = "debriddo"` (L31)
### class `class CliError(Exception)` : Exception (L34-37)

### fn `def ensure_no_debriddo_modules_loaded() -> None` (L38-55)
L39-44> Verifica che nessun modulo del package 'debriddo' sia stato caricato. Raises: CliError: Se vengono rilevati moduli 'debriddo' caricati.
L51> `raise CliError(`

### class `class TargetUrls` `@dataclass` (L57-62)

### class `class CheckResult` `@dataclass` (L64-69)

### fn `def normalize_config_url(raw_value: str) -> TargetUrls` (L70-118)
L71-82> Analizza e normalizza l'URL di configurazione fornito. Args: raw_value (str): L'URL grezzo passato come input. Returns: TargetUrls: Oggetto contenente URL base, segmento config e URL completo. Raises: CliError: Se l'URL non è valido o manca del segmento di configurazione.
L85> `raise CliError("config URL vuota.")`
L89> `raise CliError(f"URL non valido: '{value}'.")`
L93> `raise CliError("Path URL non valido: manca il segmento C_<config>.")`
L104> `raise CliError("Impossibile trovare un segmento 'C_' nell'URL di configurazione.")`
L112> `return TargetUrls(`

### fn `def get_target_from_args(args: argparse.Namespace) -> TargetUrls` (L119-139)
L120-131> Recupera l'URL target dagli argomenti CLI o variabili d'ambiente. Args: args (argparse.Namespace): Gli argomenti parsati della CLI. Returns: TargetUrls: L'oggetto TargetUrls risolto. Raises: CliError: Se la configurazione è mancante.
L134> `raise CliError(`
L137> `return normalize_config_url(config_url)`

### fn `def request_url(` (L140-146)

### fn `def make_url(base_url: str, path: str) -> str` (L172-185)
L173-182> Costruisce un URL completo combinando base URL e path. Args: base_url (str): L'URL base. path (str): Il percorso relativo. Returns: str: L'URL completo senza doppi slash.
L183> `return f"{base_url.rstrip('/')}/{path.lstrip('/')}"`

### fn `def parse_json_body(response: requests.Response) -> Optional[Any]` (L186-201)
L187-195> Tenta di parsare il corpo della risposta come JSON. Args: response (requests.Response): La risposta HTTP. Returns: Optional[Any]: Il JSON parsato o None se il parsing fallisce.
L197> `return response.json()`
L199> `return None`

### fn `def print_response_summary(` (L202-205)

### fn `def call_simple_endpoint(` (L237-243)

### fn `def build_stream_path(` (L273-277)

### fn `def cmd_target(args: argparse.Namespace) -> int` (L297-313)
L298-306> Stampa le informazioni sul target risolto (comando 'target'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Sempre 0.
L311> `return 0`

### fn `def cmd_root(args: argparse.Namespace) -> int` (L314-335)
L315-323> Esegue il test dell'endpoint root '/' (comando 'root'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L326> `return call_simple_endpoint(`

### fn `def cmd_configure(args: argparse.Namespace) -> int` (L336-351)
L337-345> Esegue il test dell'endpoint '/configure' (comando 'configure'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L349> `return call_simple_endpoint(session, args, target, path, method="GET")`

### fn `def cmd_manifest(args: argparse.Namespace) -> int` (L352-367)
L353-361> Esegue il test dell'endpoint '/manifest.json' (comando 'manifest'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L365> `return call_simple_endpoint(session, args, target, path, method="GET")`

### fn `def cmd_site_webmanifest(args: argparse.Namespace) -> int` (L368-382)
L369-377> Esegue il test dell'endpoint '/site.webmanifest' (comando 'site-webmanifest'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L380> `return call_simple_endpoint(session, args, target, "/site.webmanifest", method="GET")`

### fn `def cmd_asset(args: argparse.Namespace) -> int` (L383-415)
L384-392> Esegue il test degli asset statici (comando 'asset'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L407> `raise CliError(f"Tipo asset non supportato: {args.asset_type}")`
L413> `return call_simple_endpoint(session, args, target, asset_path, method="GET")`

### fn `def request_stream(` (L416-422)

### fn `def cmd_stream(args: argparse.Namespace) -> int` (L455-491)
L456-464> Esegue il test dell'endpoint '/stream' (comando 'stream'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L489> `return 0 if response.ok else 1`

### fn `def cmd_search(args: argparse.Namespace) -> int` (L492-531)
L493-501> Esegue una ricerca stream stampando il payload completo (comando 'search'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L529> `return 0 if response.ok else 1`

### fn `def extract_playback_path_from_streams(streams_payload: Dict[str, Any]) -> Optional[str]` (L532-557)
L533-541> Estrae il path di playback dal payload degli stream. Args: streams_payload (Dict[str, Any]): Il payload JSON degli stream. Returns: Optional[str]: Il path di playback se trovato, altrimenti None.
L544> `return None`
L554> `return parsed.path`
L555> `return None`

### fn `def request_playback(` (L558-563)

### fn `def cmd_playback(args: argparse.Namespace) -> int` (L589-638)
L590-598> Esegue il test dell'endpoint '/playback' (comando 'playback'). Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 errore).
L608> `raise CliError("Per usare playback senza --query devi passare --stream-type e --stream-id.")`
L620> `raise CliError(`
L636> `return 0 if response.status_code < 400 else 1`

### fn `def validate_manifest_payload(payload: Dict[str, Any]) -> Tuple[bool, str]` (L639-662)
L640-648> Valida il payload del manifest JSON. Args: payload (Dict[str, Any]): Il payload JSON. Returns: Tuple[bool, str]: (Valido, Messaggio di dettaglio).
L651> `return False, "manifest senza array 'resources'"`
L659> `return True, "resource stream con movie+series trovata"`
L660> `return False, "resource stream con movie+series non trovata"`

### fn `def add_check(results: List[CheckResult], name: str, ok: bool, detail: str) -> None` (L663-675)
L664-672> Aggiunge un risultato di controllo alla lista. Args: results (List[CheckResult]): Lista dei risultati. name (str): Nome del controllo. ok (bool): Esito del controllo. detail (str): Dettaglio del controllo.

### fn `def run_smoke(args: argparse.Namespace, target: TargetUrls) -> List[CheckResult]` (L676-875)
L677-686> Esegue una serie di test smoke (controllo salute di base). Args: args (argparse.Namespace): Argomenti CLI. target (TargetUrls): URL target. Returns: List[CheckResult]: Lista dei risultati dei test.

### fn `def cmd_smoke(args: argparse.Namespace) -> int` (L904-927)
L905-913> Esegue il comando 'smoke' che lancia una suite di test. Args: args (argparse.Namespace): Argomenti CLI. Returns: int: Codice di uscita (0 successo, 1 fallimento).
L925> `return 0 if failed == 0 else 1`

### fn `def build_parser() -> argparse.ArgumentParser` (L928-1089)
L929-934> Costruisce il parser degli argomenti della riga di comando. Returns: argparse.ArgumentParser: Il parser configurato.
L1087> `return parser`

### fn `def main() -> int` (L1090-1110)
L1091-1096> Punto di ingresso principale dello script. Returns: int: Codice di uscita da passare a sys.exit().
L1102> `return int(args.func(args))`
L1105> `return 2`
L1108> `return 2`

## Comments
- L2: CLI autonoma per testare le API HTTP esposte da Debriddo. La configurazione può arrivare da: ...
- L39: Verifica che nessun modulo del package 'debriddo' sia stato caricato. Raises: ...
- L71: Analizza e normalizza l'URL di configurazione fornito. Args: ...
- L120: Recupera l'URL target dagli argomenti CLI o variabili d'ambiente. Args: ...
- L148: Esegue una richiesta HTTP utilizzando la sessione fornita. Args: ...
- L173: Costruisce un URL completo combinando base URL e path. Args: ...
- L187: Tenta di parsare il corpo della risposta come JSON. Args: ...
- L207: Stampa un riepilogo della risposta HTTP su stdout. Args: ...
- L245: Esegue una chiamata a un endpoint semplice e stampa il risultato. Args: ...
- L279: Costruisce il percorso per l'endpoint di stream. Args: ...
- L298: Stampa le informazioni sul target risolto (comando 'target'). Args: ...
- L315: Esegue il test dell'endpoint root '/' (comando 'root'). Args: ...
- L337: Esegue il test dell'endpoint '/configure' (comando 'configure'). Args: ...
- L353: Esegue il test dell'endpoint '/manifest.json' (comando 'manifest'). Args: ...
- L369: Esegue il test dell'endpoint '/site.webmanifest' (comando 'site-webmanifest'). Args: ...
- L384: Esegue il test degli asset statici (comando 'asset'). Args: ...
- L424: Esegue la richiesta HTTP per ottenere lo stream. Args: ...
- L456: Esegue il test dell'endpoint '/stream' (comando 'stream'). Args: ...
- L493: Esegue una ricerca stream stampando il payload completo (comando 'search'). Args: ...
- L533: Estrae il path di playback dal payload degli stream. Args: ...
- L565: Esegue la richiesta HTTP per il playback. Args: ...
- L590: Esegue il test dell'endpoint '/playback' (comando 'playback'). Args: ...
- L640: Valida il payload del manifest JSON. Args: ...
- L664: Aggiunge un risultato di controllo alla lista. Args: ...
- L677: Esegue una serie di test smoke (controllo salute di base). Args: ...
- L905: Esegue il comando 'smoke' che lancia una suite di test. Args: ...
- L929: Costruisce il parser degli argomenti della riga di comando. Returns: ...
- L1091: Punto di ingresso principale dello script. Returns: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`DEFAULT_CONFIG_ENV`|var|pub|29||
|`DEFAULT_TIMEOUT`|var|pub|30||
|`DEBRIDDO_MODULE_PREFIX`|var|pub|31||
|`CliError`|class|pub|34-37|class CliError(Exception)|
|`ensure_no_debriddo_modules_loaded`|fn|pub|38-55|def ensure_no_debriddo_modules_loaded() -> None|
|`TargetUrls`|class|pub|57-62|class TargetUrls|
|`CheckResult`|class|pub|64-69|class CheckResult|
|`normalize_config_url`|fn|pub|70-118|def normalize_config_url(raw_value: str) -> TargetUrls|
|`get_target_from_args`|fn|pub|119-139|def get_target_from_args(args: argparse.Namespace) -> Tar...|
|`request_url`|fn|pub|140-146|def request_url(|
|`make_url`|fn|pub|172-185|def make_url(base_url: str, path: str) -> str|
|`parse_json_body`|fn|pub|186-201|def parse_json_body(response: requests.Response) -> Optio...|
|`print_response_summary`|fn|pub|202-205|def print_response_summary(|
|`call_simple_endpoint`|fn|pub|237-243|def call_simple_endpoint(|
|`build_stream_path`|fn|pub|273-277|def build_stream_path(|
|`cmd_target`|fn|pub|297-313|def cmd_target(args: argparse.Namespace) -> int|
|`cmd_root`|fn|pub|314-335|def cmd_root(args: argparse.Namespace) -> int|
|`cmd_configure`|fn|pub|336-351|def cmd_configure(args: argparse.Namespace) -> int|
|`cmd_manifest`|fn|pub|352-367|def cmd_manifest(args: argparse.Namespace) -> int|
|`cmd_site_webmanifest`|fn|pub|368-382|def cmd_site_webmanifest(args: argparse.Namespace) -> int|
|`cmd_asset`|fn|pub|383-415|def cmd_asset(args: argparse.Namespace) -> int|
|`request_stream`|fn|pub|416-422|def request_stream(|
|`cmd_stream`|fn|pub|455-491|def cmd_stream(args: argparse.Namespace) -> int|
|`cmd_search`|fn|pub|492-531|def cmd_search(args: argparse.Namespace) -> int|
|`extract_playback_path_from_streams`|fn|pub|532-557|def extract_playback_path_from_streams(streams_payload: D...|
|`request_playback`|fn|pub|558-563|def request_playback(|
|`cmd_playback`|fn|pub|589-638|def cmd_playback(args: argparse.Namespace) -> int|
|`validate_manifest_payload`|fn|pub|639-662|def validate_manifest_payload(payload: Dict[str, Any]) ->...|
|`add_check`|fn|pub|663-675|def add_check(results: List[CheckResult], name: str, ok: ...|
|`run_smoke`|fn|pub|676-875|def run_smoke(args: argparse.Namespace, target: TargetUrl...|
|`cmd_smoke`|fn|pub|904-927|def cmd_smoke(args: argparse.Namespace) -> int|
|`build_parser`|fn|pub|928-1089|def build_parser() -> argparse.ArgumentParser|
|`main`|fn|pub|1090-1110|def main() -> int|


---

# check_unused_requirements.py | Python | 124L | 3 symbols | 3 imports | 14 comments
> Path: `src/debriddo/check_unused_requirements.py`
> VERSION: 0.0.35

## Imports
```
import os
import ast
import importlib.metadata
```

## Definitions

### fn `def get_imported_modules_from_file(filepath)` (L8-35)
L9-17> Estrae i moduli importati da un file Python analizzandone l'AST. Args: filepath (str): Il percorso del file da analizzare. Returns: set: Un set di stringhe contenente i nomi dei moduli top-level importati.
L23> `return imported_modules`
L28> forziamo minuscolo
L32> forziamo minuscolo
L34> `return imported_modules`

### fn `def get_all_imported_modules(root_dir)` (L36-57)
L37-45> Scansiona ricorsivamente una directory per trovare tutti i moduli importati nei file .py. Args: root_dir (str): La directory radice da cui iniziare la scansione. Returns: set: Un set di tutti i moduli importati trovati.
L48> Ignora virtual env
L56> `return all_imports`

### fn `def get_requirements(requirements_file)` (L58-79)
L59-67> Legge un file requirements.txt e restituisce un set di pacchetti richiesti. Args: requirements_file (str): Il percorso del file requirements.txt. Returns: set: Un set di nomi di pacchetti (senza versioni).
L74> estrai il nome del pacchetto senza versione
L75> minuscolo
L78> `return packages`

## Comments
- L2: AUTHORS: Ogekuri
- L9: Estrae i moduli importati da un file Python analizzandone l'AST. Args: ...
- L37: Scansiona ricorsivamente una directory per trovare tutti i moduli importati nei file .py. Args: ...
- L48: Ignora virtual env
- L59: Legge un file requirements.txt e restituisce un set di pacchetti richiesti. Args: ...
- L74: estrai il nome del pacchetto senza versione
- L89: imported_modules ora contiene solo minuscole
- L92: required_packages ora contiene i nomi dei pacchetti in minuscolo
- L95-98: pkg_to_distributions ha una struttura: | { "bs4": ["beautifulsoup4"], "apscheduler": ["APScheduler"], ... } | Invertiamo il mapping in modo da ottenere distribution -> {top_modules}
- L111: Se non troviamo moduli top-level per questo pacchetto, supponiamo che il modulo top-level coincida con il nome del pacchetto
- L115: Controlliamo se almeno uno dei top_modules è stato importato

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_imported_modules_from_file`|fn|pub|8-35|def get_imported_modules_from_file(filepath)|
|`get_all_imported_modules`|fn|pub|36-57|def get_all_imported_modules(root_dir)|
|`get_requirements`|fn|pub|58-79|def get_requirements(requirements_file)|


---

# constants.py | Python | 15L | 6 symbols | 0 imports | 5 comments
> Path: `src/debriddo/constants.py`
> AUTHORS: Ogekuri

## Definitions

- var `APPLICATION_NAME = "Debriddo"` (L4) — AUTHORS: Ogekuri
- var `APPLICATION_VERSION = "0.0.35"` (L5)
- var `APPLICATION_DESCRIPTION = "Ricerca online i Film e le tue Serie Tv preferite."` (L6)
- var `CACHE_DATABASE_FILE = "caches_items.db"` (L9) — SQL3llite database
- var `NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/refs/heads/master/videos/nocache.mp4"` (L12) — Link per AllDebrid/Real-Debird/Premiumize che è ritornato in caso di errore
- var `RUN_IN_MULTI_THREAD = True` (L15) — Run in multi-thread
## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`APPLICATION_NAME`|var|pub|4||
|`APPLICATION_VERSION`|var|pub|5||
|`APPLICATION_DESCRIPTION`|var|pub|6||
|`CACHE_DATABASE_FILE`|var|pub|9||
|`NO_CACHE_VIDEO_URL`|var|pub|12||
|`RUN_IN_MULTI_THREAD`|var|pub|15||


---

# alldebrid.py | Python | 159L | 10 symbols | 7 imports | 10 comments
> Path: `src/debriddo/debrid/alldebrid.py`
> VERSION: 0.0.35

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

### class `class AllDebrid(BaseDebrid)` : BaseDebrid (L17-159)
- fn `def __init__(self, config)` `priv` (L18-21)
- fn `async def add_magnet(self, magnet, ip=None)` (L22-25)
  L24> `return await self.get_json_response(url)`
- fn `async def add_torrent(self, torrent_file, ip)` (L26-30)
  L29> `return await self.get_json_response(url, method='post', files=files)`
- fn `async def check_magnet_status(self, id, ip)` (L31-34)
  L33> `return await self.get_json_response(url)`
- fn `async def unrestrict_link(self, link, ip)` (L35-38)
  L37> `return await self.get_json_response(url)`
- fn `async def get_stream_link(self, query, ip=None)` (L39-111)
  L50> `return False`
  L51> `return status_response.get("data", {}).get("magnets", {}).get("status") == "Ready"`
  L55> `return NO_CACHE_VIDEO_URL`
  L61> `return NO_CACHE_VIDEO_URL`
  L64> `return NO_CACHE_VIDEO_URL`
  L90> `raise ValueError(f"Error: No matching files for {season} {episode} in torrent.")`
  L95> `raise ValueError("Error: Unsupported stream type.")`
  L98> `return link`
  L106> `raise ValueError("Error: Failed to unlock link.")`
  L110> `return unlocked_link_data["data"]["link"]`
- fn `async def is_ready()` (L47-52)
  L50> `return False`
  L51> `return status_response.get("data", {}).get("magnets", {}).get("status") == "Ready"`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L112-132)
  L117> `return ids`
  L122> `return ids`
  L124> if len(hashes_or_magnets) == 0:
  L125> logger.debug("No hashes to be sent to All-Debrid.")
  L126> return dict()
  L128> url = f"{self.base_url}magnet/instant?agent=debriddo&apikey={self.config['debridKey']}&magnets[]={'&magnets[]='.join(hashes_or_magnets)}&ip={ip}
  L129> logger.debug(url)
  L130> return await self.get_json_response(url)
- fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None, ip=None)` `priv` (L133-159) L130> return await self.get_json_response(url)
  L141> `raise ValueError("Error: Failed to add magnet.")`
  L154> `raise ValueError("Error: Failed to add torrent file.")`
  L159> `return torrent_id`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L124-129: if len(hashes_or_magnets) == 0: | logger.debug("No hashes to be sent to All-Debrid.") | return dict() | url = f"{self.base_url}magnet/instant?agent=debriddo&apikey={self.config['debridKey']}&magnets[]=... | logger.debug(url)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`AllDebrid`|class|pub|17-159|class AllDebrid(BaseDebrid)|
|`AllDebrid.__init__`|fn|priv|18-21|def __init__(self, config)|
|`AllDebrid.add_magnet`|fn|pub|22-25|async def add_magnet(self, magnet, ip=None)|
|`AllDebrid.add_torrent`|fn|pub|26-30|async def add_torrent(self, torrent_file, ip)|
|`AllDebrid.check_magnet_status`|fn|pub|31-34|async def check_magnet_status(self, id, ip)|
|`AllDebrid.unrestrict_link`|fn|pub|35-38|async def unrestrict_link(self, link, ip)|
|`AllDebrid.get_stream_link`|fn|pub|39-111|async def get_stream_link(self, query, ip=None)|
|`AllDebrid.is_ready`|fn|pub|47-52|async def is_ready()|
|`AllDebrid.get_availability_bulk`|fn|pub|112-132|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`AllDebrid.__add_magnet_or_torrent`|fn|priv|133-159|async def __add_magnet_or_torrent(self, magnet, torrent_d...|


---

# base_debrid.py | Python | 66L | 9 symbols | 5 imports | 5 comments
> Path: `src/debriddo/debrid/base_debrid.py`
> VERSION: 0.0.35

## Imports
```
import json
import asyncio
import httpx
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class BaseDebrid` (L12-66)
- fn `def __init__(self, config)` `priv` (L13-16)
- fn `async def wait_for_ready_status_async_func(self, check_status_func, timeout=30, interval=5)` (L17-28)
  L21> Se check_status_func è asincrona, uso `await check_status_func()`.
  L24> `return True`
  L27> `return False`
- fn `async def wait_for_ready_status_sync_func(self, check_status_func, timeout=30, interval=5)` (L29-41)
  L33> Se check_status_func è sincrona, la chiamiamo direttamente.
  L36> `return True`
  L39> `return False`
- fn `async def get_json_response(self, url, **kwargs)` (L42-47)
  L43> Usa il client asincrono
  L46> `return ret`
- fn `async def download_torrent_file(self, download_url)` (L48-54)
  L49> Usa il client asincrono
  L52> `return ret`
- fn `async def get_stream_link(self, query, ip=None)` (L55-58)
  L56> `raise NotImplementedError`
- fn `async def add_magnet(self, magnet, ip=None)` (L59-62)
  L60> `raise NotImplementedError`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L63-66)
  L64> `raise NotImplementedError`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L21: Se check_status_func è asincrona, uso `await check_status_func()`.
- L33: Se check_status_func è sincrona, la chiamiamo direttamente.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BaseDebrid`|class|pub|12-66|class BaseDebrid|
|`BaseDebrid.__init__`|fn|priv|13-16|def __init__(self, config)|
|`BaseDebrid.wait_for_ready_status_async_func`|fn|pub|17-28|async def wait_for_ready_status_async_func(self, check_st...|
|`BaseDebrid.wait_for_ready_status_sync_func`|fn|pub|29-41|async def wait_for_ready_status_sync_func(self, check_sta...|
|`BaseDebrid.get_json_response`|fn|pub|42-47|async def get_json_response(self, url, **kwargs)|
|`BaseDebrid.download_torrent_file`|fn|pub|48-54|async def download_torrent_file(self, download_url)|
|`BaseDebrid.get_stream_link`|fn|pub|55-58|async def get_stream_link(self, query, ip=None)|
|`BaseDebrid.add_magnet`|fn|pub|59-62|async def add_magnet(self, magnet, ip=None)|
|`BaseDebrid.get_availability_bulk`|fn|pub|63-66|async def get_availability_bulk(self, hashes_or_magnets, ...|


---

# get_debrid_service.py | Python | 26L | 1 symbols | 5 imports | 3 comments
> Path: `src/debriddo/debrid/get_debrid_service.py`
> VERSION: 0.0.35

## Imports
```
from fastapi.exceptions import HTTPException
from debriddo.debrid.alldebrid import AllDebrid
from debriddo.debrid.premiumize import Premiumize
from debriddo.debrid.realdebrid import RealDebrid
from debriddo.debrid.torbox import TorBox
```

## Definitions

### fn `def get_debrid_service(config)` (L13-26)
L24> `raise HTTPException(status_code=500, detail="Invalid service configuration.")`
L26> `return debrid_service`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_debrid_service`|fn|pub|13-26|def get_debrid_service(config)|


---

# premiumize.py | Python | 138L | 10 symbols | 5 imports | 7 comments
> Path: `src/debriddo/debrid/premiumize.py`
> VERSION: 0.0.35

## Imports
```
import json
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import get_info_hash_from_magnet, season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class Premiumize(BaseDebrid)` : BaseDebrid (L16-138)
- fn `def __init__(self, config)` `priv` (L17-20)
- fn `async def add_magnet(self, magnet, ip=None)` (L21-25)
  L24> `return await self.get_json_response(url, method='post', data=form)`
- fn `async def add_torrent(self, torrent_file)` (L27-31) L26> Doesn't work for the time being. Premiumize does not support torrent file torrents
  L30> `return await self.get_json_response(url, method='post', data=form)`
- fn `async def list_transfers(self)` (L32-35)
  L34> `return await self.get_json_response(url)`
- fn `async def get_folder_or_file_details(self, item_id, is_folder=True)` (L36-44)
  L43> `return await self.get_json_response(url)`
- fn `async def get_availability(self, hash)` (L45-48)
  L47> `return await self.get_json_response(url)`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L49-53)
  L52> `return await self.get_json_response(url)`
- fn `async def get_stream_link(self, query, ip=None)` (L54-138)
  L65> `raise ValueError("Error: Failed to create transfer.")`
  L72> `return False`
  L74> `return isinstance(transcoded, list) and len(transcoded) > 0 and bool(transcoded[0])`
  L78> `return NO_CACHE_VIDEO_URL`
  L82> Assuming the transfer is complete, we need to find whether it's a file or a folder
  L96> `raise ValueError("Error: Transfer completed but no item ID found.")`
  L103> For movies, we pick the largest file in the folder or the file itself
  L107> `raise ValueError("Error: Empty Premiumize folder content.")`
  L125> `raise ValueError(f"Error: No matching files for {season} {episode} in torrent.")`
  L132> `raise ValueError("Error: Unsupported stream type.")`
  L135> `raise ValueError("Error: No Premiumize link found.")`
  L138> `return link`
- fn `async def is_ready()` (L69-75)
  L72> `return False`
  L74> `return isinstance(transcoded, list) and len(transcoded) > 0 and bool(transcoded[0])`

## Comments
- L2-5: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri | Assuming the BaseDebrid class and necessary imports are already defined as shown previously
- L82: Assuming the transfer is complete, we need to find whether it's a file or a folder
- L103: For movies, we pick the largest file in the folder or the file itself

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Premiumize`|class|pub|16-138|class Premiumize(BaseDebrid)|
|`Premiumize.__init__`|fn|priv|17-20|def __init__(self, config)|
|`Premiumize.add_magnet`|fn|pub|21-25|async def add_magnet(self, magnet, ip=None)|
|`Premiumize.add_torrent`|fn|pub|27-31|async def add_torrent(self, torrent_file)|
|`Premiumize.list_transfers`|fn|pub|32-35|async def list_transfers(self)|
|`Premiumize.get_folder_or_file_details`|fn|pub|36-44|async def get_folder_or_file_details(self, item_id, is_fo...|
|`Premiumize.get_availability`|fn|pub|45-48|async def get_availability(self, hash)|
|`Premiumize.get_availability_bulk`|fn|pub|49-53|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`Premiumize.get_stream_link`|fn|pub|54-138|async def get_stream_link(self, query, ip=None)|
|`Premiumize.is_ready`|fn|pub|69-75|async def is_ready()|


---

# realdebrid.py | Python | 318L | 19 symbols | 10 imports | 20 comments
> Path: `src/debriddo/debrid/realdebrid.py`
> VERSION: 0.0.35

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

### class `class RealDebrid(BaseDebrid)` : BaseDebrid (L20-219)
L215> `raise ValueError("Error: Failed to add magnet.")`
- fn `def __init__(self, config)` `priv` (L21-25)
- fn `async def add_magnet(self, magnet, ip=None)` (L26-30)
  L29> `return await self.get_json_response(url, method='post', headers=self.headers, data=data)`
- fn `async def add_torrent(self, torrent_file)` (L31-34)
  L33> `return await self.get_json_response(url, method='put', headers=self.headers, data=torrent_file)`
- fn `async def delete_torrent(self, id)` (L35-38)
  L37> `return await self.get_json_response(url, method='delete', headers=self.headers)`
- fn `async def get_torrent_info(self, torrent_id)` (L39-49)
  L45> `return None`
  L47> `return torrent_info`
  L48> `return None`
- fn `async def select_files(self, torrent_id, file_id)` (L50-57)
  L54> TODO verificare perché è stato sostituito dalla get_json_response che tanto non ritorna nulla!
  L55> self.request_post(url, headers=self.headers, data=data)
- fn `async def unrestrict_link(self, link)` (L58-62) L55> self.request_post(url, headers=self.headers, data=data)
  L61> `return await self.get_json_response(url, method='post', headers=self.headers, data=data)`
- fn `async def is_already_added(self, magnet)` (L63-72)
  L70> `return torrent['id']`
  L71> `return False`
- fn `async def wait_for_link(self, torrent_id, timeout=30, interval=2)` (L73-82)
  L78> `return torrent_info['links']`
  L81> `return None`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L83-99)
  L86> `return dict()`
  L88> TODO: verificare che cazzo fa sta cosa
  L93> `return dict()`
  L98> `return await self.get_json_response(url, headers=self.headers)`
- fn `async def get_stream_link(self, query, ip=None)` (L100-160)
  L120> `raise ValueError("Error: Unsupported stream type.")`
  L122> The torrent is not yet added
  L126> `raise ValueError("Error: Failed to get torrent info.")`
  L131> == operator, to avoid adding the season pack twice and setting 5 as season pack treshold
  L141> Waiting for the link(s) to be ready
  L144> `return NO_CACHE_VIDEO_URL`
  L153> Unrestricting the download link
  L156> `raise ValueError("Error: Failed to unrestrict link.")`
  L159> `return unrestrict_response['download']`
- fn `async def __get_cached_torrent_ids(self, info_hash)` `priv` (L161-173)
  L171> `return torrent_ids`
  L172> `return []`
- fn `async def __get_cached_torrent_info(self, cached_ids, file_index, season, episode)` `priv` (L174-190)
  L181> If the links are ready
  L182> `return cached_torrent_info`
  L187> `return None`
  L189> `return max(cached_torrents, key=lambda x: x['progress'])`
- fn `def __torrent_contains_file(self, torrent_info, file_index, season, episode)` `priv` (L191-205)
  L193> `return False`
  L198> `return True`
  L202> `return file["selected"] == 1`
  L204> `return False`

### fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None)` `priv` (L206-235)
L215> `raise ValueError("Error: Failed to add magnet.")`
L229> `raise ValueError("Error: Failed to add torrent file.")`
L234> `return await self.get_torrent_info(torrent_id)`

### fn `async def __prefetch_season_pack(self, magnet, torrent_download, timeout=30, interval=2)` `priv` (L236-253)
L239> `return None`
L248> TODO: da testare bene
L249> await asyncio.sleep(10)
L252> `return await self.get_torrent_info(torrent_info["id"])`

### fn `async def __select_file(self, torrent_info, stream_type, file_index, season, episode)` `priv` (L254-285)
L259> `return`
L272> if season_episode_in_filename(file["path"], season, episode, strict=True):
L273> strict_matching_files.append(file)
L274> elif season_episode_in_filename(file["path"], season, episode, strict=False):
L275> matching_files.append(file)
L281> `raise ValueError("Error: No matching file found in torrent.")`

### fn `def __find_appropiate_link(self, torrent_info, links, file_index, season, episode)` `priv` (L286-318)
L301> if season_episode_in_filename(file["path"], season, episode, strict=True):
L302> strict_matching_indexes.append({"index": index, "file": file})
L303> elif season_episode_in_filename(file["path"], season, episode, strict=False):
L304> matching_indexes.append({"index": index, "file": file})
L311> `return NO_CACHE_VIDEO_URL`
L316> `return NO_CACHE_VIDEO_URL`
L318> `return links[index]`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L54: TODO verificare perché è stato sostituito dalla get_json_response che tanto non ritorna nulla!
- L88: TODO: verificare che cazzo fa sta cosa
- L122: The torrent is not yet added
- L131: == operator, to avoid adding the season pack twice and setting 5 as season pack treshold
- L141: Waiting for the link(s) to be ready
- L153: Unrestricting the download link
- L248-249: TODO: da testare bene | await asyncio.sleep(10)
- L272-275: if season_episode_in_filename(file["path"], season, episode, strict=True): | strict_matching_files.append(file) | elif season_episode_in_filename(file["path"], season, episode, strict=False): | matching_files.append(file)
- L301-304: if season_episode_in_filename(file["path"], season, episode, strict=True): | strict_matching_indexes.append({"index": index, "file": file}) | elif season_episode_in_filename(file["path"], season, episode, strict=False): | matching_indexes.append({"index": index, "file": file})

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`RealDebrid`|class|pub|20-219|class RealDebrid(BaseDebrid)|
|`RealDebrid.__init__`|fn|priv|21-25|def __init__(self, config)|
|`RealDebrid.add_magnet`|fn|pub|26-30|async def add_magnet(self, magnet, ip=None)|
|`RealDebrid.add_torrent`|fn|pub|31-34|async def add_torrent(self, torrent_file)|
|`RealDebrid.delete_torrent`|fn|pub|35-38|async def delete_torrent(self, id)|
|`RealDebrid.get_torrent_info`|fn|pub|39-49|async def get_torrent_info(self, torrent_id)|
|`RealDebrid.select_files`|fn|pub|50-57|async def select_files(self, torrent_id, file_id)|
|`RealDebrid.unrestrict_link`|fn|pub|58-62|async def unrestrict_link(self, link)|
|`RealDebrid.is_already_added`|fn|pub|63-72|async def is_already_added(self, magnet)|
|`RealDebrid.wait_for_link`|fn|pub|73-82|async def wait_for_link(self, torrent_id, timeout=30, int...|
|`RealDebrid.get_availability_bulk`|fn|pub|83-99|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`RealDebrid.get_stream_link`|fn|pub|100-160|async def get_stream_link(self, query, ip=None)|
|`RealDebrid.__get_cached_torrent_ids`|fn|priv|161-173|async def __get_cached_torrent_ids(self, info_hash)|
|`RealDebrid.__get_cached_torrent_info`|fn|priv|174-190|async def __get_cached_torrent_info(self, cached_ids, fil...|
|`RealDebrid.__torrent_contains_file`|fn|priv|191-205|def __torrent_contains_file(self, torrent_info, file_inde...|
|`__add_magnet_or_torrent`|fn|priv|206-235|async def __add_magnet_or_torrent(self, magnet, torrent_d...|
|`__prefetch_season_pack`|fn|priv|236-253|async def __prefetch_season_pack(self, magnet, torrent_do...|
|`__select_file`|fn|priv|254-285|async def __select_file(self, torrent_info, stream_type, ...|
|`__find_appropiate_link`|fn|priv|286-318|def __find_appropiate_link(self, torrent_info, links, fil...|


---

# torbox.py | Python | 196L | 9 symbols | 8 imports | 16 comments
> Path: `src/debriddo/debrid/torbox.py`
> VERSION: 0.0.35

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

### class `class TorBox(BaseDebrid)` : BaseDebrid (L18-196)
L158> def get_json_response(self, url, method='get', **kwargs):
L159> try:
L160> if method == 'get':
L161> response = requests.request_get(url, headers=self.headers, **kwargs)
L162> elif method == 'post':
L163> response = requests.request_post(url, headers=self.headers, **kwargs)
L164> else:
L165> raise ValueError(f"Unsupported HTTP method: {method}")
L167> response.raise_for_status()
L168> return response.json()
L169> except requests.exceptions.RequestException as e:
- fn `def __init__(self, config)` `priv` (L19-25)
- fn `async def wait_for_files(self, torrent_hash, timeout=30, interval=5)` (L26-41)
  L36> `return files`
  L40> `return None`
- fn `async def add_magnet(self, magnet, ip=None)` (L42-69)
  L58> `return None`
  L60> `return {`
  L68> `return None`
- fn `async def check_magnet_status(self, torrent_hash)` (L70-80)
  L76> `return response["data"] if response["data"] else []`
  L79> `return None`
- fn `async def get_file_download_link(self, torrent_id, file_name)` (L81-90)
  L86> `return response["data"]`
  L89> `return None`
- fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None)` `priv` (L91-100)
  L99> `return torrent_id`
- fn `async def get_stream_link(self, query, ip=None)` (L101-157)
  L110> `return NO_CACHE_VIDEO_URL`
  L115> `return NO_CACHE_VIDEO_URL`
  L124> `return NO_CACHE_VIDEO_URL`
  L128> `return NO_CACHE_VIDEO_URL`
  L133> `return NO_CACHE_VIDEO_URL`
  L139> `return await self.get_file_download_link(torrent_id, largest_file_index)`
  L150> `return await self.get_file_download_link(torrent_id, selected_index)`
  L153> `return NO_CACHE_VIDEO_URL`
  L156> `raise ValueError("Error: Unsupported stream type.")`
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L173-196) L170> logger.error(f"HTTP request failed: {e}")
  L196> `return available_torrents`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L158-169: def get_json_response(self, url, method='get', **kwargs): | try: | if method == 'get': | response = requests.request_get(url, headers=self.headers, **kwargs) | elif method == 'post': | response = requests.request_post(url, headers=self.headers, **kwargs) | else: | raise ValueError(f"Unsupported HTTP method: {method}") | response.raise_for_status() | return response.json() | except requests.exceptions.RequestException as e:

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorBox`|class|pub|18-196|class TorBox(BaseDebrid)|
|`TorBox.__init__`|fn|priv|19-25|def __init__(self, config)|
|`TorBox.wait_for_files`|fn|pub|26-41|async def wait_for_files(self, torrent_hash, timeout=30, ...|
|`TorBox.add_magnet`|fn|pub|42-69|async def add_magnet(self, magnet, ip=None)|
|`TorBox.check_magnet_status`|fn|pub|70-80|async def check_magnet_status(self, torrent_hash)|
|`TorBox.get_file_download_link`|fn|pub|81-90|async def get_file_download_link(self, torrent_id, file_n...|
|`TorBox.__add_magnet_or_torrent`|fn|priv|91-100|async def __add_magnet_or_torrent(self, magnet, torrent_d...|
|`TorBox.get_stream_link`|fn|pub|101-157|async def get_stream_link(self, query, ip=None)|
|`TorBox.get_availability_bulk`|fn|pub|173-196|async def get_availability_bulk(self, hashes_or_magnets, ...|


---

# main.py | Python | 761L | 23 symbols | 36 imports | 93 comments
> Path: `src/debriddo/main.py`
> VERSION: 0.0.35

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

- var `APP_DIR = Path(__file__).resolve().parent` (L53)
- var `WEB_DIR = APP_DIR / "web"` (L54)
### fn `def calculate_optimal_thread_count()` (L101-118)
L100> calcola il numero ottimale di thread
L102-108> Calcola il numero ottimale di thread basato sui core della CPU. Formula: (N CPU Cores * 2) + 1. Returns: int: Il numero ottimale di thread.
L109> Ottieni il numero di core della CPU
L112> `raise RuntimeError("os.cpu_count() non ha restituito un valore valido")`
L114> Calcola il numero ottimale di threads
L116> `return optimal_num_threads`

### fn `def resolve_thread_count()` (L119-146)
L120-125> Risolve il numero di thread da utilizzare basandosi sulle variabili d'ambiente. Returns: int: Il numero di thread risolto.
L128> `return resolve_auto_thread_count()`
L132> `return resolve_auto_thread_count()`
L138> `return 1`
L142> `return 1`
L144> `return n_threads`

### fn `def resolve_auto_thread_count()` (L147-160)
L148-153> Risolve automaticamente il numero di thread calcolandolo. Returns: int: Il numero di thread calcolato o 1 in caso di errore.
L155> `return calculate_optimal_thread_count()`
L158> `return 1`

### fn `def get_or_create_event_loop()` (L161-175)
L162-167> Ottiene il loop di eventi corrente o ne crea uno nuovo se non esiste. Returns: asyncio.AbstractEventLoop: Il loop di eventi.
L169> `return asyncio.get_event_loop()`
L173> `return loop`

### fn `async def lifespan(app: FastAPI)` `@asynccontextmanager` (L178-206)
L176> Lifespan: gestisce startup e shutdown
L179-187> Gestisce il ciclo di vita dell'applicazione (avvio e arresto). Args: app (FastAPI): L'istanza dell'applicazione FastAPI. Yields: None: Controllo restituito all'applicazione.
L189> Il check dell'update ogni 60 secondi
L193> Verifica se il server Uvicorn è configurato con reload
L200> `yield` — Qui puoi mettere codice che deve girare durante la vita dell'app
L202> terminazione

### class `class LogFilterMiddleware` (L218-275)
L217> Aggiunge il loggin del middleware fastapi
- fn `def __init__(self, app)` `priv` (L222-230) L219> Middleware per il filtraggio e il logging delle richieste.
  L223-228> Inizializza il middleware. Args: app (ASGIApp): L'applicazione ASGI successiva.
- fn `async def __call__(self, scope, receive, send)` `priv` (L231-275) L223> Inizializza il middleware. Args: ...
  L232-242> Gestisce la richiesta in ingresso. Args: scope (dict): Lo scope della connessione. receive (callable): Funzione per ricevere messaggi. send (callable): Funzione per inviare messaggi. Returns: None: Il risultato dell'invocazione dell'app successiva.
  L243> Gestisci solo richieste HTTP,
  L244> la classe Request di Starlette è progettata solo per gestire richieste HTTP,
  L245> quindi non può essere utilizzata con eventi "lifespan" (es. avvio e arresto).
  L247> `return await self.app(scope, receive, send)`
  L250> Log informazioni sulla richiesta
  L255> GET - /C_<CONFIG>/config
  L258> GET - /playback/C_<CONFIG>/Q_<QUERY>
  L263> Log body della richiesta (se presente)
  L267> Chiamata all'applicazione
  L272> `raise HTTPException(status_code=500, detail="An error occurred while processing the request.")`
  L274> `return response`

### fn `async def root()` `@app.get("/")` (L299-307)
L297> root:
L300-305> Gestisce la root path reindirizzando alla pagina di configurazione. Returns: RedirectResponse: Redirect alla configurazione.
L306> `return RedirectResponse(url="/configure")`

### fn `async def get_favicon()` `@app.get("/favicon.ico")` (L310-319)
L308> favicon.ico
L311-316> Restituisce l'icona favicon. Returns: FileResponse: Il file favicon.ico.
L318> `return response`

### fn `async def get_config_js()` `@app.get("/{config}/config.js")` (L323-332)
L320> config.js
L324-329> Restituisce il file javascript di configurazione. Returns: FileResponse: Il file config.js.
L331> `return response`

### fn `async def get_lz_string_js()` `@app.get("/{config}/lz-string.min.js")` (L336-345)
L333> lz-string.min.js
L337-342> Restituisce la libreria lz-string minimizzata. Returns: FileResponse: Il file lz-string.min.js.
L344> `return response`

### fn `async def get_styles_css()` `@app.get("/{config}/styles.css")` (L349-358)
L346> styles.css
L350-355> Restituisce il foglio di stile CSS. Returns: FileResponse: Il file styles.css.
L357> `return response`

### fn `async def configure()` `@app.get("/{config}/configure", response_class=HTMLResponse)` (L363-371)
L360> ?/configure
L364-369> Restituisce la pagina HTML di configurazione. Returns: HTMLResponse: La pagina HTML generata.
L370> `return get_index(app_name, app_version, app_environment)`

### fn `async def function(file_path: str)` `@app.get("/{config}/images/{file_path:path}")` (L375-387)
L372> imges/?
L376-384> Serve le immagini statiche dalla directory images. Args: file_path (str): Il percorso relativo del file immagine. Returns: FileResponse: Il file immagine richiesto.
L386> `return response`

### fn `async def get_webmanifest()` `@app.get("/site.webmanifest", response_class=HTMLResponse)` (L390-426)
L388> site.webmanifest
L391-396> Genera e restituisce il web manifest per l'applicazione. Returns: JSONResponse: Il contenuto del manifest in formato JSON.
L422> `return JSONResponse(`
L424> Specifica il Content-Type corretto

### fn `async def get_manifest()` `@app.get("/{params}/manifest.json")` (L431-512)
L428> ?/manifest.json
L432-437> Restituisce il manifest di Stremio. Returns: JSONResponse: Il manifest in formato JSON.
L459> TODO: da implementare (volendo)
L460> fornisce come catalogo la lista dei file su Real-Debird
L461> catalogs": [
L462> {
L463> id": app_name_lc + "-realdebrid",
L464> name": "RealDebrid",
L465> type": "other",
L466> extra": [
L467> {
L468> name": "skip
L469> }
L470> ]
L471> }
L472> ],
L508> `return JSONResponse(`
L510> Specifica il Content-Type corretto

### fn `async def get_results(config_url: str, stream_type: str, stream_id: str, request: Request)` `@app.get("/{config_url}/stream/{stream_type}/{stream_id}")` (L515-627)
L513> ?/stream/?/?
L516-527> Gestisce la richiesta di stream per un determinato media. Args: config_url (str): La configurazione codificata. stream_type (str): Il tipo di stream (movie o series). stream_id (str): L'ID del media (es. IMDB ID). request (Request): La richiesta HTTP originale. Returns: JSONResponse: La lista degli stream disponibili.
L540> `return Response(`
L566> se la cache non ritorna abbastanza risultati
L611> TODO: Maybe add an if to only save to cache if caching is enabled?
L625> `return {"streams": stream_list}`

### fn `async def head_playback(config: str, query: str, request: Request)` `@app.head("/playback/{config_url}/{query}")` (L630-647)
L628> playback/?/?
L631-641> Gestisce la richiesta HEAD per il playback (check di validità). Args: config (str): La configurazione codificata. query (str): La query string codificata. request (Request): La richiesta HTTP originale. Returns: Response: Risposta con status code.
L643> `raise HTTPException(status_code=400, detail="Query required.")`
L644> Qui potrei limitarmi a controllare la validità di config e query
L645> e restituire comunque lo stesso set di header (es: un redirect) senza generare effettivamente la destinazione.
L646> `return Response(status_code=status.HTTP_200_OK)`

### fn `async def get_playback(config_url: str, query_string: str, request: Request)` `@app.get("/playback/{config_url}/{query_string}")` (L650-685)
L648> playback/?/?
L651-661> Gestisce il playback e restituisce il link di streaming (redirect). Args: config_url (str): La configurazione codificata. query_string (str): La query string codificata. request (Request): La richiesta HTTP originale. Returns: RedirectResponse: Redirect al link di streaming finale.
L664> `raise HTTPException(status_code=400, detail="Query required.")`
L667> decodifica la query
L670> logger.debug(f"Decoded <QUERY>: {query}")
L678> `raise HTTPException(status_code=500, detail="Unable to get stream link.")`
L679> `return RedirectResponse(url=link, status_code=status.HTTP_301_MOVED_PERMANENTLY)`
L683> `raise HTTPException(status_code=500, detail="An error occurred while processing the request.")`

### fn `async def update_app()` (L690-755)
L687> # self update ###
L691-699> Verifica e applica aggiornamenti automatici dell'applicazione. Se l'applicazione è avviata con --reload e non in modalità sviluppo, controlla GitHub Releases e aggiorna il codice. Returns: None
L701> senza --reload non gestisce l'upgrade, --reload implica --workers 1
L703> `return`
L705> in modalità sviluppo non fa l'upgrade
L707> `return`
L710> Usa il client asincrono
L715> `return`
L723> `return`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L57: load .env
- L61: get environment variables
- L78: define common string
- L88: logger
- L92: application start
- L96: verifica se è in reload
- L102-109: Calcola il numero ottimale di thread basato sui core della CPU. Formula: (N CPU Cores * 2) + 1. ... | Ottieni il numero di core della CPU
- L114: Calcola il numero ottimale di threads
- L120: Risolve il numero di thread da utilizzare basandosi sulle variabili d'ambiente. Returns: ...
- L148: Risolve automaticamente il numero di thread calcolandolo. Returns: ...
- L162: Ottiene il loop di eventi corrente o ne crea uno nuovo se non esiste. Returns: ...
- L179: Gestisce il ciclo di vita dell'applicazione (avvio e arresto). Args: ...
- L193: Verifica se il server Uvicorn è configurato con reload
- L202: terminazione
- L207: Creazione dell'app FastAPI
- L210: Imposta un maggior numero di thread, per esempio 16
- L232-245: Gestisce la richiesta in ingresso. Args: ... | Gestisci solo richieste HTTP, | la classe Request di Starlette è progettata solo per gestire richieste HTTP, | quindi non può essere utilizzata con eventi "lifespan" (es. avvio e arresto).
- L250: Log informazioni sulla richiesta
- L255: GET - /C_<CONFIG>/config
- L258: GET - /playback/C_<CONFIG>/Q_<QUERY>
- L263: Log body della richiesta (se presente)
- L267: Chiamata all'applicazione
- L280: Abilita CORSMiddleware per le chiamate OPTIONS e il redirect
- L292-294: ############## | # Fast API ### | ##############
- L300: Gestisce la root path reindirizzando alla pagina di configurazione. Returns: ...
- L311: Restituisce l'icona favicon. Returns: ...
- L324: Restituisce il file javascript di configurazione. Returns: ...
- L337: Restituisce la libreria lz-string minimizzata. Returns: ...
- L350: Restituisce il foglio di stile CSS. Returns: ...
- L359: configure
- L364: Restituisce la pagina HTML di configurazione. Returns: ...
- L376: Serve le immagini statiche dalla directory images. Args: ...
- L391: Genera e restituisce il web manifest per l'applicazione. Returns: ...
- L427: manifest.json
- L432: Restituisce il manifest di Stremio. Returns: ...
- L459-472: TODO: da implementare (volendo) | fornisce come catalogo la lista dei file su Real-Debird | catalogs": [ | { | id": app_name_lc + "-realdebrid", | name": "RealDebrid", | type": "other", | extra": [ | { | name": "skip | } | ] | } | ],
- L516: Gestisce la richiesta di stream per un determinato media. Args: ...
- L566: se la cache non ritorna abbastanza risultati
- L611: TODO: Maybe add an if to only save to cache if caching is enabled?
- L631: Gestisce la richiesta HEAD per il playback (check di validità). Args: ...
- L644-645: Qui potrei limitarmi a controllare la validità di config e query | e restituire comunque lo stesso set di header (es: un redirect) senza generare effettivamente la ...
- L651: Gestisce il playback e restituisce il link di streaming (redirect). Args: ...
- L667: decodifica la query
- L670: logger.debug(f"Decoded <QUERY>: {query}")
- L686: #################
- L691-701: Verifica e applica aggiornamenti automatici dell'applicazione. Se l'applicazione è avviata con --... | senza --reload non gestisce l'upgrade, --reload implica --workers 1
- L705: in modalità sviluppo non fa l'upgrade
- L756-758: ########## | # MAIN ### | ##########

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`APP_DIR`|var|pub|53||
|`WEB_DIR`|var|pub|54||
|`calculate_optimal_thread_count`|fn|pub|101-118|def calculate_optimal_thread_count()|
|`resolve_thread_count`|fn|pub|119-146|def resolve_thread_count()|
|`resolve_auto_thread_count`|fn|pub|147-160|def resolve_auto_thread_count()|
|`get_or_create_event_loop`|fn|pub|161-175|def get_or_create_event_loop()|
|`lifespan`|fn|pub|178-206|async def lifespan(app: FastAPI)|
|`LogFilterMiddleware`|class|pub|218-275|class LogFilterMiddleware|
|`LogFilterMiddleware.__init__`|fn|priv|222-230|def __init__(self, app)|
|`LogFilterMiddleware.__call__`|fn|priv|231-275|async def __call__(self, scope, receive, send)|
|`root`|fn|pub|299-307|async def root()|
|`get_favicon`|fn|pub|310-319|async def get_favicon()|
|`get_config_js`|fn|pub|323-332|async def get_config_js()|
|`get_lz_string_js`|fn|pub|336-345|async def get_lz_string_js()|
|`get_styles_css`|fn|pub|349-358|async def get_styles_css()|
|`configure`|fn|pub|363-371|async def configure()|
|`function`|fn|pub|375-387|async def function(file_path: str)|
|`get_webmanifest`|fn|pub|390-426|async def get_webmanifest()|
|`get_manifest`|fn|pub|431-512|async def get_manifest()|
|`get_results`|fn|pub|515-627|async def get_results(config_url: str, stream_type: str, ...|
|`head_playback`|fn|pub|630-647|async def head_playback(config: str, query: str, request:...|
|`get_playback`|fn|pub|650-685|async def get_playback(config_url: str, query_string: str...|
|`update_app`|fn|pub|690-755|async def update_app()|


---

# cinemeta.py | Python | 43L | 2 symbols | 4 imports | 3 comments
> Path: `src/debriddo/metdata/cinemeta.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class Cinemeta(MetadataProvider)` : MetadataProvider (L11-43)
- fn `async def get_metadata(self, id, type)` (L13-43)
  L19> Usa il client asincrono
  L42> `return result`
  L43> `return None`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Cinemeta`|class|pub|11-43|class Cinemeta(MetadataProvider)|
|`Cinemeta.get_metadata`|fn|pub|13-43|async def get_metadata(self, id, type)|


---

# metadata_provider_base.py | Python | 39L | 4 symbols | 1 imports | 3 comments
> Path: `src/debriddo/metdata/metadata_provider_base.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class MetadataProvider` (L7-39)
- fn `def __init__(self, config)` `priv` (L9-13)
- fn `def replace_weird_characters(self, string)` (L14-37)
  L36> `return string`
- fn `async def get_metadata(self, id, type)` (L38-39)
  L39> `raise NotImplementedError`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MetadataProvider`|class|pub|7-39|class MetadataProvider|
|`MetadataProvider.__init__`|fn|priv|9-13|def __init__(self, config)|
|`MetadataProvider.replace_weird_characters`|fn|pub|14-37|def replace_weird_characters(self, string)|
|`MetadataProvider.get_metadata`|fn|pub|38-39|async def get_metadata(self, id, type)|


---

# tmdb.py | Python | 55L | 2 symbols | 6 imports | 3 comments
> Path: `src/debriddo/metdata/tmdb.py`
> VERSION: 0.0.35

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

### class `class TMDB(MetadataProvider)` : MetadataProvider (L12-55)
- fn `async def get_metadata(self, id, type)` (L14-55)
  L24> Usa il client asincrono
  L55> `return result`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TMDB`|class|pub|12-55|class TMDB(MetadataProvider)|
|`TMDB.get_metadata`|fn|pub|14-55|async def get_metadata(self, id, type)|


---

# media.py | Python | 22L | 2 symbols | 0 imports | 5 comments
> Path: `src/debriddo/models/media.py`
> VERSION: 0.0.35

## Definitions

### class `class Media` (L5-22)
L2> AUTHORS: aymene69
- fn `def __init__(self, id, titles, languages, type)` `priv` (L9-22) L6> Rappresenta un media generico (film o serie TV).
  L10-18> Inizializza un oggetto Media. Args: id (str): L'identificatore del media (es. IMDB ID). titles (list): Lista dei titoli associati. languages (list): Lista delle lingue. type (str): Il tipo di media ('movie' o 'series').

## Comments
- L10: Inizializza un oggetto Media. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Media`|class|pub|5-22|class Media|
|`Media.__init__`|fn|priv|9-22|def __init__(self, id, titles, languages, type)|


---

# movie.py | Python | 22L | 2 symbols | 1 imports | 5 comments
> Path: `src/debriddo/models/movie.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.models.media import Media
```

## Definitions

### class `class Movie(Media)` : Media (L7-22)
- fn `def __init__(self, id, titles, year, languages)` `priv` (L11-22) L8> Rappresenta un film.
  L12-20> Inizializza un oggetto Movie. Args: id (str): L'identificatore del film. titles (list): Lista dei titoli. year (str|int): L'anno di uscita. languages (list): Lista delle lingue.

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L12: Inizializza un oggetto Movie. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Movie`|class|pub|7-22|class Movie(Media)|
|`Movie.__init__`|fn|priv|11-22|def __init__(self, id, titles, year, languages)|


---

# series.py | Python | 25L | 2 symbols | 1 imports | 5 comments
> Path: `src/debriddo/models/series.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.models.media import Media
```

## Definitions

### class `class Series(Media)` : Media (L7-25)
- fn `def __init__(self, id, titles, season, episode, languages)` `priv` (L11-25) L8> Rappresenta un episodio di una serie TV.
  L12-21> Inizializza un oggetto Series. Args: id (str): L'identificatore della serie. titles (list): Lista dei titoli. season (str): Identificatore della stagione (es. S01). episode (str): Identificatore dell'episodio (es. E01). languages (list): Lista delle lingue.

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L12: Inizializza un oggetto Series. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Series`|class|pub|7-25|class Series(Media)|
|`Series.__init__`|fn|priv|11-25|def __init__(self, id, titles, season, episode, languages)|


---

# base_plugin.py | Python | 18L | 5 symbols | 1 imports | 2 comments
> Path: `src/debriddo/search/plugins/base_plugin.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class BasePlugin` (L6-18)
- fn `def __init__(self, config)` `priv` (L7-10)
- fn `async def login(self, session=None) -> bool | None` (L11-13)
- fn `async def search(self, what, cat='all')` (L14-16)
  L15> `raise NotImplementedError`
- fn `async def download_torrent(self, info)` (L17-18)
  L18> `raise NotImplementedError`

## Comments
- L2: AUTHORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BasePlugin`|class|pub|6-18|class BasePlugin|
|`BasePlugin.__init__`|fn|priv|7-10|def __init__(self, config)|
|`BasePlugin.login`|fn|pub|11-13|async def login(self, session=None) -> bool | None|
|`BasePlugin.search`|fn|pub|14-16|async def search(self, what, cat='all')|
|`BasePlugin.download_torrent`|fn|pub|17-18|async def download_torrent(self, info)|


---

# ilcorsaroblu.py | Python | 304L | 7 symbols | 7 imports | 29 comments
> Path: `src/debriddo/search/plugins/ilcorsaroblu.py`
> VERSION: 0.0.35

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

### class `class ilcorsaroblu(BasePlugin)` : BasePlugin (L12-211)
L18> uncomment appropriate lines to include TPB category in qBittorrent search category
L19> currently set to include only HD video for "movies" & "tv
L24> Parodie
L25> DVD-R (DVD5 & DVD9)
L26> 1080p
L27> 720p
L28> 3D
L29> BDRip-mkv-h264
L30> Movies - Films
L31> 4K-UltraHD
L32> Anime
L33> Cartoons
L34> Documentari
L35> Films (TNT Village)
L36> Sport / Gare
L37> Commedia
L38> BDRip-mkv-h264-TNT
L42> Fumetti
L43> Pdf
L44> eBooks
L45> Romanzi
L46> Edicola: Giornali/Quotidiani
L50> Games -> Console
L51> Games -> Xbox360
L52> Retro Games
L53> Games -> Nintendo
L54> Games -> PC
L58> Audio -> Mp3
L59> Radio Trasmissioni
L60> Audio / Music
L64> Archive
L66> but not games
L68> Windows
L69> Linux
L70> Macintosh-Apple
L71> Student's Office
L72> Android
L73> iOS / iPhone
L77> TV Show 1080p
L78> TV Show 720p
L79> TV Show Standard
L80> TV Show (TNT Village)
L84> Disegni e Modelli
L85> Other
L86> Adult
L90> V.I.P.
L91> Premium
L202> Usa il client asincrono
L204> login
L207> `return None`
L211> Esegui la ricerca
- fn `def __init__(self, config)` `priv` (L113-120)
  L115> Dati del form di autenticazione
- fn `async def __extract_info_hash(self, html_content, suffix_to_remove=" - il CorSaRo Blu")` `priv` (L121-150)
  L122-127> Estrae l'info hash da un contenuto HTML. :param html_content: stringa contenente il contenuto HTML :return: lista di info hash trovati (può essere vuota se non ce ne sono)
  L130> Trova name
  L135> Rimuovi il suffisso, se presente
  L139> Trova il primo input con name="info_hash
  L147> `return info_hash, name`
  L149> `return None`
- fn `async def __generate_magnet_link(self, info_hash, name=None, tracker_urls=None)` `priv` (L151-178)
  L152-159> Genera un magnet link dato un info hash, un nome e (opzionalmente) una lista di tracker URLs. :param info_hash: stringa contenente l'info hash (SHA-1) del torrent :param name: stringa contenente il nome descrittivo del torrent (opzionale) :param tracker_urls: lista di URL dei tracker opzionali (default: None) :return: stringa con il magnet link generato
  L160> Base del magnet link con l'info hash
  L163> Aggiungi il nome se fornito
  L165> Codifica il nome per essere compatibile con URL
  L170> Aggiungi i tracker se forniti
  L172> Aggiungi ogni tracker al magnet link
  L176> `return base_magnet`
- fn `async def login(self, session=None)` (L179-199)
  L181> `return False`
  L182> Esegui il login
  L188> Verifica se il login è stato effettuato correttamente
  L192> `return True`
  L197> `return False`

### fn `async def download_torrent(self,info)` (L200-228)
L202> Usa il client asincrono
L204> login
L207> `return None`
L211> Esegui la ricerca
L222> `return magnet_link`
L227> `return None`

### fn `async def search(self,what,cat='all')` (L229-304)
L230> Usa il client asincrono
L232> login
L235> `return None`
L245> TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
L248> URL e parametri per la ricerca
L251> Esegui la ricerca
L256> Parsing della risposta HTML
L259> Identifica righe della tabella con classe "lista
L261> Identifica righe della tabella con classe "lista
L263> Estrai i dati desiderati
L266> scarta l'intestazione
L268> Assicura che ci siano abbastanza colonne
L278> non usati
L279> Data": date,
L280> C": completed,
L293> Stampa i risultati
L296> salta l'intestazione
L304> `return prettyPrinter.get()`

## Comments
- L2: AUTHORS: Ogekuri
- L18-19: uncomment appropriate lines to include TPB category in qBittorrent search category | currently set to include only HD video for "movies" & "tv
- L115: Dati del form di autenticazione
- L122: Estrae l'info hash da un contenuto HTML. :param html_content: stringa contenente il contenuto HTML ...
- L130: Trova name
- L135: Rimuovi il suffisso, se presente
- L139: Trova il primo input con name="info_hash
- L152-160: Genera un magnet link dato un info hash, un nome e (opzionalmente) una lista di tracker URLs. :pa... | Base del magnet link con l'info hash
- L163-165: Aggiungi il nome se fornito | Codifica il nome per essere compatibile con URL
- L170-172: Aggiungi i tracker se forniti | Aggiungi ogni tracker al magnet link
- L182: Esegui il login
- L188: Verifica se il login è stato effettuato correttamente
- L204: login
- L211: Esegui la ricerca
- L232: login
- L245: TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
- L248: URL e parametri per la ricerca
- L251: Esegui la ricerca
- L256: Parsing della risposta HTML
- L263: Estrai i dati desiderati
- L278-280: non usati | Data": date, | C": completed,
- L293: Stampa i risultati

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ilcorsaroblu`|class|pub|12-211|class ilcorsaroblu(BasePlugin)|
|`ilcorsaroblu.__init__`|fn|priv|113-120|def __init__(self, config)|
|`ilcorsaroblu.__extract_info_hash`|fn|priv|121-150|async def __extract_info_hash(self, html_content, suffix_...|
|`ilcorsaroblu.__generate_magnet_link`|fn|priv|151-178|async def __generate_magnet_link(self, info_hash, name=No...|
|`ilcorsaroblu.login`|fn|pub|179-199|async def login(self, session=None)|
|`download_torrent`|fn|pub|200-228|async def download_torrent(self,info)|
|`search`|fn|pub|229-304|async def search(self,what,cat='all')|


---

# ilcorsaronero.py | Python | 110L | 7 symbols | 6 imports | 8 comments
> Path: `src/debriddo/search/plugins/ilcorsaronero.py`
> VERSION: 0.0.35

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

### class `class ilcorsaronero(BasePlugin)` : BasePlugin (L13-110)
L38> `return`
L54> Find all TR nodes with class odd or odd2
L56> Skip the first TR node because it's the header
L57> Extract from the A node all the needed information
L72> `return torrents`
- fn `async def download_torrent(self, info)` (L74-89)
  L75> Usa il client asincrono
  L83> `return(str(magnet_str + " " + magnet_str))`
  L86> `raise Exception('Error, please fill a bug report!')`
  L88> `return None`
- fn `async def search(self, what, cat='all')` (L90-110)
  L91> Usa il client asincrono
  L96> filter = '&cat={0}'.format(self.supported_categories[cat])
  L98> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L101> Some replacements to format the html source
  L110> `return prettyPrinter.get()`

### class `class HTMLParser` (L27-73)
- fn `def __init__(self, url)` `priv` (L29-32)
- fn `def feed(self, html)` (L33-51)
  L38> `return`
- fn `def __findTorrents(self, html)` `priv` (L52-73)
  L54> Find all TR nodes with class odd or odd2
  L56> Skip the first TR node because it's the header
  L57> Extract from the A node all the needed information
  L72> `return torrents`

## Comments
- L2-3: AUTHORS: LightDestory (https://github.com/LightDestory) | CONTRIBUTORS: Ogekuri
- L54: Find all TR nodes with class odd or odd2
- L57: Extract from the A node all the needed information
- L96-98: filter = '&cat={0}'.format(self.supported_categories[cat]) | TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
- L101: Some replacements to format the html source

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ilcorsaronero`|class|pub|13-110|class ilcorsaronero(BasePlugin)|
|`HTMLParser`|class|pub|27-73|class HTMLParser|
|`HTMLParser.__init__`|fn|priv|29-32|def __init__(self, url)|
|`HTMLParser.feed`|fn|pub|33-51|def feed(self, html)|
|`HTMLParser.__findTorrents`|fn|priv|52-73|def __findTorrents(self, html)|
|`ilcorsaronero.download_torrent`|fn|pub|74-89|async def download_torrent(self, info)|
|`ilcorsaronero.search`|fn|pub|90-110|async def search(self, what, cat='all')|


---

# limetorrents.py | Python | 157L | 9 symbols | 9 imports | 9 comments
> Path: `src/debriddo/search/plugins/limetorrents.py`
> VERSION: 0.0.35

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

### class `class limetorrents(BasePlugin)` : BasePlugin (L20-157)
L34> Sub-class for parsing results
L44> dict for found item
L49> key's name in current_item dict
L69> `return`
L71> noqa
L76> `return`
- fn `async def download_torrent(self, info)` (L122-137)
  L123> Usa il client asincrono
  L124> since limetorrents provides torrent links in itorrent (cloudflare protected),
  L125> we have to fetch the info page and extract the magnet link
  L131> `return(str(magnet_match.groups()[0] + " " + info))`
  L134> `raise Exception('Error, please fill a bug report!')`
  L136> `return None`
- fn `async def search(self, what, cat='all')` (L138-157)
  L139> Usa il client asincrono
  L140> Performs search
  L146> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L157> `return prettyPrinter.get()`

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L33-121)
- fn `def error(self, message)` (L36-38) L34> Sub-class for parsing results
- fn `def __init__(self, url)` `priv` (L41-62)
  L44> dict for found item
  L49> key's name in current_item dict
- fn `def handle_starttag(self, tag, attrs)` (L63-94)
  L69> `return`
  L71> noqa
  L76> `return`
- fn `def handle_data(self, data)` (L95-109)
- fn `def handle_endtag(self, tag)` (L110-121)

## Comments
- L2-3: AUTHORS: Lima66 | CONTRIBUTORS: Ogekuri, Diego de las Heras (ngosang@hotmail.es)
- L15: Fix invalid certificate in Windows
- L124-125: since limetorrents provides torrent links in itorrent (cloudflare protected), | we have to fetch the info page and extract the magnet link
- L140: Performs search
- L146: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`limetorrents`|class|pub|20-157|class limetorrents(BasePlugin)|
|`MyHtmlParser`|class|pub|33-121|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|36-38|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|41-62|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|63-94|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|95-109|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|110-121|def handle_endtag(self, tag)|
|`limetorrents.download_torrent`|fn|pub|122-137|async def download_torrent(self, info)|
|`limetorrents.search`|fn|pub|138-157|async def search(self, what, cat='all')|


---

# one337x.py | Python | 159L | 9 symbols | 7 imports | 32 comments
> Path: `src/debriddo/search/plugins/one337x.py`
> VERSION: 0.0.35

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

### class `class one337x(BasePlugin)` : BasePlugin (L33-159)
L74> `return`
L77> `return`
L80> `return`
L87> `return`
L91> `return`
L95> fix non scarico subito il file
L96> torrent_page = retrieve_url(link)
L97> magnet_regex = r'href="magnet:.
L98> matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE)
L99> magnet_urls = [x.group() for x in matches]
L100> self.row['link'] = magnet_urls[0].split('"')[1]
L101> self.row['engine_url'] = self.url
L102> self.row['desc_link'] = link
L121> `return`
- fn `async def download_torrent(self, info)` (L125-139)
  L126> Usa il client asincrono
  L127> fix le info dopo
  L136> `return(str(magnet))`
  L138> `return None`
- fn `async def search(self, what, cat='all')` (L140-159)
  L141> Usa il client asincrono
  L147> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L154> exists on every page but the last
  L159> `return prettyPrinter.get()`

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L48-124)
- fn `def error(self, message)` (L50-52)
- fn `def __init__(self, url)` `priv` (L55-69)
- fn `def handle_starttag(self, tag, attrs)` (L70-106)
  L74> `return`
  L77> `return`
  L80> `return`
  L87> `return`
  L91> `return`
  L95> fix non scarico subito il file
  L96> torrent_page = retrieve_url(link)
  L97> magnet_regex = r'href="magnet:.
  L98> matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE)
  L99> magnet_urls = [x.group() for x in matches]
  L100> self.row['link'] = magnet_urls[0].split('"')[1]
  L101> self.row['engine_url'] = self.url
  L102> self.row['desc_link'] = link
- fn `def handle_data(self, data)` (L107-113)
- fn `def handle_endtag(self, tag)` (L114-124)
  L121> `return`

## Comments
- L2-22: AUTHORS: sa3dany, Alyetama, BurningMop, scadams | CONTRIBUTORS: Ogekuri | LICENSING INFORMATION | Permission is hereby granted, free of charge, to any person obtaining a copy | of this software and associated documentation files (the "Software"), to deal | in the Software without restriction, including without limitation the rights | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell | copies of the Software, and to permit persons to whom the Software is | furnished to do so, subject to the following conditions: | The above copyright notice and this permission notice shall be included in | all copies or substantial portions of the Software. | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE | SOFTWARE.
- L95-102: fix non scarico subito il file | torrent_page = retrieve_url(link) | magnet_regex = r'href="magnet:. | matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE) | magnet_urls = [x.group() for x in matches] | self.row['link'] = magnet_urls[0].split('"')[1] | self.row['engine_url'] = self.url | self.row['desc_link'] = link
- L127: fix le info dopo
- L147: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
- L154: exists on every page but the last

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`one337x`|class|pub|33-159|class one337x(BasePlugin)|
|`MyHtmlParser`|class|pub|48-124|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|50-52|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|55-69|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|70-106|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|107-113|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|114-124|def handle_endtag(self, tag)|
|`one337x.download_torrent`|fn|pub|125-139|async def download_torrent(self, info)|
|`one337x.search`|fn|pub|140-159|async def search(self, what, cat='all')|


---

# thepiratebay_categories.py | Python | 153L | 4 symbols | 7 imports | 13 comments
> Path: `src/debriddo/search/plugins/thepiratebay_categories.py`
> VERSION: 0.0.35

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

### class `class thepiratebay(BasePlugin)` : BasePlugin (L15-43)
L22> uncomment appropriate lines to include TPB category in qBittorrent search category
L23> currently set to include only HD video for "movies" & "tv
L28> Video > HD - Movies
L29> Video > HD - TV shows
L30> Video > Movies
L31> Video > Movies DVDR
L32> Video > TV shows
L33> Video > Handheld
L34> Video > 3D
L35> Video > Other
L36> Porn > Movies
L37> Porn > Movies DVDR
L38> Porn > HD - Movies
L39> Porn > Other			!!! comma after each number...
L40> Other > Other			!!! ...except the last!

### fn `async def download_torrent(self,info)` (L101-121)
L102> Usa il client asincrono
L112> `return(str(self.magnet.format(hash		=data['info_hash'],`
L118> `raise Exception('Error in "'+self.name+'" search plugin, download_torrent()')`
L120> `return None`

### fn `async def search(self,what,cat='all')` (L122-140)
L123> Usa il client asincrono
L127> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
L130> fix risulati nulli
L139> `return prettyPrinter.get()`

### fn `def parseJSON(self,collection)` (L141-153)

## Comments
- L2-3: AUTHORS: Scare! (https://Scare.ca/dl/qBittorrent/) | CONTRIBUTORS: Ogekuri, LightDestory https://github.com/LightDestory
- L22-23: uncomment appropriate lines to include TPB category in qBittorrent search category | currently set to include only HD video for "movies" & "tv
- L44: 102,	# Audio > Audio books
- L55-57: 201,	# Video > Movies | 202,	# Video > Movies DVDR | 209,	# Video > 3D
- L62: 203,	# Video > Music videos
- L78: 205,	# Video > TV shows
- L127: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
- L130: fix risulati nulli

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`thepiratebay`|class|pub|15-43|class thepiratebay(BasePlugin)|
|`download_torrent`|fn|pub|101-121|async def download_torrent(self,info)|
|`search`|fn|pub|122-140|async def search(self,what,cat='all')|
|`parseJSON`|fn|pub|141-153|def parseJSON(self,collection)|


---

# therarbg.py | Python | 208L | 11 symbols | 7 imports | 26 comments
> Path: `src/debriddo/search/plugins/therarbg.py`
> VERSION: 0.0.35

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

### class `class therarbg(BasePlugin)` : BasePlugin (L34-208)
L107> torrent_page = await session.retrieve_url(link)
L108> matches = re.finditer(self.magnet_regex, torrent_page, re.MULTILINE)
L109> magnet_urls = [x.group() for x in matches]
L110> self.row['link'] = magnet_urls[0].split('"')[1]
- fn `async def download_torrent(self, info)` (L160-173)
  L161> Usa il client asincrono
  L168> `return str(magnet_urls[0].split('"')[1])`
  L172> `return None`
- fn `def getPageUrl(self, what, cat, page)` (L174-179)
  L176> `return f'{self.url}/get-posts/order:-se:category:{cat}:keywords:{what}/?page={page}'`
  L178> `return f'{self.url}/get-posts/order:-se:keywords:{what}/?page={page}'`
- fn `async def page_search(self, session, page, what, cat)` (L180-194)
- fn `async def search(self, what, cat = 'all')` (L195-208)
  L196> Usa il client asincrono
  L202> TODO: leggere prima il numero di pagine e poi mandare le richieste in modo asincrono
  L208> `return prettyPrinter.get()`

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L54-159)
- fn `def error(self, message)` (L56-58)
- fn `def __init__(self, url)` `priv` (L61-81)
- fn `def handle_starttag(self, tag, attrs)` (L82-124)
  L107> torrent_page = await session.retrieve_url(link)
  L108> matches = re.finditer(self.magnet_regex, torrent_page, re.MULTILINE)
  L109> magnet_urls = [x.group() for x in matches]
  L110> self.row['link'] = magnet_urls[0].split('"')[1]
- fn `def handle_data(self, data)` (L125-146)
- fn `def handle_endtag(self, tag)` (L147-159)

## Comments
- L2-22: AUTHORS: BurningMop (burning.mop@yandex.com) | CONTRIBUTORS: Ogekuri | LICENSING INFORMATION | Permission is hereby granted, free of charge, to any person obtaining a copy | of this software and associated documentation files (the "Software"), to deal | in the Software without restriction, including without limitation the rights | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell | copies of the Software, and to permit persons to whom the Software is | furnished to do so, subject to the following conditions: | The above copyright notice and this permission notice shall be included in | all copies or substantial portions of the Software. | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE | SOFTWARE.
- L107-110: torrent_page = await session.retrieve_url(link) | matches = re.finditer(self.magnet_regex, torrent_page, re.MULTILINE) | magnet_urls = [x.group() for x in matches] | self.row['link'] = magnet_urls[0].split('"')[1]
- L202: TODO: leggere prima il numero di pagine e poi mandare le richieste in modo asincrono

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`therarbg`|class|pub|34-208|class therarbg(BasePlugin)|
|`MyHtmlParser`|class|pub|54-159|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|56-58|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|61-81|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|82-124|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|125-146|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|147-159|def handle_endtag(self, tag)|
|`therarbg.download_torrent`|fn|pub|160-173|async def download_torrent(self, info)|
|`therarbg.getPageUrl`|fn|pub|174-179|def getPageUrl(self, what, cat, page)|
|`therarbg.page_search`|fn|pub|180-194|async def page_search(self, session, page, what, cat)|
|`therarbg.search`|fn|pub|195-208|async def search(self, what, cat = 'all')|


---

# torrentgalaxyone.py | Python | 117L | 3 symbols | 6 imports | 14 comments
> Path: `src/debriddo/search/plugins/torrentgalaxyone.py`
> VERSION: 0.0.35

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

### class `class torrentgalaxy(BasePlugin)` : BasePlugin (L13-117)
L18> debug=True
L20> uncomment appropriate lines to include TPB category in qBittorrent search category
L21> currently set to include only HD video for "movies" & "tv
- fn `async def download_torrent(self,info)` (L38-59)
  L39> Usa il client asincrono
  L41> Esegui la ricerca
  L46> Parsing della risposta HTML
  L49> Trova la prima tabella
  L53> `return magnet_link`
  L58> `return None`
- fn `async def search(self,what,cat='all')` (L60-117)
  L61> Usa il client asincrono
  L67> TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
  L70> URL e parametri per la ricerca
  L73> Esegui la ricerca
  L78> Parsing della risposta HTML
  L81> Trova la prima tabella
  L83> Trova la prima tabella
  L86> 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF
  L87> - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf
  L88> - /get-posts/keywords:tt14257582
  L92> Divide per "/" e converte in interi
  L106> Stampa i risultati
  L109> salta l'intestazione
  L117> `return prettyPrinter.get()`

## Comments
- L2: AUTHORS: Ogekuri
- L20-21: uncomment appropriate lines to include TPB category in qBittorrent search category | currently set to include only HD video for "movies" & "tv
- L41: Esegui la ricerca
- L46: Parsing della risposta HTML
- L67: TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
- L70: URL e parametri per la ricerca
- L73: Esegui la ricerca
- L78: Parsing della risposta HTML
- L86-88: 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF | - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf | - /get-posts/keywords:tt14257582
- L106: Stampa i risultati

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentgalaxy`|class|pub|13-117|class torrentgalaxy(BasePlugin)|
|`torrentgalaxy.download_torrent`|fn|pub|38-59|async def download_torrent(self,info)|
|`torrentgalaxy.search`|fn|pub|60-117|async def search(self,what,cat='all')|


---

# torrentgalaxyto.py | Python | 156L | 7 symbols | 10 imports | 23 comments
> Path: `src/debriddo/search/plugins/torrentgalaxyto.py`
> VERSION: 0.0.35

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

- var `SITE_URL = "https://torrentgalaxy.to/"` (L37)
### class `class torrentgalaxy(BasePlugin)` : BasePlugin (L39-153)
L66> if (my_attrs.get('class') == 'tgxtablerow txlight'):
- fn `async def do_search(self, session, url)` (L119-124)
- fn `async def search(self, what, cat='all')` (L125-153)
  L126> Usa il client asincrono
  L147> TODO: run in multi-thread?
  L152> `return prettyPrinter.get()`

### class `class TorrentGalaxyParser(HTMLParser)` : HTMLParser (L56-118)
- fn `def handle_starttag(self, tag, attrs)` (L63-104)
  L66> if (my_attrs.get('class') == 'tgxtablerow txlight'):
- fn `def handle_data(self, data)` (L105-118)

## Comments
- L2-22: AUTHORS: nindogo (nindogo@gmail.com) | CONTRIBUTORS: Ogekuri | LICENSING INFORMATION | Permission is hereby granted, free of charge, to any person obtaining a copy | of this software and associated documentation files (the "Software"), to deal | in the Software without restriction, including without limitation the rights | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell | copies of the Software, and to permit persons to whom the Software is | furnished to do so, subject to the following conditions: | The above copyright notice and this permission notice shall be included in | all copies or substantial portions of the Software. | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE | SOFTWARE.
- L66: if (my_attrs.get('class') == 'tgxtablerow txlight'):
- L147: TODO: run in multi-thread?

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SITE_URL`|var|pub|37||
|`torrentgalaxy`|class|pub|39-153|class torrentgalaxy(BasePlugin)|
|`TorrentGalaxyParser`|class|pub|56-118|class TorrentGalaxyParser(HTMLParser)|
|`TorrentGalaxyParser.handle_starttag`|fn|pub|63-104|def handle_starttag(self, tag, attrs)|
|`TorrentGalaxyParser.handle_data`|fn|pub|105-118|def handle_data(self, data)|
|`torrentgalaxy.do_search`|fn|pub|119-124|async def do_search(self, session, url)|
|`torrentgalaxy.search`|fn|pub|125-153|async def search(self, what, cat='all')|


---

# torrentproject.py | Python | 143L | 9 symbols | 7 imports | 18 comments
> Path: `src/debriddo/search/plugins/torrentproject.py`
> VERSION: 0.0.35

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

### class `class torrentproject(BasePlugin)` : BasePlugin (L15-119)
L44> `return {`
L77> ignore trash stuff
L81> ignore those with link and desc_link equals to -1
L84> fix
L85> data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago
L87> try:
L88> date_string = self.singleResData['pub_date']
L89> date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
L90> self.singleResData['pub_date'] = int(date.timestamp())
L91> except Exception:
L92> logger.error("self.singleResData['pub_date']", self.singleResData)
- fn `async def search(self, what, cat='all')` (L109-119)
  L110> Usa il client asincrono
  L112> curr_cat = self.supported_categories[cat]
  L116> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L118> analyze first 5 pages of results

### class `class MyHTMLParser(HTMLParser)` : HTMLParser (L22-108)
- fn `def __init__(self, url)` `priv` (L24-42)
- fn `def get_single_data(self)` (L43-54)
  L44> `return {`
- fn `def handle_starttag(self, tag, attrs)` (L55-70)
- fn `def handle_endtag(self, tag)` (L71-97)
  L77> ignore trash stuff
  L81> ignore those with link and desc_link equals to -1
  L84> fix
  L85> data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago
  L87> try:
  L88> date_string = self.singleResData['pub_date']
  L89> date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
  L90> self.singleResData['pub_date'] = int(date.timestamp())
  L91> except Exception:
  L92> logger.error("self.singleResData['pub_date']", self.singleResData)
- fn `def handle_data(self, data)` (L98-108)

### fn `async def download_torrent(self, info)` (L132-143)
L133> Usa il client asincrono
L134> Downloader
L141> `return(str(magnet + ' ' + info))`
L143> `return None`

## Comments
- L2-3: AUTHORS: mauricci | CONTRIBUTORS: Ogekuri
- L77: ignore trash stuff
- L81: ignore those with link and desc_link equals to -1
- L84-92: fix | data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago | try: | date_string = self.singleResData['pub_date'] | date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S') | self.singleResData['pub_date'] = int(date.timestamp()) | except Exception: | logger.error("self.singleResData['pub_date']", self.singleResData)
- L112: curr_cat = self.supported_categories[cat]
- L116-120: TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina | analyze first 5 pages of results | url = self.url + '/browse?t={0}&p={1}'.format(what, currPage)
- L134: Downloader

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentproject`|class|pub|15-119|class torrentproject(BasePlugin)|
|`MyHTMLParser`|class|pub|22-108|class MyHTMLParser(HTMLParser)|
|`MyHTMLParser.__init__`|fn|priv|24-42|def __init__(self, url)|
|`MyHTMLParser.get_single_data`|fn|pub|43-54|def get_single_data(self)|
|`MyHTMLParser.handle_starttag`|fn|pub|55-70|def handle_starttag(self, tag, attrs)|
|`MyHTMLParser.handle_endtag`|fn|pub|71-97|def handle_endtag(self, tag)|
|`MyHTMLParser.handle_data`|fn|pub|98-108|def handle_data(self, data)|
|`torrentproject.search`|fn|pub|109-119|async def search(self, what, cat='all')|
|`download_torrent`|fn|pub|132-143|async def download_torrent(self, info)|


---

# torrentz.py | Python | 91L | 3 symbols | 7 imports | 11 comments
> Path: `src/debriddo/search/plugins/torrentz.py`
> VERSION: 0.0.35

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

### class `class torrentz(BasePlugin)` : BasePlugin (L14-91)
L19-22> TLDR; It is safer to force an 'all' research Torrentz2 categories not supported
L77> `return results`
- fn `def __parseHTML(self, html)` `priv` (L26-65)
  L30> Trova tutti i blocchi <dl> nella pagina
  L32> Estrai il titolo e il link
  L42> Estrai il magnet link
  L51> Estrai gli altri campi
  L59> rmuove i caratteri che non sono numeri
  L64> Crea il dizionario per il risultato
- fn `async def search(self, what, cat='all')` (L79-91)
  L80> Usa il client asincrono
  L83> url = '{0}search?q={1}&cat=0'.format(self.api_url, what)
  L84> TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
  L90> `return prettyPrinter.get()`

## Comments
- L2: AUTHORS: Ogekuri
- L19: TLDR; It is safer to force an 'all' research Torrentz2 categories not supported
- L30-32: Trova tutti i blocchi <dl> nella pagina | Estrai il titolo e il link
- L42: Estrai il magnet link
- L51: Estrai gli altri campi
- L59: rmuove i caratteri che non sono numeri
- L64: Crea il dizionario per il risultato
- L83-84: url = '{0}search?q={1}&cat=0'.format(self.api_url, what) | TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentz`|class|pub|14-91|class torrentz(BasePlugin)|
|`torrentz.__parseHTML`|fn|priv|26-65|def __parseHTML(self, html)|
|`torrentz.search`|fn|pub|79-91|async def search(self, what, cat='all')|


---

# search_indexer.py | Python | 15L | 2 symbols | 1 imports | 2 comments
> Path: `src/debriddo/search/search_indexer.py`
> VERSION: 0.0.35

## Imports
```
from typing import Any
```

## Definitions

### class `class SearchIndexer` (L7-15)
- fn `def __init__(self)` `priv` (L8-15)
  L9> general name
  L10> id
  L11> supported language
  L14> engine object
  L15> engine name

## Comments
- L2: AUTHORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SearchIndexer`|class|pub|7-15|class SearchIndexer|
|`SearchIndexer.__init__`|fn|priv|8-15|def __init__(self)|


---

# search_result.py | Python | 111L | 4 symbols | 4 imports | 24 comments
> Path: `src/debriddo/search/search_result.py`
> VERSION: 0.0.35

## Imports
```
from RTN import parse
from debriddo.models.series import Series
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class SearchResult` (L12-111)
- fn `def __init__(self)` `priv` (L16-42) L13> Rappresenta un risultato di ricerca grezzo dai motori torrent.
  L17-19> Inizializza un oggetto SearchResult vuoto.
  L20> Raw title of the torrent
  L21> Title of the torrent
  L22> Size of the torrent
  L23> Download link for the torrent file or magnet url
  L24> Indexer
  L25> Seeders count
  L27> Indexer Name
  L29> Magnet url
  L30> infoHash by Search
  L31> public or private (determina se sarà o meno salvato in cache)
  L33> Extra processed details for further filtering
  L34> Language of the torrent
  L35> series or movie
  L37> from cache?
  L40> parsed data
  L41> Ranked result
- fn `def convert_to_torrent_item(self)` (L43-82) L40> parsed data
  L44-49> Converte questo risultato in un oggetto TorrentItem. Returns: TorrentItem: L'oggetto TorrentItem convertito.
  L50> def TorrentItem::__init__(self,
  L51> raw_title,
  L52> title,
  L53> size,
  L54> magnet,
  L55> info_hash,
  L56> link,
  L57> seeders,
  L58> languages,
  L59> indexer,
  L60> engine_name,
  L61> privacy,
  L62> type=None,
  L63> parsed_data=None,
  L64> from_cache=False):
  L66> `return TorrentItem(`
  L75> ilCorSaRoNeRo
  L76> ilcorsaronero (tutto minuscolo)
- fn `def from_cached_item(self, cached_item)` (L83-111)
  L84-92> Popola il SearchResult da un dizionario di item in cache. Args: cached_item (dict): Il dizionario contenente i dati della cache. Returns: SearchResult: L'istanza stessa popolata.
  L111> `return self`

## Comments
- L2: AUTHORS: Ogekuri
- L17: Inizializza un oggetto SearchResult vuoto.
- L33: Extra processed details for further filtering
- L37: from cache?
- L44-64: Converte questo risultato in un oggetto TorrentItem. Returns: ... | def TorrentItem::__init__(self, | raw_title, | title, | size, | magnet, | info_hash, | link, | seeders, | languages, | indexer, | engine_name, | privacy, | type=None, | parsed_data=None, | from_cache=False):
- L84: Popola il SearchResult da un dizionario di item in cache. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SearchResult`|class|pub|12-111|class SearchResult|
|`SearchResult.__init__`|fn|priv|16-42|def __init__(self)|
|`SearchResult.convert_to_torrent_item`|fn|pub|43-82|def convert_to_torrent_item(self)|
|`SearchResult.from_cached_item`|fn|pub|83-111|def from_cached_item(self, cached_item)|


---

# search_service.py | Python | 689L | 20 symbols | 29 imports | 55 comments
> Path: `src/debriddo/search/search_service.py`
> VERSION: 0.0.35

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

- var `SEARCHE_FALL_BACK = True` (L43) — Se non trova risultati prova una ricerca più estesa
### class `class SearchService` (L45-244)
- fn `def __init__(self, config)` `priv` (L49-80) L46> Servizio principale per la ricerca di torrent su diversi indexer.
  L50-55> Inizializza il servizio di ricerca. Args: config (dict): La configurazione dell'applicazione.
- fn `async def search(self, media)` (L81-148)
  L82-90> Esegue la ricerca di torrent per il media specificato. Args: media (Media): L'oggetto media (Movie o Series) da cercare. Returns: list: Una lista di oggetti SearchResult o None se nessun risultato trovato.
  L100> Invece di eseguire le coroutine direttamente sul loop principale,
  L101> le "incapsuliamo" in run_in_executor, cosi ciascuna gira in un proprio thread/loop
  L104> Ora attendiamo i risultati. Il loop principale non si bloccherà,
  L105> perché quel codice gira in un thread separato.
  L119> `return []`
  L121> concatena i risultati
  L127> spost process result ############################################
  L146> `return results`
- fn `def __get_engine(self, engine_name)` `priv` (L149-180)
  L150-158> Recupera l'istanza del plugin motore specificato. Args: engine_name (str): Il nome del motore di ricerca. Returns: object: L'istanza del plugin del motore o solleva ValueError.
  L160> `return thepiratebay(self.__config)`
  L162> `return one337x(self.__config)`
  L164> `return limetorrents(self.__config)`
  L166> `return torrentproject(self.__config)`
  L168> `return torrentz(self.__config)`
  L170> `return torrentgalaxy(self.__config)`
  L172> `return therarbg(self.__config)`
  L174> `return ilcorsaronero(self.__config)`
  L176> `return ilcorsaroblu(self.__config)`
  L178> `raise ValueError(f"Torrent Search '{engine_name}' not supported")`
- fn `def __get_requested_languages(self)` `priv` (L181-193)
  L182-187> Recupera la lista delle lingue richieste dalla configurazione. Returns: list: Lista di codici lingua o [None].
  L190> `return config_languages`
  L191> `return [None]`
- fn `def __get_title_for_language(self, media, lang)` `priv` (L194-220)
  L195-204> Ottiene il titolo del media per la lingua specificata. Args: media (Media): L'oggetto media. lang (str): Il codice lingua. Returns: str: Il titolo localizzato o il primo titolo disponibile.
  L207> `return ""`
  L210> `return titles[0]`
  L216> `return titles[lang_index]`
  L218> `return titles[0]`
- fn `def __get_lang_tag(self, indexer_language, lang)` `priv` (L221-240)
  L222-231> Restituisce il tag lingua appropriato per la ricerca. Args: indexer_language (str): La lingua dell'indexer. lang (str): La lingua richiesta. Returns: str: Il tag lingua mappato o stringa vuota.
  L233> `return ""`
  L236> `return ""`
  L238> `return self.__language_tags.get(lang, self.__default_lang_tag)`

### fn `def __build_query(self, *parts)` `priv` (L241-254)
L242-250> Costruisce una stringa di query normalizzata concatenando le parti. Args: parts: Componenti della query. Returns: str: La query normalizzata.
L252> `return normalize(query)`

### fn `def __build_query_keep_dash(self, *parts)` `priv` (L255-272)
L256-264> Costruisce una query mantenendo i trattini, utile per ricerche specifiche. Args: parts: Componenti della query. Returns: str: La query processata e pulita.
L270> `return query.lower().strip()`

### fn `async def __search_torrents(self, media, indexer, search_string, category)` `priv` (L273-296)
L274-285> Esegue la ricerca torrent su un indexer specifico. Args: media (Media): L'oggetto media. indexer (SearchIndexer): L'indexer su cui cercare. search_string (str): La stringa di ricerca. category (str): La categoria di ricerca. Returns: list: Lista di oggetti SearchResult.
L288> `return []`
L292> `return []`
L294> `return torrents`

### fn `def __log_query_result(` `priv` (L297-303)

### fn `async def __search_movie_indexer(self, movie, indexer)` `priv` (L328-403)
L329-340> Esegue la ricerca per un film su un indexer specifico. Itera sulle lingue richieste e costruisce query appropriate. Args: movie (Movie): L'oggetto film. indexer (SearchIndexer): L'indexer su cui cercare. Returns: list: Lista di risultati trovati.
L401> `return results`

### fn `async def __search_series_indexer(self, series, indexer)` `priv` (L404-504)
L405-416> Esegue la ricerca per una serie TV su un indexer specifico. Gestisce diverse strategie di ricerca (episodio singolo, pack, stagione). Args: series (Series): L'oggetto serie TV. indexer (SearchIndexer): L'indexer su cui cercare. Returns: list: Lista di risultati trovati.
L427> Esempio balordo:
L428> Arcane.S02E01-03.WEBDL 1080p Ita Eng x264-NAHOM
L429> Arcane.S02E04-06.WEBDL 1080p Ita Eng x264-NAHOM
L430> Arcane.S02E07-09.WEBDL 1080p Ita Eng x264-NAHOM
L431> Arcane.S02.720p.ITA-ENG.MULTI.WEBRip.x265.AAC-V3SP4EV3R
L433> Se cerco S02 E02 non lo trovo da nessuna parte, ma è presente in 2 file
L434> Se cerco S02 E04 lo trova in un file, ma è presente in 2 file
L435> Se cerco S02 trova 4 file ma è presente in 2 file
L437> Decido di prendere sempe tutti i risultati e vedere se poi dopo è sufficiente filtrarli
L439> se non ci sono risultati riprova omettendo l'episodio
L440> perché ci sono i torrent con l'intera serie inclusa
L441> bisogna poi cercare il file corretto
L502> `return results`

### fn `def __get_indexers(self)` `priv` (L505-521)
L506-511> Recupera e inizializza tutti gli indexer configurati. Returns: dict: Dizionario degli indexer attivi con nome motore come chiave.
L514> creiamo un dizionario con title come chiave
L516> `return indexers`
L519> `return {}`

### fn `def __get_indexer_from_engines(self, engines)` `priv` (L522-570)
L523-531> Istanzia gli oggetti SearchIndexer a partire dalla lista di motori. Args: engines (list): Lista dei nomi dei motori da attivare. Returns: list: Lista di oggetti SearchIndexer configurati.
L568> `return indexer_list`

### fn `def __get_torrents_from_list_of_dicts(self, media, indexer, list_of_dicts)` `priv` (L571-609)
L572-582> Converte una lista di dizionari grezzi in oggetti SearchResult. Args: media (Media): L'oggetto media. indexer (SearchIndexer): L'indexer di provenienza. list_of_dicts (list): Lista di risultati grezzi dal motore. Returns: list: Lista di oggetti SearchResult.
L595> engine name 'Il Corsaro Nero
L596> engine type 'ilcorsaronero' (minuscolo)
L597> series or movie
L598> public or private (determina se sarà o meno salvato in cache)
L600> processed on __post_process_results after getting pages
L601> shoud be content the link of magnet or .torrent file
L602> but NOW contain the web page or magnet, will be __post_process_results
L603> processed on __post_process_results after getting pages
L607> `return result_list`

### fn `def __is_magnet_link(self, link)` `priv` (L610-623)
L611-619> Verifica se una stringa è un magnet link. Args: link (str): Il link da verificare. Returns: bool: True se è un magnet link, False altrimenti.
L620> Check if link inizia con "magnet:?
L621> `return link.startswith("magnet:?")`

### fn `def __extract_info_hash(self, magnet_link)` `priv` (L624-651)
L625-636> Estrae l'info hash da un magnet link. Args: magnet_link (str): Il magnet link. Returns: str: L'info hash estratto. Raises: ValueError: Se il magnet link non è valido.
L637> parse
L640> extract 'xt
L645> remove prefix "urn:btih:
L647> `return info_hash`
L649> `raise ValueError("Magnet link invalid")`

### fn `async def __post_process_result(self, indexers, result, media)` `priv` (L652-689)
L653-663> Post-processa un risultato di ricerca, risolvendo i magnet link se necessario. Args: indexers (dict): Dizionario degli indexer disponibili. result (SearchResult): Il risultato da processare. media (Media): L'oggetto media. Returns: SearchResult: Il risultato processato o None in caso di fallimento.
L674> raise Exception('Error, please fill a bug report!')
L675> se non riesce a scarica il file ritorna None
L676> `return None`
L679> parse RAW title to detect languages
L681> result.languages = [languages.get(name=language).alpha2 for language in parsed_result.language]
L683> TODO: replace with parsed_result.lang_codes when RTN is updated
L689> `return result`

## Comments
- L2: AUTHORS: Ogekuri
- L31: from search.plugins.torrentgalaxyto import torrentgalaxy
- L50: Inizializza il servizio di ricerca. Args: ...
- L82: Esegue la ricerca di torrent per il media specificato. Args: ...
- L100-101: Invece di eseguire le coroutine direttamente sul loop principale, | le "incapsuliamo" in run_in_executor, cosi ciascuna gira in un proprio thread/loop
- L104-105: Ora attendiamo i risultati. Il loop principale non si bloccherà, | perché quel codice gira in un thread separato.
- L121: concatena i risultati
- L127: spost process result ############################################
- L150: Recupera l'istanza del plugin motore specificato. Args: ...
- L182: Recupera la lista delle lingue richieste dalla configurazione. Returns: ...
- L195: Ottiene il titolo del media per la lingua specificata. Args: ...
- L222: Restituisce il tag lingua appropriato per la ricerca. Args: ...
- L242: Costruisce una stringa di query normalizzata concatenando le parti. Args: ...
- L256: Costruisce una query mantenendo i trattini, utile per ricerche specifiche. Args: ...
- L274: Esegue la ricerca torrent su un indexer specifico. Args: ...
- L305: Registra nei log i risultati di una query. Args: ...
- L329: Esegue la ricerca per un film su un indexer specifico. Itera sulle lingue richieste e costruisce query appropriate. ...
- L405: Esegue la ricerca per una serie TV su un indexer specifico. Gestisce diverse strategie di ricerca (episodio singolo, pack, stagione). ...
- L427-441: Esempio balordo: | Arcane.S02E01-03.WEBDL 1080p Ita Eng x264-NAHOM | Arcane.S02E04-06.WEBDL 1080p Ita Eng x264-NAHOM | Arcane.S02E07-09.WEBDL 1080p Ita Eng x264-NAHOM | Arcane.S02.720p.ITA-ENG.MULTI.WEBRip.x265.AAC-V3SP4EV3R | Se cerco S02 E02 non lo trovo da nessuna parte, ma è presente in 2 file | Se cerco S02 E04 lo trova in un file, ma è presente in 2 file | Se cerco S02 trova 4 file ma è presente in 2 file | Decido di prendere sempe tutti i risultati e vedere se poi dopo è sufficiente filtrarli | se non ci sono risultati riprova omettendo l'episodio | perché ci sono i torrent con l'intera serie inclusa | bisogna poi cercare il file corretto
- L506: Recupera e inizializza tutti gli indexer configurati. Returns: ...
- L514: creiamo un dizionario con title come chiave
- L523: Istanzia gli oggetti SearchIndexer a partire dalla lista di motori. Args: ...
- L572: Converte una lista di dizionari grezzi in oggetti SearchResult. Args: ...
- L602: but NOW contain the web page or magnet, will be __post_process_results
- L611-620: Verifica se una stringa è un magnet link. Args: ... | Check if link inizia con "magnet:?
- L625-637: Estrae l'info hash da un magnet link. Args: ... | parse
- L640: extract 'xt
- L645: remove prefix "urn:btih:
- L653: Post-processa un risultato di ricerca, risolvendo i magnet link se necessario. Args: ...
- L674-675: raise Exception('Error, please fill a bug report!') | se non riesce a scarica il file ritorna None
- L679-683: parse RAW title to detect languages | result.languages = [languages.get(name=language).alpha2 for language in parsed_result.language] | TODO: replace with parsed_result.lang_codes when RTN is updated

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SEARCHE_FALL_BACK`|var|pub|43||
|`SearchService`|class|pub|45-244|class SearchService|
|`SearchService.__init__`|fn|priv|49-80|def __init__(self, config)|
|`SearchService.search`|fn|pub|81-148|async def search(self, media)|
|`SearchService.__get_engine`|fn|priv|149-180|def __get_engine(self, engine_name)|
|`SearchService.__get_requested_languages`|fn|priv|181-193|def __get_requested_languages(self)|
|`SearchService.__get_title_for_language`|fn|priv|194-220|def __get_title_for_language(self, media, lang)|
|`SearchService.__get_lang_tag`|fn|priv|221-240|def __get_lang_tag(self, indexer_language, lang)|
|`__build_query`|fn|priv|241-254|def __build_query(self, *parts)|
|`__build_query_keep_dash`|fn|priv|255-272|def __build_query_keep_dash(self, *parts)|
|`__search_torrents`|fn|priv|273-296|async def __search_torrents(self, media, indexer, search_...|
|`__log_query_result`|fn|priv|297-303|def __log_query_result(|
|`__search_movie_indexer`|fn|priv|328-403|async def __search_movie_indexer(self, movie, indexer)|
|`__search_series_indexer`|fn|priv|404-504|async def __search_series_indexer(self, series, indexer)|
|`__get_indexers`|fn|priv|505-521|def __get_indexers(self)|
|`__get_indexer_from_engines`|fn|priv|522-570|def __get_indexer_from_engines(self, engines)|
|`__get_torrents_from_list_of_dicts`|fn|priv|571-609|def __get_torrents_from_list_of_dicts(self, media, indexe...|
|`__is_magnet_link`|fn|priv|610-623|def __is_magnet_link(self, link)|
|`__extract_info_hash`|fn|priv|624-651|def __extract_info_hash(self, magnet_link)|
|`__post_process_result`|fn|priv|652-689|async def __post_process_result(self, indexers, result, m...|


---

# test_plugins.py | Python | 87L | 7 symbols | 13 imports | 8 comments
> Path: `src/debriddo/test_plugins.py`
> VERSION: 0.0.35

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

- var `SRC_DIR = Path(__file__).resolve().parents[1]` (L9) — Allow execution as a standalone script from any working directory.
### fn `def build_engines()` (L33-38)
L34> `return [`

- var `SEARCH_STRING = "The Fall Guy 2024 ITA"` (L39)
- var `SEARCH_TYPE = "movies"` (L40)
### fn `def __is_torrent(link: str) -> bool` `priv` (L42-45)
L43> Controlla se il link termina con ".torrent
L44> `return link.endswith(".torrent")`

### fn `def __is_magnet_link(link: str) -> bool` `priv` (L46-49)
L43> Controlla se il link termina con ".torrent
L47> Check if link inizia con "magnet:?
L48> `return link.startswith("magnet:?")`

### fn `async def main()` (L50-85)
L47> Check if link inizia con "magnet:?
L62> final results
L84> Plugin instances don't need explicit close

## Comments
- L2: AUTHORS: Ogekuri
- L19: from debriddo.search.plugins.torrentgalaxyto import torrentgalaxy
- L26: Dati del form di autenticazione
- L62: final results

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SRC_DIR`|var|pub|9||
|`build_engines`|fn|pub|33-38|def build_engines()|
|`SEARCH_STRING`|var|pub|39||
|`SEARCH_TYPE`|var|pub|40||
|`__is_torrent`|fn|priv|42-45|def __is_torrent(link: str) -> bool|
|`__is_magnet_link`|fn|priv|46-49|def __is_magnet_link(link: str) -> bool|
|`main`|fn|pub|50-85|async def main()|


---

# test_sviluppo_plugins.py | Python | 97L | 2 symbols | 6 imports | 28 comments
> Path: `src/debriddo/test_sviluppo_plugins.py`
> VERSION: 0.0.35

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

- var `SRC_DIR = Path(__file__).resolve().parents[1]` (L10)
### fn `async def main()` (L16-96)
L20> Variabili per l'autenticazione
L24> URL del form di login e dati richiesti
L28> Dati del form di autenticazione
L36> # Esegui il login
L37> try:
L38> response = session.post(login_url, data=data, headers=headers)
L39> print(response.url)  # URL generato da requests
L40> response.raise_for_status()  # Controlla errori HTTP
L41> # Verifica se il login è stato effettuato correttamente
L42> if "Benvenuto" in response.text or "Logout" in response.text:
L43> print("Login effettuato con successo!")
L44> login = True
L45> else:
L46> print("Errore nel login. Controlla username e password.")
L47> except requests.RequestException as e:
L48> print(f"Errore durante il tentativo di login: {e}")
L51> Variabili per la ricerca
L53> https://torrentgalaxy.one/get-posts/category:Movies:keywords:Wolfs%202024%20ITA
L54> https://torrentgalaxy.one/get-posts/category:TV:keywords:Arcane%20S01%20ITA
L55> https://torrentgalaxy.one/get-posts/category:Anime:keywords:Arcane%20S01%20ITA
L61> URL e parametri per la ricerca
L65> Esegui la ricerca
L68> Controlla errori HTTP
L73> Parsing della risposta HTML
L75> Trova la prima tabella
L78> Trova la prima tabella
L81> 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF
L82> - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf
L83> - /get-posts/keywords:tt14257582
L87> Divide per "/" e converte in interi

## Comments
- L2: AUTHORS: Ogekuri
- L20: Variabili per l'autenticazione
- L24: URL del form di login e dati richiesti
- L28: Dati del form di autenticazione
- L36-48: # Esegui il login | try: | response = session.post(login_url, data=data, headers=headers) | print(response.url)  # URL generato da requests | response.raise_for_status()  # Controlla errori HTTP | # Verifica se il login è stato effettuato correttamente | if "Benvenuto" in response.text or "Logout" in response.text: | print("Login effettuato con successo!") | login = True | else: | print("Errore nel login. Controlla username e password.") | except requests.RequestException as e: | print(f"Errore durante il tentativo di login: {e}")
- L51-55: Variabili per la ricerca | https://torrentgalaxy.one/get-posts/category:Movies:keywords:Wolfs%202024%20ITA | https://torrentgalaxy.one/get-posts/category:TV:keywords:Arcane%20S01%20ITA | https://torrentgalaxy.one/get-posts/category:Anime:keywords:Arcane%20S01%20ITA
- L61: URL e parametri per la ricerca
- L65: Esegui la ricerca
- L73: Parsing della risposta HTML
- L81-83: 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF | - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf | - /get-posts/keywords:tt14257582

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SRC_DIR`|var|pub|10||
|`main`|fn|pub|16-96|async def main()|


---

# torrent_item.py | Python | 50L | 3 symbols | 5 imports | 3 comments
> Path: `src/debriddo/torrent/torrent_item.py`
> VERSION: 0.0.35

## Imports
```
from urllib.parse import quote
from typing import Any
from debriddo.models.media import Media
from debriddo.models.series import Series
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TorrentItem` (L13-50)
- fn `def __init__(self, raw_title, title, size, magnet, info_hash, link, seeders, languages, indexer,` `priv` (L14-41)
  L18> Raw title of the torrent
  L19> Title of the torrent
  L20> Size of the video file inside the torrent - it may be updated during __process_torrent()
  L21> Magnet to torrent
  L22> Hash of the torrent
  L23> Link to download torrent file or magnet link
  L24> The number of seeders
  L25> Language of the torrent
  L26> Indexer of the torrent (ilCorSaRoNeRo)
  L27> Engine name of the torrent (ilcorsaronero)
  L28> public or private (determina se sarà o meno salvato in cache)
  L29> series" or "movie
  L30> by default is not from cache
  L32> it may be updated during __process_torrent()
  L33> The files inside of the torrent. If it's None, it means that there is only one file inside of the torrent
  L34> The torrent download url if its None, it means that there is only a magnet link provided by Jackett. It also means, that we cant do series file filtering before debrid.
  L35> Trackers of the torrent
  L36> Index of the file inside of the torrent - it may be updated durring __process_torrent() and update_availability(). If the index is None and torrent is not None, it means that the series episode is not inside of the torrent.
  L37> If it's instantly available on the debrid service
  L40> Ranked result
- fn `def to_debrid_stream_query(self, media: Media) -> dict` (L42-50)
  L43> `return {`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentItem`|class|pub|13-50|class TorrentItem|
|`TorrentItem.__init__`|fn|priv|14-41|def __init__(self, raw_title, title, size, magnet, info_h...|
|`TorrentItem.to_debrid_stream_query`|fn|pub|42-50|def to_debrid_stream_query(self, media: Media) -> dict|


---

# torrent_service.py | Python | 341L | 13 symbols | 14 imports | 42 comments
> Path: `src/debriddo/torrent/torrent_service.py`
> VERSION: 0.0.35

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

### class `class TorrentService` (L23-222)
L33> # versione originale multi-thread
L34> async def convert_and_process(self, results: List[SearchResult]):
L36> threads = []
L37> torrent_items_queue = queue.Queue()
L38> def thread_target(result: SearchResult):
L39> torrent_item = result.convert_to_torrent_item()
L40> if torrent_item.link.startswith("magnet:"):
L41> processed_torrent_item = self.__process_magnet(torrent_item)
L42> else:
L43> processed_torrent_item = self.__process_web_url(torrent_item)
L44> torrent_items_queue.put(processed_torrent_item)
L45> for result in results:
L46> threads.append(threading.Thread(target=thread_target, args=(result,)))
L47> for thread in threads:
L48> thread.start()
L49> for thread in threads:
L50> thread.join()
L51> torrent_items_result = []
L52> while not torrent_items_queue.empty():
L53> torrent_items_result.append(torrent_items_queue.get())
L212-222> Costruisce una stringa magnet link. Args: hash (str): Info hash. display_name (str): Nome visualizzato. trackers (list): Lista dei tracker. Returns: str: Il magnet link.
- fn `def __init__(self)` `priv` (L27-32) L24> Servizio per la gestione e il processing dei file torrent.
  L28-30> Inizializza il servizio TorrentService.
- fn `async def __process_web_url_or_process_magnet(self, result: SearchResult)` `priv` (L57-78) L54> return torrent_items_result
  L58-66> Processa un risultato determinando se è un link web o magnet. Args: result (SearchResult): Il risultato della ricerca. Returns: TorrentItem: L'item processato o None.
  L71> `return None`
  L74> `return self.__process_magnet(torrent_item)`
  L76> `return await self.__process_web_url(torrent_item)`
- fn `async def convert_and_process(self, results: List[SearchResult])` (L79-100)
  L80-88> Converte e processa una lista di risultati di ricerca. Args: results (List[SearchResult]): Lista dei risultati. Returns: list: Lista di TorrentItem processati.
  L98> `return torrent_items_result`
- fn `async def __process_web_url(self, result: TorrentItem)` `priv` (L101-135)
  L102-110> Scarica e processa un file torrent da un URL web. Args: result (TorrentItem): L'item del torrent. Returns: TorrentItem: L'item aggiornato o None.
  L113> `return None`
  L114> TODO: is the timeout enough?
  L115> Usa il client asincrono
  L116> response = await session.request_get(result.link, allow_redirects=False, timeout=2)
  L121> `return self.__process_torrent(result, response.content)`
  L124> `return self.__process_magnet(result)`
  L128> `return result`
  L133> `return None`
- fn `def __process_torrent(self, result: TorrentItem, torrent_file)` `priv` (L136-176)
  L137-146> Estrae i metadati dal contenuto binario di un file torrent. Args: result (TorrentItem): L'item del torrent. torrent_file (bytes): Il contenuto del file. Returns: TorrentItem: L'item aggiornato con i metadati.
  L156> `return result`
  L175> `return result`
- fn `def __process_magnet(self, result: TorrentItem)` `priv` (L177-196)
  L178-186> Processa un magnet link estraendo info hash e tracker. Args: result (TorrentItem): L'item del torrent. Returns: TorrentItem: L'item aggiornato.
  L195> `return result`
- fn `def __convert_torrent_to_hash(self, torrent_contents)` `priv` (L197-210)
  L198-206> Calcola l'info hash SHA1 del contenuto del torrent. Args: torrent_contents (dict): Contenuto del dizionario 'info'. Returns: str: L'hash esadecimale.
  L209> `return hexHash.lower()`

### fn `def __build_magnet(self, hash, display_name, trackers)` `priv` (L211-230)
L212-222> Costruisce una stringa magnet link. Args: hash (str): Info hash. display_name (str): Nome visualizzato. trackers (list): Lista dei tracker. Returns: str: Il magnet link.
L229> `return magnet`

### fn `def __get_trackers_from_torrent(self, torrent_metadata)` `priv` (L231-261)
L232-240> Estrae la lista dei tracker dai metadati del torrent. Args: torrent_metadata (dict): I metadati del torrent. Returns: list: Lista dei tracker.
L241> Sometimes list, sometimes string
L243> Sometimes 2D array, sometimes 1D array
L260> `return list(trackers)`

### fn `def __get_trackers_from_magnet(self, magnet: str)` `priv` (L262-280)
L263-271> Estrae la lista dei tracker da un magnet link. Args: magnet (str): Il magnet link. Returns: list: Lista dei tracker.
L279> `return trackers`

### fn `def __find_episode_file(self, file_structure, season, episode)` `priv` (L281-321)
L282-292> Trova il file corrispondente a un episodio specifico nella struttura dei file. Args: file_structure (list): Lista dei file nel torrent. season (list): Stagione cercata. episode (list): Episodio cercato. Returns: dict: Dettagli del file trovato o None.
L297> `return None`
L314> Doesn't that need to be indented?
L318> `return None`
L320> `return max(episode_files, key=lambda file: file["size"])`

### fn `def __find_movie_file(self, file_structure)` `priv` (L322-341)
L323-331> Trova il file principale (film) basandosi sulla dimensione. Args: file_structure (list): Lista dei file nel torrent. Returns: int: Indice del file più grande.
L341> `return max_file_index`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L28: Inizializza il servizio TorrentService.
- L33-53: # versione originale multi-thread | async def convert_and_process(self, results: List[SearchResult]): | threads = [] | torrent_items_queue = queue.Queue() | def thread_target(result: SearchResult): | torrent_item = result.convert_to_torrent_item() | if torrent_item.link.startswith("magnet:"): | processed_torrent_item = self.__process_magnet(torrent_item) | else: | processed_torrent_item = self.__process_web_url(torrent_item) | torrent_items_queue.put(processed_torrent_item) | for result in results: | threads.append(threading.Thread(target=thread_target, args=(result,))) | for thread in threads: | thread.start() | for thread in threads: | thread.join() | torrent_items_result = [] | while not torrent_items_queue.empty(): | torrent_items_result.append(torrent_items_queue.get())
- L58: Processa un risultato determinando se è un link web o magnet. Args: ...
- L80: Converte e processa una lista di risultati di ricerca. Args: ...
- L102: Scarica e processa un file torrent da un URL web. Args: ...
- L114-116: TODO: is the timeout enough? | response = await session.request_get(result.link, allow_redirects=False, timeout=2)
- L137: Estrae i metadati dal contenuto binario di un file torrent. Args: ...
- L178: Processa un magnet link estraendo info hash e tracker. Args: ...
- L198: Calcola l'info hash SHA1 del contenuto del torrent. Args: ...
- L212: Costruisce una stringa magnet link. Args: ...
- L232-243: Estrae la lista dei tracker dai metadati del torrent. Args: ... | Sometimes list, sometimes string | Sometimes 2D array, sometimes 1D array
- L263: Estrae la lista dei tracker da un magnet link. Args: ...
- L282: Trova il file corrispondente a un episodio specifico nella struttura dei file. Args: ...
- L314: Doesn't that need to be indented?
- L323: Trova il file principale (film) basandosi sulla dimensione. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentService`|class|pub|23-222|class TorrentService|
|`TorrentService.__init__`|fn|priv|27-32|def __init__(self)|
|`TorrentService.__process_web_url_or_process_magnet`|fn|priv|57-78|async def __process_web_url_or_process_magnet(self, resul...|
|`TorrentService.convert_and_process`|fn|pub|79-100|async def convert_and_process(self, results: List[SearchR...|
|`TorrentService.__process_web_url`|fn|priv|101-135|async def __process_web_url(self, result: TorrentItem)|
|`TorrentService.__process_torrent`|fn|priv|136-176|def __process_torrent(self, result: TorrentItem, torrent_...|
|`TorrentService.__process_magnet`|fn|priv|177-196|def __process_magnet(self, result: TorrentItem)|
|`TorrentService.__convert_torrent_to_hash`|fn|priv|197-210|def __convert_torrent_to_hash(self, torrent_contents)|
|`__build_magnet`|fn|priv|211-230|def __build_magnet(self, hash, display_name, trackers)|
|`__get_trackers_from_torrent`|fn|priv|231-261|def __get_trackers_from_torrent(self, torrent_metadata)|
|`__get_trackers_from_magnet`|fn|priv|262-280|def __get_trackers_from_magnet(self, magnet: str)|
|`__find_episode_file`|fn|priv|281-321|def __find_episode_file(self, file_structure, season, epi...|
|`__find_movie_file`|fn|priv|322-341|def __find_movie_file(self, file_structure)|


---

# torrent_smart_container.py | Python | 232L | 16 symbols | 9 imports | 9 comments
> Path: `src/debriddo/torrent/torrent_smart_container.py`
> VERSION: 0.0.35

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

### class `class TorrentSmartContainer` (L20-219)
L186> Simple recursion to traverse the file structure returned by AllDebrid
- fn `def __init__(self, torrent_items: List[TorrentItem], media)` `priv` (L21-25)
- fn `def get_hashes(self)` (L26-28)
  L27> `return list(self.__itemsDict.keys())`
- fn `def get_items(self)` (L29-31)
  L30> `return list(self.__itemsDict.values())`
- fn `def get_direct_torrentable(self)` (L32-38)
  L37> `return direct_torrentable_items`
- fn `def get_best_matching(self)` (L39-56)
  L46> Torrent download
  L49> If the season/episode is present inside the torrent filestructure (movies always have a
  L50> file_index)
  L52> Magnet
  L53> If it's a movie with a magnet link
  L55> `return best_matching`
- fn `def cache_container_items(self)` (L57-63)
  L58> threading.Thread(target=self.__save_to_cache).start()
  L59> la versione originale esegue l'upload dei risultati quindi
  L60> gira in un tread separato, ma per sqllite non serve
- fn `def __save_to_cache(self)` `priv` (L64-67)
- fn `def update_availability(self, debrid_response, debrid_type, media)` (L68-79)
  L78> `raise NotImplemented`
- fn `def __update_availability_realdebrid(self, response, media)` `priv` (L80-117)
- fn `def __update_availability_alldebrid(self, response, media)` `priv` (L118-134)
  L121> `return`
- fn `def __update_availability_torbox(self, response, media)` `priv` (L135-153)
- fn `def __update_availability_premiumize(self, response)` `priv` (L154-164)
  L157> `return`
- fn `def __update_file_details(self, torrent_item, files)` `priv` (L165-174)
  L167> `return`
- fn `def __build_items_dict_by_infohash(self, items: List[TorrentItem])` `priv` (L175-185)
  L184> `return items_dict`

### fn `def __explore_folders(self, folder, files, file_index, type, season=None, episode=None)` `priv` (L187-232)
L186> Simple recursion to traverse the file structure returned by AllDebrid
L232> `return file_index`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L49-50: If the season/episode is present inside the torrent filestructure (movies always have a | file_index)
- L58-60: threading.Thread(target=self.__save_to_cache).start() | la versione originale esegue l'upload dei risultati quindi | gira in un tread separato, ma per sqllite non serve

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentSmartContainer`|class|pub|20-219|class TorrentSmartContainer|
|`TorrentSmartContainer.__init__`|fn|priv|21-25|def __init__(self, torrent_items: List[TorrentItem], media)|
|`TorrentSmartContainer.get_hashes`|fn|pub|26-28|def get_hashes(self)|
|`TorrentSmartContainer.get_items`|fn|pub|29-31|def get_items(self)|
|`TorrentSmartContainer.get_direct_torrentable`|fn|pub|32-38|def get_direct_torrentable(self)|
|`TorrentSmartContainer.get_best_matching`|fn|pub|39-56|def get_best_matching(self)|
|`TorrentSmartContainer.cache_container_items`|fn|pub|57-63|def cache_container_items(self)|
|`TorrentSmartContainer.__save_to_cache`|fn|priv|64-67|def __save_to_cache(self)|
|`TorrentSmartContainer.update_availability`|fn|pub|68-79|def update_availability(self, debrid_response, debrid_typ...|
|`TorrentSmartContainer.__update_availability_realdebrid`|fn|priv|80-117|def __update_availability_realdebrid(self, response, media)|
|`TorrentSmartContainer.__update_availability_alldebrid`|fn|priv|118-134|def __update_availability_alldebrid(self, response, media)|
|`TorrentSmartContainer.__update_availability_torbox`|fn|priv|135-153|def __update_availability_torbox(self, response, media)|
|`TorrentSmartContainer.__update_availability_premiumize`|fn|priv|154-164|def __update_availability_premiumize(self, response)|
|`TorrentSmartContainer.__update_file_details`|fn|priv|165-174|def __update_file_details(self, torrent_item, files)|
|`TorrentSmartContainer.__build_items_dict_by_infohash`|fn|priv|175-185|def __build_items_dict_by_infohash(self, items: List[Torr...|
|`__explore_folders`|fn|priv|187-232|def __explore_folders(self, folder, files, file_index, ty...|


---

# async_httpx_session.py | Python | 391L | 17 symbols | 11 imports | 96 comments
> Path: `src/debriddo/utils/async_httpx_session.py`
> VERSION: 0.0.35

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

- var `DEFAULT_TIMEOUT = 20.0  # 20 secondi` (L16)
### class `class AsyncThreadSafeSession` (L18-217)
L19-21> Gestisce sessioni HTTP asincrone thread-safe con supporto per HTTP/2, proxy e cookie.
L208> versione originale sincrona
L210> def retrieve_url(url):
L211> Return the content of the url page as a string
L212> try:
L213> req = urllib.request.Request(url, headers=headers)
L214> response = urllib.request.urlopen(req)
L215> except urllib.error.URLError as errno:
L216> logger.error(" ".join(("Connection error:", str(errno.reason))))
L217> return
- fn `def __init__(self, proxy=None)` `priv` (L30-49)
  L31-36> Inizializza la sessione HTTP. Args: proxy (str, optional): Proxy in formato user:pass@host:port. Defaults to None.
  L37> Gestione esplicita dei cookie
  L38> Associa i cookie al client, abilita i reindirizzamenti
  L39> self._lock = asyncio.Lock()  # Usa un lock asincrono
  L40> Timeout predefinito di 20 secondi
  L42> SOCKS5 Proxy setup (if provided)
  L46> per il check dei close
- fn `async def close(self)` (L50-59)
  L51-56> Chiude il client HTTPX e rilascia le risorse. Returns: None
- fn `async def __aenter__(self)` `priv` (L60-68)
  L61-66> Inizia il contesto asincrono. Returns: AsyncThreadSafeSession: L'istanza della sessione.
  L67> `return self`
- fn `async def __aexit__(self, exc_type, exc_val, exc_tb)` `priv` (L69-79) L61> Inizia il contesto asincrono. Returns: ...
  L70-77> Chiude la sessione quando il contesto termina. Args: exc_type: Tipo dell'eccezione. exc_val: Valore dell'eccezione. exc_tb: Traceback dell'eccezione.
- fn `def __del__(self)` `priv` (L80-87) L70> Chiude la sessione quando il contesto termina. Args: ...
  L81-83> Verifica se la sessione è stata chiusa correttamente.
  L85> Logga un avviso, senza tentare di chiudere la sessione
- fn `def _html_entity_decode(s)` `priv` (L91-116) L88> per Debrid
  L92-100> Decodifica le entità HTML in una stringa. Args: s (str): La stringa da decodificare. Returns: str: La stringa decodificata.
  L101> First convert alpha entities (such as &eacute;)
  L102> (Inspired from http://mail.python.org/pipermail/python-list/2007-June/443813.html)
  L106> `return chr(html.entities.name2codepoint[entity])`
  L107> `return " "` — Unknown entity: We replace with a space.
  L110> Then convert numerical entities (such as &#233;)
  L113> Then convert hexa entities (such as &#x00E9;)
  L114> `return re.sub(r'&#x(\w+);', lambda x: chr(int(x.group(1), 16)), t)`
- fn `def entity2char(m)` (L103-107) L92> Decodifica le entità HTML in una stringa. Args: ...
  L106> `return chr(html.entities.name2codepoint[entity])`
  L107> `return " "` — Unknown entity: We replace with a space.
- fn `def _setup_proxy(self, proxy)` `priv` (L117-141)
  L118-126> Configura il proxy SOCKS5. Args: proxy (str): Stringa proxy formattata. Raises: ValueError: Se il formato del proxy non è valido.
  L139> `raise ValueError("Invalid proxy format. Expected format: user:pass@host:port or host:port")`
- fn `async def request(self, method, url, **kwargs)` (L144-179) L142> per i Plug-Ins
  L145-155> Esegue una richiesta HTTP. Args: method (str): Metodo HTTP (GET, POST, etc.). url (str): URL di destinazione. kwargs: Argomenti aggiuntivi per httpx.request. Returns: httpx.Response: La risposta HTTP o None in caso di errore.
  L156> async with self._lock:
  L158> Combina gli header specificati con quelli di default
  L160> Unisce gli header di default e quelli personalizzati
  L162> Usa un timeout personalizzato o quello predefinito
  L168> Solleva un'eccezione per errori HTTP 4xx o 5xx
  L169> `return response` — Restituisce la risposta finale dopo i reindirizzamenti
  L171> Logga l'errore e restituisce una risposta informativa
  L173> `return None`
  L175> Logga l'errore e genera un'eccezione per errori di connessione o altro
  L177> `return None`
- fn `async def request_get(self, url, **kwargs)` (L180-193)
  L181-190> Esegue una richiesta GET. Args: url (str): URL di destinazione. kwargs: Argomenti aggiuntivi. Returns: httpx.Response: La risposta HTTP o None.
  L191> `return await self.request("GET", url, headers=self.headers, **kwargs)`
- fn `async def request_post(self, url, **kwargs)` (L194-206)
  L195-204> Esegue una richiesta POST. Args: url (str): URL di destinazione. kwargs: Argomenti aggiuntivi. Returns: httpx.Response: La risposta HTTP o None.
  L205> `return await self.request("POST", url, headers=self.headers, **kwargs)`

### fn `async def retrieve_url(self, url)` (L237-264)
L234> # return dat.encode('utf-8', 'replace')
L238-246> Recupera il contenuto dell'URL come stringa decodificata. Args: url (str): L'URL da recuperare. Returns: str: Il contenuto decodificato o None.
L252> Handle gzip encoding
L256> Decode the content
L259> `return self._html_entity_decode(decoded_data)`
L263> `return None`

### fn `async def download_file(self, url, referer=None)` (L292-327)
L289> # return file path
L293-302> Scarica un file da un URL e lo salva in un file temporaneo. Args: url (str): URL del file. referer (str, optional): Header referer. Defaults to None. Returns: str: Il percorso del file temporaneo salvato o None.
L313> Handle gzip encoding
L317> Write to a temporary file
L322> `return file_path`
L326> `return None`

### fn `async def get_json_response(self, url, **kwargs)` (L330-378)
L328> per la classe base di Debrid
L331-340> Esegue una richiesta e restituisce il corpo JSON. Args: url (str): URL della richiesta. kwargs: Argomenti aggiuntivi (headers, timeout, method). Returns: dict: Il JSON decodificato o None.
L342> Prende method
L343> per default usa GET
L345> Combina gli header specificati con quelli di default
L347> Unisce gli header di default e quelli personalizzati
L349> Usa un timeout personalizzato o quello predefinito
L357> Solleva un'eccezione per errori HTTP 4xx o 5xx
L360> `return response.json()` — Restituisce la risposta finale dopo i reindirizzamenti
L363> `return None`
L367> `return None`
L369> Logga l'errore e restituisce una risposta informativa
L371> `return None`
L373> Logga l'errore e genera un'eccezione per errori di connessione o altro
L375> `return None`
L377> `return None`

### fn `async def download_torrent_file(self, download_url)` (L379-391)
L380-388> Scarica un file torrent in streaming. Args: download_url (str): L'URL del file torrent. Returns: bytes: Il contenuto binario del file torrent.
L391> `return await response.aread()`

## Comments
- L2: AUTHORS: Ogekuri
- L19: Gestisce sessioni HTTP asincrone thread-safe con supporto per HTTP/2, proxy e cookie.
- L31: Inizializza la sessione HTTP. Args: ...
- L39: self._lock = asyncio.Lock()  # Usa un lock asincrono
- L42: SOCKS5 Proxy setup (if provided)
- L46: per il check dei close
- L51: Chiude il client HTTPX e rilascia le risorse. Returns: ...
- L81-85: Verifica se la sessione è stata chiusa correttamente. | Logga un avviso, senza tentare di chiudere la sessione
- L110: Then convert numerical entities (such as &#233;)
- L113: Then convert hexa entities (such as &#x00E9;)
- L118: Configura il proxy SOCKS5. Args: ...
- L145-158: Esegue una richiesta HTTP. Args: ... | async with self._lock: | Combina gli header specificati con quelli di default
- L162: Usa un timeout personalizzato o quello predefinito
- L171: Logga l'errore e restituisce una risposta informativa
- L175: Logga l'errore e genera un'eccezione per errori di connessione o altro
- L181: Esegue una richiesta GET. Args: ...
- L195: Esegue una richiesta POST. Args: ...
- L207-233: versione originale sincrona | def retrieve_url(url): | Return the content of the url page as a string | try: | req = urllib.request.Request(url, headers=headers) | response = urllib.request.urlopen(req) | except urllib.error.URLError as errno: | logger.error(" ".join(("Connection error:", str(errno.reason)))) | return | dat = response.read() | # Check if it is gzipped | if dat[:2] == b'\x1f\x8b': | # Data is gzip encoded, decode it | compressedstream = io.BytesIO(dat) | gzipper = gzip.GzipFile(fileobj=compressedstream) | extracted_data = gzipper.read() | dat = extracted_data | info = response.info() | charset = 'utf-8 | try: | ignore, charset = info['Content-Type'].split('charset=') | except Exception: | pass | dat = dat.decode(charset, 'replace') | dat = htmlentitydecode(dat)
- L238: Recupera il contenuto dell'URL come stringa decodificata. Args: ...
- L252: Handle gzip encoding
- L256: Decode the content
- L265-288: versione originale sincrona | def download_file(url, referer=None): | Download file at url and write it to a file, return the path to the file and the url | file, path = tempfile.mkstemp() | file = os.fdopen(file, "wb") | # Download url | req = urllib.request.Request(url, headers=headers) | if referer is not None: | req.add_header('referer', referer) | response = urllib.request.urlopen(req) | dat = response.read() | # Check if it is gzipped | if dat[:2] == b'\x1f\x8b': | # Data is gzip encoded, decode it | compressedstream = io.BytesIO(dat) | gzipper = gzip.GzipFile(fileobj=compressedstream) | extracted_data = gzipper.read() | dat = extracted_data | # Write it to a file | file.write(dat) | file.close()
- L293: Scarica un file da un URL e lo salva in un file temporaneo. Args: ...
- L313: Handle gzip encoding
- L317: Write to a temporary file
- L331-342: Esegue una richiesta e restituisce il corpo JSON. Args: ... | Prende method
- L345: Combina gli header specificati con quelli di default
- L349: Usa un timeout personalizzato o quello predefinito
- L369: Logga l'errore e restituisce una risposta informativa
- L373: Logga l'errore e genera un'eccezione per errori di connessione o altro
- L380: Scarica un file torrent in streaming. Args: ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`DEFAULT_TIMEOUT`|var|pub|16||
|`AsyncThreadSafeSession`|class|pub|18-217|class AsyncThreadSafeSession|
|`AsyncThreadSafeSession.__init__`|fn|priv|30-49|def __init__(self, proxy=None)|
|`AsyncThreadSafeSession.close`|fn|pub|50-59|async def close(self)|
|`AsyncThreadSafeSession.__aenter__`|fn|priv|60-68|async def __aenter__(self)|
|`AsyncThreadSafeSession.__aexit__`|fn|priv|69-79|async def __aexit__(self, exc_type, exc_val, exc_tb)|
|`AsyncThreadSafeSession.__del__`|fn|priv|80-87|def __del__(self)|
|`AsyncThreadSafeSession._html_entity_decode`|fn|priv|91-116|def _html_entity_decode(s)|
|`AsyncThreadSafeSession.entity2char`|fn|pub|103-107|def entity2char(m)|
|`AsyncThreadSafeSession._setup_proxy`|fn|priv|117-141|def _setup_proxy(self, proxy)|
|`AsyncThreadSafeSession.request`|fn|pub|144-179|async def request(self, method, url, **kwargs)|
|`AsyncThreadSafeSession.request_get`|fn|pub|180-193|async def request_get(self, url, **kwargs)|
|`AsyncThreadSafeSession.request_post`|fn|pub|194-206|async def request_post(self, url, **kwargs)|
|`retrieve_url`|fn|pub|237-264|async def retrieve_url(self, url)|
|`download_file`|fn|pub|292-327|async def download_file(self, url, referer=None)|
|`get_json_response`|fn|pub|330-378|async def get_json_response(self, url, **kwargs)|
|`download_torrent_file`|fn|pub|379-391|async def download_torrent_file(self, download_url)|


---

# cache.py | Python | 330L | 3 symbols | 8 imports | 29 comments
> Path: `src/debriddo/utils/cache.py`
> VERSION: 0.0.35

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

- var `TABLE_NAME = "cached_items"` (L13)
### fn `def search_cache(config, media)` (L53-159)
L54-63> Cerca risultati nella cache SQLite per il media specificato. Args: config (dict): La configurazione dell'applicazione. media (Media): L'oggetto media da cercare. Returns: list: Lista di risultati trovati in cache o None.
L68> Verifica se la tabella esiste
L69> cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
L72> `return None`
L77> cursor.execute(f"""DELETE FROM '{TABLE_NAME}' WHERE created_at < datetime('now', '-{days} days');""")
L86> cicla sulle lingue
L119> Costruisci la query di filtro in base a `cache_search`
L125> Genera la query dinamica
L128> Esegui la query con i parametri
L132> Recupera i nomi delle colonne
L136> Trasforma ogni riga in un dizionario
L139> strighe di lista in lista
L154> `return cache_items`
L156> `return None`
L157> `return None`

### fn `def cache_results(torrents: List[TorrentItem], media)` (L160-330)
L161-170> Salva i risultati torrent nella cache SQLite. Args: torrents (List[TorrentItem]): Lista di item da cachare. media (Media): L'oggetto media associato. Returns: None
L174> Verifica se il file esiste (opzionale, SQLite lo crea comunque)
L177> Connetti al database (crea il file se non esiste)
L184> Verifica se la tabella esiste, altrimenti la crea
L185> cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
L195> crea dizionario dei titoli
L198> elenco delle entry da aggiungere
L204> Esegui una query per verificare l'esistenza dell'hash
L208> Restituisci True se il risultato non è None
L216> cicla sulle lingue
L241> clean_episode = int(media.episode.replace("E", ""))
L246> parsed_result = parse(result.raw_title) - già popolato
L258> True = contiene la stagione intera
L262> True = contiene la stagione intera
L266> False = contiene un episodio
L270> False = contiene un episodio
L274> prepara i dati per l'inserimento
L281> lista
L290> lista
L298> lista
L301> lista
L304> bool
L315> Estrai dinamicamente le colonne dalla lista di dizionari
L318> Placeholder per ogni colonna
L322> cursor.execute(f"""INSERT INTO {TABLE_NAME} ({", ".join(columns)}) VALUES ({placeholders}) """, data)

## Comments
- L2: AUTHORS: Ogekuri
- L15: TABLE_SCHEMA = CREATE TABLE IF NOT EXISTS cached_items ( id INTEGER PRIMARY KEY AUTOINCREMENT, created_at TIMESTAMP, ...
- L54: Cerca risultati nella cache SQLite per il media specificato. Args: ...
- L68-69: Verifica se la tabella esiste | cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
- L77: cursor.execute(f"""DELETE FROM '{TABLE_NAME}' WHERE created_at < datetime('now', '-{days} days');""")
- L86: cicla sulle lingue
- L119: Costruisci la query di filtro in base a `cache_search`
- L125: Genera la query dinamica
- L128: Esegui la query con i parametri
- L132: Recupera i nomi delle colonne
- L136: Trasforma ogni riga in un dizionario
- L139: strighe di lista in lista
- L161: Salva i risultati torrent nella cache SQLite. Args: ...
- L174: Verifica se il file esiste (opzionale, SQLite lo crea comunque)
- L177: Connetti al database (crea il file se non esiste)
- L184-185: Verifica se la tabella esiste, altrimenti la crea | cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
- L195: crea dizionario dei titoli
- L198: elenco delle entry da aggiungere
- L204: Esegui una query per verificare l'esistenza dell'hash
- L208: Restituisci True se il risultato non è None
- L216: cicla sulle lingue
- L241: clean_episode = int(media.episode.replace("E", ""))
- L246: parsed_result = parse(result.raw_title) - già popolato
- L274: prepara i dati per l'inserimento
- L315: Estrai dinamicamente le colonne dalla lista di dizionari
- L322: cursor.execute(f"""INSERT INTO {TABLE_NAME} ({", ".join(columns)}) VALUES ({placeholders}) """, data)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TABLE_NAME`|var|pub|13||
|`search_cache`|fn|pub|53-159|def search_cache(config, media)|
|`cache_results`|fn|pub|160-330|def cache_results(torrents: List[TorrentItem], media)|


---

# detection.py | Python | 31L | 1 symbols | 1 imports | 3 comments
> Path: `src/debriddo/utils/detection.py`
> VERSION: 0.0.35

## Imports
```
import re
```

## Definitions

### fn `def detect_languages(torrent_name)` (L7-31)
L29> `return ["en"]`
L31> `return languages`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`detect_languages`|fn|pub|7-31|def detect_languages(torrent_name)|


---

# base_filter.py | Python | 19L | 5 symbols | 0 imports | 3 comments
> Path: `src/debriddo/utils/filter/base_filter.py`
> VERSION: 0.0.35

## Definitions

### class `class BaseFilter` (L5-19)
L2> AUTHORS: aymene69
- fn `def __init__(self, config, additional_config=None)` `priv` (L6-9)
- fn `def filter(self, data)` (L10-12)
  L11> `raise NotImplementedError`
- fn `def can_filter(self)` (L13-15)
  L14> `raise NotImplementedError`
- fn `def __call__(self, data)` `priv` (L16-19)
  L18> `return self.filter(data)`
  L19> `return data`

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BaseFilter`|class|pub|5-19|class BaseFilter|
|`BaseFilter.__init__`|fn|priv|6-9|def __init__(self, config, additional_config=None)|
|`BaseFilter.filter`|fn|pub|10-12|def filter(self, data)|
|`BaseFilter.can_filter`|fn|pub|13-15|def can_filter(self)|
|`BaseFilter.__call__`|fn|priv|16-19|def __call__(self, data)|


---

# language_filter.py | Python | 31L | 4 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/filter/language_filter.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class LanguageFilter(BaseFilter)` : BaseFilter (L11-31)
- fn `def __init__(self, config)` `priv` (L12-14)
- fn `def filter(self, data)` (L15-29)
  L28> `return filtered_data`
- fn `def can_filter(self)` (L30-31)
  L31> `return bool(self.config.get('languages'))`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`LanguageFilter`|class|pub|11-31|class LanguageFilter(BaseFilter)|
|`LanguageFilter.__init__`|fn|priv|12-14|def __init__(self, config)|
|`LanguageFilter.filter`|fn|pub|15-29|def filter(self, data)|
|`LanguageFilter.can_filter`|fn|pub|30-31|def can_filter(self)|


---

# max_size_filter.py | Python | 23L | 4 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/filter/max_size_filter.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class MaxSizeFilter(BaseFilter)` : BaseFilter (L11-23)
- fn `def __init__(self, config, additional_config=None)` `priv` (L12-14)
- fn `def filter(self, data)` (L15-21)
  L20> `return filtered_data`
- fn `def can_filter(self)` (L22-23)
  L23> `return int(self.config['maxSize']) > 0 and self.item_type == 'movie'`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MaxSizeFilter`|class|pub|11-23|class MaxSizeFilter(BaseFilter)|
|`MaxSizeFilter.__init__`|fn|priv|12-14|def __init__(self, config, additional_config=None)|
|`MaxSizeFilter.filter`|fn|pub|15-21|def filter(self, data)|
|`MaxSizeFilter.can_filter`|fn|pub|22-23|def can_filter(self)|


---

# quality_exclusion_filter.py | Python | 39L | 6 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/filter/quality_exclusion_filter.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class QualityExclusionFilter(BaseFilter)` : BaseFilter (L11-39)
- fn `def __init__(self, config)` `priv` (L12-14)
- var `RIPS = ["HDRIP", "BRRIP", "BDRIP", "WEBRIP", "TVRIP", "VODRIP", "HDRIP"]` (L15)
- var `CAMS = ["CAM", "TS", "TC", "R5", "DVDSCR", "HDTV", "PDTV", "DSR", "WORKPRINT", "VHSRIP", "HDCAM"]` (L16)
- fn `def filter(self, data)` (L18-37)
  L36> `return filtered_items`
- fn `def can_filter(self)` (L38-39)
  L39> `return self.config['exclusion'] is not None and len(self.config['exclusion']) > 0`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`QualityExclusionFilter`|class|pub|11-39|class QualityExclusionFilter(BaseFilter)|
|`QualityExclusionFilter.__init__`|fn|priv|12-14|def __init__(self, config)|
|`QualityExclusionFilter.RIPS`|var|pub|15||
|`QualityExclusionFilter.CAMS`|var|pub|16||
|`QualityExclusionFilter.filter`|fn|pub|18-37|def filter(self, data)|
|`QualityExclusionFilter.can_filter`|fn|pub|38-39|def can_filter(self)|


---

# results_per_quality_filter.py | Python | 32L | 4 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/filter/results_per_quality_filter.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class ResultsPerQualityFilter(BaseFilter)` : BaseFilter (L11-32)
- fn `def __init__(self, config)` `priv` (L12-14)
- fn `def filter(self, data)` (L15-30)
  L29> `return filtered_items`
- fn `def can_filter(self)` (L31-32)
  L32> `return self.config['resultsPerQuality'] is not None and int(self.config['resultsPerQuality']) > 0`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ResultsPerQualityFilter`|class|pub|11-32|class ResultsPerQualityFilter(BaseFilter)|
|`ResultsPerQualityFilter.__init__`|fn|priv|12-14|def __init__(self, config)|
|`ResultsPerQualityFilter.filter`|fn|pub|15-30|def filter(self, data)|
|`ResultsPerQualityFilter.can_filter`|fn|pub|31-32|def can_filter(self)|


---

# filter_results.py | Python | 388L | 10 symbols | 9 imports | 61 comments
> Path: `src/debriddo/utils/filter_results.py`
> VERSION: 0.0.35

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

### fn `def _match_complete_season(raw_title, numeric_season)` `priv` (L50-92)
L53> Localized complete season must use season/complete labels from the same language.
L54> Support both "Season Snn ... COMPLETE" and "Season d ... COMPLETE" (numeric) formats
L60> Pattern 1: Season Snn ... COMPLETE (e.g., "Season S03 ... COMPLETE")
L73> `return True`
L75> Pattern 2: Season d ... COMPLETE (e.g., "Stagione 3 ... COMPLETA")
L88> `return True`
L90> `return False`

### fn `def _match_episode_range_pack(raw_title, numeric_season, numeric_episode)` `priv` (L93-109)
L106> `return True`
L107> `return False`

### fn `def _match_season_episode_pair(raw_title, numeric_season, numeric_episode)` `priv` (L110-122)
L120> `return season_episode_match.search(title) is not None`

### fn `def _match_title_with_season(raw_title, media_title, numeric_season)` `priv` (L123-175)
L124-129> Match title followed by season in three forms for series: 1. <title>.+Snn (basic season format) 2. <title>.+Season Snn (localized season label with Snn) 3. <title>.+Season d (localized season label with numeric season)
L131> Normalize title to handle dots, spaces, underscores as separators
L132> Replace each word separator in media_title with flexible separator pattern
L135> Pattern 1: <title>.+Snn (e.g., "Person of Interest ... S03" or "Person.Of.Interest.S03")
L141> `return True`
L143> Pattern 2 and 3: <title>.+Season Snn or <title>.+Season d (localized)
L145> Pattern 2: <title>.+Season Snn (e.g., "Person of Interest ... Season S03")
L157> `return True`
L159> Pattern 3: <title>.+Season d (e.g., "Person of Interest ... Stagione 3")
L171> `return True`
L173> `return False`

### fn `def sort_quality(item)` (L176-197)
L177> if item.parsed_data.data.resolution is None or item.parsed_data.data.resolution == "unknown" or item.parsed_data.data.resolution == "":
L178> return float('inf'), True
L180> # TODO: first resolution?
L181> return quality_order.get(item.parsed_data.data.resolution[0],
L182> float('inf')), item.parsed_data.data.resolution is None
L184> Controlla la presenza di parsed_data e data
L186> `return float('inf'), True` — True = non trovato
L190> Gestione dei casi con risoluzione mancante o sconosciuta
L192> `return float('inf'), True` — True = non trovato
L194> Ritorna il valore di quality_order con fallback a infinito
L195> `return quality_order.get(resolution, float('inf')), False` — False = trovato

### fn `def items_sort(items, config)` (L198-250)
L205> custom_ranks={
L206> uhd": CustomRank(enable=True, fetch=True, rank=200),
L207> hdr": CustomRank(enable=True, fetch=True, rank=100),
L208> }
L211> Se genera l'eccezione poi l'ordinamento dei TorrentItems basato sui Torrent non funziona
L212> if rank < self.settings.options["remove_ranks_under"]:
L213> raise GarbageTorrent(f"'{raw_title}' does not meet the minimum rank requirement, got rank of {rank}")
L215> maximun negative value => non ne leva nessuno
L217> default: remove_ranks_under = -10000,
L218> 32 bit?
L222> torrents = [rtn.rank(item.raw_title, item.info_hash) for item in items]
L241> `return sorted(items, key=sort_quality)`
L243> `return sorted(items, key=lambda x: int(x.size))`
L245> `return sorted(items, key=lambda x: int(x.size), reverse=True)`
L247> `return sorted(items, key=lambda x: (sort_quality(x), -int(x.size)))`
L248> `return items`

### fn `def filter_out_non_matching(items, season, episode)` (L267-294)
L264> return filtered_items
L270> logger.debug(item.parsed_data)
L292> `return filtered_items`

### fn `def remove_non_matching_title(items, titles, media)` (L295-339)
L297> default: threshold: float = 0.85
L304> For series, use season-aware matching
L309> Check if title has season-aware match (validates season is correct)
L314> Generic title match only if no season info in raw_title
L315> (fallback for items without explicit season in title)
L317> Check if raw_title contains any season pattern
L324> Only accept generic match if no season pattern found in title
L329> For movies, use generic title match
L337> `return filtered_items`

### fn `def filter_items(items, media, config)` (L340-383)
L341> vengono processati nell'ordine in cui sono dichiarati
L344> Max size filtering only happens for movies, so it
L350> Filtering out 100% non-matching for series
L358> TODO: is titles[0] always the correct title? Maybe loop through all titles and get the highest match?
L364> finché ci sono risultati
L373> per esempio se ci sono solo versioni in inglese, le tiene e ritorna quelle
L381> `return items`

### fn `def sort_items(items, config)` (L384-388)
L386> `return items_sort(items, config)`
L388> `return items`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L53-54: Localized complete season must use season/complete labels from the same language. | Support both "Season Snn ... COMPLETE" and "Season d ... COMPLETE" (numeric) formats
- L60: Pattern 1: Season Snn ... COMPLETE (e.g., "Season S03 ... COMPLETE")
- L75: Pattern 2: Season d ... COMPLETE (e.g., "Stagione 3 ... COMPLETA")
- L124-132: Match title followed by season in three forms for series: 1. <title>.+Snn (basic season format) 2... | Normalize title to handle dots, spaces, underscores as separators | Replace each word separator in media_title with flexible separator pattern
- L135: Pattern 1: <title>.+Snn (e.g., "Person of Interest ... S03" or "Person.Of.Interest.S03")
- L143-145: Pattern 2 and 3: <title>.+Season Snn or <title>.+Season d (localized) | Pattern 2: <title>.+Season Snn (e.g., "Person of Interest ... Season S03")
- L159: Pattern 3: <title>.+Season d (e.g., "Person of Interest ... Stagione 3")
- L177-184: if item.parsed_data.data.resolution is None or item.parsed_data.data.resolution == "unknown" or i... | return float('inf'), True | # TODO: first resolution? | return quality_order.get(item.parsed_data.data.resolution[0], | float('inf')), item.parsed_data.data.resolution is None | Controlla la presenza di parsed_data e data
- L190: Gestione dei casi con risoluzione mancante o sconosciuta
- L194: Ritorna il valore di quality_order con fallback a infinito
- L205-208: custom_ranks={ | uhd": CustomRank(enable=True, fetch=True, rank=200), | hdr": CustomRank(enable=True, fetch=True, rank=100), | }
- L211-217: Se genera l'eccezione poi l'ordinamento dei TorrentItems basato sui Torrent non funziona | if rank < self.settings.options["remove_ranks_under"]: | raise GarbageTorrent(f"'{raw_title}' does not meet the minimum rank requirement, got rank of {ran... | maximun negative value => non ne leva nessuno | default: remove_ranks_under = -10000,
- L222: torrents = [rtn.rank(item.raw_title, item.info_hash) for item in items]
- L251-263: def filter_season_episode(items, season, episode, config): | filtered_items = [] | for item in items: | if config['language'] == "ru": | if "S" + str(int(season.replace("S", ""))) + "E" + str( | int(episode.replace("E", ""))) not in item['title']: | if re.search(rf'\bS{re.escape(str(int(season.replace("S", ""))))}\b', item['title']) is None: | continue | if re.search(rf'\b{season}\s?{episode}\b', item['title']) is None: | if re.search(rf'\b{season}\b', item['title']) is None: | continue | filtered_items.append(item)
- L270: logger.debug(item.parsed_data)
- L297: default: threshold: float = 0.85
- L304: For series, use season-aware matching
- L309: Check if title has season-aware match (validates season is correct)
- L314-317: Generic title match only if no season info in raw_title | (fallback for items without explicit season in title) | Check if raw_title contains any season pattern
- L324: Only accept generic match if no season pattern found in title
- L329: For movies, use generic title match
- L341: vengono processati nell'ordine in cui sono dichiarati
- L350: Filtering out 100% non-matching for series
- L358: TODO: is titles[0] always the correct title? Maybe loop through all titles and get the highest match?
- L373: per esempio se ci sono solo versioni in inglese, le tiene e ritorna quelle

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`_match_complete_season`|fn|priv|50-92|def _match_complete_season(raw_title, numeric_season)|
|`_match_episode_range_pack`|fn|priv|93-109|def _match_episode_range_pack(raw_title, numeric_season, ...|
|`_match_season_episode_pair`|fn|priv|110-122|def _match_season_episode_pair(raw_title, numeric_season,...|
|`_match_title_with_season`|fn|priv|123-175|def _match_title_with_season(raw_title, media_title, nume...|
|`sort_quality`|fn|pub|176-197|def sort_quality(item)|
|`items_sort`|fn|pub|198-250|def items_sort(items, config)|
|`filter_out_non_matching`|fn|pub|267-294|def filter_out_non_matching(items, season, episode)|
|`remove_non_matching_title`|fn|pub|295-339|def remove_non_matching_title(items, titles, media)|
|`filter_items`|fn|pub|340-383|def filter_items(items, media, config)|
|`sort_items`|fn|pub|384-388|def sort_items(items, config)|


---

# title_exclusion_filter.py | Python | 27L | 4 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/filter/title_exclusion_filter.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TitleExclusionFilter(BaseFilter)` : BaseFilter (L11-27)
- fn `def __init__(self, config)` `priv` (L12-14)
- fn `def filter(self, data)` (L15-25)
  L24> `return filtered_items`
- fn `def can_filter(self)` (L26-27)
  L27> `return self.config['exclusionKeywords'] is not None and len(self.config['exclusionKeywords']) > 0`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TitleExclusionFilter`|class|pub|11-27|class TitleExclusionFilter(BaseFilter)|
|`TitleExclusionFilter.__init__`|fn|priv|12-14|def __init__(self, config)|
|`TitleExclusionFilter.filter`|fn|pub|15-25|def filter(self, data)|
|`TitleExclusionFilter.can_filter`|fn|pub|26-27|def can_filter(self)|


---

# general.py | Python | 46L | 3 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/general.py`
> VERSION: 0.0.35

## Imports
```
from RTN import parse
from debriddo.utils.logger import setup_logger
```

## Definitions

### fn `def season_episode_in_filename(filename, season, episode)` (L18-24)
L20> `return False`
L22> `return int(season.replace("S", "")) in parsed_name.seasons and int(episode.replace("E", "")) in parsed_name.episodes`

### fn `def get_info_hash_from_magnet(magnet: str)` (L25-40)
L29> `return None`
L38> `return info_hash.lower()`

### fn `def is_video_file(filename)` (L41-46)
L44> `return False`
L46> `return filename[extension_idx:] in video_formats`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`season_episode_in_filename`|fn|pub|18-24|def season_episode_in_filename(filename, season, episode)|
|`get_info_hash_from_magnet`|fn|pub|25-40|def get_info_hash_from_magnet(magnet: str)|
|`is_video_file`|fn|pub|41-46|def is_video_file(filename)|


---

# logger.py | Python | 112L | 16 symbols | 2 imports | 23 comments
> Path: `src/debriddo/utils/logger.py`
> VERSION: 0.0.35

## Imports
```
import os
import logging
```

## Definitions

### class `class CustomFormatter(logging.Formatter)` : logging.Formatter (L8-68)
L26> Spaziatura
L27> INFO:
L28> DEBUG:
L29> WARNING:
L30> ERROR:
L31> CRITICAL:
- var `WHITE = "\033[97m"` (L11) L9> Logging Formatter to add colors and count warning / errors
- var `WHITE_BOLD = "\033[1;97m"` (L12)
- var `GREY = "\033[90m"` (L13)
- var `LIGHT_GREY = "\033[37m"` (L14)
- var `CYAN = "\033[36m"` (L15)
- var `MAGENTA = "\033[35m"` (L16)
- var `BLUE = "\033[34m"` (L17)
- var `RED = "\033[31m"` (L18)
- var `GREEN = "\033[32m"` (L19)
- var `YELLOW = "\033[33m"` (L20)
- var `RED_BOLD = "\033[1;31m"` (L21)
- var `RESET = "\033[0m"` (L24) L23> Reset color
- var `FORMATS =` (L46)
- fn `def format(self, record)` (L54-68)
  L55-63> Formatta il record di log applicando colori e stili. Args: record (logging.LogRecord): Il record di log da formattare. Returns: str: Il messaggio di log formattato.
  L66> `return formatter.format(record)`

### fn `def setup_logger(name, debug=None)` (L69-105)
L70-79> Configura e restituisce un logger con formatter personalizzato. Args: name (str): Il nome del logger. debug (bool, optional): Se True, imposta il livello a DEBUG. Defaults to None. Returns: logging.Logger: L'istanza del logger configurata.
L82> get environment
L89> define logging level
L96> `return logger`
L98> Create console handler with a higher log level
L100> Adjust as needed: DEBUG, INFO
L104> `return logger`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L26-31: Spaziatura | INFO: | DEBUG: | WARNING: | ERROR: | CRITICAL:
- L55: Formatta il record di log applicando colori e stili. Args: ...
- L70: Configura e restituisce un logger con formatter personalizzato. Args: ...
- L82: get environment
- L89: define logging level
- L98: Create console handler with a higher log level
- L106-112: Example usage | logger = setup_logger(__name__) | logger.debug('This is a debug message') | logger.info('This is an info message') | logger.warning('This is a warning message') | logger.error('This is an error message') | logger.critical('This is a critical message')

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CustomFormatter`|class|pub|8-68|class CustomFormatter(logging.Formatter)|
|`CustomFormatter.WHITE`|var|pub|11||
|`CustomFormatter.WHITE_BOLD`|var|pub|12||
|`CustomFormatter.GREY`|var|pub|13||
|`CustomFormatter.LIGHT_GREY`|var|pub|14||
|`CustomFormatter.CYAN`|var|pub|15||
|`CustomFormatter.MAGENTA`|var|pub|16||
|`CustomFormatter.BLUE`|var|pub|17||
|`CustomFormatter.RED`|var|pub|18||
|`CustomFormatter.GREEN`|var|pub|19||
|`CustomFormatter.YELLOW`|var|pub|20||
|`CustomFormatter.RED_BOLD`|var|pub|21||
|`CustomFormatter.RESET`|var|pub|24||
|`CustomFormatter.FORMATS`|var|pub|46||
|`CustomFormatter.format`|fn|pub|54-68|def format(self, record)|
|`setup_logger`|fn|pub|69-105|def setup_logger(name, debug=None)|


---

# multi_thread.py | Python | 16L | 2 symbols | 2 imports | 3 comments
> Path: `src/debriddo/utils/multi_thread.py`
> VERSION: 0.0.35

## Imports
```
import asyncio
from debriddo.constants import RUN_IN_MULTI_THREAD
```

## Definitions

- var `MULTI_THREAD = RUN_IN_MULTI_THREAD` (L7)
### fn `def run_coroutine_in_thread(coro)` (L10-16)
L9> Funzione per eseguire una coroutine in un nuovo event loop sul thread del pool
L14> `return new_loop.run_until_complete(coro)`

## Comments
- L2: AUTHORS: Ogekuri

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MULTI_THREAD`|var|pub|7||
|`run_coroutine_in_thread`|fn|pub|10-16|def run_coroutine_in_thread(coro)|


---

# novaprinter.py | Python | 69L | 6 symbols | 1 imports | 20 comments
> Path: `src/debriddo/utils/novaprinter.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class PrettyPrint` (L18-69)
- fn `def __init__(self)` `priv` (L19-23)
  L20> Inizializza una lista per salvare tutte le stringhe stampate
- fn `def __call__(self, dictionary): # *args, **kwargs)` `priv` (L24-31)
  L25> Se serve comunque stampare l'dictionary_list, puoi usare:
  L27> convert size to bytes
- fn `def __anySizeToBytes(self, size_string)` `priv` (L32-59)
  L33-35> Convert a string like '1 KB' to '1024' (bytes)
  L36> separate integer from unit
  L46> `return -1`
  L48> `return -1`
  L51> `return int(size)`
  L54> convert
  L58> `return int(size)`
- fn `def get(self)` (L60-66)
  L61> Restituisci l'elenco di tutte le stringhe accumulate
  L63> `return self.dictionary_list`
  L65> `return None`
- fn `def clear(self)` (L67-69)
  L68> Resetta l'elenco delle stringhe salvate

## Comments
- L2-14: AUTHORS: Ogekuri | def prettyPrinter(dictionary): | dictionary['size'] = anySizeToBytes(dictionary['size']) | outtext = "|".join((dictionary["link"], dictionary["name"].replace("|", " "), | str(dictionary["size"]), str(dictionary["seeds"]), | str(dictionary["leech"]), dictionary["engine_url"])) | if 'desc_link' in dictionary: | outtext = "|".join((outtext, dictionary["desc_link"])) | # fd 1 is stdout | with open(1, 'w', encoding='utf-8', closefd=False) as utf8stdout: | print(outtext, file=utf8stdout)
- L20: Inizializza una lista per salvare tutte le stringhe stampate
- L25-27: Se serve comunque stampare l'dictionary_list, puoi usare: | convert size to bytes
- L33-36: Convert a string like '1 KB' to '1024' (bytes) | separate integer from unit
- L54: convert
- L61: Restituisci l'elenco di tutte le stringhe accumulate
- L68: Resetta l'elenco delle stringhe salvate

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`PrettyPrint`|class|pub|18-69|class PrettyPrint|
|`PrettyPrint.__init__`|fn|priv|19-23|def __init__(self)|
|`PrettyPrint.__call__`|fn|priv|24-31|def __call__(self, dictionary): # *args, **kwargs)|
|`PrettyPrint.__anySizeToBytes`|fn|priv|32-59|def __anySizeToBytes(self, size_string)|
|`PrettyPrint.get`|fn|pub|60-66|def get(self)|
|`PrettyPrint.clear`|fn|pub|67-69|def clear(self)|


---

# parse_config.py | Python | 30L | 3 symbols | 1 imports | 9 comments
> Path: `src/debriddo/utils/parse_config.py`
> VERSION: 0.0.35

## Imports
```
from debriddo.utils.string_encoding import decode_lzstring, encode_lzstring
```

## Definitions

### fn `def parse_config(encoded_config)` (L8-15)
L7> wrapping alla decode_lzstring per gestire eventuali retro-compatibità
L10> decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
L13> `return config`

### fn `def parse_query(encoded_query)` (L17-23)
L16> wrapping alla decode_lzstring per gestire eventuali retro-compatibità
L19> decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
L22> `return query`

### fn `def encode_query(query)` (L25-30)
L24> wrapping alla encode_lzstring per gestire eventuali retro-compatibità
L27> decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
L30> `return encoded_query`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L10: decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
- L19: decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
- L27: decodifica utilizzando l'algoritmo di LZString con encodeURIComponent

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`parse_config`|fn|pub|8-15|def parse_config(encoded_config)|
|`parse_query`|fn|pub|17-23|def parse_query(encoded_query)|
|`encode_query`|fn|pub|25-30|def encode_query(query)|


---

# stremio_parser.py | Python | 185L | 8 symbols | 8 imports | 21 comments
> Path: `src/debriddo/utils/stremio_parser.py`
> VERSION: 0.0.35

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

### fn `def get_emoji(language)` (L17-34)
L16> TODO: Languages
L32> `return emoji_dict.get(language, "🇬🇧")`

- var `INSTANTLY_AVAILABLE = "[⚡"` (L35)
- var `DOWNLOAD_REQUIRED = "[⬇️"` (L36)
- var `DIRECT_TORRENT = "[🏴‍☠️"` (L37)
### fn `def filter_by_availability(item)` (L40-46)
L42> `return 0`
L44> `return 1`

### fn `def filter_by_direct_torrnet(item)` (L47-53)
L49> `return 1`
L51> `return 0`

### fn `def parse_to_debrid_stream(torrent_item: TorrentItem, config_url, node_url, playtorrent, results: queue.Queue, media: Media)` (L54-159)
L71> TODO: Always take the first resolution, is that the best one?
L72> resolution = parsed_data.resolution[0] if len(parsed_data.resolution) > 0 else "Unknown
L73> name += f"{resolution}" + (f"\n({'|'.join(parsed_data.quality)})" if len(parsed_data.quality) > 0 else "")
L75> from cache
L81> seson package
L92> formattazione pannello sinistro gui
L115> query_encoded = encode64(json.dumps(torrent_item.to_debrid_stream_query(media))).replace('=', '%3D')
L116> TODO: come mai sostituiva l'=?
L125> TODO: Use parsed title?
L130> warning per url troppo lunghi
L131> TODO: da decidere il valore
L135> Se è abilitato il play diretto del torrent lo aggiunge in coda
L136> Rimmosso 'and torrent_item.privacy == "public":', non devo condividere il torrent, non il file sulla rete torrent
L139> formattazione pannello sinistro gui
L143> if len(parsed_data.quality) > 0 and parsed_data.quality[0] != "Unknown" and \
L144> parsed_data.quality[0] != "":
L145> name += f"({'|'.join(parsed_data.quality)})
L153> TODO: Use parsed title?
L155> sources": ["tracker:" + tracker for tracker in torrent_item.trackers]

### fn `def parse_to_stremio_streams(torrent_items: List[TorrentItem], config, config_url, node_url, media)` (L160-185)
L179> `return []`
L182> ordinamento predefinito
L185> `return stream_list`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L71-75: TODO: Always take the first resolution, is that the best one? | resolution = parsed_data.resolution[0] if len(parsed_data.resolution) > 0 else "Unknown | name += f"{resolution}" + (f"\n({'|'.join(parsed_data.quality)})" if len(parsed_data.quality) > 0... | from cache
- L81: seson package
- L92: formattazione pannello sinistro gui
- L115-116: query_encoded = encode64(json.dumps(torrent_item.to_debrid_stream_query(media))).replace('=', '%3D') | TODO: come mai sostituiva l'=?
- L130-131: warning per url troppo lunghi | TODO: da decidere il valore
- L135: Se è abilitato il play diretto del torrent lo aggiunge in coda
- L139: formattazione pannello sinistro gui
- L143-145: if len(parsed_data.quality) > 0 and parsed_data.quality[0] != "Unknown" and \ | parsed_data.quality[0] != "": | name += f"({'|'.join(parsed_data.quality)})
- L155: sources": ["tracker:" + tracker for tracker in torrent_item.trackers]
- L182: ordinamento predefinito

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_emoji`|fn|pub|17-34|def get_emoji(language)|
|`INSTANTLY_AVAILABLE`|var|pub|35||
|`DOWNLOAD_REQUIRED`|var|pub|36||
|`DIRECT_TORRENT`|var|pub|37||
|`filter_by_availability`|fn|pub|40-46|def filter_by_availability(item)|
|`filter_by_direct_torrnet`|fn|pub|47-53|def filter_by_direct_torrnet(item)|
|`parse_to_debrid_stream`|fn|pub|54-159|def parse_to_debrid_stream(torrent_item: TorrentItem, con...|
|`parse_to_stremio_streams`|fn|pub|160-185|def parse_to_stremio_streams(torrent_items: List[TorrentI...|


---

# string_encoding.py | Python | 53L | 3 symbols | 4 imports | 7 comments
> Path: `src/debriddo/utils/string_encoding.py`
> VERSION: 0.0.35

## Imports
```
import json
import re
from unidecode import unidecode
import lzstring
```

## Definitions

### fn `def encode_lzstring(json_value, tag)` (L11-23)
L14> `raise ValueError("Incompatible tag encoding lz-string")`
L19> `raise ValueError(f"An error occurred decoding lz-string: {e}")`
L21> `return data`

### fn `def decode_lzstring(data, tag)` (L24-41)
L27> Se il prefisso "C_" è presente, rimuovilo
L31> `raise ValueError("Incompatible tag decoding lz-string")`
L35> `raise ValueError("Failed to decompress lz-string payload")`
L38> `raise ValueError(f"An error occurred decoding lz-string: {e}")`
L40> `return json_value`

### fn `def normalize(string)` (L42-53)
L43> kožušček -> kozuscek
L44> 北亰 -> Bei Jing
L45> François -> Francois
L47> ’s ->
L51> `return string`

## Comments
- L2-3: AUTHORS: aymene69 | CONTRIBUTORS: Ogekuri
- L27: Se il prefisso "C_" è presente, rimuovilo
- L43-45: kožušček -> kozuscek | 北亰 -> Bei Jing | François -> Francois

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`encode_lzstring`|fn|pub|11-23|def encode_lzstring(json_value, tag)|
|`decode_lzstring`|fn|pub|24-41|def decode_lzstring(data, tag)|
|`normalize`|fn|pub|42-53|def normalize(string)|


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

# pages.py | Python | 78L | 2 symbols | 1 imports | 4 comments
> Path: `src/debriddo/web/pages.py`
> VERSION: 0.0.35

## Imports
```
from pathlib import Path
```

## Definitions

- var `WEB_DIR = Path(__file__).resolve().parent` (L6)
### fn `def get_index(app_name, app_version, app_environment)` (L9-78)
L10-20> Legge e restituisce il contenuto della pagina index.html con i placeholder sostituiti. Args: app_name (str): Il nome dell'applicazione. app_version (str): La versione dell'applicazione. app_environment (str): L'ambiente di esecuzione (es. development). Returns: str: Il contenuto HTML della pagina index processata.
L26> `return index`
L27-77> error = <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Error - Page Not Found</title> <style> body { font-family: Arial, sans-serif; text-align: center; background-color: #f8f9fa; color: #333; margin: 0; padding: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; } h1 { font-size: 4rem; margin: 0; } p { font-size: 1.5rem; margin: 10px 0; } a { display: inline-block; margin-top: 20px; padding: 10px 20px; font-size: 1rem; color: #fff; background-color: #007bff; text-decoration: none; border-radius: 5px; } a:hover { background-color: #0056b3; } </style> </head> <body> <h1>404</h1> <p>Oops! The page you're looking for doesn't exist.</p> <a href="/">Go Back Home</a> </body> </html>
L78> `return error`

## Comments
- L2: AUTHORS: Ogekuri
- L10: Legge e restituisce il contenuto della pagina index.html con i placeholder sostituiti. Args: ...
- L27: error = <!DOCTYPE html> <html lang="en"> <head> ...

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`WEB_DIR`|var|pub|6||
|`get_index`|fn|pub|9-78|def get_index(app_name, app_version, app_environment)|

