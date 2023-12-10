
#! El view es el encargado de enviar la informacion colectada desde el fron al back.
#! Aca hacemos la logica que queremos implementar en el front-end, relacionado con el formulario.


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# . Vinculamos el formulario con las clases creadas en el models
from .models import Cliente, Auto
import re  # . Importa biblioteca de expresiones regulares
from django.core import serializers  # . Transforma una model(objeto) en json
import json

# . La funcion es la encargada de recibir y organizar la data colectada en el fron, criendo el objeto cliente y guardando en la DB.


def clientes(request):
    lista_clientes = Cliente.objects.all()
    if request.method == "GET":
        return render(request, 'clientes.html', {"clientes": lista_clientes})
    elif request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        dni = request.POST.get('dni')
        # . Con el getlist tomamos varios valores con un input teniendo el names iguales. En get comun solo puede recibir un unico dato
        autos = request.POST.getlist('auto')
        patentes = request.POST.getlist('patente')

        #! Prueba de captacion de la informacion
        # print(autos)
        # print(patentes)
        # print(request.POST)

        # . Guardamos toda la informacion de un cliente, juntando todos los atributos levantados, y asignamos que informacion cada columna de la base de datos va a recibir.
        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            dni=dni
        )

        # . Ingresamos una validacion para que no sea ingresado el mismo cliente 2 veces. Cremos una "flag" donde chequeamos si el dni tomado en el form ya existe en la base de datos. Si eso pasa la variable trae todos estos clientes. Si no hay ningun repetido, la variable queda como NONE
        # todo Agregar una view de cliente repetido
        cliente_repetido = Cliente.objects.filter(dni=dni)
        print(cliente_repetido)

        if cliente_repetido.exists():
            return render(request, "clientes.html", {"nombre": nombre, "apellido": apellido, "email": email, "autos": zip(autos, patentes)})

        # . En el caso de que la variable tenga contenido, la variable EXISTS se toma como true y podemos trabajar con la validacion.
        if cliente_repetido.exists():
            return HttpResponse("Cliente ya existente")

        # . Llamamos a la biblioteca de expresiones regulares. o FULLMATCH informa que eso tiene que matchear de manera completa. Pasamos la expresion regular a traves del compite y luego indicamos cual sera la variable que sera validad con esa expresion
        if not re.fullmatch(re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'), email):
            return render(request, "clientes.html", {"nombre": nombre, "apellido": apellido, "dni": dni, "autos": zip(autos, patentes)})

        cliente.save()

        # . Aca hacemos lo mismo, pero como puede haber mas de 1 auto y patente por cliente, tenemos que tomarlo coun un FOR, de lo contrario, seria solo tomada la ultima informacion agregada.
        # . La variable vehiculo, va a ser la informacion globalizada, unificando los autos con sus informaciones, las patentes y todas las informaciones de los clientes,
        for auto, patente in zip(autos, patentes):
            # columna auto lleva la info de auto, columna patente, llega la info de la variable patente.
            vehiculo = Auto(auto=auto, patente=patente, cliente=cliente)
            vehiculo.save()

        # ! Esa respuesta esta como metodo de test
        return HttpResponse("Test aprobado - Cliente guardado!")

# . Esa funcion es la responsable de escupir al frontend lo que sera visualizado al momento de elegir un cliente en la seccion de actualizar cliente


def datos_cliente(request):
    id_cliente = request.POST.get("id_cliente")
# . Aca consigo ubicar el cliente en mi base de datos conectando a traves del id_cliente al mi objeto Cliente
    cliente = Cliente.objects.filter(id=id_cliente)
# . Transformo la info de mi DB en un JSON. La data viene en un formato puro string. Para mejor el manejo transformamos la data en un json adentro de una lista.
    cliente_json = json.loads(
        serializers.serialize("json", cliente))[0]["fields"]
# .El json traz la informacion en una lista en diccionario de 3 indices (model, pk, fields). Agregamos indice 0 para sacar de la lista y buscamos por la key FIELDS que es donde estan guardadas la informacion del cliente.
    return JsonResponse(cliente_json)
# . Enviamos esa informacion el fron
