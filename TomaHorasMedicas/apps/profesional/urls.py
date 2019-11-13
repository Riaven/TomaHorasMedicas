from apps.profesional.views import NuevoProfesional, listarProfesionales
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', listarProfesionales, name='profesionales'),
    url(r'^nuevo$', NuevoProfesional, name="nuevoprofesional"), 

]
