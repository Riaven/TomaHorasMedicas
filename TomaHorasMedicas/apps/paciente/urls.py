from apps.paciente.views import nuevoPaciente, verFichaPropia, listarFichas
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', nuevoPaciente, name='pacientes'),
    url(r'^vermificha$', verFichaPropia, name='vermificha'),
    url(r'^listapacientes$', listarFichas, name='listarfichas'),
    

]