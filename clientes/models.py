from django.db import models

#! Aca es donde seteamos la info que sera guardado en la base de datos
# Create your models here.

class Cliente(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField(max_length=50)
  dni = models.CharField(max_length=8)
  
  def __str__(self) -> str:
    return self.nombre

class Auto(models.Model):
  auto = models.CharField(max_length=20)
  patente = models.CharField(max_length=10)
  cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE) #Models.cascade siguinifica que al deletar un cliente, todos los autos que estan asociados a ese cliente tambien van a ser deletados. En caso contrario, deberiamos usar models.SET_NULL
  lavados = models.IntegerField(default=0)
  arreglos = models.IntegerField(default=0)
  
  def __str__(self) -> str:
    return self.auto