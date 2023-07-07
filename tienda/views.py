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






# def admin_dashboard(request):
#     # Vista para el panel de administración
#     # Puedes agregar lógica adicional aquí según tus necesidades
#     return render(request, 'admin/dashboard.html')

def tienda(request):
    # Vista para la tienda online
    videojuegos = Videojuego.objects.all()
    return render(request, 'tienda/tienda.html', {'videojuegos': videojuegos})

def detalle_producto(request, videojuego_id):
    # Vista para mostrar los detalles de un producto en particular
    videojuego = Videojuego.objects.get(id=videojuego_id)

    return render(request, 'tienda/detalle_producto.html', {'videojuego': videojuego})

