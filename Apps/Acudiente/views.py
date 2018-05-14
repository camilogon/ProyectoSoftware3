from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Acudiente.Forms import AcudienteForm
from Apps.Acudiente.models import Acudiente

# Create your views here.

def ListarAcudiente(request):
    return render_to_response("Acudientes/ListarAcudiente.html", {"Acudientes": Acudiente.objects.all(), "messages": messages.get_messages(request)})


def CrearAcudiente(request):
    form = AcudienteForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "se Ha guardado un nuevo acudiente!")
            return HttpResponseRedirect("/Acudiente/ListarAcudiente")
    return render(request, 'Acudientes/CrearAcudiente.html', {'form': form})


def EditarAcudiente(request, id):
    instance = get_object_or_404(Acudiente, id=id)
    form = AcudienteForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El acudiente ha sido modificado correctamente!")
            return HttpResponseRedirect("/Acudiente/ListarAcudiente")

    return render(request, 'Acudientes/EditarAcudiente.html', {'form': form})


def EliminarAcudiente(request, id):
    instance = get_object_or_404(Acudiente, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El acudiente con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Acudiente/ListarAcudiente")

