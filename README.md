**-P5-OpenFoodFacts**

Creation of a python application allowing to substitute one product for another thanks to the Open Food Facts database

===============================================================================================================

**Contexte**

La startup Pur Beurre travaille connait bien les habitudes alimentaires françaises. Leur restaurant, Ratatouille, remporte un 
succès croissant et attire toujours plus de visiteurs sur la butte de Montmartre.

L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer. 
Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ? Leur idée est donc de 
créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à 
l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

===============================================================================================================

**Cahier des charges**

---------------------------------------------------------------------------------------------------------------

**Parcours utilisateur**

*2 choix:  - Quel aliment souhaitez-vous remplacer ?
          - Retrouver mes aliments substitués.*

*Sélection de la catégorie*
*Sélection du produit (description, url, magasin (si existant)*
*Sélection du substitut (description, url, magasin (si existant)*
*Possibilité d'enregistrer le résultat*

---------------------------------------------------------------------------------------------------------------

<h2>Fonctionnalités</h2>

<li Recherche d aliments dans la base Open Food Facts.></li>
<li L utilisateur interagit avec le programme dans le terminal, possibilité de développer une interface graphique.></li>
<li Si l utilisateur entre un caractère qui n est pas un chiffre, le programme doit lui répéter la question.></li>
<li La recherche doit s effectuer sur une base MySql.></li>

---------------------------------------------------------------------------------------------------------------

<h2>Étapes de travail</h2>

<h3>Organisation</h3>
<li Création du README ></li>
<li Création dun Tableau Agile></li>

<h3>Construction de la base de donnée</h3>
<li Faire un Modèle Physique de Données></li>
<li Récupérer les données depuis la base OpenFoodFacts au format JSON></li>
<li Créer un script Python qui insérera les données dans la base></li>

<h3>Construction du programme</h3>
<li Lister les fonctionnalitées de chaque classe></li>
<li Créer l architecture du programme></li>

<h3>Interaction programme-base de données</h3>
<li Travailler le question/Réponse></li>
<li Quels requêtes pour quelle(s) Table(s)></li>
<li Comment enregistrer les requêtes></li>

===============================================================================================================

<h2>Livrable</h2>

<li Modèle physique de données ou Modèle relationnelle. ></li>
<li Script de création de votre base de données ></li>
<li Code source publié sur Github ></li>
<li Tableau Trello, Taiga ou Pivotal Tracker. ></li>
<li Document texte expliquant la démarche choisie, les difficultés rencontrées et les solutions trouvées et incluant le lien vers votre code source sur Github. ></li>
<li Développez notamment le choix de l algorithme et la méthodologie de projet choisie. ></li>
<li Expliquez également les difficultés rencontrées et les solutions trouvées. ></li>
<li Le document doit être en format pdf et ne pas excéder 2 pages A4. ></li>
<li Il peut être rédigé en anglais ou en français, au choix, mais prenez bien en considération que les fautes d’orthographe et de grammaire seront évaluées ! ></li>

===============================================================================================================

<h2 Contraintes** ></h2>

<li Votre code sera écrit en anglais : variables, noms de fonctions, commentaires, documentation, ...></li>
<li Votre projet sera versionné et publié sur Github pour que votre mentor puisse laisser des commentaires.></li>
 
===============================================================================================================
