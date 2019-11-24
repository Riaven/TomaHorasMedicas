from django.shortcuts import render
from .forms import RecuperarCuenta
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

#Para poder enviar email
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


#activar mi cuenta
def activarCuenta(request):
    #Si el método es post
    if request.method == 'POST':
        #Toma los datos del form 
        form  = RecuperarCuenta(request.POST)
        #si el formulario es válido
        if form.is_valid():
            #la variable toma el rut del formulario
            userrut = request.POST['rut']
            #try por si no se encuentra el usuario
            try:
                #Usuario toma el objeto que se encontro con el rut
                usuario = User.objects.get(username = userrut)
                
                #Si el usuario esta activo 
                if usuario.is_active:
                    return HttpResponse('User ya esta activo')
                else:
                    #Cuando está inactivo, cambia el estado del usuario a activo
                    usuario.is_active = True
                    #Obtiene el correo del usuario solicitado
                    correo = usuario.email
                    #guarda los cambios del usuario
                    usuario.save()
                    
                    #Asunto de activación de cuenta
                    asunto = 'Cambio de contraseña - Activación de cuenta'
                    cambiarContrasena(correo)
                    #enviaEmail(correo, asunto)
                return HttpResponse('User activado :) al correo ' + correo)
               
            except Exception as e:
                 return HttpResponse(e)

    #si el metodo el GET
    else:
        #En el caso de que sea GET, envía el formulario vacío
        form = RecuperarCuenta()
    #Retorna el formulario
    return render(request, 'login/activarcuenta.html', {'form': form})

#Enviar email de recuperación de cuenta, recibe el correo al que se debe de enviar la recuperación 
#y el asunto, ya que es de activar cuenta, tendrá otro asunto cuando sea de ha olvidado la contraseña
def enviaEmail(correo, asunto):
   # mensaje_html = render_to_string('login/cambiocontrasena.html')
    contenido = strip_tags(mensaje_html)
    envia = 'librerialmg@gmail.com'
    

    #mail.send_mail(asunto, contenido, envia, [correo]) 

def cambiarContrasena(correo):
    template = 'login/cambiocontrasena.html'
    form = PasswordResetForm({'email' : correo})
    if form.is_valid():
        return form.save(email_template_name=template, domain_override="localhost:8000")
        