from RTN import parse

from models.series import Series
from torrent.torrent_item import TorrentItem
from utils.logger import setup_logger

logger = setup_logger(__name__)

class SearchResult:
    def __init__(self):
        self.raw_title = None  # Raw title of the torrent
        self.title = None  # Title of the torrent
        self.size = None  # Size of the torrent
        self.link = None  # Download link for the torrent file or magnet url
        self.indexer = None  # Indexer
        self.seeders = None  # Seeders count

        self.engine_name = None  # Indexer Name
        
        self.magnet = None  # Magnet url
        self.info_hash = None  # infoHash by Search
        self.privacy = None  # public or private (determina se sarà o meno salvato in cache)

        # Extra processed details for further filtering
        self.languages = None  # Language of the torrent
        self.type = None  # series or movie

        # from cache?
        self.from_cache = False

        # parsed data
        self.parsed_data = None  # Ranked result

    def convert_to_torrent_item(self):
        # def TorrentItem::__init__(self, 
        # raw_title, 
        # title, 
        # size, 
        # magnet, 
        # info_hash, 
        # link, 
        # seeders, 
        # languages, 
        # indexer, 
        # engine_name, 
        # privacy, 
        # type=None, 
        # parsed_data=None, 
        # from_cache=False):
        
        return TorrentItem(
            self.raw_title,
            self.title,
            self.size,
            self.magnet,
            self.info_hash.lower() if self.info_hash is not None else None,
            self.link,
            self.seeders,
            self.languages,
            self.indexer,       # ilCorSaRoNeRo
            self.engine_name,   # ilcorsaronero (tutto minuscolo)
            self.privacy,
            self.type,
            self.parsed_data,
            self.from_cache,
        )

    def from_cached_item(self, cached_item):
        if type(cached_item) is not dict:
            logger.error(cached_item)
        self.type = cached_item['media_type']
        self.raw_title = cached_item['torrent_raw_title']
        self.title = cached_item['torrent_title']
        self.indexer = cached_item['torrent_indexer']
        self.magnet = cached_item['torrent_magnet']
        self.link = cached_item['torrent_link']
        self.info_hash = cached_item['torrent_hash']
        self.languages = cached_item['torrent_languages']
        self.seeders = cached_item['torrent_seeders']
        self.size = cached_item['torrent_size']
        self.privacy = cached_item['torrent_privacy']
        self.from_cache = True

        parsed_result = parse(self.raw_title)
        self.parsed_data = parsed_result

        return self
