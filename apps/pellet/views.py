from django.shortcuts import render

def home_global(request):
    return render(request, 'home_global.html')

def login_user(request):
    return render(request, 'user/login_user.html')

def login_admin(request):
    return render(request, 'admin/login_admin.html')