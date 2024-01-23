from extract import extract_book_data
from write_to_csv import write_to_csv
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")


if __name__ == "__main__":
    csv_file_path = f"books_data{timestamp}.csv"
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    book_data = extract_book_data(url)
    write_to_csv(csv_file_path, book_data)


