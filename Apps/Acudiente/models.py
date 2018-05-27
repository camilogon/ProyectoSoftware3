from django.db import models

# Create your models here. ccc
from django.db import models

# Create your models here.
class Acudiente(models.Model):
	cedula = models.IntegerField()
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	direccion = models.TextField()
	celular = models.IntegerField()
	cantidadHijos = models.IntegerField()
	correo = models.EmailField()