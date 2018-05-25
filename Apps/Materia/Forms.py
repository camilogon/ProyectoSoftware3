from django import forms
from Apps.Materia.models import Materia


class MateriaForm ( forms.ModelForm ):
    class Meta:
        model = Materia
        fields = ['Nombre' , 'Descripcion']
        labels = {
            'Nombre': 'nombre' ,
            'Descripcion': 'Descripcion' ,
        }

        widgates = {'Nombre': forms.TextInput ( attrs={'class': 'myfieldclass'} ) ,
                    'Descripcion': forms.TextInput ( attrs={'class': 'myfieldclass'} ) ,
                    }
