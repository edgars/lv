from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Documento
from .tables import DocumentoTable
# Create your views here.

@login_required
def custom(request, pk):
    return render(request, "teste.html", {
        
    }) 


@login_required
def document_list_view(request):
    table = DocumentoTable(Documento.objects.all())

    return render(request, "documentos/list.html", {
        "table": table
    })      

@login_required
class DocumentoListView(ListView):
    model = Documento
    template_name = 'documentos/list.html'    