
from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaMantenimiento
from datetime import datetime
from secrets import token_hex

#! Modelado de base de datos
# . Creamos una clase para categorizar las opciones de mantenimiento, importanto las opciones desde un archivo a parte. Esas opciones DJANGO llama de CHOICES. Se crea una tabla para cada class creada en los models.


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
    protocolo_servicio = models.CharField(max_length=52, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.protocolo_servicio:
            self.protocolo_servicio = datetime.now().strftime(
                "%d/%m/%Y-%H:%M:%S-") + token_hex(16)
        super(Servicio, self).save(*args, **kwargs)

    def precio_total(self):
        precio_total = float(0)
        for categoria in self.categoria_mantenimiento.all():
            precio_total += float(categoria.precio)

        return precio_total
