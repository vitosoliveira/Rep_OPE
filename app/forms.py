from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(forms.ModelForm):
    nome_cliente = forms.CharField(required=True, max_length=50)
    telefone_cliente = forms.CharField(required=True, max_length=15)
    endereco_cliente = forms.CharField(required=True, max_length=50)
    cpf_cliente = forms.CharField(required=True, max_length=15 )
    email = forms.EmailField(required=True, max_length = 254, help_text='Required. Inform a valid email address.')
    senha = forms.CharField(required=True ,max_length=20)
    class Meta:
        model = User
        fields = ["username","nome_cliente", 
        "telefone_cliente", 
        "endereco_cliente", 
        "cpf_cliente", "email", "senha"]

