from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

#Clase Ingredientes
class Ingredients (models.Model):
    ingredientName = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredientName


#tamaño pizzas
class Size (models.Model):
    sizeName = models.CharField(max_length=200)
    def __str__(self):
        return self.sizeName


#Clase Pizzas
class Pizza (models.Model):
    pizzaName = models.CharField(max_length=200)
    ingredient = models.ManyToManyField(Ingredients)
    size = models.ManyToManyField(Size)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.pizzaName

#Clase Locales
class Store (models.Model):
    localName = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    phoneNumber = models.IntegerField()
    def __str__(self):
        return self.localName





