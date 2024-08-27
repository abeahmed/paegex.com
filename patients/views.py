from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from appointments.models import Patient, Appointment
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginPage')
def appointmentIndex(request):
    user = request.user
    return render(request, "patients/appointmentIndex.html", {
        "appointments": Appointment.objects.filter(patient__user = user),
        "patients": Patient.objects.filter(user = user)
    })


@login_required(login_url='loginPage')
def patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return render(request, "patients/patient.html", {
        "patient": patient
        
    })  

@login_required(login_url='loginPage')   
def addNotes(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    if request.method == "POST":
        patient.notes = str(request.POST.get("patientNotes"))
    patient.save()
    return HttpResponseRedirect(reverse("patient", args=(patient.id,)))

@login_required(login_url='loginPage')
def addPatient(request):
    user = request.user
    if request.method == "POST":
        patientName = request.POST["patientName"]
        newPatient = Patient.objects.create(name = patientName, user=user)
        return HttpResponseRedirect(reverse("appointmentIndex"))

@login_required(login_url='loginPage')
def removePatient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    patient.delete()
    return HttpResponseRedirect(reverse("appointmentIndex"))
