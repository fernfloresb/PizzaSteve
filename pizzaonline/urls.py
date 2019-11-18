from django.urls import path, include
from . import views 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('',views.index,name='index'),
    path('pizza',views.pizza, name='pizza'),
    path('registro',views.registro, name='registro'),
    path('carrito',views.carrito, name='carrito'),
] 

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
