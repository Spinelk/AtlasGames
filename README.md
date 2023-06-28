# Atlas Games
# Proyecto Semestral de Programación Web

## Instalación
```
git clone https://github.com/Spinelk/AtlasGames

python -m venv myvenv

.\myvenv\Scripts\activate

cd AtlasGames

pip install -r requerimientos.txt

```

## Migraciones
elimina el db.sqlite3
```
python manage.py makemigrations
python manage.py migrate
```

## RUN
Servidor normal
```
python manage.py runserver
```


Servidor en red lan
```
ipconfig
python manage.py runserver 0.0.0.0:5000
```