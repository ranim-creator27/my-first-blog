from django import forms        # Importer le module forms de Django
from .models import Robe , Contact , Reservation      # Importer le modèle Robe, contact et reservation

class RobeForm(forms.ModelForm):        #Créer une classe RobeForm qui hérite de ModelForm
    class Meta:                         #Meta = classe spéciale pour définir les options de configuration du formulaire
        model = Robe                    # le formulaire correspond au modéle Robe
        fields = ['nom', 'description', 'prix_location', 'taille', 'couleur', 'image', 'disponible'] #Liste des champs à inclure dans le formulaire

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'sujet', 'message']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date_debut', 'date_fin']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }        
def clean(self):
    cleaned_data = super(ReservationForm, self).clean()
    robe = cleaned_data.get('robe')
    debut = cleaned_data.get('date_debut')
    fin = cleaned_data.get('date_fin')

    if robe and debut and fin:
        # Vérifie si une réservation existe déjà avec exactement ces dates
        exists = Reservation.objects.filter(
            robe=robe,
            date_debut=debut,
            date_fin=fin
        ).exists()
        if exists:
            raise forms.ValidationError("Cette robe est déjà réservée pour ces dates exactes.")        
    return cleaned_data