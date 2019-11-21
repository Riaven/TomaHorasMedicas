from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
# Create your views here.

def nuevoPaciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profesionales')
    else:
        form = PacienteForm()
    return render(request, 'administracion/paciente/nuevopaciente.html', {'form': form})
