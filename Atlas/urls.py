from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404
from usuarios.views import error_404_view

handler404 = 'usuarios.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('tienda.urls')),
    path("", include('usuarios.urls'))
]
