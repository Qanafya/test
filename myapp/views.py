from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    workers = Workers.objects.all()
    managers = Managers.objects.all()
    directors = Directors.objects.all()
    return render(request, 'home.html', {'workers':workers, 'managers':managers, 'directors':directors})

def worker(request, id):
    worker = Workers.objects.filter(id=id)
    return render(request, 'info.html', {'info': worker})

def manager(request, id):
    manager = Managers.objects.filter(id=id)
    return render(request, 'info.html', {'info': manager})

def director(request, id):
    director = Directors.objects.filter(id=id)
    return render(request, 'info.html', {'info': director})