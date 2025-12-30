from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.IntegerField(max_length=8)

    def __str__(self):
        return Usuarios.nome
