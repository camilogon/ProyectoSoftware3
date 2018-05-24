from django import forms
from Apps.Profesor.models import Profesor

class ProfesorForm(forms.ModelForm):
	class Meta:
		model= Profesor
		fields= ['Nombre','Apellido','Direccion','Correo','Curso','Contrasena','Telefono',]
		labels={'Nombre':'nombre Profesor',
		        'Apellido':'apellido Profesor',
		        'Direccion':'direccion',
				'Correo':'Correo',
				'Curso':'Curso',
				'Contrasena':'Contrasena',
				'Telefono':'Telefono',}

		widgates={'Nombre':forms.TextInput(attrs={'class' : 'myfieldclass'}),
		          'Apellido':forms.TextInput(attrs={'class' : 'myfieldclass'}),
		          'Direccion':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Correo':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Curso':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Contrasena':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Telefono':forms.TextInput(attrs={'class' : 'myfieldclass'}),}
