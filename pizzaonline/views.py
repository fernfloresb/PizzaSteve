from django.shortcuts import render
from .models import Pizza,Ingredients,Store,Size
from django.views import generic


# Create your views here.
def index(request):
    return render (request,'pizzaonline/index.html')
def pizza (request):
    return render (request,'pizzaonline/pizza.html')
