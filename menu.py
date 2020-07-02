from termcolor import colored
from Database.create import database
from SQL.request import Database
from Database.filling import Fill_data
from category import *

def menu_main():
    print(colored("1. Utiliser application", "yellow",))
    print(colored("2. Supression/Création de la base de données", "magenta"))
    print(colored("0. Quitter l'application ", "red"))
    

