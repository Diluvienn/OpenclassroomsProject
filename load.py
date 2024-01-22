"""
Module write_to_csv

This module provides functions for downloading images and writing book information to CSV files.


Functions:
- download_image(titles, image_urls, category_name): Downloads and saves images for a given category.
- create_csv_for_category(category_link, category_name, links_book): Writes book information to a CSV file.
- write_to_csv(file_path, book_data): Writes book information to a CSV file.

"""

import csv
from datetime import datetime
from extract import extract_book_data
import requests
import os

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

headers = ["product_page_url",
           "universal_product_code",
           "title",
           "price_including_tax",
           "price_excluding_tax",
           "number_available",
           "product_description",
           "category",
           "review_rating",
           "image_url"]


def download_image(titles, image_urls, category_name):
    """
        Downloads and saves images for a given category.

        Parameters:
        - titles (list): List of book titles.
        - image_urls (list): List of image URLs corresponding to the titles.
        - category_name (str): The name of the book category.

        Returns:
        None
        """
    main_folder_path = os.path.join("images_output")

    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)

    category_folder_path = os.path.join(main_folder_path, f"Illustrations_{category_name}")
    if not os.path.exists(category_folder_path):
        os.makedirs(category_folder_path)

        for title, img_url in zip(titles, image_urls):
            try:
                title = title.replace(":", " ").replace("/", "-").replace("&", "and").replace("*", "_").replace("?", "").replace('"', "")
                destination_path = os.path.join(category_folder_path, f"{title}_{timestamp}.jpg")
                response = requests.get(img_url, stream=True)
                response.raise_for_status()
                with open(destination_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=4096):
                        file.write(chunk)
                    print(f"Image téléchargée avec succès : {destination_path}")
            except Exception as e:
                print(f"Erreur lors du téléchargement de l'image pour {title}: {e}")



def create_csv_for_category(category_name, links_book):
    """
        Writes the information of books to a CSV file.

        Parameters:
        - category_link (str): The URL of the book category.
        - category_name (str): The name of the book category.
        - links_book (list): List of links to the books in the category.

        Returns:
        None
        """
    # Créer un dossier pour les CSV
    main_folder_path = os.path.join("csv_output")
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)

    # Créer un fichier CSV pour la catégorie
    csv_file_path = os.path.join(main_folder_path, f"{category_name}_data_{timestamp}.csv")

    # Itérer sur les liens des livres et extraire les données
    for link_book in links_book:
        book_data = extract_book_data(link_book)
        write_to_csv(csv_file_path, book_data)


def write_to_csv(file_path, book_data):
    """
    Writes book information to a CSV file.

        Parameters:
        - file_path (str): The path to the CSV file.
        - book_data (dict): A dictionary containing the book information.

        Returns:
        None
       """



    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(book_data)


if __name__ == "__main__":
    # Testez la fonction write_to_csv avec des données de test
    test_data = {
        "product_page_url": "https://example.com",
        "universal_product_code": "123456789",
        "title": "Test Book",
        "price_including_tax": "20.99",
        "price_excluding_tax": "15.99",
        "number_available": "50",
        "product_description": "Sample description",
        "category": "Fiction",
        "review_rating": "Four",
        "image_url": "https://example.com/image.jpg"
    }
    csv_file_path = "test_output.csv"
    print("Contenu de book_data:", test_data)
    # Écrire les données de test dans le fichier CSV
    write_to_csv(csv_file_path, test_data)

    print(f"Les données ont été écrites dans {csv_file_path}.")
    # csv_file_path = "output.csv"
    # url_to_extract = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    # write_to_csv(csv_file_path, url_to_extract)

    destination_path = "img_test.jpg"
    url = "http://books.toscrape.com/media/cache/f1/78/f17805e88aed31aae352ab250b2a379d.jpg"
    download_image(url)
    print(f"l'image a été enregistrée dans {destination_path}.")
