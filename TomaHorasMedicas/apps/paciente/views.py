from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.models import User
# Create your views here.

def crearUser(user, correo):
    contrasena = User.objects.make_random_password()
    User.objects.create_user(username = user, email = correo, password = contrasena)

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
        return redirect('profesionales')
    #En el caso de que fuera un GET, despliega el formulario
    else:
        form = PacienteForm()
    return render(request, 'administracion/paciente/nuevopaciente.html', {'form': form})

