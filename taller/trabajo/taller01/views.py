from django.shortcuts import render
from django.db.models import Sum
from .models import Edificio, Departamento

def index(request):
    total_edificios = Edificio.objects.count()
    total_departamentos = Departamento.objects.count()
    
    context = {
        'total_edificios': total_edificios,
        'total_departamentos': total_departamentos,
    }
    return render(request, 'index.html', context)

def listar_edificios(request):
    edificios = Edificio.objects.all()
    context = {
        'edificios': edificios
    }
    return render(request, 'listar_edificios.html', context)

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos': departamentos
    }
    return render(request, 'listar_departamentos.html', context)
