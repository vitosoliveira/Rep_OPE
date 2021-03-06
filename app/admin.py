from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import ClienteForm, CustomClienteChangeForm
from .models import Cliente, Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('nome' , 'preco', 'slug', 'criado','modificado','ativo', 'tipo')

@admin.register(Cliente)
class CustomClienteAdmin(UserAdmin):
    add_form = ClienteForm
    form = CustomClienteChangeForm
    model = Cliente
    list_display = ('first_name', 'last_name', 'email', 'cpf', 'endereco', 'telefone')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informaçoes Pessoais', {'fields': ('first_name','last_name','cpf','endereco','telefone')}),
        ('Permissoes', {'fields':('is_active', 'is_superuser', 'groups')}),
        ('Datas',{'fields':('last_login','date_joined')})
    )

