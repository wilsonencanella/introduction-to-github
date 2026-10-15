# Polls - Django Tutorial

App de encuestas hecha siguiendo el [tutorial oficial de Django 6.1](https://docs.djangoproject.com/en/6.1/intro/tutorial01/) (partes 1 a 7).

## Coomo correrlo

Desde la carpeta `django/` (PowerShell):

```powershell
# entorno virtual, para no mezclar dependencias con otros proyectos
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instala Django y sus dependencias en las versiones exactas
pip install -r requirements.txt

cd djangotutorial

# crea las tablas en db.sqlite3 (no se sube al repo, cada quien genera la suya)
python manage.py migrate

# usuario para entrar al admin
python manage.py createsuperuser

# confirma que todo funcione
python manage.py test polls

# levanta el servidor de desarrollo (ctrl + c para detenerlo)
python manage.py runserver
```

Luego abre:

- http://127.0.0.1:8000/polls/: las encuestas
- http://127.0.0.1:8000/admin/: aquí creas preguntas y opciones
