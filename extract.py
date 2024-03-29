"""
Extract.py

This module provides functions for extract
- product_page_url,
- universal_product_code,
- title,
- price_including_tax,
- price_excluding_tax,
- number_available
- product_description
- category
- review_rating
- image_url

"""

import requests
from bs4 import BeautifulSoup
from transform import transform_title, transform_availability, transform_image_url

image_urls = []
titles = []


def extract_url(url):
    """
    Fetches the HTML content from the specified URL and returns the URL along with the BeautifulSoup object.

    Parameters:
    - url (str): The URL to extract information from.

    Returns:
    tuple: A tuple containing the response URL and the BeautifulSoup object.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return response.url, soup if response else "URL non valide"


def extract_upc(soup):
    """
    Extracts the UPC (Universal Product Code) from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The UPC if found, otherwise "UPC not found".
    """
    upc_element = soup.find('th', string='UPC')
    return upc_element.find_next('td').text if upc_element else "UPC non trouvé"


def extract_title(soup):
    """
    Extracts the title of a book from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The title of the book.
    """
    raw_title = soup.find('title').text
    title = transform_title(raw_title)
    titles.append(title)
    return title if raw_title else "Titre non trouvé"


def extract_price_excluding_tax(soup):
    """
    Extracts the price (excluding tax) from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The price (excluding tax) if found, otherwise "Price excluding tax not found".
    """
    price_excluding_element = soup.find('th', string='Price (excl. tax)')
    return price_excluding_element.find_next('td').text if price_excluding_element else "Prix hors taxe non trouvé"


def extract_price_including_tax(soup):
    """
    Extracts the price (including tax) from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The price (including tax) if found, otherwise "Price including tax not found".
    """
    price_including_element = soup.find('th', string='Price (incl. tax)')
    return price_including_element.find_next('td').text if price_including_element else "Prix avec taxe non trouvé"


def extract_availability(soup):
    """
    Extracts the raw availability information from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The raw availability information if found, otherwise "Availability information not found on the page".
    """
    available_element = soup.find('th', string='Availability')
    raw_availability = available_element.find_next('td').text if available_element else None
    availability = transform_availability(raw_availability)
    return availability


def extract_description(soup):
    """
   Extracts the product description from the provided BeautifulSoup object.

   Parameters:
   - soup (BeautifulSoup): The BeautifulSoup object of a web page.

   Returns:
   str: The product description if found, otherwise "Description not found".
   """
    description_element = soup.find('div', id='product_description')
    return description_element.find_next('p').text if description_element else "Description non trouvée"


def extract_category(soup):
    """
    Extracts the category information from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The category information if found, otherwise "Category not found".
    """
    category_element = soup.find('li', {'class': 'active'})
    return category_element.find_previous('a').text if category_element else "Catégorie non trouvée"


def extract_rating(soup):
    """
   Extracts the review rating from the provided BeautifulSoup object.

   Parameters:
   - soup (BeautifulSoup): The BeautifulSoup object of a web page.

   Returns:
   str: The review rating if found, otherwise "Rating not found".
   """
    rating_element = soup.select_one('p.star-rating')
    return rating_element['class'][-1] if rating_element else "Note non trouvée"


def extract_image_url(soup):
    """
    Extracts the image URL from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    str: The image URL if found, otherwise "Image URL not found".
    """
    raw_image_url = soup.select_one('img')['src']
    image_url = transform_image_url(raw_image_url)
    image_urls.append(image_url)
    return image_url


def extract_book_data(url):
    """
    Extracts the information of a book from the specified URL.

    Parameters:
    - url (str): The URL of the page.

    Returns:
    dict: A dictionary containing the information of the book.
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
    image_url = extract_image_url(soup)

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


def extract_links_from_page(soup):
    """
    Extracts the book links from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object of a web page.

    Returns:
    list : A list of book links
    """
    links_book = []
    all_h3 = soup.find_all('h3')
    for h3 in all_h3:
        a = h3.find('a')
        link_book = a['href'].replace('../../..', 'https://books.toscrape.com/catalogue')
        links_book.append(link_book)

    return links_book


if __name__ == "__main__":
    pass
