# VERSION: 0.0.31
# AUTHORS: Ogekuri

from bs4 import BeautifulSoup
from urllib.parse import quote
from utils.logger import setup_logger
from utils.novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from search.plugins.base_plugin import BasePlugin


class torrentgalaxy(BasePlugin):
	url='https://torrentgalaxy.one/'
	api='https://torrentgalaxy.one'
	name='TorrentGalaxy'
	language = "any"
	logger = setup_logger(__name__, True) # debug=True

	# uncomment appropriate lines to include TPB category in qBittorrent search category
	# currently set to include only HD video for "movies" & "tv"
	supported_categories={
		'all': [],
		'movies':
		[
			"Movies"
		],
		'tv':
		[
			"TV",
			"Anime"
		]
	}

	query_url='{self.api}/get-posts/category:{category}:keywords:{what}'

	
	async def download_torrent(self,info_url):
		session = AsyncThreadSafeSession()  # Usa il client asincrono
		try:
			# Esegui la ricerca
			search_response = await session.request_get(info_url)
			if search_response.text is not None and len(search_response.text) > 0:
				html_content = search_response.text
				if html_content is not None:
					# Parsing della risposta HTML
					soup = BeautifulSoup(html_content, 'html.parser')

					covercells = soup.find_all('div', class_='tpcell', id="covercell")  # Trova la prima tabella
					links = [a['href'] for a in covercells[1].find_all("a", href=True)]
					magnet_link = links[1]
					await session.close()
					return magnet_link
		except Exception as e:
			self.logger.error(f"Plugins {self.name}: Errore durante la download_torrent(): {e}")

		await session.close()
		return None

	async def search(self,what,cat='all'):
		session = AsyncThreadSafeSession()  # Usa il client asincrono
		prettyPrinter.clear()
		what = quote(what)

		try:
			results = []
			# TODO: questa ricerca puù andare in parallelo con delle chiamate asincrone
			for category in self.supported_categories[cat]:
			
				# URL e parametri per la ricerca
				search_url=self.query_url.format(self=self,what=what,category=category)

				# Esegui la ricerca
				search_response = await session.request_get(search_url)
				if search_response.text is not None and len(search_response.text) > 0:
					html_content = search_response.text
					if html_content is not None:
						# Parsing della risposta HTML
						soup = BeautifulSoup(html_content, 'html.parser')

						divs = soup.find_all('div', class_='tgxtablerow txlight')  # Trova la prima tabella
						for div in divs:
							cells = div.find_all('div', class_='tgxtablecell')  # Trova la prima tabella
							category = " ".join(cells[0].get_text(strip=True).split())
							name = " ".join(cells[3].get_text(strip=True).split())
							# 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF
							# - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf/
							# - /get-posts/keywords:tt14257582
							links = [a['href'] for a in cells[3].find_all("a", href=True)]
							link = links[0]
							size = " ".join(cells[7].get_text(strip=True).split())
							numbers = list(map(int, (" ".join(cells[10].get_text(strip=True).split())).strip(" []").split("/")))  # Divide per "/" e converte in interi
							seeders = numbers[0]
							leechers = numbers[1]

							results.append({
								"link": self.api + link,
								"name": name,
								"size": size,
								"seeds": seeders,
								"leech": leechers,
								"engine_url": self.url,
								"desc_link": self.api + link
							})

			# Stampa i risultati
			i = 0
			for result in results:
				if i > 0:   # salta l'intestazione
					prettyPrinter(result)
				i = i + 1

		except Exception as e:
			self.logger.error(f"Plugins {self.name}: Errore durante la download_torrent(): {e}")
		
		await session.close()
		return prettyPrinter.get()
