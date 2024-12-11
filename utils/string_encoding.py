# VERSION: 0.0.27
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

import base64
import re
from unidecode import unidecode


def encodeb64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')


def decodeb64(data):
    return base64.b64decode(data).decode('utf-8')

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

    