from django.urls import path
from .views import *


#Esto junto con la linea despues de 'urlpatterns' funcionan para cargar las imagenes en el html
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tienda'

urlpatterns = [
    path("explora", index, name="index"),
    path("videojuego/<slug:slug>/", juego, name="registro"),

    path("noticias", noticias, name="noticias"),
    path("biblioteca", biblioteca, name="biblioteca"),

    path('compra/', generar_compra, name='compra'),

    path('guardar_carrito_en_servidor/', guardar_carrito_en_servidor, name='guardar_carrito_en_servidor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
