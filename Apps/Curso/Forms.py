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

		widgets={'Nombre':forms.TextInput(attrs={'class' : 'form-control'}),
				  'Descripcion':forms.TextInput(attrs={'class' : 'form-control'}),
				  'Codigo': forms.TextInput(attrs={'class': 'form-control'}),
				  'CantidadEstudiante': forms.TextInput(attrs={'class': 'form-control'}),
				  }
