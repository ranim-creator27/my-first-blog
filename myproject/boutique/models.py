from django.db import models

class Robe(models.Model):       #déclaration du modéle
    TAILLES = [                 #choix du taille
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    nom = models.CharField(max_length=200) #texte court (max 200 caractéres)
    description = models.TextField() #texte long pour décrire la robe
    prix_location = models.DecimalField(max_digits=10, decimal_places=2) #prix de location (max 10 chiffres et 2 chiffres aprés la virgule)
    taille = models.CharField(max_length=2, choices=TAILLES) #stocker les choix de la taille xs,s,m,l,xl
    couleur = models.CharField(max_length=50)
    image = models.ImageField(upload_to='robes/', blank=True)
    disponible = models.BooleanField(default=True) #disponibilité de la robe vrai/faux
    date_ajout = models.DateTimeField(auto_now_add=True) #enregistrer la date exactement au moment où la robe est créée (date ajout automatique).
    
    def __str__(self):
        return self.nom    # afficher le nom du modéle dans la base
    
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.nom} - {self.sujet}"

class Reservation(models.Model):
     robe = models.ForeignKey(Robe, on_delete=models.CASCADE, null=True, blank=True)  # la robe réservée
     date_debut = models.DateField()  # Date de début de la réservation
     date_fin = models.DateField()    # Date de fin de la réservation

def __str__(self):
    return f"Réservation du {self.date_debut} au {self.date_fin}"


