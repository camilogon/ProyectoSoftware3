from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Tema.Forms import TemaForm
from Apps.Tema.models import Tema


# Create your views here.

def ListarTema(request):
    return render_to_response("Temas/ListarTema.html", {"Temas": Tema.objects.all(), "messages": messages.get_messages(request)})


def CrearTema(request):
    form = TemaForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ha guardado un nuevo Tema!")
            return HttpResponseRedirect("/Tema/ListarTema")
    return render(request, 'Temas/CrearTema.html', {'form': form})
    




def EditarTema(request, id):
    instance = get_object_or_404(Tema, Codigo=id)
    form = TemaForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El Tema ha sido modificada!")
            return HttpResponseRedirect("/Tema/ListarTema")

    return render(request, 'Temas/EditarTema.html', {'form': form})


def EliminarTema(request, id):
    instance = get_object_or_404(Tema, Codigo=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El Tema con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Tema/ListarTema")

