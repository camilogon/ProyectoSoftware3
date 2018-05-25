from django import forms
from Apps.Curso.models import Curso

class CursoForm(forms.ModelForm):
	class Meta:
		model= Curso
		fields= ['Nombre','Descripcion','Codigo','CantidadEstudiantes']
		labels={'Nombre':'nombre del curso',
				'Descripcion':'Descripcion',
				'Codigo':'codigo',
				'CantidadEstudiantes':'Cantidad de estudiantes'
				}

		widgates={'Nombre':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Descripcion':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Codigo': forms.TextInput(attrs={'class': 'myfieldclass'}),
				  'CantidadEstudiante': forms.TextInput(attrs={'class': 'myfieldclass'}),
				  }
