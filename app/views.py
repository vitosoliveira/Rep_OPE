from django.shortcuts import render
from .forms import ClienteForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password, check_password
from .models import Cliente
from django.contrib.auth.hashers import PBKDF2PasswordHasher
# from django.http import HttpResponse


def home (request):
    return render (request, 'home.html')

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

