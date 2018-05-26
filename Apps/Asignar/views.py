from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Asignar.Forms import AsignarForm
from Apps.Asignar.models import Asignar

# Create your views here.

def ListarAsignaciones(request):
    return render_to_response("Asignaciones/ListarAsignaciones.html", {"Asignaciones": Asignar.objects.all(), "messages": messages.get_messages(request)})


def CrearAsignaciones(request):
    form = AsignarForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Se ha guardado un nuevo acudiente!")
            return HttpResponseRedirect("/Asignar/ListarAsignaciones")
    return render(request, 'Asignaciones/CrearAsignaciones.html', {'form': form})


def EditarAsignaciones(request, id):
    instance = get_object_or_404(Asignar, id=id)
    form = AsignarForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El acudiente ha sido modificado correctamente!")
            return HttpResponseRedirect("/Asignar/ListarAsignaciones")
    return render(request, 'Asignaciones/EditarAsignaciones.html', {'form': form})


def EliminarAsignaciones(request, id):
    instance = get_object_or_404(Asignar, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El acudiente con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Asignar/ListarAsignaciones")

