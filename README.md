# TP7_bloc2
Projet TP7 -Bloc 2 : Développement d'une application web et dossier technique du projet API BACKEND SWAGGER TESTS


# Installation

Pour installer les packages, faire `pip install -r "requirements.txt"`

# Lancement du projet

Faire `uvicorn projet.main:app --reload` pour démarrer le projet.
Aller sur  `http://localhost:8000/docs#/` pour consulter l'interface Swagger.

# Documentation

La doc se trouve sur `http://localhost:8000/docs#/`.
Vous trouverez des précisions sous chaque route.

## Fichier .env

Creez un fichier `.env` a la racine du projet suivant ce modele, en remplissant avec vos information de connexion a votre base de donnée
````
DRIVER='DATABASE_DRIVER'
DB_USERNAME='DATABASE_USERNAME'
PASSWORD='DATABASE_PASSWORD'
HOST='DATABASE_HOST'
PORT='DATABASE_PORT'
DATABASE_NAME='DATABASE_NAME'
````