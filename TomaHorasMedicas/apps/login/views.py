from django.shortcuts import render
from .forms import RecuperarCuenta
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

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
                    #guarda los cambios del usuario
                    usuario.save()
                return HttpResponse('User activado :)')
               
            except:
                 return HttpResponse('El user no existe')
    #si el metodo el GET
    else:
        #En el caso de que sea GET, envía el formulario vacío
        form = RecuperarCuenta()
    #Retorna el formulario
    return render(request, 'login/activarcuenta.html', {'form': form})

#Enviar email de recuperación de cuenta