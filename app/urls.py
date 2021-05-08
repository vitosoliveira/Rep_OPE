from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,cadastrar,login

urlpatterns = [
    path('', home),
    path('cadastro', cadastrar, name="cadatroCliente"),
]
