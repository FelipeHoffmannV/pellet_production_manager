from django.contrib import admin
from .models import Usuario, EntradaProducao

# Register your models here.
admin.site.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

admin.site.register(EntradaProducao)
class EntradaProducaoAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'turno', 'data', 'codigoCliente', 'lote', 'quantidadeProduzida', 'numeroDeFuncionarios', 'motivoParada', 'observacoes')