from django.contrib import admin

from .models import Choice, Question


# las opciones se editan dentro de la misma pagina de la pregunta
# tabular = en filas tipo tabla, ocupa menos espacio que stacked
class ChoiceInline(admin.TabularInline):
    model = Choice
    # cuantos espacios vacios para opciones nuevas
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # agrupa los campos en secciones, la fecha va aparte
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    # columnas que salen en la lista de preguntas
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # barra lateral para filtrar por fecha
    list_filter = ["pub_date"]
    # cajita de busqueda arriba de la lista
    search_fields = ["question_text"]


# para poder editar las preguntas desde el admin
admin.site.register(Question, QuestionAdmin)
