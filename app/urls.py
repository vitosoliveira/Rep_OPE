from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from .views import home,cadastrar,login,produto,perfil,cart




urlpatterns = [
    path('', home),
    path('cadastro', cadastrar, name="cadatroCliente"),
    path('produto', produto, name='produto'),
    path('perfil', perfil, name='perfil'),
    path('cart', cart, name='cart'),     
] 

