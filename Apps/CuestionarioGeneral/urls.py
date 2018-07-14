from django.urls import path, include
from Apps.Cuestionario.views import *

urlpatterns = [

   	path(r'CrearCuestionario/<int:idMateria>', CrearCuestionario,name='CrearCuestionario'),
    path(r'ListarCuestionario/<int:idMateria>',ListarCuestionario,name= 'ListarCuestionario'),
    path ( r'Index/' , Index , name='Index' ) ,
    path(r'ListarMateria/', ListarMateria, name='ListarMateria'),
  
]