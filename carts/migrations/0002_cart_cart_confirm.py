# Generated by Django 3.2.1 on 2021-06-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_confirm',
            field=models.BooleanField(default=False),
        ),
    ]