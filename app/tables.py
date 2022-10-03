from django_tables2 import tables, TemplateColumn
from .models import Documento
from django_tables2.utils import A


class DocumentoTable(tables.Table):
    Comandos = TemplateColumn(template_name='documentos/toolbar.html')

    class Meta:
        model = Documento
        attrs = {'id': 'documentos'}
        template_name = "django_tables2/semantic.html"
        fields = ('numeracao', 'tipo_documento','veiculo','status_dodcumento','Comandos')
        