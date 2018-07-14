from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Cuestionario.Forms import CuestionarioForm
from Apps.Cuestionario.models import Cuestionario
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from Apps.Tema.models import Tema
from django.core import serializers
from Apps.Actividad.models import infoac
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
#
