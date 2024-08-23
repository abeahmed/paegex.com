from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Appointment, Patient
# Create your views here.

@login_required(login_url='loginPage')
def index(request):
    user = request.user
    return render(request, "appointments/index.html", {
        "appointments": Appointment.objects.filter(patient__user=user),
        "patients": Patient.objects.filter(user=user),
    })

@login_required(login_url='loginPage')
def appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    return render(request, "appointments/appointment.html", {
        "appointment": appointment,
    })

@login_required(login_url='loginPage')
def addAppointment(request):
    if  request.method == "POST":
        patientName = Patient.objects.get(pk=int(request.POST["patient"]))
        departmentName = request.POST["department"]
        dateValue = request.POST["date"]
        newAppointment = Appointment.objects.create(patient=patientName, department=departmentName, date=dateValue)
        newAppointment.save()
        return HttpResponseRedirect(reverse("appointment", args=(newAppointment.id,)))