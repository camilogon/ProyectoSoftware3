from django import forms
from Apps.Estudiante.models import Estudiante


class EstudianteForm ( forms.ModelForm ):
    class Meta:
        model = Estudiante
        fields = ['CodigoEstudiante' , 'Nombre' , 'Apellido' , 'FechaNacimieto']
        labels = {'CodigoEstudiante': 'Codigo del estudiante' ,
                  'Nombre': 'Nombre' ,
                  'Curso': 'Apellido' ,
                  'FechaNacimiento': 'FechaNacimiento' ,
                  }

        widgate = {'CodigoEsutidante': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'Nombre': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'Apellido': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'FechaNacimiento': forms.TextInput(attrs={'class': 'form-control'}) ,
                    }
