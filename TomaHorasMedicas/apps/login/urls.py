from apps.login.views import activarCuenta
from django.conf.urls import include, url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView, LogoutView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name= 'login'),
    url(r'^logout$', LogoutView.as_view(), name= 'logout'),
    url(r'^activarcuenta$', activarCuenta, name='activarcuenta'),
    #La carpeta registration y los templates se deben de llamar igual que originalmente en Django, para poder sobreescribirlos
    url(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]