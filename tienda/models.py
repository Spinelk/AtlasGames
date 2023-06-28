from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    foto_pq = models.ImageField(upload_to='productos/pq')
    foto_md = models.ImageField(upload_to='productos/md')
    foto_gd = models.ImageField(upload_to='productos/gd')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_usuario = models.IntegerField()

    def __str__(self):
        return self.nombre

    
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings
import os
@receiver(post_delete, sender=Producto)
def eliminar_imagen(sender, instance, **kwargs):
    if instance.foto:
        # Eliminar la imagen asociada al producto
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(instance.foto))
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)


class Usuario(models.Model):
    correo = models.EmailField()
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    correo = models.EmailField()
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Boleta(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class DetalleBoleta(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre