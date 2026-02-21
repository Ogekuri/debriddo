"""
@file src/debriddo/torrent/torrent_smart_container.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.37
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri


from typing import List, Dict

from debriddo.debrid.alldebrid import AllDebrid
from debriddo.debrid.premiumize import Premiumize
from debriddo.debrid.realdebrid import RealDebrid
from debriddo.debrid.torbox import TorBox

from debriddo.torrent.torrent_item import TorrentItem

from debriddo.utils.cache import cache_results
from debriddo.utils.general import season_episode_in_filename
from debriddo.utils.logger import setup_logger


class TorrentSmartContainer:
    """
    @brief Class `TorrentSmartContainer` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    def __init__(self, torrent_items: List[TorrentItem], media):
        """
        @brief Execute `__init__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__init__`.
        @param torrent_items Runtime input parameter consumed by `__init__`.
        @param media Runtime input parameter consumed by `__init__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.logger = setup_logger(__name__)
        self.__itemsDict: Dict[str, TorrentItem] = self.__build_items_dict_by_infohash(torrent_items)
        self.__media = media

    def get_hashes(self):
        """
        @brief Execute `get_hashes` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_hashes`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        return list(self.__itemsDict.keys())

    def get_items(self):
        """
        @brief Execute `get_items` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_items`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        return list(self.__itemsDict.values())

    def get_direct_torrentable(self):
        """
        @brief Execute `get_direct_torrentable` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_direct_torrentable`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        direct_torrentable_items = []
        for torrent_item in self.__itemsDict.values():
            if torrent_item.privacy == "public" and torrent_item.file_index is not None:
                direct_torrentable_items.append(torrent_item)
        return direct_torrentable_items

    def get_best_matching(self):
        """
        @brief Execute `get_best_matching` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_best_matching`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        best_matching = []
        self.logger.debug(f"Amount of items: {len(self.__itemsDict)}")
        for torrent_item in self.__itemsDict.values():
            self.logger.debug("-------------------")
            self.logger.debug(f"Checking {torrent_item.raw_title}")
            self.logger.debug(f"Has torrent: {torrent_item.torrent_download is not None}")
            if torrent_item.torrent_download is not None:  # Torrent download
                self.logger.debug(f"Has file index: {torrent_item.file_index is not None}")
                if torrent_item.file_index is not None:
                    # If the season/episode is present inside the torrent filestructure (movies always have a
                    # file_index)
                    best_matching.append(torrent_item)
            else:  # Magnet
                best_matching.append(torrent_item)  # If it's a movie with a magnet link

        return best_matching

    def cache_container_items(self):
        # threading.Thread(target=self.__save_to_cache).start()
        # la versione originale esegue l'upload dei risultati quindi
        # gira in un tread separato, ma per sqllite non serve
        """
        @brief Execute `cache_container_items` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `cache_container_items`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.__save_to_cache()


    def __save_to_cache(self):
        """
        @brief Execute `__save_to_cache` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__save_to_cache`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        public_torrents = list(filter(lambda x: x.privacy == "public", self.get_items()))
        cache_results(public_torrents, self.__media)

    def update_availability(self, debrid_response, debrid_type, media):
        """
        @brief Execute `update_availability` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `update_availability`.
        @param debrid_response Runtime input parameter consumed by `update_availability`.
        @param debrid_type Runtime input parameter consumed by `update_availability`.
        @param media Runtime input parameter consumed by `update_availability`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if debrid_type is RealDebrid:
            self.__update_availability_realdebrid(debrid_response, media)
        elif debrid_type is AllDebrid:
            self.__update_availability_alldebrid(debrid_response, media)
        elif debrid_type is Premiumize:
            self.__update_availability_premiumize(debrid_response)
        elif debrid_type is TorBox:
            self.__update_availability_torbox(debrid_response, media)
        else:
            raise NotImplementedError

    def __update_availability_realdebrid(self, response, media):
        """
        @brief Execute `__update_availability_realdebrid` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__update_availability_realdebrid`.
        @param response Runtime input parameter consumed by `__update_availability_realdebrid`.
        @param media Runtime input parameter consumed by `__update_availability_realdebrid`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        for info_hash, details in response.items():
            if "rd" not in details:
                continue

            torrent_item: TorrentItem = self.__itemsDict[info_hash]

            files = []
            self.logger.debug(torrent_item.type)
            if torrent_item.type == "series":
                for variants in details["rd"]:
                    for file_index, file in variants.items():
                        self.logger.debug(file["filename"])
                        clean_season = media.season.replace("S", "")
                        clean_episode = media.episode.replace("E", "")
                        numeric_season = int(clean_season)
                        numeric_episode = int(clean_episode)
                        if season_episode_in_filename(file["filename"], numeric_season, numeric_episode):
                            self.logger.debug("File details 2")
                            self.logger.debug(file["filename"])
                            files.append({
                                "file_index": file_index,
                                "title": file["filename"],
                                "size": file["filesize"]
                            })
            else:
                for variants in details["rd"]:
                    for file_index, file in variants.items():
                        self.logger.debug("File details 3")
                        self.logger.debug(file["filename"])
                        files.append({
                            "file_index": file_index,
                            "title": file["filename"],
                            "size": file["filesize"]
                        })

            self.__update_file_details(torrent_item, files)

    def __update_availability_alldebrid(self, response, media):
        """
        @brief Execute `__update_availability_alldebrid` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__update_availability_alldebrid`.
        @param response Runtime input parameter consumed by `__update_availability_alldebrid`.
        @param media Runtime input parameter consumed by `__update_availability_alldebrid`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if response["status"] != "success":
            self.logger.error(f"Error while updating availability: {response}")
            return

        for data in response["data"]["magnets"]:
            if not data["instant"]:
                continue

            torrent_item: TorrentItem = self.__itemsDict[data["hash"]]

            files = []
            self.__explore_folders(data["files"], files, 1, torrent_item.type, media.season,
                                   media.episode)

            self.__update_file_details(torrent_item, files)

    def __update_availability_torbox(self, response, media):
        """
        @brief Execute `__update_availability_torbox` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__update_availability_torbox`.
        @param response Runtime input parameter consumed by `__update_availability_torbox`.
        @param media Runtime input parameter consumed by `__update_availability_torbox`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        for torrent_hash, data in response.items():

            if not torrent_hash or torrent_hash not in self.__itemsDict:
                self.logger.warning(f"Hash {torrent_hash} not found in itemsDict.")
                continue
            torrent_item: TorrentItem = self.__itemsDict[torrent_hash]
            files = []

            self.__explore_folders(
                    folder=data.get("files", []),
                    files=files,
                    file_index=1,
                    type=torrent_item.type,
                    season=media.season,
                    episode=media.episode
            )
            self.__update_file_details(torrent_item, files)

    def __update_availability_premiumize(self, response):
        """
        @brief Execute `__update_availability_premiumize` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__update_availability_premiumize`.
        @param response Runtime input parameter consumed by `__update_availability_premiumize`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if response["status"] != "success":
            self.logger.error(f"Error while updating availability: {response}")
            return

        torrent_items = self.get_items()
        for i in range(len(response["response"])):
            if bool(response["response"][i]):
                torrent_items[i].availability = bool(response["transcoded"][i])


    def __update_file_details(self, torrent_item, files):
        """
        @brief Execute `__update_file_details` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__update_file_details`.
        @param torrent_item Runtime input parameter consumed by `__update_file_details`.
        @param files Runtime input parameter consumed by `__update_file_details`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if len(files) == 0:
            return

        file = max(files, key=lambda file: file["size"])
        torrent_item.availability = True
        torrent_item.file_index = file["file_index"]
        torrent_item.file_name = file["title"]
        torrent_item.size = file["size"]

    def __build_items_dict_by_infohash(self, items: List[TorrentItem]):
        """
        @brief Execute `__build_items_dict_by_infohash` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__build_items_dict_by_infohash`.
        @param items Runtime input parameter consumed by `__build_items_dict_by_infohash`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.logger.debug(f"Building items dict by infohash ({len(items)} items)")
        items_dict = dict()
        for item in items:
            if item.info_hash is not None:
                self.logger.debug(f"Adding {item.info_hash} to items dict")
                if item.info_hash in items_dict:
                    self.logger.debug(f"Duplicate info hash found: {item.info_hash}")
                items_dict[item.info_hash] = item
        return items_dict

    # Simple recursion to traverse the file structure returned by AllDebrid
    def __explore_folders(self, folder, files, file_index, type, season=None, episode=None):
        """
        @brief Execute `__explore_folders` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__explore_folders`.
        @param folder Runtime input parameter consumed by `__explore_folders`.
        @param files Runtime input parameter consumed by `__explore_folders`.
        @param file_index Runtime input parameter consumed by `__explore_folders`.
        @param type Runtime input parameter consumed by `__explore_folders`.
        @param season Runtime input parameter consumed by `__explore_folders`.
        @param episode Runtime input parameter consumed by `__explore_folders`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if type == "series":
            for file in folder:
                if "e" in file or "files" in file:
                    sub_folder = file.get("e") or file.get("files")
                    file_index = self.__explore_folders(sub_folder, files, file_index, type, season,
                                                        episode)
                    continue

                file_name = file.get("n") or file.get("name")
                file_size = file.get("s") or file.get("size", 0)
                if not file_name:
                    self.logger.warning(f"Filename missing for : {file}")
                    continue

                if season_episode_in_filename(file_name, season, episode):
                    files.append({
                        "file_index": file_index,
                        "title": file_name,
                        "size": file_size
                    })
                file_index += 1

        elif type == "movie":
            file_index = 1
            for file in folder:
                if "e" in file or "files" in file:
                    sub_folder = file.get("e") or file.get("files")
                    file_index = self.__explore_folders(sub_folder, files, file_index, type)
                    continue

                file_name = file.get("n") or file.get("name")
                file_size = file.get("s") or file.get("size", 0)

                if not file_name:
                    self.logger.warning(f"Filename missing for : {file}")
                    continue

                files.append({
                    "file_index": file_index,
                    "title": file_name,
                    "size": file_size
                })
                file_index += 1

        return file_index
