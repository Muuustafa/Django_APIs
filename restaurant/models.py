from uuid import uuid4

from django.db import models


# Create your models here.

class Client(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=11, null=True)
    email = models.EmailField(blank=True)


class Commande(models.Model):
    numero = models.UUIDField(default=uuid4)
    client = models.ForeignKey(Client, related_name='commandes', on_delete=models.CASCADE)


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)


class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    fournisseur = models.ForeignKey(Fournisseur, related_name='produits', on_delete=models.CASCADE)


class Menu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    commande = models.ManyToManyField(Commande)
