import csv

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


def write_to_csv(file_path, book_data):

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(book_data)

if __name__ == "__main__":
    # Testez la fonction write_to_csv avec des données de test
    test_data = {
        "product_page_url": "http://example.com",
        "universal_product_code": "123456789",
        "title": "Test Book",
        "price_including_tax": "20.99",
        "price_excluding_tax": "15.99",
        "number_available": "50",
        "product_description": "Sample description",
        "category": "Fiction",
        "review_rating": "Four",
        "image_url": "http://example.com/image.jpg"
    }
    csv_file_path = "test_output.csv"
    print("Contenu de book_data:", test_data)
    # Écrire les données de test dans le fichier CSV
    write_to_csv(csv_file_path, test_data)

    print(f"Les données ont été écrites dans {csv_file_path}.")
    # csv_file_path = "output.csv"
    # url_to_extract = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    # write_to_csv(csv_file_path, url_to_extract)