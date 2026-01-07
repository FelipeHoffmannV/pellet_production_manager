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

    data = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField()
    turno = models.CharField(max_length=2, choices=TURNOS)

    def __str__(self):
        return f"{self.data} - {self.turno} - {self.quantidade} un"