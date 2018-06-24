from datetime import time
from django.db import models
from Apps.Profesor.models import Profesor
from Apps.Tema.models import Tema
from Apps.Curso.models import Curso
from django.core.exceptions import ValidationError



def titulo_validation(value):
    if not len(value) > 1:
        raise ValidationError('no se puede dejar campo en blanco')


class Cuestionario(models.Model):
    CodigoTema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Enunciado = models.CharField(max_length=30, unique=True, validators=[titulo_validation])
    Respuesta = models.BooleanField(default=False)



    
