# VERSION: 0.0.32
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from models.media import Media

class Movie(Media):
    def __init__(self, id, titles, year, languages):
        super().__init__(id, titles, languages, "movie")
        self.year = year
