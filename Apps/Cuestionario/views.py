from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Cuestionario.Forms import CuestionarioForm
from Apps.Cuestionario.models import Cuestionario
from Apps.Curso.models import Curso
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from django.core import serializers




# Create your views here.
#

def ListarCuestionario(request):
    return render_to_response("Cuestionarios/ListarCuestionario.html", {"Cuestionarios": Cuestionario.objects.all(), "messages": messages.get_messages(request)})



def CrearCuestionario(request):
    form = CuestionarioForm ( request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "guardada Cuestionario")
            return HttpResponseRedirect("/Cuestionario/ListarCuestionario")

    return render(request, 'Cuestionarios/CrearCuestionario.html', {'form': form})


