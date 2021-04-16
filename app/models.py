from django.db import models

# class Massa (models.Model):
#     id_massa = models.AutoField(primary_key = True)
#     nome_massa = models.CharField(max_length = 50)
#     descricao_massa = models.CharField(max_length = 250)

# class Recheio (models.Model):
#     id_recheio = models.AutoField(primary_key = True)
#     nome_recheio = models.CharField(max_length = 50)
#     descricao_recheio = models.CharField(max_length = 250)


# class Cobertura (models.Model):
#     id_cobertura = models.AutoField(primary_key = True)
#     nome_cobertura = models.CharField(max_length = 50)
#     descricao_cobertura = models.CharField(max_length = 250)

# class Topping (models.Model):
#     id_topping = models.AutoField(primary_key = True)
#     nome_topping = models.CharField(max_length = 50)
#     descricao_descricao = models.CharField(max_length = 250)
#     valor_topping = models.FloatField(max_length = 20)

# class Tamanho_De_Bolo (models.Model):
#     id_tamanho_bolo = models.AutoField(primary_key = True)
#     nome_tamanho_bolo = models.CharField(max_length = 50)
#     valor_tamanho_bolo = models.FloatField(max_length = 20)

# class Bolo (models.Model):
#     bolo_tipo = (
#         ("SG", "Sem Glúten"),
#         ("SL", "Sem Lactose"),
#         ("N", "Nenhuma das opções")
#     )
#     bolo_recheio = models.ForeignKey('Recheio', on_delete = models.CASCADE)
#     bolo_massa = models.ForeignKey("Massa", on_delete=models.CASCADE)
#     bolo_topping = models.ForeignKey("Topping", on_delete=models.CASCADE)
#     bolo_cobertura = models.ForeignKey("Cobertura", on_delete=models.CASCADE)
#     bolo_tamanho = (
#         ("P", "Pequeno"),
#         ("M", "Medio"),n
#         ("G", "Grande")
#         )
#     bolo_valor_total = models.FloatField(max_lenght = 8)
	
# class Cliente (models.Model):
#     id_cliente = models.AutoField(primary_key=True)
#     nome_cliente = models.CharField(max_length=50)
#     telefone_cliente = models.CharField(max_length=15)
#     endereco_cliente = models.CharField(max_length=50)
#     cpf_cliente = models.CharField(max_length=15)

# class Pedido (models.Model):
#     produtos = models.ManyToManyField(Bolo)
#     pedido_cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE) 
#     desconto_pedido = models.FloatField(max_lenght = 10)
#     data_hora_pedido = models.DateTimeField(default=timezone.now)
#     data_hora_finalizado =
#     data_hora_retirado = 
#     status = 

# Ver depois as relaçoes 1 pra 1 e 1 pra n e n pra n