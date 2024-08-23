from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


# Create your views here.   
def home(request):
    return render(request, "users/home.html")
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('index')

    return render(request, "users/login_register.html", {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def registerUser(request):  
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user=authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('index')


    context = {'form': form, 'page': page}
    return render(request, 'users/login_register.html', context)