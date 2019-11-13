from django.db import models

# Área de atención

class AreaAtencion (models.Model):
    nombre = models.CharField(max_length=50)
    #para que retorne el nombre de la instancia y no el id
    def __str__(self):
        return self.nombre
#Profesional con foto
class Profesional (models.Model):
    nombre = models.CharField(max_length=50)
    sector = models.CharField(max_length=15)
    horarioAtencion = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='static/images/profesionales/')
    areaAtencion = models.ForeignKey(AreaAtencion, default =1, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre