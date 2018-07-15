from django import forms
from Apps.Curso.models import Curso


class CursoForm ( forms.ModelForm ):
    class Meta:
        model = Curso
        fields = ['Nombre' , 'Descripcion' , 'Codigo' , 'CantidadEstudiantes']
        labels = {'Nombre': 'Nombre del curso' ,
                  'Descripcion': 'Descripcion' ,
                  'Codigo': 'Codigo del curso' ,
                  'CantidadEstudiantes': 'Cantidad de estudiantes'
                  }

        widgets = {'Nombre': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   'Descripcion': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   'Codigo': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   'CantidadEstudiantes': forms.TextInput ( attrs={'class': 'form-control'} ) ,
                   }
