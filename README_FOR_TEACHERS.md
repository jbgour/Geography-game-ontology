# Projet final du cours de Connaissances et Raisonnement

# Jeu de Géographie Open Source

## Jean-Baptiste Gourlet, Grégoire Gambino, Thibault Monsel

github: https://github.com/jbgour/Geography-game-ontology

*Note préliminaire:* Notre premier souhait était d'utiliser les données issues de EU Open Data Portal. Cependant la
faible documentation du point d'entrée SPARQL ne nous a pas permis d'accéder aux données que nous souhaitions pour notre
application. Le point d'entrée de DBPEDIA a donc été privillégié.

# Comment jouer au jeu?

en local: instructions pour lancer l'app flask dans le fichier *README.md* \
en ligne: version déployée accessible à cette adresse: http://51.255.166.35:5000/ , il est possible que les temps de
latence soient plus longs, sur cette version.

# Documentation

## Vision joueur:

Questions de geographie, choix Duo, Carré, Cash, type de questions:

* Quelle est la capitale de tel pays?
* De quel pays telle ville est-elle la capitale?
* Quelle est la superficie de tel pays?
* Quelle est la monnaie de tel pays?
* Quel est le classement de tel pays en terme de population?

Chaque question rapporte un nombre de points différent.

## Récolte des données :

Utilisation du point d'entrée SPARQL de DBPEDIA.\
Toutes les données sont récupérés par des requêtes SPARQL, on utilise le module Python SPARQLWRAPPER.\
Les requêtes sont dans le fichier *sparql_package/sparql_queries.py*
Elles sont exécutées à chaque démarrage de session
de jeu.\
L'interêt de ce mécanisme est d'être sûr que les données de notre jeu sont au moins aussi à jour que celles de DBPEDIA.\
En effet, des pays peuvent être créés, changer de capitale ou voir leur population évoluer. \
Les mises à jour s'effectuent de manière autonome, sans intervention manuelle nécessaire.

## Création de l'ontologie :

Nous avons souhaité stocker les données du jeu sont forme d'ontologie.\
Pour cela, on utilise le langage de représenation OWL, via le package owlready2.\ L'ontologie est créée dans le
fichier *models/ontology_model.py*\
Exemple: *Country* et *Capital* sont deux classes de l'ontologie. Deux propriétés fonctionnelles sont créées pour les
lier: *is_capital_of* et *has_capital*, l'une étant déclarée comme l'inverse de l'autre. Ainsi, lors de la création de l'objet pays "France"
par exemple, on déclare explicitement "Paris est capitale de France". La relation inverse est inférée automatiquement et nous permet de faire varier la nature des questions posées.

## Fonctionnement de l'application (pattern MVC):

* Model:
    * contient les fichiers d'ontologie(*ontology_model.py*, *get_ontology_data.py*)
    * contient les templates de question(*question.py*)
* Vue:
    * HTML utilisant la logique Jinja,  minimaliste et populé par le routeur dynamiquement.
    * routage effectué à la racine *app.py*
* Controller:
    * orchestrateur dans *game_session.py*



