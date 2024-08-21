from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Appointment, Patient
# Create your views here.
def loginPage (request):
    return render(request, 'appointments/login_register.html')

def index(request):
    return render(request, "appointments/index.html", {
        "appointments": Appointment.objects.all(),
        "patients": Patient.objects.all(),
    })

def appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    return render(request, "appointments/appointment.html", {
        "appointment": appointment,
    })

def addAppointment(request):
    if  request.method == "POST":
        patientName = Patient.objects.get(pk=int(request.POST["patient"]))
        departmentName = request.POST["department"]
        dateValue = request.POST["date"]
        newAppointment = Appointment.objects.create(patient=patientName, department=departmentName, date=dateValue)
        newAppointment.save()
        return HttpResponseRedirect(reverse("appointment", args=(newAppointment.id,)))