# Changelog

## [0.1.2](https://github.com/Ogekuri/debriddo/compare/v0.1.0..v0.1.2) - 2026-02-24
### ⛰️  Features
- update .gitignore file. *(core)*

### 🐛  Bug Fixes
- Fix workflow. *(core)*

## [0.1.0](https://github.com/Ogekuri/debriddo/releases/tag/v0.1.0) - 2026-02-22
### ⛰️  Features
- update github workflow. *(core)*
- update github workflow. *(core)*
- update github workflow. *(core)*
- add seach_movie.sh and seach_series.sh scripts. *(core)*
- update requirements and doc build script [2026-02-13 19:10:00] *(pdoc)*
- add Italian Google-style docstrings to all functions [2026-02-13 19:00:59] *(docs)*
- removed one337x, limetorrents and torrentproject that not work for claudeflare protection. *(core)*
- add ita/no-lang conf. *(core)*
- add Google_Python_Style_Guide.md *(core)*
- add --reload for debug. *(core)*
- add api_tester. *(core)*
- add req/ dir. *(core)*
- add G to project. *(core)*

### 🐛  Bug Fixes
- configure pyright venv resolution [2026-02-20 15:37:37] *(core)*
- Fix static analysis errors and unused imports [2026-02-20 15:26:58] *(core)*
- minor fixes *(core)*
- manual fix. *(core)*
- add --reload. *(core)*
- resolve Pylance type-safety errors in plugins and main [2026-02-13 17:43:10] *(core)*
- resolve Pylance type-safety errors across plugins and main [2026-02-13 17:37:23] *(core)*
- caches scripts. *(core)*
- log each executed query per indexer [2026-02-13 16:54:29] *(search_service)*
- minor fixes. *(core)*
- fix Pylance issues. *(core)*
- guard empty language searches [2026-02-13 10:37:35] *(search)*
- handle missing metadata [2026-02-13 10:03:19] *(stream)*
- minor fixes. *(core)*
- guard event loop and test_plugins script [2026-02-12 19:17:29] *(main)*
- change 533 req. *(core)*
- fix .gitignore file. *(core)*
- re-add .github/ dir. *(core)*
- fix requirements.txt file. *(core)*

### 🚜  Changes
- add script and requirements/workflow updates [2026-02-17 15:24:57] *(doxygen)*
- remove pdoc support and refresh doxygen docs [2026-02-17 15:18:29] *(core)*
- remove doc-comment req and normalize doxygen docs [2026-02-15 19:46:18] *(core)*
- apply Doxygen documentation coverage and update specs [2026-02-15 19:27:42] *(core)*
- increase timeout default and specs [2026-02-13 18:47:57] *(api_tester)*
- align language-driven query rules [2026-02-13 16:28:53] *(search_service)*
- refactor search language loop and fallback rules [2026-02-13 15:45:28] *(search_service)*
- log engine results list and update specs/tests [2026-02-13 14:55:31] *(main)*
- refactor series TV filters with enhanced season matching and title validation [2026-02-13 14:14:52] *(filter_results)*
  - Enhanced REQ-532: added support for numeric season format in complete season matching (Season d ... COMPLETE)
  - Enhanced REQ-533: implemented series-specific title filtering with season-aware patterns (<title>.+Snn, <title>.+Season Snn, <title>.+Season d)
  - Added TST-533: comprehensive unit tests for series filtering (39 tests passing)
  - Updated _match_complete_season() to support both Season Snn and Season d formats with localization
  - Added _match_title_with_season() helper for series title matching with flexible separator handling
  - Updated remove_non_matching_title() to validate season correctness for series
  - Updated requirements.md version 1.0 with improved filtering specifications
  - Updated WORKFLOW.md with new function signatures and line ranges
  - Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
- log series count and update specs [2026-02-13 13:55:53] *(filter_results)*
- document series filter log count [2026-02-13 13:44:52] *(requirements)*
- refactor series season/episode matching logic [2026-02-13 13:31:01] *(filter_results)*
- align filter sort_items line reference [2026-02-13 11:40:38] *(workflow)*
- preserve complete season packs in series filtering [2026-02-13 11:40:38] *(filter_results)*
- update series pack query specs/tests [2026-02-13 11:24:15] *(search_service)*
- update search queries and specs [2026-02-13 11:12:41] *(search_service)*
- skip language filter when unset; update specs [2026-02-13 10:51:29] *(filtering)*
- fix language defaults and engines list [2026-02-13 10:16:52] *(config)*
- add search command and specs [2026-02-13 08:59:24] *(api_tester)*
- update API tester requirements and workflow [2026-02-13 08:46:45] *(api_tester)*
- document isolation and guard imports [2026-02-12 18:38:38] *(api_tester)*
- add thread count unit tests [2026-02-12 11:38:16] *(tests)*
- update thread count requirements and sizing [2026-02-12 11:36:12] *(main)*

### 📚  Documentation
- update README.md *(core)*
- Review README.md. *(core)*
- restore workflow runtime model [2026-02-20 15:45:03] *(core)*
- refresh workflow runtime model [2026-02-20 15:44:42] *(core)*
- regenerate references index [2026-02-19 17:52:27] *(core)*
- regenerate workflow runtime model [2026-02-19 17:47:29] *(core)*
- generate REFERENCES.md from source code [2026-02-15 19:19:26] *(core)*
- regenerate technical call tree [2026-02-15 18:56:56] *(workflow)*
- add comments. *(core)*
- update DEVELOP.md. *(core)*


# History

- \[0.1.0\]: https://github.com/Ogekuri/debriddo/releases/tag/v0.1.0
- \[0.1.2\]: https://github.com/Ogekuri/debriddo/releases/tag/v0.1.2

[0.1.0]: https://github.com/Ogekuri/debriddo/releases/tag/v0.1.0
[0.1.2]: https://github.com/Ogekuri/debriddo/compare/v0.1.0..v0.1.2
