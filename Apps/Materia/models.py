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