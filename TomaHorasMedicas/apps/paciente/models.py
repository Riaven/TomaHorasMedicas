from django.db import models

# Create your models here.
class Paciente (models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
   # telefono = models.