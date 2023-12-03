# Atlas Games
# Proyecto Semestral de Programación Web

## Requisitos
- Python 3.10^

## Instalación Windows
```
git clone https://github.com/Spinelk/AtlasGames

cd AtlasGames

python -m venv venv

.\venv\Scripts\activate

pip install -r requerimientos.txt
```

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


Servidor en red lan
```
ipconfig
python manage.py runserver 0.0.0.0:5000
```