from django.urls import path
from . import views

urlpatterns = [
  path("", views.clientes, name="clientes" ) #Recibe una requisicion y da una respuesta
]