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

		widgates={'cedula':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'nombre':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'apellido':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'direccion':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'celular':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'cantidadHijos':forms.TextInput(attrs={'class' : 'myfieldclass'}),
					'correo':forms.TextInput(attrs={'class' : 'myfieldclass'}),}
