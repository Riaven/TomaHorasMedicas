from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index (request):
    return render(request, 'principal/index.html')