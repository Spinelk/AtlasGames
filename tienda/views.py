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
import json

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


@login_required
def biblioteca(request):
    usuario = request.user

    compras = Compra.objects.filter(usuario=usuario.id)

    return render(request, 'biblioteca.html', {'compras': compras})


# @login_required
# def generar_compra(request):
#     carrito = request.session.get("carrito", [])
#     usuario = request.user

#     for producto in carrito:
#         console.log(producto["slug"])
#         slug = producto["slug"]
#         videojuego = Videojuego.objects.get(slug=slug)
#         compra = Compra(usuario=usuario, videojuego=videojuego)
#         compra.save()

#     # Limpiar el carrito después de generar la compra
#     request.session["carrito"] = []

#     return redirect('tienda:biblioteca')


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