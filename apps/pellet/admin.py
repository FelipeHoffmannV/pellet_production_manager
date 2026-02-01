import io
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import admin
from .models import Usuario, EntradaProducao

# Função utilitária para converter HTML em PDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Action para o Admin
@admin.action(description="Gerar Relatório PDF")
def exportar_para_pdf(modeladmin, request, queryset):
    data = {
        'producoes': queryset,
    }
    pdf = render_to_pdf('relatorio_producao.html', data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "relatorio_producao.pdf"
        content = f"inline; filename={filename}"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Erro ao gerar PDF", status=400)

@admin.register(EntradaProducao)
class EntradaProducaoAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'turno', 'data', 'codigoCliente', 'lote', 'quantidadeProduzida', 'tempoParado', 'tempoProduzido')
    actions = [exportar_para_pdf]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
