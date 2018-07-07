#-*- coding: utf8 -*-
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from Apps.Actividad.Forms import ActividadForm
from Apps.Actividad.models import Actividad
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from django.core import serializers
from Apps.Tema.models import Tema
from Apps.Actividad.models import infoac


# Create your views here.
#

def IndexProfesor(request):
    return render_to_response("Indexprofesor.html",{"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages(request)})

@csrf_exempt
def ListarMateria(request):
    dato = request.GET.get('id')
    infoac.datos=dato
    print(dato)
    dict= Materia.ListarMaterias(2751234,dato)
    resp = serializers.serialize("json", dict)
    print(resp)
    return JsonResponse(str(resp),safe=False)


def ListarActividad(request,idMateria):
    fecha=Actividad.esfechamayor
    infoac.idMateria=idMateria
    acti=Actividad.ListarActividades(idMateria,infoac.datos)
    print(acti)
    return render_to_response("Actividades/ListarActividad.html",{"Actividades":acti ,"hoy": fecha, "Materia": idMateria ,"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages ( request )})



def CrearActividad(request,idMateria):
    form = ActividadForm ( request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            actividad = Actividad ()
            actividad.Nombre= request.POST.get('Nombre')
            actividad.Descripcion = request.POST['Descripcion']
            actividad.docfile = request.POST['docfile']
            actividad.Fecha_Entrega = request.POST['Fecha_Entrega']
            actividad.idTema=Tema(request.POST.get('CodigoTema'))
            actividad.idCurso= Curso(infoac.datos)
            actividad.save()
            messages.add_message(request, messages.SUCCESS, "guardada actividad")
            return HttpResponseRedirect("/Actividad/ListarActividad/" + str(idMateria),{"Actividades": Actividad.ListarActividades(idMateria,infoac.datos) , "Materia": idMateria ,"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages ( request )})
    return render(request, 'Actividades/CrearActividad.html', {'form': form,"Temas":Tema.seleccionarTema(idMateria)})


