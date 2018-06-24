from datetime import time
from django.db import models
from Apps.Profesor.models import Profesor
from Apps.Tema.models import Tema
from Apps.Curso.models import Curso
from django.core.exceptions import ValidationError
from datetime import datetime, date, timedelta


def titulo_validation(value):
    if not len(value) > 1:
        raise ValidationError('no se puede dejar campo en blanco')


def validarFecha(value):
    fecha = datetime.now().date()
    fecha_dada = value
    fecha_final = fecha_dada.strftime('%Y-%m-%d')
    if str(fecha_final) < str(fecha):
        print("Es menor ingrese otra fecha ")
        raise ValidationError('fecha de entrega menor a fecha actual')
    else:
        print("Es mayor")

class Actividad(models.Model):
    Nombre = models.CharField(max_length=30, unique=True, validators=[titulo_validation])
    Fecha_Creacion = models.DateField(auto_now_add=True)
    Descripcion = models.CharField(max_length=30 , validators=[titulo_validation])
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE , default=2751234)
    idTema = models.ForeignKey(Tema, on_delete=models.CASCADE , default=555)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE,default=1)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)
    Fecha_Entrega = models.DateField(validators=[validarFecha])

    #def listarActividades(idprofesor, idcurso):



