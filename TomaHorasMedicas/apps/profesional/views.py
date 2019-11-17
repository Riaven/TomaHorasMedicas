from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profesional
from .forms import ProfesionalForm
# Create your views here.

#Crear nuevo profesional
def nuevoProfesional(request):
    if request.method == 'POST':
        #Envia un post y además solicita subir un archivo
        form = ProfesionalForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect('profesionales')
    else:
        form = ProfesionalForm()
    return HttpResponse('administracion/nuevoprofesional.html')

#Modificar profesional

#ELiminar profesional

#Listar profesionales
def listarProfesionales(request):
    #Carga nuevo profesional
    nuevoProfesional(request)
    #lista a todos los profesionales
    profesional = Profesional.objects.all()
    
    contexto = {'profesionales':profesional, 'form': ProfesionalForm()}
    
    return render (request, 'administracion/listaprofesional.html', contexto)

