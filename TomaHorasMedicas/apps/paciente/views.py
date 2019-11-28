from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.models import User
# Create your views here.

#Crea un usuario a la vez que se crea una nueva ficha médica
def crearUser(user, correo):
    contrasena = User.objects.make_random_password()
    #Guarda la instancia creada en usuario
    usuario =User.objects.create_user(username = user, email = correo, password = contrasena)
    #Se modifica si está activo o no
    usuario.is_active =False
    #Se guarda al usuario
    usuario.save()

#Eliminar user
def eliminarUsuario(user_rut):
    usuario = User.objects.get(username= user_rut)
    #encuentra el usuario y lo elimina
    usuario.delete()

#Eliminar paciente
def eliminarFicha(request, rut):
    #Se obtiene el objeto que tenga el mismo rut que el de la ficha
    paciente = Paciente.objects.get(rut = rut)
    if request.method == 'POST':
        # Se elimina la ficha
        paciente.delete()
        #Se elimina el usuario
        eliminarUsuario(rut)
        return redirect('listar_fichas')
    #Envía el registro de paciente
    return render(request, 'administracion/paciente/eliminarpaciente.html', {'paciente':paciente})

#Para crear una nueva ficha médica
def nuevoPaciente(request):
    #Se van a recibir los datos que se están enviando en el POST
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        #Si lo que recibe fue un post, y el formulario el válido
        if form.is_valid():
            # guarda lo que tiene el formulario
            form.save()
            #Toma los datos individualmente del formulario
            user = request.POST['rut']
            email = request.POST['email']
            #Llama a la funcion para crear un usuario, se le envía el nombre de usuaio y el email
            crearUser(user, email)
        return redirect('listar_fichas')
    #En el caso de que fuera un GET, despliega el formulario
    else:
        form = PacienteForm()
    return render(request, 'administracion/paciente/nuevopaciente.html', {'form': form})

#Listar pacientes
def listarFichas(request):
    paciente = Paciente.objects.all()
    contexto = {'pacientes' : paciente}
    return render(request, 'administracion/paciente/listapacientes.html', contexto)



def modificarPaciente(request, rut):
    paciente = Paciente.objects.get(rut = rut)
    usuario = User.objects.get(username=rut)
    if request.method == 'GET':
        form = PacienteForm(instance= paciente)
    else:
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            correo = request.POST['email']
            usuario.email = correo
            usuario.save()
        return redirect('listar_fichas')
    return render(request, 'administracion/paciente/nuevopaciente.html', {'form': form})
#Toma de horas

#Un usuario no puede tomar más de una hora con un mismo profesional

#ver tope de horas 

#Ver su propia ficha
def verFichaPropia(request):
    #obtiene el rut del usuario o el user name que esta logueado, son lo mismo
    rut_usuario = request.user.username
    #Obtiene el paciente que tenga el username = al rut
    paciente = Paciente.objects.get(rut = rut_usuario)
    #Despliega el formulario
    form = PacienteForm(instance=paciente)
    #Rellena el formulario con los datos del paciente encontrado
    return render(request, 'administracion/paciente/fichapaciente.html', {'form':form})
