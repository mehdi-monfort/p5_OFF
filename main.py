from termcolor import colored
from Database.create import database
from SQL.database import Database
from category import *
from product import *
from menu import *


def main():
    """set up attributes"""
    api_menu = False
    save_menu = False
    sub_menu = False
    prod_menu = False
    cat_menu = False
    create_data = False
    main_menu = True
    categorie = []
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
                        data.display_products(choice_cat)
                        print(colored("Choix d'un produit", "yellow"))
                        choice_prod = input(colored("\n ---> ", "green"))
                        try:
                            choice_prod = int(choice_prod)
                        except ValueError:
                            choice_prod = -1
                        select_prod = (choice_prod,)
                        if select_prod in data.search_prod_id(choice_cat):
                            liste = data.display_better_product(choice_cat)
                            liste_id = [liste[i][0] for i in range(len(liste))]

                            prod_menu = False
                            sub_menu = True
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
                    product = Product.get_products(category, i+1)
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
        elif choice =="0":
            break
        else:
            print("touch_error")

        #     while cat_menu:

        #     while prod_menu:
        #         print(colored("Choix d'un produit", "yellow"))
        #         choice_prod = input(colored("\n ---> ", "green"))
        #         try:
        #             choice_prod = int(choice_prod)
        #         except ValueError:
        #             choice_prod = -1
        #         select_prod = (choice_prod,)
        #         if select_prod in data.search_prod_id(choice_cat):
        #             liste = data.display_better_product(choice_cat)
        #             liste_id = [liste[i][0] for i in range(len(liste))]

        #             prod_menu = False
        #             sub_menu = True
        #         else:
        #             print(red_line)
        #             print(touch_error)
        #             print(red_line)
        #     while sub_menu:
        #         print(colored("Choix d'un substitut", "yellow"))
        #         choice_sub = input(colored("\n ---> ", "green"))
        #         try:
        #             choice_sub = int(choice_sub)
        #         except ValueError:
        #             choice_sub = -1
        #         if choice_sub in liste_id:
        #             sub_menu = False
        #             save_menu = True
        #         else:
        #             print(touch_error)
        #     while save_menu:
        #         print(colored("Voulez-vous sauvegarder: 1(Oui) 2(Non)", "yellow"))
        #         choice_save = input(colored("\n ---> ", "green"))
        #         try:
        #             choice_save = int(choice_save)
        #         except ValueError:
        #             choice_save = -1
        #         if choice_save == 1:
                # try:
                #     favorite.add_favorite(choice_sub,)
                #     print(red_line)
                #     print(colored("favoris enregistrer", "green"))
                #     print(red_line)
                # except mysql.connector.errors.IntegrityError as err:
                #     print(red_line)
                #     print(colored("Le favoris est déjà enregistrer", "yellow"))
                #     print(err)
                #     print(red_line)
        #             save_menu = False
        #         elif choice_save == 2:
        #             save_menu = False
        #         else:
        #             print(colored("perdu", "red"))
        #             print(colored("reessayez", "green"))


if __name__ == "__main__":
    main()
