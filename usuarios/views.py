from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tienda:index')
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos'
            return render(request, 'usuarios/login.html', {'error_message': error_message})
    else:
        return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            error_message = 'Las contraseñas no coinciden'
            return render(request, 'usuarios/register.html', {'error_message': error_message})

        # Verificar si el nombre de usuario ya está en uso
        if User.objects.filter(username=username).exists():
            error_message = 'El nombre de usuario ya está en uso'
            return render(request, 'usuarios/register.html', {'error_message': error_message})

        # Crear el nuevo usuario
        user = User.objects.create_user(username=username, password=password)
        user.save()

        login(request, user)
        return redirect('tienda:index')
    else:
        return render(request, 'usuarios/register.html')
