from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from appointments.models import Patient, Appointment
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def appointmentIndex(request):
    return render(request, "patients/appointmentIndex.html", {
        "appointments": Appointment.objects.all(),
        "patients": Patient.objects.all()
    })


  
def patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return render(request, "patients/patient.html", {
        "patient": patient
        
    })  

    
def addNotes(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    if request.method == "POST":
        patient.notes = str(request.POST.get("patientNotes"))
    patient.save()
    return HttpResponseRedirect(reverse("patient", args=(patient.id,)))

def addPatient(request):
    if request.method == "POST":
        patientName = request.POST["patientName"]
        newPatient = Patient.objects.create(name = patientName)
        return HttpResponseRedirect(reverse("appointmentIndex"))