from django.shortcuts import render
#from django.http import HttpResponse
from base.forms import ContatoForm

def inicio(request):
    return render(request,'inicio.html')

def contato(request):
    sucesso = False
    if request.method =='GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'telefone': '(351) 914 505 598/PT ou chame whatsapp.',
        'responsavel': 'Jackson Moreira',
        'form': form,
        'sucesso': sucesso
    } 
    return render(request, 'contato.html', contexto)

# Create your views here.