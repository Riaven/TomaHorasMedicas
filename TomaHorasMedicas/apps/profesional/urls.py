from apps.profesional.views import nuevoProfesional, listarProfesionales, eliminarProfesional, modificarProfesional
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings

urlpatterns = [
    url(r'^$', listarProfesionales, name='profesionales'),
    #url(r'^nuevo$', nuevoProfesional, name="nuevoprofesional"), 
    url(r'^eliminar/(?P<id>\d+)/$', eliminarProfesional, name='eliminar_profesional'),
    url(r'^modificar/(?P<id>\d+)/$', modificarProfesional, name='modificar_profesional'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# se debe de agregar a las url de cada a´pp
