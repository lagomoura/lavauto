
#! El view es el encargado de enviar la informacion colectada desde el fron al back.
#! Aca hacemos la logica que queremos implementar en el front-end, relacionado con el formulario.


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# . Vinculamos el formulario con las clases creadas en el models
from .models import Cliente, Auto
import re  # . Importa biblioteca de expresiones regulares
from django.core import serializers  # . Transforma una model(objeto) en json
import json
# . Nos da la opcion de desactivar la validacion de seguridad csrf token de un formulario
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

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
        print(autos)
        print(patentes)
        print(request.POST)

        # . Guardamos toda la informacion de un cliente, juntando todos los atributos levantados, y asignamos que informacion cada columna de la base de datos va a recibir.
        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            dni=dni
        )

        # . Ingresamos una validacion para que no sea ingresado el mismo cliente 2 veces. Cremos una "flag" donde chequeamos si el dni tomado en el form ya existe en la base de datos. Si eso pasa la variable trae todos estos clientes. Si no hay ningun repetido, la variable queda como NONE
        # TODO Agregar una view de cliente repetido
        cliente_repetido = Cliente.objects.filter(dni=dni)
        # print(cliente_repetido)

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
            vehiculo = Auto(auto=auto,
                            patente=patente,
                            cliente=cliente)

            vehiculo.save()

        # ! Esa respuesta esta como metodo de test
        return HttpResponse("Test aprobado - Cliente guardado!")

# . Esa funcion es la responsable de escupir al frontend lo que sera visualizado al momento de elegir un cliente en la seccion de actualizar cliente


def datos_cliente(request):
    id_cliente = int(request.POST.get("id_cliente"))
# . Aca consigo ubicar el cliente en mi base de datos conectando a traves del id_cliente al mi objeto Cliente

    cliente = Cliente.objects.filter(id=id_cliente)

# . Transformo la info de mi DB en un JSON. La data viene en un formato puro string. Para mejor el manejo transformamos la data en un json adentro de una lista.

    #!
    # . El metodo filter trae una lista de objetos y no un objeto en particular, por eso tenemos que indicar el indice 0.
    autos = Auto.objects.filter(cliente=cliente[0])
    auto_json = json.loads(serializers.serialize("json", autos))
    auto_json = [{"fields": auto["fields"], "id": auto["pk"]}  # . Paa cada auto quiero que me traiga el filds (nombre del diccionario donde esta guardada la info de cada auto) y el id de ese auto
                 for auto in auto_json]

    cliente_json = json.loads(
        serializers.serialize("json", cliente))[0]["fields"]

    # . Unifico la informacion del cliente con sus autos
    data = {"cliente": cliente_json,
            "autos": auto_json, "id_cliente": id_cliente}

    # .Prueba
    # print(data)
    #!

# .El json traz la informacion en una lista en diccionario de 3 indices (model, pk, fields). Agregamos indice 0 para sacar de la lista y buscamos por la key FIELDS que es donde estan guardadas la informacion del cliente.
    return JsonResponse(data)
# . Enviamos esa informacion el front


@csrf_exempt  # . Junto con la importacion del inicio del archivo desactiva la validacion de seguridad csrf token del formulario vinculado a esa funcion
def update_auto(request, id):
    nombre_auto = request.POST.get("auto")
    patente = request.POST.get("patente")

    auto = Auto.objects.get(id=id)
    # . Guardamos todos los datos de los vehiculos excluyendo los datos del proprio cliente de ese listado, asi podemos validar si la pantente ya existe sin dar conflicto con el registro del proprio cliente en el banco. Por eso se utiliza el exclude
    lista_autos = Auto.objects.filter(patente=patente).exclude(id=id)
    if lista_autos.exists():
        # . En el caso de que la patente ya exista en la BD no se hace el update.
        return HttpResponse("Patente ya existente")

    auto.auto = nombre_auto  # . En caso de update, el nuevo nombre se tome
    auto.patente = patente  # . Nueva patante se toma
    auto.save()  # . Se envia a DB

    return HttpResponse("Datos modificados con suceso")


def eliminar_auto(request, id):
    try:
        auto = Auto.objects.get(id=id)
        auto.delete()
        return redirect(reverse("cliente") + f'?aba=actualizar_cliente&id_cliente={id}')
    except Exception:
        # TODO Crear msg de error
        return redirect(reverse("clientes") + f'?aba=actualizar_cliente&id_cliente={id}')


def update_cliente(request, id):
    body = json.loads(request.body)

    nombre = body["nombre"]
    apellido = body["apellido"]
    email = body["email"]
    dni = body["dni"]

    try:
        cliente = get_object_or_404(Cliente, id=id)
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.email = email
        cliente.dni = dni

        cliente.save()

        return JsonResponse({"status": "200", "nombre": nombre, "apellido": apellido, "email": email, "dni": dni})

    except Exception:
        return JsonResponse({"status": "500"})
