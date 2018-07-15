from django import forms
from Apps.Materia.models import Materia


class MateriaForm ( forms.ModelForm ):
    class Meta:
        model = Materia
        fields = ['Nombre', 'Descripcion']
        labels = {
            'Nombre': 'Nombre',

            'Descripcion': 'Descripción',
        }

        widgets = {'Nombre': forms.TextInput ( attrs={'class': 'form-control'} ),
                    'Descripcion': forms.TextInput ( attrs={'class': 'form-control'} ),
                    }
