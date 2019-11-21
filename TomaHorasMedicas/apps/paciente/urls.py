from apps.paciente.views import nuevoPaciente
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', nuevoPaciente, name='pacientes'),
    

]