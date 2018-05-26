from django import forms
from Apps.Asignar.models import Asignar
from Apps.Curso.models import Curso
from Apps.Materia.models import Materia
from Apps.Profesor.models import Profesor

class AsignarForm ( forms.ModelForm ):
    class Meta:
        model = Asignar
        fields = ['cedula' , 'idMateria' , 'idCurso']
        labels = {'cedula': 'cedula del acudiente' ,
                  'idMateria': 'nombre' ,
                  'idCurso': 'apellido' ,
                  }

        widgets = {'cedula': forms.Select (choices=[ (o.Nombre, str(o)) for o in Profesor.objects.all()],attrs={'class': 'form-control'} ) ,
                   'idMateria': forms.Select (choices=[ (o.Nombre, str(o)) for o in Materia.objects.all()],attrs={'class': 'form-control'} ) ,
                   'idCurso': forms.Select (choices=[ (o.Nombre, str(o)) for o in Curso.objects.all()], attrs={'class': 'form-control'} ) ,
                   }
