# VERSION: 0.0.27
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
import time
import asyncio
from urllib.parse import unquote

from constants import NO_CACHE_VIDEO_URL
from debrid.base_debrid import BaseDebrid
from utils.general import get_info_hash_from_magnet
from utils.general import is_video_file
from utils.general import season_episode_in_filename
from utils.logger import setup_logger

logger = setup_logger(__name__)


class RealDebrid(BaseDebrid):
    def __init__(self, config):
        super().__init__(config)
        self.base_url = "https://api.real-debrid.com"
        self.headers = {"Authorization": f"Bearer {self.config['debridKey']}"}

    async def add_magnet(self, magnet, ip=None):
        url = f"{self.base_url}/rest/1.0/torrents/addMagnet"
        data = {"magnet": magnet}
        return await self.get_json_response(url, method='post', headers=self.headers, data=data)

    async def add_torrent(self, torrent_file):
        url = f"{self.base_url}/rest/1.0/torrents/addTorrent"
        return await self.get_json_response(url, method='put', headers=self.headers, data=torrent_file)

    async def delete_torrent(self, id):
        url = f"{self.base_url}/rest/1.0/torrents/delete/{id}"
        return await self.get_json_response(url, method='delete', headers=self.headers)

    async def get_torrent_info(self, torrent_id):
        logger.debug(f"Getting torrent info for: {torrent_id}")
        url = f"{self.base_url}/rest/1.0/torrents/info/{torrent_id}"
        torrent_info = await self.get_json_response(url, headers=self.headers)
        if torrent_info is not None:
            if not torrent_info or 'files' not in torrent_info:
                return None

            return torrent_info
        return None

    async def select_files(self, torrent_id, file_id):
        logger.debug(f"Selecting file(s): {file_id}")
        url = f"{self.base_url}/rest/1.0/torrents/selectFiles/{torrent_id}"
        data = {"files": str(file_id)}
        # TODO verificare perché è stato sostituito dalla get_json_response che tanto non ritorna nulla!
        # self.request_post(url, headers=self.headers, data=data)
        await self.get_json_response(url, method='post', headers=self.headers, data=data)

    async def unrestrict_link(self, link):
        url = f"{self.base_url}/rest/1.0/unrestrict/link"
        data = {"link": link}
        return await self.get_json_response(url, method='post', headers=self.headers, data=data)

    async def is_already_added(self, magnet):
        hash = magnet.split("urn:btih:")[1].split("&")[0].lower()
        url = f"{self.base_url}/rest/1.0/torrents"
        torrents = await self.get_json_response(url, headers=self.headers)
        if torrents is not None:
            for torrent in torrents:
                if torrent['hash'].lower() == hash:
                    return torrent['id']
        return False

    async def wait_for_link(self, torrent_id, timeout=30, interval=2):
        start_time = time.time()
        while time.time() - start_time < timeout:
            torrent_info = await self.get_torrent_info(torrent_id)
            if torrent_info and 'links' in torrent_info and len(torrent_info['links']) > 0:
                return torrent_info['links']
            await asyncio.sleep(interval)

        return None

    async def get_availability_bulk(self, hashes_or_magnets, ip=None):
        if len(hashes_or_magnets) == 0:
            logger.debug("No hashes to be sent to Real-Debrid.")
            return dict()

        # TODO: verificare che cazzo fa sta cosa
        url = f"{self.base_url}/torrents/"
        ids = []
        for element in await self.get_json_response(url)["data"]["hash"]:
            if element is not None:
                if element["hash"] in hashes_or_magnets:
                    ids.append(element["id"])
        return await self.get_json_response(url, headers=self.headers)

    async def get_stream_link(self, query_string, ip=None):
        query = json.loads(query_string)

        magnet = query['magnet']
        stream_type = query['type']
        file_index = int(query['file_index']) if query['file_index'] is not None else None
        season = query['season']
        episode = query['episode']
        torrent_download = unquote(query["torrent_download"]) if query["torrent_download"] is not None else None
        info_hash = get_info_hash_from_magnet(magnet)
        logger.debug(f"RealDebrid get stream link for {stream_type} with hash: {info_hash}")

        cached_torrent_ids = await self.__get_cached_torrent_ids(info_hash)
        logger.debug(f"Found {len(cached_torrent_ids)} cached torrents with hash: {info_hash}")

        torrent_info = None
        if len(cached_torrent_ids) > 0:
            if stream_type == "movie":
                torrent_info = await self.get_torrent_info(cached_torrent_ids[0])
            elif stream_type == "series":
                torrent_info = await self.__get_cached_torrent_info(cached_torrent_ids, file_index, season, episode)
            else:
                return "Error: Unsupported stream type."

        # The torrent is not yet added
        if torrent_info is None:
            torrent_info = await self.__add_magnet_or_torrent(magnet, torrent_download)
            if not torrent_info or 'files' not in torrent_info:
                return "Error: Failed to get torrent info."

            logger.debug("Selecting file")
            await self.__select_file(torrent_info, stream_type, file_index, season, episode)

            # == operator, to avoid adding the season pack twice and setting 5 as season pack treshold
            if len(cached_torrent_ids) == 0 and stream_type == "series" and len(torrent_info["files"]) > 5:
                logger.debug("Prefetching season pack")
                prefetched_torrent_info = await self.__prefetch_season_pack(magnet, torrent_download)
                if len(prefetched_torrent_info["links"]) > 0:
                    await self.delete_torrent(torrent_info["id"])
                    torrent_info = prefetched_torrent_info

        torrent_id = torrent_info["id"]
        logger.debug(f"Waiting for the link(s) to be ready for torrent ID: {torrent_id}")
        # Waiting for the link(s) to be ready
        links = await self.wait_for_link(torrent_id)
        if links is None:
            return NO_CACHE_VIDEO_URL

        if len(links) > 1:
            logger.debug("Finding appropiate link")
            download_link = self.__find_appropiate_link(torrent_info, links, file_index, season, episode)
        else:
            download_link = links[0]

        logger.debug(f"Unrestricting the download link: {download_link}")
        # Unrestricting the download link
        unrestrict_response = await self.unrestrict_link(download_link)
        if not unrestrict_response or 'download' not in unrestrict_response:
            return "Error: Failed to unrestrict link."

        logger.debug(f"Got download link: {unrestrict_response['download']}")
        return unrestrict_response['download']

    async def __get_cached_torrent_ids(self, info_hash):
        url = f"{self.base_url}/rest/1.0/torrents"
        torrents = await self.get_json_response(url, headers=self.headers)
        if torrents is not None:
            logger.debug(f"Searching users real-debrid downloads for {info_hash}")
            torrent_ids = []
            for torrent in torrents:
                if torrent['hash'].lower() == info_hash:
                    torrent_ids.append(torrent['id'])

            return torrent_ids
        return None

    async def __get_cached_torrent_info(self, cached_ids, file_index, season, episode):
        cached_torrents = []
        for cached_torrent_id in cached_ids:
            cached_torrent_info = await self.get_torrent_info(cached_torrent_id)
            if self.__torrent_contains_file(cached_torrent_info, file_index, season, episode):
                if len(cached_torrent_info["links"]) > 0:  # If the links are ready
                    return cached_torrent_info

                cached_torrents.append(cached_torrent_info)

        if len(cached_torrents) == 0:
            return None

        return max(cached_torrents, key=lambda x: x['progress'])

    def __torrent_contains_file(self, torrent_info, file_index, season, episode):
        if not torrent_info or "files" not in torrent_info:
            return False

        if file_index is None:
            for file in torrent_info["files"]:
                if file["selected"] and season_episode_in_filename(file['path'], season, episode):
                    return True
        else:
            for file in torrent_info["files"]:
                if file['id'] == file_index:
                    return file["selected"] == 1

        return False

    async def __add_magnet_or_torrent(self, magnet, torrent_download=None):
        torrent_id = ""
        if torrent_download is None:
            logger.debug(f"Adding magnet to RealDebrid")
            magnet_response = await self.add_magnet(magnet)
            logger.debug(f"RealDebrid add magnet response: {magnet_response}")

            if not magnet_response or 'id' not in magnet_response:
                return "Error: Failed to add magnet."

            torrent_id = magnet_response['id']
        else:
            logger.debug(f"Downloading torrent file from Jackett")
            torrent_file = self.donwload_torrent_file(torrent_download)
            logger.debug(f"Torrent file downloaded from Jackett")

            logger.debug(f"Adding torrent file to RealDebrid")
            upload_response = self.add_torrent(torrent_file)
            logger.debug(f"RealDebrid add torrent file response: {upload_response}")

            if not upload_response or 'id' not in upload_response:
                return "Error: Failed to add torrent file."

            torrent_id = upload_response['id']

        logger.debug(f"New torrent ID: {torrent_id}")
        return await self.get_torrent_info(torrent_id)

    async def __prefetch_season_pack(self, magnet, torrent_download, timeout=30, interval=2):
        torrent_info = await self.__add_magnet_or_torrent(magnet, torrent_download)
        video_file_indexes = []

        for file in torrent_info["files"]:
            if is_video_file(file["path"]):
                video_file_indexes.append(str(file["id"]))

        await self.select_files(torrent_info["id"], ",".join(video_file_indexes))
        
        # TODO: da testare bene
        # await asyncio.sleep(10)
        await self.wait_for_link(torrent_info["id"], timeout, interval)

        return await self.get_torrent_info(torrent_info["id"])

    async def __select_file(self, torrent_info, stream_type, file_index, season, episode):
        torrent_id = torrent_info["id"]
        if file_index is not None:
            logger.debug(f"Selecting file_index: {file_index}")
            await self.select_files(torrent_id, file_index)
            return

        files = torrent_info["files"]
        if stream_type == "movie":
            largest_file_id = max(files, key=lambda x: x['bytes'])['id']
            logger.debug(f"Selecting file_index: {largest_file_id}")
            await self.select_files(torrent_id, largest_file_id)
        elif stream_type == "series":
            strict_matching_files = []
            matching_files = []
            for file in files:
                if season_episode_in_filename(file["path"], season, episode):
                    strict_matching_files.append(file)
                # if season_episode_in_filename(file["path"], season, episode, strict=True):
                #     strict_matching_files.append(file)
                # elif season_episode_in_filename(file["path"], season, episode, strict=False):
                #     matching_files.append(file)

            if len(strict_matching_files) > 0:
                matching_files = strict_matching_files

            largest_file_id = max(matching_files, key=lambda x: x['bytes'])['id']
            logger.debug(f"Selecting file_index: {largest_file_id}")
            await self.select_files(torrent_id, largest_file_id)

    def __find_appropiate_link(self, torrent_info, links, file_index, season, episode):
        selected_files = list(filter(lambda file: file["selected"] == 1, torrent_info["files"]))

        index = 0
        if file_index is not None:
            for file in selected_files:
                if file["id"] == file_index:
                    break
                index += 1
        else:
            matching_indexes = []
            strict_matching_indexes = []
            for file in selected_files:
                if season_episode_in_filename(file["path"], season, episode):
                    strict_matching_indexes.append({"index": index, "file": file})
                # if season_episode_in_filename(file["path"], season, episode, strict=True):
                #     strict_matching_indexes.append({"index": index, "file": file})
                # elif season_episode_in_filename(file["path"], season, episode, strict=False):
                #     matching_indexes.append({"index": index, "file": file})
                index += 1

            if len(strict_matching_indexes) > 0:
                matching_indexes = strict_matching_indexes

            index = max(matching_indexes, key=lambda x: x["file"]["bytes"])["index"]

        if len(links) - 1 < index:
            logger.debug(f"From selected files {selected_files}, index: {index} is out of range for {links}.")
            return NO_CACHE_VIDEO_URL

        return links[index]