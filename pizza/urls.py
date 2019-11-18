
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzaonline/',include('pizzaonline.urls')),
    path('index/',include('pizzaonline.urls')),
    
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


