import queue

from RTN import parse

from debriddo.models.series import Series
from debriddo.torrent.torrent_item import TorrentItem
from debriddo.utils.stremio_parser import parse_to_debrid_stream


def test_parse_to_debrid_stream_handles_parsed_data_without_data_field():
    media = Series(
        id="tt1839578:3:1",
        titles=["Person of Interest"],
        season="S03",
        episode="E01",
        languages=["en"],
    )
    parsed = parse("Person of Interest S03E01 1080p")
    torrent_item = TorrentItem(
        raw_title="Person of Interest S03E01 1080p",
        title="Person of Interest",
        size=1024 * 1024 * 1024,
        magnet="magnet:?xt=urn:btih:abc",
        info_hash="abc",
        link="magnet:?xt=urn:btih:abc",
        seeders=1,
        languages=["en"],
        indexer="test",
        engine_name="test",
        privacy="public",
        type="series",
        parsed_data=parsed,
    )
    torrent_item.file_index = 0
    torrent_item.file_name = "file.mkv"
    torrent_item.availability = True

    results = queue.Queue()

    parse_to_debrid_stream(torrent_item, "C_dummy", "http://localhost", False, results, media)

    assert results.qsize() == 1
    stream_item = results.get_nowait()
    assert stream_item["name"].startswith("[⚡")
    assert stream_item["url"].startswith("http://localhost/playback/C_dummy/")
    assert stream_item["behaviorHints"]["bingeGroup"] == "debriddo-abc"
