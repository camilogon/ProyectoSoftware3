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

        widgtes = {'CodigoEsutidante': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'Nombre': forms.TextInput(attrs={'class': 'form-group'}) ,
                    'Apellido': forms.TextInput(attrs={'class': 'form-group'}) ,
                    'FechaNacimiento': forms.TextInput(attrs={'class': 'form-group'}) ,
                    }
