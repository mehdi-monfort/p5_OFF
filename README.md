**-P5-OpenFoodFacts**

Création d'une application python permettant de substituer un produit à un autre grâce à la base de données Open Food Facts.


***Utilisation du dossier***

	Dans /api, à l'aide de virtualenv: Créer un environnement virtuel
	*linux, mac: virtualenv -p python3 env
	*windows(powershell): virtualenv -p $env:python3 env
	Activer l'environnement virtuel :
	*linux, mac: source env/bin/activate
	*windows(powershell): ./env/scripts/activate.ps1*
	cloner le projet depuis https://github.com/mehdi-monfort/p5_OFF
	Installer le requirement.txt :
	*pip install -r requirements.txt
	Ouvrir le fichier avec python:
	*python3 main.py
	L'utilisateur peut modifier le fichier config pour entrer l'identifiant et le mot de passe de la base de données.


***Fonctionnement de l'API***


Une fois le programme lancer:

	1 - création une nouvelle base de données dans laquelle les produits et categorie seront insérer : *Menu principal - Choix 2*
	2 - il sera demander à l'utilisateur de choisir une catégorie parmis celle proposer au hasard depuis l'api d'OpenFoodFact.
	3 - L'utilisateur choisira un produit sur ceux proposés
	4 - L'utilisateur choisira parmis une liste de substitut (les 5 produits avec le nutriscore le plus faible)
	5 - L'utilisateur aura le choix d'enregistrer ou non son substitut
	6 - L'utilisateur aura la possibilité de consulter les produits sauvegarder: Menu *secondaire - Choix 2*


***Cahier des charges***

Parcours utilisateur :

	2 choix: 	- Quel aliment souhaitez-vous remplacer ?
          		- Retrouver mes aliments substitués.?   
	Sélection de la catégorie
	Sélection du produit (description, url, magasin (si existant)
	Sélection du substitut (description, url, magasin (si existant)
	Possibilité d'enregistrer le résultat


Fonctionnalités :

	Recherche d aliments dans la base Open Food Facts.
	L utilisateur interagit avec le programme dans le terminal, possibilité de développer une interface graphique.
	Si l utilisateur entre un caractère qui n est pas un chiffre, le programme doit lui répéter la question.
	La recherche doit s effectuer sur une base MySql.


***Contraintes***

	Votre code sera écrit en anglais : variables, noms de fonctions, commentaires, documentation, ...
	Votre projet sera versionné et publié sur Github pour que votre mentor puisse laisser des commentaires.

