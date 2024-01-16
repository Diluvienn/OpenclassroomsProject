import requests
from bs4 import BeautifulSoup




def extract_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return response.url, soup


def extract_upc(soup):
    upc_element = soup.find('th', string='UPC')
    return upc_element.find_next('td').text if upc_element else "UPC non trouvé"


def extract_title(soup):
    return soup.find('title').text.split('|')[0].strip()


def extract_price_excluding_tax(soup):
    price_excluding_element = soup.find('th', string='Price (excl. tax)')
    return price_excluding_element.find_next('td').text if price_excluding_element else "Prix hors taxe non trouvé"


def extract_price_including_tax(soup):
    price_including_element = soup.find('th', string='Price (incl. tax)')
    return price_including_element.find_next('td').text if price_including_element else "Prix avec taxe non trouvé"


def extract_availability(soup):
    available_element = soup.find('th', string='Availability')
    return available_element.find_next('td').text.split('(')[1].replace('available)',
                                                                        '') if available_element else ("Exemplaires "
                                                                                                       "disponibles "
                                                                                                       "non trouvés "
                                                                                                       "sur la page")


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
    return soup.select_one('img')['src'].replace("../..", "https://books.toscrape.com")


def extract_book_data(url):
    """
        Extrait les informations d'un livre à partir de l'URL spécifiée.

        Parameters:
        - url (str): L'URL de la page.

        Returns:
        dict: Un dictionnaire contenant les informations du livre.
        """
    product_page_url, soup = extract_url(url)

    universal_product_code = extract_upc(soup)
    title = extract_title(soup)
    price_excluding_tax = extract_price_excluding_tax(soup)
    price_including_tax = extract_price_including_tax(soup)
    number_available = extract_availability(soup)
    product_description = extract_description(soup)
    category = extract_category(soup)
    review_rating = extract_rating(soup)
    image_url = extract_img_url(soup)

    book_data = {
        "product_page_url": product_page_url,
        "universal_product_code": universal_product_code,
        "title": title,
        "price_excluding_tax": price_excluding_tax,
        "price_including_tax": price_including_tax,
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url
    }


    return book_data



# if __name__ == "__main__":
#     # Tester la fonction avec l'URL spécifiée
#     url_to_test = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
#     extract_book_data(url_to_test)
