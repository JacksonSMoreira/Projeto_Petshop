from django.shortcuts import render
from base.forms import ContatoForm

def inicio(request):
    return render(request,'inicio.html')

def contato(request):
    if request.method =='GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
    contexto = {
        'telefone': '(351) 914 505 598/PT ou chame whatsapp.',
        'responsavel': 'Jackson Moreira',
        'form': form
    } 
    return render(request, 'contato.html', contexto)

# Create your views here.
