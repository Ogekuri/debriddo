# run from this path

from thepiratebay_categories import thepiratebay
from one337x import one337x
from limetorrents import limetorrents
from torrentproject import torrentproject
from ilcorsaronero import ilcorsaronero
from torrentz import torrentz

from urllib.parse import quote_plus

#engines = [thepiratebay()]
#engines = [one337x()]
#engines = [limetorrents()]
#engines = [torrentproject()]
#engines = [ilcorsaronero()]
#engines = [torrentz()]
engines = [thepiratebay(), one337x(), limetorrents(), torrentproject(), ilcorsaronero(), torrentz()]

SEARCH_STRING=quote_plus("Arcane S01 ITA")
SEARCH_TYPE=quote_plus("tv")

# SEARCH_STRING=quote_plus("Wolfs (2024) ITA")
# SEARCH_TYPE=quote_plus("movies")

def __is_magnet_link(link):
    # Check if link inizia con "magnet:?"
    return link.startswith("magnet:?")

for engine in engines:
    print("###########################################################")
    print(engine.name)
    print("###########################################################")
    results = engine.search(SEARCH_STRING, SEARCH_TYPE)
    if results is not None:
        print("NUM RESULT: ", len(results))
        print(results)
        print("-----------------------------------------------------------")
        for result in results:
            link = result['link'] 
            if not __is_magnet_link(link):
                print('CONVERT: '+link)
                link = engine.download_torrent(result['link'])
            print(link)
    print("###########################################################")
    print("")
