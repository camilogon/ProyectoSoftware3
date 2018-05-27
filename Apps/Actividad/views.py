from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from Apps.Actividad.Forms import ActividadForm
from Apps.Actividad.models import Actividad




# Create your views here.
#

def ListarActividad(request):

    return render_to_response("Actividades/ListarActividad.html", {"Actividades": Actividad.objects.all(), "messages": messages.get_messages(request)})



def CrearActividad(request):
    form = ActividadForm ( request.POST or None , request.FILES)
    if request.method == 'POST':
        if form.is_valid ():
            form.save ()
            messages.add_message(request, messages.SUCCESS, "guardada actividad")
            return HttpResponseRedirect("/Actividad/ListarActividad")
    return render(request, 'Actividades/CrearActividad.html', {'form': form})


