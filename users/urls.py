from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginUser, name="loginPage"),
    path('logout/', views.logoutUser, name="logoutPage"),
    path('register/', views.registerUser, name="register"),
    path("", views.home, name="home")
]