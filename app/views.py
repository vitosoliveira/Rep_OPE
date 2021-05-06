from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

# from django.http import HttpResponse


def home (request):
    return render (request, 'home.html')

def cadastrar (request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome_cliente')
            raw_password = form.cleaned_data.get('senha')
            user = authenticate(username=nome, password=raw_password)
            return redirect('/')
    else:
        form = ClienteForm()
    return render (request, 'cadastro.html', {'form':form})

