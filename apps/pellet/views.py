from django.shortcuts import render

def index_(request):
    return render(request, 'pellet/index.html')