from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, 'noticias.html')

def inicio_sesion(request):
    return render(request, 'inicioSesion.html')

def registro(request):
    return render(request, 'registro.html')

def juego(request):
    return render(request, 'juego.html')