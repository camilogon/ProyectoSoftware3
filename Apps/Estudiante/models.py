from django.db import models

class Estudiante(models.Model):
	"""docstring for ClassName"""
	Nombre = models.CharField(max_length=50)
	Correo = models.EmailField(max_length=300)
	Curso = models.CharField(max_length=30)
	Contrasena = models.CharField(max_length=50)
	Telefono = models.IntegerField()