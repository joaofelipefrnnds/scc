from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'contrato/index.html')

def cadastro_contrato(request):
    return render(request, 'contrato/cadastro_contrato.html')

def cadastro_empresa(request):
    return render(request, 'contrato/cadastro_empresa.html')