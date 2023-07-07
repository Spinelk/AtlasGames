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
    path("<slug:slug>/", juego, name="registro"),

    
    # path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('tienda/', tienda, name='tienda'),
    path('tienda/videojuego/<int:videojuego_id>/', detalle_producto, name='detalle_producto'),
    # Agrega más URL según tus necesidades
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
