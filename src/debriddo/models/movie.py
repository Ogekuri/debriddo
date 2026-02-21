"""
@file src/debriddo/models/movie.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.38
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.models.media import Media

class Movie(Media):
    """@brief Class `Movie` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
"""
    def __init__(self, id, titles, year, languages):
        """@brief Function `__init__` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param id Runtime parameter.
@param titles Runtime parameter.
@param year Runtime parameter.
@param languages Runtime parameter.
"""
        super().__init__(id, titles, languages, "movie")
        self.year = year
