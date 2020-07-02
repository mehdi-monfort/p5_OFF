import requests

class Category:
    """classe représentant l'objet categorie"""

    def __init__(self, name):
        """Constructeur de la classe categorie"""
        self.name = name
        self.category = range(10)

    def get_categories(tags):
        url = "https://fr.openfoodfacts.org/categories.json"
        response = requests.get(url)
        resp = response.json()
        categorie = (resp["tags"][tags].get("name"))
        return categorie