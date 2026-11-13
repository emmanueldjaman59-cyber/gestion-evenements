from django import forms
from django.utils import timezone
from .models import Evenement


class EvenementForm(forms.ModelForm):

    class Meta:
        model = Evenement

        fields = [
        'titre',
        'description',
        'lieu',
        'date_evenement',
        'heure'
    ]

        widgets = {
        'date_evenement': forms.DateInput(attrs={'type': 'date'}),
        'heure': forms.TimeInput(attrs={'type': 'time'})
    }

def clean_titre(self):
    titre = self.cleaned_data.get('titre')

    if len(titre.strip()) < 3:
        raise forms.ValidationError(
            "Le titre doit contenir au moins 3 caractères."
        )

    return titre

def clean_lieu(self):
    lieu = self.cleaned_data.get('lieu')

    if not lieu.strip():
        raise forms.ValidationError(
            "Veuillez renseigner le lieu de l'événement."
        )

    return lieu

def clean_date_evenement(self):
    date = self.cleaned_data.get('date_evenement')

    if date < timezone.localdate():
        raise forms.ValidationError(
            "La date de l'événement ne peut pas être dans le passé."
        )

    return date

from .models import Inscription


class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription

        fields = [
            'participant',
            'email'
        ]

        widgets = {
            'participant': forms.TextInput(attrs={
                'placeholder': 'Entrez votre nom complet'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Entrez votre adresse e-mail'
            })
        }