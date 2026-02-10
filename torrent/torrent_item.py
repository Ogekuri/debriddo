# VERSION: 0.0.34
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from urllib.parse import quote

from models.media import Media
from models.series import Series
from utils.logger import setup_logger


class TorrentItem:
    def __init__(self, raw_title, title, size, magnet, info_hash, link, seeders, languages, indexer,
                 engine_name, privacy, type=None, parsed_data=None, from_cache=False):
        self.logger = setup_logger(__name__)

        self.raw_title = raw_title  # Raw title of the torrent
        self.title = title  # Title of the torrent
        self.size = size  # Size of the video file inside the torrent - it may be updated during __process_torrent()
        self.magnet = magnet  # Magnet to torrent
        self.info_hash = info_hash  # Hash of the torrent
        self.link = link  # Link to download torrent file or magnet link
        self.seeders = seeders  # The number of seeders
        self.languages = languages  # Language of the torrent
        self.indexer = indexer  # Indexer of the torrent (ilCorSaRoNeRo)
        self.engine_name = engine_name  # Engine name of the torrent (ilcorsaronero)
        self.privacy = privacy  # public or private (determina se sarà o meno salvato in cache)
        self.type = type  # "series" or "movie"
        self.from_cache = from_cache # by default is not from cache

        self.file_name = None  # it may be updated during __process_torrent()
        self.files = None  # The files inside of the torrent. If it's None, it means that there is only one file inside of the torrent
        self.torrent_download = None  # The torrent download url if its None, it means that there is only a magnet link provided by Jackett. It also means, that we cant do series file filtering before debrid.
        self.trackers = []  # Trackers of the torrent
        self.file_index = None  # Index of the file inside of the torrent - it may be updated durring __process_torrent() and update_availability(). If the index is None and torrent is not None, it means that the series episode is not inside of the torrent.
        self.availability = False  # If it's instantly available on the debrid service


        self.parsed_data = parsed_data  # Ranked result

    def to_debrid_stream_query(self, media: Media) -> dict:
        return {
            "magnet": self.magnet,
            "type": self.type,
            "file_index": self.file_index,
            "season": media.season if isinstance(media, Series) else None,
            "episode": media.episode if isinstance(media, Series) else None,
            "torrent_download": quote(self.torrent_download) if self.torrent_download is not None else None
        }
