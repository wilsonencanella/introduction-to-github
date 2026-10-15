import datetime

from django.db import models
from django.utils import timezone


# cada pregunta de la encuesta
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    # true si la pregunta se publico en el ultimo dia
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# opciones de respuesta, cada una amarrada a su pregunta
class Choice(models.Model):
    # si se borra la pregunta se borran sus opciones tambien
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
