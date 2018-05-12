from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Estudiante.Forms import EstudianteForm
from Apps.Estudiante.models import Estudiante


# Create your views here.

def ListarEstudiante(request):
    return render_to_response("Estudiantes/ListarEstudiante.html", {"Estudiantes": Estudiante.objects.all(), "messages": messages.get_messages(request)})


def CrearEstudiante(request):
    form = EstudianteForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ha guardado un nuevo estudiante!")
            return HttpResponseRedirect("/Estudiante/ListarEstudiante")
    return render(request, 'Estudiantes/CrearEstudiante.html', {'form': form})
    




def EditarEstudiante(request, id):
    instance = get_object_or_404(Estudiante, id=id)
    form = EstudianteForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El estudiante ha sido modificada!")
            return HttpResponseRedirect("/Estudiante/ListarEstudiante")

    return render(request, 'Estudiantes/EditarEstudiante.html', {'form': form})


def EliminarEstudiante(request, id):
    instance = get_object_or_404(Estudiante, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El estudiante con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Estudiante/ListarEstudiante")

