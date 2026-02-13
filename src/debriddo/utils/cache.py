# VERSION: 0.0.35
# AUTHORS: Ogekuri

from typing import List
import sqlite3
import os
from debriddo.constants import CACHE_DATABASE_FILE
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.logger import setup_logger
from datetime import datetime
from debriddo.utils.string_encoding import normalize

TABLE_NAME = "cached_items"

TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS cached_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP,
    title TEXT,
    language TEXT,
    media_id TEXT,
    media_type TEXT,
    media_titles TEXT,
    media_year TEXT,
    media_season TEXT,
    media_episode TEXT,
    media_languages TEXT,
    torrent_hash TEXT,
    torrent_type TEXT,
    torrent_title TEXT,
    torrent_raw_title TEXT,
    torrent_indexer TEXT,
    torrent_engine_name TEXT,
    torrent_privacy TEXT,
    torrent_languages TEXT,
    torrent_magnet TEXT,
    torrent_link TEXT,
    torrent_trackers TEXT,
    torrent_seeders INTEGER,
    torrent_size INTEGER,
    torrent_availability BOOL,
    seasonfile BOOLEAN,
    season_first INTEGER,
    season_last INTEGER,
    episode_first INTEGER,
    episode_last INTEGER,
    year INTEGER
)
"""

logger = setup_logger(__name__)

def search_cache(config, media):
    
    if os.path.exists(CACHE_DATABASE_FILE):
        try:
            connection = sqlite3.connect(CACHE_DATABASE_FILE)
            cursor = connection.cursor()
            # Verifica se la tabella esiste
            cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
        except sqlite3.Error as e:
                    logger.error(f"SQL error: {e}")
                    return None
        if cursor.fetchone() is not None:
            logger.debug("Delete expired records")
            try:
                days = config['daysCacheValid']
                cursor.execute(f"""DELETE FROM '{TABLE_NAME}' WHERE created_at < datetime('now', '-{days} days');""")
                connection.commit()
            except sqlite3.Error as e:
                logger.error(f"SQL error: {e}")

            logger.debug("Searching for cached " + media.type + " results")

            cache_items = []

            # cicla sulle lingue
            index = 0
            for language in media.languages:
                year = -1
                clean_season = -1
                clean_episode = -1

                title = media.titles[index]
                title = normalize(title)

                if media.type == "movie":
                    year = int(media.year)
                elif media.type == "series":
                    clean_season = int(media.season.replace("S", ""))
                    clean_episode = int(media.episode.replace("E", ""))
                
                logger.info("Searchching for " + media.type + " '" + title + "' @<cache>")

                cache_search = dict()
                
                cache_search['media_id'] = media.id

                cache_search['title'] = title
                cache_search['language'] = language

                if media.type == "movie":
                    cache_search['year'] = year
                elif media.type == "series":
                    cache_search['season'] = clean_season
                    cache_search['episode'] = clean_episode

                try:
                    filters = []
                    # Costruisci la query di filtro in base a `cache_search`
                    if media.type == "movie":
                        filters = [ "( (media_id = :media_id) OR (title = :title AND language = :language AND year = :year) )" ]
                    elif media.type == "series":
                        filters = [ "( (media_id = :media_id) OR (title = :title AND language = :language AND ((season_first <= :season AND season_last >= :season  AND episode_first <= :episode AND episode_last >= :episode AND seasonfile = False) OR (season_first <= :season AND season_last >= :season AND seasonfile = True))) )" ]

                    # Genera la query dinamica
                    query = f"SELECT * FROM {TABLE_NAME} WHERE " + " AND ".join(filters)

                    # Esegui la query con i parametri
                    cursor.execute(query, cache_search)
                    rows = cursor.fetchall()

                    # Recupera i nomi delle colonne
                    cursor.execute(f"PRAGMA table_info({TABLE_NAME});")
                    columns = [info[1] for info in cursor.fetchall()]

                    # Trasforma ogni riga in un dizionario
                    for row in rows:
                        cache_item = dict(zip(columns, row))
                        # strighe di lista in lista
                        cache_item['media_titles'] = eval(cache_item['media_titles'])
                        cache_item['media_languages'] = eval(cache_item['media_languages'])
                        cache_item['torrent_languages'] = eval(cache_item['torrent_languages'])
                        cache_item['torrent_trackers'] = eval(cache_item['torrent_trackers'])
                        cache_item['torrent_availability'] = bool(cache_item['torrent_availability'])
                        cache_items.append(cache_item)

                    logger.info(f"{len(cache_items)} record found on cache database table:'{TABLE_NAME}'.")
                except sqlite3.Error as e:
                    logger.error(f"SQL error: {e}")
                
                index = index + 1
            
            if cache_items is not None and len(cache_items) > 0:
                return cache_items
            else:
                return None
    return None


def cache_results(torrents: List[TorrentItem], media):

    if torrents is not None and len(torrents) > 0:

        # Verifica se il file esiste (opzionale, SQLite lo crea comunque)
        db_exists = os.path.exists(CACHE_DATABASE_FILE)

        # Connetti al database (crea il file se non esiste)
        connection = sqlite3.connect(CACHE_DATABASE_FILE)
        cursor = connection.cursor()

        if not db_exists:
            logger.info("Database crated: " + CACHE_DATABASE_FILE + " .")

        # Verifica se la tabella esiste, altrimenti la crea
        cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';""")
        table_exists = cursor.fetchone() is not None

        if not table_exists:
            cursor.execute(TABLE_SCHEMA)
            connection.commit()
            logger.info("Table crated: " + TABLE_NAME + " .")

        logger.debug("Started caching results")

        # crea dizionario dei titoli
        titles = dict(zip(media.languages, media.titles))

        # elenco delle entry da aggiungere
        cache_items = []

        for torrent in torrents:
            hash_already_exist = False
            try:
                # Esegui una query per verificare l'esistenza dell'hash
                cursor.execute(f"SELECT 1 FROM {TABLE_NAME} WHERE torrent_hash = ? LIMIT 1;", (torrent.info_hash,))
                result = cursor.fetchone()

                # Restituisci True se il risultato non è None
                if result is not None:
                    hash_already_exist = True
            except sqlite3.Error as e:
                    logger.error(f"SQL error: {e}")
            
            if not hash_already_exist:
                try:
                    # cicla sulle lingue
                    for language in torrent.languages:
                        year = -1
                        seasonfile = False
                        season_first = -1
                        season_last = -1
                        episode_first = -1
                        episode_last = -1

                        if language in media.languages:
                            title = titles[language]
                        else:
                            title = media.titles[0]
                        title = normalize(title)

                        if media.type == "movie":
                             year = int(media.year)
                             seasonfile = False
                             season_first = -1
                             season_last = -1
                             episode_first = -1
                             episode_last = -1
                        elif media.type == "series":
                            year = -1
                            clean_season = int(media.season.replace("S", ""))
                            # clean_episode = int(media.episode.replace("E", ""))
                            parsed_data = torrent.parsed_data
                            parsed_seasons = parsed_data.seasons if parsed_data is not None and hasattr(parsed_data, "seasons") else []
                            parsed_episodes = parsed_data.episodes if parsed_data is not None and hasattr(parsed_data, "episodes") else []

                            # parsed_result = parse(result.raw_title) - già popolato
                            if type(parsed_seasons) is list and len(parsed_seasons) > 0:
                                season_first = min(parsed_seasons)
                                season_last = max(parsed_seasons)
                            elif type(parsed_seasons) is int and parsed_seasons > 0:
                                season_first = parsed_seasons
                                season_last = parsed_seasons
                            else:
                                season_first = clean_season
                                season_last = clean_season

                            if type(parsed_episodes) is list and len(parsed_episodes) > 1:
                                seasonfile = True  # True = contiene la stagione intera
                                episode_first = min(parsed_episodes)
                                episode_last = max(parsed_episodes)
                            elif type(parsed_episodes) is list and len(parsed_episodes) == 1:
                                seasonfile = False  # True = contiene la stagione intera
                                episode_first = min(parsed_episodes)
                                episode_last = max(parsed_episodes)
                            elif type(parsed_episodes) is int and parsed_episodes > 0:
                                seasonfile = False  # False = contiene un episodio
                                episode_first = parsed_episodes
                                episode_last = parsed_episodes
                            else:
                                seasonfile = True  # False = contiene un episodio
                                episode_first = 0
                                episode_last = 1000

                        # prepara i dati per l'inserimento
                        cache_item = dict()
                        cache_item['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cache_item['title'] = str(title)
                        cache_item['language'] = str(language)
                        cache_item['media_id'] = str(media.id)
                        cache_item['media_type'] = str(media.type)
                        cache_item['media_titles'] = str(media.titles) # lista
                        if media.type == "movie":
                            cache_item['media_year'] = str(media.year)
                            cache_item['media_season'] = ""
                            cache_item['media_episode'] = ""
                        elif media.type == "series":
                            cache_item['media_year'] = ""
                            cache_item['media_season'] = str(media.season)
                            cache_item['media_episode'] = str(media.episode)
                        cache_item['media_languages'] = str(media.languages) # lista
                        cache_item['torrent_hash'] = str(torrent.info_hash)
                        cache_item['torrent_type'] =  str(torrent.type)
                        cache_item['torrent_title'] =  str(torrent.title)
                        cache_item['torrent_raw_title'] =  str(torrent.raw_title)
                        cache_item['torrent_indexer'] =  str(torrent.indexer)
                        cache_item['torrent_engine_name'] =  str(torrent.engine_name)
                        cache_item['torrent_privacy'] =  str(torrent.privacy)
                        cache_item['torrent_languages'] = str(torrent.languages) # lista
                        cache_item['torrent_magnet'] = str(torrent.magnet)
                        cache_item['torrent_link'] = str(torrent.link)
                        cache_item['torrent_trackers'] = str(torrent.trackers) # lista
                        cache_item['torrent_seeders'] = int(torrent.seeders)
                        cache_item['torrent_size'] = int(torrent.size)
                        cache_item['torrent_availability'] = torrent.availability # bool
                        cache_item['seasonfile'] = seasonfile
                        cache_item['season_first'] = int(season_first)
                        cache_item['season_last'] = int(season_last)
                        cache_item['episode_first'] = int(episode_first)
                        cache_item['episode_last'] = int(episode_last)
                        cache_item['year'] = int(year)
                        cache_items.append(cache_item)
                except:
                    logger.exception("An exception occured durring cache parsing")
        
        # Estrai dinamicamente le colonne dalla lista di dizionari
        if cache_items is not None and len(cache_items) > 0:
            columns = cache_items[0].keys()
            placeholders = ", ".join([":" + col for col in columns])  # Placeholder per ogni colonna

            for data in cache_items:
                try:
                    cursor.execute(f"""INSERT INTO {TABLE_NAME} ({", ".join(columns)}) VALUES ({placeholders}) """, data)
                    connection.commit()
                except sqlite3.Error as e:
                    logger.error(f"SQL error: {e}")
            
            logger.info(f"Cached {str(len(cache_items))} {media.type} results")

        if connection:
            connection.close()
