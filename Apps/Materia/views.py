from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Materia.Forms import MateriaForm
from Apps.Materia.models import Materia

# Create your views here.

def ListarMateria(request):
    return render_to_response("Materias/ListarMateria.html", {"Materias": Materia.objects.all(), "messages": messages.get_messages(request)})


def CrearMateria(request):
    form = MateriaForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "se Ha guardado una nuevo amateria!")
            return HttpResponseRedirect("/Materia/ListarMateria")
    return render(request, 'Materias/CrearMateria.html', {'form': form})


def EditarMateria(request, id):
    instance = get_object_or_404(Materia, id=id)
    form = MateriaForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La materia ha sido modificado correctamente!")
            return HttpResponseRedirect("/Materia/ListarMateria")

    return render(request, 'Materias/EditarMateria.html', {'form': form})


def EliminarMateria(request, id):
    instance = get_object_or_404(Materia, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "La materia con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Materia/ListarMateria")

