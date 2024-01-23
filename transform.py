"""
Module: transform.py

This module provides functions for transforming raw data obtained during the extraction process.
The transformation is designed to clean and format specific pieces of information extracted from the website.

Functions:
- transform_title(raw_title)
- transform_availability(raw_availability)
- transform_img_url(raw_img_url)
"""


def transform_title(raw_title):
    """
    Transform the raw title by removing extra information.

    Parameters:
    - raw_title (str): The raw title of the book.

    Returns:
    str: The transformed title.
    """
    transformed_title = raw_title.split('|')[0].strip()
    return transformed_title

def transform_availability(raw_availability):
    """
        Transform the raw availability information.

        Parameters:
        - raw_availability (str): The raw availability information.

        Returns:
        str: The transformed availability information.
        """
    return raw_availability.split('(')[1].replace('available)',
                                                  '') if raw_availability else "Exemplaires disponibles non trouvés sur la page"

def transform_img_url(raw_img_url):
    """
    Transform the raw image URL.

    Parameters:
    - raw_img_url (str): The raw image URL.

    Returns:
    str: The transformed image URL if found, otherwise "Image URL not found".
    """
    return raw_img_url.replace("../..", "https://books.toscrape.com") if raw_img_url else "Image URL not found"