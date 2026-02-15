"""
@file src/debriddo/models/movie.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.models.media import Media

class Movie(Media):
    """
    Rappresenta un film.
    """
    def __init__(self, id, titles, year, languages):
        """
        Inizializza un oggetto Movie.

        Args:
        id (str): L'identificatore del film.
        titles (list): Lista dei titoli.
        year (str|int): L'anno di uscita.
        languages (list): Lista delle lingue.
        """
        super().__init__(id, titles, languages, "movie")
        self.year = year
