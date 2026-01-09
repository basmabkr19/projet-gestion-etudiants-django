from django.urls import path
from . import views 

urlpatterns = [
    # Page d'accueil qui affiche la liste des étudiants
    path('', views.liste_etudiants, name='liste_etudiants'),
    
    # Page pour ajouter un étudiant 
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    
    # Page pour modifier un étudiant 
    path('modifier/<int:etudiant_id>/', views.modifier_etudiant, name='modifier_etudiant'),
    
    # Page pour supprimer un étudiant 
    path('supprimer/<int:etudiant_id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
]