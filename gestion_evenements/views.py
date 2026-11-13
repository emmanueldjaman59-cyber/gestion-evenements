from django.shortcuts import render, redirect, get_object_or_404

from .models import Evenement, Inscription
from .forms import EvenementForm, InscriptionForm


# Afficher la liste des événements
def liste_evenements(request):

    evenements = Evenement.objects.all()

    return render(
        request,
        'gestion_evenements/liste_evenements.html',
        {'evenements': evenements}
    )


# Ajouter un événement
def ajouter_evenement(request):

    if request.method == 'POST':

        form = EvenementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('liste_evenements')

    else:
        form = EvenementForm()

    return render(
        request,
        'gestion_evenements/formulaire_evenement.html',
        {'form': form}
    )


# Modifier un événement
def modifier_evenement(request, pk):

    evenement = get_object_or_404(Evenement, pk=pk)

    if request.method == 'POST':

        form = EvenementForm(request.POST, instance=evenement)

        if form.is_valid():
            form.save()
            return redirect('liste_evenements')

    else:
        form = EvenementForm(instance=evenement)

    return render(
        request,
        'gestion_evenements/formulaire_evenement.html',
        {'form': form}
    )


# Supprimer un événement
def supprimer_evenement(request, pk):

    evenement = get_object_or_404(Evenement, pk=pk)

    if request.method == 'POST':
        evenement.delete()
        return redirect('liste_evenements')

    return render(
        request,
        'gestion_evenements/confirmer_suppression.html',
        {'evenement': evenement}
    )
# Afficher les détails d'un événement
def details_evenement(request, pk):

    evenement = get_object_or_404(Evenement, pk=pk)

    return render(
        request,
        'gestion_evenements/details_evenement.html',
        {'evenement': evenement}
    )

def inscrire_participant(request, pk):

    evenement = get_object_or_404(Evenement, pk=pk)

    if request.method == 'POST':

        form = InscriptionForm(request.POST)

        if form.is_valid():

            inscription = form.save(commit=False)
            inscription.evenement = evenement

            # Vérifier si l'e-mail est déjà inscrit à cet événement
            deja_inscrit = Inscription.objects.filter(
                email=inscription.email,
                evenement=evenement
            ).exists()

            if deja_inscrit:
                form.add_error(
                    'email',
                    "Cette adresse e-mail est déjà inscrite à cet événement."
                )
            else:
                inscription.save()
                return redirect('liste_evenements')

    else:
        form = InscriptionForm()

    return render(
        request,
        'gestion_evenements/formulaire_inscription.html',
        {
            'form': form,
            'evenement': evenement
        }
    )

def liste_participants(request, pk):

    evenement = get_object_or_404(Evenement, pk=pk)

    participants = Inscription.objects.filter(
        evenement=evenement
    ).order_by('-date_inscription')

    return render(
        request,
        'gestion_evenements/liste_participants.html',
        {
            'evenement': evenement,
            'participants': participants
        }
    )