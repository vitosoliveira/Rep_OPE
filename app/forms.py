from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from .models import Cliente, Produto
from cpf_field.models import CPFField




class ClienteForm(UserCreationForm):
    cpf = forms.CharField(
        max_length = 14,
        required = False,
    )
    class Meta:
        model = Cliente
        fields = ('first_name','last_name','telefone', 'cpf','username')
        labels = {'username': 'E-mail'}
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class CustomClienteChangeForm(UserChangeForm):
    class Meta:
        model = Cliente
        fields = ('first_name','last_name', 'cpf')

        

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','imagem']