from apps.login.views import activarCuenta
from django.conf.urls import include, url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^$', activarCuenta, name='activarcuenta'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'login/confirmacioncontrasena.html'}, name='confirmar_contrasena'),
   # url(r'^reset/password_reset', PasswordResetView.as_view(), 
    #    {'template_name':'login/formulariocontrasena.html',
     #       'email_template_name': 'login/cambiocontrasena.html'}), 
]