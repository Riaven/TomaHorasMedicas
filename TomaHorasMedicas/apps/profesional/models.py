from django.db import models

# Área de atención

class AreaAtencion (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre