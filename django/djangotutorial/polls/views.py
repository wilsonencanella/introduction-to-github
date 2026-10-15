from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


# las ultimas 5 preguntas, de la mas nueva a la mas vieja
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # sin esto la variable en el template se llamaria question_list
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # lte = menor o igual, asi no salen las programadas para el futuro
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


# detailview ya hace el get_object_or_404 solito usando el pk de la url
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    # si alguien adivina el id de una pregunta futura igual le sale 404
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # no eligio nada (o mando un id raro), le volvemos a mostrar el form con el error
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # F() hace la suma en la base, asi dos votos al mismo tiempo no se pisan
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # redirect despues del post para que si recarga la pagina no vote doble
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
