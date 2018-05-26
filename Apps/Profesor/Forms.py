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

		widgets={'Cedula':forms.TextInput(attrs={'class' : 'form-control'}),
		          'Nombre':forms.TextInput(attrs={'class' : 'form-control'}),
		          'Apellido':forms.TextInput(attrs={'class' : 'form-control'}),
				  'Ciudad': forms.TextInput(attrs={'class': 'form-control'}),
				  'Correo':forms.TextInput(attrs={'class' : 'form-control'}),
				  'Telefono':forms.TextInput(attrs={'class' : 'form-control'}),}
