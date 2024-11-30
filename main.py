import asyncio
import logging
import os
import re
import shutil
import time
import zipfile

import requests
import starlette.status as status
from aiocron import crontab
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse

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
from utils.parse_config import parse_config
from utils.stremio_parser import parse_to_stremio_streams
from utils.string_encoding import decodeb64
from static.html import get_index

from constants import APPLICATION_NAME, APPLICATION_VERSION, APPLICATION_DESCRIPTION

load_dotenv()

root_path = os.environ.get("ROOT_PATH", None)
if root_path and not root_path.startswith("/"):
    root_path = "/" + root_path

app = FastAPI(root_path=root_path)

# get environments
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
            sensible_path = re.sub(r'/ey.*?/', '/<SENSITIVE_DATA>/', path)
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


#
# Abilita CORSMiddleware per le chiamate OPTIONS e il redirect
#
# Probailmente posso filtrare meglio
# configurando le origini consentite
#
# esempio:
#
# origins = [
#     "https://web.stremio.com",  # Specifica l'origine consentita
#     "http://localhost",        # Durante lo sviluppo
#     "http://localhost:8000",   # Durante lo sviluppo
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  # Origini consentite
#     allow_credentials=True, # Consente l'invio di credenziali (es. cookie)
#     allow_methods=["*"],    # Consente tutti i metodi (GET, POST, OPTIONS, ecc.)
#     allow_headers=["*"],    # Consente tutti gli header
# )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logger = setup_logger(__name__)

# root
@app.get("/")
async def root():
    return RedirectResponse(url="/configure")

# favicon
@app.get("/favicon.ico")
async def get_favicon():
    response = FileResponse(f"static/images/favicon.ico")
    return response


@app.get("/configure", response_class=HTMLResponse)
@app.get("/{config}/configure", response_class=HTMLResponse)
async def configure():
    return get_index(app_name, app_version, app_environment)


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
                        "src": app_website + "/static/images/web-app-manifest-192x192.png",
                        "sizes": "192x192",
                        "type": "image/png",
                        "purpose": "any maskable"
                        },
                        {
                        "src": app_website + "/static/images/web-app-manifest-512x512.png",
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


@app.get("/static/{file_path:path}")
async def function(file_path: str):
    response = FileResponse(f"static/{file_path}")
    return response


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
                "src": app_website + "/static/images/web-app-manifest-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": app_website + "/static/images/web-app-manifest-512x512.png",
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
        "background": app_website + "/static/images/background.jpg",
        "logo": app_website + "/static/images/logo.png",
        "behaviorHints": {
            "configurable": True,
            "configurationRequired": False
        }
    }
    return JSONResponse(
        content=manifest_dict,
        media_type="application/manifest+json"  # Specifica il Content-Type corretto
    )


logger.info(f"Started {app_name} {app_version} {app_environment} @ {app_website}")

@app.get("/{config}/stream/{stream_type}/{stream_id}")
async def get_results(config: str, stream_type: str, stream_id: str, request: Request):
    start = time.time()
    stream_id = stream_id.replace(".json", "")

    config = parse_config(config)
    logger.debug(stream_type + " request")

    logger.debug(f"Getting media from {config['metadataProvider']}")
    if config['metadataProvider'] == "tmdb" and config['tmdbApi']:
        metadata_provider = TMDB(config)
    else:
        metadata_provider = Cinemeta(config)
    media = metadata_provider.get_metadata(stream_id, stream_type)
    logger.info("Got media and properties: " + str(media.titles))

    debrid_service = get_debrid_service(config)

    search_results = []
    if config['cache']:
        logger.debug("Getting cached results")
        cached_results = search_cache(config, media)
        if cached_results is not None and len(cached_results) > 0:
            cached_results = [SearchResult().from_cached_item(torrent, media) for torrent in cached_results]
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
        engine_results = search_service.search(media)
        if engine_results is not None:
            logger.debug("Got " + str(len(engine_results)) + " results from Torrent Search (Engines)")

            logger.debug("Filtering Torrent Search (Engines) results")
            filtered_engine_search_results = filter_items(engine_results, media, config=config)
            logger.debug("Filtered Torrent Search (Engines) results")

            search_results.extend(filtered_engine_search_results)

    if search_results is not None:
        logger.debug("Converting result to TorrentItems (results: " + str(len(search_results)) + ")")
        torrent_service = TorrentService()
        torrent_results = torrent_service.convert_and_process(search_results)
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
        stream_list = parse_to_stremio_streams(best_matching_results, config, media)
        logger.info("Processed results (results: " + str(len(stream_list)) + ")")

        logger.info("Total time: " + str(time.time() - start) + "s")

        return {"streams": stream_list}


@app.head("/playback/{config}/{query}")
@app.get("/playback/{config}/{query}")
async def get_playback(config: str, query: str, request: Request):
    try:
        if not query:
            raise HTTPException(status_code=400, detail="Query required.")
        config = parse_config(config)
        logger.debug("Decoding query")
        query = decodeb64(query)
        logger.debug(query)
        logger.debug("Decoded query")
        ip = request.client.host
        debrid_service = get_debrid_service(config)
        link = debrid_service.get_stream_link(query, ip)

        logger.info("Got link: " + link)
        return RedirectResponse(url=link, status_code=status.HTTP_301_MOVED_PERMANENTLY)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")
    

async def update_app():
    try:
        current_version = app_version
        url = "https://api.github.com/repos/Ogekuri/debriddo/releases/latest"
        response = requests.get(url)
        data = response.json()
        latest_version = data['tag_name']
        if latest_version != current_version:
            logger.info("New version available: " + latest_version)
            logger.info("Updating...")
            logger.info("Getting update zip...")
            update_zip = requests.get(data['zipball_url'])
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
    except Exception as e:
        logger.error(f"Error during update: {e}")

# gestione dell'auto-update (ogni 5 minuti)
@crontab("*/5 * * * *", start=development is None)
async def schedule_task():
    await update_app()


async def main():
    await asyncio.gather(
        schedule_task()
    )
    return


if __name__ == "__main__":
    asyncio.run(main())
