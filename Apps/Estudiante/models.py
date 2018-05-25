from django.db import models


class Estudiante(models.Model):
    """docstring for ClassName"""
    CodigoEstudiante = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    FechaNacimieto = models.DateField()
