from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Curso.Forms import CursoForm
from Apps.Curso.models import Curso

# Create your views here.
def Inicio(request):
    return render_to_response("Cursos/ListarCurso.html", {"Cursos": Curso.objects.all(), "messages": messages.get_messages(request)})

def ListarCurso(request):
    return render_to_response("Cursos/ListarCurso.html", {"Cursos": Curso.objects.all(), "messages": messages.get_messages(request)})


def CrearCurso(request):
    form = CursoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "se Ha guardado un nuevo Curso!")
            return HttpResponseRedirect("/Curso/ListarCurso")
    return render(request, 'Cursos/CrearCurso.html', {'form': form})


def EditarCurso(request, id):
    instance = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El Curso ha sido modificado correctamente!")
            return HttpResponseRedirect("/Curso/ListarCurso")

    return render(request, 'Cursos/EditarCurso.html', {'form': form})


def EliminarCurso(request, id):
    instance = get_object_or_404(Curso, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El Curso con id %s ha sido Eliminado!" % id)
    return HttpResponseRedirect("/Cursos/ListarCurso")

