# VERSION: 0.0.28
# AUTHORS: mauricci
# CONTRIBUTORS: Ogekuri

from utils.novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
import re
from html.parser import HTMLParser
from urllib.parse import unquote, quote_plus
from utils.logger import setup_logger
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from search.plugins.base_plugin import BasePlugin


class torrentproject(BasePlugin):
    url = 'https://torrentproject.cc'
    name = 'TorrentProject'
    language = "any"
    supported_categories = {'all': '0'}


    class MyHTMLParser(HTMLParser):

        def __init__(self, url):
            HTMLParser.__init__(self)
            self.url = url
            self.insideResults = False
            self.insideDataDiv = False
            self.pageComplete = False
            self.spanCount = -1
            self.infoMap = {
                "name": 0,
                "torrLink": 0,
                "seeds": 2,
                "leech": 3,
                "pub_date": 4,
                "size": 5,
            }
            self.fullResData = []
            self.pageRes = []
            self.singleResData = self.get_single_data()

        def get_single_data(self):
            return {
                'name': '-1',
                'seeds': '-1',
                'leech': '-1',
                'size': '-1',
                'link': '-1',
                'desc_link': '-1',
                'engine_url': self.url,
                'pub_date': '-1',
            }

        def handle_starttag(self, tag, attrs):
            attributes = dict(attrs)
            if tag == 'div' and 'nav' in attributes.get('id', ''):
                self.pageComplete = True
            if tag == 'div' and attributes.get('id', '') == 'similarfiles':
                self.insideResults = True
            if tag == 'div' and self.insideResults and 'gac_bb' not in attributes.get('class', ''):
                self.insideDataDiv = True
            elif tag == 'span' and self.insideDataDiv and 'verified' != attributes.get('title', ''):
                self.spanCount += 1
            if self.insideDataDiv and tag == 'a' and len(attrs) > 0:
                if self.infoMap['torrLink'] == self.spanCount and 'href' in attributes:
                    self.singleResData['link'] = self.url + attributes['href']
                if self.infoMap['name'] == self.spanCount and 'href' in attributes:
                    self.singleResData['desc_link'] = self.url + attributes['href']

        def handle_endtag(self, tag):
            if not self.pageComplete:
                if tag == 'div':
                    self.insideDataDiv = False
                    self.spanCount = -1
                    if len(self.singleResData) > 0:
                        # ignore trash stuff
                        if self.singleResData['name'] != '-1' \
                                and self.singleResData['size'] != '-1' \
                                and self.singleResData['name'].lower() != 'nome':
                            # ignore those with link and desc_link equals to -1
                            if self.singleResData['desc_link'] != '-1' \
                                    or self.singleResData['link'] != '-1':
                                # fix
                                # data non gestita perché potrebbe anche essere qualcosa del tipi: "7 years ago"
                                self.singleResData['pub_date'] = -1
                                # try:
                                #     date_string = self.singleResData['pub_date']
                                #     date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                                #     self.singleResData['pub_date'] = int(date.timestamp())
                                # except Exception:
                                #     logger.error("self.singleResData['pub_date']", self.singleResData)
                                prettyPrinter(self.singleResData)
                                self.pageRes.append(self.singleResData)
                                self.fullResData.append(self.singleResData)
                        self.singleResData = self.get_single_data()

        def handle_data(self, data):
            if self.insideDataDiv:
                for key, val in self.infoMap.items():
                    if self.spanCount == val:
                        curr_key = key
                        if curr_key in self.singleResData and data.strip() != '':
                            if self.singleResData[curr_key] == '-1':
                                self.singleResData[curr_key] = data.strip()
                            elif curr_key != 'name':
                                self.singleResData[curr_key] += data.strip()

    async def search(self, what, cat='all'):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        prettyPrinter.clear()
        # curr_cat = self.supported_categories[cat]
        what = what.lower()
        what = quote_plus(what)
        
        # TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina

        # analyze first 5 pages of results
        for currPage in range(0, 5):
#            url = self.url + '/browse?t={0}&p={1}'.format(what, currPage)
            url = self.url + '/?t={0}&p={1}'.format(what, currPage)
            html = await session.retrieve_url(url)
            if html is not None:
                parser = self.MyHTMLParser(self.url)
                parser.feed(html)
                parser.close()
                if len(parser.pageRes) < 20:
                    break
        await session.close()
        return prettyPrinter.get()

    async def download_torrent(self, info):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        """ Downloader """
        html = await session.retrieve_url(info)
        if html is not None:
            m = re.search('href=[\'\"].*?(magnet.+?)[\'\"]', html)
            if m and len(m.groups()) > 0:
                magnet = unquote(m.group(1))
                await session.close()
                return(str(magnet + ' ' + info))
        await session.close()
        return None
