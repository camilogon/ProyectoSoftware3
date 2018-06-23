from django.db import models
from Apps.Curso.models import Curso

class Estudiante(models.Model):
    """docstring for ClassName"""
    CodigoEstudiante = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    FechaNacimieto = models.DateField()

    def listarEstudiantesCurso(idcurso):
        Estudiantes = Estudiante.objects.all ().filter ( idcurso )
        return Estudiantes
