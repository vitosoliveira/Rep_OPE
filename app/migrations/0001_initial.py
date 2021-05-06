# Generated by Django 3.2.1 on 2021-05-06 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolo',
            fields=[
                ('id_tamanho', models.AutoField(primary_key=True, serialize=False, verbose_name='id_bolo')),
                ('sem_glutem', models.IntegerField(verbose_name='glutem')),
                ('sem_lactose', models.IntegerField(verbose_name='lactose')),
                ('valor_bolo', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_bolo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='id_cliente')),
                ('nome_cliente', models.CharField(max_length=50, verbose_name='nome_cliente')),
                ('telefone_cliente', models.CharField(max_length=15, verbose_name='telefone')),
                ('endereco_cliente', models.CharField(max_length=50, verbose_name='endereco')),
                ('cpf_cliente', models.CharField(max_length=15, unique=True, verbose_name='cpf')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('senha', models.CharField(max_length=20, verbose_name='senha')),
            ],
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id_cobertura', models.AutoField(primary_key=True, serialize=False, verbose_name='cobertura_id')),
                ('nome_cobertura', models.CharField(max_length=50, verbose_name='nome_cobertura')),
                ('descricao_cobertura', models.CharField(max_length=250, verbose_name='descricao_cobertura')),
                ('sem_glutem', models.IntegerField(verbose_name='glutem')),
                ('sem_lactose', models.IntegerField(verbose_name='lactose')),
                ('valor_cobertura', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_cobertura')),
            ],
        ),
        migrations.CreateModel(
            name='Massa',
            fields=[
                ('id_massa', models.AutoField(primary_key=True, serialize=False, verbose_name='id_massa')),
                ('nome_massa', models.CharField(max_length=50, verbose_name='nome_massa')),
                ('descricao_massa', models.CharField(max_length=250, verbose_name='descricao')),
                ('sem_glutem', models.IntegerField(verbose_name='glutem')),
                ('sem_lactose', models.IntegerField(verbose_name='lactose')),
                ('valor_massa', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_massa')),
            ],
        ),
        migrations.CreateModel(
            name='Recheio',
            fields=[
                ('id_recheio', models.AutoField(primary_key=True, serialize=False, verbose_name='id_recheio')),
                ('nome_recheio', models.CharField(max_length=50, verbose_name='nome_recheio')),
                ('descricao_recheio', models.CharField(max_length=250, verbose_name='descricao_recheio')),
                ('sem_glutem', models.IntegerField(verbose_name='glutem')),
                ('sem_lactose', models.IntegerField(verbose_name='lactose')),
                ('valor_recheio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_recheio')),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id_tamanho', models.AutoField(primary_key=True, serialize=False, verbose_name='Tamanho')),
                ('nome_tamanho', models.CharField(max_length=50, verbose_name='nome_tamanho')),
                ('valor_tamanho', models.FloatField(max_length=20, verbose_name='valor_tamanho')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id_topping', models.AutoField(primary_key=True, serialize=False, verbose_name='íd_topping')),
                ('nome_topping', models.CharField(max_length=50, verbose_name='nome_topping')),
                ('descricao_topping', models.CharField(max_length=250, verbose_name='descricao_topping')),
                ('valor_topping', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_topping')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False, verbose_name='id_pedido')),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='desconto')),
                ('data_hora_pedido', models.DateTimeField(verbose_name='data_pedido')),
                ('data_hora_pedido_finalizado', models.DateTimeField(blank=True, null=True, verbose_name='data_finalizado')),
                ('data_hora_pedido_retirado', models.DateTimeField(blank=True, null=True, verbose_name='data_retirado')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor_total')),
                ('bolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bolo', verbose_name='Bolo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_cobertura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cobertura', verbose_name='Bolo_cobertura'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_massa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.massa', verbose_name='Boloc_Massa'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_recheio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recheio', verbose_name='Bolo_Recheio'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tamanho', verbose_name='Bolo_Tamanho'),
        ),
        migrations.AddField(
            model_name='bolo',
            name='bolo_topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topping', verbose_name='Bolo_Topping'),
        ),
    ]