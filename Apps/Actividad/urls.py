from django.urls import path, include
from Apps.Actividad.views import *

urlpatterns = [
    path(r'IndexProfesor/', IndexProfesor, name='IndexProfesor'),
   	path(r'CrearActividad/', CrearActividad,name='CrearActividad'),
    path(r'ListarActividad/',ListarActividad,name= 'ListarActividad'),
    path(r'ListarMateria/', ListarMateria, name='ListarMateria'),

  
]