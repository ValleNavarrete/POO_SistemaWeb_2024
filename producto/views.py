from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola a través de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1")

#crear vista principal
def inicio(request):
    return render(request, 'base.html')

