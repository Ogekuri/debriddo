"""
@file src/debriddo/metdata/tmdb.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.39
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from debriddo.metdata.metadata_provider_base import MetadataProvider
from debriddo.models.movie import Movie
from debriddo.models.series import Series
from debriddo.utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono

class TMDB(MetadataProvider):

    """
    @brief Class `TMDB` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    async def get_metadata(self, id, type):
        """
        @brief Execute `get_metadata` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get_metadata`.
        @param id Runtime input parameter consumed by `get_metadata`.
        @param type Runtime input parameter consumed by `get_metadata`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.logger.debug("Getting metadata for " + type + " with id " + id)

        full_id = id.split(":")

        result = None
        languages = self.config.get('languages') or ["en"]

        for lang in languages:
            url = f"https://api.themoviedb.org/3/find/{full_id[0]}?api_key={self.config['tmdbApi']}&external_source=imdb_id&language={lang}"
            session = AsyncThreadSafeSession()  # Usa il client asincrono
            response = await session.request_get(url)
            await session.close()
            if response is not None:
                data = response.json()

                if lang == languages[0]:
                    if type == "movie":
                        result = Movie(
                            id=id,
                            titles=[self.replace_weird_characters(data["movie_results"][0]["title"])],
                            year=data["movie_results"][0]["release_date"][:4],
                            languages=languages
                        )
                    else:
                        result = Series(
                            id=id,
                            titles=[self.replace_weird_characters(data["tv_results"][0]["name"])],
                            season="S{:02d}".format(int(full_id[1])),
                            episode="E{:02d}".format(int(full_id[2])),
                            languages=languages
                        )
                else:
                    if result is None:
                        continue
                    if type == "movie":
                        result.titles.append(self.replace_weird_characters(data["movie_results"][0]["title"]))
                    else:
                        result.titles.append(self.replace_weird_characters(data["tv_results"][0]["name"]))

        self.logger.debug("Got metadata for " + type + " with id " + id)
        return result
