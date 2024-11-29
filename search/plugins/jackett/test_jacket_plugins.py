import requests
import yaml
from bs4 import BeautifulSoup

# Carica il file YAML
def load_config(file_path):
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

# Costruisci la query
def build_query(config, keywords, category=0):
    base_url = config['links'][0]  # Usa il primo link nella lista
    search_path = config['search']['paths'][0]['path']
    search_url = f"{base_url}/{search_path}"
    
    # Parametri di ricerca
    search_params = {
        'page': 'torrents',
        'search': keywords,
        'category': category,
        'options': 0,  # Configurazione standard dal file YAML
        'active': 0,  # Cerca attivi e inattivi
        'order': config['settings'][5]['default'],  # Default sort
        'by': config['settings'][6]['default'],  # Default order
    }
    return search_url, search_params

# Effettua la ricerca
def perform_search(search_url, search_params):
    response = requests.get(search_url, params=search_params)
    response.raise_for_status()  # Solleva un'eccezione per errori HTTP
    return response.text

# Analizza i risultati
def parse_results(html, config):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    
    # Selettore dei risultati dalla configurazione YAML
    row_selector = config['search']['rows']['selector']
    rows = soup.select(row_selector)

    for row in rows:
        # Estrarre campi specifici
        title = row.select_one(config['search']['fields']['title']['selector']).text.strip()
        download_link = row.select_one(config['search']['fields']['download']['selector'])
        if download_link:
            download_url = download_link['href']
        else:
            download_url = None
        
        results.append({
            'title': title,
            'download_url': download_url,
        })

    return results

# Funzione principale
def main():
    # Percorso al file YAML
    yaml_path = 'ilcorsaroblu.yml'
    
    # Carica configurazione
    config = load_config(yaml_path)

    print(config)
    
    # Parola chiave da cercare
    keywords = 'Arcane S01E02'
    
    # Costruisci la query
    search_url, search_params = build_query(config, keywords)
    print(search_url)
    print(search_params)
    
    # Effettua la ricerca
#    print(f"Searching: {search_url} with {search_params}")
#    html = perform_search(search_url, search_params)
    
    # Analizza i risultati
#    results = parse_results(html, config)
    
    # Stampa i risultati
#    for result in results:
#        print(f"Title: {result['title']}")
#        print(f"Download URL: {result['download_url']}")
#        print('---')

if __name__ == '__main__':
    main()

