from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nombre = request.POST.get('nombre')
        sobrenombre = request.POST.get('sobrenombre')
        email = request.POST.get('email')
        dni = request.POST.get('dni')
