"""
@file src/debriddo/utils/filter/language_filter.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger

logger = setup_logger(__name__)


class LanguageFilter(BaseFilter):
    """
    @brief Class `LanguageFilter` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    def __init__(self, config):
        """
        @brief Execute `__init__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__init__`.
        @param config Runtime input parameter consumed by `__init__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        super().__init__(config)

    def filter(self, data):
        """
        @brief Execute `filter` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `filter`.
        @param data Runtime input parameter consumed by `filter`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        filtered_data = []
        for torrent in data:
            if len(torrent.languages) == 0:
                continue

            for language in torrent.languages:
                if language in self.config['languages']:
                    filtered_data.append(torrent)
                    continue

            if "multi" in torrent.languages:
                filtered_data.append(torrent)
        return filtered_data

    def can_filter(self):
        """
        @brief Execute `can_filter` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `can_filter`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        return bool(self.config.get('languages'))
