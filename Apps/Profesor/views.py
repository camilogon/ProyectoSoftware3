from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Profesor.Forms import ProfesorForm
from Apps.Profesor.models import Profesor


# Create your views here.

def ListarProfesor(request):
    return render_to_response("Profesores/ListarProfesor.html", {"Profesores": Profesor.objects.all(), "messages": messages.get_messages(request)})


def CrearProfesor(request):
    form = ProfesorForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ha guardado un nuevo profesor!")
            return HttpResponseRedirect("/Profesor/ListarProfesor")
    return render(request, 'Profesores/CrearProfesor.html', {'form': form})


def EditarProfesor(request, id):
    instance = get_object_or_404(Profesor, Cedula=id)
    form = ProfesorForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "el profesor a sido notificado!")
            return HttpResponseRedirect("/Profesor/ListarProfesor")

    return render(request, 'Profesores/EditarProfesor.html', {'form': form})


def EliminarProfesor(request, id):
    instance = get_object_or_404(Profesor, Cedula=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El profesor con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Profesor/ListarProfesor")
    

