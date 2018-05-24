from django.urls import path, include
from Apps.Profesor.views import *

urlpatterns = [
    path(r'CrearProfesor/', CrearProfesor,name='CrearProfesor'),
    path(r'ListarProfesor/',ListarProfesor,name= 'ListarProfesor'),
    path(r'EditarProfesor/<int:id>/', EditarProfesor, name='EditarProfesor'), #formulario para editar
    path(r'EliminarProfesor/<int:id>/', EliminarProfesor, name='EliminarProfesor'), #ruta para eliminar
]