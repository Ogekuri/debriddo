# VERSION: 0.0.27
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import json
from lzstring import LZString

# from utils.string_encoding import decodeb64

# def parse_config(b64config):
#     config = json.loads(decodeb64(b64config))

#     # For backwards compatibility
#     if "languages" not in config:
#         config["languages"] = [config["language"]]

#     return config

def parse_config(encoded_config):
    
    lz = LZString()

    # Se il prefisso "C_" è presente, rimuovilo
    if encoded_config.startswith("C_"):
        encoded_config = encoded_config[2:]
    
    # decodifica e decomprime utilizzando l'algoritmo di LZString con encodeURIComponent
    decompressed = lz.decompressFromEncodedURIComponent(encoded_config)
    config = json.loads(decompressed)

    # Compatibilità retroattiva
    if "languages" not in config and "language" in config:
        config["languages"] = [config["language"]]

    return config
