# VERSION: 0.0.29
# AUTHORS: Ogekuri

from bs4 import BeautifulSoup
from urllib.parse import quote, quote_plus
from utils.async_httpx_session import AsyncThreadSafeSession  # Importa la classe per HTTP/2 asyncrono
import sys
import asyncio

async def main():
    session = AsyncThreadSafeSession()


    # Variabili per l'autenticazione
    myusername = "tuo_username"
    mypassword = "tua_password"

    # URL del form di login e dati richiesti
    login_url = "https://ilcorsaroblu.org/index.php?page=login"


    # Dati del form di autenticazione
    data = {
        "uid": "ogekuri",
        "pwd": "******"
    }


    login = True
    # # Esegui il login
    # try:
    #     response = session.post(login_url, data=data, headers=headers)
    #     print(response.url)  # URL generato da requests
    #     response.raise_for_status()  # Controlla errori HTTP
    #     # Verifica se il login è stato effettuato correttamente
    #     if "Benvenuto" in response.text or "Logout" in response.text:
    #         print("Login effettuato con successo!")
    #         login = True
    #     else:
    #         print("Errore nel login. Controlla username e password.")
    # except requests.RequestException as e:
    #     print(f"Errore durante il tentativo di login: {e}")

    if login is not None:
        # Variabili per la ricerca

        # https://torrentgalaxy.one/get-posts/category:Movies:keywords:Wolfs%202024%20ITA
        # https://torrentgalaxy.one/get-posts/category:TV:keywords:Arcane%20S01%20ITA
        # https://torrentgalaxy.one/get-posts/category:Anime:keywords:Arcane%20S01%20ITA

        mytext = "Wolfs 2024 ITA"
        mycategory = "Movies"  # 
        mytext = quote(mytext)

        # URL e parametri per la ricerca
        search_url = f"https://torrentgalaxy.one/get-posts/category:{mycategory}:keywords:{mytext}"
        print(search_url)

        # Esegui la ricerca
        search_response = await session.request_get(search_url)
        if search_response is not None:
            search_response.raise_for_status()  # Controlla errori HTTP

            html_content = search_response.text

            if html_content is not None:
                # Parsing della risposta HTML
                soup = BeautifulSoup(html_content, 'html.parser')
                divs = soup.find_all('div', class_='tgxtablerow txlight')  # Trova la prima tabella
                r = 0
                for div in divs:
                    cells = div.find_all('div', class_='tgxtablecell')  # Trova la prima tabella
                    category = " ".join(cells[0].get_text().split())
                    name = " ".join(cells[3].get_text().split())
                    # 1/3: Wolfs 2024 Eng Fre Ger Ita Por Spa 2160p WEBMux DV HDR HEVC Atmos SGF
                    # - /post-detail/74d894/wolfs-2024-eng-fre-ger-ita-por-spa-2160p-webmux-dv-hdr-hevc-atmos-sgf/
                    # - /get-posts/keywords:tt14257582
                    links = [a['href'] for a in cells[3].find_all("a", href=True)]
                    link = links[0]
                    size = " ".join(cells[7].get_text().split())
                    numbers = list(map(int, (" ".join(cells[10].get_text().split())).strip(" []").split("/")))  # Divide per "/" e converte in interi
                    S = numbers[0]
                    L = numbers[1]

                    print(f"category: {category}, name: {name}, link: {link}, size: {size}, S: {S}, L: {L}")
    
    await session.close()



asyncio.run(main())