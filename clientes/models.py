from django.db import models

#! Aca es donde seteamos la info que sera guardado en la base de datos

# . Creamos una tabla llamada clientes. Esa tabla tiene nombre, apellido, email y dni como columnas y pasamos que datos son aceptados por esa columna


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    dni = models.CharField(max_length=8)

    # . Retornamos como modo de resumen de la informacion, el nombre del cliente
    def __str__(self) -> str:
        return self.nombre

# . Aca hacemos lo mismo, creando una tabla par Auto con sus atributos correspondientes(columnas)


class Auto(models.Model):
    auto = models.CharField(max_length=20)
    patente = models.CharField(max_length=10)
    # Models.cascade siguinifica que al deletar un cliente, todos los autos que estan asociados a ese cliente tambien van a ser deletados. En caso contrario, deberiamos usar models.SET_NULL
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavados = models.IntegerField(default=0)
    arreglos = models.IntegerField(default=0)

    # . Retornamos como modo de resumen de la informacion, el modelo del auto
    def __str__(self) -> str:
        return self.auto
