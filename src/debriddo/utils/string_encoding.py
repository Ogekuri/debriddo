"""
@file src/debriddo/utils/string_encoding.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.35
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
import re
from unidecode import unidecode
import lzstring


def encode_lzstring(json_value, tag):
    """
    @brief Execute `encode_lzstring` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param json_value Runtime input parameter consumed by `encode_lzstring`.
    @param tag Runtime input parameter consumed by `encode_lzstring`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    lz = lzstring.LZString()
    if type(tag) is not str and len(tag) != 2:
        raise ValueError("Incompatible tag encoding lz-string")
    try:
        json_string = json.dumps(json_value)
        data = tag + lz.compressToEncodedURIComponent(json_string)
    except Exception as e:
        raise ValueError(f"An error occurred decoding lz-string: {e}")
    
    return data


def decode_lzstring(data, tag):
    """
    @brief Execute `decode_lzstring` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param data Runtime input parameter consumed by `decode_lzstring`.
    @param tag Runtime input parameter consumed by `decode_lzstring`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    lz = lzstring.LZString()

    # Se il prefisso "C_" è presente, rimuovilo
    if data.startswith(tag):
        data = data[2:]
    else:
        raise ValueError("Incompatible tag decoding lz-string")
    try:
        decompressed = lz.decompressFromEncodedURIComponent(data)
        if decompressed is None:
            raise ValueError("Failed to decompress lz-string payload")
        json_value = json.loads(decompressed)
    except Exception as e:
        raise ValueError(f"An error occurred decoding lz-string: {e}")

    return json_value

def normalize(string):
    # kožušček -> kozuscek
    # 北亰 -> Bei Jing
    # François -> Francois
    """
    @brief Execute `normalize` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param string Runtime input parameter consumed by `normalize`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    string = unidecode(string)
    string = re.sub("'s ", ' ', string) # ’s -> ''
    string = re.sub('[^0-9a-zA-Z]', ' ', string)
    string = re.sub(' +', ' ', string)
    string = string.lower()
    return string

    
