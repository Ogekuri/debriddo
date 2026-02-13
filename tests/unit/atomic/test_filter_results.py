from types import SimpleNamespace

import pytest

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


def test_filter_out_non_matching_keeps_snn_space_emm_episode_match():
    items = [
        build_item("Person of Interest S03 E01", seasons=[], episodes=[]),
        build_item("Person of Interest S03 E02", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest S03 E01"


def test_filter_out_non_matching_keeps_snn_dash_emm_episode_match():
    items = [
        build_item("Person of Interest S03-E01", seasons=[], episodes=[]),
        build_item("Person of Interest S03-E02", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest S03-E01"


def test_filter_out_non_matching_keeps_complete_pack_snn_e01_e_pattern():
    items = [
        build_item("Person of Interest S03E01-E10 1080p", seasons=[], episodes=[]),
        build_item("Person of Interest S02E01-E10 1080p", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest S03E01-E10 1080p"


def test_filter_out_non_matching_keeps_complete_pack_snn_e01_range_without_second_e():
    items = [
        build_item("Person of Interest S03E01-23 1080p", seasons=[], episodes=[]),
        build_item("Person of Interest S02E01-23 1080p", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest S03E01-23 1080p"


def test_filter_out_non_matching_keeps_localized_complete_season_label():
    items = [
        build_item("Person of Interest Stagione 3 foo bar COMPLETA 1080p", seasons=[], episodes=[]),
        build_item("Person of Interest Stagione 3 1080p", seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert len(filtered) == 1
    assert filtered[0].raw_title == "Person of Interest Stagione 3 foo bar COMPLETA 1080p"


@pytest.mark.parametrize(
    ("raw_title", "is_valid"),
    [
        ("Person.Of.Interest.S05E01-13.WEBDL.ITA.ENG.Aac.m1080p", False),
        ("Person.Of.Interest.S04E01-22.WEBDL.ITA.ENG.Aac.m1080p", False),
        ("Person.Of.Interest.S03E01-23.WEBDL.ITA.ENG.Aac.m1080p", True),
        ("Person.Of.Interest.S02E01-22.WEBDL.ITA.ENG.Aac.m1080p", False),
        ("Person.Of.Interest.S01E01-23.WEBDL.ITA.ENG.Aac.m1080p", False),
        ("Person of Interest Stagione 4 (2015) [COMPLETA] 1080p", False),
        ("Person of Interest Stagione 2 (2013) [COMPLETA] 1080p", False),
        ("Person of Interest Stagione 1 (2012) [COMPLETA] 1080p", False),
        ("Person of Interest Stagione 3 (2014) [COMPLETA] 1080p", True),
        ("Person of Interest Stagione 5 (2016) [COMPLETA] 1080p", False),
        ("Person of Interest S05 ITA ENG 720p BDMux x264", False),
        ("Person of Interest S03 ITA ENG 720p BDMux x264", False),
        ("Person of Interest Season S03E01-07 ITA ENG 1080p", True),
        ("Person of Interest Season S03E07-22 ITA ENG 1080p", False),
        ("Person of Interest Season S03 ITA ENG 1080p", False),
        ("Person of Interest Season S03 foo bar COMPLETE ITA ENG 1080p", True),
        ("Person of Interest Stagione 3 foo bar COMPLETA ITA ENG 1080p", True),
        ("Person of Interest Stagione 3 ITA ENG 1080p", False),
    ],
)
def test_filter_out_non_matching_matches_requested_series_logic(raw_title, is_valid):
    items = [
        build_item(raw_title, seasons=[], episodes=[]),
    ]

    filtered = filter_out_non_matching(items, "S03", "E01")

    assert (len(filtered) == 1) is is_valid
