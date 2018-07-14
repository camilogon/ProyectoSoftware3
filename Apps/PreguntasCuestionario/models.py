from datetime import time
from django.db import models
from Apps.Profesor.models import Profesor
from Apps.Cuestionario.models import Cuestionario
from Apps.CuestionarioGeneral.models import CuestionarioGeneral
from Apps.Curso.models import Curso
from django.core.exceptions import ValidationError



def titulo_validation(value):
    if not len(value) > 1:
        raise ValidationError('no se puede dejar campo en blanco')


class PreguntasCuestionario(models.Model):
    CodigoCuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    idCurso = models.ForeignKey (Curso, on_delete=models.CASCADE)
    CodigoCuestionarioGeneral = models.ForeignKey (CuestionarioGeneral,on_delete=models.CASCADE)
    RespuestaEstudiante = models.BooleanField()


