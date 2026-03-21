from django.shortcuts import render, redirect


# Create your views here.
def login_(request):
    return render(request, 'users/login.html')