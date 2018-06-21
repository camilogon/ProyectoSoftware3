from django.db import models

# Create your models here. ccc
from django.db import models
#from Apps.Asignar.models import Asignar



# Create your models here.
class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    CantidadEstudiantes = models.IntegerField()

    def Listarcursos(idprofesor):
        query = 'SELECT distinct c.* FROM asignar_asignar a inner join curso_curso c ON a.idCurso_id= c.id where a.cedula_id =' + idprofesor
        cursos = Curso.objects.raw(query)
        return cursos

