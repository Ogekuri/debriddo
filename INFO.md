
# Informazioni per gli sviluppatori

## Versionamento, repository e deplyoment

    - La costante APPLICATION_VERSION nel constant.py contiene il numero di versione nel formato x.y.z (ad esempio 1.2.3).

    - Le versioni rilasciate vengono taggate nel brench "master" nel formato vx.y.z (ad esempio v1.2.3).

    - Ad ogni rilascio, quando il master viene taggato, una nuova immagine docker viene buildata e resa disponibile.

## TODO

### Implementazioni

    * Implementare il supporto per https://debrid-link.com/
    * Implementare il supporto per Il Corsaro Blu
    * Modificare CORSMiddleware, cambiare "origins"

### Test

    * Testare NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/main/videos/nocache.mp4"
