# Vision joueur:

Question de geographie, choix Duo, Carré, Cash, type de questions:
* Quelle est la capitale de tel pays?
* Nom de famille du president?
* Combien d'habitants (fourchette)?
* De quel pays telle ville est-elle la capitale?

Une vue départ du jeu
Puis rentre sur une page, défilement de questions. on voit la question, on reponds, on a la réponse.
Au bout de 10 questions, le jeu est fini, on donne le score.
On peut rejouer

# Dans le back:
Les questions sont sous formes de template: exemple quel est la capitale de str(countrie)?
A chaque load du jeu, on va demander via sparql de récupérer:
* la liste des pays de l'onu
* leur capitale
* leur population
* leur président
* order by nombre d'habitants (on suppose que pour les petits pays, les questions sont plus dificiles...)

On créé tout ça au sein d'une ontologie.
Justification de pourquoi on stocke rien en dur: ce sont des datas qui sont évolutives!


# Fonctionnement du jeu:
pattern MVC:
* Model: 
  * contient la classe country et ses attributs
  * contient les templates de question (une super classe et des sous classes)
* Vue:
  * simple code html qui display la question et les choix
* Controller:
  * partie tricky: capte les choix du user, son nom, où il en est et va taper dans les modèles



