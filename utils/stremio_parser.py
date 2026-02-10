# VERSION: 0.0.33
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
import queue
import threading
from typing import List
from models.media import Media
from torrent.torrent_item import TorrentItem
from utils.logger import setup_logger
from utils.parse_config import encode_query

logger = setup_logger(__name__)

# TODO: Languages
def get_emoji(language):
    emoji_dict = {
        "fr": "🇫🇷",
        "en": "🇬🇧",
        "es": "🇪🇸",
        "de": "🇩🇪",
        "it": "🇮🇹",
        "pt": "🇵🇹",
        "ru": "🇷🇺",
        "in": "🇮🇳",
        "nl": "🇳🇱",
        "hu": "🇭🇺",
        "la": "🇲🇽",
        "multi": "🌍"
    }
    return emoji_dict.get(language, "🇬🇧")


INSTANTLY_AVAILABLE = "[⚡"
DOWNLOAD_REQUIRED = "[⬇️"
DIRECT_TORRENT = "[🏴‍☠️"


def filter_by_availability(item):
    if item["name"].startswith(INSTANTLY_AVAILABLE):
        return 0
    else:
        return 1


def filter_by_direct_torrnet(item):
    if item["name"].startswith(DIRECT_TORRENT):
        return 1
    else:
        return 0


def parse_to_debrid_stream(torrent_item: TorrentItem, config_url, node_url, playtorrent, results: queue.Queue, media: Media):
    if torrent_item.availability == True:
        name = f"{INSTANTLY_AVAILABLE}"
    else:
        name = f"{DOWNLOAD_REQUIRED}"

    parsed_data = torrent_item.parsed_data.data

    # TODO: Always take the first resolution, is that the best one?
    # resolution = parsed_data.resolution[0] if len(parsed_data.resolution) > 0 else "Unknown"
    # name += f"{resolution}" + (f"\n({'|'.join(parsed_data.quality)})" if len(parsed_data.quality) > 0 else "")

    # from cache
    if torrent_item.from_cache:
        cache = "🔄"
    else:
        cache = ""

    # seson package
    if len(parsed_data.episodes) == 0 and len(parsed_data.seasons) > 0:
        package = "📦"
    else:
        package = ""

    # risoluzioni
    if parsed_data.resolution != None and parsed_data.resolution != "unknown":
        resolution = parsed_data.resolution 
    else:
        resolution = ""
    
    # qualità
    if parsed_data.quality != None and parsed_data.quality != "unknown":
        quality = parsed_data.quality
    else:
        quality = ""

    # formattazione pannello sinistro gui
    name += f"{package}{cache}] \n{resolution} \n{quality} "

    size_in_gb = round(int(torrent_item.size) / 1024 / 1024 / 1024, 2)

    title = f"{torrent_item.raw_title}\n"

    if torrent_item.file_name is not None:
        title += f"{torrent_item.file_name}\n"

    title += f"👥 {torrent_item.seeders}   💾 {size_in_gb}GB   🔍 {torrent_item.indexer}\n"

    if parsed_data.codec:
        title += f"🎥 {parsed_data.codec.upper()}   "
    if parsed_data.audio:
        title += f"🎧 {', '.join(parsed_data.audio)}"
    if parsed_data.codec or parsed_data.audio:
        title += "\n"

    for language in torrent_item.languages:
        title += f"{get_emoji(language)}/"
    title = title[:-1]

    # query_encoded = encode64(json.dumps(torrent_item.to_debrid_stream_query(media))).replace('=', '%3D')
    # TODO: come mai sostituiva l'=?
    query_encoded = encode_query(torrent_item.to_debrid_stream_query(media))

    item = {
        "name": name,
        "description": title,
        "url": f"{node_url}/playback/{config_url}/{query_encoded}",
        "behaviorHints":{
            "bingeGroup": f"debriddo-{torrent_item.info_hash}",
            "filename": torrent_item.file_name if torrent_item.file_name is not None else torrent_item.raw_title # TODO: Use parsed title?
        }
    }
    results.put(item)

    # warning per url troppo lunghi
    # TODO: da decidere il valore
    if len(item['url']) > 2000:
           logger.warning(f"Generated url is too long in item: {torrent_item.raw_title}")
   
    # Se è abilitato il play diretto del torrent lo aggiunge in coda
    if playtorrent: # Rimmosso 'and torrent_item.privacy == "public":', non devo condividere il torrent, non il file sulla rete torrent
        name = f"{DIRECT_TORRENT}"
        
        # formattazione pannello sinistro gui
        name += f"{package}{cache}] \n{resolution} \n{quality} "


        # if len(parsed_data.quality) > 0 and parsed_data.quality[0] != "Unknown" and \
        #         parsed_data.quality[0] != "":
        #     name += f"({'|'.join(parsed_data.quality)})"
        item = {
            "name": name,
            "description": title,
            "infoHash": torrent_item.info_hash,
            "fileIdx": int(torrent_item.file_index) if torrent_item.file_index else None,
            "behaviorHints":{
                "bingeGroup": f"debriddo-{torrent_item.info_hash}",
                "filename": torrent_item.file_name if torrent_item.file_name is not None else torrent_item.raw_title # TODO: Use parsed title?
            }
            # "sources": ["tracker:" + tracker for tracker in torrent_item.trackers]
        }
        results.put(item)


def parse_to_stremio_streams(torrent_items: List[TorrentItem], config, config_url, node_url, media):
    stream_list = []
    threads = []
    thread_results_queue = queue.Queue()

    for torrent_item in torrent_items[:int(config['maxResults'])]:
        thread = threading.Thread(target=parse_to_debrid_stream,
                                  args=(torrent_item, config_url, node_url, config['playtorrent'], thread_results_queue, media),
                                  daemon=True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    while not thread_results_queue.empty():
        stream_list.append(thread_results_queue.get())

    if len(stream_list) == 0:
        return []

    if config['debrid']:
        # ordinamento predefinito
        stream_list = sorted(stream_list, key=filter_by_availability)
        stream_list = sorted(stream_list, key=filter_by_direct_torrnet)
    return stream_list
