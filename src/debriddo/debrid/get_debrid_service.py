"""
@file src/debriddo/debrid/get_debrid_service.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.39
# AUTHORS: aymene69
# CONTRIBUTORS: Ogekuri

from fastapi.exceptions import HTTPException

from debriddo.debrid.alldebrid import AllDebrid
from debriddo.debrid.premiumize import Premiumize
from debriddo.debrid.realdebrid import RealDebrid
from debriddo.debrid.torbox import TorBox


def get_debrid_service(config):
    """
    @brief Execute `get_debrid_service` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param config Runtime input parameter consumed by `get_debrid_service`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    service_name = config['service']
    if service_name == "realdebrid":
        debrid_service = RealDebrid(config)
    elif service_name == "alldebrid":
        debrid_service = AllDebrid(config)
    elif service_name == "premiumize":
        debrid_service = Premiumize(config)
    elif service_name == "torbox":
        debrid_service = TorBox(config)
    else:
        raise HTTPException(status_code=500, detail="Invalid service configuration.")

    return debrid_service