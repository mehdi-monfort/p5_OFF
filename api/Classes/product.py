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
            # "categories": resp["products"][product].get("categories", "0"),
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
        if product["market"] == "":
            product["market"] = "Non renseigner"
        good_name = product["name"] != ""
        good_score = product["nutriscore"] != ""
        if good_code and good_name and good_score:
            list_product.append(product)
            return list_product
