from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Cuestionario.Forms import CuestionarioForm
from Apps.Cuestionario.models import Cuestionario
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from Apps.Tema.models import Tema
from django.core import serializers
from Apps.Actividad.models import infoac
from Apps.CuestionarioGeneral.models import CuestionarioGeneral
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
#
def IndexEstudiante(request):
    materias = Materia.ListarMateriasEstudiante ( 123456 )
    return render_to_response("indexEstudiante.html",{"Materias": materias, "messages": messages.get_messages(request)})

"""Metodo que nos muestra en la interfaz los cuestionarios disponibles
segun un id de materia que ingresa por paramentro"""
def ListarCuestionarios(request,idMateria):
    cuestionarios=CuestionarioGeneral.ListarCuestionariosGeneral(idMateria,1)
    materias = Materia.ListarMateriasEstudiante ( 123456 )
    return render_to_response ( "PreguntasCuestionarios/ListarCuestionariosPreguntas.html" , {"Materias": materias,"Cuestionarios":cuestionarios, "messages": messages.get_messages ( request )} )

def ResolverCuestionario(request,idCuestionario):
    preguntas= Cuestionario.ListarCuestionariosResolver(idCuestionario)
    cuestionarioNombre= CuestionarioGeneral.ListarNombreCuestionarios(idCuestionario)
    nombre=""
    for cues in cuestionarioNombre:
        nombre=cues.Nombre
    return render_to_response ( "PreguntasCuestionarios/ResolverCuestionario.html" , {"NombreCues":nombre,"Preguntas":preguntas ,"messages": messages.get_messages ( request )})