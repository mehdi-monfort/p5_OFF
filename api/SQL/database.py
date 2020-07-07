import mysql.connector
from config import DB_CONFIG


class Database:
    """allows to make sql requests"""

    def __init__(self):
        """allows connection with the database"""
        self.cnx = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.cnx.cursor()

    ###########################################################################
    #                                adding data                              #
    ###########################################################################

    def add_category(self, categorie):
        """add favorite in table"""
        request_sql = "INSERT IGNORE Categories(categorie) VALUES (%s)"
        categorie = (categorie,)
        self.cursor.execute(request_sql, categorie)
        return self.cursor.fetchone()

    def add_product(self, barcode, name, nutriscore, url, market):
        """add product in table"""
        request_sql = """
        INSERT IGNORE Products(barcode, name, score, url, market)
        VALUES (%s, %s, %s, %s, %s)
            """
        element = (
            barcode,
            name,
            nutriscore,
            url,
            market,
        )
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchone()

    def add_favorite(self, code):
        """add favorite in table"""
        request_sql = "INSERT INTO Favorites(code) VALUES (%s)"
        element = (code,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchone()

    def add_relation(self, cat_id, barcode):
        """add product in table"""
        request_sql = """
            INSERT INTO Relations(cat_id, barcode)
            VALUES (%s, %s)
            """
        element = (
            cat_id,
            barcode,
        )
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchone()

    ###########################################################################
    #                                delete data                              #
    ###########################################################################

    def del_category(self, cat_id):
        """add favorite in table"""
        request_sql = "DELETE FROM Categories WHERE cat_id = (%s)"
        element = (cat_id,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchone()

    ###########################################################################
    #                              Selecting data                             #
    ###########################################################################

    def search_favorite(self):
        """ display the favorites """
        search_fav = """
            SELECT * FROM Products JOIN Favorites
            ON Products.barcode = Favorites.code
            """
        self.cursor.execute(search_fav)
        return self.cursor.fetchall()

    def check_favorite(self):
        """check if favorite table is empty"""
        check_fav = "SELECT COUNT(*) FROM Favorites"
        self.cursor.execute(check_fav)
        return self.cursor.fetchone()[0]

    def search_product(self, cat_id):
        """ display the products """
        request_sql = """
            SELECT * FROM Products INNER JOIN Relations
            ON Relations.barcode = Products.barcode
            WHERE cat_id = (%s)
            """
        element = (cat_id,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchall()

    def search_better_products(self, cat_id):
        """ search better products """
        request_sql = """
            SELECT * FROM Products INNER JOIN Relations
            ON Relations.barcode = Products.barcode
            WHERE cat_id = (%s) ORDER BY score ASC LIMIT 5
            """
        element = (cat_id,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchall()

    def search_categorie(self):
        """ display the categories """
        display_cat = "SELECT categorie FROM Categories"
        self.cursor.execute(display_cat)
        return self.cursor.fetchall()

    ###########################################################################
    #                               Display data                              #
    ###########################################################################

    def display_better_products(self, cat_id):
        liste = self.search_better_products(cat_id)
        for i in range(len(liste)):
            print(i + 1, ".\t", liste[i][0], "\t", liste[i][2])
        nb_substitut = i + 1
        return nb_substitut

    def display_categorie(self):
        liste = self.search_categorie()
        for i, categorie in enumerate(liste):
            print(i + 1, categorie)
        return i

    def display_products(self, cat_id):
        """ display the products """
        liste = self.search_product(cat_id)
        for i in range(len(liste)):
            print(i, ".\t", liste[i][0], "\t", liste[i][2])
        return i

    def save_favorite(self, cat, sub):
        liste = self.search_better_products(cat)
        sub -= 1
        barcode = liste[sub][1]
        self.add_favorite(barcode)

    def display_favorite(self):
        """ diplay the favorites """
        liste = self.search_favorite()
        for i in range(len(liste)):
            print(
                i + 1, ".\t", liste[i][:4], "\n",
                 "..\t", "store:", liste[i][4]
                )
