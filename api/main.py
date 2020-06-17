from termcolor import colored
from Database.create import database
from SQL.request import Database
from Database.filling import Fill_data


def main():
    """set up attributes"""
    main_menu = True
    api_menu = False
    save_menu = False
    sub_menu = False
    prod_menu = False
    cat_menu = False
    data = Database()
    green_line = colored("-------------------------------------------------", "green")
    red_line = colored("-------------------------------------------------", "red")
    touch_error = colored("Attention: Pour faire une sélection. Tapez son numéro", "red")

    while main_menu:
        print(green_line)
        print(colored("1. Utiliser application", "yellow",))
        print(colored("2. Supression/Création de la base de données", "magenta"))
        print(colored("0. Quitter l'application ", "red"))
        print(green_line)
        choice_main = input(colored("\n ---> ", "green"))
        print(green_line)
        try:
            choice_main = int(choice_main)
        except ValueError:
            choice_main = -1
        if choice_main == 1:
            api_menu = True
        elif choice_main == 2:
            database()
            print(green_line)
            print("Waiting, request in progress ...")
            req = Fill_data()
            req.make_request(data)
            print(green_line)
            print("Request complete.")
            print(green_line)
        elif choice_main == 0:
            main_menu = False
        else:
            print(touch_error)
        while api_menu:
            print(colored("1. Menu application", "yellow"))
            print(colored("2. Afficher sauvegarde", "yellow"))
            print(colored("0. Quitter le programme", "red"))
            print(green_line)
            choice_api = input(colored("\n ---> ", "green"))
            print(green_line)
            try:
                choice_api = int(choice_api)
            except ValueError:
                choice_api = -1
            if choice_api == 1:
                api_menu = False
                cat_menu = True
            elif choice_api == 2:
                check = data.check_favorite()
                if check == 0:
                    print(colored("*.backup is empty", "yellow"))
                else:
                    data.display_favorite()
                    print(green_line)
            elif choice_api == 0:
                main_menu = False
                api_menu = False
            else:
                print(touch_error)
        while cat_menu:
            data.display_categorie()
            print(colored("Choix de la catégorie", "yellow"))
            choice_cat = input(colored("\n ---> ", "green"))
            data.display_products(choice_cat)
            try:
                choice_cat = int(choice_cat)
            except ValueError:
                choice_cat = -1
            if choice_cat >= 1 and choice_cat <= 5:
                cat_menu = False
                prod_menu = True
            else:
                print(touch_error)
        while prod_menu:
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
                print(red_line)
                print(touch_error)
                print(red_line)
        while sub_menu:
            print(colored("Choix d'un substitut", "yellow"))
            choice_sub = input(colored("\n ---> ", "green"))
            try:
                choice_sub = int(choice_sub)
            except ValueError:
                choice_sub = -1
            if choice_sub in liste_id:
                sub_menu = False
                save_menu = True
            else:
                print(touch_error)
        while save_menu:
            print(colored("Voulez-vous sauvegarder: 1(Oui) 2(Non)", "yellow"))
            choice_save = input(colored("\n ---> ", "green"))
            try:
                choice_save = int(choice_save)
            except ValueError:
                choice_save = -1
            if choice_save == 1:
                try:
                    data.add_favorite(choice_sub,)
                    print(red_line)
                    print(colored("favoris enregistrer", "green"))
                    print(red_line)
                except Exception:
                    print(red_line)
                    print(colored("Le favoris est déjà enregistrer", "yellow"))
                    print(red_line)
                save_menu = False
            elif choice_save == 2:
                save_menu = False
            else:
                print(colored("perdu", "red"))
                print(colored("reessayez", "green"))


if __name__ == "__main__":
    main()
