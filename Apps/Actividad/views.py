from django.http import JsonResponse
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from Apps.Actividad.Forms import ActividadForm
from Apps.Actividad.models import Actividad
from Apps.Curso.models import Curso

from django.core import serializers




# Create your views here.
#
from Apps.Materia.models import Materia


def IndexProfesor(request):
    return render_to_response("Indexprofesor.html",{"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages(request)})

@csrf_exempt
def ListarMateria(request):
    #print(request['POST'])
    #dict = {"navas","hola"}
    #resp = serializers.serialize("json",dict)
    #resp = resp.replace("\"","'")
    #data = {"resp" : resp}
    dato = request.GET.get('id')
    print(dato)
    dict= Materia.ListarMaterias(2751234,dato)
    resp = serializers.serialize("json", dict)
    print(resp)
    return JsonResponse(str(resp),safe=False)


def ListarActividad(request):
    ##Curso.listarCursos(2751232)
    return render_to_response("Actividades/ListarActividad.html", {"Actividades": Actividad.objects.all(), "messages": messages.get_messages(request)})



def CrearActividad(request):
    form = ActividadForm ( request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "guardada actividad")
            return HttpResponseRedirect("/Actividad/ListarActividad")

    return render(request, 'Actividades/CrearActividad.html', {'form': form})


