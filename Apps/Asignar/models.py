from django.db import models

# Create your models here. ccc
from django.db import models
from Apps.Curso.models import Curso
from Apps.Profesor.models import Profesor
from Apps.Materia.models import Materia


# Create your models here.
class Asignar ( models.Model ):
    cedula = models.ForeignKey ( Profesor , on_delete=models.CASCADE )
    idCurso = models.ForeignKey ( Curso , on_delete=models.CASCADE )
    idMateria = models.ForeignKey ( Materia , on_delete=models.CASCADE )
