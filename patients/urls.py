from django.urls import path

from . import views

urlpatterns = [
    path("", views.appointmentIndex, name="appointmentIndex"),
    path("<int:patient_id>", views.patient, name="patient"),
    path("addNotes/<int:patient_id>", views.addNotes, name="addNotes"),
    path("addPatient", views.addPatient, name="addPatient"),
    path("removePatient/<int:patient_id>", views.removePatient, name="removePatient")
]
