from django.db import models
from Apps.Materia.models import Materia


class Tema(models.Model):
    """docstring for ClassName"""
    Codigo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    idMateria = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Nombre)

    def listarTema(idmateria):
        Materias = Materia.objects.all().filter(idMateria_id=idmateria)
        return Materias

    def seleccionarTema(idMateria):
        query = 'SELECT * FROM tema_tema where idMateria_id =' + str ( idMateria )
        tema = Tema.objects.raw ( query )
        return tema
