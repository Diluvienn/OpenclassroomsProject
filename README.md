# Projet 2 - Utilisez les bases de Python pour l'analyse de marché

Ce script permet de parcourir le site http://books.toscrape.com/index.html pour en extraire les informations 
des livres ainsi que les illustrations, catégorie par catégorie.
Les informations récupérées sont :
 - product page_url
 - universal_product_code (upc)
 - title
 - price_including_tax
 - price_excluding_tax
 - number_available
 - product_description
 - category
 - review_rating$image_url

Ces données sont enregistrées dans des fichiers CSV par catégorie.
Les images sont enregistrées en .jpeg dans des sous dossiers nommés selon la catégorie, dans un dossier parent 
"Book illustrations".

## Installation
1. Clonez le dépot

Depuis le terminal :
git clone https://github.com/Diluvienn/OpenclassroomsProject.git

3. Créez un environnement virtuel
Dans le terminal :
- cd OpenclassroomsProject
- python -m venv venv
- venv/Scripts/activate

3. Installez les dépendances 

pip install -r requirements.txt

## Comment executer
Dans le terminal :
- python main.py

Cela lancera le script et génèrera les dossiers :
- csv_output (avec les csv des livres par catégorie)
- images_output (avec les images des livres par catégorie)

L'ensemble du processus prend une 10ène de minutes. 
Il faut indiquer à chaque itération si on veut continuer ou non (y/n).


## Structure du projet

Projet2/

├── main.py

├── extract.py

├── transform.py

├── load.py

├── requirements.txt

├── README.md

Après execution du script ajout de :

├── csv_output

├── images_output


