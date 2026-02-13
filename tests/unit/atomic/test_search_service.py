import asyncio

from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.search.search_indexer import SearchIndexer
from debriddo.search.search_service import SearchService
from debriddo.utils.string_encoding import normalize


class DummyEngine:
    name = "DummyEngine"
    supported_categories = {"tv": True, "movies": True, "all": True}

    def __init__(self, results_by_query=None, language="it"):
        self.language = language
        self.calls = []
        self._results_by_query = results_by_query or {}

    async def search(self, search_string, category):
        self.calls.append((search_string, category))
        return self._results_by_query.get(search_string, [])


def build_result(name):
    return [{"seeds": 1, "name": name, "size": 1024, "link": "magnet:?xt=urn:btih:abc"}]


def test_search_series_indexer_with_unsupported_language_returns_empty():
    service = SearchService({})
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(language="it")
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


def test_search_movie_indexer_uses_language_tag_and_fallback_when_needed():
    service = SearchService({})
    primary_query = normalize("Dune 2024 ENG")
    fallback_query = normalize("Dune ENG")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={fallback_query: build_result("Dune 2024")},
        language="it",
    )
    indexer.language = indexer.engine.language
    indexer.title = indexer.engine.name
    indexer.engine_name = "dummy"
    indexer.movie_search_capatabilities = "movies"

    movie = Movie(id="tt15239678", titles=["Dune"], year="2024", languages=["en"])

    results = asyncio.run(service._SearchService__search_movie_indexer(movie, indexer))

    assert [call[0] for call in indexer.engine.calls] == [primary_query, fallback_query]
    assert len(results) == 1


def test_search_movie_indexer_omits_language_tag_when_language_matches():
    service = SearchService({})
    primary_query = normalize("Dune 2024")
    fallback_query = normalize("Dune")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={fallback_query: build_result("Dune 2024")},
        language="en",
    )
    indexer.language = indexer.engine.language
    indexer.title = indexer.engine.name
    indexer.engine_name = "dummy"
    indexer.movie_search_capatabilities = "movies"

    movie = Movie(id="tt15239678", titles=["Dune"], year="2024", languages=["en"])

    results = asyncio.run(service._SearchService__search_movie_indexer(movie, indexer))

    assert [call[0] for call in indexer.engine.calls] == [primary_query, fallback_query]
    assert len(results) == 1


def test_search_series_indexer_runs_primary_queries_and_skips_fallback():
    service = SearchService({})
    primary_episode = normalize("Person of Interest S03E01 ENG")
    primary_season = normalize("Person of Interest Season 3 ENG")
    primary_pack = normalize("Person of Interest S03E01-E ENG")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={primary_season: build_result("Season pack")},
        language="it",
    )
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

    assert [call[0] for call in indexer.engine.calls] == [
        primary_episode,
        primary_pack,
        primary_season,
    ]
    assert len(results) == 1


def test_search_series_indexer_runs_fallback_when_primary_empty():
    service = SearchService({})
    primary_episode = normalize("Person of Interest S03E01 ENG")
    primary_season = normalize("Person of Interest Season 3 ENG")
    primary_pack = normalize("Person of Interest S03E01-E ENG")
    fallback_query = normalize("Person of Interest ENG")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={fallback_query: build_result("Fallback")},
        language="it",
    )
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

    assert [call[0] for call in indexer.engine.calls] == [
        primary_episode,
        primary_pack,
        primary_season,
        fallback_query,
    ]
    assert len(results) == 1
