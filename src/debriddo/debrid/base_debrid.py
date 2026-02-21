"""
@file src/debriddo/debrid/base_debrid.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.36
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import asyncio
from debriddo.utils.logger import setup_logger
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono


class BaseDebrid:
    """
    @brief Class `BaseDebrid` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    def __init__(self, config):
        """
        @brief Execute `__init__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__init__`.
        @param config Runtime input parameter consumed by `__init__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.config = config
        self.logger = setup_logger(__name__)

    async def wait_for_ready_status_async_func(self, check_status_func, timeout=30, interval=5):
        """
        @brief Execute `wait_for_ready_status_async_func` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `wait_for_ready_status_async_func`.
        @param check_status_func Runtime input parameter consumed by `wait_for_ready_status_async_func`.
        @param timeout Runtime input parameter consumed by `wait_for_ready_status_async_func`.
        @param interval Runtime input parameter consumed by `wait_for_ready_status_async_func`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
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
        """
        @brief Execute `wait_for_ready_status_sync_func` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `wait_for_ready_status_sync_func`.
        @param check_status_func Runtime input parameter consumed by `wait_for_ready_status_sync_func`.
        @param timeout Runtime input parameter consumed by `wait_for_ready_status_sync_func`.
        @param interval Runtime input parameter consumed by `wait_for_ready_status_sync_func`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
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
        """
        @brief Execute `get_json_response` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_json_response`.
        @param url Runtime input parameter consumed by `get_json_response`.
        @param **kwargs Runtime input parameter consumed by `get_json_response`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        ret = await session.get_json_response(url, **kwargs)
        await session.close()
        return ret

    async def download_torrent_file(self, download_url):
        """
        @brief Execute `download_torrent_file` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `download_torrent_file`.
        @param download_url Runtime input parameter consumed by `download_torrent_file`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        ret = await session.download_torrent_file(download_url)
        await session.close()
        return ret


    async def get_stream_link(self, query, ip=None):
        """
        @brief Execute `get_stream_link` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_stream_link`.
        @param query Runtime input parameter consumed by `get_stream_link`.
        @param ip Runtime input parameter consumed by `get_stream_link`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        raise NotImplementedError


    async def add_magnet(self, magnet, ip=None):
        """
        @brief Execute `add_magnet` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `add_magnet`.
        @param magnet Runtime input parameter consumed by `add_magnet`.
        @param ip Runtime input parameter consumed by `add_magnet`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        raise NotImplementedError


    async def get_availability_bulk(self, hashes_or_magnets, ip=None):
        """
        @brief Execute `get_availability_bulk` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_availability_bulk`.
        @param hashes_or_magnets Runtime input parameter consumed by `get_availability_bulk`.
        @param ip Runtime input parameter consumed by `get_availability_bulk`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        raise NotImplementedError


