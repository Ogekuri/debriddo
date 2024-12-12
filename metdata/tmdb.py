# VERSION: 0.0.30
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from metdata.metadata_provider_base import MetadataProvider
from models.media import Media
from models.movie import Movie
from models.series import Series
from utils.logger import setup_logger
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono

class TMDB(MetadataProvider):

    async def get_metadata(self, id, type):
        self.logger.debug("Getting metadata for " + type + " with id " + id)

        full_id = id.split(":")

        result = None

        for lang in self.config['languages']:
            url = f"https://api.themoviedb.org/3/find/{full_id[0]}?api_key={self.config['tmdbApi']}&external_source=imdb_id&language={lang}"
            session = AsyncThreadSafeSession()  # Usa il client asincrono
            response = await session.request_get(url)
            await session.close()
            if response is not None:
                data = response.json()

                if lang == self.config['languages'][0]:
                    if type == "movie":
                        result = Movie(
                            id=id,
                            titles=[self.replace_weird_characters(data["movie_results"][0]["title"])],
                            year=data["movie_results"][0]["release_date"][:4],
                            languages=self.config['languages']
                        )
                    else:
                        result = Series(
                            id=id,
                            titles=[self.replace_weird_characters(data["tv_results"][0]["name"])],
                            season="S{:02d}".format(int(full_id[1])),
                            episode="E{:02d}".format(int(full_id[2])),
                            languages=self.config['languages']
                        )
                else:
                    if type == "movie":
                        result.titles.append(self.replace_weird_characters(data["movie_results"][0]["title"]))
                    else:
                        result.titles.append(self.replace_weird_characters(data["tv_results"][0]["name"]))

        self.logger.debug("Got metadata for " + type + " with id " + id)
        return result

