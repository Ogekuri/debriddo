"""
@file src/debriddo/utils/multi_thread.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.37
# AUTHORS: Ogekuri

import asyncio
from debriddo.constants import RUN_IN_MULTI_THREAD

#: @brief Exported constant `MULTI_THREAD` used by runtime workflows.
MULTI_THREAD = RUN_IN_MULTI_THREAD

# Funzione per eseguire una coroutine in un nuovo event loop sul thread del pool
def run_coroutine_in_thread(coro):
    """
    @brief Execute `run_coroutine_in_thread` operational logic.
    @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
    @param coro Runtime input parameter consumed by `run_coroutine_in_thread`.
    @return Computed result payload; `None` when side-effect-only execution path is selected.
    @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
    """
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    try:
        return new_loop.run_until_complete(coro)
    finally:
        new_loop.close()
