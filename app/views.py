from docesdaleite.settings import AUTH_USER_MODEL
from .forms import ClienteForm, ProdutoModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .models import Cliente
from django.template import RequestContext
from django.contrib.messages import constants

# from django.http import HttpResponse


def home (request):
    return render (request, 'home.html')

def produto(request):
    return render(request, 'produto.html')


def cadastrar (request):
    if request.method == 'POST':   
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClienteForm()
    return render (request, 'cadastro.html', {'form':form})


def perfil (request):
    if AUTH_USER_MODEL == login:
        return render (request, 'perfil.html')
    else:
        return redirect('login')
    

def cart (request):
    return render(request, 'cart.html')


