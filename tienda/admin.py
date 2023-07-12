from django.contrib import admin
from tienda.models import *

class VideojuegoAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Genero)
admin.site.register(Estudio)
admin.site.register(PEGI)
admin.site.register(ESBR)


admin.site.register(Noticia)


admin.site.register(Compra)