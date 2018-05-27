# Generated by Django 2.0.4 on 2018-05-26 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profesor', '0001_initial'),
        ('Curso', '0001_initial'),
        ('Materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profesor.Profesor')),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
                ('idMateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Materia.Materia')),
            ],
        ),
    ]
