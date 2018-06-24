# Generated by Django 2.0.4 on 2018-06-24 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=100)),
                ('idMateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Materia.Materia')),
            ],
        ),
    ]
