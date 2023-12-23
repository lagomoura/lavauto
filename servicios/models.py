from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaMantenimiento

# Create your models here.


class CategoriaMantenimiento(models.Model):
    titulo = models.CharField(
        max_length=3, choices=ChoicesCategoriaMantenimiento.choices)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.titulo


class Servicio(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    categoria_mantenimiento = models.ManyToManyField(CategoriaMantenimiento)
    fecha_ingreso = models.DateField(null=True)
    fecha_salida = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo_servicio = models.CharField(max_length=32, null=True, blank=True)
