from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from product.models import Category


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Username or Password')
    return render(request, 'fontend/pages/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')