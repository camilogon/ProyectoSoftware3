# Generated by Django 2.0.4 on 2018-06-24 23:57

import Apps.Cuestionario.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tema', '0001_initial'),
        ('Profesor', '0001_initial'),
        ('Curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enunciado', models.CharField(max_length=30, unique=True, validators=[Apps.Cuestionario.models.titulo_validation])),
                ('Respuesta', models.BooleanField(default=False)),
                ('CodigoTema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tema.Tema')),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
                ('idProfesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor')),
            ],
        ),
    ]
