from django.urls import path
from . import views

urlpatterns = [
  path('nuevo_servicio/', views.nuevo_servicio, name='nuevo_servicio')
]