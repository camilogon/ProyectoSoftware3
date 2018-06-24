from django.http import JsonResponse
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from Apps.Actividad.Forms import ActividadForm
from Apps.Actividad.models import Actividad
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from django.core import serializers



# Create your views here.
#


class infoac:
    datos=0

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
    infoac.datos=dato
    print(dato)
    dict= Materia.ListarMaterias(2751234,dato)
    resp = serializers.serialize("json", dict)
    print(resp)
    return JsonResponse(str(resp),safe=False)


def ListarActividad(request,idMateria):
    #{"Actividades": Actividad.objects.all () , "Materia": datos , "messages": messages.get_messages ( request )}
    return render_to_response("Actividades/ListarActividad.html",{"Actividades": Actividad.objects.all () , "Materia": idMateria ,"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages ( request )})



def CrearActividad(request,idMateria):
    form = ActividadForm ( request.POST or None)
    print("mas datos"+infoac.datos)
    if request.method == 'POST':
        form.idCurso= infoac.datos
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "guardada actividad")
            return HttpResponseRedirect("/Actividad/ListarActividad/" + str(idMateria),{"Actividades": Actividad.objects.all () , "Materia": idMateria ,"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages ( request )})
    return render(request, 'Actividades/CrearActividad.html', {'form': form})


