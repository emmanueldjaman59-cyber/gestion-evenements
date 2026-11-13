from django.urls import path
from . import views


urlpatterns = [

    path('', views.liste_evenements, name='liste_evenements'),

    path('ajouter/', views.ajouter_evenement, name='ajouter_evenement'),

    path('<int:pk>/modifier/', views.modifier_evenement, name='modifier_evenement'),

    path('<int:pk>/supprimer/', views.supprimer_evenement, name='supprimer_evenement'),

    path('<int:pk>/', views.details_evenement, name='details_evenement'),

    path(
    '<int:pk>/inscription/',
    views.inscrire_participant,
    name='inscrire_participant'
),

path(
    '<int:pk>/participants/',
    views.liste_participants,
    name='liste_participants'
),

]