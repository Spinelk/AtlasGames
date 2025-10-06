# Atlas Games - Tienda WEB
# Proyecto Semestral de Programación Web - Revision 2052

<br>
<br>

## INSTRUCCIONES DE INSTALACIÓN PROVISIONALES


## Teteado en Podman
- Fedora 37 / Python 3.11.6

## Creacion de podman con toolbx en fedora
```
toolbox create <name> -r 37

```

<br>

## Instalación
```
toolbox enter <name>

sudo dnf install python3-pip

git clone https://github.com/Spinelk/AtlasGames

cd AtlasGames

pip install -r requerimientos.txt
```

<br>
<br>

# Instrucciones de uso 

## Consideración
Es posible que deba utilizar 'python3' en lugar de 'python' dependiendo del entorno/imagen que se utilice.

## Migraciones
```
python manage.py makemigrations
python manage.py migrate
```

## RUN
Servidor normal
```
python manage.py runserver
```

Servidor dentro de podman. El puerto por defecto puede estar ocupado, se debe elegir uno disponible
```
python manage.py runserver 0.0.0.0:5000
```

Servidor en red lan
```
ipconfig
python manage.py runserver 0.0.0.0:5000
```