from django.forms import ModelForm
from .models import Servicio, CategoriaMantenimiento


class FormServicio(ModelForm):
    class Meta:
        model = Servicio
        # . Va a traer todos los campos de Servicio, menos los mencionados
        exclude = ['finalizado', 'protocolo_servicio']

    #. Manera de sobreescribir una clase.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'}) #. Agregamos una clase a cada field.
            
