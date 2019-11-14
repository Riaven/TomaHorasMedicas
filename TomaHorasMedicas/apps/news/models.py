from django.db import models
from datetime import datetime
# Create your models here.
import datetime
class Noticias (models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=300)
    fechaPublicacion = models.DateField()




