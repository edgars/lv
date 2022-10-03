from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey;
from auditlog.registry import auditlog
from django.conf.urls.static import static
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging


logger = logging.getLogger(__name__)

class Marca(models.Model):
    nome = models.CharField('Marca', max_length=50,blank=False, default="ENTRE COM A MARCA")   

    def save(self, *args, **kwargs):
      self.nome = self.nome.upper()
      super(Marca,self).save(*args,**kwargs)     
    def __str__(self):  return self.nome 

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=50,blank=False, default="ENTRE COM O NOME DO MODELO") 

    def __str__(self):  return self.modelo   
    
    def save(self, *args, **kwargs):
      self.modelo = self.modelo.upper()
      super(Modelo,self).save(*args,**kwargs) 

class TipoDocumento(models.Model):
    verbose_name_plural = "Tipos de Documentos"
    verbose_name = "Tipo de Documento"
    titulo = models.CharField('Titulo', max_length=50,blank=False, help_text="Titulo/nome do documento")   

    def __str__(self):  return self.titulo   
    
    def save(self, *args, **kwargs):
      self.titulo = self.titulo.upper()
      super(TipoDocumento,self).save(*args,**kwargs)       

        

  


class Cliente(models.Model): 
   TIPO_CLIENTE = (
   ('pf', 'Pessoa Física'),
   ('revenda','Revenda')
   )

   tipo_cliente = models.CharField('Tipo de Cliente:', max_length=30,choices=TIPO_CLIENTE, default='revenda')

   razao_social = models.CharField('Razão Social ou Nome',blank=False,max_length=250)
   documento_cliente = models.CharField('CNPJ ou CPF',blank=False, max_length=20,  help_text="Use apenas números", default='000000000000', unique=True)
   email = models.EmailField(max_length=254)

   nome_contato = models.CharField('Contato Principal',blank=True, max_length=100)
   celular_contato = models.CharField('WhatsApp',blank=True, max_length=30)
   cep = models.CharField('CEP', blank=True, max_length=10)
   banco = models.CharField('Banco',blank=True, max_length=10)
   banco_codigo = models.CharField('Código do Banco',blank=True, max_length=10)
   banco_agencia = models.CharField('Agência',blank=True, max_length=20)
   banco_conta = models.CharField('Conta Corrente',blank=True, max_length=20)
   pix_conta = models.CharField('Chave PIX',blank=True, max_length=20)


   responsavel = models.ForeignKey(User,verbose_name="Usuário Responsável", on_delete=models.CASCADE,
                     related_name='cliente_cadastrado', blank=False)
   data_cadastro = models.DateTimeField(default=timezone.now)

   def __str__(self):  return self.razao_social   

   def save(self, *args, **kwargs):
    self.razao_social = self.razao_social.upper()
    self.nome_contato = self.nome_contato.upper()
    self.banco = self.banco.upper()

    super(Cliente,self).save(*args,**kwargs)       



class Veiculo(models.Model): 

   list_display = ('placa', 'marca', 'modelo', 'responsavel')  

   antigo_dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='antigo_dono', verbose_name="Antigo Dono",blank=False)

   novo_dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='novo_dono', verbose_name="Novo Dono",blank=True,null=True)

   placa = models.CharField('Placa', max_length=30,blank=False, help_text="Entre com a placa, apenas letras e números, sem espaços", unique=True)

   marca = models.ForeignKey(Marca, on_delete=models.CASCADE, editable=False)
   modelo = GroupedForeignKey(Modelo, "marca", help_text="Selecione o modelo do veículo")

   



   valor_compra = models.FloatField('Valor de Compra',help_text="Valor pago pelo veículo", default='0', )

   valor_venda = models.FloatField('Valor de Venda',help_text="Valor de Venda",default='0', )

   valor_reparo = models.FloatField('Valor de Reparo', help_text="Qual o valor pago pelo reparo",default='0', )

   foto = models.ImageField(upload_to='fotos-carros', blank=True)
   



   responsavel = models.ForeignKey(User,verbose_name="Usuário Responsável", on_delete=models.CASCADE,
                     related_name='carro_cadastrado', blank=False, help_text="Usuário responsável pelo cadastro")
   data_cadastro = models.DateTimeField(default=timezone.now, editable=False)

   def __str__(self):  return self.placa

   def save(self, *args, **kwargs):
    self.placa = self.placa.upper()
    self.marca = self.modelo.marca

    super(Veiculo,self).save(*args,**kwargs) 

class Documento(models.Model):  

   STATUS_DOCUMENTO = (
   ('novo', 'Novo'),
   ('processando','Processando'),
   ('atraso', 'Em atraso'),
   ('despachante', 'Com Despachante'),
   ('pronto', 'Pronto'),
   )  

   dono_documento = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Dono do Documento",blank=False)

   veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veículo Relacionado",related_name='veiculo', blank=False, default=1 )

   tipo_documento = models.ForeignKey(TipoDocumento,verbose_name="Tipo de Documento", on_delete=models.CASCADE,
                     related_name='tipo_documento', blank=False)
   status_dodcumento = models.CharField('Status do Documento', max_length=30,choices=STATUS_DOCUMENTO, default='novo') 
   numeracao =   models.CharField('Numeracao', max_length=30,help_text="Entre com a numeracao do documento") 
   media_docs = upload_to=str(settings.MEDIA_ROOT)+'documentos'
   anexo = models.FileField(upload_to='documentos',blank=True,) 

   def __str__(self):  return str(self.tipo_documento) + '  - Número: ' +  str(self.numeracao)

           


auditlog.register(Veiculo)
auditlog.register(Cliente)


# Events

@receiver(post_save, sender=Documento)
def save_profile(sender, instance, **kwargs):
  print('>>>>> status do documento: ' + instance.status_dodcumento )
  logger.info('status do documento: ' + instance.status_dodcumento )
  


