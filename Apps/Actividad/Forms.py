from django import forms
from Apps.Actividad.models import Actividad
from Apps.Actividad.models import infoac
from Apps.Tema.models import Tema
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['Nombre', 'Descripcion','docfile', 'Fecha_Entrega']
        labels = {
            'Nombre': 'Titulo Actividad:',
            'Descripcion': 'Descripción Actividad:',
            #'idTema': 'Tema:',
            'docfile': 'Archivo:',
            'Fecha_Entrega': 'Fecha Entrega:',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            #'idTema': forms.Select(attrs={'class': 'form-control'}),
            'docfile': forms.FileInput(attrs={'class': 'form-control'}),
            'Fecha_Entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }



