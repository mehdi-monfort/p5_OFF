import requests
from Class.category import Category
from Class.product import Product
from Class.relation import Relation


class Request():
    """class allowing queries with the Open Food Facts API,
    sorting and adding data to the database"""
    def __init__(self):
        """builder Request: url and categories"""
        self.url = "https://world.openfoodfacts.org/cgi/search.pl?search_terms={}&search_simple=1&page_size=500&action=process&json=1"
        self.categories = [
            "Produits fermentés",
            "Jus et nectars",
            "Gelées de fruits",
            "Matières grasses",
            "snacks",
        ]

    def create_database(self, database):
        """queries, sorting and adding"""
        print("Waiting, request in progress ...")
        for cat_id, name in enumerate(self.categories):
            n_prod = 0
            n_prod_remove = 0
            n_prod_keep = 0
            cat_id += 1
            category = Category(cat_id, name)
            database.add_category(category.name)
            print("------------------------------------------------------")
            print(category.name, "...waiting...")
            print("------------------------------------------------------")
            response = requests.get(self.url.format(name))
            resp = response.json()
            for i in range(500):
                try:
                    prod = Product(
                        resp["products"][i].get("nutrition_grades", "0"),
                        resp["products"][i].get("_id", 0),
                        resp["products"][i].get("product_name_fr", "0"),
                        resp["products"][i].get("url", "absent"),
                        resp["products"][i].get("stores", "absent"),
                        )
                    n_prod += 1
                    checkers = [
                        3 * 10 ** 12 < int(prod.barcode) < 8 * 10 ** 12,
                        str(prod.name) != "0" and str(prod.name) != "",
                        str(prod.nutriscore) != "0"
                    ]
                    if all(checkers):
                        database.add_product(
                            (prod.nutriscore).upper(),
                            prod.barcode,
                            prod.name,
                            prod.url,
                            prod.market,
                        )
                        n_prod_keep += 1
                        link = Relation(category.cat_id, prod.barcode)
                        database.add_relation(link.cat_id, link.barcode)
                    else:
                        continue
                except IndexError:
                    continue
                n_prod_ignore = n_prod - n_prod_keep
            print(f"{n_prod} products collected.")
            print(f"{n_prod_ignore} products ignored.")
            print(f"{n_prod_keep} products added.")
            print("Request complete.")
