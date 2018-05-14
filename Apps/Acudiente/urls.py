from django.urls import path, include
from Apps.Acudiente.views import *

urlpatterns = [
    path(r'CrearAcudiente/', CrearAcudiente,name='CrearAcudiente'),
    path(r'ListarAcudiente/',ListarAcudiente,name= 'ListarAcudiente'),
    path(r'EditarAcudiente/<int:id>/', EditarAcudiente, name='EditarAcudiente'), #formulario para editar
    path(r'EliminarAcudiente/<int:id>/', EliminarAcudiente, name='EliminarAcudiente'), #ruta para eliminar
]