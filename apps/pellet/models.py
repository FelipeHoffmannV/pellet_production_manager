from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    
    def __str__(self):
        return self.username


class EntradaProducao(models.Model):
    TURNOS = [
        ('1', '1 - Turno'),
        ('2', '2 - Turno'),
        ('3', '3 - Turno'),
    ]

    MAQUINA = [('01', 'PEL - 01')]

    MOTIVOS_DE_PARADA = [
        ('Mecânica', 'Manutenção Mecânica'),
        ('Elétrica', 'Manutenção Elétrica'),
        ('Falta de material', 'Falta de Cavaco Seco'),
        ('Setup', 'Ajustes na Máquina'),
    ]

    maquina = models.CharField(max_length=2, choices=MAQUINA)
    turno = models.CharField(max_length=2, choices=TURNOS)
    data = models.DateField(auto_now_add=True)
    codigoCliente = models.CharField(max_length=100)
    lote = models.CharField(max_length=8)
    quantidadeProduzida = models.IntegerField()
    numeroDeFuncionarios = models.IntegerField()
    motivoParada = models.CharField(max_length=100, choices=MOTIVOS_DE_PARADA)
    observacoes = models.TextField()



    def __str__(self):
        return f"{self.data} - {self.turno} - {self.quantidadeProduzida} un"