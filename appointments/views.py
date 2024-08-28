from django.core.checks import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Appointment, Department, Patient
# Create your views here.

@login_required(login_url='loginPage')
def index(request):
    user = request.user
    return render(request, "appointments/index.html", {
        "appointments": Appointment.objects.filter(patient__user=user),
        "patients": Patient.objects.filter(user=user),
        "departments": Department.objects.filter(user=user)
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
        departmentName = Department.objects.get(pk=int(request.POST["department"]))
        dateValue = request.POST["date"]
        newAppointment = Appointment.objects.create(patient=patientName, department=departmentName, date=dateValue)
        newAppointment.save()
        return HttpResponseRedirect(reverse("appointment", args=(newAppointment.id,)))

@login_required(login_url='loginPage')
def removeAppointment(request):
    if request.method == "POST":
        selectedAppointment = Appointment.objects.get(pk=int(request.POST["appointmentComplete"]))
        selectedAppointment.delete()
        return HttpResponseRedirect(reverse("index"))

@login_required(login_url='loginPage')
def departments(request):
    user=request.user
    return render(request, "appointments/departments.html", {
        "departments": Department.objects.filter(user=user)
    })

@login_required(login_url='loginPage')
def addDepartment(request):
    user=request.user
    if request.method == "POST":
        departmentName = request.POST["departmentName"]
        nameCount = Department.objects.filter(user=user, name = departmentName).count()
        if nameCount > 0:
            messages.error(request, "This department has already been added")
            return HttpResponseRedirect(reverse("departments"))
        else:
            newDepartment = Department.objects.create(name = departmentName, user =  user)
            newDepartment.save()
            return HttpResponseRedirect(reverse("departments"))

@login_required(login_url='loginPage')
def removeDepartment(request, department_id):
        department = Department.objects.get(pk=department_id)
        department.delete()
        return HttpResponseRedirect(reverse("departments"))
