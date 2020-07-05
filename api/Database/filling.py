import mysql.connector
import requests
from config import DB_CONFIG


class Fill_data:
    """filling data in the database"""

    def __init__(self):
        """attribute of the class "request"""
        self.cnx = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.cnx.cursor(buffered=True)
        self.cat_id = self.cursor.lastrowid
        self.cat = 0
        self.nb_pages = 0
        self.nb_prod = 0
        self.nb_prod_remove = 0
        self.nb_prod_to_keep = 0 
        self.url = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
        self.categories = [
            "Aliments et boissons à base de végétaux",
            "Aliments d'origine végétale",
            "Boissons",
            "Snacks sucrés",
            "Snacks",
        ]

    def make_request(self, database):
        """Adding data to the database"""
        for category in self.categories:
            self.nb_pages = 1
            database.add_category(self.cat_id, category)
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
