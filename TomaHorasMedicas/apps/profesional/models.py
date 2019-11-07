from django.db import models

# Área de atención

class AreaAtencion (models.Model):
    nombre = models.CharField(max_length=50)
    #para que retorne el nombre de la instancia y no el id
    def __str__(self):
        return self.nombre