from django.shortcuts import render, redirect
from .models import Robe
from .forms import RobeForm , ContactForm , ReservationForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def accueil(request):
    robes = Robe.objects.filter(disponible=True)
    return render(request, 'boutique/accueil.html', {'robes': robes})

def nos_robes(request):
    robes = Robe.objects.all()
    return render(request, 'boutique/nos_robes.html', {'robes': robes})

def is_supervisor(user):
    return user.is_staff  # True si l'utilisateur a accès admin

# Page “Ajouter une robe” protégée 
@user_passes_test(is_supervisor, login_url='/login/')  #décorateur
def ajouter_robe(request): 
    if request.method == 'POST':            #la methode d'envoi du formulaire est HTTP POST
        form = RobeForm(request.POST, request.FILES)       # récupérer les données du formulaire
        if form.is_valid():                 #vérifier si les données sont valides
            form.save()                     # sauvegarder dans la base de données
            return redirect('nos_robes')    # aller à la page nos_robes de nouveau pour la nouvelle robe qui vient d'être ajoutée
    else:
        form = RobeForm()                   # Créer un formulaire vide
    return render(request, 'boutique/ajouter_robe.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre dans la base
            return render(request, 'boutique/contact_success.html')  
    else:
        form = ContactForm()

    return render(request, 'boutique/contact.html', {'form': form})


def reserver_robe(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la réservation
            return redirect('reservation_success')  # redirige vers une page de succès
    else:
        form = ReservationForm()

    return render(request, 'boutique/reserver_robe.html', {'form': form})

def reservation_success(request):
    return render(request, 'boutique/reservation_success.html')
