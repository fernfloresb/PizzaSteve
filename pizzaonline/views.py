from django.shortcuts import render
from .models import Pizza,Ingredients,Store,Size
from django.views import generic
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render (request,'index.html')
def pizza (request):
    pizzas = Pizza.objects.all()

    return render (request,'pizza.html', {'pizzas': pizzas})
def registro (request):
    return render (request,'registro.html')
def carrito (request):
    return render(request,'carrito.html')
