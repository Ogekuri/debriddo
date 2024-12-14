# VERSION: 0.0.32
# AUTHORS: sa3dany, Alyetama, BurningMop, scadams
# CONTRIBUTORS: Ogekuri

# LICENSING INFORMATION
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
from urllib.parse import quote_plus
from html.parser import HTMLParser
from utils.logger import setup_logger
from utils.novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from search.plugins.base_plugin import BasePlugin

class one337x(BasePlugin):
    url = 'https://1337x.to'
    name = '1337x'
    language = "any"
    supported_categories = {
        'all': None,
        'anime': 'Anime',
        'software': 'Apps',
        'games': 'Games',
        'movies': 'Movies',
        'music': 'Music',
        'tv': 'TV',
    }


    class MyHtmlParser(HTMLParser):

        def error(self, message):
            pass

        A, TD, TR, HREF, TBODY, TABLE = ('a', 'td', 'tr', 'href', 'tbody', 'table')

        def __init__(self, url):
            HTMLParser.__init__(self)
            self.url = url
            self.row = {}
            self.column = None
            self.insideRow = False
            self.foundTable = False
            self.foundResults = False
            self.parser_class = {
                'name': 'name',
                'seeds': 'seeds',
                'leech': 'leeches',
                'size': 'size'
            }

        def handle_starttag(self, tag, attrs):
            params = dict(attrs)
            if 'search-page' in params.get('class', ''):
                self.foundResults = True
                return
            if self.foundResults and tag == self.TBODY:
                self.foundTable = True
                return
            if self.foundTable and tag == self.TR:
                self.insideRow = True
                return
            if self.insideRow and tag == self.TD:
                classList = params.get('class', None)
                for columnName, classValue in self.parser_class.items():
                    if classValue in classList:
                        self.column = columnName
                        self.row[self.column] = -1
                return

            if self.insideRow and tag == self.A:
                if self.column != 'name' or self.HREF not in params:
                    return
                link = params[self.HREF]
                if link.startswith('/torrent/'):
                    link = f'{self.url}{link}'
                # fix non scarico subito il file
                #     torrent_page = retrieve_url(link)
                #     magnet_regex = r'href="magnet:.*"'
                #     matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE)
                #     magnet_urls = [x.group() for x in matches]
                #     self.row['link'] = magnet_urls[0].split('"')[1]
                #     self.row['engine_url'] = self.url
                #     self.row['desc_link'] = link
                    self.row['link'] = link
                    self.row['engine_url'] = self.url
                    self.row['desc_link'] = link

        def handle_data(self, data):
            if self.insideRow and self.column:
                if self.column == 'size':
                    data = data.replace(',', '')
                self.row[self.column] = data
                self.column = None

        def handle_endtag(self, tag):
            if tag == self.TABLE:
                self.foundTable = False
            if self.insideRow and tag == self.TR:
                self.insideRow = False
                self.column = None
                if not self.row:
                    return
                prettyPrinter(self.row)
                self.row = {}

    async def download_torrent(self, info):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        # fix le info dopo
        torrent_page = await session.retrieve_url(info)
        if torrent_page is not None:
            magnet_regex = r'href="magnet:.*"'
            matches = re.finditer(magnet_regex, torrent_page, re.MULTILINE)
            if matches is not None:
                magnet_urls = [x.group() for x in matches]
                magnet = magnet_urls[0].split('"')[1]
                await session.close()
                return(str(magnet))
        await session.close()
        return None

    async def search(self, what, cat='all'):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        prettyPrinter.clear()
        parser = self.MyHtmlParser(self.url)
        what = quote_plus(what)
        category = self.supported_categories[cat]
        page = 1
        # TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
        while True:
            page_url = f'{self.url}/category-search/{what}/{category}/{page}/' if category else f'{self.url}/search/{what}/{page}/'
            html = await session.retrieve_url(page_url)
            if html is not None:
                parser.feed(html)
                if html.find('<li class="last">') == -1:
                    # exists on every page but the last
                    break
                page += 1
        parser.close()
        await session.close()
        return prettyPrinter.get()
