"""TomaHorasMedicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from apps.news import urls as urlNoticias
from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #Para agregar lo de las noticias
    path('inicio/', include ('apps.news.urls')),
    path('profesionales/', include('apps.profesional.urls')),
    path('pacientes/', include('apps.paciente.urls')),
    url('login/', include('apps.login.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)