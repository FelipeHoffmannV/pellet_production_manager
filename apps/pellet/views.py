from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, EntradaProducaoForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('producao')
            else:
                form.add_error(None, 'errado')
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required(login_url='')
def producao(request):
    if request.method == 'POST':
        form = EntradaProducaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producao')
    else:
        form = EntradaProducaoForm()

    return render(request, 'entradaProducao.html' , {'form': form})