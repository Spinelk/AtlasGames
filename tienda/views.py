from django.shortcuts import render, get_object_or_404
from tienda.models import Videojuego
from tienda.models import Noticia
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'index.html', {'videojuegos': videojuegos})

@login_required
def juego(request, slug):
    videojuegos = Videojuego.objects.all()
    videojuego = get_object_or_404(Videojuego, slug=slug)
    return render(request, 'juego.html', {'videojuego': videojuego, 'videojuegos': videojuegos})


@login_required
def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})



def error_404_view(request, exception):
    return render(request, '404.html', status=404)


    
@login_required
def inicio_sesion(request):
    return render(request, 'usuarios/inicioSesion.html')

@login_required
def registro(request):
    return render(request, 'usuarios/registro.html')

