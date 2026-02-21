"""
@file src/debriddo/constants.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# AUTHORS: Ogekuri

# Application name
#: @brief Exported constant `APPLICATION_NAME` used by runtime workflows.
APPLICATION_NAME = "Debriddo"
#: @brief Exported constant `APPLICATION_VERSION` used by runtime workflows.
APPLICATION_VERSION = "0.0.36"
#: @brief Exported constant `APPLICATION_DESCRIPTION` used by runtime workflows.
APPLICATION_DESCRIPTION = "Ricerca online i Film e le tue Serie Tv preferite."

# SQL3llite database
#: @brief Exported constant `CACHE_DATABASE_FILE` used by runtime workflows.
CACHE_DATABASE_FILE = "caches_items.db"

# Link per AllDebrid/Real-Debird/Premiumize che è ritornato in caso di errore
#: @brief Exported constant `NO_CACHE_VIDEO_URL` used by runtime workflows.
NO_CACHE_VIDEO_URL = "https://github.com/Ogekuri/debriddo/raw/refs/heads/master/videos/nocache.mp4"

# Run in multi-thread
#: @brief Exported constant `RUN_IN_MULTI_THREAD` used by runtime workflows.
RUN_IN_MULTI_THREAD = True
