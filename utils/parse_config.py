# VERSION: 0.0.34
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from utils.string_encoding import decode_lzstring, encode_lzstring

# wrapping alla decode_lzstring per gestire eventuali retro-compatibità
def parse_config(encoded_config):
        
    # decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
    config = decode_lzstring(encoded_config, "C_")

    return config


# wrapping alla decode_lzstring per gestire eventuali retro-compatibità
def parse_query(encoded_query):
        
    # decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
    query = decode_lzstring(encoded_query, "Q_")

    return query

# wrapping alla encode_lzstring per gestire eventuali retro-compatibità
def encode_query(query):
        
    # decodifica utilizzando l'algoritmo di LZString con encodeURIComponent
    encoded_query = encode_lzstring(query, "Q_")

    return encoded_query