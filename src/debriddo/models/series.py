"""
@file src/debriddo/models/series.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.models.media import Media

class Series(Media):
    """@brief Class `Series` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
"""
    def __init__(self, id, titles, season, episode, languages):
        """@brief Function `__init__` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param id Runtime parameter.
@param titles Runtime parameter.
@param season Runtime parameter.
@param episode Runtime parameter.
@param languages Runtime parameter.
"""
        super().__init__(id, titles, languages, "series")
        self.season = season
        self.episode = episode
        self.seasonfile = None
