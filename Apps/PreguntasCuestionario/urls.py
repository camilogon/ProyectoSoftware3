from django.urls import path, include
from Apps.PreguntasCuestionario.views import *

urlpatterns = [

   	path(r'IndexEstudiante/', IndexEstudiante,name='IndexEstudiante'),
    path(r'ListarCuestionarios/<int:idMateria>',ListarCuestionarios,name= 'ListarCuestionarios'),
    path ( r'ResolverCuestionario/<int:idCuestionario>' , ResolverCuestionario , name='ResolverCuestionario' ) ,
    #path(r'ListarMateria/', ListarMateria, name='ListarMateria'),
  
]