import mysql.connector
import requests
import random
from config import DB_CONFIG

class Category:
    """classe représentant l'objet categorie"""

    def __init__(self):
        """Constructeur de la classe categorie"""
        self.cat = 0
        self.nb_pages = 0
        self.nb_prod = 0
        self.nb_prod_remove = 0
        self.nb_prod_to_keep = 0 
        self.url = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
        self.categories = []

    def find_categories(self):
        for i in range(5):
            url = "https://fr.openfoodfacts.org/categories.json"
            num = random.randrange(500)
            response = requests.get(url)
            resp = response.json()
            categorie = (resp["tags"][num].get("name"))
            self.categories.append(categorie)

    def get_categories(self, database):
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor(buffered=True)
        for category in self.categories:
            self.nb_pages = 1
            database.add_category(category)
            print("------------------------------------------------------")
            print((self.categories[self.cat]), "...waiting...")
            print("------------------------------------------------------")
            self.cat += 1
            for product in range(20):
                response = requests.get(self.url.format(category, self.nb_pages))
                resp = response.json()
                self.nb_pages += 1
                for i in range(20):
                    self.nb_prod += 1
                    product = {
                        "barcode": resp["products"][i].get("_id", 0),
                        "name": resp["products"][i].get("product_name_fr", "0"),
                        "nutriscore": resp["products"][i].get("nutrition_grades", "0"),
                        "url": resp["products"][i].get("url", "Non renseigner"),
                        "market": resp["products"][i].get("stores", "Non renseigner"),
                        "cat_id": self.cat,
                    }
                    correct_barcode = (
                        int(product["barcode"]) > 3000000000000
                        and int(product["barcode"]) < 8000000000000
                    )
                    correct_name = (
                        str(product["name"]) != "0" and str(product["name"]) != ""
                    )
                    correct_nutriscore = str(product["nutriscore"]) != "0"
                    if correct_barcode and correct_name and correct_nutriscore:
                        database.add_product(
                            product["barcode"],
                            product["name"],
                            (product["nutriscore"]).upper(),
                            product["url"],
                            product["market"],
                        )
                        self.nb_prod_to_keep += 1
                        self.nb_prod_remove = self.nb_prod - self.nb_prod_to_keep
            print("{} products collected.".format(self.nb_prod))
            print("{} products removed.".format(self.nb_prod_remove))
            print("{} products added.".format(self.nb_prod_to_keep))
            self.nb_prod = self.nb_prod_remove = self.nb_prod_to_keep = 0
