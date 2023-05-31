from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'inicio.html')

def contato(request):
    contexto = {
        'telefone': '(99) 9999.9999',
        'responsavel': 'Mario da Silva'
    } 
    return render(request, 'contato.html', contexto)

# Create your views here.
