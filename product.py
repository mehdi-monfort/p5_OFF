import requests
import re


class Product:
    """classe représentant l'objet produit"""

    def __init__(self, barcode, name, nutriscore, url, market):
        """Constructeur de la classe Produit"""
        self.barcode = barcode
        self.name = name
        self.nutriscore = nutriscore
        self.url = url
        self.market = market

    def get_products(category, prod):
        url = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
        response = requests.get(url.format(category, prod))
        resp = response.json()
        product = {
            "barcode": resp["products"][prod].get("_id", ""),
            "name": resp["products"][prod].get("product_name_fr", ""),
            "nutriscore": resp["products"][prod].get("nutrition_grades", "0"),
            "url": resp["products"][prod].get("url", "Non renseigner"),
            "market": resp["products"][prod].get("stores", "Non renseigner"),
            # "categories": resp["products"][prod].get("categories", "0"),
        }
        products = Product(
            product["barcode"],
            product["name"],
            product["nutriscore"],
            product["url"],
            product["market"],
            # product["categories"],
        )
        good_code = (
            int(product["barcode"]) > 3000000000000
            and int(product["barcode"]) < 8000000000000
        )
        good_name = product["name"] != ""
        good_score = product["nutriscore"] != ""
        if good_code and good_name and good_score:
            # regex = r"(, |,|en:|fr:)"
            # liste = product["categories"]
            # subst = "\n"
            # product["categories"] = re.sub(regex, subst, liste, 0, re.MULTILINE)
            # print(product["categories"])
            return product
