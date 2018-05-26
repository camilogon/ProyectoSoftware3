from django.urls import path, include
from Apps.Asignar.views import *

urlpatterns = [
    path(r'CrearAsignaciones/', CrearAsignaciones,name='CrearAsignaciones'),
    path(r'ListarAsignaciones/',ListarAsignaciones,name= 'ListarAsignaciones'),
    path(r'EditarAsignaciones/<int:id>/', EditarAsignaciones, name='EditarAsignaciones'), #formulario para editar
    path(r'EliminarAsignaciones/<int:id>/', EliminarAsignaciones, name='EliminarAsignaciones'), #ruta para eliminar
]