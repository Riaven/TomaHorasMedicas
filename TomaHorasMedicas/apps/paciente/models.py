from django.db import models
from datetime import datetime

# Create your models here.
class Paciente (models.Model):
    TIPO_PROBLEMAS = (('C', 'Cardiaco'),
                      ('E', 'Endocrino'),
                      ('CI', 'Circulación'),
                      ('D', 'Digestivo'),
                      ('T', 'Tensión arterial'),
                      ('N', 'Ninguno'))
    ESTADO_CIVIL = (('S' , 'Soltero'),
                    ('V' , 'Viudo'),
                    ('C' , 'Casado'),
                    ('D' , 'Divorsiado'))
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=100, default='direccion')
    telefono = models.CharField(max_length=9, default='99999999')
    estadoCivil = models.CharField(max_length=10, choices=ESTADO_CIVIL, default=ESTADO_CIVIL[0])
    numeroHijos = models.IntegerField(default=0)
    problemasSalud = models.CharField(max_length=20, choices=TIPO_PROBLEMAS, default=TIPO_PROBLEMAS[5])
    peso = models.IntegerField(default=99)
    altura = models.IntegerField(default=150)
