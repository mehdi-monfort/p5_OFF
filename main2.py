from termcolor import colored
from Database.create import database
from SQL.database import Database
from category import *
from product import *
from menu import *
import mysql


def main():
    """set up attributes"""
    api_menu = False
    save_menu = False
    sub_menu = False
    prod_menu = False
    cat_menu = False
    create_data = False
    main_menu = True
    id_product = []
    data = Database()
    display = Display()

    while main_menu:
        choice = display.menu1()
        if choice == "1":
            choice2 = display.menu2()
            if choice2 == "1":
                for categorie in range(4):
                    data.display_categorie()
                    print(colored("Choix de la catégorie", "yellow"))
                    choice_cat = input(colored("\n ---> ", "green"))
                    try:
                        choice_cat = int(choice_cat)
                    except ValueError:
                        choice_cat = -1
                    if 5 >= choice_cat >= 1:
                        nb_product = data.display_products(choice_cat)
                        print(colored("Choix d'un produit", "yellow"))
                        choice_prod = input(colored("\n ---> ", "green"))
                        try:
                            choice_prod = int(choice_prod)
                        except ValueError:
                            choice_prod = -1
                        if choice_prod <= nb_product:
                            nb_substitut = data.display_better_products(choice_cat)
                            print(colored("Choix d'un substitut", "yellow"))
                            choice_sub = input(colored("\n ---> ", "green"))
                            try:
                                choice_sub = int(choice_sub)
                            except ValueError:
                                choice_sub = -1
                            if choice_sub <= nb_substitut:
                                print(
                                    colored(
                                        "Voulez-vous sauvegarder: 1(Oui) 2(Non)",
                                        "yellow",
                                    )
                                )
                                choice_save = input(colored("\n ---> ", "green"))
                                try:
                                    choice_save = int(choice_save)
                                except ValueError:
                                    choice_save = -1
                                if choice_save == 1:
                                    print(choice_sub,)
                                    try:
                                        data.add_favorite(choice_sub,)
                                        print(colored("favoris enregistrer", "green"))
                                    except mysql.connector.errors.IntegrityError as err:
                                        print(
                                            colored(
                                                "Le favoris est déjà enregistrer",
                                                "yellow",
                                            )
                                        )
                                        print(err)
                                        break
                                elif choice_save == 2:
                                    break
                                else:
                                    print(colored("perdu", "red"))
                                    print(colored("reessayez", "green"))
                            elif choice_sub > nb_substitut:
                                print(touch_error)
                        else:
                            print("touch_error")
                    else:
                        print("touch_error")
            elif choice2 == "2":
                check = data.check_favorite()
                if check == 0:
                    print(colored("*.backup is empty", "yellow"))
                else:
                    data.display_favorite()
            elif choice2 == "0":
                break
            else:
                print("touch_error")
        elif choice == "2":
            database()
            print("Waiting, request in progress ...")
            for categorie in range(3):
                category = Category.get_categories(categorie)
                data.add_category(category)
                print(category)
                for i in range(19):
                    product = Product.get_products(category, i + 1)
                    if product != None:
                        data.add_product(
                            product["barcode"],
                            product["name"],
                            (product["nutriscore"]).upper(),
                            product["url"],
                            product["market"],
                        )
            data.add_relation()
            print("Request complete.")
        elif choice == "0":
            break
        else:
            print("touch_error")


if __name__ == "__main__":
    main()
