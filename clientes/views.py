from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Auto #. Vinculamos el formulario con las clases creadas en el models

# Create your views here.

#. Aca hacemos la logica que queremos implementar en el front-end, relacionado con el formulario.
def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        dni = request.POST.get('dni')
        #. Con el getlist tomamos varios valores con un input teniendo el name igual
        autos = request.POST.getlist('auto')
        patentes = request.POST.getlist('patente')

        #. Prueba de captacion de la informacion
        print(autos)
        print(patentes)
        print(request.POST)

        #. Guardamos toda la informacion de un cliente, juntando todos los atributos levantados, y asignamos que informacion cada columna de la base de datos va a recibir.
        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            dni=dni
        )
        
        #. Ingresamos una validacion para que no sea ingresado el mismo cliente 2 veces. Cremos una "flag" donde chequeamos si el dni tomado en el form ya existe en la base de datos. Si eso pasa la variable trae todos estos clientes. Si no hay ningun repetido, la variable queda como NONE
        cliente_repetido = Cliente.objects.filter(dni=dni)
        print(cliente_repetido)
        
        #. En el caso de que la variable tenga contenido, la variable EXISTS se toma como true y podemos trabajar con la validacion.
        if cliente_repetido.exists():
            return HttpResponse("Cliente ya existente")
        
        
        cliente.save()

        #. Aca hacemos lo mismo, pero como puede haber mas de 1 auto y patente por cliente, tenemos que tomarlo coun un FOR, de lo contrario, seria solo tomada la ultima informacion agregada. 
        #. La variable vehiculo, va a ser la informacion globalizada, unificando los autos con sus informaciones, las patentes y todas las informaciones de los clientes,
        for auto, patente in zip(autos, patentes):
            vehiculo = Auto(auto=auto, patente=patente, cliente=cliente) #columna auto lleva la info de auto, columna patente, llega la info de la variable patente. 
            vehiculo.save()

        return HttpResponse("test") #! Esa respuesta esta como metodo de test
