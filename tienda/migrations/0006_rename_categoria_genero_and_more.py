# Generated by Django 4.2.2 on 2023-06-28 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_videojuego_delete_producto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Genero',
        ),
        migrations.RenameField(
            model_name='videojuego',
            old_name='categoria',
            new_name='genero',
        ),
    ]