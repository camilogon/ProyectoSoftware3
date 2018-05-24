from django.urls import path, include
from Apps.Curso.views import *

urlpatterns = [
	path(r'Inicio/', CrearCurso,name='Inicio'),
    path(r'CrearCurso/', CrearCurso,name='CrearCurso'),
    path(r'ListarCurso/',ListarCurso,name= 'ListarCurso'),
    path(r'EditarCurso/<int:id>/', EditarCurso, name='EditarCurso'), #formulario para editar
    path(r'EliminarCurso/<int:id>/', EliminarCurso, name='EliminarCurso'), #ruta para eliminar
]