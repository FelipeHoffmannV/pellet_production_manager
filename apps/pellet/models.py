from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome

class Lote(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('PLANEJADO', 'Planejado'),
        ('PRODUZINDO', 'Em Produção'),
        ('FINALIZADO', 'Finalizado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='lotes')
    codigo_lote = models.CharField(max_length=50, unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    quantidade_containers_prevista = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANEJADO')

    def __str__(self):
        return f"Lote {self.codigo_lote} - {self.cliente.nome}"

    @property
    def total_sacos_estimado(self):
        # 1 container = 22 pacotes * 84 sacos
        return self.quantidade_containers_prevista * 22 * 84

class Container(models.Model):
    id = models.AutoField(primary_key=True)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='containers')
    identificador = models.CharField(max_length=100) # Ex: Sigla do container físico
    data_carregamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Container {self.identificador} (Lote {self.lote.codigo_lote})"

class Pacote(models.Model):
    id = models.AutoField(primary_key=True)
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='pacotes')
    numero_sequencial = models.PositiveIntegerField()
    quantidade_sacos = models.PositiveIntegerField(default=84) # 84 sacos por pacote
    peso_saco_kg = models.DecimalField(max_digits=5, decimal_places=2, default=15.0)

    def __str__(self):
        return f"Pacote {self.numero_sequencial} - {self.container.identificador}"
    

