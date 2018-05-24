from django.db import models

# Create your models here. ccc
from django.db import models

# Create your models here.
class Curso(models.Model):

	nombre = models.CharField(max_length=50)

	codigo = models.CharField(max_length=50)
	
