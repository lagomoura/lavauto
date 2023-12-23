from django.shortcuts import render

# Create your views here.


def nuevo_servicio(request):
    return render(request, 'nuevo_servicio.html')
