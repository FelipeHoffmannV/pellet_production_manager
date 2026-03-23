from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import userPellet

@admin.register(userPellet)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
# Register your models here.
