# Generated by Django 4.2.2 on 2023-07-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0018_remove_videojuego_genero_videojuego_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='slug',
            field=models.SlugField(default='default-name'),
            preserve_default=False,
        ),
    ]