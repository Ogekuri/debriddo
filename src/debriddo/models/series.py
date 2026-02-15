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
    """
    Rappresenta un episodio di una serie TV.
    """
    def __init__(self, id, titles, season, episode, languages):
        """
        Inizializza un oggetto Series.

        Args:
        id (str): L'identificatore della serie.
        titles (list): Lista dei titoli.
        season (str): Identificatore della stagione (es. S01).
        episode (str): Identificatore dell'episodio (es. E01).
        languages (list): Lista delle lingue.
        """
        super().__init__(id, titles, languages, "series")
        self.season = season
        self.episode = episode
        self.seasonfile = None
