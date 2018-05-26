from django import forms
from Apps.Acudiente.models import Acudiente

class AcudienteForm(forms.ModelForm):
	class Meta:
		model= Acudiente
		fields= ['cedula','nombre','apellido','direccion','celular','cantidadHijos','correo']
		labels={'cedula':'cedula del acudiente',
				'nombre':'nombre',
				'apellido':'apellido',
				'direccion':'direccion',
				'celular':'celular',
				'cantidadHijos':'numero de hijos',
				'correo':'correo'}

		widgets={'cedula':forms.TextInput(attrs={'class' : 'form-control'}),
					'nombre':forms.TextInput(attrs={'class' : 'form-control'}),
					'apellido':forms.TextInput(attrs={'class' : 'form-control'}),
					'direccion':forms.TextInput(attrs={'class' : 'form-control'}),
					'celular':forms.TextInput(attrs={'class' : 'form-control'}),
					'cantidadHijos':forms.TextInput(attrs={'class' : 'form-control'}),
					'correo':forms.TextInput(attrs={'class' : 'form-control'}),}
