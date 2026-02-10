# VERSION: 0.0.34
# AUTHORS: Ogekuri

import gzip
import re
import socket
import tempfile
from urllib.parse import urlparse
import html.entities
import asyncio
import httpx
import socks
import json
from utils.logger import setup_logger

DEFAULT_TIMEOUT = 20.0  # 20 secondi

class AsyncThreadSafeSession:

    logger = setup_logger(__name__)
    
    headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
		"Accept-Language": "en-US,en;q=0.5",
	}
         
    def __init__(self, proxy=None):
        self.cookies = httpx.Cookies()  # Gestione esplicita dei cookie
        self._client = httpx.AsyncClient(http2=True, cookies=self.cookies, follow_redirects=True)   # Associa i cookie al client, abilita i reindirizzamenti
        # self._lock = asyncio.Lock()  # Usa un lock asincrono
        self.default_timeout = httpx.Timeout(DEFAULT_TIMEOUT)  # Timeout predefinito di 20 secondi

        # SOCKS5 Proxy setup (if provided)
        if proxy:
            self._setup_proxy(proxy)

        # per il check dei close
        self.closed = False


    async def close(self):
        """Close the HTTPX client to release resources."""
        await self._client.aclose()
        self.closed = True

    async def __aenter__(self):
        """Inizia il contesto asincrono."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Chiude la sessione quando il contesto termina."""
        await self.close()

    def __del__(self):
        """Verifica se la sessione è stata chiusa."""
        if not self.closed:
            # Logga un avviso, senza tentare di chiudere la sessione
            self.logger.warning("Session not closed. Please call close() explicitly.")

    # per Debrid

    @staticmethod
    def _html_entity_decode(s):
        # First convert alpha entities (such as &eacute;)
        # (Inspired from http://mail.python.org/pipermail/python-list/2007-June/443813.html)
        def entity2char(m):
            entity = m.group(1)
            if entity in html.entities.name2codepoint:
                return chr(html.entities.name2codepoint[entity])
            return " "  # Unknown entity: We replace with a space.
        t = re.sub('&(%s);' % '|'.join(html.entities.name2codepoint), entity2char, s)

        # Then convert numerical entities (such as &#233;)
        t = re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), t)

        # Then convert hexa entities (such as &#x00E9;)
        return re.sub(r'&#x(\w+);', lambda x: chr(int(x.group(1), 16)), t)


    def _setup_proxy(self, proxy):
        match = re.match(r"^(?:(?P<username>[^:]+):(?P<password>[^@]+)@)?(?P<host>[^:]+):(?P<port>\w+)$", proxy)
        if match:
            socks.setdefaultproxy(
                socks.PROXY_TYPE_SOCKS5,
                match.group('host'),
                int(match.group('port')),
                True,
                match.group('username'),
                match.group('password'),
            )
            socket.socket = socks.socksocket
        else:
            raise ValueError("Invalid proxy format. Expected format: user:pass@host:port or host:port")


    # per i Plug-Ins

    async def request(self, method, url, **kwargs):
        """Wrapper for HTTP requests with thread-safe access."""
        # async with self._lock:
        if True:
            # Combina gli header specificati con quelli di default
            headers = kwargs.pop("headers", {})
            headers = {**self.headers, **headers}  # Unisce gli header di default e quelli personalizzati

            # Usa un timeout personalizzato o quello predefinito
            timeout = kwargs.pop("timeout", self.default_timeout)
            try:
                response = await self._client.request(
                    method, url, headers=headers, timeout=timeout, **kwargs
                )
                response.raise_for_status()  # Solleva un'eccezione per errori HTTP 4xx o 5xx
                return response  # Restituisce la risposta finale dopo i reindirizzamenti
            except httpx.HTTPStatusError as e:
                # Logga l'errore e restituisce una risposta informativa
                self.logger.error(f"Errore HTTP durante la richiesta: {e.response.status_code} {e.response.url}")
                return None
            except httpx.RequestError as e:
                # Logga l'errore e genera un'eccezione per errori di connessione o altro
                self.logger.error(f"Errore durante la connessione a {url}: {e}")
                return None


    async def request_get(self, url, **kwargs):
        return await self.request("GET", url, headers=self.headers, **kwargs)


    async def request_post(self, url, **kwargs):
        return await self.request("POST", url, headers=self.headers, **kwargs)

    #
    # versione originale sincrona
    #
    # def retrieve_url(url):
    #     """ Return the content of the url page as a string """
    #     try:
    #         req = urllib.request.Request(url, headers=headers)
    #         response = urllib.request.urlopen(req)
    #     except urllib.error.URLError as errno:
    #         logger.error(" ".join(("Connection error:", str(errno.reason))))
    #         return ""
    #     dat = response.read()
    #     # Check if it is gzipped
    #     if dat[:2] == b'\x1f\x8b':
    #         # Data is gzip encoded, decode it
    #         compressedstream = io.BytesIO(dat)
    #         gzipper = gzip.GzipFile(fileobj=compressedstream)
    #         extracted_data = gzipper.read()
    #         dat = extracted_data
    #     info = response.info()
    #     charset = 'utf-8'
    #     try:
    #         ignore, charset = info['Content-Type'].split('charset=')
    #     except Exception:
    #         pass
    #     dat = dat.decode(charset, 'replace')
    #     dat = htmlentitydecode(dat)
    #     # return dat.encode('utf-8', 'replace')
    #     return dat

    async def retrieve_url(self, url):
        """Retrieve the content of the URL as a decoded string."""
        try:
            response = await self.request_get(url)
            if response is not None:
                data = response.content

                # Handle gzip encoding
                if data[:2] == b'\x1f\x8b':
                    data = gzip.decompress(data)

                # Decode the content
                charset = response.encoding or 'utf-8'
                decoded_data = data.decode(charset, errors='replace')
                return self._html_entity_decode(decoded_data)
        except Exception as e:
            self.logger.error(f"Error retrieving URL {url}: {e}")
        
        return None

    #
    # versione originale sincrona
    #
    # def download_file(url, referer=None):
    #     """ Download file at url and write it to a file, return the path to the file and the url """
    #     file, path = tempfile.mkstemp()
    #     file = os.fdopen(file, "wb")
    #     # Download url
    #     req = urllib.request.Request(url, headers=headers)
    #     if referer is not None:
    #         req.add_header('referer', referer)
    #     response = urllib.request.urlopen(req)
    #     dat = response.read()
    #     # Check if it is gzipped
    #     if dat[:2] == b'\x1f\x8b':
    #         # Data is gzip encoded, decode it
    #         compressedstream = io.BytesIO(dat)
    #         gzipper = gzip.GzipFile(fileobj=compressedstream)
    #         extracted_data = gzipper.read()
    #         dat = extracted_data

    #     # Write it to a file
    #     file.write(dat)
    #     file.close()
    #     # return file path
    #     return (path + " " + url)

    async def download_file(self, url, referer=None):
        """Download a file from a URL and save it to a temporary file."""
        headers = {}
        if referer:
            headers['Referer'] = referer

        try:
            response = await self.request_get(url, headers=headers)

            if response is not None:
                data = response.content

                # Handle gzip encoding
                if data[:2] == b'\x1f\x8b':
                    data = gzip.decompress(data)

                # Write to a temporary file
                file_handle, file_path = tempfile.mkstemp()
                with open(file_path, "wb") as file:
                    file.write(data)

                return file_path
        except Exception as e:
            self.logger.error(f"Error downloading file from {url}: {e}")
        
        return None

    # per la classe base di Debrid

    async def get_json_response(self, url, **kwargs):

        # Prende method
        method = kwargs.pop("method", 'get') # per default usa GET

        # Combina gli header specificati con quelli di default
        headers = kwargs.pop("headers", {})
        headers = {**self.headers, **headers}  # Unisce gli header di default e quelli personalizzati

        # Usa un timeout personalizzato o quello predefinito
        timeout = kwargs.pop("timeout", self.default_timeout)

        try:
            response = await self._client.request(
                method, url, headers=headers, timeout=timeout, **kwargs
            )
            response.raise_for_status()  # Solleva un'eccezione per errori HTTP 4xx o 5xx
            if response.is_success:
                if response.text.strip():
                    return response.json() # Restituisce la risposta finale dopo i reindirizzamenti
                else:
                    self.logger.warning(f"HTTP request with empty response")
                    return None
            
        except json.JSONDecodeError:
                self.logger.error(f"Failed to parse response as JSON: {response.text}")
                return None
        except httpx.HTTPStatusError as e:
            # Logga l'errore e restituisce una risposta informativa
            self.logger.error(f"Errore HTTP durante la richiesta: {e.response.status_code} {e.response.url}")
            return None
        except httpx.RequestError as e:
            # Logga l'errore e genera un'eccezione per errori di connessione o altro
            self.logger.error(f"Errore durante la connessione a {url}: heasers: {headers} {e}")
            return None
        
        return None

    async def download_torrent_file(self, download_url):
        async with self._client.stream("GET", download_url) as response:
            response.raise_for_status()
            return await response.aread()
