from django.contrib import *
from django import forms

# Register your models here.

from .models import Cliente
from .models import Veiculo
from .models import Marca
from .models import Modelo
from .models import TipoDocumento
from .models import Documento


class DocumentoInline(admin.TabularInline):
    model = Documento

class VeiculoInline(admin.TabularInline):
    model = Veiculo    


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo','responsavel', "valor_compra", "valor_venda")
    search_fields = ('placa', 'marca', 'modelo','responsavel')
    inlines = [DocumentoInline]




# admin.site.register(Veiculo)
admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Modelo)  
admin.site.register(TipoDocumento)  
admin.site.register(Documento)  