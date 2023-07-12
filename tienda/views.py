from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Videojuego
from tienda.models import Noticia
from tienda.models import Compra
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from random import shuffle
import json

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
    
    videojuegos = Videojuego.objects.filter(estudio=estudio).exclude(slug=slug)
    videojuegos_estudio = list(videojuegos)
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


@login_required
def generar_compra(request):
    carrito = request.session.get("carrito", [])
    usuario = request.user

    print("test 1")
    for producto in carrito:
        print("test 2")
        slug = producto["slug"]
        videojuego = Videojuego.objects.get(slug=slug)
        compra = Compra(usuario=usuario, videojuego=videojuego)
        compra.save()
    print("test 3")
    
    # Limpiar el carrito después de generar la compra
    request.session["carrito"] = []


    return redirect('tienda:biblioteca')


@csrf_exempt
def guardar_carrito_en_servidor(request):
    if request.method == 'POST':
        carrito_str = request.POST.get('carrito', '[]')
        carrito = json.loads(carrito_str)

        usuario = request.user

        for producto in carrito:
            slug = producto['slug']
            videojuego = Videojuego.objects.get(slug=slug)
            compra = Compra(usuario=usuario, videojuego=videojuego)
            compra.save()
    
        messages.success(request, "La compra se generó con éxito.")
        return redirect('tienda:biblioteca')