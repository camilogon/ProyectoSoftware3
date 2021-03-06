# Generated by Django 2.0.4 on 2018-07-13 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('CodigoEstudiante', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('FechaNacimieto', models.DateField()),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
            ],
        ),
    ]
