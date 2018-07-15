from django import forms
from Apps.Estudiante.models import Estudiante
from Apps.Curso.models import Curso
from django.forms import ModelForm


class DateInput (forms.DateInput):
    input_type = 'date'


class EstudianteForm ( ModelForm ):
    class Meta:
        model = Estudiante
        fields = ['CodigoEstudiante' , 'Nombre' , 'Apellido' ,'Curso', 'FechaNacimieto']
        labels = {'CodigoEstudiante': 'Codigo del estudiante' ,
                  'Nombre': 'Nombre del estudiante' ,
                  'Apellido':'Apellido del estudiante',
                  'Curso' : 'Seleccione el curso del estudiante' ,
                  'FechaNacimieto': 'FechaNacimiento del estudiante' ,
                  }

        widgets = {'CodigoEstudiante': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   'Nombre': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   'Apellido': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   'Curso': forms.Select(attrs={'class': 'form-control'} ) ,
                   'FechaNacimieto': forms.DateInput(attrs={'type':'date', 'class': 'form-control'} ) ,
                   }
