from django.db import models


class Profesor(models.Model):
    Cedula = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)
    Correo = models.EmailField()
    Telefono = models.IntegerField()
