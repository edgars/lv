# Generated by Django 4.1.1 on 2022-10-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_veiculo_marca_alter_veiculo_modelo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='valor_compra',
            field=models.FloatField(default='0', help_text='Valor pago pelo veículo', verbose_name='Valor de Compra'),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='valor_reparo',
            field=models.FloatField(default='0', help_text='Qual o valor pago pelo reparo', verbose_name='Valor de Reparo'),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='valor_venda',
            field=models.FloatField(default='0', help_text='Valor de Venda', verbose_name='Valor de Venda'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='documento_cliente',
            field=models.CharField(default='000000000000', help_text='Use apenas números', max_length=20, unique=True, verbose_name='CNPJ ou CPF'),
        ),
    ]
