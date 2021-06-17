from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from .views import home,cadastrar,produto,perfil
from .classes import password_reset , password_reset_done, password_reset_confirm, password_reset_complete
from app import views 




urlpatterns = [
    path('', home),
    path('cadastro', cadastrar, name="cadatroCliente"),
    path('produto', produto, name='produto'),
    path('perfil', perfil, name='perfil'), 
    path('resetPassword/', password_reset , name='resetPassword'),
    path('cart/', include("carts.urls", namespace="cart")),
    path('resetPassword/password_reset_done/', password_reset_done , name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm , name='password_reset_confirm '),
    path('reset/done', password_reset_complete, name='password_reset_complete'),

    

] 

