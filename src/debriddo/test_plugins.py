"""
@file src/debriddo/test_plugins.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: Ogekuri

import asyncio
from pathlib import Path

from debriddo.search.plugins.torrentgalaxyone import torrentgalaxy

# Allow execution as a standalone script from any working directory.
#: @brief Exported constant `SRC_DIR` used by runtime workflows.
SRC_DIR = Path(__file__).resolve().parents[1]


# Dati del form di autenticazione
ilcorsaroblu_user = {
    "uid": "ogekuri",
    "pwd": "Oge!123456"
}


def build_engines():
    """
    @brief Execute `build_engines` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    return [
        torrentgalaxy({})
    ]


#: @brief Exported constant `SEARCH_STRING` used by runtime workflows.
SEARCH_STRING = "The Fall Guy 2024 ITA"
#: @brief Exported constant `SEARCH_TYPE` used by runtime workflows.
SEARCH_TYPE = "movies"

def __is_torrent(link: str) -> bool:
    # Controlla se il link termina con ".torrent"
    """
    @brief Execute `__is_torrent` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param link Runtime input parameter consumed by `__is_torrent`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    return link.endswith(".torrent")

def __is_magnet_link(link: str) -> bool:
    # Check if link inizia con "magnet:?"
    """
    @brief Execute `__is_magnet_link` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param link Runtime input parameter consumed by `__is_magnet_link`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    return link.startswith("magnet:?")

async def main():
    """
    @brief Execute `main` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    engines = build_engines()
    print(f"Search: {SEARCH_STRING}/{SEARCH_TYPE}")
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
        pass  # Plugin instances don't need explicit close

if __name__ == "__main__":
    asyncio.run(main())
