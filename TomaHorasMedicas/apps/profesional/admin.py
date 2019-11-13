from django.contrib import admin
from .models import AreaAtencion, Profesional
# Register your models here.

#Se agrega área de atención para ser manipulada por el super usuario
admin.site.register(AreaAtencion)
admin.site.register(Profesional)