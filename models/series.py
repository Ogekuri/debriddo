# VERSION: 0.0.32
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from models.media import Media

class Series(Media):
    def __init__(self, id, titles, season, episode, languages):
        super().__init__(id, titles, languages, "series")
        self.season = season
        self.episode = episode
        self.seasonfile = None
