from django.db import models
from datetime import datetime

# Create your models here.
class Paciente (models.Model):
    TIPO_PROBLEMAS = (('Cardiaco', 'Cardiaco'),
                      ('Endocrino', 'Endocrino'),
                      ('Circulación', 'Circulación'),
                      ('Digestivo', 'Digestivo'),
                      ('Tensión arterial', 'Tensión arterial'),
                      ('Ninguno', 'Ninguno'))
    ESTADO_CIVIL = (('Soltero' , 'Soltero'),
                    ('Viudo' , 'Viudo'),
                    ('Casado' , 'Casado'),
                    ('Divorciado' , 'Divorciado'))
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    estadoCivil = models.CharField(max_length=10, choices=ESTADO_CIVIL, default=ESTADO_CIVIL[0])
    numeroHijos = models.IntegerField()
    problemasSalud = models.CharField(max_length=20, choices=TIPO_PROBLEMAS, default=TIPO_PROBLEMAS[5])
    peso = models.IntegerField()
    altura = models.IntegerField()

    def __str__(self):
        return self.nombre
