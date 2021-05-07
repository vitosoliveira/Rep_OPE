from django.urls import path

from .views import home,cadastrar

urlpatterns = [
    path('', home),
    path('cadastro', cadastrar, name="cadatroCliente", )
]
