import csv
from datetime import datetime
from extract import extract_book_data

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

def create_csv_for_category(category_link, category_name, links_book):
    # Créer un fichier CSV pour la catégorie
    csv_file_path = f"{category_name}_data_{timestamp}.csv"

    # Itérer sur les liens des livres et extraire les données
    for link_book in links_book:
        book_data = extract_book_data(link_book)
        write_to_csv(csv_file_path, book_data)


def write_to_csv(file_path, book_data):
    """
       Écrit les informations d'un livre dans un fichier CSV.

       Parameters:
       - file_path (str): Le chemin du fichier CSV.
       - book_data (dict): Un dictionnaire contenant les informations du livre.

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
