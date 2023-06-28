from django.shortcuts import render
from tienda.models import Producto
from tienda.models import Noticia



# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})

def inicio_sesion(request):
    return render(request, 'inicioSesion.html')

def registro(request):
    return render(request, 'registro.html')

def juego(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'juego.html', {'producto': producto})




# def admin_dashboard(request):
#     # Vista para el panel de administración
#     # Puedes agregar lógica adicional aquí según tus necesidades
#     return render(request, 'admin/dashboard.html')

def tienda(request):
    # Vista para la tienda online
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})

def detalle_producto(request, producto_id):
    # Vista para mostrar los detalles de un producto en particular
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})
