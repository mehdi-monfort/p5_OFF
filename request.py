import requests
import random
import re


class Request:
    """classe représentant l'objet categorie"""

    def __init__(self):
        """Constructeur de la classe categorie"""
        self.cat = 0
        self.url = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
        self.categories = []

    def find_categories(self):
        """selects categories at random"""
        for i in range(10):
            url = "https://fr.openfoodfacts.org/categories.json"
            response = requests.get(url)
            resp = response.json()
            num = random.randrange(1700)
            categorie = resp["tags"][num].get("name")
            self.categories.append(categorie)

    def get_categories(self, database):
        """add categories and products in database"""
        for cat_id, category in enumerate(self.categories):
            n_prod = 0
            n_prod_remove = 0
            n_prod_keep = 0
            database.add_category(category)
            print("------------------------------------------------------")
            print((self.categories[self.cat]), "...waiting...")
            print("------------------------------------------------------")
            self.cat += 1
            for page in range(10):
                response = requests.get(self.url.format(category, page))
                resp = response.json()
                for i in range(20):
                    try:
                        product = {
                            "barcode": resp["products"][i].get("_id", 0),
                            "name": resp["products"][i].get("product_name_fr", "0"),
                            "score": resp["products"][i].get("nutrition_grades", "0"),
                            "url": resp["products"][i].get("url", "absent"),
                            "market": resp["products"][i].get("stores", "absent"),
                        }
                        n_prod += 1
                        checkers = [
                            3 * 10 ** 12 < int(product["barcode"]) < 8 * 10 ** 12,
                            str(product["name"]) != "0" and str(product["name"]) != "",
                            str(product["score"]) != "0",
                        ]
                        if all(checkers):
                            database.add_product(
                                product["barcode"],
                                product["name"],
                                (product["score"]).upper(),
                                product["url"],
                                product["market"],
                            )
                            n_prod_keep += 1
                            database.add_relation(self.cat, product["barcode"])
                        else:
                            continue
                        n_prod_remove = n_prod - n_prod_keep
                    except IndexError as err:
                        pass
            if n_prod_keep <= 5:
                print(f"la categories: {category} à été supprimé")
                database.del_category(cat_id + 1)
            elif n_prod_keep >= 1:
                print(f"{n_prod} products collected.")
                print(f"{n_prod_remove} products removed.")
                print(f"{n_prod_keep} products added.")
