# VERSION: 0.0.27
# AUTHORS: Ogekuri

from utils.logger import setup_logger

class BasePlugin:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(__name__)

    async def login(self):
        pass

    async def search(self, what, cat='all'):
        raise NotImplementedError

    async def download_torrent(self,info_url):
        raise NotImplementedError
