# Generated by Django 4.2.2 on 2023-07-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0026_alter_compra_fecha_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
