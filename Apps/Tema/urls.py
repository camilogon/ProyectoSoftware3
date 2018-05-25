from django.urls import path, include
from Apps.Tema.views import *

urlpatterns = [
    path(r'CrearTema/', CrearTema,name='CrearTema'),
    path(r'ListarTema/',ListarTema,name= 'ListarTema'),
    path(r'EditarTema/<int:Codigo>/', EditarTema, name='EditarTema'), #formulario para editar
    path(r'EliminarTema/<int:Codigo>/', EliminarTema, name='EliminarTema'), #ruta para eliminar
]