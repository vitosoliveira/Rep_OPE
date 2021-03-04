from django.db import models



class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50 ,null=False, blank=False)

class Massa (models.Model):
	id_massa = models.AutoField(primary_key = True)
	nome_massa = models.CharField(max_length = 50 ,null=False, blank=False)
	descricao_massa = models.CharField(max_length = 250 ,null=False, blank=False)

class Recheio (models.Model):
  	id_recheio = models.AutoField(primary_key = True)
	nome_recheio = models.CharField(max_length = 50 ,null=False, blank=False)
	descricao_recheio = models.CharField(max_length = 250 ,null=False, blank=False)


class Cobertura (models.Model):
	id_cobertura = models.AutoField(primary_key = True)
	nome_cobertura = models.CharField(max_length = 50 ,null=False, blank=False)
	descricao_cobertura = models.CharField(max_length = 250 ,null=False, blank=False)

class Topping (models.Model):
	id_topping = models.AutoField(primary_key = True)
	nome_topping = models.CharField(max_length = 50 ,null=False, blank=False)
	descricao_descricao = models.CharField(max_length = 250 ,null=False, blank=False)
	valor_topping = models.FloatField(max_length = 20 ,null=False, blank=False)

class Tamanho_De_Bolo (models.Model):
	id_tamanho_bolo = models.AutoField(primary_key = True)
	nome_tamanho_bolo = models.CharField(max_length = 50 ,null=False, blank=False)
	valor_tamanho_bolo = models.FloatField(max_length = 20 ,null=False, blank=False)

class Bolo (models.Model):
	bolo_recheio = models.ForeignKey('Recheio', on_delete = models.CASCADE)
	bolo_massa = models.ForeignKey("Massa", on_delete=models.CASCADE)
	bolo_topping = models.ForeignKey("Topping", on_delete=models.CASCADE)
	