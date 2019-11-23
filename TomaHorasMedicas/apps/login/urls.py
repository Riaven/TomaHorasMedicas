from apps.login.views import activarCuenta
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', activarCuenta, name='activarcuenta'),
]