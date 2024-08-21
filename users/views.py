from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "users/home.html")
def loginPage(request):
    return render(request, "users/login_register.html")

