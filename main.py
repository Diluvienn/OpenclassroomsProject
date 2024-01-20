import requests
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from extract import extract_links_from_page
from write_to_csv import  create_csv_for_category

# Nom de l'output avec horodatage
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")


# Listes pour stocker les différents liens et noms
book_links = []
category_links = []
category_names = []

# Page d'accueil
base_url = "https://books.toscrape.com/"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")


# Recherche des différentes catégories sur la page d'accueil dans <ul class=nav>
categories_element = soup.find('ul', {'class': 'nav'})

# Reformatage des url
for category in categories_element.find_all('a'):
    category_link = urljoin(base_url, category['href']).replace('index', 'page-{}')
    category_name = category.get_text(strip=True)
    category_names.append(category_name)
    category_links.append(category_link)

#Suppression du premier lien qui ramène à la page d'accueil
category_links.pop(0)
category_names.pop(0)


# Boucle dans chaque catégorie pour en extraire les liens de l'ensemble des livres
#  Boucle sur les noms des catégorie pour nommer les fichers CSV
for category_link, category_name in zip(category_links, category_names):
    page_number = 1
    category_link = category_link.format(page_number)
    print(category_link)
    response = requests.get(category_link)

    # Gestion des catégories avec une seule page. Le format de l'URL est différent
    if page_number == 1 and response.status_code != 200:
        url = category_link.replace('page-1', 'index')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Ecriture des data extraites dans le CSV
        book_links += extract_links_from_page(soup)
        create_csv_for_category(category_link, category_name, book_links)
        book_links.clear()
        print(f"Extraction et écriture du fichier {category_name} terminées.")

    # On boucle sur les pages des catégories à plusieurs pages
    elif response.status_code == 200:
        while response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            print(f"Page {page_number}")
            book_links += extract_links_from_page(soup)
            page_number += 1
            category_link = category_link.replace(f'page-{page_number - 1}', f'page-{page_number}')
            print('Après incrémentation du page number ', category_link)
            response = requests.get(category_link)

        # Ecriture des data extraites dans le CSV
        create_csv_for_category(category_link, category_name, book_links)
        book_links.clear()
        print(f"Extraction et écriture du fichier {category_name} terminées.")



