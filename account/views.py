from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

# Create your views here.

def login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            django_login(request, user)
            if not user:
                pass
            else:
                return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

def register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse_lazy('login'))
    context = {
        'form' : form
    } 
    return render(request, 'register.html', context)


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login'))