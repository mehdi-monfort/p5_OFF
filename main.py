import mysql
from termcolor import colored
from Database.create import database
from SQL.database import Database
from product import Product
from category import Category

def main():

    init = Main()
    init.main_menu()

class Main:

    def __init__(self):
        """set up attributes"""
        self.green_line = colored("---------------------------------------------", "green")
        self.red_line = colored("---------------------------------------------", "red")
        self.touch_error = colored("¨Pour faire une sélection. Tapez son numéro¨", "red")
        self.database = Database()
        self.cat = 0
        self.sub = 0

    def main_menu(self):
        print(self.green_line)
        print(colored("1. Utiliser application", "yellow",))
        print(colored("2. Supression/Création de la base de données", "magenta"))
        print(colored("0. Quitter l'application ", "red"))
        print(self.green_line)
        choice_main = input(colored("\n ---> ", "green"))
        try:
            choice_main = int(choice_main)
        except ValueError:
            choice_main = -1
        if choice_main == 1:
            self.api_menu()
        elif choice_main == 2:
            database()
            print("Waiting, request in progress ...")
            for categorie in range(5):
                category = Category.get_categories(categorie)
                self.database.add_category(category)
                print(category)
                for i in range(19):
                    product = Product.get_products(category, i+1)
                    if product is not None:
                        self.database.add_product(
                            product["barcode"],
                            product["name"],
                            (product["nutriscore"]).upper(),
                            product["url"],
                            product["market"],
                            )
            self.database.add_relation()
            print("Request complete.")
            self.main_menu()
        elif choice_main == 0:
            self.bye()
        else:
            print(self.touch_error)
            self.main_menu()

    def api_menu(self):
        print(self.green_line)
        print(colored("1. Choix d'une catégorie", "yellow"))
        print(colored("2. Afficher sauvegarde", "yellow"))
        print(colored("0. Quitter le programme", "red"))
        print(self.green_line)
        choice_api = input(colored("\n ---> ", "green"))
        print(self.green_line)
        try:
            choice_api = int(choice_api)
        except ValueError:
            choice_api = -1
        if choice_api == 1:
            self.cat_menu()
        elif choice_api == 2:
            check = self.database.check_favorite()
            if check == 0:
                print(colored("*.backup is empty", "yellow"))
                print(self.green_line)
                self.api_menu()
            else:
                self.database.display_favorite()
                print(self.green_line)
                self.api_menu()
        elif choice_api == 0:
            self.bye()
        else:
            print(self.touch_error)
            self.api_menu()

    def cat_menu(self):
        self.database.display_categorie()
        print(self.green_line)
        print(colored("Choix de la catégorie", "yellow"))
        cat = input(colored("\n ---> ", "green"))
        try:
            cat = int(cat)
        except ValueError:
            cat = -1
        self.prod_menu(cat)

    def prod_menu(self, cat):
        if 1 <= cat <= 5:
            nb_product = self.database.display_products(cat)
            print(colored("Choix d'un produit", "yellow"))
            choice_prod = input(colored("\n ---> ", "green"))
            try:
                choice_prod = int(choice_prod)
            except ValueError:
                choice_prod = -1
            if choice_prod <= nb_product:
                self.sub_menu(cat)
            else:
                print(self.red_line)
                print(self.touch_error)
                print(self.red_line)
                self.prod_menu()
        else:
            print(self.touch_error)
            self.prod_menu()

    def sub_menu(self, cat):
        nb_substitut = self.database.display_better_products(cat)
        print(colored("Choix d'un substitut", "yellow"))
        sub = input(colored("\n ---> ", "green"))
        try:
            sub = int(sub)
        except ValueError:
            sub = -1
        if sub <= nb_substitut:
            self.save_menu(cat, sub)
        else:
            print(self.touch_error)
            self.sub_menu()

    def save_menu(self, cat, sub):
        self.database.display_better_products(cat)
        print(colored("Voulez-vous sauvegarder: 1(Oui) 2(Non)", "yellow"))
        choice_save = input(colored("\n ---> ", "green"))
        try:
            choice_save = int(choice_save)
        except ValueError:
            choice_save = -1
        if choice_save == 1:
            try:
                self.database.save_favorite(cat, sub)
                print(self.red_line)
                print(colored("favoris enregistrer", "green"))
                print(self.red_line)
                self.main_menu()
            except mysql.connector.errors.IntegrityError:
                print(self.red_line)
                print(colored("Le favoris est déjà enregistrer", "yellow"))
                print(self.red_line)
                self.main_menu()
        elif choice_save == 2:
            self.main_menu()
        else:
            print(colored("perdu", "red"))
            print(colored("reessayez", "green"))

    def bye():
        print(colored("Au revoir !", "blue"))
        quit()


if __name__ == "__main__":
    main()
