# VERSION: 1.1
# AUTHORS: Ogekuri

import urllib.parse
import json
from helpers import retrieve_url, download_file
from novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
from bs4 import BeautifulSoup

class torrentz(object):
    url = 'https://torrentz2.nz/'
    api_url = "https://torrentz2.nz/"
    name = 'Torrentz2'
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

    def search(self, what, cat='all'):
        prettyPrinter.clear()
        url = '{0}search?q={1}&cat=0'.format(self.api_url, what)
        self.__parseHTML(retrieve_url(url))
        return prettyPrinter.get()

    def download_torrent(self, info):
        # non necessaria ha già i magnet nella ricarca
        return None