from django.urls import path, include
from Apps.Actividad.views import *

urlpatterns = [
    path(r'IndexProfesor/', IndexProfesor, name='IndexProfesor'),
   	path(r'CrearActividad/<int:idMateria>', CrearActividad,name='CrearActividad'),
    path(r'ListarActividad/<int:idMateria>',ListarActividad,name= 'ListarActividad'),
    path(r'ListarMateria/', ListarMateria, name='ListarMateria'),

  
]