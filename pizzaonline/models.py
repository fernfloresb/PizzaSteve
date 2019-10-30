from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

#Clase Ingredientes
class Ingredients (models.Model)
        ingredientName = models.Charfield(max_length=200)

    def __str__(self):
        return self.ingredientName

#Clase Pizzas
class Pizza (models.Model)
    pizzaName = models.Charfield(max_length=200)
    ingredient = models.ManyToManyField(Ingredients)
    price = models.IntegerField(max_length=5)

    def __str__(self):
        return self.pizzaName

#Clase Locales
class store (models.Model)
    localName = models.Charfield(max_length=200)
    adress = models.Charfield(max_length=200)
    phoneNumber = models.IntegerField(max_length=12)

    def __str__(self):
        return self.localName





