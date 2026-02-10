# VERSION: 0.0.33
# AUTHORS: Ogekuri

import urllib.parse
from utils.novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
from bs4 import BeautifulSoup
from urllib.parse import quote
from utils.logger import setup_logger
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from search.plugins.base_plugin import BasePlugin


class torrentz(BasePlugin):
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
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        # Trova tutti i blocchi <dl> nella pagina
        for dl in soup.find_all('dl'):
            # Estrai il titolo e il link
            dt = dl.find('dt')
            title = dt.get_text(strip=True)
            link = dt.find('a')['href']
            
            # Estrai il magnet link
            magnet_link = dl.find('dd').find('a')['href']
            
            # Estrai gli altri campi
            spans = dl.find('dd').find_all('span')

            time_uploaded = spans[1].get_text(strip=True)
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
				'desc_link':	urllib.parse.quote(link)
			}
            prettyPrinter(data)

        
        return results

    async def search(self, what, cat='all'):
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

