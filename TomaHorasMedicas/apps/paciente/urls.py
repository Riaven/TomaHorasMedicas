from apps.paciente.views import nuevoPaciente, verFichaPropia, listarFichas, eliminarFicha, modificarPaciente, listarFichas
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', listarFichas, name='pacientes'),
    url(r'^nuevo$', nuevoPaciente, name='nuevo_paciente'),
    url(r'^vermificha$', verFichaPropia, name='ver_mi_ficha'),
    url(r'^listapacientes$', listarFichas, name='listar_fichas'),
    url(r'^eliminar/(?P<rut>\d+)/$', eliminarFicha, name='eliminar_ficha'),
    url(r'^modificarpaciente/(?P<rut>\d+)/$', modificarPaciente, name='modificar_paciente'),
    

]