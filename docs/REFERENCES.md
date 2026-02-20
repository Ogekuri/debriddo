# Files Structure
```
.
└── src
    ├── api_tester
    │   └── api_tester.py
    └── debriddo
        ├── check_unused_requirements.py
        ├── constants.py
        ├── debrid
        │   ├── alldebrid.py
        │   ├── base_debrid.py
        │   ├── get_debrid_service.py
        │   ├── premiumize.py
        │   ├── realdebrid.py
        │   └── torbox.py
        ├── main.py
        ├── metdata
        │   ├── cinemeta.py
        │   ├── metadata_provider_base.py
        │   └── tmdb.py
        ├── models
        │   ├── media.py
        │   ├── movie.py
        │   └── series.py
        ├── search
        │   ├── plugins
        │   │   ├── base_plugin.py
        │   │   ├── ilcorsaroblu.py
        │   │   ├── ilcorsaronero.py
        │   │   ├── limetorrents.py
        │   │   ├── one337x.py
        │   │   ├── thepiratebay_categories.py
        │   │   ├── therarbg.py
        │   │   ├── torrentgalaxyone.py
        │   │   ├── torrentgalaxyto.py
        │   │   ├── torrentproject.py
        │   │   └── torrentz.py
        │   ├── search_indexer.py
        │   ├── search_result.py
        │   └── search_service.py
        ├── test_plugins.py
        ├── test_sviluppo_plugins.py
        ├── torrent
        │   ├── torrent_item.py
        │   ├── torrent_service.py
        │   └── torrent_smart_container.py
        ├── utils
        │   ├── async_httpx_session.py
        │   ├── cache.py
        │   ├── detection.py
        │   ├── filter
        │   │   ├── base_filter.py
        │   │   ├── language_filter.py
        │   │   ├── max_size_filter.py
        │   │   ├── quality_exclusion_filter.py
        │   │   ├── results_per_quality_filter.py
        │   │   └── title_exclusion_filter.py
        │   ├── filter_results.py
        │   ├── general.py
        │   ├── logger.py
        │   ├── multi_thread.py
        │   ├── novaprinter.py
        │   ├── parse_config.py
        │   ├── stremio_parser.py
        │   └── string_encoding.py
        └── web
            ├── config.js
            ├── lz-string.min.js
            └── pages.py
```

# api_tester.py | Python | 1022L | 33 symbols | 9 imports | 35 comments
> Path: `src/api_tester/api_tester.py`

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

- var `DEFAULT_CONFIG_ENV = "DEBRIDDO_CONFIG_URL"` (L27)
- Brief: Exported constant `DEFAULT_CONFIG_ENV` used by runtime workflows.
- var `DEFAULT_TIMEOUT = 180.0` (L29)
- Brief: Exported constant `DEFAULT_TIMEOUT` used by runtime workflows.
- var `DEBRIDDO_MODULE_PREFIX = "debriddo"` (L31)
- Brief: Exported constant `DEBRIDDO_MODULE_PREFIX` used by runtime workflows.
### class `class CliError(Exception)` : Exception (L34-41)
- Brief: Class `CliError` encapsulates cohesive runtime behavior.
- Details: Generated Doxygen block for class-level contract and extension boundaries.

### fn `def ensure_no_debriddo_modules_loaded() -> None` (L42-43)

### class `class TargetUrls` `@dataclass` (L59-68)
- Brief: Class `TargetUrls` encapsulates cohesive runtime behavior.
- Details: Generated Doxygen block for class-level contract and extension boundaries.

### class `class CheckResult` `@dataclass` (L70-79)
- Brief: Class `CheckResult` encapsulates cohesive runtime behavior.
- Details: Generated Doxygen block for class-level contract and extension boundaries.

### fn `def normalize_config_url(raw_value: str) -> TargetUrls` (L80-81)

### fn `def get_target_from_args(args: argparse.Namespace) -> TargetUrls` (L122-123)

### fn `def request_url(` (L136-142)

### fn `def make_url(base_url: str, path: str) -> str` (L164-165)

### fn `def parse_json_body(response: requests.Response) -> Optional[Any]` (L174-175)

### fn `def print_response_summary(` (L186-189)

### fn `def call_simple_endpoint(` (L220-226)

### fn `def build_stream_path(` (L252-256)

### fn `def cmd_target(args: argparse.Namespace) -> int` (L272-273)

### fn `def cmd_root(args: argparse.Namespace) -> int` (L285-286)

### fn `def cmd_configure(args: argparse.Namespace) -> int` (L303-304)

### fn `def cmd_manifest(args: argparse.Namespace) -> int` (L315-316)

### fn `def cmd_site_webmanifest(args: argparse.Namespace) -> int` (L327-328)

### fn `def cmd_asset(args: argparse.Namespace) -> int` (L338-339)

### fn `def request_stream(` (L367-373)

### fn `def cmd_stream(args: argparse.Namespace) -> int` (L402-403)

### fn `def cmd_search(args: argparse.Namespace) -> int` (L435-436)

### fn `def extract_playback_path_from_streams(streams_payload: Dict[str, Any]) -> Optional[str]` (L471-472)

### fn `def request_playback(` (L493-498)

### fn `def cmd_playback(args: argparse.Namespace) -> int` (L520-521)

### fn `def validate_manifest_payload(payload: Dict[str, Any]) -> Tuple[bool, str]` (L566-567)

### fn `def add_check(results: List[CheckResult], name: str, ok: bool, detail: str) -> None` (L586-587)

### fn `def run_smoke(args: argparse.Namespace, target: TargetUrls) -> List[CheckResult]` (L598-599)

### fn `def cmd_smoke(args: argparse.Namespace) -> int` (L822-823)

### fn `def build_parser() -> argparse.ArgumentParser` (L842-843)

### fn `def main() -> int` (L1002-1003)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`DEFAULT_CONFIG_ENV`|var|pub|27||
|`DEFAULT_TIMEOUT`|var|pub|29||
|`DEBRIDDO_MODULE_PREFIX`|var|pub|31||
|`CliError`|class|pub|34-41|class CliError(Exception)|
|`ensure_no_debriddo_modules_loaded`|fn|pub|42-43|def ensure_no_debriddo_modules_loaded() -> None|
|`TargetUrls`|class|pub|59-68|class TargetUrls|
|`CheckResult`|class|pub|70-79|class CheckResult|
|`normalize_config_url`|fn|pub|80-81|def normalize_config_url(raw_value: str) -> TargetUrls|
|`get_target_from_args`|fn|pub|122-123|def get_target_from_args(args: argparse.Namespace) -> Tar...|
|`request_url`|fn|pub|136-142|def request_url(|
|`make_url`|fn|pub|164-165|def make_url(base_url: str, path: str) -> str|
|`parse_json_body`|fn|pub|174-175|def parse_json_body(response: requests.Response) -> Optio...|
|`print_response_summary`|fn|pub|186-189|def print_response_summary(|
|`call_simple_endpoint`|fn|pub|220-226|def call_simple_endpoint(|
|`build_stream_path`|fn|pub|252-256|def build_stream_path(|
|`cmd_target`|fn|pub|272-273|def cmd_target(args: argparse.Namespace) -> int|
|`cmd_root`|fn|pub|285-286|def cmd_root(args: argparse.Namespace) -> int|
|`cmd_configure`|fn|pub|303-304|def cmd_configure(args: argparse.Namespace) -> int|
|`cmd_manifest`|fn|pub|315-316|def cmd_manifest(args: argparse.Namespace) -> int|
|`cmd_site_webmanifest`|fn|pub|327-328|def cmd_site_webmanifest(args: argparse.Namespace) -> int|
|`cmd_asset`|fn|pub|338-339|def cmd_asset(args: argparse.Namespace) -> int|
|`request_stream`|fn|pub|367-373|def request_stream(|
|`cmd_stream`|fn|pub|402-403|def cmd_stream(args: argparse.Namespace) -> int|
|`cmd_search`|fn|pub|435-436|def cmd_search(args: argparse.Namespace) -> int|
|`extract_playback_path_from_streams`|fn|pub|471-472|def extract_playback_path_from_streams(streams_payload: D...|
|`request_playback`|fn|pub|493-498|def request_playback(|
|`cmd_playback`|fn|pub|520-521|def cmd_playback(args: argparse.Namespace) -> int|
|`validate_manifest_payload`|fn|pub|566-567|def validate_manifest_payload(payload: Dict[str, Any]) ->...|
|`add_check`|fn|pub|586-587|def add_check(results: List[CheckResult], name: str, ok: ...|
|`run_smoke`|fn|pub|598-599|def run_smoke(args: argparse.Namespace, target: TargetUrl...|
|`cmd_smoke`|fn|pub|822-823|def cmd_smoke(args: argparse.Namespace) -> int|
|`build_parser`|fn|pub|842-843|def build_parser() -> argparse.ArgumentParser|
|`main`|fn|pub|1002-1003|def main() -> int|


---

# check_unused_requirements.py | Python | 115L | 3 symbols | 3 imports | 15 comments
> Path: `src/debriddo/check_unused_requirements.py`

## Imports
```
import os
import ast
import importlib.metadata
```

## Definitions

### fn `def get_imported_modules_from_file(filepath)` (L14-15)

### fn `def get_all_imported_modules(root_dir)` (L37-38)

### fn `def get_requirements(requirements_file)` (L54-55)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_imported_modules_from_file`|fn|pub|14-15|def get_imported_modules_from_file(filepath)|
|`get_all_imported_modules`|fn|pub|37-38|def get_all_imported_modules(root_dir)|
|`get_requirements`|fn|pub|54-55|def get_requirements(requirements_file)|


---

# constants.py | Python | 27L | 6 symbols | 0 imports | 12 comments
> Path: `src/debriddo/constants.py`

## Definitions

- var `APPLICATION_NAME = "Debriddo"` (L11)
- Brief: Exported constant `APPLICATION_NAME` used by runtime workflows.
- var `APPLICATION_VERSION = "0.0.35"` (L13)
- Brief: Exported constant `APPLICATION_VERSION` used by runtime workflows.
- var `APPLICATION_DESCRIPTION = "Ricerca online i Film e le tue Serie Tv preferite."` (L15)
- Brief: Exported constant `APPLICATION_DESCRIPTION` used by runtime workflows.
- var `CACHE_DATABASE_FILE = "caches_items.db"` (L19)
- Brief: Exported constant `CACHE_DATABASE_FILE` used by runtime workflows.
- var `NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/refs/heads/master/videos/nocache.mp4"` (L23)
- Brief: Exported constant `NO_CACHE_VIDEO_URL` used by runtime workflows.
- var `RUN_IN_MULTI_THREAD = True` (L27)
- Brief: Exported constant `RUN_IN_MULTI_THREAD` used by runtime workflows.
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

# main.py | Python | 693L | 23 symbols | 35 imports | 96 comments
> Path: `src/debriddo/main.py`

## Imports
```
import os
import sys
import re
import shutil
import time
import zipfile
import uvicorn
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

- var `APP_DIR = Path(__file__).resolve().parent` (L59)
- Brief: Exported constant `APP_DIR` used by runtime workflows.
- var `WEB_DIR = APP_DIR / "web"` (L61)
- Brief: Exported constant `WEB_DIR` used by runtime workflows.
### fn `def calculate_optimal_thread_count()` (L108-109)

### fn `def resolve_thread_count()` (L122-123)

### fn `def resolve_auto_thread_count()` (L147-148)

### fn `def get_or_create_event_loop()` (L158-159)

### fn `async def lifespan(app: FastAPI)` `@asynccontextmanager` (L172-173)

### class `class LogFilterMiddleware` (L207-208)

### fn `def __init__(self, app)` `priv` (L211-212)
- Brief: Class `LogFilterMiddleware` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

### fn `async def __call__(self, scope, receive, send)` `priv` (L218-219)

### fn `async def root()` `@app.get("/")` (L281-282)

### fn `async def get_favicon()` `@app.get("/favicon.ico")` (L289-290)

### fn `async def get_config_js()` `@app.get("/{config}/config.js")` (L299-300)

### fn `async def get_lz_string_js()` `@app.get("/{config}/lz-string.min.js")` (L309-310)

### fn `async def get_styles_css()` `@app.get("/{config}/styles.css")` (L319-320)

### fn `async def configure()` `@app.get("/{config}/configure", response_class=HTMLResponse)` (L330-331)

### fn `async def function(file_path: str)` `@app.get("/{config}/images/{file_path:path}")` (L339-340)

### fn `async def get_webmanifest()` `@app.get("/site.webmanifest", response_class=HTMLResponse)` (L349-350)

### fn `async def get_manifest()` `@app.get("/{params}/manifest.json")` (L387-388)

### fn `async def get_results(config_url: str, stream_type: str, stream_id: str, request: Request)` `@app.get("/{config_url}/stream/{stream_type}/{stream_id}")` (L468-469)

### fn `async def head_playback(config: str, query: str, request: Request)` `@app.head("/playback/{config_url}/{query}")` (L578-579)

### fn `async def get_playback(config_url: str, query_string: str, request: Request)` `@app.get("/playback/{config_url}/{query_string}")` (L593-594)

### fn `async def update_app()` (L628-629)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`APP_DIR`|var|pub|59||
|`WEB_DIR`|var|pub|61||
|`calculate_optimal_thread_count`|fn|pub|108-109|def calculate_optimal_thread_count()|
|`resolve_thread_count`|fn|pub|122-123|def resolve_thread_count()|
|`resolve_auto_thread_count`|fn|pub|147-148|def resolve_auto_thread_count()|
|`get_or_create_event_loop`|fn|pub|158-159|def get_or_create_event_loop()|
|`lifespan`|fn|pub|172-173|async def lifespan(app: FastAPI)|
|`LogFilterMiddleware`|class|pub|207-208|class LogFilterMiddleware|
|`__init__`|fn|priv|211-212|def __init__(self, app)|
|`__call__`|fn|priv|218-219|async def __call__(self, scope, receive, send)|
|`root`|fn|pub|281-282|async def root()|
|`get_favicon`|fn|pub|289-290|async def get_favicon()|
|`get_config_js`|fn|pub|299-300|async def get_config_js()|
|`get_lz_string_js`|fn|pub|309-310|async def get_lz_string_js()|
|`get_styles_css`|fn|pub|319-320|async def get_styles_css()|
|`configure`|fn|pub|330-331|async def configure()|
|`function`|fn|pub|339-340|async def function(file_path: str)|
|`get_webmanifest`|fn|pub|349-350|async def get_webmanifest()|
|`get_manifest`|fn|pub|387-388|async def get_manifest()|
|`get_results`|fn|pub|468-469|async def get_results(config_url: str, stream_type: str, ...|
|`head_playback`|fn|pub|578-579|async def head_playback(config: str, query: str, request:...|
|`get_playback`|fn|pub|593-594|async def get_playback(config_url: str, query_string: str...|
|`update_app`|fn|pub|628-629|async def update_app()|


---

# test_plugins.py | Python | 109L | 7 symbols | 3 imports | 15 comments
> Path: `src/debriddo/test_plugins.py`

## Imports
```
import asyncio
from pathlib import Path
from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy
```

## Definitions

- var `SRC_DIR = Path(__file__).resolve().parents[1]` (L17)
- Brief: Exported constant `SRC_DIR` used by runtime workflows.
### fn `def build_engines()` (L27-38)
- Brief: Execute `build_engines` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

- var `SEARCH_STRING = "The Fall Guy 2024 ITA"` (L40)
- Brief: Exported constant `SEARCH_STRING` used by runtime workflows.
- var `SEARCH_TYPE = "movies"` (L42)
- Brief: Exported constant `SEARCH_TYPE` used by runtime workflows.
### fn `def __is_torrent(link: str) -> bool` `priv` (L44-54)
- Brief: Execute `__is_torrent` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: link Runtime input parameter consumed by `__is_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __is_magnet_link(link: str) -> bool` `priv` (L55-65)
- Brief: Execute `__is_magnet_link` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: link Runtime input parameter consumed by `__is_magnet_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def main()` (L66-107)
- Brief: Execute `main` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SRC_DIR`|var|pub|17||
|`build_engines`|fn|pub|27-38|def build_engines()|
|`SEARCH_STRING`|var|pub|40||
|`SEARCH_TYPE`|var|pub|42||
|`__is_torrent`|fn|priv|44-54|def __is_torrent(link: str) -> bool|
|`__is_magnet_link`|fn|priv|55-65|def __is_magnet_link(link: str) -> bool|
|`main`|fn|pub|66-107|async def main()|


---

# test_sviluppo_plugins.py | Python | 109L | 2 symbols | 5 imports | 40 comments
> Path: `src/debriddo/test_sviluppo_plugins.py`

## Imports
```
import asyncio
from pathlib import Path
from urllib.parse import quote
from bs4 import BeautifulSoup
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

- var `SRC_DIR = Path(__file__).resolve().parents[1]` (L20)
- Brief: Exported constant `SRC_DIR` used by runtime workflows.
### fn `async def main()` (L22-108)
- Brief: Execute `main` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SRC_DIR`|var|pub|20||
|`main`|fn|pub|22-108|async def main()|


---

# config.js | JavaScript | 236L | 3 symbols | 0 imports | 11 comments
> Path: `src/debriddo/web/config.js`

## Definitions

### fn `function setElementDisplay(elementId, displayStatus)` (L9-15)

### fn `function loadData()` (L18-236)

### fn `function getLink(method)` (L97-236)

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

# pages.py | Python | 80L | 2 symbols | 1 imports | 6 comments
> Path: `src/debriddo/web/pages.py`

## Imports
```
from pathlib import Path
```

## Definitions

- var `WEB_DIR = Path(__file__).resolve().parent` (L13)
- Brief: Exported constant `WEB_DIR` used by runtime workflows.
### fn `def get_index(app_name, app_version, app_environment)` (L16-17)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`WEB_DIR`|var|pub|13||
|`get_index`|fn|pub|16-17|def get_index(app_name, app_version, app_environment)|


---

# search_indexer.py | Python | 32L | 2 symbols | 1 imports | 5 comments
> Path: `src/debriddo/search/search_indexer.py`

## Imports
```
from typing import Any
```

## Definitions

### class `class SearchIndexer` (L13-32)
- Brief: Class `SearchIndexer` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self)` `priv` (L18-32)
  - Brief: Class `SearchIndexer` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SearchIndexer`|class|pub|13-32|class SearchIndexer|
|`SearchIndexer.__init__`|fn|priv|18-32|def __init__(self)|


---

# search_result.py | Python | 112L | 4 symbols | 3 imports | 25 comments
> Path: `src/debriddo/search/search_result.py`

## Imports
```
from RTN import parse
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class SearchResult` (L17-18)

### fn `def __init__(self)` `priv` (L21-22)
- Brief: Class `SearchResult` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

### fn `def convert_to_torrent_item(self)` (L50-51)

### fn `def from_cached_item(self, cached_item)` (L89-90)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SearchResult`|class|pub|17-18|class SearchResult|
|`__init__`|fn|priv|21-22|def __init__(self)|
|`convert_to_torrent_item`|fn|pub|50-51|def convert_to_torrent_item(self)|
|`from_cached_item`|fn|pub|89-90|def from_cached_item(self, cached_item)|


---

# search_service.py | Python | 610L | 20 symbols | 24 imports | 57 comments
> Path: `src/debriddo/search/search_service.py`

## Imports
```
import asyncio
import re
import time
from itertools import chain
from urllib.parse import parse_qs, urlparse
from RTN import parse
from unidecode import unidecode
from debriddo.search.search_indexer import SearchIndexer
from debriddo.search.search_result import SearchResult
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.detection import detect_languages
from debriddo.utils.logger import setup_logger
from debriddo.utils.string_encoding import normalize
from debriddo.search.plugins.thepiratebay_categories import thepiratebay
from debriddo.search.plugins.one337x import one337x
from debriddo.search.plugins.limetorrents import limetorrents
from debriddo.search.plugins.torrentproject import torrentproject
from debriddo.search.plugins.ilcorsaronero import ilcorsaronero
from debriddo.search.plugins.torrentz import torrentz
from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy
from debriddo.search.plugins.therarbg import therarbg
from debriddo.search.plugins.ilcorsaroblu import ilcorsaroblu
from debriddo.utils.multi_thread import MULTI_THREAD, run_coroutine_in_thread
```

## Definitions

- var `SEARCHE_FALL_BACK = True` (L43)
- Brief: Exported constant `SEARCHE_FALL_BACK` used by runtime workflows.
### class `class SearchService` (L45-46)

### fn `def __init__(self, config)` `priv` (L49-50)
- Brief: Class `SearchService` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

### fn `async def search(self, media)` (L79-80)

### fn `def __get_engine(self, engine_name)` `priv` (L142-143)

### fn `def __get_requested_languages(self)` `priv` (L169-170)

### fn `def __get_title_for_language(self, media, lang)` `priv` (L181-182)

### fn `def __get_lang_tag(self, indexer_language, lang)` `priv` (L203-204)

### fn `def __build_query(self, *parts)` `priv` (L218-219)

### fn `def __build_query_keep_dash(self, *parts)` `priv` (L229-230)

### fn `async def __search_torrents(self, media, indexer, search_string, category)` `priv` (L244-245)

### fn `def __log_query_result(` `priv` (L263-269)

### fn `async def __search_movie_indexer(self, movie, indexer)` `priv` (L292-293)

### fn `async def __search_series_indexer(self, series, indexer)` `priv` (L361-362)

### fn `def __get_indexers(self)` `priv` (L455-456)

### fn `def __get_indexer_from_engines(self, engines)` `priv` (L471-472)

### fn `def __get_torrents_from_list_of_dicts(self, media, indexer, list_of_dicts)` `priv` (L515-516)

### fn `def __is_magnet_link(self, link)` `priv` (L549-550)

### fn `def __extract_info_hash(self, magnet_link)` `priv` (L558-559)

### fn `async def __post_process_result(self, indexers, result, media)` `priv` (L578-579)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SEARCHE_FALL_BACK`|var|pub|43||
|`SearchService`|class|pub|45-46|class SearchService|
|`__init__`|fn|priv|49-50|def __init__(self, config)|
|`search`|fn|pub|79-80|async def search(self, media)|
|`__get_engine`|fn|priv|142-143|def __get_engine(self, engine_name)|
|`__get_requested_languages`|fn|priv|169-170|def __get_requested_languages(self)|
|`__get_title_for_language`|fn|priv|181-182|def __get_title_for_language(self, media, lang)|
|`__get_lang_tag`|fn|priv|203-204|def __get_lang_tag(self, indexer_language, lang)|
|`__build_query`|fn|priv|218-219|def __build_query(self, *parts)|
|`__build_query_keep_dash`|fn|priv|229-230|def __build_query_keep_dash(self, *parts)|
|`__search_torrents`|fn|priv|244-245|async def __search_torrents(self, media, indexer, search_...|
|`__log_query_result`|fn|priv|263-269|def __log_query_result(|
|`__search_movie_indexer`|fn|priv|292-293|async def __search_movie_indexer(self, movie, indexer)|
|`__search_series_indexer`|fn|priv|361-362|async def __search_series_indexer(self, series, indexer)|
|`__get_indexers`|fn|priv|455-456|def __get_indexers(self)|
|`__get_indexer_from_engines`|fn|priv|471-472|def __get_indexer_from_engines(self, engines)|
|`__get_torrents_from_list_of_dicts`|fn|priv|515-516|def __get_torrents_from_list_of_dicts(self, media, indexe...|
|`__is_magnet_link`|fn|priv|549-550|def __is_magnet_link(self, link)|
|`__extract_info_hash`|fn|priv|558-559|def __extract_info_hash(self, magnet_link)|
|`__post_process_result`|fn|priv|578-579|async def __post_process_result(self, indexers, result, m...|


---

# base_plugin.py | Python | 61L | 5 symbols | 1 imports | 8 comments
> Path: `src/debriddo/search/plugins/base_plugin.py`

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class BasePlugin` (L12-61)
- Brief: Class `BasePlugin` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `login` operational logic. Execute `search` operational logic. Execute `download_torrent` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `login`. session Runtime input parameter consumed by `login`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`. self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L17-28)
  - Brief: Class `BasePlugin` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def login(self, session=None) -> bool | None` (L29-39)
  - Brief: Execute `login` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `login`. session Runtime input parameter consumed by `login`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L40-51)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L52-61)
  - Brief: Execute `download_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BasePlugin`|class|pub|12-61|class BasePlugin|
|`BasePlugin.__init__`|fn|priv|17-28|def __init__(self, config)|
|`BasePlugin.login`|fn|pub|29-39|async def login(self, session=None) -> bool | None|
|`BasePlugin.search`|fn|pub|40-51|async def search(self, what, cat='all')|
|`BasePlugin.download_torrent`|fn|pub|52-61|async def download_torrent(self, info)|


---

# ilcorsaroblu.py | Python | 354L | 7 symbols | 6 imports | 37 comments
> Path: `src/debriddo/search/plugins/ilcorsaroblu.py`

## Imports
```
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
from urllib.parse import quote
```

## Definitions

### class `class ilcorsaroblu(BasePlugin)` : BasePlugin (L20-219)
- Brief: Class `ilcorsaroblu` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `__extract_info_hash` operational logic. Execute `__generate_magnet_link` operational logic. Execute `login` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Parses ilCorSaRo Blu detail page HTML and extracts tuple `(info_hash, normalized_name)` when both fields are available. Builds a magnet URI from info hash and optional display name plus tracker list. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `__extract_info_hash`. html_content Runtime input parameter consumed by `__extract_info_hash`. suffix_to_remove Runtime input parameter consumed by `__extract_info_hash`. self Runtime input parameter consumed by `__generate_magnet_link`. info_hash Runtime input parameter consumed by `__generate_magnet_link`. name Runtime input parameter consumed by `__generate_magnet_link`. tracker_urls Runtime input parameter consumed by `__generate_magnet_link`. self Runtime input parameter consumed by `login`. session Runtime input parameter consumed by `login`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when required nodes are missing. @side_effect No external side effects. Computed result payload containing the generated magnet URI. @side_effect No external side effects. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L125-140)
  - Brief: Execute `__init__` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def __extract_info_hash(self, html_content, suffix_to_remove=" - il CorSaRo Blu")` `priv` (L141-173)
  - Brief: Execute `__extract_info_hash` operational logic.
  - Details: Parses ilCorSaRo Blu detail page HTML and extracts tuple `(info_hash, normalized_name)` when both fields are available.
  - Param: self Runtime input parameter consumed by `__extract_info_hash`. html_content Runtime input parameter consumed by `__extract_info_hash`. suffix_to_remove Runtime input parameter consumed by `__extract_info_hash`.
  - Return: Computed result payload; `None` when required nodes are missing. @side_effect No external side effects.
- fn `async def __generate_magnet_link(self, info_hash, name=None, tracker_urls=None)` `priv` (L174-203)
  - Brief: Execute `__generate_magnet_link` operational logic.
  - Details: Builds a magnet URI from info hash and optional display name plus tracker list.
  - Param: self Runtime input parameter consumed by `__generate_magnet_link`. info_hash Runtime input parameter consumed by `__generate_magnet_link`. name Runtime input parameter consumed by `__generate_magnet_link`. tracker_urls Runtime input parameter consumed by `__generate_magnet_link`.
  - Return: Computed result payload containing the generated magnet URI. @side_effect No external side effects.

### fn `async def login(self, session=None)` (L204-232)
- Brief: Execute `login` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `login`. session Runtime input parameter consumed by `login`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def download_torrent(self,info)` (L233-269)
- Brief: Execute `download_torrent` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def search(self,what,cat='all')` (L270-354)
- Brief: Execute `search` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ilcorsaroblu`|class|pub|20-219|class ilcorsaroblu(BasePlugin)|
|`ilcorsaroblu.__init__`|fn|priv|125-140|def __init__(self, config)|
|`ilcorsaroblu.__extract_info_hash`|fn|priv|141-173|async def __extract_info_hash(self, html_content, suffix_...|
|`ilcorsaroblu.__generate_magnet_link`|fn|priv|174-203|async def __generate_magnet_link(self, info_hash, name=No...|
|`login`|fn|pub|204-232|async def login(self, session=None)|
|`download_torrent`|fn|pub|233-269|async def download_torrent(self,info)|
|`search`|fn|pub|270-354|async def search(self,what,cat='all')|


---

# ilcorsaronero.py | Python | 167L | 7 symbols | 5 imports | 16 comments
> Path: `src/debriddo/search/plugins/ilcorsaronero.py`

## Imports
```
import re
from urllib.parse import quote_plus
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class ilcorsaronero(BasePlugin)` : BasePlugin (L21-167)
- Brief: Class `ilcorsaronero` encapsulates cohesive runtime behavior. Class `HTMLParser` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `feed` operational logic. Execute `__findTorrents` operational logic. Execute `download_torrent` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `feed`. html Runtime input parameter consumed by `feed`. self Runtime input parameter consumed by `__findTorrents`. html Runtime input parameter consumed by `__findTorrents`. self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L114-137)
  - Brief: Execute `download_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L138-167)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### class `class HTMLParser` (L39-113)
- Brief: Class `HTMLParser` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `feed` operational logic. Execute `__findTorrents` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `feed`. html Runtime input parameter consumed by `feed`. self Runtime input parameter consumed by `__findTorrents`. html Runtime input parameter consumed by `__findTorrents`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L45-56)
  - Brief: Class `HTMLParser` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def feed(self, html)` (L57-83)
  - Brief: Execute `feed` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `feed`. html Runtime input parameter consumed by `feed`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __findTorrents(self, html)` `priv` (L84-113)
  - Brief: Execute `__findTorrents` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__findTorrents`. html Runtime input parameter consumed by `__findTorrents`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ilcorsaronero`|class|pub|21-167|class ilcorsaronero(BasePlugin)|
|`HTMLParser`|class|pub|39-113|class HTMLParser|
|`HTMLParser.__init__`|fn|priv|45-56|def __init__(self, url)|
|`HTMLParser.feed`|fn|pub|57-83|def feed(self, html)|
|`HTMLParser.__findTorrents`|fn|priv|84-113|def __findTorrents(self, html)|
|`ilcorsaronero.download_torrent`|fn|pub|114-137|async def download_torrent(self, info)|
|`ilcorsaronero.search`|fn|pub|138-167|async def search(self, what, cat='all')|


---

# limetorrents.py | Python | 230L | 9 symbols | 8 imports | 18 comments
> Path: `src/debriddo/search/plugins/limetorrents.py`

## Imports
```
import re
import ssl
from datetime import datetime, timedelta
from html.parser import HTMLParser
from urllib.parse import quote
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class limetorrents(BasePlugin)` : BasePlugin (L28-227)
- Brief: Class `limetorrents` encapsulates cohesive runtime behavior. Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic. Execute `__init__` operational logic. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `handle_endtag` operational logic. Execute `download_torrent` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Specialized HTML parser collecting torrent entries from LimeTorrents search result rows. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`. self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`. self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L178-201)
  - Brief: Execute `download_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L45-177)
- Brief: Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic. Execute `__init__` operational logic. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `handle_endtag` operational logic.
- Details: Specialized HTML parser collecting torrent entries from LimeTorrents search result rows. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`. self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def error(self, message)` (L51-61)
  - Brief: Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic.
  - Details: Specialized HTML parser collecting torrent entries from LimeTorrents search result rows. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L64-93)
  - Brief: Execute `__init__` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L94-134)
  - Brief: Execute `handle_starttag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_data(self, data)` (L135-157)
  - Brief: Execute `handle_data` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L158-177)
  - Brief: Execute `handle_endtag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def search(self, what, cat='all')` (L202-230)
- Brief: Execute `search` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`limetorrents`|class|pub|28-227|class limetorrents(BasePlugin)|
|`MyHtmlParser`|class|pub|45-177|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|51-61|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|64-93|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|94-134|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|135-157|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|158-177|def handle_endtag(self, tag)|
|`limetorrents.download_torrent`|fn|pub|178-201|async def download_torrent(self, info)|
|`search`|fn|pub|202-230|async def search(self, what, cat='all')|


---

# one337x.py | Python | 233L | 9 symbols | 6 imports | 42 comments
> Path: `src/debriddo/search/plugins/one337x.py`

## Imports
```
import re
from html.parser import HTMLParser
from urllib.parse import quote_plus
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class one337x(BasePlugin)` : BasePlugin (L41-233)
- Brief: Class `one337x` encapsulates cohesive runtime behavior. Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic. Execute `__init__` operational logic. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `handle_endtag` operational logic. Execute `download_torrent` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`. self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`. self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L182-204)
  - Brief: Execute `download_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L205-233)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L60-181)
- Brief: Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic. Execute `__init__` operational logic. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `handle_endtag` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`. self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def error(self, message)` (L66-76)
  - Brief: Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L79-101)
  - Brief: Execute `__init__` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L102-147)
  - Brief: Execute `handle_starttag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_data(self, data)` (L148-162)
  - Brief: Execute `handle_data` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L163-181)
  - Brief: Execute `handle_endtag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`one337x`|class|pub|41-233|class one337x(BasePlugin)|
|`MyHtmlParser`|class|pub|60-181|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|66-76|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|79-101|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|102-147|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|148-162|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|163-181|def handle_endtag(self, tag)|
|`one337x.download_torrent`|fn|pub|182-204|async def download_torrent(self, info)|
|`one337x.search`|fn|pub|205-233|async def search(self, what, cat='all')|


---

# thepiratebay_categories.py | Python | 191L | 4 symbols | 7 imports | 18 comments
> Path: `src/debriddo/search/plugins/thepiratebay_categories.py`

## Imports
```
import json
import urllib.parse
from urllib.parse import quote
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class thepiratebay(BasePlugin)` : BasePlugin (L24-56)
- Brief: Class `thepiratebay` encapsulates cohesive runtime behavior.
- Details: Generated Doxygen block for class-level contract and extension boundaries.

### fn `async def download_torrent(self,info)` (L114-142)
- Brief: Execute `download_torrent` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def search(self,what,cat='all')` (L143-170)
- Brief: Execute `search` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def parseJSON(self,collection)` (L171-191)
- Brief: Execute `parseJSON` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `parseJSON`. collection Runtime input parameter consumed by `parseJSON`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`thepiratebay`|class|pub|24-56|class thepiratebay(BasePlugin)|
|`download_torrent`|fn|pub|114-142|async def download_torrent(self,info)|
|`search`|fn|pub|143-170|async def search(self,what,cat='all')|
|`parseJSON`|fn|pub|171-191|def parseJSON(self,collection)|


---

# therarbg.py | Python | 303L | 11 symbols | 6 imports | 40 comments
> Path: `src/debriddo/search/plugins/therarbg.py`

## Imports
```
import re
from html.parser import HTMLParser
from urllib.parse import quote
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class therarbg(BasePlugin)` : BasePlugin (L42-241)
- Brief: Class `therarbg` encapsulates cohesive runtime behavior. Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic. Execute `__init__` operational logic. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `handle_endtag` operational logic. Execute `download_torrent` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`. self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`. self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self, info)` (L217-238)
  - Brief: Execute `download_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### class `class MyHtmlParser(HTMLParser)` : HTMLParser (L66-216)
- Brief: Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic. Execute `__init__` operational logic. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `handle_endtag` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`. self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def error(self, message)` (L72-82)
  - Brief: Class `MyHtmlParser` encapsulates cohesive runtime behavior. Execute `error` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `error`. message Runtime input parameter consumed by `error`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L85-113)
  - Brief: Execute `__init__` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L114-165)
  - Brief: Execute `handle_starttag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_data(self, data)` (L166-195)
  - Brief: Execute `handle_data` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L196-216)
  - Brief: Execute `handle_endtag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def getPageUrl(self, what, cat, page)` (L239-254)
- Brief: Execute `getPageUrl` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `getPageUrl`. what Runtime input parameter consumed by `getPageUrl`. cat Runtime input parameter consumed by `getPageUrl`. page Runtime input parameter consumed by `getPageUrl`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def page_search(self, session, page, what, cat)` (L255-280)
- Brief: Execute `page_search` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `page_search`. session Runtime input parameter consumed by `page_search`. page Runtime input parameter consumed by `page_search`. what Runtime input parameter consumed by `page_search`. cat Runtime input parameter consumed by `page_search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def search(self, what, cat = 'all')` (L281-303)
- Brief: Execute `search` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`therarbg`|class|pub|42-241|class therarbg(BasePlugin)|
|`MyHtmlParser`|class|pub|66-216|class MyHtmlParser(HTMLParser)|
|`MyHtmlParser.error`|fn|pub|72-82|def error(self, message)|
|`MyHtmlParser.__init__`|fn|priv|85-113|def __init__(self, url)|
|`MyHtmlParser.handle_starttag`|fn|pub|114-165|def handle_starttag(self, tag, attrs)|
|`MyHtmlParser.handle_data`|fn|pub|166-195|def handle_data(self, data)|
|`MyHtmlParser.handle_endtag`|fn|pub|196-216|def handle_endtag(self, tag)|
|`therarbg.download_torrent`|fn|pub|217-238|async def download_torrent(self, info)|
|`getPageUrl`|fn|pub|239-254|def getPageUrl(self, what, cat, page)|
|`page_search`|fn|pub|255-280|async def page_search(self, session, page, what, cat)|
|`search`|fn|pub|281-303|async def search(self, what, cat = 'all')|


---

# torrentgalaxyone.py | Python | 148L | 3 symbols | 6 imports | 18 comments
> Path: `src/debriddo/search/plugins/torrentgalaxyone.py`

## Imports
```
from urllib.parse import quote
from bs4 import BeautifulSoup
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class torrentgalaxy(BasePlugin)` : BasePlugin (L23-148)
- Brief: Class `torrentgalaxy` encapsulates cohesive runtime behavior. Execute `download_torrent` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent(self,info)` (L52-81)
  - Brief: Execute `download_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self,what,cat='all')` (L82-148)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentgalaxy`|class|pub|23-148|class torrentgalaxy(BasePlugin)|
|`torrentgalaxy.download_torrent`|fn|pub|52-81|async def download_torrent(self,info)|
|`torrentgalaxy.search`|fn|pub|82-148|async def search(self,what,cat='all')|


---

# torrentgalaxyto.py | Python | 208L | 7 symbols | 9 imports | 31 comments
> Path: `src/debriddo/search/plugins/torrentgalaxyto.py`

## Imports
```
import asyncio
import math
import re
import time
from html.parser import HTMLParser
from urllib.parse import quote_plus
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

- var `SITE_URL = "https://torrentgalaxy.to/"` (L46)
- Brief: Exported constant `SITE_URL` used by runtime workflows.
### class `class torrentgalaxy(BasePlugin)` : BasePlugin (L48-205)
- Brief: Class `torrentgalaxy` encapsulates cohesive runtime behavior. Class `TorrentGalaxyParser` encapsulates cohesive runtime behavior. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic. Execute `do_search` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `do_search`. session Runtime input parameter consumed by `do_search`. url Runtime input parameter consumed by `do_search`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def do_search(self, session, url)` (L153-167)
  - Brief: Execute `do_search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `do_search`. session Runtime input parameter consumed by `do_search`. url Runtime input parameter consumed by `do_search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L168-205)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### class `class TorrentGalaxyParser(HTMLParser)` : HTMLParser (L69-152)
- Brief: Class `TorrentGalaxyParser` encapsulates cohesive runtime behavior. Execute `handle_starttag` operational logic. Execute `handle_data` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L80-130)
  - Brief: Execute `handle_starttag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_data(self, data)` (L131-152)
  - Brief: Execute `handle_data` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`SITE_URL`|var|pub|46||
|`torrentgalaxy`|class|pub|48-205|class torrentgalaxy(BasePlugin)|
|`TorrentGalaxyParser`|class|pub|69-152|class TorrentGalaxyParser(HTMLParser)|
|`TorrentGalaxyParser.handle_starttag`|fn|pub|80-130|def handle_starttag(self, tag, attrs)|
|`TorrentGalaxyParser.handle_data`|fn|pub|131-152|def handle_data(self, data)|
|`torrentgalaxy.do_search`|fn|pub|153-167|async def do_search(self, session, url)|
|`torrentgalaxy.search`|fn|pub|168-205|async def search(self, what, cat='all')|


---

# torrentproject.py | Python | 216L | 9 symbols | 6 imports | 28 comments
> Path: `src/debriddo/search/plugins/torrentproject.py`

## Imports
```
import re
from html.parser import HTMLParser
from urllib.parse import quote_plus, unquote
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class torrentproject(BasePlugin)` : BasePlugin (L23-184)
- Brief: Class `torrentproject` encapsulates cohesive runtime behavior. Class `MyHTMLParser` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `get_single_data` operational logic. Execute `handle_starttag` operational logic. Execute `handle_endtag` operational logic. Execute `handle_data` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `get_single_data`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L165-184)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### class `class MyHTMLParser(HTMLParser)` : HTMLParser (L34-164)
- Brief: Class `MyHTMLParser` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `get_single_data` operational logic. Execute `handle_starttag` operational logic. Execute `handle_endtag` operational logic. Execute `handle_data` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `get_single_data`. self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`. self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`. self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, url)` `priv` (L40-66)
  - Brief: Class `MyHTMLParser` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. url Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_single_data(self)` (L67-85)
  - Brief: Execute `get_single_data` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_single_data`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_starttag(self, tag, attrs)` (L86-110)
  - Brief: Execute `handle_starttag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_starttag`. tag Runtime input parameter consumed by `handle_starttag`. attrs Runtime input parameter consumed by `handle_starttag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_endtag(self, tag)` (L111-145)
  - Brief: Execute `handle_endtag` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_endtag`. tag Runtime input parameter consumed by `handle_endtag`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def handle_data(self, data)` (L146-164)
  - Brief: Execute `handle_data` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `handle_data`. data Runtime input parameter consumed by `handle_data`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def download_torrent(self, info)` (L197-216)
- Brief: Execute `download_torrent` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `download_torrent`. info Runtime input parameter consumed by `download_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentproject`|class|pub|23-184|class torrentproject(BasePlugin)|
|`MyHTMLParser`|class|pub|34-164|class MyHTMLParser(HTMLParser)|
|`MyHTMLParser.__init__`|fn|priv|40-66|def __init__(self, url)|
|`MyHTMLParser.get_single_data`|fn|pub|67-85|def get_single_data(self)|
|`MyHTMLParser.handle_starttag`|fn|pub|86-110|def handle_starttag(self, tag, attrs)|
|`MyHTMLParser.handle_endtag`|fn|pub|111-145|def handle_endtag(self, tag)|
|`MyHTMLParser.handle_data`|fn|pub|146-164|def handle_data(self, data)|
|`torrentproject.search`|fn|pub|165-184|async def search(self, what, cat='all')|
|`download_torrent`|fn|pub|197-216|async def download_torrent(self, info)|


---

# torrentz.py | Python | 121L | 3 symbols | 6 imports | 16 comments
> Path: `src/debriddo/search/plugins/torrentz.py`

## Imports
```
import urllib.parse
from urllib.parse import quote
from bs4 import BeautifulSoup
from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
from debriddo.utils.novaprinter import PrettyPrint
```

## Definitions

### class `class torrentz(BasePlugin)` : BasePlugin (L23-121)
- Brief: Class `torrentz` encapsulates cohesive runtime behavior. Execute `__parseHTML` operational logic. Execute `search` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__parseHTML`. html Runtime input parameter consumed by `__parseHTML`. self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __parseHTML(self, html)` `priv` (L39-99)
  - Brief: Execute `__parseHTML` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__parseHTML`. html Runtime input parameter consumed by `__parseHTML`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def search(self, what, cat='all')` (L100-121)
  - Brief: Execute `search` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `search`. what Runtime input parameter consumed by `search`. cat Runtime input parameter consumed by `search`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`torrentz`|class|pub|23-121|class torrentz(BasePlugin)|
|`torrentz.__parseHTML`|fn|priv|39-99|def __parseHTML(self, html)|
|`torrentz.search`|fn|pub|100-121|async def search(self, what, cat='all')|


---

# cinemeta.py | Python | 62L | 2 symbols | 4 imports | 6 comments
> Path: `src/debriddo/metdata/cinemeta.py`

## Imports
```
from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class Cinemeta(MetadataProvider)` : MetadataProvider (L17-62)
- Brief: Class `Cinemeta` encapsulates cohesive runtime behavior. Execute `get_metadata` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `get_metadata`. id Runtime input parameter consumed by `get_metadata`. type Runtime input parameter consumed by `get_metadata`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_metadata(self, id, type)` (L23-62)
  - Brief: Class `Cinemeta` encapsulates cohesive runtime behavior. Execute `get_metadata` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_metadata`. id Runtime input parameter consumed by `get_metadata`. type Runtime input parameter consumed by `get_metadata`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Cinemeta`|class|pub|17-62|class Cinemeta(MetadataProvider)|
|`Cinemeta.get_metadata`|fn|pub|23-62|async def get_metadata(self, id, type)|


---

# metadata_provider_base.py | Python | 74L | 4 symbols | 1 imports | 8 comments
> Path: `src/debriddo/metdata/metadata_provider_base.py`

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class MetadataProvider` (L13-74)
- Brief: Class `MetadataProvider` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `replace_weird_characters` operational logic. Execute `get_metadata` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `replace_weird_characters`. string Runtime input parameter consumed by `replace_weird_characters`. self Runtime input parameter consumed by `get_metadata`. id Runtime input parameter consumed by `get_metadata`. type Runtime input parameter consumed by `get_metadata`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L19-31)
  - Brief: Class `MetadataProvider` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def replace_weird_characters(self, string)` (L32-63)
  - Brief: Execute `replace_weird_characters` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `replace_weird_characters`. string Runtime input parameter consumed by `replace_weird_characters`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_metadata(self, id, type)` (L64-74)
  - Brief: Execute `get_metadata` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_metadata`. id Runtime input parameter consumed by `get_metadata`. type Runtime input parameter consumed by `get_metadata`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MetadataProvider`|class|pub|13-74|class MetadataProvider|
|`MetadataProvider.__init__`|fn|priv|19-31|def __init__(self, config)|
|`MetadataProvider.replace_weird_characters`|fn|pub|32-63|def replace_weird_characters(self, string)|
|`MetadataProvider.get_metadata`|fn|pub|64-74|async def get_metadata(self, id, type)|


---

# tmdb.py | Python | 72L | 2 symbols | 4 imports | 6 comments
> Path: `src/debriddo/metdata/tmdb.py`

## Imports
```
from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class TMDB(MetadataProvider)` : MetadataProvider (L16-72)
- Brief: Class `TMDB` encapsulates cohesive runtime behavior. Execute `get_metadata` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `get_metadata`. id Runtime input parameter consumed by `get_metadata`. type Runtime input parameter consumed by `get_metadata`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_metadata(self, id, type)` (L22-72)
  - Brief: Class `TMDB` encapsulates cohesive runtime behavior. Execute `get_metadata` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_metadata`. id Runtime input parameter consumed by `get_metadata`. type Runtime input parameter consumed by `get_metadata`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TMDB`|class|pub|16-72|class TMDB(MetadataProvider)|
|`TMDB.get_metadata`|fn|pub|22-72|async def get_metadata(self, id, type)|


---

# alldebrid.py | Python | 246L | 10 symbols | 6 imports | 21 comments
> Path: `src/debriddo/debrid/alldebrid.py`

## Imports
```
import uuid
from urllib.parse import unquote
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class AllDebrid(BaseDebrid)` : BaseDebrid (L22-221)
- Brief: Class `AllDebrid` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `add_magnet` operational logic. Execute `add_torrent` operational logic. Execute `check_magnet_status` operational logic. Execute `unrestrict_link` operational logic. Execute `get_stream_link` operational logic. Execute `is_ready` operational logic. Execute `get_availability_bulk` operational logic. Execute `__add_magnet_or_torrent` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`. self Runtime input parameter consumed by `add_torrent`. torrent_file Runtime input parameter consumed by `add_torrent`. ip Runtime input parameter consumed by `add_torrent`. self Runtime input parameter consumed by `check_magnet_status`. id Runtime input parameter consumed by `check_magnet_status`. ip Runtime input parameter consumed by `check_magnet_status`. self Runtime input parameter consumed by `unrestrict_link`. link Runtime input parameter consumed by `unrestrict_link`. ip Runtime input parameter consumed by `unrestrict_link`. self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`. self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`. self Runtime input parameter consumed by `__add_magnet_or_torrent`. magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. ip Runtime input parameter consumed by `__add_magnet_or_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L27-38)
  - Brief: Class `AllDebrid` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L39-51)
  - Brief: Execute `add_magnet` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_torrent(self, torrent_file, ip)` (L52-65)
  - Brief: Execute `add_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_torrent`. torrent_file Runtime input parameter consumed by `add_torrent`. ip Runtime input parameter consumed by `add_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def check_magnet_status(self, id, ip)` (L66-78)
  - Brief: Execute `check_magnet_status` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `check_magnet_status`. id Runtime input parameter consumed by `check_magnet_status`. ip Runtime input parameter consumed by `check_magnet_status`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def unrestrict_link(self, link, ip)` (L79-91)
  - Brief: Execute `unrestrict_link` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `unrestrict_link`. link Runtime input parameter consumed by `unrestrict_link`. ip Runtime input parameter consumed by `unrestrict_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_stream_link(self, query, ip=None)` (L92-179)
  - Brief: Execute `get_stream_link` operational logic. Execute `is_ready` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def is_ready()` (L109-120)
  - Brief: Execute `is_ready` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L180-209)
  - Brief: Execute `get_availability_bulk` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None, ip=None)` `priv` (L210-246)
- Brief: Execute `__add_magnet_or_torrent` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__add_magnet_or_torrent`. magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. ip Runtime input parameter consumed by `__add_magnet_or_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`AllDebrid`|class|pub|22-221|class AllDebrid(BaseDebrid)|
|`AllDebrid.__init__`|fn|priv|27-38|def __init__(self, config)|
|`AllDebrid.add_magnet`|fn|pub|39-51|async def add_magnet(self, magnet, ip=None)|
|`AllDebrid.add_torrent`|fn|pub|52-65|async def add_torrent(self, torrent_file, ip)|
|`AllDebrid.check_magnet_status`|fn|pub|66-78|async def check_magnet_status(self, id, ip)|
|`AllDebrid.unrestrict_link`|fn|pub|79-91|async def unrestrict_link(self, link, ip)|
|`AllDebrid.get_stream_link`|fn|pub|92-179|async def get_stream_link(self, query, ip=None)|
|`AllDebrid.is_ready`|fn|pub|109-120|async def is_ready()|
|`AllDebrid.get_availability_bulk`|fn|pub|180-209|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`__add_magnet_or_torrent`|fn|priv|210-246|async def __add_magnet_or_torrent(self, magnet, torrent_d...|


---

# base_debrid.py | Python | 146L | 9 symbols | 3 imports | 15 comments
> Path: `src/debriddo/debrid/base_debrid.py`

## Imports
```
import asyncio
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
```

## Definitions

### class `class BaseDebrid` (L16-146)
- Brief: Class `BaseDebrid` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `wait_for_ready_status_async_func` operational logic. Execute `wait_for_ready_status_sync_func` operational logic. Execute `get_json_response` operational logic. Execute `download_torrent_file` operational logic. Execute `get_stream_link` operational logic. Execute `add_magnet` operational logic. Execute `get_availability_bulk` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `wait_for_ready_status_async_func`. check_status_func Runtime input parameter consumed by `wait_for_ready_status_async_func`. timeout Runtime input parameter consumed by `wait_for_ready_status_async_func`. interval Runtime input parameter consumed by `wait_for_ready_status_async_func`. self Runtime input parameter consumed by `wait_for_ready_status_sync_func`. check_status_func Runtime input parameter consumed by `wait_for_ready_status_sync_func`. timeout Runtime input parameter consumed by `wait_for_ready_status_sync_func`. interval Runtime input parameter consumed by `wait_for_ready_status_sync_func`. self Runtime input parameter consumed by `get_json_response`. url Runtime input parameter consumed by `get_json_response`. **kwargs Runtime input parameter consumed by `get_json_response`. self Runtime input parameter consumed by `download_torrent_file`. download_url Runtime input parameter consumed by `download_torrent_file`. self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`. self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`. self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L21-32)
  - Brief: Class `BaseDebrid` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def wait_for_ready_status_async_func(self, check_status_func, timeout=30, interval=5)` (L33-54)
  - Brief: Execute `wait_for_ready_status_async_func` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `wait_for_ready_status_async_func`. check_status_func Runtime input parameter consumed by `wait_for_ready_status_async_func`. timeout Runtime input parameter consumed by `wait_for_ready_status_async_func`. interval Runtime input parameter consumed by `wait_for_ready_status_async_func`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def wait_for_ready_status_sync_func(self, check_status_func, timeout=30, interval=5)` (L55-77)
  - Brief: Execute `wait_for_ready_status_sync_func` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `wait_for_ready_status_sync_func`. check_status_func Runtime input parameter consumed by `wait_for_ready_status_sync_func`. timeout Runtime input parameter consumed by `wait_for_ready_status_sync_func`. interval Runtime input parameter consumed by `wait_for_ready_status_sync_func`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_json_response(self, url, **kwargs)` (L78-92)
  - Brief: Execute `get_json_response` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_json_response`. url Runtime input parameter consumed by `get_json_response`. **kwargs Runtime input parameter consumed by `get_json_response`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def download_torrent_file(self, download_url)` (L93-107)
  - Brief: Execute `download_torrent_file` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `download_torrent_file`. download_url Runtime input parameter consumed by `download_torrent_file`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_stream_link(self, query, ip=None)` (L108-120)
  - Brief: Execute `get_stream_link` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L121-133)
  - Brief: Execute `add_magnet` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L134-146)
  - Brief: Execute `get_availability_bulk` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`BaseDebrid`|class|pub|16-146|class BaseDebrid|
|`BaseDebrid.__init__`|fn|priv|21-32|def __init__(self, config)|
|`BaseDebrid.wait_for_ready_status_async_func`|fn|pub|33-54|async def wait_for_ready_status_async_func(self, check_st...|
|`BaseDebrid.wait_for_ready_status_sync_func`|fn|pub|55-77|async def wait_for_ready_status_sync_func(self, check_sta...|
|`BaseDebrid.get_json_response`|fn|pub|78-92|async def get_json_response(self, url, **kwargs)|
|`BaseDebrid.download_torrent_file`|fn|pub|93-107|async def download_torrent_file(self, download_url)|
|`BaseDebrid.get_stream_link`|fn|pub|108-120|async def get_stream_link(self, query, ip=None)|
|`BaseDebrid.add_magnet`|fn|pub|121-133|async def add_magnet(self, magnet, ip=None)|
|`BaseDebrid.get_availability_bulk`|fn|pub|134-146|async def get_availability_bulk(self, hashes_or_magnets, ...|


---

# get_debrid_service.py | Python | 39L | 1 symbols | 5 imports | 5 comments
> Path: `src/debriddo/debrid/get_debrid_service.py`

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
- Brief: Execute `get_debrid_service` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: config Runtime input parameter consumed by `get_debrid_service`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_debrid_service`|fn|pub|19-39|def get_debrid_service(config)|


---

# premiumize.py | Python | 220L | 10 symbols | 4 imports | 18 comments
> Path: `src/debriddo/debrid/premiumize.py`

## Imports
```
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import get_info_hash_from_magnet, season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class Premiumize(BaseDebrid)` : BaseDebrid (L21-220)
- Brief: Class `Premiumize` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `add_magnet` operational logic. Execute `add_torrent` operational logic. Execute `list_transfers` operational logic. Execute `get_folder_or_file_details` operational logic. Execute `get_availability` operational logic. Execute `get_availability_bulk` operational logic. Execute `get_stream_link` operational logic. Execute `is_ready` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`. self Runtime input parameter consumed by `add_torrent`. torrent_file Runtime input parameter consumed by `add_torrent`. self Runtime input parameter consumed by `list_transfers`. self Runtime input parameter consumed by `get_folder_or_file_details`. item_id Runtime input parameter consumed by `get_folder_or_file_details`. is_folder Runtime input parameter consumed by `get_folder_or_file_details`. self Runtime input parameter consumed by `get_availability`. hash Runtime input parameter consumed by `get_availability`. self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`. self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L26-37)
  - Brief: Class `Premiumize` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L38-51)
  - Brief: Execute `add_magnet` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_torrent(self, torrent_file)` (L53-65)
  - Brief: Execute `add_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_torrent`. torrent_file Runtime input parameter consumed by `add_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def list_transfers(self)` (L66-76)
  - Brief: Execute `list_transfers` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `list_transfers`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_folder_or_file_details(self, item_id, is_folder=True)` (L77-94)
  - Brief: Execute `get_folder_or_file_details` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_folder_or_file_details`. item_id Runtime input parameter consumed by `get_folder_or_file_details`. is_folder Runtime input parameter consumed by `get_folder_or_file_details`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_availability(self, hash)` (L95-106)
  - Brief: Execute `get_availability` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_availability`. hash Runtime input parameter consumed by `get_availability`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L107-120)
  - Brief: Execute `get_availability_bulk` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_stream_link(self, query, ip=None)` (L121-220)
  - Brief: Execute `get_stream_link` operational logic. Execute `is_ready` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def is_ready()` (L145-157)
  - Brief: Execute `is_ready` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Premiumize`|class|pub|21-220|class Premiumize(BaseDebrid)|
|`Premiumize.__init__`|fn|priv|26-37|def __init__(self, config)|
|`Premiumize.add_magnet`|fn|pub|38-51|async def add_magnet(self, magnet, ip=None)|
|`Premiumize.add_torrent`|fn|pub|53-65|async def add_torrent(self, torrent_file)|
|`Premiumize.list_transfers`|fn|pub|66-76|async def list_transfers(self)|
|`Premiumize.get_folder_or_file_details`|fn|pub|77-94|async def get_folder_or_file_details(self, item_id, is_fo...|
|`Premiumize.get_availability`|fn|pub|95-106|async def get_availability(self, hash)|
|`Premiumize.get_availability_bulk`|fn|pub|107-120|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`Premiumize.get_stream_link`|fn|pub|121-220|async def get_stream_link(self, query, ip=None)|
|`Premiumize.is_ready`|fn|pub|145-157|async def is_ready()|


---

# realdebrid.py | Python | 495L | 19 symbols | 9 imports | 40 comments
> Path: `src/debriddo/debrid/realdebrid.py`

## Imports
```
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

### class `class RealDebrid(BaseDebrid)` : BaseDebrid (L25-224)
- Brief: Class `RealDebrid` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `add_magnet` operational logic. Execute `add_torrent` operational logic. Execute `delete_torrent` operational logic. Execute `get_torrent_info` operational logic. Execute `select_files` operational logic. Execute `unrestrict_link` operational logic. Execute `is_already_added` operational logic. Execute `wait_for_link` operational logic. Execute `get_availability_bulk` operational logic. Execute `get_stream_link` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`. self Runtime input parameter consumed by `add_torrent`. torrent_file Runtime input parameter consumed by `add_torrent`. self Runtime input parameter consumed by `delete_torrent`. id Runtime input parameter consumed by `delete_torrent`. self Runtime input parameter consumed by `get_torrent_info`. torrent_id Runtime input parameter consumed by `get_torrent_info`. self Runtime input parameter consumed by `select_files`. torrent_id Runtime input parameter consumed by `select_files`. file_id Runtime input parameter consumed by `select_files`. self Runtime input parameter consumed by `unrestrict_link`. link Runtime input parameter consumed by `unrestrict_link`. self Runtime input parameter consumed by `is_already_added`. magnet Runtime input parameter consumed by `is_already_added`. self Runtime input parameter consumed by `wait_for_link`. torrent_id Runtime input parameter consumed by `wait_for_link`. timeout Runtime input parameter consumed by `wait_for_link`. interval Runtime input parameter consumed by `wait_for_link`. self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`. self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L30-42)
  - Brief: Class `RealDebrid` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L43-56)
  - Brief: Execute `add_magnet` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_torrent(self, torrent_file)` (L57-68)
  - Brief: Execute `add_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_torrent`. torrent_file Runtime input parameter consumed by `add_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def delete_torrent(self, id)` (L69-80)
  - Brief: Execute `delete_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `delete_torrent`. id Runtime input parameter consumed by `delete_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_torrent_info(self, torrent_id)` (L81-99)
  - Brief: Execute `get_torrent_info` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_torrent_info`. torrent_id Runtime input parameter consumed by `get_torrent_info`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def select_files(self, torrent_id, file_id)` (L100-116)
  - Brief: Execute `select_files` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `select_files`. torrent_id Runtime input parameter consumed by `select_files`. file_id Runtime input parameter consumed by `select_files`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def unrestrict_link(self, link)` (L117-129)
  - Brief: Execute `unrestrict_link` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `unrestrict_link`. link Runtime input parameter consumed by `unrestrict_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def is_already_added(self, magnet)` (L130-147)
  - Brief: Execute `is_already_added` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `is_already_added`. magnet Runtime input parameter consumed by `is_already_added`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def wait_for_link(self, torrent_id, timeout=30, interval=2)` (L148-167)
  - Brief: Execute `wait_for_link` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `wait_for_link`. torrent_id Runtime input parameter consumed by `wait_for_link`. timeout Runtime input parameter consumed by `wait_for_link`. interval Runtime input parameter consumed by `wait_for_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L168-193)
  - Brief: Execute `get_availability_bulk` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def get_stream_link(self, query, ip=None)` (L194-263)
- Brief: Execute `get_stream_link` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def __get_cached_torrent_ids(self, info_hash)` `priv` (L264-284)
- Brief: Execute `__get_cached_torrent_ids` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__get_cached_torrent_ids`. info_hash Runtime input parameter consumed by `__get_cached_torrent_ids`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def __get_cached_torrent_info(self, cached_ids, file_index, season, episode)` `priv` (L285-312)
- Brief: Execute `__get_cached_torrent_info` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__get_cached_torrent_info`. cached_ids Runtime input parameter consumed by `__get_cached_torrent_info`. file_index Runtime input parameter consumed by `__get_cached_torrent_info`. season Runtime input parameter consumed by `__get_cached_torrent_info`. episode Runtime input parameter consumed by `__get_cached_torrent_info`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __torrent_contains_file(self, torrent_info, file_index, season, episode)` `priv` (L313-338)
- Brief: Execute `__torrent_contains_file` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__torrent_contains_file`. torrent_info Runtime input parameter consumed by `__torrent_contains_file`. file_index Runtime input parameter consumed by `__torrent_contains_file`. season Runtime input parameter consumed by `__torrent_contains_file`. episode Runtime input parameter consumed by `__torrent_contains_file`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None)` `priv` (L339-377)
- Brief: Execute `__add_magnet_or_torrent` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__add_magnet_or_torrent`. magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def __prefetch_season_pack(self, magnet, torrent_download, timeout=30, interval=2)` `priv` (L378-406)
- Brief: Execute `__prefetch_season_pack` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__prefetch_season_pack`. magnet Runtime input parameter consumed by `__prefetch_season_pack`. torrent_download Runtime input parameter consumed by `__prefetch_season_pack`. timeout Runtime input parameter consumed by `__prefetch_season_pack`. interval Runtime input parameter consumed by `__prefetch_season_pack`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def __select_file(self, torrent_info, stream_type, file_index, season, episode)` `priv` (L407-450)
- Brief: Execute `__select_file` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__select_file`. torrent_info Runtime input parameter consumed by `__select_file`. stream_type Runtime input parameter consumed by `__select_file`. file_index Runtime input parameter consumed by `__select_file`. season Runtime input parameter consumed by `__select_file`. episode Runtime input parameter consumed by `__select_file`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __find_appropiate_link(self, torrent_info, links, file_index, season, episode)` `priv` (L451-495)
- Brief: Execute `__find_appropiate_link` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__find_appropiate_link`. torrent_info Runtime input parameter consumed by `__find_appropiate_link`. links Runtime input parameter consumed by `__find_appropiate_link`. file_index Runtime input parameter consumed by `__find_appropiate_link`. season Runtime input parameter consumed by `__find_appropiate_link`. episode Runtime input parameter consumed by `__find_appropiate_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`RealDebrid`|class|pub|25-224|class RealDebrid(BaseDebrid)|
|`RealDebrid.__init__`|fn|priv|30-42|def __init__(self, config)|
|`RealDebrid.add_magnet`|fn|pub|43-56|async def add_magnet(self, magnet, ip=None)|
|`RealDebrid.add_torrent`|fn|pub|57-68|async def add_torrent(self, torrent_file)|
|`RealDebrid.delete_torrent`|fn|pub|69-80|async def delete_torrent(self, id)|
|`RealDebrid.get_torrent_info`|fn|pub|81-99|async def get_torrent_info(self, torrent_id)|
|`RealDebrid.select_files`|fn|pub|100-116|async def select_files(self, torrent_id, file_id)|
|`RealDebrid.unrestrict_link`|fn|pub|117-129|async def unrestrict_link(self, link)|
|`RealDebrid.is_already_added`|fn|pub|130-147|async def is_already_added(self, magnet)|
|`RealDebrid.wait_for_link`|fn|pub|148-167|async def wait_for_link(self, torrent_id, timeout=30, int...|
|`RealDebrid.get_availability_bulk`|fn|pub|168-193|async def get_availability_bulk(self, hashes_or_magnets, ...|
|`get_stream_link`|fn|pub|194-263|async def get_stream_link(self, query, ip=None)|
|`__get_cached_torrent_ids`|fn|priv|264-284|async def __get_cached_torrent_ids(self, info_hash)|
|`__get_cached_torrent_info`|fn|priv|285-312|async def __get_cached_torrent_info(self, cached_ids, fil...|
|`__torrent_contains_file`|fn|priv|313-338|def __torrent_contains_file(self, torrent_info, file_inde...|
|`__add_magnet_or_torrent`|fn|priv|339-377|async def __add_magnet_or_torrent(self, magnet, torrent_d...|
|`__prefetch_season_pack`|fn|priv|378-406|async def __prefetch_season_pack(self, magnet, torrent_do...|
|`__select_file`|fn|priv|407-450|async def __select_file(self, torrent_info, stream_type, ...|
|`__find_appropiate_link`|fn|priv|451-495|def __find_appropiate_link(self, torrent_info, links, fil...|


---

# torbox.py | Python | 275L | 9 symbols | 6 imports | 26 comments
> Path: `src/debriddo/debrid/torbox.py`

## Imports
```
import time
import asyncio
from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TorBox(BaseDebrid)` : BaseDebrid (L22-221)
- Brief: Class `TorBox` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `wait_for_files` operational logic. Execute `add_magnet` operational logic. Execute `check_magnet_status` operational logic. Execute `get_file_download_link` operational logic. Execute `__add_magnet_or_torrent` operational logic. Execute `get_stream_link` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `wait_for_files`. torrent_hash Runtime input parameter consumed by `wait_for_files`. timeout Runtime input parameter consumed by `wait_for_files`. interval Runtime input parameter consumed by `wait_for_files`. self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`. self Runtime input parameter consumed by `check_magnet_status`. torrent_hash Runtime input parameter consumed by `check_magnet_status`. self Runtime input parameter consumed by `get_file_download_link`. torrent_id Runtime input parameter consumed by `get_file_download_link`. file_name Runtime input parameter consumed by `get_file_download_link`. self Runtime input parameter consumed by `__add_magnet_or_torrent`. magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`. self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L27-41)
  - Brief: Class `TorBox` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def wait_for_files(self, torrent_hash, timeout=30, interval=5)` (L42-67)
  - Brief: Execute `wait_for_files` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `wait_for_files`. torrent_hash Runtime input parameter consumed by `wait_for_files`. timeout Runtime input parameter consumed by `wait_for_files`. interval Runtime input parameter consumed by `wait_for_files`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def add_magnet(self, magnet, ip=None)` (L68-104)
  - Brief: Execute `add_magnet` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `add_magnet`. magnet Runtime input parameter consumed by `add_magnet`. ip Runtime input parameter consumed by `add_magnet`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def check_magnet_status(self, torrent_hash)` (L105-123)
  - Brief: Execute `check_magnet_status` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `check_magnet_status`. torrent_hash Runtime input parameter consumed by `check_magnet_status`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def get_file_download_link(self, torrent_id, file_name)` (L124-142)
  - Brief: Execute `get_file_download_link` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_file_download_link`. torrent_id Runtime input parameter consumed by `get_file_download_link`. file_name Runtime input parameter consumed by `get_file_download_link`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `async def __add_magnet_or_torrent(self, magnet, torrent_download=None)` `priv` (L143-161)
  - Brief: Execute `__add_magnet_or_torrent` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__add_magnet_or_torrent`. magnet Runtime input parameter consumed by `__add_magnet_or_torrent`. torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def get_stream_link(self, query, ip=None)` (L162-227)
- Brief: Execute `get_stream_link` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `get_stream_link`. query Runtime input parameter consumed by `get_stream_link`. ip Runtime input parameter consumed by `get_stream_link`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `async def get_availability_bulk(self, hashes_or_magnets, ip=None)` (L243-275)
- Brief: Execute `get_availability_bulk` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `get_availability_bulk`. hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`. ip Runtime input parameter consumed by `get_availability_bulk`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorBox`|class|pub|22-221|class TorBox(BaseDebrid)|
|`TorBox.__init__`|fn|priv|27-41|def __init__(self, config)|
|`TorBox.wait_for_files`|fn|pub|42-67|async def wait_for_files(self, torrent_hash, timeout=30, ...|
|`TorBox.add_magnet`|fn|pub|68-104|async def add_magnet(self, magnet, ip=None)|
|`TorBox.check_magnet_status`|fn|pub|105-123|async def check_magnet_status(self, torrent_hash)|
|`TorBox.get_file_download_link`|fn|pub|124-142|async def get_file_download_link(self, torrent_id, file_n...|
|`TorBox.__add_magnet_or_torrent`|fn|priv|143-161|async def __add_magnet_or_torrent(self, magnet, torrent_d...|
|`get_stream_link`|fn|pub|162-227|async def get_stream_link(self, query, ip=None)|
|`get_availability_bulk`|fn|pub|243-275|async def get_availability_bulk(self, hashes_or_magnets, ...|


---

# torrent_item.py | Python | 89L | 3 symbols | 5 imports | 7 comments
> Path: `src/debriddo/torrent/torrent_item.py`

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
- Brief: Class `TorrentItem` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `to_debrid_stream_query` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. raw_title Runtime input parameter consumed by `__init__`. title Runtime input parameter consumed by `__init__`. size Runtime input parameter consumed by `__init__`. magnet Runtime input parameter consumed by `__init__`. info_hash Runtime input parameter consumed by `__init__`. link Runtime input parameter consumed by `__init__`. seeders Runtime input parameter consumed by `__init__`. languages Runtime input parameter consumed by `__init__`. indexer Runtime input parameter consumed by `__init__`. engine_name Runtime input parameter consumed by `__init__`. privacy Runtime input parameter consumed by `__init__`. type Runtime input parameter consumed by `__init__`. parsed_data Runtime input parameter consumed by `__init__`. from_cache Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `to_debrid_stream_query`. media Runtime input parameter consumed by `to_debrid_stream_query`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, raw_title, title, size, magnet, info_hash, link, seeders, languages, indexer,` `priv` (L24-72)
  - Brief: Class `TorrentItem` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. raw_title Runtime input parameter consumed by `__init__`. title Runtime input parameter consumed by `__init__`. size Runtime input parameter consumed by `__init__`. magnet Runtime input parameter consumed by `__init__`. info_hash Runtime input parameter consumed by `__init__`. link Runtime input parameter consumed by `__init__`. seeders Runtime input parameter consumed by `__init__`. languages Runtime input parameter consumed by `__init__`. indexer Runtime input parameter consumed by `__init__`. engine_name Runtime input parameter consumed by `__init__`. privacy Runtime input parameter consumed by `__init__`. type Runtime input parameter consumed by `__init__`. parsed_data Runtime input parameter consumed by `__init__`. from_cache Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def to_debrid_stream_query(self, media: Media) -> dict` (L73-89)
  - Brief: Execute `to_debrid_stream_query` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `to_debrid_stream_query`. media Runtime input parameter consumed by `to_debrid_stream_query`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentItem`|class|pub|19-89|class TorrentItem|
|`TorrentItem.__init__`|fn|priv|24-72|def __init__(self, raw_title, title, size, magnet, info_h...|
|`TorrentItem.to_debrid_stream_query`|fn|pub|73-89|def to_debrid_stream_query(self, media: Media) -> dict|


---

# torrent_service.py | Python | 291L | 13 symbols | 12 imports | 43 comments
> Path: `src/debriddo/torrent/torrent_service.py`

## Imports
```
import hashlib
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

### class `class TorrentService` (L27-28)

### fn `def __init__(self)` `priv` (L31-32)
- Brief: Class `TorrentService` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

### fn `async def __process_web_url_or_process_magnet(self, result: SearchResult)` `priv` (L63-64)

### fn `async def convert_and_process(self, results: List[SearchResult])` (L80-81)

### fn `async def __process_web_url(self, result: TorrentItem)` `priv` (L97-98)

### fn `def __process_torrent(self, result: TorrentItem, torrent_file)` `priv` (L127-128)

### fn `def __process_magnet(self, result: TorrentItem)` `priv` (L163-164)

### fn `def __convert_torrent_to_hash(self, torrent_contents)` `priv` (L178-179)

### fn `def __build_magnet(self, hash, display_name, trackers)` `priv` (L187-188)

### fn `def __get_trackers_from_torrent(self, torrent_metadata)` `priv` (L202-203)

### fn `def __get_trackers_from_magnet(self, magnet: str)` `priv` (L228-229)

### fn `def __find_episode_file(self, file_structure, season, episode)` `priv` (L242-243)

### fn `def __find_movie_file(self, file_structure)` `priv` (L277-278)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TorrentService`|class|pub|27-28|class TorrentService|
|`__init__`|fn|priv|31-32|def __init__(self)|
|`__process_web_url_or_process_magnet`|fn|priv|63-64|async def __process_web_url_or_process_magnet(self, resul...|
|`convert_and_process`|fn|pub|80-81|async def convert_and_process(self, results: List[SearchR...|
|`__process_web_url`|fn|priv|97-98|async def __process_web_url(self, result: TorrentItem)|
|`__process_torrent`|fn|priv|127-128|def __process_torrent(self, result: TorrentItem, torrent_...|
|`__process_magnet`|fn|priv|163-164|def __process_magnet(self, result: TorrentItem)|
|`__convert_torrent_to_hash`|fn|priv|178-179|def __convert_torrent_to_hash(self, torrent_contents)|
|`__build_magnet`|fn|priv|187-188|def __build_magnet(self, hash, display_name, trackers)|
|`__get_trackers_from_torrent`|fn|priv|202-203|def __get_trackers_from_torrent(self, torrent_metadata)|
|`__get_trackers_from_magnet`|fn|priv|228-229|def __get_trackers_from_magnet(self, magnet: str)|
|`__find_episode_file`|fn|priv|242-243|def __find_episode_file(self, file_structure, season, epi...|
|`__find_movie_file`|fn|priv|277-278|def __find_movie_file(self, file_structure)|


---

# torrent_smart_container.py | Python | 368L | 16 symbols | 9 imports | 26 comments
> Path: `src/debriddo/torrent/torrent_smart_container.py`

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
- Brief: Class `TorrentSmartContainer` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `get_hashes` operational logic. Execute `get_items` operational logic. Execute `get_direct_torrentable` operational logic. Execute `get_best_matching` operational logic. Execute `cache_container_items` operational logic. Execute `__save_to_cache` operational logic. Execute `update_availability` operational logic. Execute `__update_availability_realdebrid` operational logic. Execute `__update_availability_alldebrid` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. torrent_items Runtime input parameter consumed by `__init__`. media Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `get_hashes`. self Runtime input parameter consumed by `get_items`. self Runtime input parameter consumed by `get_direct_torrentable`. self Runtime input parameter consumed by `get_best_matching`. self Runtime input parameter consumed by `cache_container_items`. self Runtime input parameter consumed by `__save_to_cache`. self Runtime input parameter consumed by `update_availability`. debrid_response Runtime input parameter consumed by `update_availability`. debrid_type Runtime input parameter consumed by `update_availability`. media Runtime input parameter consumed by `update_availability`. self Runtime input parameter consumed by `__update_availability_realdebrid`. response Runtime input parameter consumed by `__update_availability_realdebrid`. media Runtime input parameter consumed by `__update_availability_realdebrid`. self Runtime input parameter consumed by `__update_availability_alldebrid`. response Runtime input parameter consumed by `__update_availability_alldebrid`. media Runtime input parameter consumed by `__update_availability_alldebrid`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, torrent_items: List[TorrentItem], media)` `priv` (L31-44)
  - Brief: Class `TorrentSmartContainer` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. torrent_items Runtime input parameter consumed by `__init__`. media Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_hashes(self)` (L45-54)
  - Brief: Execute `get_hashes` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_hashes`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_items(self)` (L55-64)
  - Brief: Execute `get_items` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_items`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_direct_torrentable(self)` (L65-78)
  - Brief: Execute `get_direct_torrentable` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_direct_torrentable`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def get_best_matching(self)` (L79-103)
  - Brief: Execute `get_best_matching` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get_best_matching`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def cache_container_items(self)` (L104-117)
  - Brief: Execute `cache_container_items` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `cache_container_items`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __save_to_cache(self)` `priv` (L118-128)
  - Brief: Execute `__save_to_cache` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__save_to_cache`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def update_availability(self, debrid_response, debrid_type, media)` (L129-150)
  - Brief: Execute `update_availability` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `update_availability`. debrid_response Runtime input parameter consumed by `update_availability`. debrid_type Runtime input parameter consumed by `update_availability`. media Runtime input parameter consumed by `update_availability`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __update_availability_realdebrid(self, response, media)` `priv` (L151-197)
  - Brief: Execute `__update_availability_realdebrid` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__update_availability_realdebrid`. response Runtime input parameter consumed by `__update_availability_realdebrid`. media Runtime input parameter consumed by `__update_availability_realdebrid`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __update_availability_alldebrid(self, response, media)` `priv` (L198-223)
  - Brief: Execute `__update_availability_alldebrid` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__update_availability_alldebrid`. response Runtime input parameter consumed by `__update_availability_alldebrid`. media Runtime input parameter consumed by `__update_availability_alldebrid`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __update_availability_torbox(self, response, media)` `priv` (L224-251)
- Brief: Execute `__update_availability_torbox` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__update_availability_torbox`. response Runtime input parameter consumed by `__update_availability_torbox`. media Runtime input parameter consumed by `__update_availability_torbox`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __update_availability_premiumize(self, response)` `priv` (L252-270)
- Brief: Execute `__update_availability_premiumize` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__update_availability_premiumize`. response Runtime input parameter consumed by `__update_availability_premiumize`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __update_file_details(self, torrent_item, files)` `priv` (L271-289)
- Brief: Execute `__update_file_details` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__update_file_details`. torrent_item Runtime input parameter consumed by `__update_file_details`. files Runtime input parameter consumed by `__update_file_details`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __build_items_dict_by_infohash(self, items: List[TorrentItem])` `priv` (L290-308)
- Brief: Execute `__build_items_dict_by_infohash` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__build_items_dict_by_infohash`. items Runtime input parameter consumed by `__build_items_dict_by_infohash`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def __explore_folders(self, folder, files, file_index, type, season=None, episode=None)` `priv` (L310-368)
- Brief: Execute `__explore_folders` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__explore_folders`. folder Runtime input parameter consumed by `__explore_folders`. files Runtime input parameter consumed by `__explore_folders`. file_index Runtime input parameter consumed by `__explore_folders`. type Runtime input parameter consumed by `__explore_folders`. season Runtime input parameter consumed by `__explore_folders`. episode Runtime input parameter consumed by `__explore_folders`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

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

# async_httpx_session.py | Python | 350L | 17 symbols | 9 imports | 99 comments
> Path: `src/debriddo/utils/async_httpx_session.py`

## Imports
```
import gzip
import re
import socket
import tempfile
import html.entities
import httpx
import socks
import json
from debriddo.utils.logger import setup_logger
```

## Definitions

- var `DEFAULT_TIMEOUT = 20.0  # 20 secondi` (L21)
- Brief: Exported constant `DEFAULT_TIMEOUT` used by runtime workflows.
### class `class AsyncThreadSafeSession` (L23-24)

### fn `def __init__(self, proxy=None)` `priv` (L35-36)

### fn `async def close(self)` (L53-54)

### fn `async def __aenter__(self)` `priv` (L62-63)

### fn `async def __aexit__(self, exc_type, exc_val, exc_tb)` `priv` (L70-71)

### fn `def __del__(self)` `priv` (L79-80)

### fn `def _html_entity_decode(s)` `priv` `@staticmethod` (L92-93)

### fn `def entity2char(m)` (L99-110)
- Brief: Execute `entity2char` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: m Runtime input parameter consumed by `entity2char`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def _setup_proxy(self, proxy)` `priv` (L120-121)

### fn `async def request(self, method, url, **kwargs)` (L142-143)

### fn `async def request_get(self, url, **kwargs)` (L172-173)

### fn `async def request_post(self, url, **kwargs)` (L180-181)

### fn `async def retrieve_url(self, url)` (L217-218)

### fn `async def download_file(self, url, referer=None)` (L267-268)

### fn `async def get_json_response(self, url, **kwargs)` (L300-301)

### fn `async def download_torrent_file(self, download_url)` (L343-344)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`DEFAULT_TIMEOUT`|var|pub|21||
|`AsyncThreadSafeSession`|class|pub|23-24|class AsyncThreadSafeSession|
|`__init__`|fn|priv|35-36|def __init__(self, proxy=None)|
|`close`|fn|pub|53-54|async def close(self)|
|`__aenter__`|fn|priv|62-63|async def __aenter__(self)|
|`__aexit__`|fn|priv|70-71|async def __aexit__(self, exc_type, exc_val, exc_tb)|
|`__del__`|fn|priv|79-80|def __del__(self)|
|`_html_entity_decode`|fn|priv|92-93|def _html_entity_decode(s)|
|`entity2char`|fn|pub|99-110|def entity2char(m)|
|`_setup_proxy`|fn|priv|120-121|def _setup_proxy(self, proxy)|
|`request`|fn|pub|142-143|async def request(self, method, url, **kwargs)|
|`request_get`|fn|pub|172-173|async def request_get(self, url, **kwargs)|
|`request_post`|fn|pub|180-181|async def request_post(self, url, **kwargs)|
|`retrieve_url`|fn|pub|217-218|async def retrieve_url(self, url)|
|`download_file`|fn|pub|267-268|async def download_file(self, url, referer=None)|
|`get_json_response`|fn|pub|300-301|async def get_json_response(self, url, **kwargs)|
|`download_torrent_file`|fn|pub|343-344|async def download_torrent_file(self, download_url)|


---

# cache.py | Python | 328L | 3 symbols | 8 imports | 32 comments
> Path: `src/debriddo/utils/cache.py`

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

- var `TABLE_NAME = "cached_items"` (L20)
- Brief: Exported constant `TABLE_NAME` used by runtime workflows.
### fn `def search_cache(config, media)` (L61-62)

### fn `def cache_results(torrents: List[TorrentItem], media)` (L163-164)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TABLE_NAME`|var|pub|20||
|`search_cache`|fn|pub|61-62|def search_cache(config, media)|
|`cache_results`|fn|pub|163-164|def cache_results(torrents: List[TorrentItem], media)|


---

# detection.py | Python | 44L | 1 symbols | 1 imports | 5 comments
> Path: `src/debriddo/utils/detection.py`

## Imports
```
import re
```

## Definitions

### fn `def detect_languages(torrent_name)` (L13-44)
- Brief: Execute `detect_languages` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: torrent_name Runtime input parameter consumed by `detect_languages`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`detect_languages`|fn|pub|13-44|def detect_languages(torrent_name)|


---

# filter_results.py | Python | 470L | 10 symbols | 9 imports | 71 comments
> Path: `src/debriddo/utils/filter_results.py`

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
- Brief: Execute `_match_complete_season` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: raw_title Runtime input parameter consumed by `_match_complete_season`. numeric_season Runtime input parameter consumed by `_match_complete_season`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def _match_episode_range_pack(raw_title, numeric_season, numeric_episode)` `priv` (L107-132)
- Brief: Execute `_match_episode_range_pack` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: raw_title Runtime input parameter consumed by `_match_episode_range_pack`. numeric_season Runtime input parameter consumed by `_match_episode_range_pack`. numeric_episode Runtime input parameter consumed by `_match_episode_range_pack`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def _match_season_episode_pair(raw_title, numeric_season, numeric_episode)` `priv` (L133-154)
- Brief: Execute `_match_season_episode_pair` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: raw_title Runtime input parameter consumed by `_match_season_episode_pair`. numeric_season Runtime input parameter consumed by `_match_season_episode_pair`. numeric_episode Runtime input parameter consumed by `_match_season_episode_pair`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def _match_title_with_season(raw_title, media_title, numeric_season)` `priv` (L155-156)

### fn `def sort_quality(item)` (L208-236)
- Brief: Execute `sort_quality` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: item Runtime input parameter consumed by `sort_quality`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def items_sort(items, config)` (L237-297)
- Brief: Execute `items_sort` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: items Runtime input parameter consumed by `items_sort`. config Runtime input parameter consumed by `items_sort`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def filter_out_non_matching(items, season, episode)` (L314-350)
- Brief: Execute `filter_out_non_matching` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: items Runtime input parameter consumed by `filter_out_non_matching`. season Runtime input parameter consumed by `filter_out_non_matching`. episode Runtime input parameter consumed by `filter_out_non_matching`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def remove_non_matching_title(items, titles, media)` (L351-404)
- Brief: Execute `remove_non_matching_title` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: items Runtime input parameter consumed by `remove_non_matching_title`. titles Runtime input parameter consumed by `remove_non_matching_title`. media Runtime input parameter consumed by `remove_non_matching_title`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def filter_items(items, media, config)` (L405-457)
- Brief: Execute `filter_items` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: items Runtime input parameter consumed by `filter_items`. media Runtime input parameter consumed by `filter_items`. config Runtime input parameter consumed by `filter_items`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def sort_items(items, config)` (L458-470)
- Brief: Execute `sort_items` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: items Runtime input parameter consumed by `sort_items`. config Runtime input parameter consumed by `sort_items`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`_match_complete_season`|fn|priv|56-106|def _match_complete_season(raw_title, numeric_season)|
|`_match_episode_range_pack`|fn|priv|107-132|def _match_episode_range_pack(raw_title, numeric_season, ...|
|`_match_season_episode_pair`|fn|priv|133-154|def _match_season_episode_pair(raw_title, numeric_season,...|
|`_match_title_with_season`|fn|priv|155-156|def _match_title_with_season(raw_title, media_title, nume...|
|`sort_quality`|fn|pub|208-236|def sort_quality(item)|
|`items_sort`|fn|pub|237-297|def items_sort(items, config)|
|`filter_out_non_matching`|fn|pub|314-350|def filter_out_non_matching(items, season, episode)|
|`remove_non_matching_title`|fn|pub|351-404|def remove_non_matching_title(items, titles, media)|
|`filter_items`|fn|pub|405-457|def filter_items(items, media, config)|
|`sort_items`|fn|pub|458-470|def sort_items(items, config)|


---

# general.py | Python | 75L | 3 symbols | 2 imports | 7 comments
> Path: `src/debriddo/utils/general.py`

## Imports
```
from RTN import parse
from debriddo.utils.logger import setup_logger
```

## Definitions

### fn `def season_episode_in_filename(filename, season, episode)` (L24-39)
- Brief: Execute `season_episode_in_filename` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: filename Runtime input parameter consumed by `season_episode_in_filename`. season Runtime input parameter consumed by `season_episode_in_filename`. episode Runtime input parameter consumed by `season_episode_in_filename`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def get_info_hash_from_magnet(magnet: str)` (L40-62)
- Brief: Execute `get_info_hash_from_magnet` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: magnet Runtime input parameter consumed by `get_info_hash_from_magnet`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def is_video_file(filename)` (L63-75)
- Brief: Execute `is_video_file` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: filename Runtime input parameter consumed by `is_video_file`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`season_episode_in_filename`|fn|pub|24-39|def season_episode_in_filename(filename, season, episode)|
|`get_info_hash_from_magnet`|fn|pub|40-62|def get_info_hash_from_magnet(magnet: str)|
|`is_video_file`|fn|pub|63-75|def is_video_file(filename)|


---

# logger.py | Python | 110L | 16 symbols | 2 imports | 24 comments
> Path: `src/debriddo/utils/logger.py`

## Imports
```
import os
import logging
```

## Definitions

### class `class CustomFormatter(logging.Formatter)` : logging.Formatter (L14-15)

- var `WHITE = "\033[97m"` (L19)
- Brief: Class `CustomFormatter` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.
- var `WHITE_BOLD = "\033[1;97m"` (L20)
- var `GREY = "\033[90m"` (L21)
- var `LIGHT_GREY = "\033[37m"` (L22)
- var `CYAN = "\033[36m"` (L23)
- var `MAGENTA = "\033[35m"` (L24)
- var `BLUE = "\033[34m"` (L25)
- var `RED = "\033[31m"` (L26)
- var `GREEN = "\033[32m"` (L27)
- var `YELLOW = "\033[33m"` (L28)
- var `RED_BOLD = "\033[1;31m"` (L29)
- var `RESET = "\033[0m"` (L32)
- var `FORMATS = {` (L54)
### fn `def format(self, record)` (L62-63)

### fn `def setup_logger(name, debug=None)` (L72-73)

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CustomFormatter`|class|pub|14-15|class CustomFormatter(logging.Formatter)|
|`WHITE`|var|pub|19||
|`WHITE_BOLD`|var|pub|20||
|`GREY`|var|pub|21||
|`LIGHT_GREY`|var|pub|22||
|`CYAN`|var|pub|23||
|`MAGENTA`|var|pub|24||
|`BLUE`|var|pub|25||
|`RED`|var|pub|26||
|`GREEN`|var|pub|27||
|`YELLOW`|var|pub|28||
|`RED_BOLD`|var|pub|29||
|`RESET`|var|pub|32||
|`FORMATS`|var|pub|54||
|`format`|fn|pub|62-63|def format(self, record)|
|`setup_logger`|fn|pub|72-73|def setup_logger(name, debug=None)|


---

# multi_thread.py | Python | 30L | 2 symbols | 2 imports | 6 comments
> Path: `src/debriddo/utils/multi_thread.py`

## Imports
```
import asyncio
from debriddo.constants import RUN_IN_MULTI_THREAD
```

## Definitions

- var `MULTI_THREAD = RUN_IN_MULTI_THREAD` (L14)
- Brief: Exported constant `MULTI_THREAD` used by runtime workflows.
### fn `def run_coroutine_in_thread(coro)` (L17-30)
- Brief: Execute `run_coroutine_in_thread` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: coro Runtime input parameter consumed by `run_coroutine_in_thread`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`MULTI_THREAD`|var|pub|14||
|`run_coroutine_in_thread`|fn|pub|17-30|def run_coroutine_in_thread(coro)|


---

# novaprinter.py | Python | 113L | 6 symbols | 1 imports | 26 comments
> Path: `src/debriddo/utils/novaprinter.py`

## Imports
```
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class PrettyPrint` (L24-113)
- Brief: Class `PrettyPrint` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `__call__` operational logic. Execute `__anySizeToBytes` operational logic. Execute `get` operational logic. Execute `clear` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Converts a human-readable size token into integer byte units using binary prefixes. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `__call__`. dictionary Runtime input parameter consumed by `__call__`. self Runtime input parameter consumed by `__anySizeToBytes`. size_string Runtime input parameter consumed by `__anySizeToBytes`. self Runtime input parameter consumed by `get`. self Runtime input parameter consumed by `clear`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `-1` when parsing fails. @side_effect No external side effects. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self)` `priv` (L29-40)
  - Brief: Class `PrettyPrint` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __call__(self, dictionary): # *args, **kwargs)` `priv` (L41-56)
  - Brief: Execute `__call__` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__call__`. dictionary Runtime input parameter consumed by `__call__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __anySizeToBytes(self, size_string)` `priv` (L57-89)
  - Brief: Execute `__anySizeToBytes` operational logic.
  - Details: Converts a human-readable size token into integer byte units using binary prefixes.
  - Param: self Runtime input parameter consumed by `__anySizeToBytes`. size_string Runtime input parameter consumed by `__anySizeToBytes`.
  - Return: Computed result payload; `-1` when parsing fails. @side_effect No external side effects.
- fn `def get(self)` (L90-103)
  - Brief: Execute `get` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `get`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def clear(self)` (L104-113)
  - Brief: Execute `clear` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `clear`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`PrettyPrint`|class|pub|24-113|class PrettyPrint|
|`PrettyPrint.__init__`|fn|priv|29-40|def __init__(self)|
|`PrettyPrint.__call__`|fn|priv|41-56|def __call__(self, dictionary): # *args, **kwargs)|
|`PrettyPrint.__anySizeToBytes`|fn|priv|57-89|def __anySizeToBytes(self, size_string)|
|`PrettyPrint.get`|fn|pub|90-103|def get(self)|
|`PrettyPrint.clear`|fn|pub|104-113|def clear(self)|


---

# parse_config.py | Python | 57L | 3 symbols | 1 imports | 13 comments
> Path: `src/debriddo/utils/parse_config.py`

## Imports
```
from debriddo.utils.string_encoding import decode_lzstring, encode_lzstring
```

## Definitions

### fn `def parse_config(encoded_config)` (L14-28)
- Brief: Execute `parse_config` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: encoded_config Runtime input parameter consumed by `parse_config`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def parse_query(encoded_query)` (L30-43)
- Brief: Execute `parse_query` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: encoded_query Runtime input parameter consumed by `parse_query`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def encode_query(query)` (L45-57)
- Brief: Execute `encode_query` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: query Runtime input parameter consumed by `encode_query`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`parse_config`|fn|pub|14-28|def parse_config(encoded_config)|
|`parse_query`|fn|pub|30-43|def parse_query(encoded_query)|
|`encode_query`|fn|pub|45-57|def encode_query(query)|


---

# stremio_parser.py | Python | 237L | 8 symbols | 7 imports | 30 comments
> Path: `src/debriddo/utils/stremio_parser.py`

## Imports
```
import queue
import threading
from typing import List
from debriddo.models.media import Media
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
from debriddo.utils.parse_config import encode_query
```

## Definitions

### fn `def get_emoji(language)` (L22-46)
- Brief: Execute `get_emoji` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: language Runtime input parameter consumed by `get_emoji`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

- var `INSTANTLY_AVAILABLE = "[⚡"` (L48)
- Brief: Exported constant `INSTANTLY_AVAILABLE` used by runtime workflows.
- var `DOWNLOAD_REQUIRED = "[⬇️"` (L50)
- Brief: Exported constant `DOWNLOAD_REQUIRED` used by runtime workflows.
- var `DIRECT_TORRENT = "[🏴‍☠️"` (L52)
- Brief: Exported constant `DIRECT_TORRENT` used by runtime workflows.
### fn `def filter_by_availability(item)` (L55-68)
- Brief: Execute `filter_by_availability` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: item Runtime input parameter consumed by `filter_by_availability`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def filter_by_direct_torrnet(item)` (L69-82)
- Brief: Execute `filter_by_direct_torrnet` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: item Runtime input parameter consumed by `filter_by_direct_torrnet`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def parse_to_debrid_stream(torrent_item: TorrentItem, config_url, node_url, playtorrent, results: queue.Queue, media: Media)` (L83-200)
- Brief: Execute `parse_to_debrid_stream` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: torrent_item Runtime input parameter consumed by `parse_to_debrid_stream`. config_url Runtime input parameter consumed by `parse_to_debrid_stream`. node_url Runtime input parameter consumed by `parse_to_debrid_stream`. playtorrent Runtime input parameter consumed by `parse_to_debrid_stream`. results Runtime input parameter consumed by `parse_to_debrid_stream`. media Runtime input parameter consumed by `parse_to_debrid_stream`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def parse_to_stremio_streams(torrent_items: List[TorrentItem], config, config_url, node_url, media)` (L201-237)
- Brief: Execute `parse_to_stremio_streams` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: torrent_items Runtime input parameter consumed by `parse_to_stremio_streams`. config Runtime input parameter consumed by `parse_to_stremio_streams`. config_url Runtime input parameter consumed by `parse_to_stremio_streams`. node_url Runtime input parameter consumed by `parse_to_stremio_streams`. media Runtime input parameter consumed by `parse_to_stremio_streams`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`get_emoji`|fn|pub|22-46|def get_emoji(language)|
|`INSTANTLY_AVAILABLE`|var|pub|48||
|`DOWNLOAD_REQUIRED`|var|pub|50||
|`DIRECT_TORRENT`|var|pub|52||
|`filter_by_availability`|fn|pub|55-68|def filter_by_availability(item)|
|`filter_by_direct_torrnet`|fn|pub|69-82|def filter_by_direct_torrnet(item)|
|`parse_to_debrid_stream`|fn|pub|83-200|def parse_to_debrid_stream(torrent_item: TorrentItem, con...|
|`parse_to_stremio_streams`|fn|pub|201-237|def parse_to_stremio_streams(torrent_items: List[TorrentI...|


---

# string_encoding.py | Python | 82L | 3 symbols | 4 imports | 11 comments
> Path: `src/debriddo/utils/string_encoding.py`

## Imports
```
import json
import re
from unidecode import unidecode
import lzstring
```

## Definitions

### fn `def encode_lzstring(json_value, tag)` (L17-37)
- Brief: Execute `encode_lzstring` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: json_value Runtime input parameter consumed by `encode_lzstring`. tag Runtime input parameter consumed by `encode_lzstring`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def decode_lzstring(data, tag)` (L38-63)
- Brief: Execute `decode_lzstring` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: data Runtime input parameter consumed by `decode_lzstring`. tag Runtime input parameter consumed by `decode_lzstring`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

### fn `def normalize(string)` (L64-82)
- Brief: Execute `normalize` operational logic.
- Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: string Runtime input parameter consumed by `normalize`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`encode_lzstring`|fn|pub|17-37|def encode_lzstring(json_value, tag)|
|`decode_lzstring`|fn|pub|38-63|def decode_lzstring(data, tag)|
|`normalize`|fn|pub|64-82|def normalize(string)|


---

# base_filter.py | Python | 61L | 5 symbols | 0 imports | 9 comments
> Path: `src/debriddo/utils/filter/base_filter.py`

## Definitions

### class `class BaseFilter` (L11-61)
- Brief: Class `BaseFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `filter` operational logic. Execute `can_filter` operational logic. Execute `__call__` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. additional_config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`. self Runtime input parameter consumed by `can_filter`. self Runtime input parameter consumed by `__call__`. data Runtime input parameter consumed by `__call__`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config, additional_config=None)` `priv` (L16-28)
  - Brief: Class `BaseFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. additional_config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L29-39)
  - Brief: Execute `filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def can_filter(self)` (L40-49)
  - Brief: Execute `can_filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `can_filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __call__(self, data)` `priv` (L50-61)
  - Brief: Execute `__call__` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__call__`. data Runtime input parameter consumed by `__call__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

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

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class LanguageFilter(BaseFilter)` : BaseFilter (L17-64)
- Brief: Class `LanguageFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `filter` operational logic. Execute `can_filter` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`. self Runtime input parameter consumed by `can_filter`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L22-32)
  - Brief: Class `LanguageFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L33-55)
  - Brief: Execute `filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def can_filter(self)` (L56-64)
  - Brief: Execute `can_filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `can_filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

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

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class MaxSizeFilter(BaseFilter)` : BaseFilter (L17-57)
- Brief: Class `MaxSizeFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `filter` operational logic. Execute `can_filter` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. additional_config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`. self Runtime input parameter consumed by `can_filter`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config, additional_config=None)` `priv` (L22-33)
  - Brief: Class `MaxSizeFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. additional_config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L34-48)
  - Brief: Execute `filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def can_filter(self)` (L49-57)
  - Brief: Execute `can_filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `can_filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

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

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class QualityExclusionFilter(BaseFilter)` : BaseFilter (L17-72)
- Brief: Class `QualityExclusionFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `filter` operational logic. Execute `can_filter` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`. self Runtime input parameter consumed by `can_filter`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L22-32)
  - Brief: Class `QualityExclusionFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- var `RIPS = ["HDRIP", "BRRIP", "BDRIP", "WEBRIP", "TVRIP", "VODRIP", "HDRIP"]` (L33)
- var `CAMS = ["CAM", "TS", "TC", "R5", "DVDSCR", "HDTV", "PDTV", "DSR", "WORKPRINT", "VHSRIP", "HDCAM"]` (L34)
- fn `def filter(self, data)` (L36-63)
  - Brief: Execute `filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def can_filter(self)` (L64-72)
  - Brief: Execute `can_filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `can_filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

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

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class ResultsPerQualityFilter(BaseFilter)` : BaseFilter (L17-65)
- Brief: Class `ResultsPerQualityFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `filter` operational logic. Execute `can_filter` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`. self Runtime input parameter consumed by `can_filter`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L22-32)
  - Brief: Class `ResultsPerQualityFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L33-56)
  - Brief: Execute `filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def can_filter(self)` (L57-65)
  - Brief: Execute `can_filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `can_filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`ResultsPerQualityFilter`|class|pub|17-65|class ResultsPerQualityFilter(BaseFilter)|
|`ResultsPerQualityFilter.__init__`|fn|priv|22-32|def __init__(self, config)|
|`ResultsPerQualityFilter.filter`|fn|pub|33-56|def filter(self, data)|
|`ResultsPerQualityFilter.can_filter`|fn|pub|57-65|def can_filter(self)|


---

# title_exclusion_filter.py | Python | 60L | 4 symbols | 2 imports | 8 comments
> Path: `src/debriddo/utils/filter/title_exclusion_filter.py`

## Imports
```
from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger
```

## Definitions

### class `class TitleExclusionFilter(BaseFilter)` : BaseFilter (L17-60)
- Brief: Class `TitleExclusionFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic. Execute `filter` operational logic. Execute `can_filter` operational logic.
- Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning. Generated Doxygen block describing callable contract for LLM-native static reasoning.
- Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`. self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`. self Runtime input parameter consumed by `can_filter`.
- Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic. Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def __init__(self, config)` `priv` (L22-32)
  - Brief: Class `TitleExclusionFilter` encapsulates cohesive runtime behavior. Execute `__init__` operational logic.
  - Details: Generated Doxygen block for class-level contract and extension boundaries. Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `__init__`. config Runtime input parameter consumed by `__init__`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def filter(self, data)` (L33-51)
  - Brief: Execute `filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `filter`. data Runtime input parameter consumed by `filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
- fn `def can_filter(self)` (L52-60)
  - Brief: Execute `can_filter` operational logic.
  - Details: Generated Doxygen block describing callable contract for LLM-native static reasoning.
  - Param: self Runtime input parameter consumed by `can_filter`.
  - Return: Computed result payload; `None` when side-effect-only execution path is selected. @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`TitleExclusionFilter`|class|pub|17-60|class TitleExclusionFilter(BaseFilter)|
|`TitleExclusionFilter.__init__`|fn|priv|22-32|def __init__(self, config)|
|`TitleExclusionFilter.filter`|fn|pub|33-51|def filter(self, data)|
|`TitleExclusionFilter.can_filter`|fn|pub|52-60|def can_filter(self)|


---

# media.py | Python | 26L | 2 symbols | 0 imports | 6 comments
> Path: `src/debriddo/models/media.py`

## Definitions

### class `class Media` (L11-12)

### fn `def __init__(self, id, titles, languages, type)` `priv` (L15-16)
- Brief: Class `Media` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Media`|class|pub|11-12|class Media|
|`__init__`|fn|priv|15-16|def __init__(self, id, titles, languages, type)|


---

# movie.py | Python | 26L | 2 symbols | 1 imports | 6 comments
> Path: `src/debriddo/models/movie.py`

## Imports
```
from debriddo.models.media import Media
```

## Definitions

### class `class Movie(Media)` : Media (L13-14)

### fn `def __init__(self, id, titles, year, languages)` `priv` (L17-18)
- Brief: Class `Movie` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Movie`|class|pub|13-14|class Movie(Media)|
|`__init__`|fn|priv|17-18|def __init__(self, id, titles, year, languages)|


---

# series.py | Python | 29L | 2 symbols | 1 imports | 6 comments
> Path: `src/debriddo/models/series.py`

## Imports
```
from debriddo.models.media import Media
```

## Definitions

### class `class Series(Media)` : Media (L13-14)

### fn `def __init__(self, id, titles, season, episode, languages)` `priv` (L17-18)
- Brief: Class `Series` runtime contract.
- Details: LLM-oriented operational contract for static analyzers and refactoring agents.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`Series`|class|pub|13-14|class Series(Media)|
|`__init__`|fn|priv|17-18|def __init__(self, id, titles, season, episode, languages)|

