# Generated by Django 4.2.2 on 2023-07-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0017_videojuego_esbr_videojuego_pegi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videojuego',
            name='genero',
        ),
        migrations.AddField(
            model_name='videojuego',
            name='generos',
            field=models.ManyToManyField(to='tienda.genero'),
        ),
    ]