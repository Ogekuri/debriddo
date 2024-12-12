# VERSION: 0.0.31
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
import re
from unidecode import unidecode
import lzstring


def encode_lzstring(json_value, tag):
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
    lz = lzstring.LZString()

    # Se il prefisso "C_" è presente, rimuovilo
    if data.startswith(tag):
        data = data[2:]
    else:
        raise ValueError("Incompatible tag decoding lz-string")
    try:
        decompressed = lz.decompressFromEncodedURIComponent(data)
        json_value = json.loads(decompressed)
    except Exception as e:
        raise ValueError(f"An error occurred decoding lz-string: {e}")

    return json_value

def normalize(string):
    # kožušček -> kozuscek
    # 北亰 -> Bei Jing
    # François -> Francois
    string = unidecode(string)
    string = re.sub("'s ", ' ', string) # ’s -> ''
    string = re.sub('[^0-9a-zA-Z]', ' ', string)
    string = re.sub(' +', ' ', string)
    string = string.lower()
    return string

    