from apps.login.views import activarCuenta
from django.conf.urls import include, url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^$', activarCuenta, name='activarcuenta'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'login/confirmarcontrasena.html'},
        name='password_reset_confirm'
        ),
]