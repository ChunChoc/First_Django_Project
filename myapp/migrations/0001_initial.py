# Generated by Django 4.2.7 on 2023-11-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero_colegiado', models.CharField(max_length=30, unique=True)),
                ('especialidad', models.CharField(max_length=100)),
                ('diagnostico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dpi', models.CharField(max_length=13, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.TextField()),
                ('razon_visita', models.TextField()),
                ('receta_medica', models.TextField()),
                ('numero_telefonico', models.CharField(max_length=8)),
            ],
        ),
    ]
