from django.shortcuts import render
from .forms import FormServicio


def nuevo_servicio(request):
    form = FormServicio()
    return render(request, 'nuevo_servicio.html', {'form': form})
