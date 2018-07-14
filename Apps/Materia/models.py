from django.db import models

# Create your models here. ccc
from django.db import models


# Create your models here.
class Materia( models.Model ):
    Nombre = models.CharField ( max_length=50 )
    Descripcion = models.CharField ( max_length=100 )

    def ListarMaterias(idprofesor,idcurso):
        query = 'SELECT DISTINCT m.* FROM materia_materia m INNER JOIN asignar_asignar a on m.id=a.idMateria_id WHERE a.cedula_id='+str(idprofesor)+' and a.idCurso_id='+str(idcurso)
        Materias = Materia.objects.raw(query)
        return Materias

    def ListarMateriasEstudiante(IdEstudiante):
        query = 'SELECT DISTINCT m.* FROM ((estudiante_estudiante e INNER JOIN curso_curso c on e.Curso_id= c.id) INNER JOIN asignar_asignar a on a.idCurso_id = c.id)' \
                'inner JOIN materia_materia m on m.id=a.idMateria_id where e.CodigoEstudiante='+str(IdEstudiante)
        Materias = Materia.objects.raw(query)
        return Materias