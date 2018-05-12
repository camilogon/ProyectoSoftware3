from django import forms
from Apps.Estudiante.models import Estudiante

class EstudianteForm(forms.ModelForm):
	class Meta:
		model= Estudiante
		fields= ['Nombre','Correo','Curso','Contrasena','Telefono',]
		labels={'Nombre':'nombre Estudiante',
				'Correo':'Correo',
				'Curso':'Curso',
				'Contrasena':'Contrasena',
				'Telefono':'Telefono',}

		widgates={'Nombre':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'Correo':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'Curso':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'Contrasena':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'Telefono':forms.TextInput(attrs={'class' : 'myfieldclass'}),}
