# Generated by Django 4.2.2 on 2023-06-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_alter_videojuego_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
