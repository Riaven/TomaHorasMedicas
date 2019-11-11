from django.shortcuts import render, redirect
from .forms import ProfesionalForm
# Create your views here.

#Crear nuevo profesional
def NuevoProfesional(request):
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
            form = ProfesionalForm()
    return render(request, 'administracion/nuevoprofesional.html', {'form': form})