from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Etudiant
from .forms import EtudiantForm

@login_required  
def liste_etudiants(request):
    
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
    return render(request, 'etudiants/liste_etudiants.html', context)

@login_required  
def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/ajouter_etudiant.html', {'form': form})

@login_required  
def modifier_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier_etudiant.html', {'form': form})


@login_required  
def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'etudiants/supprimer_etudiant.html', {'etudiant': etudiant})