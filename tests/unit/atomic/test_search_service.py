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
    service = SearchService({"languages": ["en"]})
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
    service = SearchService({"languages": ["it"]})
    primary_query = normalize("Dune 2024")
    fallback_query = normalize("Dune")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={fallback_query: build_result("Dune 2024")},
        language="it",
    )
    indexer.language = indexer.engine.language
    indexer.title = indexer.engine.name
    indexer.engine_name = "dummy"
    indexer.movie_search_capatabilities = "movies"

    movie = Movie(id="tt15239678", titles=["Dune"], year="2024", languages=["it"])

    results = asyncio.run(service._SearchService__search_movie_indexer(movie, indexer))

    assert [call[0] for call in indexer.engine.calls] == [primary_query, fallback_query]
    assert len(results) == 1


def test_search_series_indexer_runs_primary_queries_and_skips_fallback():
    service = SearchService({"languages": ["en"]})
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
    service = SearchService({"languages": ["en"]})
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


def test_search_movie_indexer_without_config_languages_runs_single_search_without_lang_tag():
    service = SearchService({})
    primary_query = normalize("Dune 2024")
    fallback_query = normalize("Dune")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={fallback_query: build_result("Fallback no lang")},
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


def test_search_movie_indexer_skips_fallback_when_any_primary_has_results():
    service = SearchService({"languages": ["en", "it"]})
    primary_query_en = normalize("Dune 2024 ENG")
    primary_query_it = normalize("Dune ITA 2024 ITA")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={primary_query_en: build_result("Primary EN")},
        language="fr",
    )
    indexer.language = indexer.engine.language
    indexer.title = indexer.engine.name
    indexer.engine_name = "dummy"
    indexer.movie_search_capatabilities = "movies"

    movie = Movie(id="tt15239678", titles=["Dune", "Dune ITA"], year="2024", languages=["en", "it"])

    results = asyncio.run(service._SearchService__search_movie_indexer(movie, indexer))

    assert [call[0] for call in indexer.engine.calls] == [primary_query_en, primary_query_it]
    assert len(results) == 1


def test_search_series_indexer_uses_localized_season_and_omits_lang_tag_for_matching_non_en_indexer():
    service = SearchService({"languages": ["it"]})
    primary_episode = normalize("Person of Interest S03E01")
    primary_pack = normalize("Person of Interest S03E01-E")
    primary_season = normalize("Person of Interest Stagione 3")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={primary_season: build_result("Season IT")},
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
        languages=["it"],
    )

    results = asyncio.run(service._SearchService__search_series_indexer(series, indexer))

    assert [call[0] for call in indexer.engine.calls] == [
        primary_episode,
        primary_pack,
        primary_season,
    ]
    assert len(results) == 1


def test_search_series_indexer_skips_fallback_when_any_primary_result_exists():
    service = SearchService({"languages": ["en", "it"]})
    primary_episode_en = normalize("Person of Interest S03E01 ENG")
    primary_pack_en = normalize("Person of Interest S03E01-E ENG")
    primary_season_en = normalize("Person of Interest Season 3 ENG")
    primary_episode_it = normalize("Person of Interest S03E01 ITA")
    primary_pack_it = normalize("Person of Interest S03E01-E ITA")
    primary_season_it = normalize("Person of Interest Stagione 3 ITA")
    indexer = SearchIndexer()
    indexer.engine = DummyEngine(
        results_by_query={primary_episode_en: build_result("Episode EN")},
        language="fr",
    )
    indexer.language = indexer.engine.language
    indexer.title = indexer.engine.name
    indexer.engine_name = "dummy"
    indexer.tv_search_capatabilities = "tv"

    series = Series(
        id="tt1839578:3:1",
        titles=["Person of Interest", "Person of Interest"],
        season="S03",
        episode="E01",
        languages=["en", "it"],
    )

    results = asyncio.run(service._SearchService__search_series_indexer(series, indexer))

    assert [call[0] for call in indexer.engine.calls] == [
        primary_episode_en,
        primary_pack_en,
        primary_season_en,
        primary_episode_it,
        primary_pack_it,
        primary_season_it,
    ]
    assert len(results) == 1
