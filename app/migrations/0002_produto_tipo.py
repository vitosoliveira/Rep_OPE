# Generated by Django 3.2 on 2021-05-21 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[(0, 'Massa'), (1, 'Cobertura'), (2, 'Recheio'), (3, 'Tamanho'), (4, 'Topping')], default=0, max_length=1),
        ),
    ]