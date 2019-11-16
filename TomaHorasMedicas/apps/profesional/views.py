from django.shortcuts import render, redirect
from .models import Profesional
from .forms import ProfesionalForm
# Create your views here.

#Crear nuevo profesional
def nuevoProfesional(request):
    if request.method == 'POST':
        form = ProfesionalForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect('profesionales')
    else:
        form = ProfesionalForm()
    return render(request, 'administracion/nuevoprofesional.html', {'form':form})

#Modificar profesional

#ELiminar profesional

#Listar profesionales
def listarProfesionales(request):
    profesional = Profesional.objects.all()
    contexto = {'profesionales':profesional}
    return render (request, 'administracion/listaprofesional.html', contexto)

