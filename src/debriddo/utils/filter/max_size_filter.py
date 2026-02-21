"""
@file src/debriddo/utils/filter/max_size_filter.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.38
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.utils.filter.base_filter import BaseFilter
from debriddo.utils.logger import setup_logger

logger = setup_logger(__name__)


class MaxSizeFilter(BaseFilter):
    """
    @brief Class `MaxSizeFilter` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    def __init__(self, config, additional_config=None):
        """
        @brief Execute `__init__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__init__`.
        @param config Runtime input parameter consumed by `__init__`.
        @param additional_config Runtime input parameter consumed by `__init__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        super().__init__(config, additional_config)

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
            if torrent.size <= (int(self.config['maxSize']) * 1024 * 1024 * 1024):
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
        return int(self.config['maxSize']) > 0 and self.item_type == 'movie'
