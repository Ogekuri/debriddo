# VERSION: 0.0.33
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import re

from RTN import title_match, RTN, DefaultRanking, SettingsModel, sort_torrents
from RTN.exceptions import GarbageTorrent
from utils.filter.language_filter import LanguageFilter
from utils.filter.max_size_filter import MaxSizeFilter
from utils.filter.quality_exclusion_filter import QualityExclusionFilter
from utils.filter.results_per_quality_filter import ResultsPerQualityFilter
from utils.filter.title_exclusion_filter import TitleExclusionFilter
from utils.logger import setup_logger

logger = setup_logger(__name__)

quality_order = {"4k": 0, "2160p": 0, "1080p": 1, "720p": 2, "480p": 3}


def sort_quality(item):
    # if item.parsed_data.data.resolution is None or item.parsed_data.data.resolution == "unknown" or item.parsed_data.data.resolution == "":
    #     return float('inf'), True

    # # TODO: first resolution?
    # return quality_order.get(item.parsed_data.data.resolution[0],
    #                          float('inf')), item.parsed_data.data.resolution is None

    # Controlla la presenza di parsed_data e data
    if not hasattr(item, 'parsed_data') or not hasattr(item.parsed_data, 'data') or not hasattr(item.parsed_data.data, 'resolution'):
        return float('inf'), True   # True = non trovato

    resolution = item.parsed_data.data.resolution

    # Gestione dei casi con risoluzione mancante o sconosciuta
    if resolution is None or resolution == "unknown" or resolution == "":
        return float('inf'), True   # True = non trovato

    # Ritorna il valore di quality_order con fallback a infinito
    return quality_order.get(resolution, float('inf')), False   # False = trovato


def items_sort(items, config):

    
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
            torrent = rtn.rank(item.raw_title, item.info_hash, False) # remove_trash: bool = False
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
    logger.debug("Filter results for season: " + season + ", spisode: " + episode)
    filtered_items = []
    for item in items:
        # logger.debug(item.parsed_data)
        clean_season = season.replace("S", "")
        clean_episode = episode.replace("E", "")
        numeric_season = int(clean_season)
        numeric_episode = int(clean_episode)
        try:
            # fix brutto per i deficienti (Stagione 1 / Stagione 01 / Season 1 / Season 01)
            pattern = re.compile(r'stagione\s0?' + str(numeric_season), re.IGNORECASE)
            if pattern.search(item.raw_title):
                filtered_items.append(item)
                continue
            pattern = re.compile(r'season\s0?' + str(numeric_season), re.IGNORECASE)
            if pattern.search(item.raw_title):
                filtered_items.append(item)
                continue
            if len(item.parsed_data.seasons) == 0 and len(item.parsed_data.episodes) == 0:
                continue
            # torrent con stagione completa (manca l'E??)
            if len(item.parsed_data.episodes) == 0 and numeric_season in item.parsed_data.seasons:
                filtered_items.append(item)
                continue
            if numeric_season in item.parsed_data.seasons and numeric_episode in item.parsed_data.episodes:
                filtered_items.append(item)
                continue
        except Exception as e:
            logger.error(f"Error while filtering out non matching torrents", exc_info=e)
    return filtered_items


def remove_non_matching_title(items, titles):
    logger.debug(f"Filtering by title: {titles}")
    # default: threshold: float = 0.85
    threshold = float(0.5)
    filtered_items = []
    for item in items:
        for title in titles:
            if not title_match(title, item.parsed_data.parsed_title, threshold):
                continue

            filtered_items.append(item)
            break

    return filtered_items


def filter_items(items, media, config):
    # vengono processati nell'ordine in cui sono dichiarati
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

    # TODO: is titles[0] always the correct title? Maybe loop through all titles and get the highest match?
    items = remove_non_matching_title(items, media.titles)
    logger.debug(f"Item count changed to {len(items)}")

    for filter_name, filter_instance in filters.items():
        try:
            if len(items) > 0:  # finché ci sono risultati
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
    if config['sort'] is not None:
        return items_sort(items, config)
    else:
        return items
