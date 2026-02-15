"""
@file src/debriddo/utils/general.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from RTN import parse

from debriddo.utils.logger import setup_logger

logger = setup_logger(__name__)

video_formats = {".mkv", ".mp4", ".avi", ".mov", ".flv", ".wmv", ".webm", ".mpg", ".mpeg", ".m4v", ".3gp", ".3g2",
                 ".ogv",
                 ".ogg", ".drc", ".gif", ".gifv", ".mng", ".avi", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".asf",
                 ".amv", ".m4p", ".m4v", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mpg", ".mpeg", ".m2v", ".m4v",
                 ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"}


def season_episode_in_filename(filename, season, episode):
    """
    @brief Execute `season_episode_in_filename` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param filename Runtime input parameter consumed by `season_episode_in_filename`.
    @param season Runtime input parameter consumed by `season_episode_in_filename`.
    @param episode Runtime input parameter consumed by `season_episode_in_filename`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    if not is_video_file(filename):
        return False
    parsed_name = parse(filename)
    return int(season.replace("S", "")) in parsed_name.seasons and int(episode.replace("E", "")) in parsed_name.episodes


def get_info_hash_from_magnet(magnet: str):
    """
    @brief Execute `get_info_hash_from_magnet` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param magnet Runtime input parameter consumed by `get_info_hash_from_magnet`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    exact_topic_index = magnet.find("xt=")
    if exact_topic_index == -1:
        logger.debug(f"No exact topic in magnet {magnet}")
        return None

    exact_topic_substring = magnet[exact_topic_index:]
    end_of_exact_topic = exact_topic_substring.find("&")
    if end_of_exact_topic != -1:
        exact_topic_substring = exact_topic_substring[:end_of_exact_topic]

    info_hash = exact_topic_substring[exact_topic_substring.rfind(":") + 1:]

    return info_hash.lower()


def is_video_file(filename):
    """
    @brief Execute `is_video_file` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param filename Runtime input parameter consumed by `is_video_file`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    extension_idx = filename.rfind(".")
    if extension_idx == -1:
        return False

    return filename[extension_idx:] in video_formats
