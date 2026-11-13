from django.shortcuts import render, redirect, get_object_or_404

from .models import Evenement
from .forms import EvenementForm


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