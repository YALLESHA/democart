from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form})

from django.contrib.auth import authenticate, login

def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html')

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to DemoCart")