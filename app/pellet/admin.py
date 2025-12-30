from django.contrib import admin
from .models import Usuarios

# Register your models here.
admin.site.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    