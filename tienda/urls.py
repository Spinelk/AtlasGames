from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("noticias", noticias, name="noticias"),
    path("iniciosesion", inicio_sesion, name="iniciosesion"),
    path("registro", registro, name="registro"),
    path("juego", juego, name="juego"),
]
