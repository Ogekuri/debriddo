from types import SimpleNamespace

from debriddo.utils.filter_results import filter_out_non_matching


def build_item(raw_title, seasons=None, episodes=None):
    return SimpleNamespace(
        raw_title=raw_title,
        parsed_data=SimpleNamespace(
            seasons=seasons if seasons is not None else [],
            episodes=episodes if episodes is not None else [],
        ),
    )


def test_filter_out_non_matching_keeps_classic_episode_match():
    items = [
        build_item("Person of Interest S03E01", seasons=[3], episodes=[1]),
        build_item("Person of Interest S03E02", seasons=[3], episodes=[2]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest S03E01"


def test_filter_out_non_matching_keeps_complete_pack_snn_e01_e_pattern():
    items = [
        build_item("Person of Interest S03E01-E10 1080p", seasons=[], episodes=[]),
        build_item("Person of Interest S02E01-E10 1080p", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest S03E01-E10 1080p"


def test_filter_out_non_matching_keeps_localized_season_label():
    items = [
        build_item("Person of Interest Stagione 3 1080p", seasons=[], episodes=[]),
        build_item("Person of Interest Season 2 1080p", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest Stagione 3 1080p"
