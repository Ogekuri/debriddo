import asyncio
from constants import RUN_IN_MULTI_THREAD

MULTI_THREAD = RUN_IN_MULTI_THREAD

# Funzione per eseguire una coroutine in un nuovo event loop sul thread del pool
def run_coroutine_in_thread(coro):
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    try:
        return new_loop.run_until_complete(coro)
    finally:
        new_loop.close()
