import requests
from bs4 import BeautifulSoup

def extract_url(url):
    """
    Extrait l'URL de la page de livre

    Parameters:
    - url (str): L'URL de la page.

    Returns:
    - str: L'URL effective de la page après toutes les redirections.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return response.url, soup

def extract_upc(soup):
    upc_element = soup.find('th', string='UPC')
    return upc_element.find_next('td').text if upc_element else "UPC non trouvé"

def extract_title(soup):
    return soup.find('title').text.split('|')[0]

def extract_price_excl_tax(soup):
    price_excl_element = soup.find('th', string='Price (excl. tax)')
    return price_excl_element.find_next('td').text if price_excl_element else "Prix hors taxe non trouvé"

def extract_price_incl_tax(soup):
    price_incl_element = soup.find('th', string='Price (incl. tax)')
    return price_incl_element.find_next('td').text if price_incl_element else "Prix avec taxe non trouvé"

def extract_availability(soup):
    available_element = soup.find('th', string='Availability')
    return available_element.find_next('td').text.split('(')[1].replace('available)', '') if available_element else "Exemplaires disponibles non trouvés sur la page"

def extract_description(soup):
    description_element = soup.find('div', id='product_description')
    return description_element.find_next('p').text if description_element else "Description non trouvée"

def extract_category(soup):
    category_element = soup.find('li', {'class': 'active'})
    return category_element.find_previous('a').text if category_element else "Catégorie non trouvée"

def extract_rating(soup):
    rating_element = soup.select_one('p.star-rating')
    return rating_element['class'][-1] if rating_element else "Note non trouvée"

def extract_img_url(soup):
    return soup.select_one('img')['src'].replace("../..", "http://books.toscrape.com")

def extract_book_data(url):
    """
    Extrait les informations d'un livre à partir de l'URL spécifiée.

    Parameters:
    - url (str): L'URL de la page.
    """
    book_url, soup = extract_url(url)

    book_upc = extract_upc(soup)
    book_title = extract_title(soup)
    book_price_excl_tax = extract_price_excl_tax(soup)
    book_price_incl_tax = extract_price_incl_tax(soup)
    book_availability = extract_availability(soup)
    book_description = extract_description(soup)
    book_category = extract_category(soup)
    book_rating = extract_rating(soup)
    book_img_url = extract_img_url(soup)

    # Afficher les informations extraites
    print(f"URL de la page : {book_url}")
    print(f"UPC : {book_upc}")
    print(f"Titre du livre : {book_title}")
    print(f"Prix hors taxe : {book_price_excl_tax}")
    print(f"Prix avec taxe : {book_price_incl_tax}")
    print(f"Exemplaires disponibles : {book_availability}")
    print(f"Description : {book_description}")
    print(f"Catégorie : {book_category}")
    print(f"Note : {book_rating}")
    print(f"Image : {book_img_url}")

if __name__ == "__main__":
    # Tester la fonction avec l'URL spécifiée
    url_to_test = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    extract_book_data(url_to_test)
