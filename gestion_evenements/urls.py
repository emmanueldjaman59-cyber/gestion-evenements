from django.urls import path
from . import views


urlpatterns = [

    path('', views.liste_evenements, name='liste_evenements'),

    path('ajouter/', views.ajouter_evenement, name='ajouter_evenement'),

    path(
        '<int:pk>/modifier/',
        views.modifier_evenement,
        name='modifier_evenement'
    ),

    path(
        '<int:pk>/supprimer/',
        views.supprimer_evenement,
        name='supprimer_evenement'
    ),

]