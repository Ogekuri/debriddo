"""
@file src/debriddo/search/plugins/ilcorsaroblu.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.37
# AUTHORS: Ogekuri

from bs4 import BeautifulSoup
from urllib.parse import quote_plus

from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
    AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.utils.novaprinter import PrettyPrint

prettyPrinter = PrettyPrint()

class ilcorsaroblu(BasePlugin):
    """
    @brief Class `ilcorsaroblu` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    url='https://ilcorsaroblu.org/'
    api='https://ilcorsaroblu.org/'
    name='IlCorsaroBlu'
    language="it"

    # uncomment appropriate lines to include TPB category in qBittorrent search category
    # currently set to include only HD video for "movies" & "tv"
    supported_categories={
        'all': [],
        'movies':
        [
            46,		# Parodie
            11,		# DVD-R (DVD5 & DVD9)
            13,		# 1080p
            14,		# 720p
            15,		# 3D
            17,		# BDRip-mkv-h264
            21,		# Movies - Films
            25,		# 4K-UltraHD
            28,		# Anime
            29,		# Cartoons
            35,		# Documentari
            36,		# Films (TNT Village)
            37,		# Sport / Gare
            38,		# Commedia
            39		# BDRip-mkv-h264-TNT
        ],
        'books':
        [
            45,		# Fumetti
            51,		# Pdf
            6, 		# eBooks
            33,		# Romanzi
            26		# Edicola: Giornali/Quotidiani
        ],
        'games':
        [
            27,		# Games -> Console
            41,		# Games -> Xbox360
            43,		# Retro Games
            47,		# Games -> Nintendo
            3		# Games -> PC
        ],
        'music':
        [
            48,		# Audio -> Mp3
            49,		# Radio Trasmissioni
            2		# Audio / Music
        ],
        'archives':
        [
            23		# Archive
        ],
        'software':	# but not games
        [
            7,		# Windows
            8,		# Linux
            9,		# Macintosh-Apple
            34,		# Student's Office
            5,		# Android
            30		# iOS / iPhone
        ],
        'tv':
        [
            19,		# TV Show 1080p
            20,		# TV Show 720p
            24,		# TV Show Standard
            50		# TV Show (TNT Village)
        ],
        'others':
        [
            42,		#  Disegni e Modelli
            4,		# Other
            12		#  Adult
        ],
        'premium':
        [
            16, 		# V.I.P.
            32 		# Premium
        ]
    }

    login_url='{self.api}index.php?page=login'
    query_url='{self.api}index.php?page=torrents&category={category}&search={what}'

    tracker_urls=[
        'udp://tracker.coppersurfer.tk:6969/announce',
        'udp://tracker.openbittorrent.com:6969/announce',
        'udp://9.rarbg.to:2710/announce',
        'udp://9.rarbg.me:2780/announce',
        'udp://9.rarbg.to:2730/announce',
        'udp://tracker.opentrackr.org:1337',
        'http://p4p.arenabg.com:1337/announce',
        'udp://tracker.torrent.eu.org:451/announce',
        'udp://tracker.tiny-vps.com:6969/announce',
        'udp://open.stealth.si:80/announce'
        ]
    
    logged = None
    
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
        # Dati del form di autenticazione
        self.login_data = {
            "uid": self.config['ilcorsarobluUid'],
            "pwd": self.config['ilcorsarobluPwd']
        }

    async def __extract_info_hash(self, html_content, suffix_to_remove=" - il CorSaRo Blu"):
        """
        @brief Execute `__extract_info_hash` operational logic.
        @details Parses ilCorSaRo Blu detail page HTML and extracts tuple `(info_hash, normalized_name)` when both fields are available.
        @param self Runtime input parameter consumed by `__extract_info_hash`.
        @param html_content Runtime input parameter consumed by `__extract_info_hash`.
        @param suffix_to_remove Runtime input parameter consumed by `__extract_info_hash`.
        @return Computed result payload; `None` when required nodes are missing.
        @side_effect No external side effects.
        """
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trova name
        name = None
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.text.strip()
            # Rimuovi il suffisso, se presente
            if title.endswith(suffix_to_remove):
                name = title[:-len(suffix_to_remove)]

        # Trova il primo input con name="info_hash"
        info_hash = None
        input_tag = soup.find('input', {'name': 'info_hash'})
        if input_tag:
            info_hash = input_tag.get('value')


        if info_hash is not None and name is not None:
            return info_hash, name

        return None

    async def __generate_magnet_link(self, info_hash, name=None, tracker_urls=None):
        """
        @brief Execute `__generate_magnet_link` operational logic.
        @details Builds a magnet URI from info hash and optional display name plus tracker list.
        @param self Runtime input parameter consumed by `__generate_magnet_link`.
        @param info_hash Runtime input parameter consumed by `__generate_magnet_link`.
        @param name Runtime input parameter consumed by `__generate_magnet_link`.
        @param tracker_urls Runtime input parameter consumed by `__generate_magnet_link`.
        @return Computed result payload containing the generated magnet URI.
        @side_effect No external side effects.
        """
        # Base del magnet link con l'info hash
        base_magnet = f"magnet:?xt=urn:btih:{info_hash}"
        
        # Aggiungi il nome se fornito
        if name:
            # Codifica il nome per essere compatibile con URL
            from urllib.parse import quote
            encoded_name = quote(name)
            base_magnet += f"&dn={encoded_name}"
        
        # Aggiungi i tracker se forniti
        if tracker_urls:
            # Aggiungi ogni tracker al magnet link
            trackers = ''.join([f"&tr={tracker}" for tracker in tracker_urls])
            base_magnet += trackers
        
        return base_magnet


    async def login(self, session=None):
        """
        @brief Execute `login` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `login`.
        @param session Runtime input parameter consumed by `login`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if session is None:
            return False
        # Esegui il login
        try:
            self.logged = None
            auth_url=self.login_url.format(self=self)
            response = await session.request_post(auth_url, data=self.login_data)
            if response is not None:
                # Verifica se il login è stato effettuato correttamente
                if "Benvenuto" in response.text or "Logout" in response.text:
                    self.logger.debug(f"Plugins {self.name}: Login effettuato con successo!")
                    self.logged = True
                    return True
                else:
                    self.logger.error(f"Plugins {self.name}: Errore nel login. Controlla username e password.")
        except Exception as e:
            self.logger.error(f"Plugins {self.name}: Errore durante la download_torrent(): {e}")
        return False


    async def download_torrent(self,info):

        """
        @brief Execute `download_torrent` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `download_torrent`.
        @param info Runtime input parameter consumed by `download_torrent`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        session = AsyncThreadSafeSession()  # Usa il client asincrono

        # login
        if not await self.login(session):
            await session.close()
            return None

        try:
            if self.logged is not None:
                # Esegui la ricerca
                search_response = await session.request_get(info)
                if search_response is not None and search_response.text is not None and len(search_response.text) > 0:
                    html_content = search_response.text
                    if html_content is not None:
                        result = await self.__extract_info_hash(html_content)
                        if result is not None:
                            info_hash, name = result
                            magnet_link = await self.__generate_magnet_link(info_hash, name, self.tracker_urls)
                            if magnet_link is not None:
                                await session.close()
                                return magnet_link
        except Exception as e:
            self.logger.error(f"Plugins {self.name}: Errore durante la download_torrent(): {e}")
        
        await session.close()
        return None

    async def search(self,what,cat='all'):
        """
        @brief Execute `search` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `search`.
        @param what Runtime input parameter consumed by `search`.
        @param cat Runtime input parameter consumed by `search`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        session = AsyncThreadSafeSession()  # Usa il client asincrono

        # login
        if not await self.login(session):
            await session.close()
            return None


        prettyPrinter.clear()
        what = quote_plus(what)

        try:
            if self.logged is not None:
                
                results = []
                # TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
                for category in self.supported_categories[cat]:
                
                    # URL e parametri per la ricerca
                    search_url=self.query_url.format(self=self,what=what,category=category)

                    # Esegui la ricerca
                    search_response = await session.request_get(search_url)
                    if search_response is not None and search_response.text is not None and len(search_response.text) > 0:
                        html_content = search_response.text
                        if html_content is not None:
                            # Parsing della risposta HTML
                            soup = BeautifulSoup(html_content, 'html.parser')

                            tables = soup.find_all('table', class_='lista')  # Identifica righe della tabella con classe "lista"
                            result_table = tables[5]
                            table_rows = result_table.find_all('tr')  # Identifica righe della tabella con classe "lista"

                            # Estrai i dati desiderati
                            i_row = 0
                            for row in table_rows:
                                if i_row > 0:	# scarta l'intestazione
                                    columns = row.find_all('td')
                                    if len(columns) >= 8:  # Assicura che ci siano abbastanza colonne
                                        name = columns[1].get_text(strip=True)
                                        a_tag = columns[1].find('a')
                                        download_link = str(a_tag['href']) if a_tag else ""
                                        # date = columns[4].get_text(strip=True)
                                        seeders = columns[5].get_text(strip=True)
                                        leechers = columns[6].get_text(strip=True)
                                        # completed = columns[7].get_text(strip=True)
                                        size = columns[9].get_text(strip=True)

                                        # non usati
                                        # "Data": date,
                                        # "C": completed,

                                        results.append({
                                            "link": self.api + download_link,
                                            "name": name,
                                            "size": size,
                                            "seeds": seeders,
                                            "leech": leechers,
                                            "engine_url": self.url,
                                            "desc_link": download_link
                                        })
                                i_row = i_row + 1

                # Stampa i risultati
                i = 0
                for result in results:
                    if i > 0:   # salta l'intestazione
                        prettyPrinter(result)
                    i = i + 1

        except Exception as e:
            self.logger.error(f"Plugins {self.name}: Errore durante la download_torrent(): {e}")
        
        await session.close()
        return prettyPrinter.get()
