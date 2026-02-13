import asyncio

from debriddo.models.series import Series
from debriddo.search.search_indexer import SearchIndexer
from debriddo.search.search_service import SearchService


class DummyEngine:
    name = "DummyEngine"
    language = "it"
    supported_categories = {"tv": True, "movies": True, "all": True}

    async def search(self, search_string, category):
        return []


def test_search_series_indexer_with_unsupported_language_returns_empty():
    service = SearchService({})
    indexer = SearchIndexer()
    indexer.engine = DummyEngine()
    indexer.language = indexer.engine.language
    indexer.title = indexer.engine.name
    indexer.engine_name = "dummy"
    indexer.tv_search_capatabilities = "tv"

    series = Series(
        id="tt1839578:3:1",
        titles=["Person of Interest"],
        season="S03",
        episode="E01",
        languages=["en"],
    )

    results = asyncio.run(service._SearchService__search_series_indexer(series, indexer))

    assert results == []
