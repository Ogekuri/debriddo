# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

class Media:
    """
    Rappresenta un media generico (film o serie TV).
    """
    def __init__(self, id, titles, languages, type):
        """
        Inizializza un oggetto Media.

        Args:
            id (str): L'identificatore del media (es. IMDB ID).
            titles (list): Lista dei titoli associati.
            languages (list): Lista delle lingue.
            type (str): Il tipo di media ('movie' o 'series').
        """
        self.id = id
        self.titles = titles
        self.languages = languages
        self.type = type
