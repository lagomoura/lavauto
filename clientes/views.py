from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Auto
# Create your views here.


def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        dni = request.POST.get('dni')
        # Con el getlist tomamos varios valores con un input teniendo el name igual
        autos = request.POST.getlist('auto')
        patentes = request.POST.getlist('patente')


        


        print(autos)
        print(patentes)
        print(request.POST)

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            dni=dni
        )
        
        cliente.save()

        for auto, patente in zip(autos, patentes):
            aut = Auto(auto=auto, patente=patente, cliente=cliente) #columna auto lleva la info de auto, columna patente, llega la info de la variable patente. 
            aut.save()

        return HttpResponse("test")
