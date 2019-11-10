from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.core import serializers

#Index
def index (request):
    return render(request, 'principal/index.html')

#Quienes somos vista
def somos(request):
    try:
        return render(request, 'principal/quienessomos.html')
    except:
        raise Http404("Error")

#def mostrarNoticia(request, idNoticia):
    
