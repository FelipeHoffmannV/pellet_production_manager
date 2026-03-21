from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Usamos o UserAdmin pronto do Django para herdar todas 
# as funcionalidades de segurança e layout do Admin original
@admin.register(User)
class MyUserAdmin(UserAdmin):
    # Aqui você define quais campos aparecem na lista do Admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
# Register your models here.
