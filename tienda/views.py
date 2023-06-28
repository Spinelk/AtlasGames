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



from tienda.models import Producto

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
