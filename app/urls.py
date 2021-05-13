from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,cadastrar,login,produto,perfil

urlpatterns = [
    path('', home),
    path('cadastro', cadastrar, name="cadatroCliente"),
    path('produto', produto, name='produto'),
    path('perfil', perfil, name='perfil'),
]
