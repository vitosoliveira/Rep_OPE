from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from cpf_field.models import CPFField
from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals  
from django.template.defaultfilters import slugify 

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)


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
    id_tamanho = models.AutoField('id_bolo', primary_key = True)
    sem_glutem = models.IntegerField('glutem')
    sem_lactose = models.IntegerField('lactose')
    bolo_recheio = models.ForeignKey(Recheio, verbose_name="Bolo_Recheio", on_delete = models.CASCADE)
    bolo_massa = models.ForeignKey(Massa, verbose_name="Boloc_Massa", on_delete=models.CASCADE)
    bolo_topping = models.ForeignKey(Topping, verbose_name="Bolo_Topping", on_delete=models.CASCADE)
    bolo_cobertura = models.ForeignKey(Cobertura, verbose_name="Bolo_cobertura", on_delete=models.CASCADE)
    bolo_tamanho = models.ForeignKey(Tamanho, verbose_name="Bolo_Tamanho", on_delete=models.CASCADE)
    valor_bolo = models.DecimalField('valor_bolo', max_digits = 6, decimal_places = 2)

class ClienteManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None,  **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)

    def create_superuser(self, email, password=None,  **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super precisa ser true')
        

        return self._create_user(email,password, **extra_fields)

        
class Cliente (AbstractUser):
    email = models.EmailField('email',unique=True, max_length = 254)
    telefone = models.CharField('telefone', max_length=15)
    endereco = models.CharField('endereco', max_length=50)
    cpf = CPFField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf']

    def __str__(self):
        return self.email
    
    objects = ClienteManager()
    


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