# VERSION: 0.0.34
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono


class Cinemeta(MetadataProvider):

    async def get_metadata(self, id, type):
        self.logger.debug("Getting metadata for " + type + " with id " + id)

        full_id = id.split(":")

        url = f"https://v3-cinemeta.strem.io/meta/{type}/{full_id[0]}.json"
        session = AsyncThreadSafeSession()  # Usa il client asincrono
        response = await session.request_get(url)
        await session.close()
        if response is not None:
            data = response.json()

            if type == "movie":
                result = Movie(
                    id=id,
                    titles=[self.replace_weird_characters(data["meta"]["name"])],
                    year=data["meta"]["year"],
                    languages=["en"]
                )
            else:
                result = Series(
                    id=id,
                    titles=[self.replace_weird_characters(data["meta"]["name"])],
                    season="S{:02d}".format(int(full_id[1])),
                    episode="E{:02d}".format(int(full_id[2])),
                    languages=["en"]
                )

            self.logger.debug("Got metadata for " + type + " with id " + id)
            return result
        return None
