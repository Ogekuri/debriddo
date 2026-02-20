"""
@file src/debriddo/search/search_service.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: Ogekuri

import asyncio
import re
import time

from itertools import chain
from urllib.parse import parse_qs, urlparse

from RTN import parse
from unidecode import unidecode

from debriddo.search.search_indexer import SearchIndexer
from debriddo.search.search_result import SearchResult
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.detection import detect_languages
from debriddo.utils.logger import setup_logger
from debriddo.utils.string_encoding import normalize

from debriddo.search.plugins.thepiratebay_categories import thepiratebay
from debriddo.search.plugins.one337x import one337x
from debriddo.search.plugins.limetorrents import limetorrents
from debriddo.search.plugins.torrentproject import torrentproject
from debriddo.search.plugins.ilcorsaronero import ilcorsaronero
from debriddo.search.plugins.torrentz import torrentz
# from search.plugins.torrentgalaxyto import torrentgalaxy
from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy
from debriddo.search.plugins.therarbg import therarbg
from debriddo.search.plugins.ilcorsaroblu import ilcorsaroblu

from debriddo.utils.multi_thread import MULTI_THREAD, run_coroutine_in_thread

# Se non trova risultati prova una ricerca più estesa
#: @brief Exported constant `SEARCHE_FALL_BACK` used by runtime workflows.
SEARCHE_FALL_BACK = True

class SearchService:
    """@brief Class `SearchService` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
"""
    def __init__(self, config):
        """@brief Function `__init__` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param config Runtime parameter.
"""
        self.__config = config

        self.logger = setup_logger(__name__)

        self.__language_tags = {
            'en':'ENG', 
            'fr':'FRA', 
            'es':'ESP', 
            'de':'GER', 
            'it':'ITA', 
            'pt':'POR', 
            'ru':'RUS', 
            'in':'INDIAN', 
            'nl':'NLD', 
            'hu':'HUN', 
            'la':'LATIN', 
            'multi':'MULTI',
            }
        self.__default_lang_tag = self.__language_tags['en']
        self.__season_labels = {
            'it': 'Stagione',
        }

  

    async def search(self, media):
        """@brief Function `search` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param media Runtime parameter.
"""
        self.logger.debug("Started Search search for " + media.type + " " + media.titles[0])

        indexers = self.__get_indexers()
        tasks_results = []

        if isinstance(media, Movie):
            if MULTI_THREAD:
                loop = asyncio.get_event_loop()

                # Invece di eseguire le coroutine direttamente sul loop principale,
                # le "incapsuliamo" in run_in_executor, cosi ciascuna gira in un proprio thread/loop
                tasks = [loop.run_in_executor(None, run_coroutine_in_thread, self.__search_movie_indexer(media, indexer)) for indexer in indexers.values()]
                
                # Ora attendiamo i risultati. Il loop principale non si bloccherà,
                # perché quel codice gira in un thread separato.
                tasks_results = await asyncio.gather(*tasks)
            else:
                tasks = [self.__search_movie_indexer(media, indexer) for indexer in indexers.values()] 
                tasks_results = await asyncio.gather(*tasks)
        elif isinstance(media, Series):
            if MULTI_THREAD:
                loop = asyncio.get_event_loop()
                tasks = [loop.run_in_executor(None, run_coroutine_in_thread, self.__search_series_indexer(media, indexer)) for indexer in indexers.values()]
                tasks_results = await asyncio.gather(*tasks)
            else:
                tasks = [self.__search_series_indexer(media, indexer) for indexer in indexers.values()] 
                tasks_results = await asyncio.gather(*tasks)
        else:
            return []

        # concatena i risultati
        search_results = list(chain.from_iterable(tasks_results))


        start_time = time.time()
        if search_results is not None and len(search_results) > 0:
            # spost process result ############################################
            self.logger.debug("Post process " + str(len(search_results)) + " results")

            if MULTI_THREAD:
                loop = asyncio.get_event_loop()
                tasks = [loop.run_in_executor(None, run_coroutine_in_thread, self.__post_process_result(indexers, result, media)) for result in search_results]
                results = await asyncio.gather(*tasks)
            else:
                tasks = [self.__post_process_result(indexers, result, media) for result in search_results] 
                results = await asyncio.gather(*tasks)

        else:
            results = None

        if results is not None:
            self.logger.info(f"Post processed {len(results)} results for {media.titles[0]}/{media.type} in {round(time.time() - start_time, 1)} [s]")
        else: 
            self.logger.info(f"No result found for {media.titles[0]}/{media.type}")

        return results


    def __get_engine(self, engine_name):
        """@brief Function `__get_engine` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param engine_name Runtime parameter.
"""
        if engine_name == 'thepiratebay':
            return thepiratebay(self.__config)
        elif engine_name == 'one337x':
            return one337x(self.__config)
        elif engine_name == 'limetorrents':
            return limetorrents(self.__config)
        elif engine_name == 'torrentproject':
            return torrentproject(self.__config)
        elif engine_name == 'torrentz':
            return torrentz(self.__config)
        elif engine_name == 'torrentgalaxy':
            return torrentgalaxy(self.__config)
        elif engine_name == 'therarbg':
            return therarbg(self.__config)
        elif engine_name == 'ilcorsaronero':
            return ilcorsaronero(self.__config)
        elif engine_name == 'ilcorsaroblu':
            return ilcorsaroblu(self.__config)
        else:
            raise ValueError(f"Torrent Search '{engine_name}' not supported")
    

    def __get_requested_languages(self):
        """@brief Function `__get_requested_languages` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param self Runtime parameter.
@return Runtime return value.
"""
        config_languages = self.__config.get('languages')
        if isinstance(config_languages, list) and len(config_languages) > 0:
            return config_languages
        return [None]


    def __get_title_for_language(self, media, lang):
        """@brief Function `__get_title_for_language` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param media Runtime parameter.
@param lang Runtime parameter.
"""
        titles = media.titles or []
        if len(titles) == 0:
            return ""

        if lang is None:
            return titles[0]

        config_languages = self.__config.get('languages')
        if isinstance(config_languages, list) and lang in config_languages:
            lang_index = config_languages.index(lang)
            if lang_index < len(titles):
                return titles[lang_index]

        return titles[0]


    def __get_lang_tag(self, indexer_language, lang):
        """@brief Function `__get_lang_tag` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param indexer_language Runtime parameter.
@param lang Runtime parameter.
"""
        if lang is None:
            return ""

        if indexer_language != 'en' and indexer_language == lang:
            return ""

        return self.__language_tags.get(lang, self.__default_lang_tag)


    def __build_query(self, *parts):
        """@brief Function `__build_query` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param self Runtime parameter.
@param parts Runtime parameter.
@return Runtime return value.
"""
        query = " ".join(str(part) for part in parts if str(part).strip() != "")
        return normalize(query)


    def __build_query_keep_dash(self, *parts):
        """@brief Function `__build_query_keep_dash` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param self Runtime parameter.
@param parts Runtime parameter.
@return Runtime return value.
"""
        query = " ".join(str(part) for part in parts if str(part).strip() != "")
        query = unidecode(query)
        query = re.sub("'s ", ' ', query)
        query = re.sub(r'[^0-9a-zA-Z-]', ' ', query)
        query = re.sub(r' +', ' ', query)
        return query.lower().strip()


    async def __search_torrents(self, media, indexer, search_string, category):
        """@brief Function `__search_torrents` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param media Runtime parameter.
@param indexer Runtime parameter.
@param search_string Runtime parameter.
@param category Runtime parameter.
"""
        list_of_dicts = await indexer.engine.search(search_string, category)
        if list_of_dicts is None or len(list_of_dicts) == 0:
            return []

        torrents = self.__get_torrents_from_list_of_dicts(media, indexer, list_of_dicts)
        if torrents is None or type(torrents) is not list or len(torrents) == 0:
            return []

        return torrents


    def __log_query_result(
        self,
        search_string,
        indexer,
        category,
        query_start_time,
        result_count,
    ):
        """@brief Function `__log_query_result` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param search_string Runtime parameter.
@param indexer Runtime parameter.
@param category Runtime parameter.
@param query_start_time Runtime parameter.
@param result_count Runtime parameter.
"""
        elapsed = round(time.time() - query_start_time, 1)
        if result_count > 0:
            self.logger.info(
                f"Found {result_count} for '{search_string}' @ "
                f"{indexer.engine_name}/{category} in {elapsed} [s]"
            )
        else:
            self.logger.info(
                f"No results found for '{search_string}' @ "
                f"{indexer.engine_name}/{category} in {elapsed} [s]"
            )


    async def __search_movie_indexer(self, movie, indexer):
        """@brief Function `__search_movie_indexer` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param movie Runtime parameter.
@param indexer Runtime parameter.
"""
        results = []
        indexer_start_time = time.time()
        base_title = movie.titles[0] if movie.titles else ""
        search_string = base_title
        category = str(indexer.movie_search_capatabilities)
        requested_languages = self.__get_requested_languages()
        primary_results_found = False

        for lang in requested_languages:
            try:
                title = self.__get_title_for_language(movie, lang)
                lang_tag = self.__get_lang_tag(indexer.language, lang)
                search_string = self.__build_query(title, movie.year, lang_tag)

                query_start_time = time.time()
                torrents = await self.__search_torrents(movie, indexer, search_string, category)
                self.__log_query_result(
                    search_string,
                    indexer,
                    category,
                    query_start_time,
                    len(torrents),
                )
                if len(torrents) > 0:
                    results.extend(torrents)
                    primary_results_found = True
            except Exception:
                self.logger.exception(
                    f"An exception occured while searching for a movie on Search with indexer {indexer.title} and "
                    f"language {lang}.")

        if SEARCHE_FALL_BACK and not primary_results_found:
            for lang in requested_languages:
                try:
                    title = self.__get_title_for_language(movie, lang)
                    lang_tag = self.__get_lang_tag(indexer.language, lang)
                    search_string = self.__build_query(title, lang_tag)

                    query_start_time = time.time()
                    torrents = await self.__search_torrents(movie, indexer, search_string, category)
                    self.__log_query_result(
                        search_string,
                        indexer,
                        category,
                        query_start_time,
                        len(torrents),
                    )
                    if len(torrents) > 0:
                        results.extend(torrents)
                except Exception:
                    self.logger.exception(
                        f"An exception occured while searching for a movie on Search with indexer {indexer.title} and "
                        f"language {lang}.")

        self.logger.debug(
            f"Movie search completed with {len(results)} results for "
            f"{indexer.engine_name}/{category} in "
            f"{round(time.time() - indexer_start_time, 1)} [s]"
        )

        return results
    

    async def __search_series_indexer(self, series, indexer):
        """@brief Function `__search_series_indexer` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param series Runtime parameter.
@param indexer Runtime parameter.
"""
        results = []
        indexer_start_time = time.time()
        base_title = series.titles[0] if series.titles else ""
        search_string = base_title
        category = str(indexer.tv_search_capatabilities)
        requested_languages = self.__get_requested_languages()
        primary_results_found = False

        for lang in requested_languages:
            try:
                # Esempio balordo:
                # Arcane.S02E01-03.WEBDL 1080p Ita Eng x264-NAHOM
                # Arcane.S02E04-06.WEBDL 1080p Ita Eng x264-NAHOM
                # Arcane.S02E07-09.WEBDL 1080p Ita Eng x264-NAHOM
                # Arcane.S02.720p.ITA-ENG.MULTI.WEBRip.x265.AAC-V3SP4EV3R
                #
                # Se cerco S02 E02 non lo trovo da nessuna parte, ma è presente in 2 file
                # Se cerco S02 E04 lo trova in un file, ma è presente in 2 file
                # Se cerco S02 trova 4 file ma è presente in 2 file
                #
                # Decido di prendere sempe tutti i risultati e vedere se poi dopo è sufficiente filtrarli
                #
                # se non ci sono risultati riprova omettendo l'episodio
                # perché ci sono i torrent con l'intera serie inclusa
                # bisogna poi cercare il file corretto

                title = self.__get_title_for_language(series, lang)
                lang_tag = self.__get_lang_tag(indexer.language, lang)
                episode_search = self.__build_query(title, series.season + series.episode, lang_tag)
                pack_search = self.__build_query_keep_dash(title, series.season + 'E01-', lang_tag)
                primary_candidates = [episode_search, pack_search]

                if lang is not None:
                    season_label = self.__season_labels.get(lang, "Season")
                    season_number = int(series.season[1:])
                    season_search = self.__build_query(title, season_label, season_number, lang_tag)
                    primary_candidates.append(season_search)

                for candidate in primary_candidates:
                    search_string = candidate
                    query_start_time = time.time()
                    torrents = await self.__search_torrents(series, indexer, search_string, category)
                    self.__log_query_result(
                        search_string,
                        indexer,
                        category,
                        query_start_time,
                        len(torrents),
                    )
                    if len(torrents) > 0:
                        results.extend(torrents)
                        primary_results_found = True

            except Exception:
                self.logger.exception(
                    f"An exception occured while searching for a series on Search with indexer {indexer.title} and language {lang}.")

        if SEARCHE_FALL_BACK and not primary_results_found:
            for lang in requested_languages:
                try:
                    title = self.__get_title_for_language(series, lang)
                    lang_tag = self.__get_lang_tag(indexer.language, lang)
                    search_string = self.__build_query(title, lang_tag)

                    query_start_time = time.time()
                    torrents = await self.__search_torrents(series, indexer, search_string, category)
                    self.__log_query_result(
                        search_string,
                        indexer,
                        category,
                        query_start_time,
                        len(torrents),
                    )
                    if len(torrents) > 0:
                        results.extend(torrents)
                except Exception:
                    self.logger.exception(
                        f"An exception occured while searching for a series on Search with indexer {indexer.title} and language {lang}.")

        self.logger.debug(
            f"Series search completed with {len(results)} results for "
            f"{indexer.engine_name}/{category} in "
            f"{round(time.time() - indexer_start_time, 1)} [s]"
        )

        return results


    def __get_indexers(self):
        """@brief Function `__get_indexers` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param self Runtime parameter.
@return Runtime return value.
"""
        try:
            search_indexers = self.__get_indexer_from_engines(self.__config['engines'])
            # creiamo un dizionario con title come chiave
            indexers = {si.engine_name: si for si in search_indexers}
            return indexers
        except Exception:
            self.logger.exception("An exception occured while getting indexers from Search.")
            return {}


    def __get_indexer_from_engines(self, engines):
        """@brief Function `__get_indexer_from_engines` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param engines Runtime parameter.
"""
        indexer_list = []
        id = 0
        for engine_name in engines:
            indexer = SearchIndexer()
            engine = self.__get_engine(engine_name)
            supported_categories = engine.supported_categories

            indexer.engine = engine
            indexer.language = engine.language

            indexer.title = engine.name
            indexer.id = id
            indexer.engine_name = engine_name

            if ('movies' in supported_categories) and (supported_categories['movies'] is not None):
                indexer.movie_search_capatabilities = 'movies'
            else:
                if ('all' in supported_categories) and (supported_categories['all'] is not None):
                    indexer.movie_search_capatabilities = 'all'
                else:
                    self.logger.info(f"Movie search not available for {indexer.title}")

            if ('tv' in supported_categories) and (supported_categories['tv'] is not None):
                indexer.tv_search_capatabilities = 'tv'
            else:
                if ('all' in supported_categories) and (supported_categories['all'] is not None):
                    indexer.movie_search_capatabilities = 'all'
                else:
                    self.logger.info(f"TV search not available for {indexer.title}")

            indexer_list.append(indexer)
            
            self.logger.debug(f"Indexer: {indexer.id} - {indexer.engine_name} - {indexer.title} - {indexer.language} - {indexer.movie_search_capatabilities} - {indexer.tv_search_capatabilities}")

            id += 1

        return indexer_list


    def __get_torrents_from_list_of_dicts(self, media, indexer, list_of_dicts):
        """@brief Function `__get_torrents_from_list_of_dicts` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param media Runtime parameter.
@param indexer Runtime parameter.
@param list_of_dicts Runtime parameter.
"""
        result_list = []
        
        for item in list_of_dicts:
            result = SearchResult()

            result.seeders = item['seeds']
            if int(result.seeders) <= 0:
                continue

            result.raw_title = item['name']
            result.title = item['name']
            result.size = item['size']
            result.indexer = indexer.title              # engine name 'Il Corsaro Nero' 
            result.engine_name = indexer.engine_name    # engine type 'ilcorsaronero' (minuscolo)
            result.type = media.type                    # series or movie
            result.privacy = 'public'                   # public or private (determina se sarà o meno salvato in cache)

            result.magnet = None        # processed on __post_process_results after getting pages
            result.link = item['link']  # shoud be content the link of magnet or .torrent file 
                                        # but NOW contain the web page or magnet, will be __post_process_results
            result.info_hash = None     # processed on __post_process_results after getting pages

            result_list.append(result)

        return result_list


    def __is_magnet_link(self, link):
        """@brief Function `__is_magnet_link` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param link Runtime parameter.
"""
        # Check if link inizia con "magnet:?"
        return link.startswith("magnet:?")


    def __extract_info_hash(self, magnet_link):
        """@brief Function `__extract_info_hash` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param magnet_link Runtime parameter.
"""
        # parse
        parsed = urlparse(magnet_link)
        
        # extract 'xt'
        params = parse_qs(parsed.query)
        xt = params.get("xt", [None])[0]
        
        if xt and xt.startswith("urn:btih:"):
            # remove prefix "urn:btih:"
            info_hash = xt.split("urn:btih:")[1]
            return info_hash
        else:
            raise ValueError("Magnet link invalid")


    async def __post_process_result(self, indexers, result, media):
        """@brief Function `__post_process_result` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param indexers Runtime parameter.
@param result Runtime parameter.
@param media Runtime parameter.
"""
        if self.__is_magnet_link(result.link):
            result.magnet = result.link
        else:
            start_time = time.time()
            indexer = indexers[result.engine_name]
            res_link = await indexer.engine.download_torrent(result.link)
            if res_link is not None and self.__is_magnet_link(res_link):
                result.magnet = res_link
                result.link = result.magnet
            else:
                # raise Exception('Error, please fill a bug report!')
                # se non riesce a scarica il file ritorna None
                return None
            self.logger.debug(f"Download magnet of result {result.title} @ {result.engine_name} in {round(time.time() - start_time, 1)} [s]")

        # parse RAW title to detect languages
        parsed_result = parse(result.raw_title)
        # result.languages = [languages.get(name=language).alpha2 for language in parsed_result.language]
        result.parsed_data = parsed_result
        # TODO: replace with parsed_result.lang_codes when RTN is updated
        result.languages = detect_languages(result.raw_title)

        result.type = media.type
        result.info_hash = self.__extract_info_hash(result.magnet)

        return result
