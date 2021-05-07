from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Cliente
from cpf_field.models import CPFField




class ClienteForm(forms.ModelForm):
    nome_cliente = forms.CharField(required=True, max_length=50)
    telefone_cliente = forms.CharField(required=True, max_length=15)
    endereco_cliente = forms.CharField(required=True, max_length=50)
    cpf_cliente = CPFField()
    email = forms.EmailField(required=True, max_length = 254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(required=True ,max_length=20, widget=forms.PasswordInput)

    def get_password(self):
        return self.password
    class Meta:
        model = Cliente
        fields = ["nome_cliente", 
        "telefone_cliente", 
        "endereco_cliente", 
        "cpf_cliente", "email", "password"]

        error_messages = {
            'nome': {
                'required': 'teste'
            }
        }


