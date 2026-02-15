"""
@file src/debriddo/utils/parse_config.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.utils.string_encoding import decode_lzstring, encode_lzstring

# wrapping alla decode_lzstring per gestire eventuali retro-compatibità
def parse_config(encoded_config):
        
    # decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
    """
    @brief Execute `parse_config` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param encoded_config Runtime input parameter consumed by `parse_config`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    config = decode_lzstring(encoded_config, "C_")

    return config


# wrapping alla decode_lzstring per gestire eventuali retro-compatibità
def parse_query(encoded_query):
        
    # decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
    """
    @brief Execute `parse_query` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param encoded_query Runtime input parameter consumed by `parse_query`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    query = decode_lzstring(encoded_query, "Q_")

    return query

# wrapping alla encode_lzstring per gestire eventuali retro-compatibità
def encode_query(query):
        
    # decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
    """
    @brief Execute `encode_query` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param query Runtime input parameter consumed by `encode_query`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    encoded_query = encode_lzstring(query, "Q_")

    return encoded_query