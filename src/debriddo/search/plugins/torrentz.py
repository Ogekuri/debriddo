"""
@file src/debriddo/search/plugins/torrentz.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.38
# AUTHORS: Ogekuri

import urllib.parse
from urllib.parse import quote

from bs4 import BeautifulSoup

from debriddo.search.plugins.base_plugin import BasePlugin
from debriddo.utils.async_httpx_session import \
    AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.utils.novaprinter import PrettyPrint

prettyPrinter = PrettyPrint()


class torrentz(BasePlugin):
    """
    @brief Class `torrentz` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    url = 'https://torrentz2.nz/'
    api_url = "https://torrentz2.nz/"
    name = 'Torrentz2'
    language = "any"
    """ 
        TLDR; It is safer to force an 'all' research
        Torrentz2 categories not supported
    """
    supported_categories = {'all': '0'}


    def __parseHTML(self, html):
        """
        @brief Execute `__parseHTML` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__parseHTML`.
        @param html Runtime input parameter consumed by `__parseHTML`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        # Trova tutti i blocchi <dl> nella pagina
        for dl in soup.find_all('dl'):
            # Estrai il titolo e il link
            dt = dl.find('dt')
            if dt is None:
                continue
            title = dt.get_text(strip=True)
            dt_a = dt.find('a')
            if dt_a is None:
                continue
            link = str(dt_a['href'])
            
            # Estrai il magnet link
            dd = dl.find('dd')
            if dd is None:
                continue
            dd_a = dd.find('a')
            if dd_a is None:
                continue
            magnet_link = str(dd_a['href'])
            
            # Estrai gli altri campi
            spans = dd.find_all('span')

            # time_uploaded = spans[1].get_text(strip=True)
            size = spans[2].get_text(strip=True)
            seeders = spans[3].get_text(strip=True)
            leechers = spans[4].get_text(strip=True)

            # rmuove i caratteri che non sono numeri
            seeders = ''.join(c for c in seeders if c.isdigit())
            leechers = ''.join(c for c in leechers if c.isdigit())

            
            # Crea il dizionario per il risultato
            data={
                'link':			magnet_link,
                'name':			title,
                'size':			size,
                'seeds':		int(seeders),
                'leech':		int(leechers),
                'engine_url':	self.url,
                'desc_link':	urllib.parse.quote(str(link))
            }
            prettyPrinter(data)

        
        return results

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
        what = quote(what)
        # url = '{0}search?q={1}&cat=0'.format(self.api_url, what)
        # TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
        url = '{0}search?q={1}'.format(self.api_url, what)
        page = await session.retrieve_url(url)
        if page is not None:
            self.__parseHTML(page)
        await session.close()
        return prettyPrinter.get()

