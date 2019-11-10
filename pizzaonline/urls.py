from django.urls import path
from . import views 

 
urlpatterns = [ 
    path('',views.index,name='index'),
    path('pizza',views.pizza, name='pizza'),
    path('registro',views.registro, name='registro'),
    path('carriyo',views.carrito, name='carrito'),
    
] 

