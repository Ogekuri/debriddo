# VERSION: 0.0.34
# AUTHORS: nindogo (nindogo@gmail.com)
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
import math
import time
from urllib.parse import quote_plus
from debriddo.utils.logger import setup_logger
from debriddo.utils.novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
from html.parser import HTMLParser
import asyncio
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from debriddo.search.plugins.base_plugin import BasePlugin


SITE_URL = "https://torrentgalaxy.to/"

class torrentgalaxy(BasePlugin):
    url = SITE_URL
    name = "TorrentGalaxy"
    language = "any"
    supported_categories = {
        'all': '',
        'movies': 'c3=1&c46=1&c45=1&c42=1&c4=1&c1=1&',
        'tv': 'c41=1&c5=1&c6=1&c7=1&c11=1&',
        'music': 'c23=1&c24=1&c25=1&c26=1&c17=1&',
        'games': 'c43=1&c10=1&',
        'anime': 'c28=1&',
        'software': 'c20=1&c21=1&c18=1&',
        'pictures': 'c37=1&',
        'books': 'c13=1&c19=1&c12=1&c14=1&c15=1&',
    }


    class TorrentGalaxyParser(HTMLParser):
        DIV, A, SPAN, FONT, SMALL, = 'div', 'a', 'span', 'font', 'small'
        count_div, = -1,
        get_size, get_seeds, get_leechs, get_pub_date0, get_pub_date = False, False, False, False, False
        this_record = {}
        url = SITE_URL

        def handle_starttag(self, tag, attrs):
            if tag == self.DIV:
                my_attrs = dict(attrs)
                # if (my_attrs.get('class') == 'tgxtablerow txlight'):
                if  my_attrs.get('class') and 'tgxtablerow' in my_attrs.get('class'):
                    self.count_div = 0
                    self.this_record = {}
                    self.this_record['engine_url'] = self.url
                if  my_attrs.get('class') and ('tgxtablecell' in my_attrs.get('class')) and self.count_div >= 0:
                    self.count_div += 1
                if my_attrs.get('style') and ('text-align:right' in my_attrs.get('style')) and self.count_div >= 0:
                    self.get_pub_date0 = True

            if tag == self.A and self.count_div < 13:
                my_attrs = dict(attrs)
                if 'title' in my_attrs and ('class' in my_attrs) and 'txlight' in my_attrs.get('class') and not my_attrs.get('id'):
                    self.this_record['name'] = my_attrs['title']
                    self.this_record['desc_link'] = \
                        self.url + my_attrs['href']
                if 'role' in my_attrs and my_attrs.get('role') == 'button':
                    self.this_record['link'] = my_attrs['href']

            if tag == self.SPAN:
                my_attrs = dict(attrs)
                if 'class' in my_attrs and 'badge badge-secondary' in my_attrs.get('class'):
                    self.get_size = True

            if tag == self.FONT:
                my_attrs = dict(attrs)
                if my_attrs.get('color') == 'green':
                    self.get_seeds = True
                elif my_attrs.get('color') == '#ff0000':
                    self.get_leechs = True

            if self.count_div == 13 and tag == self.SMALL:
                prettyPrinter(self.this_record)
                self.this_record = {}
                self.count_div = -1
                
            if self.get_pub_date0 and tag == self.SMALL:
                self.get_pub_date = True

        def handle_data(self, data):
            if self.get_size is True and self.count_div < 13:
                self.this_record['size'] = data.strip().replace(',', '')
                self.get_size = False
            if self.get_seeds is True:
                self.this_record['seeds'] = data.strip().replace(',', '')
                self.get_seeds = False
            if self.get_leechs is True:
                self.this_record['leech'] = data.strip().replace(',', '')
                self.get_leechs = False
            if self.get_pub_date is True:
                self.this_record['pub_date'] = str(int(time.mktime(time.strptime(data.strip(),"%d/%m/%y %H:%M"))))
                self.get_pub_date, self.get_pub_date0 = False, False

    async def do_search(self, session, url):
        webpage = await session.retrieve_url(url)
        if webpage is not None:
            tgParser = self.TorrentGalaxyParser()
            tgParser.feed(webpage)

    async def search(self, what, cat='all'):
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        prettyPrinter.clear()
        query = quote_plus(what)
        search_url = SITE_URL + 'torrents.php?'
        full_url = \
            search_url + \
            self.supported_categories[cat.lower()] + \
            'sort=seeders&order=desc&search=' + \
            query
        
        webpage = await session.retrieve_url(full_url)
        if webpage is not None:
            tgParser = self.TorrentGalaxyParser()
            tgParser.feed(webpage)
            all_results_re = re.compile(r'steelblue[^>]+>(.*?)<')
            if all_results_re is not None and type(all_results_re) is list and len(all_results_re) > 0:
                all_results = all_results_re.findall(webpage)[0]
                all_results = all_results.replace(' ', '')
                pages = math.ceil(int(all_results) / 50)
                
                this_urls = [ full_url + '&page=' + str(page) for page in range(0, pages)]
                # TODO: run in multi-thread?
                tasks = [self.do_search(session, this_url) for this_url in this_urls] 
                await asyncio.gather(*tasks)
        
        await session.close()
        return prettyPrinter.get()

if __name__ == '__main__':
    a = torrentgalaxy()
    a.search('ncis new', 'all')
