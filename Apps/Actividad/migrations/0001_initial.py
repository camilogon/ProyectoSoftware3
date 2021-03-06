# Generated by Django 2.0.4 on 2018-07-13 20:07

import Apps.Actividad.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Curso', '0001_initial'),
        ('Tema', '0001_initial'),
        ('Profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30, unique=True, validators=[Apps.Actividad.models.titulo_validation])),
                ('Fecha_Creacion', models.DateField(auto_now_add=True)),
                ('Descripcion', models.CharField(max_length=30, validators=[Apps.Actividad.models.titulo_validation])),
                ('docfile', models.FileField(blank=True, upload_to='documents/%Y/%m/%d')),
                ('Fecha_Entrega', models.DateField(validators=[Apps.Actividad.models.validarFecha])),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
                ('idProfesor', models.ForeignKey(default=2751234, on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor')),
                ('idTema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tema.Tema')),
            ],
        ),
    ]
