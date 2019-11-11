from apps.profesional.views import NuevoProfesional
from django.conf.urls import include, url


urlpatterns = [
   # url(r'^$', index, name='profesionales'),
    url(r'^nuevo$', NuevoProfesional, name="nuevoprofesional"), 
]
