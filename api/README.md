<h1>-P5-OpenFoodFacts</h1>

<hr />
Création d'une application python permettant de substituer un produit à un autre grâce à la base de données Open Food Facts.
<hr />

<h2>Utilisation du dossier</h2>
<ul>
<li>Dans /api, à l'aide de virtualenv: Créer un environnement virtuel </li>
<li>linux, mac: virtualenv -p python3 env</li>
<li>windows(powershell): virtualenv -p $env:python3 env</li>
<li>Activer l'environnement virtuel</li>
<li>linux, mac: source env/bin/activate</li>
<li>windows(powershell): ./env/scripts/activate.ps1</li>
<li>cloner le projet depuis https://github.com/mehdi-monfort/p5_OFF</li>
<li>Installer le requirement.txt pip install -r requirements.txt</li>
<li>Ouvre le fichier avec python: python3 main.py</li>
<li>L'utilisateur peut modifier le fichier config pour entrer l'identifiant et le mot de passe de la base de données.</li>
</ul>

<hr />

<h2>Fonctionnement de l'API</h2>

<ul>

<li>	Une fois le programme lancer:</li>
<li>	1 - création une nouvelle base de données dans laquelle les produits et categorie seront insérer : Menu principal - Choix 2</li>
<li>	2 - il sera demander à l'utilisateur de choisir une catégorie parmis celle proposer au hasard depuis l'api d'OpenFoodFact.</li>
<li>	3 - L'utilisateur choisira un produit sur ceux proposés</li>
<li>	4 - L'utilisateur choisira parmis une liste de substitut (les 5 produits avec le nutriscore le plus faible)</li>
<li>	5 - L'utilisateur aura le choix d'enregistrer ou non son substitut</li>
<li>	6 - L'utilisateur aura la possibilité de consulter les produits sauvegarder: Menu secondaire - Choix 2</li>
</ul>

<hr />

<h2>Cahier des charges</h2>

<h3>Parcours utilisateur</h3>
<ul>
<li>2 choix:<br /> - Quel aliment souhaitez-vous remplacer ?<br />
          	- Retrouver mes aliments substitués.?</li><br />
          
<li>Sélection de la catégorie</li>
<li>Sélection du produit (description, url, magasin (si existant)</li>
<li>Sélection du substitut (description, url, magasin (si existant)</li>
<li>Possibilité d'enregistrer le résultat</li>
</ul>

<h3>Fonctionnalités</h3>
<ul>
<li>Recherche d aliments dans la base Open Food Facts.</li>
<li>L utilisateur interagit avec le programme dans le terminal, possibilité de développer une interface graphique.</li>
<li>Si l utilisateur entre un caractère qui n est pas un chiffre, le programme doit lui répéter la question.</li>
<li>La recherche doit s effectuer sur une base MySql.</li>
</ul>

<h3>Contraintes</h3>
<ul>
<li>Votre code sera écrit en anglais : variables, noms de fonctions, commentaires, documentation, ...</li>
<li>Votre projet sera versionné et publié sur Github pour que votre mentor puisse laisser des commentaires.</li>
</ul>
