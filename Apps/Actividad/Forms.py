from django import forms
from Apps.Actividad.models import Actividad
from django.forms import ModelForm



class DateInput (forms.DateInput):
    input_type = 'date'


class ActividadForm(forms.ModelForm):
	class Meta:
		model= Actividad
		fields= ['Nombre','Estado_Actividad','Fecha_Creacion','Descripcion','idProfesor','idTema','idCurso','filename', 'docfile', 'Fecha_Entrega']
		labels={
				'Nombre' : 'Nombre',
				'Estado_Actividad' : 'Estado Actividad',
				'Fecha_Creacion':'Fecha Creacion',
				'Descripcion':'Descripcion Actividad',
				'idProfesor' : 'Id Profesor',
				'idTema' : 'Id Tema',
				'idCurso' : 'Id Curso',
				'filename' : 'name archivo',
				'docfile' : 'docfiles',
				'Fecha_Entrega' : 'Fecha_Entrega'
				}

		widgets={
					'Nombre':forms.TextInput(attrs={'class' : 'form-control'}),
					'Estado_Actividad':forms.TextInput(attrs={'class' : 'form-control'}),
					'Fecha_Creacion':forms.DateInput(attrs={'type':'date','class' : 'form-control'}),
					'Descripcion':forms.TextInput(attrs={'class' : 'form-control'}),
					'idProfesor':forms.Select(attrs={'class' : 'form-control'}),
					'idTema':forms.Select(attrs={'class' : 'form-control'}),
					'idCurso':forms.Select(attrs={'class' : 'form-control'}),
					'filename':forms.TextInput(attrs={'class' : 'form-control'}),
					'docfile':forms.FileInput(attrs={'class' : 'form-control'}),
					'Fecha_Entrega':forms.DateInput(attrs={'type':'date','class' : 'form-control'}),
						
					}
