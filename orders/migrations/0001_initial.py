# Generated by Django 3.2.1 on 2021-06-17 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Criado'), ('paid', 'Pago'), ('shipped', 'Enviado'), ('refunded', 'Devolvido')], default='created', max_length=120)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='carts.cart')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
