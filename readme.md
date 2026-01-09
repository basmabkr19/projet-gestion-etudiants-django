Projet de Gestion des Étudiants :

Une application web moderne et sécurisée développée avec le framework Django. Ce projet permet de gérer efficacement une liste d'étudiants en offrant toutes les fonctionnalités de base (CRUD) et une interface utilisateur soignée.

Fonctionnalités :

Authentification Sécurisée : Une page de connexion protège l'accès à l'application.
Liste Complète : Affiche tous les étudiants enregistrés avec leurs informations clés.
Ajout d'Étudiant : Formulaire simple pour ajouter un nouvel étudiant à la base de données.
Modification d'Étudiant : Met à jour les informations d'un étudiant existant.
Suppression d'Étudiant : Supprime un étudiant de la liste après confirmation.
Interface Intuitive : Design épuré et responsive grâce à du CSS personnalisé.
Technologies Utilisées
Backend :Python, Django
Frontend : HTML5, CSS3
Base de Données : SQLite

Comment Lancer le Projet :

Pour exécuter ce projet localement, suivez ces étapes simples :

1-Cloner le dépôt :
git clone https://github.com/basmabkr19/projet-gestion-etudiants-django.gitcd projet-gestion-etudiants-django

2-Créer et activer un environnement virtuel
# Sur Windowspython -m venv envenv\Scripts\activate# Sur macOS / Linuxpython3 -m venv envsource env/bin/activate

3-Installer les dépendances :
pip install django

4-Appliquer les migrations de la base de données :
Cette commande prépare la base de données en créant toutes les tables nécessaires.
python manage.py migrate

5-Créer un utilisateur pour la démonstration :
Créez un compte pour pouvoir vous connecter à l'application.
python manage.py createsuperuser
Suivez les instructions pour définir un nom d'utilisateur, un email et un mot de passe.

6-Lancer le serveur de développement :
python manage.py runserver

7-Accéder à l'applicationOuvrez votre navigateur web et naviguez vers l'adresse http://127.0.0.1:8000/. Vous serez automatiquement redirigé vers la page de connexion.

🔑 Accès pour la Démonstration :
Pour faciliter l'évaluation, vous pouvez utiliser les identifiants suivants pour vous connecter directement :

Nom d'utilisateur : basma
Mot de passe : python2025
Note de sécurité : Ces identifiants sont fournis exclusivement pour la correction de ce projet pédagogique. Dans un contexte de production, de telles informations ne seraient jamais communiquées publiquement.

👤 Auteur
Projet réalisé par Basma Bakar dans le cadre d'une formation en programmation avancée.