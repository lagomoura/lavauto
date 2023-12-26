from django.shortcuts import render
from .forms import FormServicio
from django.http import HttpResponse


def nuevo_servicio(request):
    if request.method == "GET":
        form = FormServicio()
        return render(request, 'nuevo_servicio.html', {'form': form})
    elif request.method == "POST":
        form = FormServicio(request.POST)

        if form.is_valid():  # . El is_valid ya valida automaticamente el formulario con base en lo seteado en el archivo de form
            form.save()
            return HttpResponse("Guardado con suceso!!")

        else:
            return render(request, 'nuevo_servicio', {'form': form})
