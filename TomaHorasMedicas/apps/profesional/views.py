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
        #Despliega solo un html
    return HttpResponse('administracion/nuevoprofesional.html')

#Listar profesionales
def listarProfesionales(request):
    #Carga nuevo profesional
    nuevoProfesional(request)
    #lista a todos los profesionales
    profesional = Profesional.objects.all()
    
    contexto = {'profesionales':profesional, 'form': ProfesionalForm()}
    
    return render (request, 'administracion/listaprofesional.html', contexto)

#Eliminar un profesional
def eliminarProfesional(request, id_profesional):
    profesional = Profesional.objects.get(id = id_profesional)
    if request.method == 'POST':
        profesional.delete()
        redirect('profesionales')
    return (request, 'administracion/eliminarprofesional', {'profesional':profesional})


#Modificar un profesional
def modificarProfesional(request, id_profesional):
    profesional = Profesional.objects.get(id = id_profesional)
    if request.method == 'GET':
        form = ProfesionalForm(instance=profesional)
    else:
        form = ProfesionalForm(request.POST, instance=profesional)
        if form.is_valid():
            form.save()
            return redirect('profesionales')
    return render(request, 'administracion/modificarprofesional.html', {'form': form})


