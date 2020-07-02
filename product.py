import requests
import re


class Product:
    """classe représentant l'objet produit"""

    def __init__(self, barcode, name, nutriscore, url, market, category, language):
        """Constructeur de la classe Produit"""
        self.barcode = barcode
        self.name = name
        self.nutriscore = nutriscore
        self.url = url
        self.market = market

    def get_products(category, prod):
        url = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
        response = requests.get(url.format(category, prod + 1))
        resp = response.json()
        product = {
            "barcode": resp["products"][prod].get("_id", 0),
            "name": resp["products"][prod].get("product_name_fr", "0"),
            "nutriscore": resp["products"][prod].get("nutrition_grades", "0"),
            "url": resp["products"][prod].get("url", "Non renseigner"),
            "market": resp["products"][prod].get("stores", "Non renseigner"),
            "categories": resp["products"][prod].get("categories", "0"),
            "language": resp["products"][prod].get("lc", "0"),
        }

        products = Product(
            product["barcode"],
            product["name"],
            product["nutriscore"],
            product["url"],
            product["market"],
            product["categories"],
            product["language"],
        )
        correct_barcode = (
            int(product["barcode"]) > 3000000000000
            and int(product["barcode"]) < 8000000000000
        )
        correct_name = product["name"] != "0" and product["name"] != ""
        correct_nutriscore = (
            product["nutriscore"] != "0" and product["nutriscore"] != ""
        )
        correct_language = product["language"] != "0"
        if correct_barcode and correct_name and correct_nutriscore and correct_language:
            regex = r", "
            test_str = product["categories"]
            subst = "\n"
            result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
            regex2 = r","
            test2 = result
            product["categories"] = re.sub(regex2, subst, test2, 0, re.MULTILINE)
            return product
