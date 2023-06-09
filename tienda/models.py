from django.db import models
from django.utils.text import slugify

# Imports para borrar las imagenes si se borra el 'objeto'
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings
import os


from django.contrib.auth.models import User
from django.utils import timezone


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
    slug = models.SlugField(unique=True, blank=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto_pq = models.ImageField(upload_to='videojuego/portada/pq')
    foto_md = models.ImageField(upload_to='videojuego/portada/md')
    foto_gd = models.ImageField(upload_to='videojuego/portada/gd')
    generos = models.ManyToManyField(Genero, blank=False)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    esbr = models.ForeignKey(ESBR, on_delete=models.CASCADE)
    pegi = models.ForeignKey(PEGI, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
        
    def get_precio_formateado(self):
        if (self.precio == 0):
            return 'Gratis'

        precio_formateado = "{:,.0f}".format(self.precio).replace(",", ".")
        return '$'+precio_formateado

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


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['usuario', 'videojuego']

    def __str__(self):
        return f"{self.usuario}: {self.videojuego}"