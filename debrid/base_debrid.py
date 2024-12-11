# VERSION: 0.0.26
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
import asyncio
import httpx
from utils.logger import setup_logger
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono


class BaseDebrid:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(__name__)

    async def wait_for_ready_status_async_func(self, check_status_func, timeout=30, interval=5):
        self.logger.debug(f"Waiting for {timeout} seconds to cache.")
        start_time = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start_time < timeout:
            # Se check_status_func è asincrona, uso `await check_status_func()`.
            if await check_status_func():
                self.logger.debug("File is ready!")
                return True
            await asyncio.sleep(interval)
        self.logger.debug("Waiting timed out.")
        return False
    
    async def wait_for_ready_status_sync_func(self, check_status_func, timeout=30, interval=5):
        self.logger.debug(f"Waiting for {timeout} seconds to cache.")
        start_time = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start_time < timeout:
            # Se check_status_func è sincrona, la chiamiamo direttamente.
            if check_status_func():
                self.logger.debug("File is ready!")
                return True
            await asyncio.sleep(interval)
        self.logger.debug("Waiting timed out.")
        return False


    async def get_json_response(self, url, **kwargs):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        ret = await session.get_json_response(url, **kwargs)
        await session.close()
        return ret

    async def download_torrent_file(self, download_url):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        ret = await session.download_torrent_file(download_url)
        await session.close()
        return ret


    async def get_stream_link(self, query, ip=None):
        raise NotImplementedError


    async def add_magnet(self, magnet, ip=None):
        raise NotImplementedError


    async def get_availability_bulk(self, hashes_or_magnets, ip=None):
        raise NotImplementedError


