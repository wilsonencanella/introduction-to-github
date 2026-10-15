from django.contrib import admin

from .models import Question

# para poder editar las preguntas desde el admin
admin.site.register(Question)
