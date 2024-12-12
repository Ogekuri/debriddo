# VERSION: 0.0.30
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import os
import sys
import re
import shutil
import time
import zipfile
import uvicorn
import json
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

from debrid.get_debrid_service import get_debrid_service

from search.search_result import SearchResult
from search.search_service import SearchService

from metdata.cinemeta import Cinemeta
from metdata.tmdb import TMDB

from torrent.torrent_service import TorrentService
from torrent.torrent_smart_container import TorrentSmartContainer

from utils.cache import search_cache
from utils.filter_results import filter_items, sort_items
from utils.logger import setup_logger
from utils.parse_config import parse_config, parse_query
from utils.stremio_parser import parse_to_stremio_streams
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono

from web.pages import get_index

from constants import APPLICATION_NAME, APPLICATION_VERSION, APPLICATION_DESCRIPTION


# load .env
load_dotenv()


# get environment variables
root_path = os.environ.get("ROOT_PATH", None)
if root_path and not root_path.startswith("/"):
    root_path = "/" + root_path

node_url = os.getenv("NODE_URL", "http://127.0.0.1:8000")
if node_url is not None and type(node_url) is str and len(node_url) > 0:
    app_website = node_url
else:
    app_website = "http://127.0.0.1:8000"
node_env = os.getenv("NODE_ENV", None)
if node_env is not None and type(node_env) is str and len(node_env) > 0:
    development = node_env.lower()
else:
    development = None


# define common string
app_name = str(APPLICATION_NAME)
app_name_lc = str(APPLICATION_NAME).lower()
app_version = 'v' + str(APPLICATION_VERSION)
app_desc = str(APPLICATION_DESCRIPTION)
app_environment = f"({development})" if development is not None else ""
app_id = str(APPLICATION_VERSION) + '.' + development if development is not None else str(APPLICATION_VERSION)



# logger
logger = setup_logger(__name__)


# application start
logger.info(f"Started {app_name} {app_version} {app_environment} @ {app_website}")


# verifica se è in reload
is_reload_enabled = any("--reload" in arg for arg in sys.argv)


# calcola il numero ottimale di thread
def calculate_optimal_thread_count():
    """
    Calcola il numero ottimale di thread basato sui core della CPU.
    Formula: (N CPU Cores * 2) + 1
    """
    try:
        # Ottieni il numero di core della CPU
        cpu_cores = os.cpu_count()
        if cpu_cores is None:
            return 8
        
        # Calcola il numero ottimale di threads
        optimal_num_threads = (cpu_cores * 2) + 1
        return optimal_num_threads
    except Exception as e:
        logger.error(f"Errore nel calcolo dei numero dei threads: {e}")
        return 8
    

# Lifespan: gestisce startup e shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_app, 'interval', seconds=60)  # Il check dell'update ogni 60 secondi
    scheduler.start()
    logger.info(f"Scheduler avviato")

    # Verifica se il server Uvicorn è configurato con reload
    if is_reload_enabled:
        logger.warning("L'applicazione è in modalità reload.")
    else:
        logger.debug("L'applicazione non è in modalità reload.")

    try:
        yield  # Qui puoi mettere codice che deve girare durante la vita dell'app
    
    # terminazione
    finally:
        scheduler.shutdown()
        logger.info(f"Scheduler arrestato")

# Creazione dell'app FastAPI
app = FastAPI(lifespan=lifespan)

# Imposta un maggior numero di thread, per esempio 16
n_threads = calculate_optimal_thread_count()
logger.info(f"Set numeber of thread to: {n_threads}")
executor = ThreadPoolExecutor(max_workers=n_threads)
loop = asyncio.get_event_loop()
loop.set_default_executor(executor)

# Aggiunge il loggin del middleware fastapi
class LogFilterMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # Gestisci solo richieste HTTP, 
        # la classe Request di Starlette è progettata solo per gestire richieste HTTP, 
        # quindi non può essere utilizzata con eventi "lifespan" (es. avvio e arresto).
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        
        try:
            # Log informazioni sulla richiesta
            request = Request(scope, receive)
            path = request.url.path
                        
            
            # GET - /C_<CONFIG>/config
            sensible_path = re.sub(r'/C_.*?/', '/<CONFIG>/', path)
            
            # GET - /playback/C_<CONFIG>/Q_<QUERY>/
            sensible_path = re.sub(r'/Q_.*?$', '/<QUERY>', sensible_path)

            logger.debug(f"{request.method} - {sensible_path}")

            # Log body della richiesta (se presente)
            body = await request.body()
            logger.debug(f"Request Body: {body.decode('utf-8') if body else '<empty>'}")

            # Chiamata all'applicazione
            response = await self.app(scope, receive, send)

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while processing the request.")

        return response

if development is not None:
    app.add_middleware(LogFilterMiddleware)


# Abilita CORSMiddleware per le chiamate OPTIONS e il redirect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Origini consentite
    allow_credentials=True, # Consente l'invio di credenziali (es. cookie)
    allow_methods=["*"],    # Consente tutti i metodi (GET, POST, OPTIONS, ecc.)
    allow_headers=["*"],    # Consente tutti gli header
)




################
### Fast API ###
################


# root: /
@app.get("/")
async def root():
    return RedirectResponse(url="/configure")

# /favicon.ico
@app.get("/favicon.ico")
async def get_favicon():
    response = FileResponse(f"web/images/favicon.ico")
    return response

# /config.js
@app.get("/config.js")
@app.get("/{config}/config.js")
async def get_favicon():
    response = FileResponse(f"web/config.js")
    return response

# /lz-string.min.js
@app.get("/lz-string.min.js")
@app.get("/{config}/lz-string.min.js")
async def get_favicon():
    response = FileResponse(f"web/lz-string.min.js")
    return response

# /styles.css
@app.get("/styles.css")
@app.get("/{config}/styles.css")
async def get_favicon():
    response = FileResponse(f"web/styles.css")
    return response

# /configure
# /?/configure
@app.get("/configure", response_class=HTMLResponse)
@app.get("/{config}/configure", response_class=HTMLResponse)
async def configure():
    return get_index(app_name, app_version, app_environment)

# /imges/?
@app.get("/images/{file_path:path}")
@app.get("/{config}/images/{file_path:path}")
async def function(file_path: str):
    response = FileResponse(f"web/images/{file_path}")
    return response

# /site.webmanifest
@app.get("/site.webmanifest", response_class=HTMLResponse)
async def configure():
    menifest_dict = {
                    "id": "com.stremio." + app_name_lc + "." + app_id,
                    "version": str(APPLICATION_VERSION),
                    "name": app_name + ' ' + app_environment,
                    "short_name": app_name,
                    "description": app_desc,
                    "start_url": app_website,
                    "icons": [
                        {
                        "src": app_website + "/images/web-app-manifest-192x192.png",
                        "sizes": "192x192",
                        "type": "image/png",
                        "purpose": "any maskable"
                        },
                        {
                        "src": app_website + "/images/web-app-manifest-512x512.png",
                        "sizes": "512x512",
                        "type": "image/png",
                        "purpose": "any maskable"
                        }
                    ],
                    "theme_color": "#ffffff",
                    "background_color": "#ffffff",
                    "display": "standalone"
                }
    return JSONResponse(
            content=menifest_dict,
            media_type="application/manifest+json"  # Specifica il Content-Type corretto
        )

# /manifest.json
# /?/manifest.json
@app.get("/manifest.json")
@app.get("/{params}/manifest.json")
async def get_manifest():
    manifest_dict = {
        "id": "com.stremio." + app_name_lc + "." + app_id,
        "version": str(APPLICATION_VERSION),
        "name": app_name + ' ' + app_environment,
        "short_name": app_name,
        "description": app_desc,
        "start_url": app_website,
        "icons": [
            {
                "src": app_website + "/images/web-app-manifest-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": app_website + "/images/web-app-manifest-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ],
        "catalogs": [
            {
                "id": app_name_lc + "-realdebrid",
                "name": "RealDebrid",
                "type": "other",
                "extra": [
                    {
                    "name": "skip"
                    }
                ]
            }
        ],
        "resources": [
            {
                "name": "stream",
                "types": [
                    "movie",
                    "series"
                ],
                "idPrefixes": [
                    "tt",
                    "kitsu"
                ]
            },
            {
                "name": "meta",
                "types": [
                    "other"
                ],
                "idPrefixes": [
                    "realdebrid"
                ]
            }
        ],
        "types": [
            "movie",
            "series",
            "anime",
            "other"
        ],
        "background": app_website + "/images/background.jpg",
        "logo": app_website + "/images/logo.png",
        "behaviorHints": {
            "configurable": True,
            "configurationRequired": False
        }
    }
    return JSONResponse(
        content=manifest_dict,
        media_type="application/manifest+json"  # Specifica il Content-Type corretto
    )

# /?/stream/?/?
@app.get("/{config_url}/stream/{stream_type}/{stream_id}")
async def get_results(config_url: str, stream_type: str, stream_id: str, request: Request):
    start = time.time()
    stream_id = stream_id.replace(".json", "")
    config = parse_config(config_url)
    logger.debug(stream_type + " request")
    logger.debug(f"Getting media from {config['metadataProvider']}")
    if config['metadataProvider'] == "tmdb" and config['tmdbApi']:
        metadata_provider = TMDB(config)
    else:
        metadata_provider = Cinemeta(config)
    media = await metadata_provider.get_metadata(stream_id, stream_type)
    logger.info("Got media and properties: " + str(media.titles))

    debrid_service = get_debrid_service(config)

    search_results = []
    if config['cache']:
        logger.debug("Getting cached results")
        cached_results = search_cache(config, media)
        if cached_results is not None and len(cached_results) > 0:
            cached_results = [SearchResult().from_cached_item(torrent) for torrent in cached_results]
            logger.debug("Got " + str(len(cached_results)) + " cached results")

            if len(cached_results) > 0:
                logger.debug("Filtering cached results")
                search_results = filter_items(cached_results, media, config=config)
                logger.debug("Filtered cached results")

    # se la cache non ritorna abbastanza risultati
    if config['search'] and len(search_results) < int(config['minCacheResults']):
        if len(search_results) > 0 and config['cache']:
            logger.debug("Not enough cached results found (results: " + str(len(search_results)) + ")")
        elif config['cache']:
            logger.debug("No cached results found")

        logger.debug("Searching for results direct with Torrent Search (Engines)")
        search_service = SearchService(config)
        engine_results = await search_service.search(media)
        if engine_results is not None:
            logger.debug("Got " + str(len(engine_results)) + " results from Torrent Search (Engines)")
            for result in engine_results:
                if result.raw_title:
                    logger.debug("- " + str(result.raw_title))
                else:
                    logger.error(f"Error on result: {result}")        

            logger.debug("Filtering Torrent Search (Engines) results")
            filtered_engine_search_results = filter_items(engine_results, media, config=config)
            logger.debug("Filtered Torrent Search (Engines) results")

            search_results.extend(filtered_engine_search_results)

    if search_results is not None:
        logger.debug("Converting result to TorrentItems (results: " + str(len(search_results)) + ")")
        torrent_service = TorrentService()
        torrent_results = await torrent_service.convert_and_process(search_results)
        logger.debug("Converted result to TorrentItems (results: " + str(len(torrent_results)) + ")")

        torrent_smart_container = TorrentSmartContainer(torrent_results, media)

    if config['debrid']:
        if config['service'] == "torbox":
            logger.debug("Checking availability")
            hashes = torrent_smart_container.get_hashes()
            ip = request.client.host
            result = debrid_service.get_availability_bulk(hashes, ip)
            if result is not None:
                torrent_smart_container.update_availability(result, type(debrid_service), media)
                logger.debug("Checked availability (results: " + str(len(result.items())) + ")")
            else:
                logger.error("Unable to checked availability")

        # TODO: Maybe add an if to only save to cache if caching is enabled?
        torrent_smart_container.cache_container_items()

        logger.debug("Getting best matching results")
        best_matching_results = torrent_smart_container.get_best_matching()
        best_matching_results = sort_items(best_matching_results, config)
        logger.debug("Got best matching results (results: " + str(len(best_matching_results)) + ")")

        logger.debug("Processing results")
        stream_list = parse_to_stremio_streams(best_matching_results, config, config_url, node_url, media)
        logger.info("Processed results (results: " + str(len(stream_list)) + ")")

        logger.info("Total time: " + str(time.time() - start) + "s")

        return {"streams": stream_list}


# /playback/?/?
@app.head("/playback/{config_url}/{query}")
async def head_playback(config: str, query: str, request: Request):
    if not query:
        raise HTTPException(status_code=400, detail="Query required.")
    # Qui potrei limitarmi a controllare la validità di config e query
    # e restituire comunque lo stesso set di header (es: un redirect) senza generare effettivamente la destinazione.
    return Response(status_code=status.HTTP_200_OK)

# /playback/?/?
@app.get("/playback/{config_url}/{query_string}")
async def get_playback(config_url: str, query_string: str, request: Request):
    try:
        if not query_string:
            raise HTTPException(status_code=400, detail="Query required.")
        config = parse_config(config_url)

        # decodifica la query
        query = parse_query(query_string)

        # logger.debug(f"Decoded <QUERY>: {query}")
        logger.debug(f"Decoded <QUERY>: type: {str(query['type'])}, file_index: {str(query['file_index'])}, season: {str(query['season'])}, episode: {str(query['episode'])}, torrent_download: {str(query['torrent_download'])}")
        ip = request.client.host
        debrid_service = get_debrid_service(config)
        link = await debrid_service.get_stream_link(query, ip)

        logger.info("Got link: " + link)
        return RedirectResponse(url=link, status_code=status.HTTP_301_MOVED_PERMANENTLY)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")
    

###################
### self update ###
###################

async def update_app():

    # senza --reload non gestisce l'upgrade, --reload implica --workers 1
    if is_reload_enabled is False:
        return

    # in modalità sviluppo non fa l'upgrade
    if development is not None:
        return
  
    try:
        session = AsyncThreadSafeSession()  # Usa il client asincrono    
        url = "https://api.github.com/repos/Ogekuri/debriddo/releases/latest"
        response = session.request_get(url)
        data = response.json()
        latest_version = data['tag_name']
        if latest_version != app_version:
            logger.warning(f"{APPLICATION_NAME} upgrade is started")
            logger.info(f"Updating from {app_version} to {latest_version}...")
            logger.info("Getting update zip...")
            update_zip = await session.request_get(data['zipball_url'])
            with open("update.zip", "wb") as file:
                file.write(update_zip.content)
            logger.info("Update zip downloaded")
            logger.info("Extracting update...")
            with zipfile.ZipFile("update.zip", 'r') as zip_ref:
                zip_ref.extractall("update")
            logger.info("Update extracted")

            extracted_folder = os.listdir("update")[0]
            extracted_folder_path = os.path.join("update", extracted_folder)
            for item in os.listdir(extracted_folder_path):
                s = os.path.join(extracted_folder_path, item)
                d = os.path.join(".", item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            logger.info("Files copied")

            logger.info("Cleaning up...")
            shutil.rmtree("update")
            os.remove("update.zip")
            logger.info("Cleaned up")
            logger.info("Updated !")
        else:
            logger.info(f"{APPLICATION_NAME} it's already updated ({app_version}).")
        
        await session.close()
    except Exception as e:
        logger.error(f"Error during update: {e}")


############
### MAIN ###
############

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
