from apps.profesional.views import nuevoProfesional, listarProfesionales
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings

urlpatterns = [
    url(r'^$', listarProfesionales, name='profesionales'),
    url(r'^nuevo$', nuevoProfesional, name="nuevoprofesional"), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# se debe de agregar a las url de cada a´pp
