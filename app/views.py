from django.shortcuts import render
from .forms import ClienteForm, ProdutoModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password, check_password
from .models import Cliente
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.template import RequestContext
from django.contrib.messages import constants

# from django.http import HttpResponse


def home (request):
    return render (request, 'home.html')

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')
            messages.success(request, 'Produto salvo com sucesso.')
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }

    return render(request, 'produto.html', context)


def cadastrar (request):
    form = ClienteForm(request.POST)
    if request.method == 'POST':   
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            form.save()
            return redirect('/')
    else:
        form = ClienteForm()
    return render (request, 'cadastro.html', {'form':form})

