# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Modulos Python
from random import shuffle
import json

# Modelos
from tienda.models import Videojuego
from tienda.models import Noticia
from tienda.models import Compra


@login_required
def index(request):
    videojuegos = Videojuego.objects.all()
    videojuegos_todos = list(videojuegos)
    shuffle(videojuegos_todos)

    videojuegos_gratuitos = list(Videojuego.objects.filter(precio=0))
    shuffle(videojuegos_gratuitos)

    videojuegos_indie = list(Videojuego.objects.filter(generos__nombre="Indie"))
    shuffle(videojuegos_indie)

    context = {
        'videojuegos': videojuegos_todos,
        'videojuegos_gratuitos': videojuegos_gratuitos,
        'videojuegos_indie': videojuegos_indie,
    }
    
    return render(request, 'index.html', context)

@login_required
def juego(request, slug):
    videojuego = get_object_or_404(Videojuego, slug=slug)
    estudio = videojuego.estudio
    
    videojuegos_estudio = list(Videojuego.objects.filter(estudio=estudio).exclude(slug=slug))
    shuffle(videojuegos_estudio)

    context = {
        'videojuegos_estudio': videojuegos_estudio,
        'videojuego': videojuego
    }

    return render(request, 'juego.html', context)


@login_required
def noticias(request):
    noticias = Noticia.objects.all()

    return render(request, 'noticias.html', {'noticias': noticias})


@login_required
def biblioteca(request):
    usuario = request.user

    compras = Compra.objects.filter(usuario=usuario.id)

    return render(request, 'biblioteca.html', {'compras': compras})


@csrf_exempt # Esto no deberia ser necesario
@login_required
@login_required
@require_POST 
def generar_compra(request):
    carrito_str = request.POST.get('carrito', '[]')
    carrito = json.loads(carrito_str)

    usuario = request.user

    for producto in carrito:
        slug = producto['slug']
        videojuego = Videojuego.objects.get(slug=slug)
        compra = Compra(usuario=usuario, videojuego=videojuego)
        compra.save()

    return redirect('tienda:biblioteca')


def explorar(request):
    print("TEST")
    query = request.GET.get('q') or ""

    if query:
        videojuegos = Videojuego.objects.filter(nombre__icontains=query)
    else:
        videojuegos = []

    context = {
        'query': query,
        'videojuegos': videojuegos,
    }

    return render(request, 'explorar.html', context)
