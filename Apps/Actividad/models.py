from django.db import models
from Apps.Profesor.models import Profesor
from Apps.Tema.models import Tema
from Apps.Curso.models import Curso

class Actividad(models.Model):
	
	
	Nombre = models.CharField(max_length=30)
	Estado_Actividad = models.CharField(max_length=30)	
	Fecha_Creacion = models.DateField()
	Descripcion = models.CharField(max_length=30)
	idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
	idTema = models.ForeignKey(Tema, on_delete=models.CASCADE)
	idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	Fecha_Entrega = models.DateField()
