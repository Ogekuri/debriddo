🚧 **DRAFT:** Preliminary Version 📝 - Work in Progress 🏗️ 🚧

⚠️ **IMPORTANT NOTICE**: Created with **[useReq/req](https://github.com/Ogekuri/useReq)** 🤖✨ ⚠️

# Debriddo

**Version: 0.0.39**

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-GPL--3.0-491?style=flat-square" alt="License: GPL-3.0">
  <img src="https://img.shields.io/badge/platform-Linux-6A7EC2?style=flat-square&logo=terminal&logoColor=white" alt="Platforms">
  <img src="https://img.shields.io/badge/docs-live-b31b1b" alt="Docs">
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</p>

<p align="center">
<strong>Debriddo is a Stremio add-on that searches for movies and TV series on online torrent search engines.</strong><br>
It provides a web-based configuration page, builds compressed install URLs for Stremio, aggregates torrent results from multiple engines, applies quality/language/size filtering, uses a local SQLite cache, and can redirect playback through supported Debrid services.
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> |
  <a href="#feature-highlights">Feature Highlights</a> |
  <a href="#acknowledgments">Acknowledgments</a>
<p>

## Feature Highlights
- Stremio-compatible add-on manifest and `stream` endpoints for `movie` and `series`.
- Web configuration UI with shareable compressed config payloads (`C_...`) for install and reconfiguration links.
- Configurable multi-engine torrent search (The Pirate Bay, Torrentz, TorrentGalaxy, TheRARBG, Il Corsaro Nero, Il Corsaro Blu).
- Metadata lookup via TMDB (with API key) or Cinemeta.
- Result filtering and ordering by language, excluded keywords/qualities, max size, per-quality cap, and sort mode.
- Local SQLite cache (`caches_items.db`) to reuse previous searches and reduce repeated engine lookups.
- Optional Debrid playback redirect support for Real-Debrid, AllDebrid, Premiumize, and TorBox.
- Docker-first run flow plus a CLI API tester for endpoint checks and smoke tests.

## Quick Start

### Docker

- Pull the Docker image from GitHub Container Registry
    ```sh
    sudo docker pull "ghcr.io/ogekuri/debriddo:latest"
    ```
- Run the Docker container
    ```sh
    sudo docker run -p "0.0.0.0:8000:8000" --env DOCKER_PORT="8000" --env DOCKER_URL="https://foo.bar:443" --env NUM_WORKERS="auto" --env N_THREADS="auto" "ghcr.io/ogekuri/debriddo:latest"
    ```
- Optionally, you can define the environment with `DOCKER_ENV` (e.g. `test`)
    ```sh
    sudo docker run -p "0.0.0.0:8000:8000" --env DOCKER_PORT="8000" --env DOCKER_URL="https://foo.bar:443" --env DOCKER_ENV="test" "ghcr.io/ogekuri/debriddo:latest"
    ```
  It is accessible through the URL set in `DOCKER_URL` (default: `http://127.0.0.1:8000`); the default port is `8000`.

- Supported parameters in the `docker run` command:
  - `DOCKER_PORT`: listening port of the service inside the container.
  - `DOCKER_URL`: public URL used by the add-on in manifests.
  - `DOCKER_ENV` (optional): environment name (e.g. `test`, `develop`).
  - `NUM_WORKERS` (optional): number of Uvicorn workers (`auto` supported).
  - `N_THREADS` (optional): number of application threads (`auto` supported).

- Stop the application
    ```sh
    Ctrl+C
    ```

### API Tester (CLI)

To test Debriddo HTTP endpoints, you can use:

```sh
./api_tester.sh --help
```

- Supported global options:
  - `--config-url`
  - `--config-url-env`
  - `--timeout`
  - `--insecure`
  - `--print-body`

- Available commands:
  - `target`
  - `root`
  - `configure`
  - `manifest`
  - `site-webmanifest`
  - `asset`
  - `stream`
  - `search`
  - `playback`
  - `smoke`

## Acknowledgments

Special thanks to **Riki**, who excellently replaced ChatGPT entirely for free.

This project is based on **aymene69**'s [Stremio Jackett Addon](https://github.com/aymene69/stremio-jackett), from which it integrates part of the source code.

However, since support for the [Jackett API Server](https://github.com/Jackett/Jackett) has been completely removed in favor of direct searches, this project is not maintained as a fork of the main project, but as an independent project.
Thanks to **aymene69** and the **Jackett** team for their valuable contribution!

Finally, thanks also to the creators of the qTorrentio plugins integrated into this project: [LightDestory](https://github.com/LightDestory), [Scare!](https://Scare.ca/dl/qBittorrent/), Lima66, Diego de las Heras, sa3dany, Alyetama, BurningMop, scadams, BurningMop, nindogo, mauricci.
