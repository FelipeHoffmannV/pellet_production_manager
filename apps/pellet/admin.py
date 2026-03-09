from django.contrib import admin
from .models import Cliente, Lote, Container, Pacote

# Permite editar Pacotes dentro da página do Container
class PacoteInline(admin.TabularInline):
    model = Pacote
    extra = 0  # Não exibe linhas vazias extras por padrão
    fields = ('numero_sequencial', 'quantidade_sacos', 'peso_saco_kg')

# Permite editar Containers dentro da página do Lote
class ContainerInline(admin.TabularInline):
    model = Container
    extra = 0
    show_change_link = True # Adiciona um link para editar o container individualmente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
    search_fields = ('nome', 'cnpj')

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('codigo_lote', 'cliente', 'quantidade_containers_prevista', 'status', 'total_sacos_estimado', 'data_criacao')
    list_filter = ('status', 'cliente')
    search_fields = ('codigo_lote', 'cliente__nome')
    inlines = [ContainerInline] # Onde a mágica acontece

    # Como total_sacos_estimado é uma @property, precisamos definir como short_description
    def total_sacos_estimado(self, obj):
        return obj.total_sacos_estimado
    total_sacos_estimado.short_description = 'Total Sacos (Est.)'

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'lote', 'data_carregamento')
    list_filter = ('lote__cliente',)
    inlines = [PacoteInline] # Permite ver os 22 pacotes aqui

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('numero_sequencial', 'container', 'quantidade_sacos', 'peso_saco_kg')
    list_filter = ('container__lote',)
