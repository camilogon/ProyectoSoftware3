from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Cuestionario.Forms import CuestionarioForm
from Apps.Cuestionario.models import Cuestionario
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from Apps.Tema.models import Tema
from django.core import serializers
from Apps.Actividad.models import infoac
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
#
def Index(request):
    return render_to_response("index.html",{"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages(request)})

@csrf_exempt
def ListarMateria(request):
    dato = request.GET.get('id')
    infoac.datos=dato
    #print("llegue"+ dato)
    dict= Materia.ListarMaterias(2751234,dato)
    resp = serializers.serialize("json", dict)
    #print(resp)
    return JsonResponse(str(resp),safe=False)


def ListarCuestionario(request,idMateria):
    infoac.idMateria = idMateria
    print(infoac.datos)
    return render_to_response("Cuestionarios/ListarCuestionario.html", {"Cursos": Curso.Listarcursos(2751234),"Cuestionarios": Cuestionario.ListarCuestionarios(idMateria,infoac.datos),"Materia":idMateria ,"messages": messages.get_messages(request)})



def CrearCuestionario(request,idMateria):
    form = CuestionarioForm ( request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cuestionario=Cuestionario()
            cuestionario.Enunciado=request.POST['Enunciado']
            #print("soy el checkbox "+ str(request.POST.get('Respuesta')))
            respuesta=request.POST.get('Respuesta')
            if(respuesta=='on'):
            #    print("entre al if")
                cuestionario.Respuesta=1
            #    print(Cuestionario.Respuesta)
            else:
                cuestionario.Respuesta =0
            #   print ( cuestionario.Respuesta )
            #cuestionario.idCurso= Curso(infoac.datos)
            cuestionario.CodigoTema= Tema(request.POST.get('CodigoTema'))
            cuestionario.save()
            messages.add_message(request, messages.SUCCESS, "guardada Cuestionario")
            return HttpResponseRedirect("/Cuestionario/ListarCuestionario/"+str(idMateria),{"Actividades":Cuestionario.ListarCuestionarios(infoac.idMateria,infoac.datos) , "Materia": idMateria ,"Cursos": Curso.Listarcursos(2751234), "messages": messages.get_messages ( request )})
    return render(request, 'Cuestionarios/CrearCuestionario.html', {'form': form,"Temas":Tema.seleccionarTema(idMateria)},)


