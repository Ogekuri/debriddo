# VERSION: 0.0.34
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

# Assuming the BaseDebrid class and necessary imports are already defined as shown previously
import json

from debriddo.constants import NO_CACHE_VIDEO_URL
from debriddo.debrid.base_debrid import BaseDebrid
from debriddo.utils.general import get_info_hash_from_magnet, season_episode_in_filename
from debriddo.utils.logger import setup_logger

logger = setup_logger(__name__)


class Premiumize(BaseDebrid):
    def __init__(self, config):
        super().__init__(config)
        self.base_url = "https://www.premiumize.me/api"

    async def add_magnet(self, magnet, ip=None):
        url = f"{self.base_url}/transfer/create?apikey={self.config['debridKey']}"
        form = {'src': magnet}
        return await self.get_json_response(url, method='post', data=form)

    # Doesn't work for the time being. Premiumize does not support torrent file torrents
    async def add_torrent(self, torrent_file):
        url = f"{self.base_url}/transfer/create?apikey={self.config['debridKey']}"
        form = {'file': torrent_file}
        return await self.get_json_response(url, method='post', data=form)

    async def list_transfers(self):
        url = f"{self.base_url}/transfer/list?apikey={self.config['debridKey']}"
        return await self.get_json_response(url)

    async def get_folder_or_file_details(self, item_id, is_folder=True):
        if is_folder:
            logger.debug(f"Getting folder details with id: {item_id}")
            url = f"{self.base_url}/folder/list?id={item_id}&apikey={self.config['debridKey']}"
        else:
            logger.debug(f"Getting file details with id: {item_id}")
            url = f"{self.base_url}/item/details?id={item_id}&apikey={self.config['debridKey']}"
        return await self.get_json_response(url)

    async def get_availability(self, hash):
        url = f"{self.base_url}/cache/check?apikey={self.config['debridKey']}&items[]={hash}"
        return await self.get_json_response(url)

    async def get_availability_bulk(self, hashes_or_magnets, ip=None):
        url = f"{self.base_url}/cache/check?apikey={self.config['debridKey']}&items[]=" + "&items[]=".join(
            hashes_or_magnets)
        return await self.get_json_response(url)

    async def get_stream_link(self, query, ip=None):
        magnet = query['magnet']
        logger.debug(f"Received query for magnet: {magnet}")
        info_hash = get_info_hash_from_magnet(magnet)
        logger.debug(f"Info hash extracted: {info_hash}")
        stream_type = query['type']
        logger.debug(f"Stream type: {stream_type}")

        transfer_data = await self.add_magnet(magnet)
        if not transfer_data or 'id' not in transfer_data:
            logger.error("Failed to create transfer.")
            raise ValueError("Error: Failed to create transfer.")
        transfer_id = transfer_data['id']
        logger.debug(f"Transfer created with ID: {transfer_id}")

        if not self.wait_for_ready_status_async_func(lambda: self.get_availability(info_hash)["transcoded"][0] is True):
            logger.debug("Torrent not ready, caching in progress")
            return NO_CACHE_VIDEO_URL

        logger.debug("Torrent is ready.")

        # Assuming the transfer is complete, we need to find whether it's a file or a folder
        transfers = await self.list_transfers()
        item_id, is_folder = None, False
        for item in transfers.get('transfers', []):
            if item['id'] == transfer_id:
                if item.get('folder_id'):
                    item_id = item['folder_id']
                    is_folder = True
                else:
                    item_id = item['file_id']
                break

        if not item_id:
            logger.error("Transfer completed but no item ID found.")
            raise ValueError("Error: Transfer completed but no item ID found.")

        details = await self.get_folder_or_file_details(item_id, is_folder)
        logger.debug(f"Got details")

        if stream_type == "movie":
            logger.debug("Getting link for movie")
            # For movies, we pick the largest file in the folder or the file itself
            if is_folder:
                link = max(details.get("content", []), key=lambda x: x["size"])["link"]
            else:
                link = details.get('link')
        elif stream_type == "series":
            logger.debug("Getting link for series")
            if is_folder:
                season = query["season"]
                episode = query["episode"]
                files = details.get("content", [])
                matching_files = []

                for file in files:
                    if season_episode_in_filename(file["name"], season, episode):
                        matching_files.append(file)

                if len(matching_files) == 0:
                    logger.error(f"No matching files for {season} {episode} in torrent.")
                    raise ValueError(f"Error: No matching files for {season} {episode} in torrent.")

                link = max(matching_files, key=lambda x: x["size"])["link"]
            else:
                link = details.get('link')
        else:
            logger.error("Unsupported stream type.")
            raise ValueError("Error: Unsupported stream type.")

        logger.debug(f"Link generated: {link}")
        return link
