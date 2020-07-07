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
        for cat_id in range(5):
            category = Category.get_categories()
            print(category)
            self.database.add_category(category)
            for page in range(19):
                for product in range(19):
                    product = Product.get_products(category, page+1, product+1)
                    if product is not None:
                        self.database.add_product(
                            product["barcode"],
                            product["name"],
                            (product["nutriscore"]).upper(),
                            product["url"],
                            product["market"],
                        )
                        self.database.add_relation(
                            cat_id+1, product["barcode"]
                        )
        print("Request complete.")
        url = "https://fr.openfoodfacts.org/categories.json"
        num = random.randrange(500)
        response = requests.get(url)
        resp = response.json()
        categorie = (resp["tags"][num].get("name"))
        return categorie

    def get_products(category, page, product):
        list_product = []
        url = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
        response = requests.get(url.format(category, page))
        resp = response.json()
        product = {
            "barcode": resp["products"][product].get("_id", ""),
            "name": resp["products"][product].get("product_name_fr", ""),
            "nutriscore": resp["products"][product].get("nutrition_grades", ""),
            "url": resp["products"][product].get("url", "Non renseigner"),
            "market": resp["products"][product].get("stores", "Non renseigner"),
        }
        products = Product(
            product["barcode"],
            product["name"],
            product["nutriscore"],
            product["url"],
            product["market"],
        )
        good_code = (
            int(product["barcode"]) > 3000000000000
            and int(product["barcode"]) < 8000000000000
        )
        if product["market"] == "":
            product["market"] = "Non renseigner"
        good_name = product["name"] != ""
        good_score = product["nutriscore"] != ""
        if good_code and good_name and good_score:
            return product
