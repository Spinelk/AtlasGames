from django.urls import path
from .views import *


#Esto junto con la linea despues de 'urlpatterns' funcionan para cargar las imagenes en el html
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("noticias", noticias, name="noticias"),
    path("iniciosesion", inicio_sesion, name="iniciosesion"),
    path("registro", registro, name="registro"),
    path("videojuego/<slug:slug>/", juego, name="registro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
