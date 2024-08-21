from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),
    path("", views.home, name="home")
]