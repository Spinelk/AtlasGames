from django.db import models

# Imports para borrar las imagenes si se borra el 'objeto'
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings
import os

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Estudio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class PEGI(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class ESBR(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto_pq = models.ImageField(upload_to='videojuego/portada/pq')
    foto_md = models.ImageField(upload_to='videojuego/portada/md')
    foto_gd = models.ImageField(upload_to='videojuego/portada/gd')
    # genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Genero, blank=False)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    esbr = models.ForeignKey(ESBR, on_delete=models.CASCADE)
    pegi = models.ForeignKey(PEGI, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


@receiver(post_delete, sender=Videojuego)
def eliminar_imagen(sender, instance, **kwargs):
    if instance.foto_pq:
        # Eliminar la imagen asociada al videojuego
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(instance.foto_pq))
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

    if instance.foto_md:
        # Eliminar la imagen asociada al videojuego
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(instance.foto_md))
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

    if instance.foto_gd:
        # Eliminar la imagen asociada al videojuego
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(instance.foto_gd))
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='noticias')

    def __str__(self):
            return self.titulo


class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario