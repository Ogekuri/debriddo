# VERSION: 0.0.30
# AUTHORS: Scare! (https://Scare.ca/dl/qBittorrent/)
# CONTRIBUTORS: Ogekuri, LightDestory https://github.com/LightDestory

import urllib.parse
import json
from urllib.parse import quote
from utils.logger import setup_logger
from utils.novaprinter import PrettyPrint
prettyPrinter = PrettyPrint()
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
from search.plugins.base_plugin import BasePlugin


class thepiratebay(BasePlugin):
	url='https://thepiratebay.org'
	api='https://apibay.org'
	name='ThePirateBay'
	language = "any"
	logger = setup_logger(__name__)

	# uncomment appropriate lines to include TPB category in qBittorrent search category
	# currently set to include only HD video for "movies" & "tv"
	supported_categories={
		'all':		[0],
		'anime':
		[
			207,	# Video > HD - Movies
			208,	# Video > HD - TV shows
			201,	# Video > Movies
			202,	# Video > Movies DVDR
			205,	# Video > TV shows
			206,	# Video > Handheld
			209,	# Video > 3D
			299,	# Video > Other
			501,	# Porn > Movies
			502,	# Porn > Movies DVDR
			505,	# Porn > HD - Movies
			599,	# Porn > Other			!!! comma after each number...
			699		# Other > Other			!!! ...except the last!
		],
		'books':
		[
#			102,	# Audio > Audio books
			601,	# Other > E-books
			602		# Other > Comics
		],
		'games':
		[
			400,	# Games
			504		# Porn > Games
		],
		'movies':
		[
#			201,	# Video > Movies
#			202,	# Video > Movies DVDR
#			209,	# Video > 3D
			207		# Video > HD - Movies
		],
		'music':
		[
#			203,	# Video > Music videos
			101,	# Audio > Music
			104		# Audio > FLAC
		],
		'pictures':
		[
			603,	# Other > Pictures
			604,	# Other > Covers
			503		# Porn > Pictures
		],
		'software':	# but not games
		[
			300		# Applications
		],
		'tv':
		[
#			205,	# Video > TV shows
			208		# Video > HD - TV shows
		]
	}

	torrent='{self.url}/description.php?id={id}'
	download='{self.api}/t.php?id={id}'
	magnet='magnet:?xt=urn:btih:{hash}&dn={name}&{trackers} {info}'
	query='{self.api}/q.php?q={what}&cat={category}'

	trackers=[
		'udp://tracker.coppersurfer.tk:6969/announce',
		'udp://tracker.openbittorrent.com:6969/announce',
		'udp://9.rarbg.to:2710/announce',
		'udp://9.rarbg.me:2780/announce',
		'udp://9.rarbg.to:2730/announce',
		'udp://tracker.opentrackr.org:1337',
		'http://p4p.arenabg.com:1337/announce',
		'udp://tracker.torrent.eu.org:451/announce',
		'udp://tracker.tiny-vps.com:6969/announce',
		'udp://open.stealth.si:80/announce']


	async def download_torrent(self,info):
		session = AsyncThreadSafeSession()  # Usa il client asincrono
		torrent_id=urllib.parse.unquote(info).split('=')[-1]
		url=self.download.format(self=self,id=torrent_id)
		page = await session.retrieve_url(url)
		if page is not None:
			data=json.loads(page)
			if data:
				name=urllib.parse.quote(data['name'],safe='')
				trs=urllib.parse.urlencode({'tr':self.trackers},True)
				await session.close()
				return(str(self.magnet.format(hash		=data['info_hash'],
										name		=name,
										trackers	=trs,
										info		=info)))
			else:
				await session.close()
				raise Exception('Error in "'+self.name+'" search plugin, download_torrent()')
		await session.close()
		return None

	async def search(self,what,cat='all'):
		session = AsyncThreadSafeSession()  # Usa il client asincrono
		prettyPrinter.clear()
		what = quote(what)
		x=[]
		# TODO: leggere il numero di pagine e fare una chiamata asincrona per ogni pagina
		for category in self.supported_categories[cat]:
			url=self.query.format(self=self,what=what,category=category)
			# fix risulati nulli
			result = await session.retrieve_url(url)
			if result is not None and type(result) is str and len(result) > 0:
				parse = json.loads(result)
				if type(parse) is list and len(parse) > 0:
					if parse[0]['name'] != "No results returned" and parse[0]['info_hash'] != "0000000000000000000000000000000000000000":
						x+=json.loads(result)
		self.parseJSON(x)
		await session.close()
		return prettyPrinter.get()

	def parseJSON(self,collection):
		for torrent in collection:
			torrent_id=self.torrent.format(self=self,id=torrent['id'])
			data={
				'link':			urllib.parse.quote(torrent_id),
				'name':			torrent['name'],
				'size':			torrent['size'],
				'seeds':		torrent['seeders'],
				'leech':		torrent['leechers'],
				'engine_url':	self.url,
				'desc_link':	torrent_id
			}
			prettyPrinter(data)
