from django.urls import path, include
from Apps.Estudiante.views import *

urlpatterns = [
    path(r'CrearEstudiante/', CrearEstudiante,name='CrearEstudiante'),
    path(r'ListarEstudiante/',ListarEstudiante,name= 'ListarEstudiante'),
    path(r'EditarEstudiante/<int:id>/', EditarEstudiante, name='EditarEstudiante'), #formulario para editar
    path(r'EliminarEstudiante/<int:id>/', EliminarEstudiante, name='EliminarEstudiante'), #ruta para eliminar
]