# Generated by Django 4.1.1 on 2022-10-03 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_veiculo_valor_compra_veiculo_valor_reparo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Titulo/nome do documento', max_length=50, verbose_name='Titulo')),
            ],
        ),
    ]
