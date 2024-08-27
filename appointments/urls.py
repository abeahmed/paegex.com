from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("<int:appointment_id>", views.appointment, name="appointment"),
    path("addAppointment", views.addAppointment, name="addAppointment"),
    path("removeAppointment", views.removeAppointment, name="removeAppointment")
    
]
