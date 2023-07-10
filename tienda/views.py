from django.shortcuts import render, get_object_or_404
from tienda.models import Videojuego
from tienda.models import Noticia
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    username = request.user.username

    videojuegos = Videojuego.objects.all()
    
    return render(request, 'index.html', {'videojuegos': videojuegos,'username': username})

@login_required
def juego(request, slug):
    username = request.user.username

    videojuegos = Videojuego.objects.all()
    videojuego = get_object_or_404(Videojuego, slug=slug)

    return render(request, 'juego.html', {'videojuego': videojuego, 'videojuegos': videojuegos,'username': username})


@login_required
def noticias(request):
    username = request.user.username

    noticias = Noticia.objects.all()

    return render(request, 'noticias.html', {'noticias': noticias,'username': username})

