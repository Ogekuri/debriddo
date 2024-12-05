# run from this path

from thepiratebay_categories import thepiratebay
from one337x import one337x
from limetorrents import limetorrents
from torrentproject import torrentproject
from ilcorsaronero import ilcorsaronero
from torrentz import torrentz
from torrentgalaxy import torrentgalaxy
from therarbg import therarbg

from urllib.parse import quote_plus

# engines = [thepiratebay(), one337x(), limetorrents(), torrentproject(), ilcorsaronero(), torrentz(), torrentgalaxy(), therarbg()]
# engines = [thepiratebay()]
# engines = [one337x()]
# engines = [limetorrents()]
# engines = [torrentproject()]
# engines = [ilcorsaronero()]
# engines = [torrentz()]
# engines = [torrentgalaxy()]
engines = [therarbg()]

# SEARCH_STRING="Arcane S02 ITA"
# SEARCH_TYPE="tv"

# SEARCH_STRING="Wolfs 2024 ITA"
# SEARCH_TYPE="movies"

# SEARCH_STRING="The Fall Guy 2024 ITA"
# SEARCH_TYPE="movies"

SEARCH_STRING="Star Wars Tales of the Empire S01"
SEARCH_TYPE="tv"

print(f"Search: {SEARCH_STRING}/{SEARCH_TYPE}")

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
        for result in results:
            print('RESULT: ' + str(result))
            print("-----------------------------------------------------------")
        print("")
        for result in results:
            link = result['link'] 
            if not __is_magnet_link(link):
                print('CONVERT: '+ str(link))
                link = engine.download_torrent(result['link'])
                print('RESULT: ' + str(link))
                print("-----------------------------------------------------------")
    print("###########################################################")
    print("")
