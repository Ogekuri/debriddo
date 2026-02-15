"""
@file src/debriddo/utils/filter_results.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import re

from RTN import title_match, RTN, DefaultRanking, SettingsModel, sort_torrents
from RTN.exceptions import GarbageTorrent
from debriddo.utils.filter.language_filter import LanguageFilter
from debriddo.utils.filter.max_size_filter import MaxSizeFilter
from debriddo.utils.filter.quality_exclusion_filter import QualityExclusionFilter
from debriddo.utils.filter.results_per_quality_filter import ResultsPerQualityFilter
from debriddo.utils.filter.title_exclusion_filter import TitleExclusionFilter
from debriddo.utils.logger import setup_logger

logger = setup_logger(__name__)

quality_order = {"4k": 0, "2160p": 0, "1080p": 1, "720p": 2, "480p": 3}
season_labels = {
    "en": "Season",
    "it": "Stagione",
    "fr": "Saison",
    "es": "Temporada",
    "de": "Staffel",
    "pt": "Temporada",
    "ru": "Sezon",
    "in": "Season",
    "nl": "Seizoen",
    "hu": "Evad",
    "la": "Season",
    "multi": "Season",
}

complete_labels = {
    "en": "Complete",
    "it": "Completa",
    "fr": "Complete",
    "es": "Completa",
    "de": "Komplett",
    "pt": "Completa",
    "ru": "Polnyj",
    "in": "Complete",
    "nl": "Compleet",
    "hu": "Teljes",
    "la": "Complete",
    "multi": "Complete",
}


def _match_complete_season(raw_title, numeric_season):
    """
    @brief Execute `_match_complete_season` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param raw_title Runtime input parameter consumed by `_match_complete_season`.
    @param numeric_season Runtime input parameter consumed by `_match_complete_season`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    title = str(raw_title or "")

    # Localized complete season must use season/complete labels from the same language.
    # Support both "Season Snn ... COMPLETE" and "Season d ... COMPLETE" (numeric) formats
    for language, season_label in season_labels.items():
        complete_label = complete_labels.get(language)
        if complete_label is None:
            continue

        # Pattern 1: Season Snn ... COMPLETE (e.g., "Season S03 ... COMPLETE")
        season_token_snn = r"(?:S\s*0?" + str(numeric_season) + r")"
        label_match_snn = re.compile(
            r"\b"
            + re.escape(season_label)
            + r"\s+"
            + season_token_snn
            + r"\b.*?\b"
            + re.escape(complete_label)
            + r"\b",
            re.IGNORECASE,
        )
        if label_match_snn.search(title):
            return True

        # Pattern 2: Season d ... COMPLETE (e.g., "Stagione 3 ... COMPLETA")
        season_token_numeric = r"(?:0?" + str(numeric_season) + r")"
        label_match_numeric = re.compile(
            r"\b"
            + re.escape(season_label)
            + r"\s+"
            + season_token_numeric
            + r"\b.*?\b"
            + re.escape(complete_label)
            + r"\b",
            re.IGNORECASE,
        )
        if label_match_numeric.search(title):
            return True

    return False


def _match_episode_range_pack(raw_title, numeric_season, numeric_episode):
    """
    @brief Execute `_match_episode_range_pack` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param raw_title Runtime input parameter consumed by `_match_episode_range_pack`.
    @param numeric_season Runtime input parameter consumed by `_match_episode_range_pack`.
    @param numeric_episode Runtime input parameter consumed by `_match_episode_range_pack`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    title = str(raw_title or "")
    pattern = re.compile(
        r"\bS0?(?P<season>\d{1,2})(?:\s+|-)?E0?(?P<episode_start>\d{1,3})\s*-\s*(?:E0?)?(?P<episode_end>\d{1,3})\b",
        re.IGNORECASE,
    )
    for match in pattern.finditer(title):
        season = int(match.group("season"))
        episode_start = int(match.group("episode_start"))
        episode_end = int(match.group("episode_end"))
        if season != numeric_season:
            continue
        if episode_start <= numeric_episode <= episode_end:
            return True
    return False


def _match_season_episode_pair(raw_title, numeric_season, numeric_episode):
    """
    @brief Execute `_match_season_episode_pair` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param raw_title Runtime input parameter consumed by `_match_season_episode_pair`.
    @param numeric_season Runtime input parameter consumed by `_match_season_episode_pair`.
    @param numeric_episode Runtime input parameter consumed by `_match_season_episode_pair`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    title = str(raw_title or "")
    season_episode_match = re.compile(
        r"\bS0?"
        + str(numeric_season)
        + r"(?:\s*-\s*|\s+)?E0?"
        + str(numeric_episode)
        + r"\b",
        re.IGNORECASE,
    )
    return season_episode_match.search(title) is not None


def _match_title_with_season(raw_title, media_title, numeric_season):
    """
    Match title followed by season in three forms for series:
    1. <title>.+Snn (basic season format)
    2. <title>.+Season Snn (localized season label with Snn)
    3. <title>.+Season d (localized season label with numeric season)
    """
    title = str(raw_title or "")
    # Normalize title to handle dots, spaces, underscores as separators
    # Replace each word separator in media_title with flexible separator pattern
    normalized_title = re.escape(str(media_title or "")).replace(r"\ ", r"[\s\._-]+")

    # Pattern 1: <title>.+Snn (e.g., "Person of Interest ... S03" or "Person.Of.Interest.S03")
    pattern1 = re.compile(
        r"\b" + normalized_title + r".+\bS0?" + str(numeric_season) + r"\b",
        re.IGNORECASE,
    )
    if pattern1.search(title):
        return True

    # Pattern 2 and 3: <title>.+Season Snn or <title>.+Season d (localized)
    for language, season_label in season_labels.items():
        # Pattern 2: <title>.+Season Snn (e.g., "Person of Interest ... Season S03")
        pattern2 = re.compile(
            r"\b"
            + normalized_title
            + r".+"
            + re.escape(season_label)
            + r"\s+S0?"
            + str(numeric_season)
            + r"\b",
            re.IGNORECASE,
        )
        if pattern2.search(title):
            return True

        # Pattern 3: <title>.+Season d (e.g., "Person of Interest ... Stagione 3")
        pattern3 = re.compile(
            r"\b"
            + normalized_title
            + r".+"
            + re.escape(season_label)
            + r"\s+0?"
            + str(numeric_season)
            + r"\b",
            re.IGNORECASE,
        )
        if pattern3.search(title):
            return True

    return False


def sort_quality(item):
    # if item.parsed_data.data.resolution is None or item.parsed_data.data.resolution == "unknown" or item.parsed_data.data.resolution == "":
    #     return float('inf'), True

    # # TODO: first resolution?
    # return quality_order.get(item.parsed_data.data.resolution[0],
    #                          float('inf')), item.parsed_data.data.resolution is None

    # Controlla la presenza di parsed_data e data
    """
    @brief Execute `sort_quality` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param item Runtime input parameter consumed by `sort_quality`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    if not hasattr(item, 'parsed_data') or not hasattr(item.parsed_data, 'data') or not hasattr(item.parsed_data.data, 'resolution'):
        return float('inf'), True   # True = non trovato

    resolution = item.parsed_data.data.resolution

    # Gestione dei casi con risoluzione mancante o sconosciuta
    if resolution is None or resolution == "unknown" or resolution == "":
        return float('inf'), True   # True = non trovato

    # Ritorna il valore di quality_order con fallback a infinito
    return quality_order.get(resolution, float('inf')), False   # False = trovato


def items_sort(items, config):

    
    """
    @brief Execute `items_sort` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param items Runtime input parameter consumed by `items_sort`.
    @param config Runtime input parameter consumed by `items_sort`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    settings = SettingsModel(
        require=[],
        exclude=config['exclusionKeywords'] + config['exclusion'],
        preferred=[],
        # custom_ranks={
        #     "uhd": CustomRank(enable=True, fetch=True, rank=200),
        #     "hdr": CustomRank(enable=True, fetch=True, rank=100),
        # }
    )
    
    # Se genera l'eccezione poi l'ordinamento dei TorrentItems basato sui Torrent non funziona
    # if rank < self.settings.options["remove_ranks_under"]:
    # raise GarbageTorrent(f"'{raw_title}' does not meet the minimum rank requirement, got rank of {rank}")
    #
    # maximun negative value => non ne leva nessuno
    #
    # default: remove_ranks_under = -10000,
    settings.options.remove_ranks_under = -2147483648   # 32 bit?

    rtn = RTN(settings=settings, ranking_model=DefaultRanking())
    
    # torrents = [rtn.rank(item.raw_title, item.info_hash) for item in items]
    torrents = []
    for item in items:
        try:
            torrent = rtn.rank(item.raw_title, item.info_hash, remove_trash=False)
            torrents.append(torrent)
        except GarbageTorrent as e:
            logger.error(f"Error while ranking the torrent: {item.raw_title} - {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error for torrent: {item.raw_title}", exc_info=e)
    
    sorted_torrents = sort_torrents(set(torrents))

    for key, value in sorted_torrents.items():
        index = next((i for i, item in enumerate(items) if item.info_hash == key), None)
        if index is not None:
            items[index].parsed_data = value

    if config['sort'] == "quality":
        return sorted(items, key=sort_quality)
    if config['sort'] == "sizeasc":
        return sorted(items, key=lambda x: int(x.size))
    if config['sort'] == "sizedesc":
        return sorted(items, key=lambda x: int(x.size), reverse=True)
    if config['sort'] == "qualitythensize":
        return sorted(items, key=lambda x: (sort_quality(x), -int(x.size)))
    return items


# def filter_season_episode(items, season, episode, config):
#     filtered_items = []
#     for item in items:
#         if config['language'] == "ru":
#             if "S" + str(int(season.replace("S", ""))) + "E" + str(
#                     int(episode.replace("E", ""))) not in item['title']:
#                 if re.search(rf'\bS{re.escape(str(int(season.replace("S", ""))))}\b', item['title']) is None:
#                     continue
#         if re.search(rf'\b{season}\s?{episode}\b', item['title']) is None:
#             if re.search(rf'\b{season}\b', item['title']) is None:
#                 continue

#         filtered_items.append(item)
#     return filtered_items

# TODO: not needed anymore because of RTN
def filter_out_non_matching(items, season, episode):
    """
    @brief Execute `filter_out_non_matching` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param items Runtime input parameter consumed by `filter_out_non_matching`.
    @param season Runtime input parameter consumed by `filter_out_non_matching`.
    @param episode Runtime input parameter consumed by `filter_out_non_matching`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    filtered_items = []
    for item in items:
        # logger.debug(item.parsed_data)
        clean_season = season.replace("S", "")
        clean_episode = episode.replace("E", "")
        numeric_season = int(clean_season)
        numeric_episode = int(clean_episode)
        try:
            if _match_season_episode_pair(item.raw_title, numeric_season, numeric_episode):
                filtered_items.append(item)
                continue
            if _match_episode_range_pack(item.raw_title, numeric_season, numeric_episode):
                filtered_items.append(item)
                continue
            if _match_complete_season(item.raw_title, numeric_season):
                filtered_items.append(item)
                continue
            if len(item.parsed_data.seasons) == 0 and len(item.parsed_data.episodes) == 0:
                continue
            if numeric_season in item.parsed_data.seasons and numeric_episode in item.parsed_data.episodes:
                filtered_items.append(item)
                continue
        except Exception as e:
            logger.error(f"Error while filtering out non matching torrents", exc_info=e)
    return filtered_items


def remove_non_matching_title(items, titles, media):
    """
    @brief Execute `remove_non_matching_title` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param items Runtime input parameter consumed by `remove_non_matching_title`.
    @param titles Runtime input parameter consumed by `remove_non_matching_title`.
    @param media Runtime input parameter consumed by `remove_non_matching_title`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    logger.debug(f"Filtering by title: {titles}")
    # default: threshold: float = 0.85
    threshold = float(0.5)
    filtered_items = []

    for item in items:
        item_matched = False
        for title in titles:
            # For series, use season-aware matching
            if media.type == "series":
                clean_season = media.season.replace("S", "")
                numeric_season = int(clean_season)

                # Check if title has season-aware match (validates season is correct)
                if _match_title_with_season(item.raw_title, title, numeric_season):
                    item_matched = True
                    break

                # Generic title match only if no season info in raw_title
                # (fallback for items without explicit season in title)
                if title_match(title, item.parsed_data.parsed_title, threshold):
                    # Check if raw_title contains any season pattern
                    has_season_pattern = bool(re.search(r'\bS\d{1,2}\b', item.raw_title, re.IGNORECASE))
                    for season_label in season_labels.values():
                        if re.search(r'\b' + re.escape(season_label) + r'\s+\d{1,2}\b', item.raw_title, re.IGNORECASE):
                            has_season_pattern = True
                            break

                    # Only accept generic match if no season pattern found in title
                    if not has_season_pattern:
                        item_matched = True
                        break
            else:
                # For movies, use generic title match
                if title_match(title, item.parsed_data.parsed_title, threshold):
                    item_matched = True
                    break

        if item_matched:
            filtered_items.append(item)

    return filtered_items


def filter_items(items, media, config):
    # vengono processati nell'ordine in cui sono dichiarati
    """
    @brief Execute `filter_items` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param items Runtime input parameter consumed by `filter_items`.
    @param media Runtime input parameter consumed by `filter_items`.
    @param config Runtime input parameter consumed by `filter_items`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    filters = {
        "languages": LanguageFilter(config),
        "maxSize": MaxSizeFilter(config, media.type),  # Max size filtering only happens for movies, so it
        "exclusionKeywords": TitleExclusionFilter(config),
        "exclusion": QualityExclusionFilter(config),
        "resultsPerQuality": ResultsPerQualityFilter(config)
    }

    # Filtering out 100% non-matching for series
    logger.debug(f"Item count before filtering: {len(items)}")
    if media.type == "series":
        logger.debug(f"Filtering out non matching series torrents")
        items = filter_out_non_matching(items, media.season, media.episode)
        logger.debug(f"Item count changed to {len(items)}")
        logger.debug("Filter results for season: " + media.season + ", spisode: " + media.episode)

    # TODO: is titles[0] always the correct title? Maybe loop through all titles and get the highest match?
    items = remove_non_matching_title(items, media.titles, media)
    logger.debug(f"Item count changed to {len(items)}")

    for filter_name, filter_instance in filters.items():
        try:
            if len(items) > 0:  # finché ci sono risultati
                if filter_name == "languages" and not config.get("languages"):
                    logger.debug("Skipping language filtering: no languages configured")
                    continue
                logger.debug(f"Filtering by {filter_name}: " + str(config[filter_name]))
                new_items = filter_instance(items)
                if len(new_items) > 0:
                    items = new_items
                else:
                    # per esempio se ci sono solo versioni in inglese, le tiene e ritorna quelle
                    logger.warning(f"Ignoring filterning by {filter_name} that cause 0 results")
                logger.debug(f"Item count changed to {len(items)}")
        except Exception as e:
            logger.error(f"Error while filtering by {filter_name}", exc_info=e)
    logger.debug(f"Item count after filtering: {len(items)}")
    logger.debug("Finished filtering torrents")

    return items


def sort_items(items, config):
    """
    @brief Execute `sort_items` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param items Runtime input parameter consumed by `sort_items`.
    @param config Runtime input parameter consumed by `sort_items`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    if config['sort'] is not None:
        return items_sort(items, config)
    else:
        return items
