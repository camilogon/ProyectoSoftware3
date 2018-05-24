from django import forms
from Apps.Curso.models import Curso

class CursoForm(forms.ModelForm):
	class Meta:
		model= Curso
		fields= ['nombre','codigo']
		labels={'nombre':'nombre del curso',
				'codigo':'codigo'
				}

		widgates={'nombre':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'codigo':forms.TextInput(attrs={'class' : 'myfieldclass'}),}
