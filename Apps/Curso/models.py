from django.db import models

# Create your models here. ccc
from django.db import models
from Apps.Estudiante.models import Estudiante


# Create your models here.
class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    CodigoEstudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    CantidadEstudiantes = models.IntegerField()
