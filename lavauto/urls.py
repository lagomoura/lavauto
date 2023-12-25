
from django.contrib import admin
from django.urls import path, include

# . Aca guardamos todas las urls que vamos a utilizar en la aplicacion. Representamos la url como 1ro parametro y la respuesta en el segundo. Esa respuesta llama lo que esta puesto en el archivo de urls de cada uno de los apps listados abajo

#. clientes/ y servicios/ son apps de Django.

urlpatterns = [
    path('admin/', admin.site.urls),
    path("clientes/", include("clientes.urls")),
    path("servicios/", include("servicios.urls")),
]
