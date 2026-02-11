# VERSION: 0.0.34
# AUTHORS: Ogekuri

import sys
import asyncio
from pathlib import Path

# Allow execution as a standalone script from any working directory.
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from debriddo.search.plugins.thepiratebay_categories import thepiratebay
from debriddo.search.plugins.one337x import one337x
from debriddo.search.plugins.limetorrents import limetorrents
from debriddo.search.plugins.torrentproject import torrentproject
from debriddo.search.plugins.ilcorsaronero import ilcorsaronero
from debriddo.search.plugins.torrentz import torrentz
# from debriddo.search.plugins.torrentgalaxyto import torrentgalaxy
from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy
from debriddo.search.plugins.therarbg import therarbg
from debriddo.search.plugins.ilcorsaroblu import ilcorsaroblu

from urllib.parse import quote_plus

# Dati del form di autenticazione
ilcorsaroblu_user = {
    "uid": "ogekuri",
    "pwd": "Oge!123456"
}


# engines = [thepiratebay(), one337x(), limetorrents(), torrentproject(), ilcorsaronero(), torrentz(), torrentgalaxy(), therarbg(), ilcorsaroblu(ilcorsaroblu_user['uid'], ilcorsaroblu_user['pwd'])]
# engines = [thepiratebay()]
# engines = [one337x()]
# engines = [limetorrents()]
# engines = [torrentproject()]
# engines = [ilcorsaronero()]
# engines = [torrentz()]
engines = [torrentgalaxy()]
# engines = [therarbg()]
# engines = [ilcorsaroblu(ilcorsaroblu_user['uid'], ilcorsaroblu_user['pwd'])]

# SEARCH_STRING="Arcane S02 ITA"
# SEARCH_TYPE="tv"

# SEARCH_STRING="Wolfs 2024 ITA"
# SEARCH_TYPE="movies"

# SEARCH_STRING="Wolfs 2024"
# SEARCH_TYPE="movies"

SEARCH_STRING="The Fall Guy 2024 ITA"
SEARCH_TYPE="movies"

# SEARCH_STRING="Star Wars Tales of the Empire S01"
# SEARCH_TYPE="tv"

# SEARCH_STRING="Star Wars"
# SEARCH_TYPE="tv"

print(f"Search: {SEARCH_STRING}/{SEARCH_TYPE}")

def __is_torrent(link: str) -> bool:
    # Controlla se il link termina con ".torrent"
    return link.endswith(".torrent")

def __is_magnet_link(link: str) -> bool:
    # Check if link inizia con "magnet:?"
    return link.startswith("magnet:?")

async def main():
    all_results = []
    for engine in engines:
        await engine.login()
        results = await engine.search(SEARCH_STRING, SEARCH_TYPE)
        if results is not None:
            for result in results:
                result['engine'] = engine
                all_results.append(result)

    # final results
    final_results = []
    if all_results is not None:
        for result in all_results:
            engine = result['engine']
            link = result['link'] 
            if not __is_magnet_link(link) and not __is_torrent(link):
                link = await engine.download_torrent(result['link'])
                result['link'] = link
                final_results.append(result)
            else:
                final_results.append(result)

    if final_results is not None:
        print("NUM RESULT: ", len(final_results))
        print("###########################################################")
        for result in final_results:
            engine = result['engine']
            print('RESULT - engine:' + engine.name + ', name: ' + str(result['name']) + ', link: ' + str(result['link']))
            print("-----------------------------------------------------------")
    
    for engine in engines:
        await engine.close()  # Buona pratica: chiudere manualmente

asyncio.run(main())
