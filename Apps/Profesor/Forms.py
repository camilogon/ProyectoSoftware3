from django import forms
from Apps.Profesor.models import Profesor

class ProfesorForm(forms.ModelForm):
	class Meta:
		model= Profesor
		fields= ['Cedula','Nombre','Apellido','Ciudad','Correo','Telefono',]
		labels={'Cedula':'Cedula del Profesor',
				'Nombre': 'Nombre del Profesor',
		        'Apellido':'apellido Profesor',
		        'Ciudad':'Ciudad',
				'Correo':'Correo',
				'Telefono':'Telefono',}

		widgates={'Cedula':forms.TextInput(attrs={'class' : 'myfieldclass'}),
		          'Nombre':forms.TextInput(attrs={'class' : 'myfieldclass'}),
		          'Apellido':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Ciudad': forms.TextInput(attrs={'class': 'myfieldclass'}),
				  'Correo':forms.TextInput(attrs={'class' : 'myfieldclass'}),
				  'Telefono':forms.TextInput(attrs={'class' : 'myfieldclass'}),}
