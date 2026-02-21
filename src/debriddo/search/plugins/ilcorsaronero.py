"""
@file src/debriddo/search/plugins/ilcorsaronero.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.38
# AUTHORS: LightDestory (https://github.com/LightDestory)
# CONTRIBUTORS: Ogekuri

import re
from urllib.parse import quote_plus

from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
    AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.utils.novaprinter import PrettyPrint

prettyPrinter = PrettyPrint()

class ilcorsaronero(BasePlugin):
    """
    @brief Class `ilcorsaronero` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    url = 'https://ilcorsaronero.link/'
    name = 'ilCorSaRoNeRo'
    language = "it"
    supported_categories = {'all': '',
                            'movies': 'film',
                            'music': 'musica',
                            'games': 'giochi',
                            'anime': 'animazione',
                            'books': 'libri',
                            'software': 'software',
                            'tv': 'serie-tv'}
    

    class HTMLParser:

        """
        @brief Class `HTMLParser` encapsulates cohesive runtime behavior.
        @details Generated Doxygen block for class-level contract and extension boundaries.
        """
        def __init__(self, url):
            """
            @brief Execute `__init__` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `__init__`.
            @param url Runtime input parameter consumed by `__init__`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            self.url = url
            self.noTorrents = False

        def feed(self, html):
            """
            @brief Execute `feed` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `feed`.
            @param html Runtime input parameter consumed by `feed`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            self.noTorrents = False
            torrents = self.__findTorrents(html)
            if len(torrents) == 0:
                self.noTorrents = True
                return
            for torrent in range(len(torrents)):
                data = {
                    'link': torrents[torrent][0],
                    'name': torrents[torrent][1],
                    'size': torrents[torrent][2],
                    'seeds': torrents[torrent][3],
                    'leech': torrents[torrent][4],
                    'engine_url': self.url,
                    'desc_link': torrents[torrent][5],
                    'pub_date': torrents[torrent][6]
                }
                prettyPrinter(data)

        def __findTorrents(self, html):
            """
            @brief Execute `__findTorrents` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `__findTorrents`.
            @param html Runtime input parameter consumed by `__findTorrents`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            torrents = []
            # Find all TR nodes with class odd or odd2
            trs = re.findall(r'(<tr>.+?</tr>)', html)
            for tr in trs[1:]: # Skip the first TR node because it's the header
                # Extract from the A node all the needed information
                url_titles = re.search(
                    r'href=\"(.+?)\">(.+?)</a>.+?green.+?>.*?([0-9]+).*?red.*?>.*?([0-9]+).+?([0-9\.\,]+ (?:TiB|GiB|MiB|KiB|B)).+?timestamp=\"(.+?)\"',
                    tr)
                if url_titles:
                    generic_url = '{0}{1}'.format(self.url[:-1], url_titles.group(1))
                    torrents.append([
                        generic_url,
                        url_titles.group(2),
                        url_titles.group(5),
                        url_titles.group(3),
                        url_titles.group(4),
                        generic_url,
                        url_titles.group(6)
                    ])
            return torrents

    async def download_torrent(self, info):
        """
        @brief Execute `download_torrent` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `download_torrent`.
        @param info Runtime input parameter consumed by `download_torrent`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        page = await session.retrieve_url(info)
        if page is not None:
            torrent_page = ' '.join((page).split())
            magnet_match = re.search(r'href=\"(magnet:.*?)\"', torrent_page)
            if magnet_match and magnet_match.groups():
                magnet_str = magnet_match.groups()[0]
                await session.close()
                return(str(magnet_str + " " + magnet_str))
            else:
                await session.close()
                raise Exception('Error, please fill a bug report!')
        await session.close()
        return None

    async def search(self, what, cat='all'):
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
        prettyPrinter.clear()
        what = quote_plus(what)
        parser = self.HTMLParser(self.url)
        counter: int = 1
        # filter = '&cat={0}'.format(self.supported_categories[cat])
        filter = self.supported_categories[cat]
        # TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
        while True:
            url = '{0}search?q={1}&cat={2}&page={3}'.format(self.url, what, filter, counter)
            # Some replacements to format the html source
            page = await session.retrieve_url(url)
            if page is not None:
                html = ' '.join((page).split())
                parser.feed(html)
                if parser.noTorrents:
                    break
                counter += 1
        await session.close()
        return prettyPrinter.get()
