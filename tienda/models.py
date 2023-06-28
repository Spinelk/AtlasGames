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
    usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='noticias')

    def __str__(self):
            return self.titulo