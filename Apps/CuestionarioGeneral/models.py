from datetime import time
from django.db import models
from Apps.Profesor.models import Profesor
from Apps.Tema.models import Tema
from Apps.Curso.models import Curso
from django.core.exceptions import ValidationError




class CuestionarioGeneral(models.Model):
    CodigoTema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)


    def ListarCuestionariosGeneral(idMateria,idCurso):
        query='SELECT DISTINCT c.* FROM ((materia_materia m INNER JOIN tema_tema t on m.id = t.idMateria_id)INNER JOIN cuestionariogeneral_cuestionariogeneral c on t.Codigo =c.CodigoTema_id)INNER JOIN asignar_asignar a on a.idMateria_id= m.id where m.id ='+str(idCurso) + ' and m.id = ' +str(idMateria)
        Cuestionarios = CuestionarioGeneral.objects.raw ( query )
        return Cuestionarios

    def ListarNombreCuestionarios(idCuestionario):
        query = 'SELECT * FROM cuestionariogeneral_cuestionariogeneral  WHERE id =' + str ( idCuestionario )
        Cuestionario = CuestionarioGeneral.objects.raw ( query )
        return Cuestionario
