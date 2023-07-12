# Atlas Games
# Proyecto Semestral de Programación Web

## Instalación
```
git clone https://github.com/Spinelk/AtlasGames

python -m venv myvenv

.\myvenv\Scripts\activate

cd AtlasGames

pip install -r requerimientos.txt

python manage.py runserver --insecure

```

## Migraciones
```
python manage.py makemigrations
python manage.py migrate
```

## RUN
Servidor inseguro
```
python manage.py runserver --insecure
```


Servidor en red lan
```
ipconfig
python manage.py runserver 0.0.0.0:5000
```