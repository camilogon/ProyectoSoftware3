# Generated by Django 2.0.4 on 2018-05-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('Cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.IntegerField()),
            ],
        ),
    ]
