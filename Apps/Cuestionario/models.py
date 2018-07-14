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
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE,default=2751234)
    Enunciado = models.CharField(max_length=250, unique=True, validators=[titulo_validation])
    Respuesta = models.BooleanField()

    def ListarCuestionarios(idMateira , idcurso):
        query = 'SELECT DISTINCT c.* FROM ((materia_materia m INNER JOIN tema_tema t on m.id = t.idMateria_id)INNER JOIN cuestionario_cuestionario c on t.Codigo = c.CodigoTema_id )LEFT outer JOIN preguntascuestionario_preguntascuestionario pc on pc.CodigoCuestionario_id= c.id  WHERE m.id ='+str(idMateira)+' and pc.idCurso_id = '+str(idcurso)
        Cuestionarios = Cuestionario.objects.raw ( query )
        return Cuestionarios

    def ListarCuestionariosResolver(idCuestionario):
        query = 'SELECT DISTINCT c.* FROM cuestionario_cuestionario c INNER JOIN preguntascuestionario_preguntascuestionario pc on c.id=pc.CodigoCuestionario_id where pc.id= '+ str(idCuestionario)
        Cuestionarios = Cuestionario.objects.raw ( query )
        return Cuestionarios
