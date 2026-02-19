## Execution Units Index
- id: PROC:main
  type: Process
  parent_process: null
  role: FastAPI application runtime hosting HTTP endpoints, background scheduler, and async orchestration.
  entrypoint_symbols:
    - debriddo.main.__main__
    - debriddo.main.lifespan
    - debriddo.main.get_results
    - debriddo.main.get_playback
  defining_files:
    - src/debriddo/main.py
- id: THR:PROC:main#executor-worker
  type: Thread
  parent_process: PROC:main
  role: ThreadPoolExecutor worker executing async coroutines through per-thread event loops when MULTI_THREAD is enabled.
  entrypoint_symbols:
    - debriddo.utils.multi_thread.run_coroutine_in_thread
  defining_files:
    - src/debriddo/utils/multi_thread.py
    - src/debriddo/search/search_service.py
    - src/debriddo/torrent/torrent_service.py
- id: THR:PROC:main#stream-builder
  type: Thread
  parent_process: PROC:main
  role: Per-result stream rendering thread converting TorrentItem objects into Stremio stream dictionaries.
  entrypoint_symbols:
    - debriddo.utils.stremio_parser.parse_to_debrid_stream
  defining_files:
    - src/debriddo/utils/stremio_parser.py
- id: PROC:release-create-release
  type: Process
  parent_process: null
  role: GitHub Actions release job process executing release publication and container image push pipeline.
  entrypoint_symbols:
    - .github/workflows/release.yml::jobs.create-release
  defining_files:
    - .github/workflows/release.yml

## Execution Units

### PROC:main
- Entrypoint(s):
  - `debriddo.main.__main__` [`src/debriddo/main.py:693-694`]
  - `debriddo.main.lifespan(app)` [`src/debriddo/main.py:172-195`]
  - `debriddo.main.get_results(config_url, stream_type, stream_id, request)` [`src/debriddo/main.py:468-574`]
  - `debriddo.main.get_playback(config_url, query_string, request)` [`src/debriddo/main.py:593-623`]
- Lifecycle/trigger:
  - Starts when module runs and calls `uvicorn.run("debriddo.main:app", ...)`.
  - Handles HTTP requests via FastAPI route decorators.
  - Starts scheduler at lifespan startup (`scheduler.start()`), shuts down at lifespan termination (`scheduler.shutdown()`).
- Internal Call-Trace Tree:
  - `__main__(...)`: boot ASGI server [`src/debriddo/main.py:693-694`]
    - External boundary: uvicorn process/server runtime.
  - `lifespan(app)`: startup/shutdown orchestration [`src/debriddo/main.py:172-195`]
    - `update_app()`: periodic self-update coroutine target [`src/debriddo/main.py:629-687`]
  - `get_results(config_url, stream_type, stream_id, request)`: stream aggregation pipeline [`src/debriddo/main.py:468-574`]
    - `parse_config(encoded_config)`: decode addon configuration [`src/debriddo/utils/parse_config.py:14-26`]
      - `decode_lzstring(data, tag)`: decode + JSON deserialize [`src/debriddo/utils/string_encoding.py:38-62`]
    - `TMDB.get_metadata(id, type)`: metadata fetch path when TMDB selected [`src/debriddo/metdata/tmdb.py:24-74`]
    - `Cinemeta.get_metadata(id, type)`: metadata fetch path when Cinemeta selected [`src/debriddo/metdata/cinemeta.py:23-62`]
    - `get_debrid_service(config)`: instantiate provider adapter [`src/debriddo/debrid/get_debrid_service.py:19-39`]
    - `search_cache(config, media)`: query cache database [`src/debriddo/utils/cache.py:61-160`]
    - `SearchResult.from_cached_item(...)`: hydrate cached search results [`src/debriddo/search/search_result.py`]
    - `filter_items(items, media, config)`: filtering pipeline [`src/debriddo/utils/filter_results.py:405-455`]
      - `filter_out_non_matching(items, season, episode)` [`src/debriddo/utils/filter_results.py:314-348`]
      - `remove_non_matching_title(items, titles, media)` [`src/debriddo/utils/filter_results.py:351-402`]
    - `SearchService.search(media)`: async indexer fan-out and post-processing [`src/debriddo/search/search_service.py:86-147`]
      - `__get_indexers()` [`src/debriddo/search/search_service.py:462-519`]
        - `__get_indexer_from_engines(engines)` [`src/debriddo/search/search_service.py:478-519`]
          - `__get_engine(engine_name)` [`src/debriddo/search/search_service.py:149-174`]
      - `__search_movie_indexer(movie, indexer)` [`src/debriddo/search/search_service.py:299-365`]
        - `__search_torrents(media, indexer, search_string, category)` [`src/debriddo/search/search_service.py:251-268`]
          - `__get_torrents_from_list_of_dicts(media, indexer, list_of_dicts)` [`src/debriddo/search/search_service.py:522-553`]
      - `__search_series_indexer(series, indexer)` [`src/debriddo/search/search_service.py:368-459`]
        - `__search_torrents(media, indexer, search_string, category)` [`src/debriddo/search/search_service.py:251-268`]
          - `__get_torrents_from_list_of_dicts(media, indexer, list_of_dicts)` [`src/debriddo/search/search_service.py:522-553`]
      - `__post_process_result(indexers, result, media)` [`src/debriddo/search/search_service.py:585-617`]
    - `TorrentService.convert_and_process(results)`: convert search results into torrent items [`src/debriddo/torrent/torrent_service.py:82-97`]
      - `__process_web_url_or_process_magnet(result)` [`src/debriddo/torrent/torrent_service.py:65-80`]
        - `__process_web_url(result)` [`src/debriddo/torrent/torrent_service.py:99-127`]
          - `__process_torrent(result, torrent_file)` [`src/debriddo/torrent/torrent_service.py:129-164`]
        - `__process_magnet(result)` [`src/debriddo/torrent/torrent_service.py:165-178`]
    - `TorrentSmartContainer.__init__(torrent_items, media)` [`src/debriddo/torrent/torrent_smart_container.py:31-44`]
      - `__build_items_dict_by_infohash(items)` [`src/debriddo/torrent/torrent_smart_container.py:290-307`]
    - `TorrentSmartContainer.get_hashes()` [`src/debriddo/torrent/torrent_smart_container.py:45-54`]
    - `TorrentSmartContainer.update_availability(debrid_response, debrid_type, media)` [`src/debriddo/torrent/torrent_smart_container.py:129-150`]
      - `__update_availability_realdebrid(response, media)` [`src/debriddo/torrent/torrent_smart_container.py:151-197`]
      - `__update_availability_alldebrid(response, media)` [`src/debriddo/torrent/torrent_smart_container.py:198-223`]
      - `__update_availability_torbox(response, media)` [`src/debriddo/torrent/torrent_smart_container.py:224-251`]
      - `__update_availability_premiumize(response)` [`src/debriddo/torrent/torrent_smart_container.py:252-269`]
      - `__update_file_details(torrent_item, files)` [`src/debriddo/torrent/torrent_smart_container.py:271-289`]
      - `__explore_folders(folder, files, file_index, type, season, episode)` [`src/debriddo/torrent/torrent_smart_container.py:310-369`]
    - `TorrentSmartContainer.cache_container_items()` [`src/debriddo/torrent/torrent_smart_container.py:104-116`]
      - `__save_to_cache()` [`src/debriddo/torrent/torrent_smart_container.py:118-128`]
        - `cache_results(torrents, media)` [`src/debriddo/utils/cache.py:163-329`]
    - `TorrentSmartContainer.get_best_matching()` [`src/debriddo/torrent/torrent_smart_container.py:79-103`]
    - `sort_items(items, config)` [`src/debriddo/utils/filter_results.py:458-470`]
      - `items_sort(items, config)` [`src/debriddo/utils/filter_results.py:237-295`]
    - `parse_to_stremio_streams(torrent_items, config, config_url, node_url, media)` [`src/debriddo/utils/stremio_parser.py:202-239`]
      - `parse_to_debrid_stream(torrent_item, config_url, node_url, playtorrent, results, media)` [`src/debriddo/utils/stremio_parser.py:84-200`]
        - `encode_query(query)` [`src/debriddo/utils/parse_config.py:45-57`]
          - `encode_lzstring(json_value, tag)` [`src/debriddo/utils/string_encoding.py:17-35`]
  - `get_playback(config_url, query_string, request)`: playback redirect pipeline [`src/debriddo/main.py:593-623`]
    - `parse_config(encoded_config)` [`src/debriddo/utils/parse_config.py:14-26`]
      - `decode_lzstring(data, tag)` [`src/debriddo/utils/string_encoding.py:38-62`]
    - `parse_query(encoded_query)` [`src/debriddo/utils/parse_config.py:30-42`]
      - `decode_lzstring(data, tag)` [`src/debriddo/utils/string_encoding.py:38-62`]
    - `get_debrid_service(config)` [`src/debriddo/debrid/get_debrid_service.py:19-39`]
    - External boundary: provider `get_stream_link(...)` methods and HTTP APIs.
- External Boundaries:
  - HTTP ingress/egress via FastAPI/Uvicorn.
  - Outbound HTTP to TMDB/Cinemeta/provider APIs/search engines via async HTTP client.
  - SQLite I/O (`sqlite3.connect`, SELECT/INSERT/DELETE) in cache module.
  - Filesystem I/O for web assets (`FileResponse`) and update flow (`update.zip`, `update/`).

### THR:PROC:main#executor-worker
- Entrypoint(s):
  - `run_coroutine_in_thread(coro)` [`src/debriddo/utils/multi_thread.py:17-30`]
- Lifecycle/trigger:
  - Started by `loop.run_in_executor(None, run_coroutine_in_thread, <coroutine>)` from search and torrent services.
  - Executes one coroutine per submitted work item and terminates when task completes.
- Internal Call-Trace Tree:
  - `run_coroutine_in_thread(coro)`: create isolated event loop and run coroutine [`src/debriddo/utils/multi_thread.py:17-30`]
    - `SearchService.__search_movie_indexer(...)` [`src/debriddo/search/search_service.py:299-365`]
      - `__search_torrents(...)` [`src/debriddo/search/search_service.py:251-268`]
    - `SearchService.__search_series_indexer(...)` [`src/debriddo/search/search_service.py:368-459`]
      - `__search_torrents(...)` [`src/debriddo/search/search_service.py:251-268`]
    - `SearchService.__post_process_result(...)` [`src/debriddo/search/search_service.py:585-617`]
    - `TorrentService.__process_web_url_or_process_magnet(...)` [`src/debriddo/torrent/torrent_service.py:65-80`]
      - `__process_web_url(...)` [`src/debriddo/torrent/torrent_service.py:99-127`]
      - `__process_magnet(...)` [`src/debriddo/torrent/torrent_service.py:165-178`]
- External Boundaries:
  - Thread scheduling via `concurrent.futures.ThreadPoolExecutor`.
  - Outbound network/file parsing performed by delegated coroutine bodies.

### THR:PROC:main#stream-builder
- Entrypoint(s):
  - `parse_to_debrid_stream(...)` [`src/debriddo/utils/stremio_parser.py:84-200`]
- Lifecycle/trigger:
  - Spawned as daemon thread per torrent item inside `parse_to_stremio_streams(...)`.
  - Joined by parent thread after queue population.
- Internal Call-Trace Tree:
  - `parse_to_stremio_streams(torrent_items, config, config_url, node_url, media)`: spawn/join worker threads [`src/debriddo/utils/stremio_parser.py:202-239`]
    - `parse_to_debrid_stream(torrent_item, config_url, node_url, playtorrent, results, media)`: render one stream entry [`src/debriddo/utils/stremio_parser.py:84-200`]
      - `encode_query(query)` [`src/debriddo/utils/parse_config.py:45-57`]
        - `encode_lzstring(json_value, tag)` [`src/debriddo/utils/string_encoding.py:17-35`]
      - `get_emoji(language)` [`src/debriddo/utils/stremio_parser.py:23-46`]
- External Boundaries:
  - Inter-thread queue operations via `queue.Queue.put/get`.

### PROC:release-create-release
- Entrypoint(s):
  - `.github/workflows/release.yml::jobs.create-release` [`.github/workflows/release.yml:12-103`]
- Lifecycle/trigger:
  - Triggered on `push.tags: v*` and executed by GitHub Actions runner.
  - Runs sequential step pipeline and exits after final step.
- Internal Call-Trace Tree:
  - No internal functions detected under `.github/workflows/`.
- External Boundaries:
  - GitHub API release operations (`softprops/action-gh-release`).
  - Docker registry login/push to GHCR.
  - Artifact download/upload over network.

## Communication Edges
- id: EDGE:PROC:main->THR:PROC:main#executor-worker
  source: PROC:main
  destination: THR:PROC:main#executor-worker
  mechanism: ThreadPoolExecutor task submission (`loop.run_in_executor`)
  endpoint_channel: in-process executor work queue
  payload_data_shape: coroutine objects (`__search_movie_indexer(...)`, `__search_series_indexer(...)`, `__post_process_result(...)`, `__process_web_url_or_process_magnet(...)`)
  evidence:
    - src/debriddo/search/search_service.py:102-103
    - src/debriddo/search/search_service.py:113-114
    - src/debriddo/search/search_service.py:132-133
    - src/debriddo/torrent/torrent_service.py:90-91
- id: EDGE:PROC:main->THR:PROC:main#stream-builder
  source: PROC:main
  destination: THR:PROC:main#stream-builder
  mechanism: `threading.Thread` start/join
  endpoint_channel: thread invocation target `parse_to_debrid_stream`
  payload_data_shape: `(TorrentItem, config_url:str, node_url:str, playtorrent:bool, results:queue.Queue, media:Media)`
  evidence:
    - src/debriddo/utils/stremio_parser.py:219-223
    - src/debriddo/utils/stremio_parser.py:225-227
- id: EDGE:THR:PROC:main#stream-builder->PROC:main
  source: THR:PROC:main#stream-builder
  destination: PROC:main
  mechanism: thread-safe queue handoff
  endpoint_channel: `queue.Queue` instance `thread_results_queue`
  payload_data_shape: stream item dict (`name`, `description`, `url|infoHash`, `behaviorHints`)
  evidence:
    - src/debriddo/utils/stremio_parser.py:161-170
    - src/debriddo/utils/stremio_parser.py:188-199
    - src/debriddo/utils/stremio_parser.py:228-229
