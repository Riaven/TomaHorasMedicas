from django.db import models

# Create your models here.
class Noticias (models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=300)
    fechaPublicacion = models.DateField()
    