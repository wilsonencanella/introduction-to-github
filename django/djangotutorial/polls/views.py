from django.http import HttpResponse


# vista mas simple posible, solo devuelve un texto
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
