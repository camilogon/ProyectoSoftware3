from django.urls import path, include
from Apps.Materia.views import *

urlpatterns = [
    path(r'CrearMateria/', CrearMateria,name='CrearMateria'),
    path(r'ListarMateria/',ListarMateria,name= 'ListarMateria'),
    path(r'EditarMateria/<int:id>/', EditarMateria, name='EditarMateria'), #formulario para editar
    path(r'EliminarMateria/<int:id>/', EliminarMateria, name='EliminarMateria'), #ruta para eliminar
]