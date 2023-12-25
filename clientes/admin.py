from django.contrib import admin
from .models import Cliente, Auto

# . Esta seccion es referente al manejo de admin que tenemos sobre la aplicacion web completa. Ingresando en la url /admin/.
# . Registramos la(s) CLASE(S) que tenemos bajo la app creada. En ese caso, la app clientes tiene las CLASES (Cliente y Auto)

admin.site.register(Cliente)
admin.site.register(Auto)
