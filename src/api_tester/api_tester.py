#!/usr/bin/env python3
"""
CLI autonoma per testare le API HTTP esposte da Debriddo.

La configurazione può arrivare da:
- parametro CLI `--config-url`
- variabile d'ambiente (default: `DEBRIDDO_CONFIG_URL`)

Il parametro CLI ha priorità sulla variabile d'ambiente.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote, urlparse

try:
    import requests
except ImportError as import_error:
    print(f"Errore: modulo 'requests' non disponibile ({import_error}).", file=sys.stderr)
    sys.exit(2)


DEFAULT_CONFIG_ENV = "DEBRIDDO_CONFIG_URL"
DEFAULT_TIMEOUT = 30.0


class CliError(Exception):
    pass


@dataclass
class TargetUrls:
    base_url: str
    config_segment: str
    config_url: str


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


def normalize_config_url(raw_value: str) -> TargetUrls:
    value = raw_value.strip()
    if not value:
        raise CliError("config URL vuota.")

    parsed = urlparse(value)
    if not parsed.scheme or not parsed.netloc:
        raise CliError(f"URL non valido: '{value}'.")

    path_segments = [segment for segment in parsed.path.split("/") if segment]
    if not path_segments:
        raise CliError("Path URL non valido: manca il segmento C_<config>.")

    if path_segments[-1] in {"manifest.json", "configure"}:
        path_segments = path_segments[:-1]

    config_index = -1
    for index, segment in enumerate(path_segments):
        if segment.startswith("C_"):
            config_index = index
            break
    if config_index < 0:
        raise CliError("Impossibile trovare un segmento 'C_' nell'URL di configurazione.")

    config_segment = path_segments[config_index]
    prefix_segments = path_segments[:config_index]
    prefix_path = "/" + "/".join(prefix_segments) if prefix_segments else ""
    base_url = f"{parsed.scheme}://{parsed.netloc}{prefix_path}"
    config_url = f"{base_url}/{config_segment}"

    return TargetUrls(
        base_url=base_url.rstrip("/"),
        config_segment=config_segment,
        config_url=config_url.rstrip("/"),
    )


def get_target_from_args(args: argparse.Namespace) -> TargetUrls:
    config_url = args.config_url or os.getenv(args.config_url_env, "")
    if not config_url:
        raise CliError(
            f"Configurazione mancante: usa --config-url o imposta {args.config_url_env}."
        )
    return normalize_config_url(config_url)


def request_url(
    session: requests.Session,
    method: str,
    url: str,
    timeout: float,
    verify_ssl: bool,
    allow_redirects: bool = False,
) -> requests.Response:
    response = session.request(
        method=method,
        url=url,
        timeout=timeout,
        verify=verify_ssl,
        allow_redirects=allow_redirects,
    )
    return response


def make_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"


def parse_json_body(response: requests.Response) -> Optional[Any]:
    try:
        return response.json()
    except ValueError:
        return None


def print_response_summary(
    response: requests.Response,
    print_body: bool = False,
    max_body_chars: int = 3000,
) -> None:
    print(f"HTTP {response.status_code}")
    location = response.headers.get("Location")
    content_type = response.headers.get("Content-Type")
    if location:
        print(f"Location: {location}")
    if content_type:
        print(f"Content-Type: {content_type}")

    if not print_body:
        return

    parsed_json = parse_json_body(response)
    if parsed_json is not None:
        body_text = json.dumps(parsed_json, indent=2, ensure_ascii=False)
    else:
        body_text = response.text

    if len(body_text) > max_body_chars:
        body_text = body_text[:max_body_chars] + "\n... [troncato]"
    print(body_text)


def call_simple_endpoint(
    session: requests.Session,
    args: argparse.Namespace,
    target: TargetUrls,
    path: str,
    method: str = "GET",
    allow_redirects: bool = False,
) -> int:
    url = make_url(target.base_url, path)
    response = request_url(
        session=session,
        method=method,
        url=url,
        timeout=args.timeout,
        verify_ssl=not args.insecure,
        allow_redirects=allow_redirects,
    )
    print(f"{method} {url}")
    print_response_summary(response, print_body=args.print_body)
    return 0 if response.ok else 1


def build_stream_path(
    target: TargetUrls,
    stream_type: str,
    stream_id: str,
    append_json_suffix: bool,
) -> str:
    encoded_stream_id = quote(stream_id, safe=":.")
    if append_json_suffix and not encoded_stream_id.endswith(".json"):
        encoded_stream_id = encoded_stream_id + ".json"
    return f"/{target.config_segment}/stream/{stream_type}/{encoded_stream_id}"


def cmd_target(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    print(f"base_url     : {target.base_url}")
    print(f"config_url   : {target.config_url}")
    print(f"config_token : {target.config_segment}")
    return 0


def cmd_root(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    with requests.Session() as session:
        return call_simple_endpoint(
            session=session,
            args=args,
            target=target,
            path="/",
            method="GET",
            allow_redirects=False,
        )


def cmd_configure(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    path = f"/{target.config_segment}/configure" if args.with_config else "/configure"
    with requests.Session() as session:
        return call_simple_endpoint(session, args, target, path, method="GET")


def cmd_manifest(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    path = f"/{target.config_segment}/manifest.json" if args.with_config else "/manifest.json"
    with requests.Session() as session:
        return call_simple_endpoint(session, args, target, path, method="GET")


def cmd_site_webmanifest(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    with requests.Session() as session:
        return call_simple_endpoint(session, args, target, "/site.webmanifest", method="GET")


def cmd_asset(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)

    if args.asset_type == "favicon":
        asset_path = "/favicon.ico"
    elif args.asset_type == "configjs":
        asset_path = "/config.js"
    elif args.asset_type == "lzstring":
        asset_path = "/lz-string.min.js"
    elif args.asset_type == "styles":
        asset_path = "/styles.css"
    elif args.asset_type == "image":
        image_path = args.image_path.lstrip("/")
        asset_path = f"/images/{image_path}"
    else:
        raise CliError(f"Tipo asset non supportato: {args.asset_type}")

    if args.with_config and args.asset_type != "favicon":
        asset_path = f"/{target.config_segment}{asset_path}"

    with requests.Session() as session:
        return call_simple_endpoint(session, args, target, asset_path, method="GET")


def request_stream(
    session: requests.Session,
    args: argparse.Namespace,
    target: TargetUrls,
    stream_type: str,
    stream_id: str,
    append_json_suffix: bool,
) -> requests.Response:
    stream_path = build_stream_path(
        target=target,
        stream_type=stream_type,
        stream_id=stream_id,
        append_json_suffix=append_json_suffix,
    )
    stream_url = make_url(target.base_url, stream_path)
    return request_url(
        session=session,
        method="GET",
        url=stream_url,
        timeout=args.timeout,
        verify_ssl=not args.insecure,
        allow_redirects=False,
    )


def cmd_stream(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    with requests.Session() as session:
        response = request_stream(
            session=session,
            args=args,
            target=target,
            stream_type=args.stream_type,
            stream_id=args.stream_id,
            append_json_suffix=args.append_json,
        )
        stream_path = build_stream_path(target, args.stream_type, args.stream_id, args.append_json)
        stream_url = make_url(target.base_url, stream_path)
        print(f"GET {stream_url}")
        print_response_summary(response, print_body=args.print_body)

        parsed = parse_json_body(response)
        if parsed is not None and isinstance(parsed, dict):
            streams = parsed.get("streams")
            if isinstance(streams, list):
                print(f"streams: {len(streams)}")
                if args.preview_streams > 0:
                    for index, item in enumerate(streams[: args.preview_streams]):
                        keys = ",".join(sorted(item.keys()))
                        print(f"  - #{index} keys={keys}")
        return 0 if response.ok else 1


def extract_playback_path_from_streams(streams_payload: Dict[str, Any]) -> Optional[str]:
    streams = streams_payload.get("streams")
    if not isinstance(streams, list):
        return None

    for item in streams:
        if not isinstance(item, dict):
            continue
        stream_url = item.get("url")
        if not isinstance(stream_url, str):
            continue
        parsed = urlparse(stream_url)
        if "/playback/" in parsed.path:
            return parsed.path
    return None


def request_playback(
    session: requests.Session,
    args: argparse.Namespace,
    target: TargetUrls,
    method: str,
    playback_path: str,
) -> requests.Response:
    playback_url = make_url(target.base_url, playback_path)
    return request_url(
        session=session,
        method=method,
        url=playback_url,
        timeout=args.timeout,
        verify_ssl=not args.insecure,
        allow_redirects=False,
    )


def cmd_playback(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)

    with requests.Session() as session:
        playback_path: Optional[str] = None

        if args.query:
            playback_path = f"/playback/{target.config_segment}/{args.query}"
        else:
            if not args.stream_type or not args.stream_id:
                raise CliError("Per usare playback senza --query devi passare --stream-type e --stream-id.")
            stream_response = request_stream(
                session=session,
                args=args,
                target=target,
                stream_type=args.stream_type,
                stream_id=args.stream_id,
                append_json_suffix=args.append_json,
            )
            stream_data = parse_json_body(stream_response) or {}
            playback_path = extract_playback_path_from_streams(stream_data)
            if not playback_path:
                raise CliError(
                    "Nessun URL playback trovato nella risposta stream. "
                    "Verifica che la configurazione Debrid sia abilitata."
                )

        method = "HEAD" if args.head else "GET"
        response = request_playback(
            session=session,
            args=args,
            target=target,
            method=method,
            playback_path=playback_path,
        )
        playback_url = make_url(target.base_url, playback_path)
        print(f"{method} {playback_url}")
        print_response_summary(response, print_body=args.print_body)
        return 0 if response.status_code < 400 else 1


def validate_manifest_payload(payload: Dict[str, Any]) -> Tuple[bool, str]:
    resources = payload.get("resources")
    if not isinstance(resources, list):
        return False, "manifest senza array 'resources'"
    for item in resources:
        if not isinstance(item, dict):
            continue
        if item.get("name") != "stream":
            continue
        stream_types = item.get("types")
        if isinstance(stream_types, list) and "movie" in stream_types and "series" in stream_types:
            return True, "resource stream con movie+series trovata"
    return False, "resource stream con movie+series non trovata"


def add_check(results: List[CheckResult], name: str, ok: bool, detail: str) -> None:
    results.append(CheckResult(name=name, ok=ok, detail=detail))


def run_smoke(args: argparse.Namespace, target: TargetUrls) -> List[CheckResult]:
    results: List[CheckResult] = []
    verify_ssl = not args.insecure

    with requests.Session() as session:
        root_url = make_url(target.base_url, "/")
        root_response = request_url(
            session=session,
            method="GET",
            url=root_url,
            timeout=args.timeout,
            verify_ssl=verify_ssl,
            allow_redirects=False,
        )
        root_ok = 300 <= root_response.status_code < 400 and root_response.headers.get("Location") == "/configure"
        add_check(
            results,
            "GET /",
            root_ok,
            f"status={root_response.status_code} location={root_response.headers.get('Location')}",
        )

        configure_response = request_url(
            session=session,
            method="GET",
            url=make_url(target.base_url, "/configure"),
            timeout=args.timeout,
            verify_ssl=verify_ssl,
            allow_redirects=False,
        )
        configure_html = configure_response.text if configure_response.ok else ""
        configure_ok = configure_response.ok and "$APP_NAME" not in configure_html
        add_check(results, "GET /configure", configure_ok, f"status={configure_response.status_code}")

        prefixed_configure_response = request_url(
            session=session,
            method="GET",
            url=make_url(target.base_url, f"/{target.config_segment}/configure"),
            timeout=args.timeout,
            verify_ssl=verify_ssl,
            allow_redirects=False,
        )
        add_check(
            results,
            "GET /{config}/configure",
            prefixed_configure_response.ok,
            f"status={prefixed_configure_response.status_code}",
        )

        asset_paths = [
            "/favicon.ico",
            "/config.js",
            "/lz-string.min.js",
            "/styles.css",
            f"/images/{args.image_path.lstrip('/')}",
            f"/{target.config_segment}/config.js",
            f"/{target.config_segment}/lz-string.min.js",
            f"/{target.config_segment}/styles.css",
            f"/{target.config_segment}/images/{args.image_path.lstrip('/')}",
        ]
        for asset_path in asset_paths:
            asset_response = request_url(
                session=session,
                method="GET",
                url=make_url(target.base_url, asset_path),
                timeout=args.timeout,
                verify_ssl=verify_ssl,
                allow_redirects=False,
            )
            add_check(
                results,
                f"GET {asset_path}",
                asset_response.ok,
                f"status={asset_response.status_code}",
            )

        site_manifest_response = request_url(
            session=session,
            method="GET",
            url=make_url(target.base_url, "/site.webmanifest"),
            timeout=args.timeout,
            verify_ssl=verify_ssl,
            allow_redirects=False,
        )
        site_manifest_ok = site_manifest_response.ok and "application/manifest+json" in site_manifest_response.headers.get(
            "Content-Type", ""
        )
        add_check(
            results,
            "GET /site.webmanifest",
            site_manifest_ok,
            f"status={site_manifest_response.status_code} content-type={site_manifest_response.headers.get('Content-Type')}",
        )

        manifest_paths = ["/manifest.json", f"/{target.config_segment}/manifest.json"]
        for manifest_path in manifest_paths:
            manifest_response = request_url(
                session=session,
                method="GET",
                url=make_url(target.base_url, manifest_path),
                timeout=args.timeout,
                verify_ssl=verify_ssl,
                allow_redirects=False,
            )
            manifest_payload = parse_json_body(manifest_response)
            if manifest_response.ok and isinstance(manifest_payload, dict):
                manifest_valid, manifest_detail = validate_manifest_payload(manifest_payload)
            else:
                manifest_valid, manifest_detail = False, "payload manifest non valido"
            add_check(
                results,
                f"GET {manifest_path}",
                manifest_response.ok and manifest_valid,
                f"status={manifest_response.status_code} {manifest_detail}",
            )

        movie_stream_response = request_stream(
            session=session,
            args=args,
            target=target,
            stream_type="movie",
            stream_id=args.movie_id,
            append_json_suffix=True,
        )
        movie_stream_payload = parse_json_body(movie_stream_response)
        movie_stream_ok = movie_stream_response.ok and isinstance(movie_stream_payload, dict)
        if movie_stream_ok:
            streams = movie_stream_payload.get("streams")
            movie_stream_ok = isinstance(streams, list)
            stream_count = len(streams) if isinstance(streams, list) else 0
        else:
            stream_count = 0
        add_check(
            results,
            "GET /{config}/stream/movie/{id}.json",
            movie_stream_ok,
            f"status={movie_stream_response.status_code} streams={stream_count}",
        )

        if args.series_id:
            series_stream_response = request_stream(
                session=session,
                args=args,
                target=target,
                stream_type="series",
                stream_id=args.series_id,
                append_json_suffix=True,
            )
            series_stream_payload = parse_json_body(series_stream_response)
            series_stream_ok = series_stream_response.ok and isinstance(series_stream_payload, dict)
            if series_stream_ok:
                streams = series_stream_payload.get("streams")
                series_stream_ok = isinstance(streams, list)
                series_stream_count = len(streams) if isinstance(streams, list) else 0
            else:
                series_stream_count = 0
            add_check(
                results,
                "GET /{config}/stream/series/{id}.json",
                series_stream_ok,
                f"status={series_stream_response.status_code} streams={series_stream_count}",
            )

        playback_path = None
        if isinstance(movie_stream_payload, dict):
            playback_path = extract_playback_path_from_streams(movie_stream_payload)

        if playback_path:
            playback_get_response = request_playback(
                session=session,
                args=args,
                target=target,
                method="GET",
                playback_path=playback_path,
            )
            playback_ok = (
                playback_get_response.status_code == 301
                and bool(playback_get_response.headers.get("Location"))
            )
            add_check(
                results,
                "GET /playback/{config}/{query}",
                playback_ok,
                f"status={playback_get_response.status_code} location={playback_get_response.headers.get('Location')}",
            )

            head_response = request_playback(
                session=session,
                args=args,
                target=target,
                method="HEAD",
                playback_path=playback_path,
            )
            add_check(
                results,
                "HEAD /playback/{config}/{query}",
                head_response.status_code == 422,
                f"status={head_response.status_code} (422 atteso per limite noto)",
            )
        else:
            add_check(
                results,
                "GET /playback/{config}/{query}",
                False,
                "nessuna URL playback disponibile nei risultati stream",
            )
            add_check(
                results,
                "HEAD /playback/{config}/{query}",
                False,
                "non eseguito: manca una URL playback valida",
            )

    return results


def cmd_smoke(args: argparse.Namespace) -> int:
    target = get_target_from_args(args)
    results = run_smoke(args, target)

    failed = 0
    for result in results:
        status_text = "PASS" if result.ok else "FAIL"
        if not result.ok:
            failed += 1
        print(f"[{status_text}] {result.name} -> {result.detail}")

    print(f"\nTotale: {len(results)} test, {failed} falliti.")
    return 0 if failed == 0 else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="debriddo_api_tester.py",
        description="Tester CLI autonomo per tutte le API HTTP esposte da Debriddo.",
    )
    parser.add_argument(
        "--config-url",
        help="URL configurazione Debriddo (es: https://host/C_xxx). Prevale su env var.",
    )
    parser.add_argument(
        "--config-url-env",
        default=DEFAULT_CONFIG_ENV,
        help=f"Nome env var da cui leggere la config URL (default: {DEFAULT_CONFIG_ENV}).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help=f"Timeout richieste HTTP in secondi (default: {DEFAULT_TIMEOUT}).",
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Disabilita verifica certificato TLS (solo per test locali).",
    )
    parser.add_argument(
        "--print-body",
        action="store_true",
        help="Stampa il body completo/troncato della risposta HTTP.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_target = subparsers.add_parser("target", help="Mostra URL base e token config risolti.")
    parser_target.set_defaults(func=cmd_target)

    parser_root = subparsers.add_parser("root", help="Test endpoint GET / (redirect).")
    parser_root.set_defaults(func=cmd_root)

    parser_configure = subparsers.add_parser("configure", help="Test endpoint configure.")
    parser_configure.add_argument(
        "--with-config",
        action="store_true",
        help="Usa GET /{config}/configure invece di GET /configure.",
    )
    parser_configure.set_defaults(func=cmd_configure)

    parser_manifest = subparsers.add_parser("manifest", help="Test endpoint manifest.")
    parser_manifest.add_argument(
        "--with-config",
        action="store_true",
        help="Usa GET /{config}/manifest.json invece di GET /manifest.json.",
    )
    parser_manifest.set_defaults(func=cmd_manifest)

    parser_site_manifest = subparsers.add_parser("site-webmanifest", help="Test GET /site.webmanifest.")
    parser_site_manifest.set_defaults(func=cmd_site_webmanifest)

    parser_asset = subparsers.add_parser("asset", help="Test endpoint asset statici.")
    parser_asset.add_argument(
        "--asset-type",
        choices=["favicon", "configjs", "lzstring", "styles", "image"],
        required=True,
        help="Tipo asset da testare.",
    )
    parser_asset.add_argument(
        "--image-path",
        default="logo.png",
        help="Nome file immagine quando --asset-type=image (default: logo.png).",
    )
    parser_asset.add_argument(
        "--with-config",
        action="store_true",
        help="Usa rotta con prefisso /{config}/ quando applicabile.",
    )
    parser_asset.set_defaults(func=cmd_asset)

    parser_stream = subparsers.add_parser("stream", help="Test endpoint stream (ricerca film/serie).")
    parser_stream.add_argument("--stream-type", choices=["movie", "series"], required=True, help="Tipo stream.")
    parser_stream.add_argument("--stream-id", required=True, help="ID media (es: tt0133093 o tt0944947:1:1).")
    parser_stream.add_argument(
        "--append-json",
        action="store_true",
        help="Aggiunge suffisso .json allo stream_id nella chiamata.",
    )
    parser_stream.add_argument(
        "--preview-streams",
        type=int,
        default=3,
        help="Numero massimo stream da riassumere in output (default: 3).",
    )
    parser_stream.set_defaults(func=cmd_stream)

    parser_playback = subparsers.add_parser("playback", help="Test endpoint playback.")
    parser_playback.add_argument(
        "--query",
        help="Query Q_<...> già codificata. Se omessa, prova a ricavarla da un test stream.",
    )
    parser_playback.add_argument(
        "--stream-type",
        choices=["movie", "series"],
        help="Necessario se --query non è valorizzata.",
    )
    parser_playback.add_argument(
        "--stream-id",
        help="Necessario se --query non è valorizzata.",
    )
    parser_playback.add_argument(
        "--append-json",
        action="store_true",
        help="Aggiunge suffisso .json allo stream_id durante la ricerca stream.",
    )
    parser_playback.add_argument(
        "--head",
        action="store_true",
        help="Esegue HEAD invece di GET su /playback.",
    )
    parser_playback.set_defaults(func=cmd_playback)

    parser_smoke = subparsers.add_parser(
        "smoke",
        help="Esegue una suite smoke su tutte le API esposte, inclusi stream e playback.",
    )
    parser_smoke.add_argument(
        "--movie-id",
        default="tt0133093",
        help="ID film per test stream movie (default: tt0133093).",
    )
    parser_smoke.add_argument(
        "--series-id",
        default="tt0944947:1:1",
        help="ID serie per test stream series (default: tt0944947:1:1).",
    )
    parser_smoke.add_argument(
        "--image-path",
        default="logo.png",
        help="Immagine da usare nel test endpoint /images (default: logo.png).",
    )
    parser_smoke.set_defaults(func=cmd_smoke)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        return int(args.func(args))
    except requests.RequestException as request_error:
        print(f"Errore HTTP: {request_error}", file=sys.stderr)
        return 2
    except CliError as cli_error:
        print(f"Errore: {cli_error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
