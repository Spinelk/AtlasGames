from django.contrib import admin
from tienda.models import *

admin.site.register(Categoria)
admin.site.register(Videojuego)
admin.site.register(Usuario)

admin.site.register(Noticia)