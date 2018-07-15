from django import forms
from Apps.Tema.models import Tema


class TemaForm ( forms.ModelForm ):
    class Meta:
        model = Tema
        fields = ['Codigo' , 'Nombre' , 'Descripcion' , 'idMateria']
        labels = {'Codigo': 'Escoja el Tema' ,
                  'Nombre': 'Nombre' ,
                  'Descripcion': 'Descripcion' ,
                  'idMateria': 'Escoja la materia' ,
                  }

        widgets = {'Codigo': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'Nombre': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'Descripcion': forms.TextInput(attrs={'class': 'form-control'}) ,
                    'idMateria': forms.Select(attrs={'class': 'form-control'}) ,
                    }
