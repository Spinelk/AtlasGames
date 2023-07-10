from django.shortcuts import render, get_object_or_404
from tienda.models import Videojuego
from tienda.models import Noticia



# Create your views here.
def index(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'index.html', {'videojuegos': videojuegos})

# def juego(request, videojuego_id):
#     videojuegos = Videojuego.objects.all()
#     videojuego = Videojuego.objects.get(id=videojuego_id)
#     return render(request, 'juego.html', {'videojuego': videojuego, 'videojuegos': videojuegos})

def juego(request, slug):
    videojuegos = Videojuego.objects.all()
    videojuego = get_object_or_404(Videojuego, slug=slug)
    return render(request, 'juego.html', {'videojuego': videojuego, 'videojuegos': videojuegos})

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})


def inicio_sesion(request):
    return render(request, 'usuarios/inicioSesion.html')

def registro(request):
    return render(request, 'usuarios/registro.html')
