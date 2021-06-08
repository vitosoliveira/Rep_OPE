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
    PRODUTO_CHOICES = (
        ("Massa", "Massa"),
        ("Cobertura", "Cobertura"),
        ("Recheio", "Recheio"),
        ("Tamanho", "Tamanho"),
        ("Topping", "Topping")        
    )
    
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    estoque = models.IntegerField('Estoque')
    tipo = models.CharField(max_length=9, choices=PRODUTO_CHOICES, blank=False, null=False)
    imagem = StdImageField('Imagem', upload_to='produtos',  blank=True, variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)

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
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)


# Ver depois as relaçoes 1 pra 1 e 1 pra n e n pra n