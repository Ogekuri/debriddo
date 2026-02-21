"""
@file src/debriddo/utils/filter/base_filter.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.36
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

class BaseFilter:
    """
    @brief Class `BaseFilter` encapsulates cohesive runtime behavior.
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
        self.config = config
        self.item_type = additional_config

    def filter(self, data):
        """
        @brief Execute `filter` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `filter`.
        @param data Runtime input parameter consumed by `filter`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        raise NotImplementedError

    def can_filter(self):
        """
        @brief Execute `can_filter` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `can_filter`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        raise NotImplementedError

    def __call__(self, data):
        """
        @brief Execute `__call__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__call__`.
        @param data Runtime input parameter consumed by `__call__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if self.config is not None and self.can_filter():
            return self.filter(data)
        return data
