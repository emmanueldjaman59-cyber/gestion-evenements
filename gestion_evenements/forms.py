from django import forms
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
            'date_evenement': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'heure': forms.TimeInput(
                attrs={'type': 'time'}
            )
        }