# VERSION: 0.0.34
# AUTHORS: Ogekuri

from typing import Any


class SearchIndexer:
    def __init__(self):
        self.title: str = ""       # general name
        self.id: int = 0           # id
        self.language: str | None = None    # supported language
        self.tv_search_capatabilities: str | None = None
        self.movie_search_capatabilities: str | None = None
        self.engine: Any = None      # engine object
        self.engine_name: str = "" # engine name
