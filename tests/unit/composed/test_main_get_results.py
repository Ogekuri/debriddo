import asyncio
import logging
from types import SimpleNamespace

from debriddo import main
from debriddo.search.search_result import SearchResult


class DummyMetadataProvider:
    def __init__(self, config):
        self.config = config

    async def get_metadata(self, stream_id, stream_type):
        return SimpleNamespace(
            type="movie",
            titles=["Example Movie"],
            year="2024",
            languages=["en"],
        )


class DummySearchService:
    def __init__(self, config):
        self.config = config

    async def search(self, media):
        result_one = SearchResult()
        result_one.raw_title = "foobar 1"
        result_one.title = "foobar 1"
        result_one.info_hash = "infohash 1"

        result_two = SearchResult()
        result_two.raw_title = "foobar 2"
        result_two.title = "foobar 2"
        result_two.info_hash = "infohash 2"

        return [result_one, result_two]


class DummyTorrentService:
    async def convert_and_process(self, results):
        return []


def dummy_filter_items(items, media, config):
    main.logger.debug(f"Item count before filtering: {len(items)}")
    return items


def test_get_results_logs_engine_results_before_filtering(monkeypatch, caplog):
    config = {
        "metadataProvider": "cinemeta",
        "tmdbApi": None,
        "cache": False,
        "search": True,
        "minCacheResults": 1,
        "debrid": False,
        "service": "realdebrid",
    }

    monkeypatch.setattr(main, "parse_config", lambda _: config)
    monkeypatch.setattr(main, "Cinemeta", DummyMetadataProvider)
    monkeypatch.setattr(main, "TMDB", DummyMetadataProvider)
    monkeypatch.setattr(main, "SearchService", DummySearchService)
    monkeypatch.setattr(main, "TorrentService", DummyTorrentService)
    monkeypatch.setattr(main, "filter_items", dummy_filter_items)
    monkeypatch.setattr(main, "get_debrid_service", lambda _: object())

    request = SimpleNamespace(client=SimpleNamespace(host="127.0.0.1"))

    main.logger.setLevel(logging.DEBUG)
    caplog.set_level(logging.DEBUG, logger=main.logger.name)

    with caplog.at_level(logging.DEBUG):
        asyncio.run(main.get_results("config", "movie", "tt1234567", request))

    messages = [record.getMessage() for record in caplog.records]
    filtering_log = "Filtering Torrent Search (Engines) results"
    first_entry = "01. \"foobar 1\" [infohash infohash 1]"
    second_entry = "02. \"foobar 2\" [infohash infohash 2]"
    count_log = "Item count before filtering: 2"

    assert filtering_log in messages
    assert first_entry in messages
    assert second_entry in messages
    assert count_log in messages
    assert messages.index(filtering_log) < messages.index(first_entry)
    assert messages.index(first_entry) < messages.index(second_entry)
    assert messages.index(second_entry) < messages.index(count_log)
