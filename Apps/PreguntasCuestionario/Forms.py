from django import forms
from Apps.Cuestionario.models import Cuestionario
from django.forms import ModelForm
from Apps.Tema.models import Tema
from Apps.Actividad.models import infoac

class DateInput(forms.DateInput):
    input_type = 'date'


class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = Cuestionario
        fields = ['Enunciado', 'Respuesta']
        labels = {
            'Enunciado': 'Enunciado de la pregunta :',
            'Respuesta': 'Respuesta a la pregunta :'
        }

        widgets = {
            #'CodigoTema': forms.Select(attrs={'class': 'form-control'},choices=Tema.seleccionarTema(infoac.idMateria)) ,
            'Enunciado': forms.TextInput(attrs={'class': 'form-control',"id":'hola'}),
            'Respuesta': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
