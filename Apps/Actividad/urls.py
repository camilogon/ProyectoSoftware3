from django.urls import path, include
from Apps.Actividad.views import *

urlpatterns = [

   	path(r'CrearActividad/', CrearActividad,name='CrearActividad'),
    path(r'ListarActividad/',ListarActividad,name= 'ListarActividad'),
  
]