from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from apps.news.forms import NoticiasForm

#Index
def index (request):
    return render(request, 'principal/index.html')

#Quienes somos vista
def somos(request):
    try:
        return render(request, 'principal/quienessomos.html')
    except:
        raise Http404("Error")

def crearNoticia(request):
    if request.method == 'POST':
        form = NoticiasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = NoticiasForm()
    return render (request, 'principal/crearnoticia.html', {'form': form})