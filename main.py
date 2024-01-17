import requests
from datetime import datetime
from bs4 import BeautifulSoup

from extract import extract_book_data
from write_to_csv import write_to_csv

# Nom de l'output avec horodatage
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
csv_file_path = f"books_data{timestamp}.csv"

# Liste pour stocker les liens des pages
links = []
page_number = 1
base_url = "http://books.toscrape.com/catalogue/category/books/travel_2/page-{}.html"

# Extraction des liens des livres
while True:
    url = base_url.format(page_number)
    print(url)
    response = requests.get(url)

    # Arret de boucle : toutes les pages de la catégorie ont été visitées
    if page_number != 1 and response.status_code != 200:
        print(f" !=1 et !=200", url)
        break

    # Gestion des catégories avec une seule page. Le format de l'URL est différente
    if page_number == 1 and response.status_code != 200:
        url = base_url.replace('page-{}', 'index')
        response = requests.get(url)
        print(f" ==1 et !=200", url)

    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Page {page_number}")
    all_h3 = soup.find_all('h3')
    for h3 in all_h3:
        a = h3.find('a')
        print(a)
        link = a['href'].replace('../../..', 'http://books.toscrape.com/catalogue')
        links.append(link)
    page_number += 1

print("nombre de links :", len(links))

#Ecriture des data extraites dans le CSV
for link in links:
    print(link)
    book_data = extract_book_data(link)
    write_to_csv(csv_file_path, book_data)

print("Extraction et écriture terminées.")


