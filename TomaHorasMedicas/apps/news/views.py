from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

#Index
def index (request):
    return render(request, 'principal/index.html')

#Quienes somos vista
def somos(request):
    try:
        return render(request, 'somos.html')
    except:
        raise Http404("Error")