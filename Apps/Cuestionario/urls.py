from django.urls import path, include
from Apps.Cuestionario.views import *

urlpatterns = [

   	path(r'CrearCuestionario/', CrearCuestionario,name='CrearCuestionario'),
    path(r'ListarCuestionario/',ListarCuestionario,name= 'ListarCuestionario'),
  
]