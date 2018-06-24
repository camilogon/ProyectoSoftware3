from django import forms
from Apps.Cuestionario.models import Cuestionario
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = Cuestionario
        fields = ['CodigoTema','idProfesor','idCurso','Enunciado', 'Respuesta']
        labels = {
            'CodigoTema': 'Codigo Tema',
            'idProfesor': 'ID profesor',
            'idCurso': 'ID Curso',
            'Enunciado': 'Enunciado pregunta:',
            'Respuesta': 'Respuesta pregunta:'
        }

        widgets = {
            'CodigoTema': forms.Select(attrs={'class': 'form-control'}) ,
            'idProfesor': forms.Select(attrs={'class': 'form-control'}) ,
            'idCurso': forms.Select(attrs={'class': 'form-control'}) ,
            'Enunciado': forms.TextInput(attrs={'class': 'form-control'}),
            'Respuesta': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
