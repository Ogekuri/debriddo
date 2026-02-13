# VERSION: 0.0.34
# AUTHORS: Ogekuri

import re
import time
import xml.etree.ElementTree as ET

import asyncio

from debriddo.search.search_indexer import SearchIndexer
from debriddo.search.search_result import SearchResult
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.detection import detect_languages
from debriddo.utils.logger import setup_logger
from debriddo.utils.string_encoding import normalize

import time
import xml.etree.ElementTree as ET

from RTN import parse

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

from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor

from itertools import chain
from debriddo.utils.multi_thread import MULTI_THREAD, run_coroutine_in_thread

# Se non trova risultati prova una ricerca più estesa
SEARCHE_FALL_BACK = True

class SearchService:
    def __init__(self, config):
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

  

    async def search(self, media):
        self.logger.debug("Started Search search for " + media.type + " " + media.titles[0])

        indexers = self.__get_indexers()

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
    

    async def __search_movie_indexer(self, movie, indexer):
        # get titles and languages
        if indexer.language == "any":
            languages = movie.languages
            titles = movie.titles
        else:
            index_of_language = [index for index, lang in enumerate(movie.languages) if lang == indexer.language]
            languages = [movie.languages[index] for index in index_of_language]
            titles = [movie.titles[index] for index in index_of_language]

        results = []
        start_time = time.time()
        base_title = movie.titles[0] if movie.titles else ""
        search_string = None
        category = str(indexer.movie_search_capatabilities)

        index = 0
        for lang in languages:
            try:
                title = titles[index]
                lang_tag = self.__language_tags[languages[index]]

                search_string = str(title + ' ' + movie.year  + ' ' +  lang_tag)
                if indexer.language == languages[index]:
                    search_string = str(title + ' ' + movie.year)   # no language tag for native language indexer
                search_string = normalize(search_string)
                category = str(indexer.movie_search_capatabilities)
                list_of_dicts = await indexer.engine.search(search_string, category)
                if list_of_dicts is not None and len(list_of_dicts) > 0:
                    torrents = self.__get_torrents_from_list_of_dicts(movie, indexer, list_of_dicts)
                    if torrents is not None and type(torrents) is list and len(torrents) >0:
                        results.extend(torrents)
                elif SEARCHE_FALL_BACK:
                    # se non ci sono risultati prova una ricerca più grossolana o in inglese (omette la lingua)
                    search_string = str(title + ' ' + movie.year)
                    if indexer.language == languages[index]:
                        search_string = str(title)   # no language tag for native language indexer
                    search_string = normalize(search_string)
                    category = str(indexer.movie_search_capatabilities)
                    list_of_dicts = await indexer.engine.search(search_string, category)
                    if list_of_dicts is not None and len(list_of_dicts) > 0:
                        torrents = self.__get_torrents_from_list_of_dicts(movie, indexer, list_of_dicts)
                        if torrents is not None and type(torrents) is list and len(torrents) >0:
                            results.extend(torrents)
                
            except Exception:
                self.logger.exception(
                    f"An exception occured while searching for a movie on Search with indexer {indexer.title} and "
                    f"language {lang}.")
            
            index = index + 1
                
        if search_string is None:
            search_string = base_title

        if len(results) > 0:
            self.logger.info(f"Found {len(results)} for '{search_string}' @ {indexer.engine_name}/{category} in {round(time.time() - start_time, 1)} [s]")
        else:
            self.logger.info(f"No results found for '{search_string}' @ {indexer.engine_name}/{category} in {round(time.time() - start_time, 1)} [s]")

        return results
    

    async def __search_series_indexer(self, series, indexer):
        # get titles and languages
        if indexer.language == "any":
            languages = series.languages
            titles = series.titles
        else:
            index_of_language = [index for index, lang in enumerate(series.languages) if lang == indexer.language]
            languages = [series.languages[index] for index in index_of_language]
            titles = [series.titles[index] for index in index_of_language]

        results = []
        start_time = time.time()
        base_title = series.titles[0] if series.titles else ""
        search_string = None
        category = str(indexer.tv_search_capatabilities)

        index = 0
        for lang in languages:
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

                title = titles[index]
                lang_tag = self.__language_tags[languages[index]]

                search_string = str(title + ' ' + series.season + series.episode + ' ' + lang_tag)
                if indexer.language == languages[index]:
                     search_string = str(title + ' ' + series.season + series.episode)   # no language tag for native language indexer
                #search_string = str(title + ' ' + series.season + ' ' + lang_tag)
                #if indexer.language == languages[index]:
                #    search_string = str(title + ' ' + series.season)   # no language tag for native language indexer
                search_string = normalize(search_string)
                category = str(indexer.tv_search_capatabilities)
                list_of_dicts = await indexer.engine.search(search_string, category)
                if list_of_dicts is not None and len(list_of_dicts) > 0:
                    torrents = self.__get_torrents_from_list_of_dicts(series, indexer, list_of_dicts)
                    if torrents is not None and type(torrents) is list and len(torrents) >0:
                        results.extend(torrents)
                elif SEARCHE_FALL_BACK:
                    # se non ci sono risultati prova una ricerca più grossolana o in inglese

                    full_season = f"Season {int(series.season[1:])}"
                    if indexer.language == 'it' or indexer.language == 'it':
                        full_season = f"Stagione {int(series.season[1:])}"
                    search_string = str(title + ' ' + full_season + ' ' + lang_tag)
                    if indexer.language == languages[index]:
                        search_string = str(title + ' ' + full_season)   # no language tag for native language indexer

                    #search_string = str(title + ' ' + series.season  + ' ' + self.__default_lang_tag)
                    #if indexer.language == languages[index]:
                    #    search_string = str(title)   # no language tag for native language indexer
                    search_string = normalize(search_string)
                    category = str(indexer.tv_search_capatabilities)
                    list_of_dicts = await indexer.engine.search(search_string, category)
                    if list_of_dicts is not None and len(list_of_dicts) > 0:
                        torrents = self.__get_torrents_from_list_of_dicts(series, indexer, list_of_dicts)
                        if torrents is not None and type(torrents) is list and len(torrents) >0:
                            results.extend(torrents)


            except Exception:
                self.logger.exception(
                    f"An exception occured while searching for a series on Search with indexer {indexer.title} and language {lang}.")
            
            index = index +1
        
        if search_string is None:
            search_string = base_title

        if len(results) > 0:
            self.logger.info(f"Found {len(results)} for '{search_string}' @ {indexer.engine_name}/{category} in {round(time.time() - start_time, 1)} [s]")
        else:
            self.logger.info(f"No results found for '{search_string}' @ {indexer.engine_name}/{category} in {round(time.time() - start_time, 1)} [s]")

        return results


    def __get_indexers(self):
        try:
            search_indexers = self.__get_indexer_from_engines(self.__config['engines'])
            # creiamo un dizionario con title come chiave
            indexers = {si.engine_name: si for si in search_indexers}
            return indexers
        except Exception:
            self.logger.exception("An exception occured while getting indexers from Search.")
            return []


    def __get_indexer_from_engines(self, engines):

        indexer_list = []
        id = 0
        for engine_name in engines:
            indexer = SearchIndexer()

            indexer.engine = self.__get_engine(engine_name)
            indexer.language = indexer.engine.language

            indexer.title = indexer.engine.name
            indexer.id = id
            indexer.engine_name = engine_name

            supported_categories = indexer.engine.supported_categories
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
        # Check if link inizia con "magnet:?"
        return link.startswith("magnet:?")


    def __extract_info_hash(self, magnet_link):
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
