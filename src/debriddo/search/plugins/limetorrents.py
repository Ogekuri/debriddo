"""
@file src/debriddo/search/plugins/limetorrents.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: Lima66
# CONTRIBUTORS: Ogekuri, Diego de las Heras (ngosang@hotmail.es)

import re
import ssl
from datetime import datetime, timedelta
from html.parser import HTMLParser
from urllib.parse import quote

from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
    AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.utils.novaprinter import PrettyPrint

# Fix invalid certificate in Windows
ssl._create_default_https_context = ssl._create_unverified_context

prettyPrinter = PrettyPrint()


class limetorrents(BasePlugin):
    """
    @brief Class `limetorrents` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    url = "https://www.limetorrents.lol"
    name = "LimeTorrents"
    language = "any"
    supported_categories = {'all': 'all',
                            'anime': 'anime',
                            'software': 'applications',
                            'games': 'games',
                            'movies': 'movies',
                            'music': 'music',
                            'tv': 'tv'}
    
    
    class MyHtmlParser(HTMLParser):
        """
        @brief Class `MyHtmlParser` encapsulates cohesive runtime behavior.
        @details Specialized HTML parser collecting torrent entries from LimeTorrents search result rows.
        """

        def error(self, message):
            """
                @brief Execute `error` operational logic.
                @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
                @param self Runtime input parameter consumed by `error`.
                @param message Runtime input parameter consumed by `error`.
                @return Computed result payload; `None` when side-effect-only execution path is selected.
                @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
                """
            pass

        A, TD, TR, HREF = ('a', 'td', 'tr', 'href')

        def __init__(self, url):
            """
            @brief Execute `__init__` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `__init__`.
            @param url Runtime input parameter consumed by `__init__`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            HTMLParser.__init__(self)
            self.url = url
            self.current_item = {}  # dict for found item
            self.page_items = 0
            self.inside_table = False
            self.inside_tr = False
            self.column_index = -1
            self.column_name = None  # key's name in current_item dict
            self.columns = ["name", "pub_date", "size", "seeds", "leech"]

            now = datetime.now()
            self.date_parsers = {
                r"yesterday": lambda m: now - timedelta(days=1),
                r"last\s+month": lambda m: now - timedelta(days=30),
                r"(\d+)\s+years?": lambda m: now - timedelta(days=int(m[1]) * 365),
                r"(\d+)\s+months?": lambda m: now - timedelta(days=int(m[1]) * 30),
                r"(\d+)\s+days?": lambda m: now - timedelta(days=int(m[1])),
                r"(\d+)\s+hours?": lambda m: now - timedelta(hours=int(m[1])),
                r"(\d+)\s+minutes?": lambda m: now - timedelta(minutes=int(m[1])),
            }

        def handle_starttag(self, tag, attrs):
            """
            @brief Execute `handle_starttag` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `handle_starttag`.
            @param tag Runtime input parameter consumed by `handle_starttag`.
            @param attrs Runtime input parameter consumed by `handle_starttag`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            params = dict(attrs)

            if params.get('class') == 'table2':
                self.inside_table = True
            elif not self.inside_table:
                return

            if tag == self.TR and (params.get('bgcolor') == '#F4F4F4' or params.get('bgcolor') == '#FFFFFF'):  # noqa
                self.inside_tr = True
                self.column_index = -1
                self.current_item = {"engine_url": self.url}
            elif not self.inside_tr:
                return

            if tag == self.TD:
                self.column_index += 1
                if self.column_index < len(self.columns):
                    self.column_name = self.columns[self.column_index]
                else:
                    self.column_name = None

            if self.column_name == "name" and tag == self.A and self.HREF in params:
                link = params["href"]
                if link and link.endswith(".html"):
                    try:
                        safe_link = quote(self.url + link, safe='/:')
                    except KeyError:
                        safe_link = self.url + link
                    self.current_item["link"] = safe_link
                    self.current_item["desc_link"] = safe_link

        def handle_data(self, data):
            """
            @brief Execute `handle_data` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `handle_data`.
            @param data Runtime input parameter consumed by `handle_data`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            if self.column_name:
                if self.column_name in ["size", "seeds", "leech"]:
                    data = data.replace(',', '')
                elif self.column_name == "pub_date":
                    timestamp = -1
                    for pattern, calc in self.date_parsers.items():
                        m = re.match(pattern, data, re.IGNORECASE)
                        if m:
                            timestamp = int(calc(m).timestamp())
                            break
                    data = str(timestamp)
                self.current_item[self.column_name] = data.strip()
                self.column_name = None

        def handle_endtag(self, tag):
            """
            @brief Execute `handle_endtag` operational logic.
            @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
            @param self Runtime input parameter consumed by `handle_endtag`.
            @param tag Runtime input parameter consumed by `handle_endtag`.
            @return Computed result payload; `None` when side-effect-only execution path is selected.
            @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
            """
            if tag == 'table':
                self.inside_table = False

            if self.inside_tr and tag == self.TR:
                self.inside_tr = False
                self.column_name = None
                if "link" in self.current_item:
                    prettyPrinter(self.current_item)
                    self.page_items += 1


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
        # since limetorrents provides torrent links in itorrent (cloudflare protected),
        # we have to fetch the info page and extract the magnet link
        info_page = await session.retrieve_url(info)
        if info_page is not None:
            magnet_match = re.search(r"href\s*\=\s*\"(magnet[^\"]+)\"", info_page)
            if magnet_match and magnet_match.groups():
                await session.close()
                return(str(magnet_match.groups()[0] + " " + info))
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
        # """ Performs search """
        prettyPrinter.clear()
        query = quote(what)
        query = query.replace("%20", "-")
        category = self.supported_categories[cat]
        
        # TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
        for page in range(1, 5):
            page_url = f"{self.url}/search/{category}/{query}/seeds/{page}/"
            html = await session.retrieve_url(page_url)
            if html is not None:
                parser = self.MyHtmlParser(self.url)
                parser.feed(html)
                parser.close()
                if parser.page_items < 20:
                    break
        await session.close()
        return prettyPrinter.get()
