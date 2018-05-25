from django import forms
from Apps.Tema.models import Tema


class TemaForm ( forms.ModelForm ):
    class Meta:
        model = Tema
        fields = ['Codigo' , 'Nombre' , 'Descripcion' , 'idMateria']
        labels = {'Codigo': 'Codigo del Tema' ,
                  'Nombre': 'Nombre' ,
                  'Descripcion': 'Descripcion' ,
                  'idMateria': 'Escoja la materia' ,
                  }

        widgets = {'Codigo': forms.TextInput(attrs={'class': 'form-group'}) ,
                    'Nombre': forms.TextInput(attrs={'class': 'form-group'}) ,
                    'Descripcion': forms.TextInput(attrs={'class': 'form-group'}) ,
                    'idMateria': forms.TextInput(attrs={'class': 'form-group'}) ,
                    }
