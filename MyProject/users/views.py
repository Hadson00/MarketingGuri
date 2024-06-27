from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user_temp = User.objects.get(email= email)
            user = authenticate(username=user_temp, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar!')
            
            
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('home')