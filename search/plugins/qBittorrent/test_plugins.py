# run from this path

import sys
# serve per helpers.py e novaprinter.py che voglio tenere in quel percorso
sys.path.append("search/plugins/qBittorren")

from thepiratebay_categories import thepiratebay
from one337x import one337x
from ilcorsaronero import ilcorsaronero
from ilcorsaroblu import corsaroblu

from urllib.parse import quote_plus

#engines = [thepiratebay(), one337x(), ilcorsaronero(), coraroblu()]
engines = [corsaroblu()]

SEARCH_STRING=quote_plus("Arcane S01E02")

def __is_magnet_link(link):
    # Check if link inizia con "magnet:?"
    return link.startswith("magnet:?")

for engine in engines:
    print(engine.name)
    results = engine.search(SEARCH_STRING, 'tv')
    if results is not None:
        print(type(results))
        print(len(results))
        # print(results)
        for result in results:
            link = result['link'] 
            if not __is_magnet_link(link):
                print('convert:'+link)
                link = engine.download_torrent(result['link'])
            print(link)

