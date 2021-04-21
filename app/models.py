from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Massa (models.Model):
    id_massa = models.AutoField('id_massa',primary_key = True)
    nome_massa = models.CharField('nome_massa',max_length = 50)
    descricao_massa = models.CharField('descricao',max_length = 250)
    sem_glutem = models.IntegerField('glutem')
    sem_lactose = models.IntegerField('lactose')
    valor_massa = models.DecimalField('valor_massa',max_digits = 6, decimal_places = 2)
    
class Recheio (models.Model):
    id_recheio = models.AutoField('id_recheio', primary_key = True)
    nome_recheio = models.CharField('nome_recheio', max_length = 50)
    descricao_recheio = models.CharField('descricao_recheio', max_length = 250)
    sem_glutem = models.IntegerField('glutem')
    sem_lactose = models.IntegerField('lactose')
    valor_recheio = models.DecimalField('valor_recheio', max_digits = 6, decimal_places = 2)


class Cobertura (models.Model):
    id_cobertura = models.AutoField('cobertura_id', primary_key = True)
    nome_cobertura = models.CharField('nome_cobertura', max_length = 50)
    descricao_cobertura = models.CharField('descricao_cobertura', max_length = 250)
    sem_glutem = models.IntegerField('glutem')
    sem_lactose = models.IntegerField('lactose')
    valor_cobertura = models.DecimalField('valor_cobertura', max_digits = 6, decimal_places = 2)

class Topping (models.Model):
    id_topping = models.AutoField('íd_topping', primary_key = True)
    nome_topping = models.CharField('nome_topping', max_length = 50)
    descricao_topping = models.CharField('descricao_topping', max_length = 250)
    valor_topping = models.DecimalField('valor_topping', max_digits = 6, decimal_places = 2)

class Tamanho (models.Model):
    id_tamanho = models.AutoField('Tamanho', primary_key = True)
    nome_tamanho = models.CharField('nome_tamanho',max_length = 50)
    valor_tamanho = models.FloatField('valor_tamanho',max_length = 20)

class Bolo (models.Model):
    sem_glutem = models.IntegerField('glutem')
    sem_lactose = models.IntegerField('lactose')
    bolo_recheio = models.ForeignKey(Recheio, verbose_name="Bolo_Recheio", on_delete = models.CASCADE)
    bolo_massa = models.ForeignKey(Massa, verbose_name="Boloc_Massa", on_delete=models.CASCADE)
    bolo_topping = models.ForeignKey(Topping, verbose_name="Bolo_Topping", on_delete=models.CASCADE)
    bolo_cobertura = models.ForeignKey(Cobertura, verbose_name="Bolo_cobertura", on_delete=models.CASCADE)
    bolo_tamanho = models.ForeignKey(Tamanho, verbose_name="Bolo_Tamanho", on_delete=models.CASCADE)
    valor_bolo = models.DecimalField('valor_bolo', max_digits = 6, decimal_places = 2)
	
class Cliente (models.Model):
    id_cliente = models.AutoField('id_cliente', primary_key=True)
    nome_cliente = models.CharField('nome_cliente', max_length=50)
    telefone_cliente = models.CharField('telefone', max_length=15)
    endereco_cliente = models.CharField('endereco', max_length=50)
    cpf_cliente = models.CharField('cpf',max_length=15)
    email = models.EmailField(max_length = 254)


class Pedido (models.Model):
    id_pedido = models.AutoField('id_pedido', primary_key=True)
    desconto = models.DecimalField('desconto', max_digits = 6, decimal_places = 2)
    data_hora_pedido = models.DateTimeField('data_pedido')
    data_hora_pedido_finalizado = models.DateTimeField('data_finalizado', null=True, blank=True)
    data_hora_pedido_retirado = models.DateTimeField('data_retirado' , null=True, blank=True)
    data_hora_pedido_retirado = models.DateTimeField('data_retirado' , null=True, blank=True)
    valor_total = models.DecimalField('valor_total', max_digits = 6, decimal_places = 2)
    bolo = models.ForeignKey(Bolo, verbose_name="Bolo", on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)



# Ver depois as relaçoes 1 pra 1 e 1 pra n e n pra n