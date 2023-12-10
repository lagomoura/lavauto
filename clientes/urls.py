from django.urls import path
from . import views

# . Aca guardamos todas las urls que vamos a utilizar en la aplicacion de clientes. Unimos cada url con una vista y con un nombre que representa

urlpatterns = [
    # .Recibe una requisicion y da una respuesta
    path("", views.clientes, name="clientes"), 
    path("actualiza_cliente/", views.datos_cliente, name="actualiza_cliente")
]
