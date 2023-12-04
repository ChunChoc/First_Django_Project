from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    razon_visita = models.TextField()
    receta_medica = models.TextField()
    numero_telefonico = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre
    
class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    numero_colegiado = models.CharField(max_length=30, unique=True)
    especialidad = models.CharField(max_length=100)
    diagnostico = models.TextField()

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"