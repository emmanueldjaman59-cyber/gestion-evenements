from django.contrib import admin
from .models import Evenement, Inscription


@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'lieu',
        'date_evenement',
        'heure'
    )

    search_fields = (
        'titre',
        'lieu'
    )

    list_filter = (
        'date_evenement',
        'lieu'
    )

    ordering = ('date_evenement',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):

    list_display = (
        'participant',
        'email',
        'evenement',
        'date_inscription'
    )

    search_fields = (
        'participant',
        'email'
    )

    list_filter = (
        'evenement',
        'date_inscription'
    )