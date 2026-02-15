"""
@file src/debriddo/debrid/torbox.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
import time
import asyncio
from urllib.parse import unquote

from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger

logger = setup_logger(__name__)


class TorBox(BaseDebrid):
    """
    @brief Class `TorBox` encapsulates cohesive runtime behavior.
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
        super().__init__(config)
        self.base_url = "https://api.torbox.app/v1/api/"
        self.headers = {
            "Authorization": f"Bearer {self.config['debridKey']}",
        }

    async def wait_for_files(self, torrent_hash, timeout=30, interval=5):
        """
        @brief Execute `wait_for_files` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `wait_for_files`.
        @param torrent_hash Runtime input parameter consumed by `wait_for_files`.
        @param timeout Runtime input parameter consumed by `wait_for_files`.
        @param interval Runtime input parameter consumed by `wait_for_files`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            status = await self.check_magnet_status(torrent_hash)
            if status:
                logger.debug(f"Torrent status: {status}")
                if isinstance(status, list) and len(status) > 0 and "files" in status[0]:
                    files = status[0]["files"]
                    if files:
                        logger.debug(f"Files are ready: {files}")
                        return files
            logger.debug("Files not ready yet, retrying...")
            await asyncio.sleep(interval)
        logger.error("Timeout while waiting for torrent files.")
        return None

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
        url = f"{self.base_url}torrents/createtorrent"
        data = {
            "magnet": magnet,
            "seed": 2
        }
        logger.debug(f"URL: {url}")
        logger.debug(f"Headers: {self.headers}")
        logger.debug(f"Form Data: {data}")

        response = await self.get_json_response(url, method="post", data=data)
        if response is not None:
            if response and response.get("success", False):
                data = response.get("data", {})
                if "torrent_id" not in data:
                    logger.error(f"Missing 'torrent_id' in response: {response}")
                    return None
                cached = "Found Cached Torrent" in response.get("detail", "")
                return {
                    "torrent_id": data["torrent_id"],
                    "hash": data["hash"],
                    "is_cached": cached
                }
            else:
                logger.error(f"Failed to add magnet: {response}")
        
        return None

    async def check_magnet_status(self, torrent_hash):
        """
        @brief Execute `check_magnet_status` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `check_magnet_status`.
        @param torrent_hash Runtime input parameter consumed by `check_magnet_status`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        url = f"{self.base_url}torrents/checkcached?hash={torrent_hash}&format=object&list_files=true"
        response = await self.get_json_response(url)
        if response is not None:
            logger.debug(f"Response from check_magnet_status: {response}")
            if response and response.get("success", False):
                return response["data"] if response["data"] else []
            else:
                logger.error(f"Failed to check status for hash {torrent_hash}: {response}")
        return None

    async def get_file_download_link(self, torrent_id, file_name):
        """
        @brief Execute `get_file_download_link` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_file_download_link`.
        @param torrent_id Runtime input parameter consumed by `get_file_download_link`.
        @param file_name Runtime input parameter consumed by `get_file_download_link`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        url = f"{self.base_url}torrents/requestdl?token={self.config['debridKey']}&torrent_id={torrent_id}&file_id={file_name}&zip_link=false&torrent_file=false"
        response = await self.get_json_response(url, method='get')
        if response is not None:
            if response and response.get("success", False):
                return response["data"]
            else:
                logger.error(f"Failed to get download link for torrent_id {torrent_id} and file {file_name}: {response}")
        return None

    async def __add_magnet_or_torrent(self, magnet, torrent_download=None):
        """
        @brief Execute `__add_magnet_or_torrent` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__add_magnet_or_torrent`.
        @param magnet Runtime input parameter consumed by `__add_magnet_or_torrent`.
        @param torrent_download Runtime input parameter consumed by `__add_magnet_or_torrent`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        torrent_id = None
        if magnet:
            logger.debug(f"Adding magnet to TorBox")
            torrent_id = await self.add_magnet(magnet)
            logger.debug(f"TorBox add magnet response: {torrent_id}")
        else:
            logger.error("Only magnet links are supported for TorBox.")
        return torrent_id

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
        magnet = query["magnet"]
        stream_type = query["type"]
        season = query.get("season")
        episode = query.get("episode")

        magnet_data = await self.add_magnet(magnet)
        if not magnet_data:
            logger.error("Failed to add magnet or retrieve torrent_id.")
            return NO_CACHE_VIDEO_URL

        torrent_id = magnet_data.get("torrent_id")
        if not torrent_id:
            logger.error("Missing torrent_id in magnet_data.")
            return NO_CACHE_VIDEO_URL

        is_cached = magnet_data["is_cached"]

        if is_cached:
            logger.debug("Magnet is already cached. Files are ready.")
            cached_status = await self.check_magnet_status(magnet_data["hash"])
            if not isinstance(cached_status, dict):
                logger.error("Invalid cached torrent status response.")
                return NO_CACHE_VIDEO_URL
            files = cached_status.get(magnet_data["hash"])
            if not isinstance(files, dict) or "files" not in files:
                logger.error("Files not found in cached torrent.")
                return NO_CACHE_VIDEO_URL
        else:
            files = await self.wait_for_files(magnet_data["hash"])
            if not files:
                logger.error(f"No files found for magnet {magnet}.")
                return NO_CACHE_VIDEO_URL

        if stream_type == "movie":
            largest_file_index, largest_file = max(
                enumerate(files["files"]), key=lambda x: x[1]["size"]
            )
            return await self.get_file_download_link(torrent_id, largest_file_index)
        elif stream_type == "series":
            files = files["files"]
            matching_files = [
                (index, file) for index, file in enumerate(files)
                if season_episode_in_filename(file["name"], season, episode)
            ]
            if matching_files:
                selected_index, selected_file = max(
                    matching_files, key=lambda x: x[1]["size"]
                )
                return await self.get_file_download_link(torrent_id, selected_index)
            else:
                logger.error(f"No matching files found for {season}x{episode}.")
                return NO_CACHE_VIDEO_URL
        else:
            logger.error("Unsupported stream type.")
            raise ValueError("Error: Unsupported stream type.")

    # def get_json_response(self, url, method='get', **kwargs):
    #     try:
    #         if method == 'get':
    #             response = requests.request_get(url, headers=self.headers, **kwargs)
    #         elif method == 'post':
    #             response = requests.request_post(url, headers=self.headers, **kwargs)
    #         else:
    #             raise ValueError(f"Unsupported HTTP method: {method}")

    #         response.raise_for_status()
    #         return response.json()
    #     except requests.exceptions.RequestException as e:
    #         logger.error(f"HTTP request failed: {e}")
    #         return None

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
        available_torrents = {}

        for torrent_hash in hashes_or_magnets:
            url = f"{self.base_url}torrents/checkcached?hash={torrent_hash}&format=list&list_files=true"
            try:
                response = await self.get_json_response(url)
                if response is not None:
                    if response.get("success") and response.get("data"):
                        torrent_data = response["data"][0]
                        available_torrents[torrent_hash] = {
                            "name": torrent_data["name"],
                            "size": torrent_data["size"],
                            "files": torrent_data["files"]
                        }
                else:
                    self.logger.warning(f"Torrent {torrent_hash} is not cached or invalid response: {response}")

            except Exception as e:
                self.logger.error(f"Error while checking availability for hash {torrent_hash}: {e}")
                continue

        return available_torrents
