import mysql.connector
from config import DB_CONFIG

class Database:
    """allows to make sql requests"""
    def __init__(self):
        """allows connection with the database"""
        self.cnx = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.cnx.cursor()

    #############################################################################################
    #                                          adding data                                      #
    #############################################################################################

    def add_category(self, cat_id, name):
        """add favorite in table"""
        request_sql = "INSERT INTO Categories(c_id, name) VALUES (%s, %s)"
        categorie = (
            cat_id,
            name,
        )
        self.cursor.execute(request_sql, categorie)
        return self.cursor.fetchone()

    def add_product(self, barcode, name, nutriscore, url, market, cat_id):
        """add product in table"""
        request_sql = "INSERT INTO Products(barcode, name, score, url, market, cat_id) VALUES (%s, %s, %s, %s, %s, %s)"
        element = (
            barcode,
            name,
            nutriscore,
            url,
            market,
            cat_id,
        )
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchone()

    def add_favorite(self, fav_id):
        """add favorite in table"""
        request_sql = "INSERT INTO Favorites (fav_id) VALUES (%s)"
        element = (fav_id,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchone()

    #############################################################################################
    #                                        Selecting data                                    #
    #############################################################################################

    def search_favorite(self):
        """ display the favorites """
        search_fav = (
            "SELECT * FROM Products JOIN Favorites ON Products.p_id = Favorites.fav_id"
        )
        self.cursor.execute(search_fav)
        return self.cursor.fetchall()

    def check_favorite(self):
        """check if favorite table is empty"""
        check_fav = "SELECT COUNT(*) FROM Favorites"
        self.cursor.execute(check_fav)
        return self.cursor.fetchone()[0]

    def search_product(self, cat_id):
        """ display the products """
        request_sql = "SELECT * FROM Products WHERE cat_id = (%s)"
        element = (cat_id,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchall()

    def display_products(self, cat_id):
        """ display the products """
        liste = self.search_product(cat_id)
        for i in range(len(liste)):
            print(liste[i][0], ".\t", liste[i][4], "\t", liste[i][2])

    def search_prod_id(self, cat_id):
        """ display the products """
        request_sql = "SELECT p_id FROM Products WHERE cat_id = (%s)"
        element = (cat_id,)
        self.cursor.execute(request_sql, element)
        return self.cursor.fetchall()

    def display_better_product(self, cat_id):
        """ display the products with better nutriscore"""
        request_sql = (
            "SELECT * FROM Products WHERE cat_id = (%s) ORDER BY score ASC LIMIT 15"
        )
        element = (cat_id,)
        self.cursor.execute(request_sql, element)
        liste = self.cursor.fetchall()
        for i in range(len(liste)):
            print(liste[i][0], ".\t", liste[i][4], "\t", liste[i][2])
        return liste

    def display_favorite(self):
        """ diplay the favorites """
        liste = self.search_favorite()
        for i in range(len(liste)):
            print(
                i + 1,
                ".\t",
                liste[i][0],
                "(",
                liste[i][2],
                ")",
                liste[i][4],
                "\n",
                " .\t",
                liste[i][5],
                "\n",
                " .\t",
                "store:",
                "(",
                liste[i][6],
                ")",
            )

    def display_categorie(self):
        """ display the categories """
        display_cat = "SELECT * FROM Categories"
        self.cursor.execute(display_cat)
        liste = self.cursor.fetchall()
        for i in range(len(liste)):
            print(liste[i][0], ".\t", liste[i][1])
