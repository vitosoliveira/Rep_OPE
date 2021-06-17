from docesdaleite.settings import AUTH_USER_MODEL
from .forms import ClienteForm, ProdutoModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .models import  Cliente, Produto
from django.template import RequestContext, context
from django.contrib.messages import constants
from carts.models import Cart


# from django.http import HttpResponse

def home (request):
    return render (request, 'home.html')

def produto(request):
    context={        
        'tamanho': Produto.objects.filter(tipo="Tamanho"),
        'massa': Produto.objects.filter(tipo="Massa"),
        'recheio': Produto.objects.filter(tipo="Recheio"),
        'cobertura': Produto.objects.filter(tipo="Cobertura"),
        'topping': Produto.objects.filter(tipo="Topping")

    }
    return render(request, 'produto.html', context)


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
    items = Cart.objects.filter(user = request.user).first()
    context = {
        'name': request.user.first_name,
        'pedidos': [],
        'produtos':[]
        }    
    if items != None:
        context.update({
            'pedidos': request.user.orders_client.all(),
            'produtos': Cart.objects.filter(user = request.user).first().products.all()
            })
    return render (request, 'perfil.html', context=context)
             
    
